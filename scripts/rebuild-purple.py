"""Maintainer-reviewed monthly Purple Book snapshot rebuild; no auto-publish.
Usage: python scripts/rebuild-purple.py FDA.csv 'September 2026' SOURCE_HTTPS_URL
Review date/status/relationships and tests before committing; input is public FDA data only.
"""
from pathlib import Path
import csv,json,hashlib,sys,datetime
from urllib.parse import urlparse
if len(sys.argv)!=4: raise SystemExit(__doc__)
p,month,url=Path(sys.argv[1]),sys.argv[2],sys.argv[3]
if urlparse(url).hostname!='www.accessdata.fda.gov' or urlparse(url).scheme!='https':raise SystemExit('Use the original FDA download URL.')
b=p.read_bytes();rows=list(csv.reader(b.decode('utf-8-sig').splitlines()))
if month.lower() not in rows[0][0].lower():raise SystemExit('Month does not match FDA report title.')
indices=[i for i,row in enumerate(rows) if row[:2]==['N/R/U','Applicant']]
if len(indices)!=2:raise SystemExit('Unexpected monthly report structure; review before importing.')
keep=['BLA Number','Proprietary Name','Proper Name','License Type','Strength','Dosage Form','Route of Administration','Product Presentation','Marketing Status','Licensure','Approval Date','Inter. Approval Date','Ref. Product Proper Name','Ref. Product Proprietary Name','Product Number']
data=[];seen=set()
for row in rows[indices[-1]+1:]:
 d=dict(zip(rows[indices[-1]],row))
 if not d.get('License Type','').startswith('351(k)'):continue
 x={k:d.get(k,'') for k in keep};key=json.dumps(x,sort_keys=True)
 if key not in seen:data.append(x);seen.add(key)
if not data:raise SystemExit('No biosimilar rows; import rejected.')
r=Path(__file__).resolve().parent.parent;doc={'month':month,'checked':datetime.date.today().isoformat(),'source':url,'sha256':hashlib.sha256(b).hexdigest(),'products':data}
(r/'docs/data/purple-book.json').write_text(json.dumps(doc,indent=2));(r/'docs/assets/purple-data.js').write_text('window.ClinicalPurpleData='+json.dumps(doc)+';\n')
print('Review-required snapshot generated:',len(data),'presentations. No deployment performed.')
