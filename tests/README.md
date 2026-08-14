# Protocol fixtures

The **33 deterministic fixtures** encode named Readback First protocol
invariants.
Each fixture contains a deliberately bad output and a compliant output. The
runner checks that the bad output triggers the expected failure code and the
good output does not.

Run:

```bash
python3 tests/validate_fixtures.py
python3 tests/validate_contract.py
```

The set covers:

- unauthorized compression and compact-view coverage loss;
- premature closure and clarification during open input;
- correction overwrite and silent contextual correction;
- candidate promotion and AI induction presented as user source;
- qualifier omission, invented intent, and unresolved-item disappearance;
- summary-only confirmation, confirmation-scope overreach, and confirmation-
  depth overreach;
- direct-answer authority bypass and overblocking a clear closed request;
- unverified artifact claims;
- version-coordinate, locator-scope, and session-lineage collapse;
- ingestion-fidelity and source-trace overclaim;
- source-to-synthesis trace gaps;
- invalid delta baselines.
- missing default readback and overblocked proceed-after-readback;
- required-gate bypass after a proceed request;
- interrupting corrections that leave dependent provisional output stale;
- low-impact ambiguity that is over-questioned and material ambiguity that is
  silently assumed;
- unnecessary presentation menus and session preferences that remove required
  coverage;
- overview-only confirmation substituted for material reception coverage.

## Evidence boundary

These fixtures validate the evaluator and the protocol invariants represented
by their JSON fields. They do **not** run a language model, install the Skill,
or prove that a model will follow the protocol in a real conversation.

`RBF-FIX-018` uses an externally declared meaning-unit inventory to verify that
a compact view did not drop a material unit. In contrast, legacy
`RBF-FIX-001` retains the original synthetic 1,000-item range as a regression
fixture; its generated range is not semantic-coverage proof.

Observed runtime behavior belongs in `evals/`, with the source prompt, runtime
and model metadata, raw output, repeated runs, rubric, and known failures kept
together.
