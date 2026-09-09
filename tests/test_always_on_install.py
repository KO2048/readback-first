import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('installer', ROOT/'scripts/enable_always_on.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class Installation(unittest.TestCase):
    def test_preserves_rules_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as d:
            rules = Path(d)/'AGENTS.md'
            rules.write_text('原有治理\n')
            m.enable(ROOT, rules)
            first = rules.read_bytes()
            self.assertTrue(first.decode().startswith('原有治理\n'))
            self.assertEqual(m.enable(ROOT, rules), 'unchanged')
            self.assertEqual(first, rules.read_bytes())
            self.assertEqual(next(Path(d).glob('*backup*')).read_text(), '原有治理\n')
    def test_missing_dependency_does_not_write(self):
        with tempfile.TemporaryDirectory() as d:
            rules = Path(d)/'AGENTS.md'
            with self.assertRaises(ValueError): m.enable(d, rules)
            self.assertFalse(rules.exists())
    def test_malformed_markers_preserved(self):
        with tempfile.TemporaryDirectory() as d:
            rules = Path(d)/'AGENTS.md'
            rules.write_text(m.START)
            with self.assertRaises(ValueError): m.enable(ROOT, rules)
            self.assertEqual(rules.read_text(), m.START)
    def test_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            target = Path(d)/'source'; target.write_text('preserve')
            rules = Path(d)/'AGENTS.md'; rules.symlink_to(target)
            with self.assertRaises(ValueError): m.enable(ROOT, rules)
            self.assertEqual(target.read_text(), 'preserve')

if __name__ == '__main__': unittest.main()
