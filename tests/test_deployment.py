import importlib.util,hashlib,unittest
from pathlib import Path
s=importlib.util.spec_from_file_location('deployment',Path(__file__).resolve().parents[1]/'scripts/verify-deployment.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class DeploymentTests(unittest.TestCase):
 def test_exact_and_mixed_deployment(self):
  manifest={'version':'test','sha256':{'index.html':hashlib.sha256(b'new').hexdigest(),'assets/app.js':hashlib.sha256(b'new').hexdigest()}}
  result=m.check('https://example.org',manifest,lambda u:b'new' if u.endswith('index.html') else b'old')
  self.assertFalse(result['passed']);self.assertEqual([x['status'] for x in result['files']],['MATCH','MISMATCH'])
  self.assertTrue(m.check('https://example.org',manifest,lambda u:b'new')['passed'])
 def test_failure_and_path_rejection(self):
  def failed(url):raise TimeoutError('offline')
  result=m.check('https://example.org',{'version':'test','sha256':{'index.html':'x','../secret':'x'}},failed)
  self.assertEqual([x['status'] for x in result['files']],['UNREACHABLE','INVALID_PATH']);self.assertFalse(result['passed'])
