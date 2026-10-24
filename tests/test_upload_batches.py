import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from upload_batches import make_batches
class UploadTests(unittest.TestCase):
 def test_complete_unique_and_bounded(self):
  paths=['docs/index.html','docs/assets/app.js']+[f'documentation/file{i}.md' for i in range(201)]+['.github/workflows/release-check.yml']
  batches=make_batches(paths)
  self.assertEqual(sorted(sum(batches.values(),[])),sorted(paths))
  self.assertTrue(all(len(x)<100 for x in batches.values()))
  self.assertEqual(batches['01_SITE'],['docs/assets/app.js','docs/index.html'])
 def test_reject_bad_inputs(self):
  for paths in [['docs/index.html']*2,['../secret','docs/index.html'],['README.md'],['docs/index.html']+[f'docs/{i}' for i in range(100)]]:
   with self.assertRaises(ValueError):make_batches(paths)
