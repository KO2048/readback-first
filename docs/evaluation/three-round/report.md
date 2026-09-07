# 三轮配对观察与修复 / Three-round observation and patch

Date: 2026-09-07. Baseline: installed v0.7.0, tag 8ba109b7c343959de01213218da334ba0a43f881.
Plan-v6 covered probes; plan-v7 approved the scoped diagram patch and replay.

## Method / 方法

这是真实采样的两个连续对话、各三轮，共六份输出；不是三次独立复现实验，
也不是主代理代写的示范对照。测试输入由主代理构造，使用客户反馈这一合成场景。
A 按治理规则指导，B 显式读取 Skill；两者不读取对方输出。分支代理 fork_turns=none，
模型/推理设置继承宿主，精确服务版本和全部宿主前缀未独立审计，不声称完全隔离或因果归因。

A requested reads: ~/.codex/AGENTS.md and ~/.codex/skills/typeless/SKILL.md.
B requested reads: ~/.codex/skills/readback-first/SKILL.md and PROTOCOL.md.
The controller instructed both to remain read-only and return ordinary responses.
This constraint itself can improve action restraint: the result does not establish
unconstrained tool-use safety. Only returned answers are archived here, not full
provider tool traces. No claim of verified zero side effects is made from prose alone.

两组共享测试任务约束。因此本轮能检查回应中的授权表达，不能证明离开测试约束后
不会越权。原始答复逐字记录；工具读取和宿主加载没有完整独立审计。未运行渲染器，
Mermaid 的“内容关系审查”与实际渲染验证分开。

## Inputs and raw responses / 输入与原始输出

| Round | Input | Governance A | Skill B |
| --- | --- | --- | --- |
| 1 | [unfinished input](raw/round-1-input.md) | [A1](raw/round-1-a.md) | [B1](raw/round-1-b.md) |
| 2 | [correction and judgment](raw/round-2-input.md) | [A2](raw/round-2-a.md) | [B2](raw/round-2-b.md) |
| 3 | [draft, placeholder and diagrams](raw/round-3-input.md) | [A3](raw/round-3-a.md) | [B3](raw/round-3-b.md) |

## Criteria and observations / 核对标准与结果

人工按源信息核对以下标准；这是定性审查，不是盲评、预注册实验或统计得分。

| 轮次 | 核对标准 | A 与 B 的实际表现 | 判断 |
| --- | --- | --- | --- |
| 1 | 保留理由、猜想、可复用认知、未来用途；关注新用户不排除老用户；未完句不强制确认或提前设计 | 两组都保留上述内容，以“你继续”收尾；B 比 A 更紧凑 | 本场景均满足 |
| 2 | 撤回新用户优先；原句不改、理由新旧可追溯；流失定义未决不阻断方向判断 | 两组都保留改动及未决项，继续给“值得做”的理由，没有问卷 | 本场景均满足 |
| 3 | 仅在聊天起草；7天仅占位；旧边界延续；图分别帮助检查关系与顺序；给建议且不虚报落地 | 两组文字、第二张流程图、建议基本满足；第一张图均有可改进的条件表达 | 局部图文一致性未满足 |

B3 的第一图把 F 标为“支持、反驳或仍不足以判断”，又用无条件 F → G
指向“形成有依据、带限定的判断”。这不必然表示已声称实施，但让证据不足也可能
流向有依据判断；不能用后文或第二张图中正确的门禁替它消除歧义。
此外第一图偏处理顺序，与第二图重复，关系的支持/反驳含义不够直接。

A3 也不是金标准：第一图 A、B、D 均无条件进入阶段性判断，条件不够清楚；
但它至少标注了“引出可能解释”和“支持、反驳或仍不足以判断”的关系。
应修复可检查的效果，不复制 A 的全部措辞和箭头。

## Implemented change / 已实施改动

v0.7.1 candidate adds Diagram semantic consistency to SKILL.md and normative
PROTOCOL.md: inspect each arrow independently, distinguish relationship meaning
from workflow order, keep insufficient evidence unresolved, and never promote
an unapproved placeholder through a diagram. No additional mandatory diagram
type or fixed response template is introduced.

本轮没有观察到足以支持全面改写多价值接收或实质回应的缺陷，故不为了版本数量
增添规则。候选 v0.8–v0.11 仍是待证据收敛的范围。此补丁完成一个局部修复，
不表示可移植 Skill 已全面达到治理层能力。

## Targeted replay / 修复重测

Targeted semantic review: PASS for the reported ambiguity. The replay uses a fresh read-only agent, candidate Skill and the same
three original inputs, without either arm's answers or the failure analysis.
The replay only generates the third answer; preceding assistant history differs.
It therefore checks the targeted fix, not a matched end-to-end replication.

## Remaining evidence / 仍需证据

- Every-turn automatic activation, context reload and missing-Skill behavior.
- WorkBuddy-specific runtime and renderer behavior.
- Actual action traces under ordinary host authority instead of read-only probes.
- Broader inputs, longer correction chains and independently reviewed source coverage.

[Raw patch replay](raw/round-3-patch-replay.md) separates “足以支持时”, “构成反证时”
and “无法区分时” in its relationship view, and “支持充分”, “出现反证” and “不足或冲突”
in its workflow view. Neither diagram applies the unapproved seven-day placeholder.
The reply still supplies a discussion draft and recommendation. It is longer than
the baseline; this single replay does not establish a general quality gain.

复测是一次新代理重放，不是三轮完整重复；原始样本中的两个失败图均原样保留。
Contract validation and 39 authored fixtures passed after the patch.
