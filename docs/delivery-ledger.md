# Issue → 开发提交 → PR → 发布版本

这是已核验交付的快照，不是运行效果保证。以GitHub实际状态、tag及原始证据为准。
Issue开放可能表示部分已交付但验收未完成；PR合并也不等于全部能力已经验证。

实现commit记录具体改动，merge commit记录合入main的位置，发布tag指向交付快照。
以下PR均已推送并合并，各版本已发布。旧提交信息保持原样，不改写历史。

| 版本 | Issue | PR | 改动commit | merge commit | 交付性质 | 尚欠什么 |
|---|---|---|---|---|---|---|
| [v0.8.0](https://github.com/KO2048/readback-first/releases/tag/v0.8.0) | #21；#12/#17部分 | [#22](https://github.com/KO2048/readback-first/pull/22) | [1871acb](https://github.com/KO2048/readback-first/commit/1871acb6318b2820fcb354aaf1f1dbf8beb4318d) | [6e76cb8](https://github.com/KO2048/readback-first/commit/6e76cb807ad7b78d37949e5df9c6ee25ed138458) | 行为修改：来源具体程度；连续回应回归 | #21关闭，其余仍待全面验收 |
| [v0.8.1](https://github.com/KO2048/readback-first/releases/tag/v0.8.1) | #12/#13/#14/#17/#19 | [#23](https://github.com/KO2048/readback-first/pull/23) | [396ff07](https://github.com/KO2048/readback-first/commit/396ff07862882f4adc24050834c1173723ca014a) | [524d862](https://github.com/KO2048/readback-first/commit/524d8623e602a2fdcb0c27c368947ffcf43cba51) | 示例与证据；未修改Skill行为指令 | 长链、独立宿主与实际动作未验收 |
| [v0.8.2](https://github.com/KO2048/readback-first/releases/tag/v0.8.2) | #24；#15/#18/#19 | [#25](https://github.com/KO2048/readback-first/pull/25) | [5d63d18](https://github.com/KO2048/readback-first/commit/5d63d188a8156c67ec965cb4e3b69ce73000bfa7) | [f53f984](https://github.com/KO2048/readback-first/commit/f53f984e89e4843a7269b577628db2c632c2e6b2) | 版本识别修复；未决交接为示例和证据 | #24关闭，交接行为全面验收仍开放 |
| [v0.8.3](https://github.com/KO2048/readback-first/releases/tag/v0.8.3) | #16/#19；总览#11 | [#26](https://github.com/KO2048/readback-first/pull/26) | [e8a4650](https://github.com/KO2048/readback-first/commit/e8a4650484c050197da435800aa3a73da529c843) | [69caf04](https://github.com/KO2048/readback-first/commit/69caf043f4750a049ee2650b98ddeab5e0ac5d21) | 跨主题示例与证据；未修改Skill行为指令 | 不能据同宿主样本宣称全面对齐 |
| [v0.9.0](https://github.com/KO2048/readback-first/releases/tag/v0.9.0) | #27/#19 | [#28](https://github.com/KO2048/readback-first/pull/28) | [fd97b6e](https://github.com/KO2048/readback-first/commit/fd97b6e8557796b0edaed10e2d1ccd7e544f1381) | [0a0b7bd](https://github.com/KO2048/readback-first/commit/0a0b7bd1da72c9a60b8dd72eba7ff400ae06e691) | 行为修改：正式消息先于任务工具；顺序检查 | 真实宿主显示与默认加载仍待验收 |
| [v0.10.0](https://github.com/KO2048/readback-first/releases/tag/v0.10.0) | #29 | [#30](https://github.com/KO2048/readback-first/pull/30) | [236acc2](https://github.com/KO2048/readback-first/commit/236acc28e55c3c979e2e5a0aee16063eb96f4961) | [0928704](https://github.com/KO2048/readback-first/commit/0928704334e745b13af6e35c5b3f3e4e8c5d1bff) | 新增行为契约：默认值、动作与依据；合成回复回归 | 真实动作与独立宿主未验收，#29开放 |

## 这次分批

- 第一批v0.10.0：#29契约补齐，PR #30，实际修改Skill与协议，独立发布。
- 第二批v0.10.1：本台账、提交约定及首页入口；属于交付可追溯文档，**没有新增模型行为**。
  本文所属提交由本版tag和Git历史定位，自身文件不伪造包含自身的commit hash。
- 后续验收批次：#29真实动作与边界；#27正式消息显示/普通请求/后续轮次；
  #12–#19长链及独立上下文。按观察到的缺口决定实现或证据交付，不预填完成日期，
  不因发布一个版本批量关闭Issue。

## 后续commit与PR写法

暂用英文type、中文主题和中文正文，技术标识保持原文。例如：

`feat(readback): 补齐默认值与实际行为的授权记账`

正文记录：版本、Issue、具体改动、验证结果、未完成验收。PR说明写相同边界，
链接实现commit与测试证据。只交付文档用docs，不写成fix；只有修复证据支持才用fix。

版本号不是验收结论。具体Issue仅在其验收条件满足时关闭；部分交付写Refs而不是
Fixes。旧Issue中“当前最新版”等文字属于历史记录，现状应从最新release与本表核对。
