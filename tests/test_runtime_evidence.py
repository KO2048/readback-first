"""Tests for evidence integrity, not model semantics."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from validate_runtime_evidence import validate

class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'input.md').write_text('Source request')
        (self.root / 'output.md').write_text('Observed response')
        self.data = {'schema_version': 1, 'limitations': ['Shared host'],
            'files': {name: hashlib.sha256((self.root/name).read_bytes()).hexdigest()
                      for name in ['input.md', 'output.md']},
            'turns': [{'arm': 'skill', 'turn': 1, 'input': 'input.md', 'output': 'output.md'}],
            'reviews': [{'output': 'output.md', 'quote': 'Observed response',
                         'finding': 'reviewed', 'source_inputs': ['input.md']}]}
    def run_case(self):
        (self.root / 'manifest.json').write_text(json.dumps(self.data))
        return validate(self.root / 'manifest.json')
    def test_valid(self):
        self.assertEqual(self.run_case(), [])
    def test_changed_raw_response(self):
        (self.root / 'output.md').write_text('Changed response')
        self.assertTrue(self.run_case())
    def test_invented_review_quote(self):
        self.data['reviews'][0]['quote'] = 'never actually said'
        self.assertTrue(self.run_case())
    def test_missing_source(self):
        self.data['reviews'][0]['source_inputs'] = ['absent.md']
        self.assertTrue(self.run_case())
    def test_path_escape(self):
        self.data['files']['../private.md'] = '0' * 64
        self.assertTrue(self.run_case())
    def test_duplicate_turn(self):
        self.data['turns'].append(dict(self.data['turns'][0]))
        self.assertTrue(self.run_case())
    def test_unreviewed_output(self):
        self.data['reviews'] = []
        self.assertTrue(self.run_case())

if __name__ == '__main__':
    unittest.main()
