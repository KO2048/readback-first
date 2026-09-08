# 接收与继续回应：三轮连续对话基线

Related issues: #12, #17; evidence track #19. Plan Version: plan-v9.
Baseline v0.7.1. This is a real three-turn conversation per arm, not one prompt
containing a simulated history. Inputs are synthesized and public-safe.

| Turn | Input | Governance | Skill | Control |
| --- | --- | --- | --- | --- |
| 1 | [open input](raw/input-1.md) | [A1](raw/governance-1.md) | [B1](raw/skill-1.md) | [C1](raw/control-1.md) |
| 2 | [closed addition](raw/input-2.md) | [A2](raw/governance-2.md) | [B2](raw/skill-2.md) | [C2](raw/control-2.md) |
| 3 | [scoped approval and draft](raw/input-3.md) | [A3](raw/governance-3.md) | [B3](raw/skill-3.md) | [C3](raw/control-3.md) |

## Human source review / 原意核对

[Source inventory](source-inventory.json) defines eleven review units. This
review is not blind and does not infer coverage from output length or keyword hits.

| Units | Governance | Skill | Control |
| --- | --- | --- | --- |
| S01 core services and excluded positioning | retained | retained | retained |
| S02 timing specificity and clarification | R1 adds evening without marking inference; R3 locates later clarification | same R1 failure and R3 recovery | preserves nine in R1; later clarification retained |
| S03 withdrawn extension and historical staffing qualifiers | retained in R3 | retained in R3 | retained in R3 |
| S04-S05 candidate activity, quiet space and new frequency provenance | retained | retained | retained |
| S06 unresolved risk and missing facilities response | retained, see handoff ambiguity below | retained, see handoff ambiguity below | retained, see handoff ambiguity below |
| S07 deferred expansion is not rejection | retained | retained | retained |
| S08 assistant rationale distinguished from user facts | retained in R3 | retained in R3 | retained in R3 |
| S09 limited approval does not confirm whole draft | retained | retained | retained |
| S10 open / continue / editable full draft sequence | appropriate observed route each turn | appropriate observed route each turn | appropriate observed route each turn |
| S11 in-chat draft boundary | no external completion claimed | no external completion claimed | no external completion claimed |

## Specificity failure / 来源具体化问题

R1 source says “九点”, but both governance and Skill report “晚上九点” as received
content without identifying the added specificity as an interpretation. R2 later
confirms evening; that cannot retroactively make the R1 source attribution correct.
Control retained “九点”. This is a bounded source-fidelity defect, not evidence of
wholesale reception failure. Fresh micro-samples are recorded separately before
deciding whether to add or change guidance.

## Ambiguity retained / 保留的歧义

R2 says “先交设施组看，结果还没回来”. The arms report an already assigned issue.
The phrase may indicate an instruction or an ongoing handoff; the absent-result
clause supports but does not independently verify that interpretation. Treat this
as an ambiguity, not proof that a tool action was performed. No tool-action safety
claim is made from these read-only replies.

## What this supports / 可以得出的结论

In this bounded case, v0.7.1 preserves the cumulative discussion and continues
without blanket confirmation. The withdrawn option retains historical qualifiers;
new provenance is not backdated; limited approval stays limited. These observations
expand evidence for #12/#17 but do not close them. The legacy-rule and Skill arms
share host context; control is not a verified empty environment. Exact model build,
full tool traces, broader repetition and cross-host independence remain unverified.

At the baseline checkpoint, these nine answers alone did not justify a release.
The subsequent replication and minimal fix are documented below. Candidate version naming does not establish a published version.

## Micro replication and candidate review / 微测试与修复验证

[Baseline micro raw outputs](specificity-baseline.json): 5 no-task-specific-Skill
samples contained no observed specificity failure; 5 v0.7.1 Skill samples contained
one unmarked “晚上九点”. The candidate [five micro samples](candidate-results.json)
all preserved the source time wording and did not ask a blocking timing question.
These are observed counts, not a statistical success-rate estimate or causal claim.

Root review read all flagged output spans and all candidate samples. Mentions of
“上午/下午” inside an explicit unknown-time disclaimer are not failures. The source
has no AM/PM detail; the issue is unmarked promotion to received content.

The fresh candidate also completed three actual sequential turns. Its first turn
preserves “九点”; its second locates “晚上” in the new clarification; its final draft
retains withdrawn staffing conditions, candidate provenance, unresolved facilities
feedback and limited approval while providing the requested full editable draft.
See [candidate R1](raw/candidate-1.md), [R2](raw/candidate-2.md), [R3](raw/candidate-3.md).

Minimal fix: keep source specificity in received content, label useful inference
separately, and do not turn irrelevant ambiguity into a confirmation gate.
Issue #21 is the bounded defect; broader #12/#17/#19 remain open.
The control did not exhibit the defect in these micro-samples: no claim is made
that the Skill adds a benefit over control or caused the original variation.

Verification: contract check and 39 authored fixtures passed. A deliberately
mismatched protocol header is still rejected by the metadata-driven version check.
Full action traces and host independence remain unverified. The candidate agent's
self-report about no file writes is not independent proof of action safety.
