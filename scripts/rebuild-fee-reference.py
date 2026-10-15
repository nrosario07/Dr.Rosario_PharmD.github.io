"""Manually rebuild the reviewed annual Texas office-fee comparison subset.
Source changes stop the build for review. Does not publish or establish payer eligibility.
"""
from pathlib import Path
import csv,hashlib,io,json,urllib.request,zipfile
root=Path(__file__).resolve().parent.parent
bundle=json.loads((root/'docs/data/clinical-rules.json').read_text())
fees=[]
for ref,qp in [('R02','nonqp'),('R03','qp')]:
 source=next(x for x in bundle['provenance'] if x['id']==ref)
 data=urllib.request.urlopen(source['url'],timeout=30).read()
 if hashlib.sha256(data).hexdigest()!=source['sha256']:raise SystemExit('Source changed; review required: '+ref)
 with zipfile.ZipFile(io.BytesIO(data)) as z:
  for row in csv.reader(z.read('PFTX26A.TXT').decode().splitlines()):
   if len(row)>7 and row[3] in ['99211','99202','99203','99204','99205','99212','99213','99214','99215'] and not row[4].strip():fees.append(dict(year=row[0],locality=row[2],code=row[3],nonfacility=float(row[5]),facility=float(row[6]),qp=qp))
assert len(fees)==144
(root/'docs/assets/fee-reference.js').write_text('window.ClinicalFeeReference='+json.dumps(fees)+';\n')
print('Reviewed annual subset rebuilt; rerun tests, inspect changes and update release manifest before packaging.')
