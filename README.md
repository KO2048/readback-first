# Readback First

**0.2.0 candidate — Separate source, reception, decision and authority**

Make the AI's working understanding inspectable before it responds or acts.
Preserve qualifiers, corrections and open items. Readback is neither factual
verification nor action authorization.

[中文](README.zh-CN.md) · [Protocol](PROTOCOL.md) · [This iteration](docs/releases/0.2.0.md) · [Version sequence](docs/release-sequence.md)

## What this version changes

- Separate source, reception, decision and action-authority axes.
- Retain correction links, coverage and unresolved items; confirm only the named target.

## Install this candidate

Install the repository-root Skill from branch `codex/release-v02-semantics`, then reload as required
by the host. Installing from default main will not select this candidate.
Installation alone does not establish mandatory every-turn activation.

## Evidence and status

**24 deterministic fixtures** and a contract consistency check are provided:

```bash
python3 tests/validate_contract.py
python3 tests/validate_fixtures.py
```

These checks do not run a model. Runtime behavior, loading and rendering evidence
remain pending. This is not a tagged stable release and does not replace global
rules. See the [evaluation matrix](tests/runtime-matrix.md).

[Complete examples](examples/before-after.md) · [Changelog](CHANGELOG.md) · Apache-2.0
