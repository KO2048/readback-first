# Readback First 0.3 Candidate Design

## Status / 状态

Approved conversation design baseline for `plan-v2`; implementation and runtime evidence remain pending.

这是 `plan-v2` 已批准的对话设计基线；实施与运行时证据仍待完成。

## Product contract / 产品契约

Readback First makes a visible readback the default before an AI relies on new user expression to answer or act. The readback adapts in density and organization. After showing it, the AI normally continues on the visible working understanding; the user may interrupt and correct it at any time.

Readback First 让 AI 在依据新的用户表达回答或行动前，默认先展示回讲。回讲的详略和组织方式可以自适应。回讲展示后，AI 通常基于这份可见工作理解继续推进；用户可以随时打断和纠正。

## Core boundaries / 核心边界

- `READBACK_SHOWN` remains a reception state; continuation is a separate response route.
- Ordinary simple input gets a one-line readback and same-turn answer.
- Explicit direct-answer requests may omit visible readback only where no other gate requires it.
- Closed, sufficiently understood, non-consequential in-chat analysis or drafting proceeds after readback.
- Open input, source inadequacy, material ambiguity, explicit confirm-first requests, and host safety or action authorization may still block.
- User correction preserves the old expression, appends the correction, links the relation, and invalidates only dependent provisional output.
- The AI chooses presentation silently by default. It surfaces uncertainty only when different reasonable interpretations or forms materially change the result.
- Recommendation-first means: show understood content, identify the uncertainty, explain impact, give the current judgment and recommendation, then ask only when necessary.

- `READBACK_SHOWN` 仍是接收状态；继续推进属于独立的 response route。
- 普通简单输入采用一句回讲并同轮回答。
- 只有在不存在其他必要门禁时，显式直答才可省略可见回讲。
- 已闭合、来源足够、非外部行动的聊天内分析或草稿，在回讲后继续推进。
- 输入未完成、来源不足、实质模糊、用户明确要求先确认，以及宿主安全或行动授权，仍可阻塞。
- 用户纠正保留旧表达，追加新表达和关系，只使依赖旧理解的临时输出失效。
- AI 默认静默选择呈现形式；只有不同合理解释或形式会实质改变结果时才暴露不确定。
- Recommendation-first 的顺序是：回讲明确内容、指出不确定、说明影响、给出当前判断与建议，只在必要时询问。

## Evidence boundary / 证据边界

Protocol fixtures validate named invariants. Fresh-agent tests with explicit Skill exposure validate conditional Skill behavior. Neither proves a host delivers Readback First by default. Host-level default delivery and action authorization require separate runtime evidence.

协议 fixtures 验证具名不变量；显式暴露 Skill 的 fresh-agent 测试验证条件行为。两者都不能证明宿主默认交付 Readback First。宿主层默认交付与行动授权需要独立运行时证据。

## Out of scope / 范围外

Host adapters, live `CODEX-SETTING`, action-authorization enforcement, push, publish, releases, ASR, input methods, durable ledgers, plugins, and private KO material.

宿主 adapter、live `CODEX-SETTING`、行动授权强制、push、publish、release、ASR、输入法、永久账本、插件及 KO 私有材料均不在本次范围内。
