import importlib.util
import pathlib
import unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
def load(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/f'{name}.py')
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
approve=load('review-source-baseline').approve
summary=load('source-review-summary').summary
class GovernanceTests(unittest.TestCase):
    def report(self,status='CONTENT_CHANGED_REVIEW'):
        return {'checked':'2026-10-21T00:00:00Z','sources':[{'url':'https://example.org/guideline','status':status,'sha256':'a'*64,'finalURL':'https://example.org/guideline'}]}
    def test_selected_approval_preserves_other_records(self):
        old={'https://example.org/older':{'sha256':'b'*64}}
        result=approve(self.report(),old,['https://example.org/guideline'],'Reviewer','Checked effective date; no rule edits')
        self.assertEqual(result['https://example.org/older'],old['https://example.org/older'])
        self.assertNotIn('https://example.org/guideline',old)
        self.assertEqual(result['https://example.org/guideline']['reviewer'],'Reviewer')
    def test_unavailable_cannot_be_baselined(self):
        with self.assertRaises(ValueError):approve(self.report('UNAVAILABLE_REVIEW'),{},['https://example.org/guideline'],'Reviewer','Review')
    def test_missing_rationale_rejected(self):
        with self.assertRaises(ValueError):approve(self.report(),{},['https://example.org/guideline'],'Reviewer',' ')
    def test_bad_hash_rejected(self):
        r=self.report();r['sources'][0]['sha256']='short'
        with self.assertRaises(ValueError):approve(r,{},['https://example.org/guideline'],'Reviewer','Review')
    def test_summary_distinguishes_hash_change_from_clinical_decision(self):
        text=summary(self.report())
        self.assertIn('CONTENT_CHANGED_REVIEW',text);self.assertIn('may be cosmetic',text);self.assertIn('proposed or withdrawn',text)
if __name__=='__main__':unittest.main()
