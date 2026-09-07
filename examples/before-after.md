# Complete response examples

These are authored reference examples, not recorded runtime results.

## Closed input: read back, then answer

User:

> 我想把回讲能力从治理文档迁入 Skill，但每次仍要自动使用。你认为可行吗？先别修改。

### Plausible failure

> Received: migrate readback. State: WAITING_FOR_CONFIRMATION. 请确认后我再分析。

### Better response

回讲：你希望由 Skill 承载详细回讲逻辑，同时保留每次自动应用；这次只讨论可行性，不修改。

可行。全局入口可以强制应用 Skill，Skill 再根据内容选择回讲深度与回应方式。
这样能集中维护协议，但迁移时要保留原有的修正链、未决项和授权边界。
我建议先以现有真实对话比较新旧效果，通过后再替换详细规则。

| 层次 | 职责 |
| --- | --- |
| 全局入口 | 每条用户输入强制应用 Skill |
| Skill | 接收、表达、继续回应、必要澄清 |
| 宿主权限 | 判断实际操作是否已获授权 |

## Trace note for evaluators

The closed advisory example uses `response_route: proceed_with_provisional_response`
and `reception_state: shown`, not user confirmation. A correction marks only
its dependent provisional output `needs_revision`; retain unrelated content and
all source qualifiers. This note is evaluation bookkeeping, not part of the
normal user-facing response.
