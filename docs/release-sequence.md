# Public iteration sequence / 公开迭代顺序

These are reviewable candidates, not published releases. The six stages preserve
existing v0.2/v0.3 lineage and split umbrella PR #1; they do not manufacture a
release history. Each stage records its problem, source, delta and evidence.

这些是可分别评审的候选，不是已发布版本。保留旧候选谱系，按真实改动记录，
便于公开解释价值；效果未验证时不将其包装成已证明的收益。

| Version / 版本 | Theme / 主题 | Status / 状态 |
| --- | --- | --- |
| [0.2.0](releases/0.2.0.md) | 来源与确认分离 | candidate in this history / 本分支已包含候选 |
| [0.3.0](releases/0.3.0.md) | 回讲后继续回应 | candidate in this history / 本分支已包含候选 |
| [0.4.0](releases/0.4.0.md) | 准确等待 | candidate in this history / 本分支已包含候选 |
| 0.5.0 | 自然正文 | planned / 后续候选 |
| 0.6.0 | 多视图表达 | planned / 后续候选 |
| 0.7.0 | 每轮强制应用 | planned / 后续候选 |

Review dependency: main → 0.2 → 0.3 → 0.4 → 0.5 → 0.6 → 0.7.
The original umbrella remains provenance, not a competing merge route. Later PRs
use the preceding branch as their base, so reviewers see a scoped incremental diff.
After a base is merged, retarget its successor to main and recheck the diff; keep
commit ancestry when merging the stack. Candidate creation, review, merge, tag,
installation and verified runtime adoption are distinct states.

公开传播每次回答四件事：遇到什么问题、改了什么、拿什么证据验证、还有什么限制。
Version number increases do not prove quality gains. No schedule or launch dates
are fabricated, and no promotional messages are sent by this change.
