"""Validate an FDA monthly snapshot and stage it locally; never auto-publish.
Usage: python scripts/rebuild-purple.py FDA.csv 'September 2026' SOURCE_HTTPS_URL
A failed validation leaves the existing published data untouched.
"""
from pathlib import Path
import csv,json,hashlib,sys,datetime
from urllib.parse import urlparse
KEEP=['BLA Number','Proprietary Name','Proper Name','License Type','Strength','Dosage Form','Route of Administration','Product Presentation','Marketing Status','Licensure','Approval Date','Inter. Approval Date','Ref. Product Proper Name','Ref. Product Proprietary Name','Product Number']

def parse_snapshot(raw,month,url):
    parsed=urlparse(url)
    if parsed.hostname!='www.accessdata.fda.gov' or parsed.scheme!='https' or parsed.username or parsed.password:
        raise ValueError('Use the original FDA HTTPS download URL.')
    try: datetime.datetime.strptime(month,'%B %Y')
    except ValueError: raise ValueError('Month must be a full month and year.')
    rows=list(csv.reader(raw.decode('utf-8-sig').splitlines()))
    if not rows or not rows[0] or month.lower() not in rows[0][0].lower():raise ValueError('Month does not match FDA report title.')
    indices=[i for i,row in enumerate(rows) if row[:2]==['N/R/U','Applicant']]
    if len(indices)!=2:raise ValueError('Unexpected monthly report structure; review before importing.')
    header=rows[indices[-1]]
    if len(set(header))!=len(header) or not set(KEEP).issubset(header):raise ValueError('Missing or duplicate FDA columns; import rejected.')
    data=[];seen=set();identities={};duplicates=0
    for line,row in enumerate(rows[indices[-1]+1:],indices[-1]+2):
        d=dict(zip(header,row))
        if not d.get('License Type','').startswith('351(k)'):continue
        if len(row)!=len(header):raise ValueError(f'Row {line}: unexpected column count.')
        x={k:d[k].strip() for k in KEEP}
        if x['License Type'] not in ('351(k) Biosimilar','351(k) Interchangeable'):raise ValueError(f'Row {line}: unknown biosimilar designation.')
        for k in ['BLA Number','Product Number','Proprietary Name','Proper Name','Strength','Route of Administration','Product Presentation','Licensure','Ref. Product Proprietary Name']:
            if not x[k]:raise ValueError(f'Row {line}: missing {k}.')
        if not x['BLA Number'].isdigit() or not x['Product Number'].isdigit():raise ValueError(f'Row {line}: invalid BLA/product identifier.')
        for k in ['Approval Date','Inter. Approval Date']:
            if x[k]:
                try: datetime.datetime.strptime(x[k],'%B %d, %Y')
                except ValueError: raise ValueError(f'Row {line}: invalid {k}.')
        key=json.dumps(x,sort_keys=True)
        identity=(x['BLA Number'],x['Product Number'])
        if identity in identities and identities[identity]!=key:raise ValueError(f'Row {line}: conflicting records for BLA/product {identity}.')
        identities[identity]=key
        if key in seen:duplicates+=1;continue
        seen.add(key);data.append(x)
    if not data:raise ValueError('No biosimilar rows; import rejected.')
    return {'month':month,'checked':datetime.date.today().isoformat(),'source':url,'sha256':hashlib.sha256(raw).hexdigest(),'products':data},duplicates

def main(args):
    if len(args)!=3:raise SystemExit(__doc__)
    p,month,url=Path(args[0]),args[1],args[2]
    try: doc,duplicates=parse_snapshot(p.read_bytes(),month,url)
    except (ValueError,UnicodeError) as exc:raise SystemExit(str(exc))
    root=Path(__file__).resolve().parent.parent
    prior=json.loads((root/'docs/data/purple-book.json').read_text())
    report={'state':'REVIEW_REQUIRED_NOT_PUBLISHED','source':url,'sha256':doc['sha256'],'previousMonth':prior['month'],'newMonth':month,'previousPresentations':len(prior['products']),'newPresentations':len(doc['products']),'exactDuplicateRowsRemoved':duplicates,'reviewRequired':['Designation and reference changes','Marketing and licensure changes','Presentation/strength and date changes','Unexpected count changes','Clinical and deployment acceptance']}
    (root/'documentation/PURPLE_IMPORT_REVIEW.json').write_text(json.dumps(report,indent=2)+'\n')
    (root/'docs/data/purple-book.json').write_text(json.dumps(doc,indent=2))
    (root/'docs/assets/purple-data.js').write_text('window.ClinicalPurpleData='+json.dumps(doc)+';\n')
    print('Validated local snapshot staged:',len(doc['products']),'presentations. Review report required; no deployment performed.')
if __name__=='__main__':main(sys.argv[1:])
