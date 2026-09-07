# Readback First

**0.5.0 candidate — 自然正文**

先让用户看清 AI 接收到什么，再进行实质回应。回讲保留原意、限定、修正与未决项；
回讲不等于事实核验或行动授权。

[English](README.md) · [协议](PROTOCOL.md) · [本版迭代记录](docs/releases/0.5.0.md) · [版本路线](docs/release-sequence.md)

## 本版解决什么

自然正文。本版基于前一候选逐步演进，不把后续版本能力算作已经完成。

- Deliver natural Markdown in the user’s language instead of machine-record templates.
- Use complete readback-plus-answer examples, with precise exceptions for open/readback-only input.

## 回讲之后，继续回答

**用户：**“我想把回讲迁入 Skill，但每次都要用。你认为可行吗？先别修改。”

回讲：你希望由 Skill 承载详细逻辑，同时保持每次应用；这次只讨论，不修改。

可行。全局入口可以规定每轮应用，Skill 负责回讲的内容与表达。我建议先验证
原意、修正和后续回应是否保留，再替换旧规则，避免只换了文件位置却损失效果。

## 安装与证据

从本候选分支 `codex/release-v05-presentation` 安装仓库根目录中的 Skill，并按宿主要求重新加载。
不要将默认 main 安装误认为安装了本候选。仅安装不证明每轮自动应用。

本版有 **38 个确定性 fixtures**。检查：

```bash
python3 tests/validate_contract.py
python3 tests/validate_fixtures.py
```

这些检查不调用模型。实际回复质量、宿主加载和渲染仍待验证；本版不是已发布稳定版，
没有替换你的全局规则。参见[验证矩阵](tests/runtime-matrix.md)。

[完整示例](examples/before-after.md) · [变更记录](CHANGELOG.md) · Apache-2.0
