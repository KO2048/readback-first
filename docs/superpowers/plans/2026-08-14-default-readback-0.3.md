# Readback First 0.3 Candidate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Update the public candidate so readback is default, continuation normally follows the visible readback, user corrections can interrupt provisional work, and uncertainty is recommendation-first without mode menus.

**目标：**更新公开候选，使回讲默认发生、展示后通常继续推进、用户纠正可打断临时工作，并以 recommendation-first 处理不确定而不制造模式菜单。

**Architecture:** `PROTOCOL.md` remains normative; `SKILL.md` is the reference behavior when loaded; deterministic fixtures encode invariants; runtime pressure tests prove only conditional Skill behavior. Host default delivery and action authorization stay outside this change.

**架构：**`PROTOCOL.md` 继续作为规范真相源；`SKILL.md` 是被加载后的参考行为；deterministic fixtures 固定协议不变量；运行时压力测试只证明 Skill 条件行为。宿主默认交付与行动授权不在本次变更内。

**Tech Stack:** Markdown, JSON fixtures, Python 3 validators, fresh Codex subagents.

**技术栈：**Markdown、JSON fixtures、Python 3 validators、fresh Codex subagents。

## Global Constraints / 全局约束

- Plan version is `plan-v2`; branch is `codex/readback-first-default-readback-v3`.
- Base commit is `d89353b`; protocol target is `0.3 candidate`.
- Preserve fixtures `001-024` unless a directly conflicting contract requires a scoped migration.
- Use RED → GREEN → REFACTOR for every behavior slice.
- Do not touch prior untracked `evals/`, `CODEX-SETTING`, live targets, or private source material.
- Do not push, publish, tag, or create a release.

- Plan version 为 `plan-v2`；branch 为 `codex/readback-first-default-readback-v3`。
- Base commit 为 `d89353b`；目标协议为 `0.3 candidate`。
- 除非存在直接冲突的契约迁移，否则保留 fixtures `001-024`。
- 每个行为 slice 都执行 RED → GREEN → REFACTOR。
- 不触碰旧未追踪 `evals/`、`CODEX-SETTING`、live 或私有材料。
- 不 push、不 publish、不打 tag、不创建 release。

---

### Task 1: Default readback and proceed-after-readback / 默认回讲与回讲后继续

**Files:** `PROTOCOL.md`, `SKILL.md`, `tests/protocol_rules.py`, `tests/validate_contract.py`, `tests/fixtures/025-027*.json`, design/plan docs.

**Interfaces:** reception remains `shown`; response route becomes `proceed_with_provisional_response`; named blockers remain open input, source inadequacy, material ambiguity, explicit confirm-first, and host action authority.

- [x] Add fixture `025` for missing default readback and run `python3 tests/validate_fixtures.py`; expect failure because the new failure mode is unknown.
- [x] Add fixture `026` for an overblocked closed in-chat provisional draft and fixture `027` for bypassing a required gate; re-run and observe RED.
- [x] Add minimal evaluator branches and contract assertions; run validators and observe the old protocol contract fail.
- [x] Update `PROTOCOL.md` and `SKILL.md` minimally, preserving `reception_state: shown` while separating continuation route.
- [x] Run both validators and the existing 24-case regression; expect all cases to pass.
- [ ] Commit the independently green slice.

### Task 2: Interrupting corrections / 打断式纠正

**Files:** `PROTOCOL.md`, `SKILL.md`, `tests/protocol_rules.py`, `tests/fixtures/028-interrupt-correction-stale-output.json`.

**Interfaces:** append correction → link `corrects`/`supersedes` → mark only dependent provisional output `needs_revision` or `superseded` → re-evaluate blockers → continue or wait.

- [x] Run a fresh-agent multi-turn scenario against the pre-slice Skill. The observed behavior already passed: it preserved source, linked corrections, invalidated only dependent draft points, and continued without reopening unrelated scope. Do not fabricate a runtime RED.
- [x] Add fixture `028`; run fixture validation and observe RED from the previously unknown invariant.
- [x] Add the minimal rule and explicit protocol/Skill contract for the already-observed behavior.
- [x] Preserve the fresh-agent transcript as the conditional GREEN evidence for this slice; no second behavior-changing run was necessary.
- [ ] Run all validators and commit the green slice.

### Task 3: Recommendation-first uncertainty without menus / 推荐优先且无菜单的不确定处理

**Files:** `PROTOCOL.md`, `SKILL.md`, `tests/protocol_rules.py`, `tests/fixtures/029-033*.json`.

**Interfaces:** input completion → source adequacy → semantic ambiguity → output-form uncertainty. No material uncertainty means silent adaptation; low-impact uncertainty states a working assumption and continues; material uncertainty exposes impact and recommendation before waiting.

- [x] Add fixtures `029-033` for overquestioning, silent material assumption, mode menus, session-preference coverage bypass, and overview-only coverage; observe fixture RED.
- [x] Add evaluator branches and contract assertions; observe contract RED on the pre-slice wording.
- [x] Update the normative protocol and reference Skill; remove required mode footer/menu language.
- [x] Re-run the exact public-introduction pressure scenario and verify no menu, no unnecessary wait, and a normal continuation.
- [ ] Run all validators and commit the green slice.

### Task 4: Public alignment and final verification / 公开对齐与最终验证

**Files:** `README.md`, `README.zh-CN.md`, `CHANGELOG.md`, `examples/before-after.md`, `agents/openai.yaml`, `tests/README.md`.

- [ ] Update public definitions and the 0.2 → 0.3 migration without claiming host default delivery.
- [ ] Update the example to show readback followed by provisional continuation and user interruption.
- [ ] Update metadata so discovery covers ordinary user expression while stating reference-Skill limits.
- [ ] Run `python3 tests/validate_contract.py` and `python3 tests/validate_fixtures.py` fresh.
- [ ] Run fresh-agent pressure regressions for simple readback, proceed-after-readback, interrupt correction, low/high-impact ambiguity, and no-menu adaptation.
- [ ] Review `git diff --check`, `git status --short --branch`, and the full scoped diff.
- [ ] Commit the aligned public package. Do not push or publish.
