# 历史要求到实现与验收

来源：用户本轮重申的通用要求，以及既有治理文本中“正式答复正文、无需展开”的
约束。这里追踪本项要求，不宣称已经重新穷尽所有历史会话。

| 要求 | 实现 | 验收 |
| --- | --- | --- |
| 所有harness默认应用 | SKILL首段、PROTOCOL §0、always-on入口 | 普通请求；宿主/版本/实际加载记录 |
| 首个任务内容是实质回讲 | First output；行动通知不算 | 事件中的receipt与action_notice分开审阅 |
| 必须在正式对话正文 | 所有入口排除thinking、progress、collapsed status | UI映射必须有证据；未知不通过 |
| 先回讲再工具/判断 | may改MUST；只豁免契约加载 | TASK_BEFORE_RECEIPT、ANSWER_BEFORE_RECEIPT |
| 最终正文也保留 | Reader-facing response | FINAL_RECEIPT_MISSING |
| 不靠用户反复提示 | 默认普通请求，无readback cue | 实际普通任务；自动发现另测 |
| 不新增确认循环 | 不支持则说明宿主限制，不要求再次确认输入 | 候选受限宿主输出 |
| 不能用模型自报冒充显示证据 | 适配器观测与语义审阅分工 | traces+UI；单个布尔量不证明履约 |

修复原则：认知资产不仅保留为文字，还必须对应执行位置、失败条件与复核依据。
