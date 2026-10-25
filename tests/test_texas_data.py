import unittest,importlib.util,io,zipfile,tempfile,urllib.error,json
from pathlib import Path
spec=importlib.util.spec_from_file_location('vdp',Path(__file__).resolve().parents[1]/'scripts/fetch-texas-vdp.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class TexasData(unittest.TestCase):
 def test_text_is_not_schema_approval(self):self.assertFalse(m.validate_payload(b'ndc|value\n123|1','text')['schemaVerified'])
 def test_reject_errors(self):
  for b in [b'',b'<html>Forbidden</html>',b'AccessDenied',b'abc\x00def']:
   with self.assertRaises(ValueError):m.validate_payload(b,'text')
 def test_reject_html_type(self):
  with self.assertRaises(ValueError):m.validate_payload(b'error','text','text/html')
 def test_zip_requires_excel(self):
  b=io.BytesIO()
  with zipfile.ZipFile(b,'w') as z:z.writestr('readme.txt','test')
  with self.assertRaises(ValueError):m.validate_payload(b.getvalue(),'zip')
 def test_zip_traversal(self):
  b=io.BytesIO()
  with zipfile.ZipFile(b,'w') as z:z.writestr('../data.xlsx','test')
  with self.assertRaises(ValueError):m.validate_payload(b.getvalue(),'zip')
 def test_origin_failure_stops_remaining_requests(self):
  calls=[]
  def fail(f):calls.append(f);raise urllib.error.HTTPError(f['url'],403,'Forbidden',{},None)
  feeds=[{'id':str(i),'url':'https://www.txvendordrug.com/test','format':'text'} for i in range(2)]
  with tempfile.TemporaryDirectory() as d:
   r=m.run(d,feeds,fail);self.assertEqual(len(calls),1);self.assertEqual(r['records'][1]['status'],'NOT_ATTEMPTED_ORIGIN_ACCESS_FAILURE');self.assertFalse(r['publishesSiteData']);self.assertEqual(len(list(Path(d).iterdir())),1)
 def test_failed_refresh_preserves_old_file(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'last-good.txt';p.write_text('good')
   def fail(f):raise ValueError('bad')
   m.run(d,[{'id':'drug','url':'https://www.txvendordrug.com/test','format':'text'}],fail);self.assertEqual(p.read_text(),'good')
 def test_registry_has_nine_unique_official_sources(self):
  feeds=json.loads((m.ROOT/'documentation/texas-vdp-sources.json').read_text())['feeds'];self.assertEqual(len(feeds),9);self.assertEqual(len({x['id'] for x in feeds}),9);self.assertTrue(all(x['url'].startswith('https://www.txvendordrug.com/sites/default/files/docs/') for x in feeds))
