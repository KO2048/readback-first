# Public iteration sequence / 公开迭代顺序

Latest public version: **v0.7.0**. Install from `main`, or pin the v0.7.0 release.
The intermediate versions below were merged separately as iteration milestones;
this publication does not invent earlier releases or tag every milestone.

用户直接从 main 安装最新版；中间版本保留独立合并、问题、改动与验证记录。
本次仅发布 v0.7.0 tag，不把候选拆分伪装成过去发生过的多次发布。

| Version | Theme | Record | Status |
| --- | --- | --- | --- |
| [0.2.0](releases/0.2.0.md) | 来源与确认分离 | [PR #2](https://github.com/KO2048/readback-first/pull/2) | merged; `4f19051` |
| [0.3.0](releases/0.3.0.md) | 回讲后继续回应 | [PR #3](https://github.com/KO2048/readback-first/pull/3) | merged; `416e79d` |
| [0.4.0](releases/0.4.0.md) | 准确等待 | [PR #4](https://github.com/KO2048/readback-first/pull/4) | merged; `98c633d` |
| [0.5.0](releases/0.5.0.md) | 自然正文 | [PR #5](https://github.com/KO2048/readback-first/pull/5) | merged; `25e468f` |
| [0.6.0](releases/0.6.0.md) | 多视图表达 | [PR #6](https://github.com/KO2048/readback-first/pull/6) | merged; `d7b6782` |
| [0.7.0](releases/0.7.0.md) | 每轮强制应用 | [PR #7](https://github.com/KO2048/readback-first/pull/7) | merged; `5095805` |

## Evidence boundary / 证据边界

Each stage passed its recorded deterministic checks. Cross-model response quality,
host activation and renderer evaluation remain pending. These limits are stated
in the release notes; they do not require users to install an older implementation.

每次传播说明真实问题、改动、证据与限制，不以版本号增长替代效果证明。
The original umbrella PR #1 remains a closed historical source.
