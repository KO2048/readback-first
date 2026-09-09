# Readback First

**0.10.2 — Batched delivery and commit traceability**

Make the AI's working understanding inspectable before it responds or acts.
Preserve qualifiers, corrections and open items. Readback is neither factual
verification nor action authorization.

[中文](README.zh-CN.md) · [Protocol](PROTOCOL.md) · [This iteration](docs/releases/0.10.2.md) · [Version sequence](docs/release-sequence.md)

## What this version changes

- Add the [delivery ledger](docs/delivery-ledger.md): issue, implementation commit, merge commit, PR, version and remaining acceptance.
- Document Chinese-first commit conventions and distinguish behavior, examples, tests and documentation.
- This is a documentation patch; the behavioral contract remains v0.10.0.

## Read back, then answer

**User:** “Can a Skill own readback while keeping it mandatory every turn? Do not edit yet.”

Readback: You want the detailed protocol in a Skill, with mandatory every-turn
application. This turn is discussion only.

Yes. The host entry can require it while the Skill owns reception and expression.
I recommend comparing real replies before replacing old rules, so corrections,
source coverage and useful continuation survive the move.

## Install the latest version

The default `main` branch contains **v0.10.2**. Ask your agent:

> Install the Skill at https://github.com/KO2048/readback-first from the repository
> root on main, named readback-first. If already installed, preserve local changes
> and update it to the latest main version.

For a new Codex installation, the manual equivalent is:

```bash
git clone --branch main --depth 1 https://github.com/KO2048/readback-first.git ~/.codex/skills/readback-first
```

Do not run the clone over an existing directory. For a Git-based installation,
review local changes before updating with `git pull --ff-only origin main` from
that installation; other installations can be updated by the agent/installer.
Reload the Skill or start a new session as your host requires. Check `release.json`
for version `0.10.2`; installing this Skill does not itself update host rules.

**Complete installation includes the persistent entry.** After installing or
updating the package, run (Codex):

```bash
python3 ~/.codex/skills/readback-first/scripts/enable_always_on.py --skill-dir ~/.codex/skills/readback-first --rules-file ~/.codex/AGENTS.md
```

This preserves existing rules, backs up changes, and is safe to run repeatedly.
For WorkBuddy or another host, pass its installed Skill directory and its
**verified always-loaded instruction file**; do not guess a host path. If that
host only offers a rules UI, paste the adapter from [always-on.md](docs/always-on.md)
there. Package copying alone is incomplete every-turn setup. Reload/start a fresh
session afterwards. Configuration success does not attest model compliance or UI
visibility; existing governance remains in place.

## Evidence and status

**39 deterministic fixtures** and a contract consistency check are provided:

```bash
python3 tests/validate_contract.py
python3 tests/validate_fixtures.py
```

These checks do not run a model. The [source-specificity runtime report](docs/evaluation/reception-continuation/review.md) archives three three-turn baseline conversations, ten baseline micro samples, five candidate micro samples and a three-turn candidate replay; broader runtime behavior, loading and rendering remain pending. This is a published 0.x protocol/Skill release, not a claim of
cross-model reliability. It does not silently replace global rules. See the [evaluation matrix](tests/runtime-matrix.md).

[Complete examples](examples/before-after.md) · [Changelog](CHANGELOG.md) · Apache-2.0

## Semantic views / 语义视图

```mermaid
flowchart LR
    A[Source meaning] --> B[Inspectable readback]
    B --> C[Useful response]
```

Use different diagrams for different relationships; inferred links need labels.
根据不同关系分别选图；推测关系必须标识。See examples/before-after.md.

[Mandatory every-turn adapter / 每轮强制入口](docs/always-on.md)

[对齐状态 / Alignment status](docs/alignment-status.md) · [原题与累计稿](examples/identity-current-view.md) · [未决交接](examples/unresolved-lineage.md) · [跨题更新](examples/cognition-evidence.md)

[本版示例 / Worked example](examples/formal-receipt-first.md) · [本版实际观察 / Runtime observations](docs/evaluation/formal-delivery/review.md)
