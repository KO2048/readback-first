# Pair 001 — installation and comparison request

Evidence class: authored same-session comparison illustration. Both responses
below are composed in one shared-context Codex turn after reading the installed
v0.7.0 contract. They are not independently sampled or blinded model runs, and A
is not claimed to be an uncontaminated governance-only baseline.

证据级别：本轮编写的同会话对照示例；非独立运行，不做纯治理与纯 Skill 的效果归因。

## Original input / 用户原始输入

> 继续规划多个版本，对齐当前我们的版本能力
>
> 你可以先把最新的0.7.0 安装上，然后 同步对比，先不拆掉我们的治理层的回讲逻辑。
>
> 如何对比。
>
> 可以是，治理层先进行回讲---这是默认的，然后，在做一个划分，用readback-first skills进行skill执行，然后 对比内容，如何？？

## A — Governance-priority response / 治理优先回应

回讲：你希望继续分版本对齐当前回讲能力；先安装 0.7.0，保留原治理逻辑，再用同一条输入，
先给治理回应、分隔后给 Skill 回应，最后比较内容。

可以。对照既要看接收是否完整，也要看回讲后是否有判断、理由和有效推进。
本轮先完成新增安装与规划，治理文件保留；同会话结果用于发现差异，独立效果后续另测。

## B — Explicit Skill-guided response / 显式应用 Skill

回讲：你的目标是让后续版本逐步达到当前协作效果。眼下先安装 0.7.0，不替换治理层；
比较顺序是治理回应、Skill 回应，再检查差异。

这个顺序适合日常核对。建议把每次对比固定到同一份原始输入，检查遗漏、AI 增加的假设、
表达方式和后续回应；实际动作只执行一次。两份回答共享上下文，不能据此判定 Skill 单独
达到相同水平。后续版本按具体差异立项，而不预先宣布已经补齐。

## Comparison / 内容比较

- Both preserve all six central constraints: multi-version alignment, install
  v0.7.0, retain governance, governance first, explicit Skill separation, comparison.
- A explicitly stresses the completeness of the substantive response after readback.
- B more explicitly enumerates comparison checks and the no-duplicate-action boundary.
- These wording differences are observations about authored outputs, not proof of
  a causal Skill advantage. Neither pair supplies independent runtime validation.
- No user preference judgment of this pair has been recorded yet.

两份保留同一范围；A 强调“回讲之后继续”，B 展开对比维度与动作只执行一次。
差异尚不能归因于 Skill，用户对这组效果的判断也尚未记录。

## Actual work, separate from the two responses / 实际动作

Installed pinned v0.7.0 with skill-installer. Verified the installed tracked files
against the release tag and kept existing governance/Typeless hashes unchanged.
Protocol and 39 deterministic fixtures passed. Prepared planning/evaluation docs;
no next-version implementation, global-rule replacement or isolated A/B run.

See [method](governance-v070-comparison.md) and [version candidates](../plans/2026-09-07-v08-v11-alignment.md).
