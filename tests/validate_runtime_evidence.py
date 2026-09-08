#!/usr/bin/env python3
"""Check archived response integrity and review references, never semantic truth."""
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]


def validate(manifest: Path) -> list[str]:
    errors = []
    root = manifest.parent.resolve()
    try:
        data = json.loads(manifest.read_text())
        if data.get('schema_version') != 1 or not data.get('limitations'):
            errors.append('schema version or limitations missing')
        texts = {}
        for name, digest in data['files'].items():
            path = (root / name).resolve()
            if not path.is_relative_to(root):
                errors.append('path outside evidence directory: ' + name)
                continue
            if not path.is_file():
                errors.append('missing file: ' + name)
                continue
            raw = path.read_bytes()
            if hashlib.sha256(raw).hexdigest() != digest:
                errors.append('hash mismatch: ' + name)
            texts[name] = raw.decode('utf-8')
        seen, inputs, outputs = set(), set(), set()
        if not data['turns']:
            errors.append('no recorded turns')
        for turn in data['turns']:
            key = (turn['arm'], turn['turn'])
            if key in seen:
                errors.append('duplicate arm/turn: ' + str(key))
            seen.add(key)
            inputs.add(turn['input'])
            outputs.add(turn['output'])
            for name in (turn['input'], turn['output']):
                if name not in texts:
                    errors.append('unavailable turn file: ' + name)
        reviewed = set()
        for review in data['reviews']:
            name = review['output']
            if name not in outputs:
                errors.append('review does not reference an output: ' + name)
            if not review['quote'] or review['quote'] not in texts.get(name, ''):
                errors.append('review quote not found: ' + name)
            if not review['finding'] or not review['source_inputs']:
                errors.append('review finding or source missing: ' + name)
            for source in review['source_inputs']:
                if source not in inputs or source not in texts:
                    errors.append('unknown review source: ' + source)
            reviewed.add(name)
        for name in outputs - reviewed:
            errors.append('output not reviewed: ' + name)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        errors.append('invalid evidence manifest: ' + str(exc))
    return errors


def main():
    paths = [Path(p) for p in sys.argv[1:]] or sorted(
        (ROOT / 'docs/evaluation/versioned').glob('*/manifest.json'))
    if not paths:
        print('EVIDENCE VALIDATION FAILED: no manifests')
        return 1
    failures = [(str(p), error) for p in paths for error in validate(p)]
    for path, error in failures:
        print(path + ': ' + error)
    print('EVIDENCE VALIDATION ' + ('FAILED' if failures else 'PASSED') +
          ': ' + str(len(paths)) + ' suites; integrity only, not semantic scoring')
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
