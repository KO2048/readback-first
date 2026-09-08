# History-driven alignment batches / 历史纠错对齐批次

Plan Version: plan-v8. Baseline v0.7.1. This plan refines the earlier v0.8–v0.11
proposal using historical corrections; it does not assign new release versions.
Earlier proposed version slots remain candidates, not a delivery schedule.

## Objective / 目标

Recover the cumulative collaboration effect from actual correction histories.
Keep global governance while comparing. Publish sanitized reproducible cases,
not private source conversations. Distinguish source audit, tests, behavior fixes
and releases throughout.

依据真实纠错恢复累计协作效果，对比期保留治理层。公开脱敏案例，私人原始来源单独
留存。来源审计、测试、行为实现和发布分开记录。

## Issue map / 工作项

- [overview #11](https://github.com/KO2048/readback-first/issues/11) — [对齐总览] 从历史纠错到可复现的回讲能力
- [H01 #12](https://github.com/KO2048/readback-first/issues/12) — [对齐 H01] 接收完整性：总览正确不能替代信息覆盖
- [H02 #13](https://github.com/KO2048/readback-first/issues/13) — [对齐 H02] 问题身份：跨轮保留原编号、标题和层级
- [H03 #14](https://github.com/KO2048/readback-first/issues/14) — [对齐 H03] 累计理解：局部修正后提供同题完整当前视图
- [H04 #15](https://github.com/KO2048/readback-first/issues/15) — [对齐 H04] 未决继承：转交、改版和解决证据不能丢链
- [H05 #16](https://github.com/KO2048/readback-first/issues/16) — [对齐 H05] 认知演变：检查跨主题影响与完整重整边界
- [H06 #17](https://github.com/KO2048/readback-first/issues/17) — [对齐 H06] 共同推演：可继续修改的理解不等于提交验收
- [H07 #18](https://github.com/KO2048/readback-first/issues/18) — [对齐 H07] 版本留痕：区分表达者、来源快照与可编辑下一稿
- [H08 #19](https://github.com/KO2048/readback-first/issues/19) — [对齐 H08] 对齐证据：区分规范、实际输出与宿主补足

## PR sequence / PR 顺序

1. Evidence foundation: source-to-capability audit, eight sanitized scenarios and
   first H02 baseline observation. No protocol or version change.
   证据基础：能力映射、八项案例及 H02 首次基线；不改协议或版本，不关闭行为 issues。
2. Reception and continuation: test H01/H06 together so fixing information loss
   does not introduce blanket confirmation gates.
   接收与继续：联合验证 H01/H06，避免修复信息丢失时引入全面停等。
3. Stable identity and cumulative view: H02/H03, including long chains and
   source question hierarchies. Add rules only for observed or confirmed gaps.
   稳定身份与累计视图：H02/H03，加入长链和来源问题层级；依据缺口改规则。
4. Inheritance and impact: H04/H05/H07, separate PRs when independently testable.
   Persist only with a verified host capability and existing authorization.
   继承与影响：H04/H05/H07，能独立验收时分 PR；持久化依赖真实宿主与授权。
5. H08 is an evidence track across all batches: host loading, context reload,
   missing dependency behavior, render support and real action traces.
   H08 贯穿各批次：宿主加载、重载、缺失依赖、渲染与真实动作分别取证。

## Acceptance and publication / 验收与发布

Each behavior PR links the issue, source case, raw baseline, minimal change,
replay and limitations. An authored scenario or keyword check does not resolve
a behavior issue. If current behavior passes, retain the regression and broaden
the evidence without claiming a new capability.

每个行为 PR 都有问题、案例、原始基线、最小修复、重测与局限。现版已通过时保留
回归并扩大证据，不为了增版本编造改进。实际版本通过自身检查后合入 main 并发布，
确保普通安装用户取得最新正式版本；候选版不取代正式版。

The initial plan-v8 PR is a test/evidence delivery, not full alignment. Scope:
docs and tests only, isolated branch codex/history-alignment-regressions.
Existing installed v0.7.1 and global governance remain unchanged.
