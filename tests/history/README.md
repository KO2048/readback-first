# 历史纠错回归 / Historical correction regressions

Eight authored, sanitized scenarios extracted from recurring collaboration
failure patterns. They are not verbatim private transcripts or runtime passes.
The existing 39 fixtures remain separate.

## Manual evaluation / 人工评估

For each case, read the input and source-state inventory before inspecting the
answer. Check every listed criterion semantically, including qualifiers and
relationships. A keyword hit, ID list or model self-score is not coverage proof.
Record met / missed / unclear with an exact output span and a reason.

每个案例都需要保存实际输入、实际输出与逐项判断。遗漏和解释歧义分开，不能只比
字数或编号数量。保持原始失败；测试题中有显式提醒，后续必须加入去掉提醒和长链变体。

For a behavior change, record the current Skill baseline before editing. Compare
with governance-guided output against the same source, not against a presumed
perfect governance answer. If testing independent contribution, also capture a
no-guidance control and verify host configuration. Shared-host observations must
remain labelled as such. Proposed, started and verified actions need actual trace
evidence; read-only probes cannot establish ordinary action safety.

## Release boundary / 发布边界

This PR adds evaluation assets only. It does not change SKILL.md, PROTOCOL.md,
release.json, installed Skills or global governance. No issue is resolved merely
because its scenario exists. Each behavioral PR must link its issue, baseline,
minimal change, replay, remaining limitations and release decision.
