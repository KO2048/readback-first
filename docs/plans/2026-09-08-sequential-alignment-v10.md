# Sequential alignment / 顺序能力对齐

Plan Version: plan-v10. User authorized completing sequential releases without
waiting for per-version confirmation; preserve existing governance.

用户授权逐版本直接完成，保留现有治理。范围依次为：问题身份和累计理解；未决项
与版本交接；跨主题认知更新与证据边界。每批基于上一发布版建立独立工作目录。

Test current behavior first with actual sequential conversations. Preserve raw
outputs, compare against source units, and record limitations. Only change behavior
when a concrete failure supports a minimal correction. Otherwise deliver examples
and evidence as patch releases. Run separate Push and Publish Gates for each batch.

先实测再决定修复。未复现的历史问题不伪称修复；示例和证据按补丁版交付。每批
检查协议、fixtures、证据引用和工作目录，再分别通过推送和发布审核。实际安装前
核对旧版无漂移并备份，安装后对照发布tag逐文件校验。

Owned scope: SKILL.md, PROTOCOL.md, examples/, docs/, tests/, README.md,
README.zh-CN.md, CHANGELOG.md, release.json. Public synthetic scenarios only.
