# Readback First

**0.3.0 candidate — 回讲后继续回应**

先让用户看清 AI 接收到什么，再进行实质回应。回讲保留原意、限定、修正与未决项；
回讲不等于事实核验或行动授权。

[English](README.md) · [协议](PROTOCOL.md) · [本版迭代记录](docs/releases/0.3.0.md) · [版本路线](docs/release-sequence.md)

## 本版解决什么

回讲后继续回应。本版基于前一候选逐步演进，不把后续版本能力算作已经完成。

- Apply readback by default when loaded, then normally continue.
- Invalidate only output depending on a correction; avoid unnecessary confirmation loops.

## 安装与证据

从本候选分支 `codex/release-v03-continuation` 安装仓库根目录中的 Skill，并按宿主要求重新加载。
不要将默认 main 安装误认为安装了本候选。仅安装不证明每轮自动应用。

本版有 **33 个确定性 fixtures**。检查：

```bash
python3 tests/validate_contract.py
python3 tests/validate_fixtures.py
```

这些检查不调用模型。实际回复质量、宿主加载和渲染仍待验证；本版不是已发布稳定版，
没有替换你的全局规则。参见[验证矩阵](tests/runtime-matrix.md)。

[完整示例](examples/before-after.md) · [变更记录](CHANGELOG.md) · Apache-2.0
