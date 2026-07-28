# Behavior fixtures

These deterministic fixtures preserve the RED baseline that motivated
Readback First. Each case contains a known-bad output and a compliant output.

Run:

```bash
python3 tests/validate_fixtures.py
```

The public set covers:

- unauthorized compression;
- premature closure during continuing input;
- correction overwrite;
- candidate promotion;
- qualifier omission;
- invented intent;
- summary-only confirmation;
- direct-answer authority bypass;
- unresolved-item disappearance;
- confirmation-scope overreach;
- overblocking a clear closed request.

The fixtures validate protocol invariants. They are not a claim that every
model will produce the same wording.
