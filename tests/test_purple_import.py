import unittest,importlib.util,csv,io,json
from pathlib import Path
spec=importlib.util.spec_from_file_location('purple',Path(__file__).resolve().parents[1]/'scripts/rebuild-purple.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class PurpleImport(unittest.TestCase):
 def raw(self,changes=None,duplicate=False):
  x={'BLA Number':'761378','Product Number':'001','Proprietary Name':'Example','Proper Name':'example-abcd','License Type':'351(k) Biosimilar','Strength':'2MG','Dosage Form':'Injection','Route of Administration':'Intravitreal','Product Presentation':'Single-Dose Vial','Marketing Status':'Rx','Licensure':'Licensed','Approval Date':'June 28, 2024','Inter. Approval Date':'','Ref. Product Proper Name':'reference','Ref. Product Proprietary Name':'Reference'}
  x.update(changes or {});h=['N/R/U','Applicant']+m.KEEP;out=io.StringIO();w=csv.writer(out);w.writerow(['Purple Book September 2026']);w.writerow(h);w.writerow(h);row=['','Example']+[x[k] for k in m.KEEP];w.writerow(row)
  if duplicate:w.writerow(row)
  return out.getvalue().encode()
 def parse(self,b):return m.parse_snapshot(b,'September 2026','https://www.accessdata.fda.gov/example.csv')
 def test_valid_and_exact_duplicate(self):
  doc,n=self.parse(self.raw(duplicate=True));self.assertEqual(len(doc['products']),1);self.assertEqual(n,1);self.assertEqual(len(doc['sha256']),64)
 def test_unknown_designation(self):
  with self.assertRaises(ValueError):self.parse(self.raw({'License Type':'351(k) Unknown'}))
 def test_invalid_date(self):
  with self.assertRaises(ValueError):self.parse(self.raw({'Approval Date':'tomorrow'}))
 def test_missing_reference(self):
  with self.assertRaises(ValueError):self.parse(self.raw({'Ref. Product Proprietary Name':''}))
 def test_wrong_month(self):
  with self.assertRaises(ValueError):m.parse_snapshot(self.raw(),'October 2026','https://www.accessdata.fda.gov/example.csv')
 def test_wrong_host(self):
  with self.assertRaises(ValueError):m.parse_snapshot(self.raw(),'September 2026','https://example.com/example.csv')
 def test_conflict(self):
  b=self.raw();extra=self.raw({'License Type':'351(k) Interchangeable'}).decode().splitlines()[-1]
  with self.assertRaises(ValueError):self.parse(b+extra.encode()+b'\n')
