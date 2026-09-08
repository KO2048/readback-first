# 从纠错历史到能力验收 / History-driven alignment

Baseline inspected: v0.7.1, commit 2251aff6b5592075ff42dab720629f4b0316df75.
Plan Version: plan-v8. This document audits selected correction windows in two
private conversations, including preceding assistant output and following response.
It is not an exhaustive audit of every turn or verification of historical file writes.

Public examples are newly authored and sanitized. Private conversation identities,
paths, exact quotations and product details are kept outside this repository.
Local evidence maps H01–H08 to source events; public reviewers can reproduce the
generalized scenarios without access to private conversations.

## Evolution / 演变逻辑

1. The assistant offered a plausible summary and an organized result; the user
   objected that source meaning and ongoing additions were not inspectable.
   Correction: preserve material content before treating an overview as sufficient.
2. Overcorrection created a submit-and-accept process. The user instead needed to
   keep thinking, rejecting and revising the assistant's current understanding.
   Correction: detailed reception and normal continuation must coexist.
3. New editing sections displaced original question identities. Even claimed
   preservation was hard to inspect. Correction: stable source questions, nested
   meaning units and an integrated current view must survive revisions.
4. An overview was accepted as correct but incomplete. Correction: correctness
   of the displayed subset does not establish coverage of prior confirmed content.
5. Open questions must survive version changes and handoff, with source and
   resolution evidence. The user should not have to recall already recorded input.
6. Later cognition may change premises shared by several topics. Correction:
   inspect impact and recompose the authorized scope when a local patch is inadequate.

这些校正是累积关系，不应只选最早的“等待确认”，也不应只选后来的“继续讨论”。
来源内容、接收确认、当前认知与行动授权必须分开；讨论继续不代表全部定案。

## Capability mapping / 能力对照

### H01 — 接收完整性：总览正确不能替代信息覆盖

- Historical failure pattern: AI 给出看似正确的总览并声称已整理，但用户无法核对未展示的理由、例外和候选。
- User correction, paraphrased: 按来源逐项保留信息；总览只作导航，不能代替完整当前内容。
- Current source: PROTOCOL.md §§2, 6, 9
- Finding: 规则已有；复杂样本覆盖不足
- Regression: tests/history/cases.json, H01

### H02 — 问题身份：跨轮保留原编号、标题和层级

- Historical failure pattern: AI 用本轮处理章节替代原问题编号，导致同一编号指向不同主题，用户无法定位修正。
- User correction, paraphrased: 保留原问题身份；拆分子项应保持父子关系，新增内部编号不能替换来源编号。
- Current source: PROTOCOL.md §5; SKILL.md Build the readback
- Finding: 稳定 ID 已有；来源问题与新条目映射欠明确
- Regression: tests/history/cases.json, H02

### H03 — 累计理解：局部修正后提供同题完整当前视图

- Historical failure pattern: AI 仅在文末追加本轮差量或编辑区，用户看不到旧内容与新修正如何合成同一问题。
- User correction, paraphrased: 用户请求整合稿时，回到原主题提供累计当前理解；仅更新受影响内容，保留来源和旧状态。
- Current source: PROTOCOL.md §7; §8 delta constraints
- Finding: 局部依赖失效已有；累计视图触发需明确
- Regression: tests/history/cases.json, H03

### H04 — 未决继承：转交、改版和解决证据不能丢链

- Historical failure pattern: 用户担心已外化的问题在新文档或系统整合后消失；AI 的保存承诺不等于可核实保存。
- User correction, paraphrased: 保留问题、来源、状态和去向；转交不等于解决，已解决仍保留解决依据。
- Current source: SKILL.md Precise waiting and continuation; PROTOCOL.md §§6,10
- Finding: 原则已有；跨版本与转交验证不足
- Regression: tests/history/cases.json, H04

### H05 — 认知演变：检查跨主题影响与完整重整边界

- Historical failure pattern: 同题新答案被当成局部措辞修正，忽略它改变其他主题共同前提的可能性。
- User correction, paraphrased: 区分新认知与旧答案错误；检查已知依赖，必要时在授权范围重整完整当前方案，未知保持未知。
- Current source: PROTOCOL.md §7; §8 full view
- Finding: 依赖失效规则部分覆盖；跨主题影响检查不足
- Regression: tests/history/cases.json, H05

### H06 — 共同推演：可继续修改的理解不等于提交验收

- Historical failure pattern: AI 先因信息不全而过早总结，随后过度纠偏，把每轮共同讨论都变成整体接受和完整性验收。
- User correction, paraphrased: 确认仅绑定明示范围；允许在当前理解上继续反驳和补充，不重开整批确认循环；明确只回讲和开放输入仍应等待。
- Current source: PROTOCOL.md §4; SKILL.md Incremental continuation
- Finding: 继续回应与批次门禁已有；讨论型场景需回归
- Regression: tests/history/cases.json, H06

### H07 — 版本留痕：区分表达者、来源快照与可编辑下一稿

- Historical failure pattern: 用户直接改写 AI 输出稿会抹掉谁在何时表达什么；反复改变批次版本又让讨论失去连续性。
- User correction, paraphrased: 在有真实存储能力时保留源快照与用户修改的派生关系；协议不强制所有用户采用奇偶版本，也不自行决定正式路径。
- Current source: PROTOCOL.md §§5,7,10
- Finding: 来源追加原则已有；宿主文档交接约定未覆盖
- Regression: tests/history/cases.json, H07

### H08 — 对齐证据：区分规范、实际输出与宿主补足

- Historical failure pattern: 历史完成报告、漂亮账本或同宿主样本容易被误当成技能独立能力与每轮生效证明。
- User correction, paraphrased: 原始输入、输出、配置、加载与真实动作分开取证；记录相同宿主污染、缺失来源和未验证项目。
- Current source: PROTOCOL.md §12; docs/always-on.md
- Finding: 证据分层已有；独立运行与长链测试不足
- Regression: tests/history/cases.json, H08

## Claims / 证据边界

Historical assistant messages sometimes claim changes, saves, validation or
publication. This audit treats those as historical reports, not freshly verified
facts. User objections demonstrate the unmet collaboration requirement in that
context; they do not prove every fault remains in v0.7.1.

No runtime outcome is assigned to a case until an actual answer is archived and
reviewed. A passed sample is not broad reliability, automatic activation or
independence from legacy governance. Diagram work is outside this batch.

[Issue and PR sequence](../plans/2026-09-08-history-alignment.md).
[First H02 observation](history-H02/review.md): identity failure not reproduced; other wording concerns retained.
