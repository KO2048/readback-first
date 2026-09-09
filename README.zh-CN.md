# Readback First

**0.10.2 — 分批交付与提交追溯**

先让用户看清 AI 接收到什么，再进行实质回应。回讲保留原意、限定、修正与未决项；
回讲不等于事实核验或行动授权。

[English](README.md) · [协议](PROTOCOL.md) · [本版迭代记录](docs/releases/0.10.2.md) · [版本路线](docs/release-sequence.md)

## 本版更新什么

- 新增[逐项交付台账](docs/delivery-ledger.md)：Issue、改动commit、合并commit、PR、版本与待验收项。
- 明确中文为主的提交约定，区分行为修改、示例、测试和文档交付。
- 本版是文档补丁，行为契约继承v0.10.0，不宣称新增模型能力。

## 回讲之后，继续回答

**用户：**“我想把回讲迁入 Skill，但每次都要用。你认为可行吗？先别修改。”

回讲：你希望由 Skill 承载详细逻辑，同时保持每次应用；这次只讨论，不修改。

可行。全局入口可以规定每轮应用，Skill 负责回讲的内容与表达。我建议先验证
原意、修正和后续回应是否保留，再替换旧规则，避免只换了文件位置却损失效果。

## 安装最新版

默认 `main` 已包含 **v0.10.2**。可以直接对 Agent 说：

> 从 https://github.com/KO2048/readback-first 的 main 分支安装仓库根目录中的 Skill，
> 名称为 readback-first。如果已经安装，先保留本地改动，再更新到最新版。

全新 Codex 安装也可以使用：

```bash
git clone --branch main --depth 1 https://github.com/KO2048/readback-first.git ~/.codex/skills/readback-first
```

已有目录不要直接覆盖。Git 安装先检查本地改动，再在安装目录执行
`git pull --ff-only origin main`；其他安装方式交由 Agent／安装器更新。
按宿主要求重新加载或新开会话，并检查 `release.json` 中的版本为 `0.10.2`。

要求**每条输入都应用**时，将[强制宿主入口](docs/always-on.md)放入宿主始终加载的规则。
安装 Skill 与配置这个入口分别完成；需要固定版本时使用
[v0.10.2 发布快照](https://github.com/KO2048/readback-first/releases/tag/v0.10.2)。

## 验证与限制

本版有 **39 个确定性 fixtures**。检查：

```bash
python3 tests/validate_contract.py
python3 tests/validate_fixtures.py
```

这些检查不调用模型。跨模型实际回复质量、宿主加载和渲染仍待验证。本版发布协议与 Skill 实现，
不宣称跨模型可靠性已证明，也不会静默替换你的全局规则。参见[验证矩阵](tests/runtime-matrix.md)。

[完整示例](examples/before-after.md) · [变更记录](CHANGELOG.md) · Apache-2.0

## Semantic views / 语义视图

```mermaid
flowchart LR
    A[Source meaning] --> B[Inspectable readback]
    B --> C[Useful response]
```

Use different diagrams for different relationships; inferred links need labels.
根据不同关系分别选图；推测关系必须标识。See examples/before-after.md.

[Mandatory every-turn adapter / 每轮强制入口](docs/always-on.md)

[对齐状态 / Alignment status](docs/alignment-status.md) · [原题与累计稿](examples/identity-current-view.md) · [未决交接](examples/unresolved-lineage.md) · [跨题更新](examples/cognition-evidence.md)

[本版示例 / Worked example](examples/formal-receipt-first.md) · [本版实际观察 / Runtime observations](docs/evaluation/formal-delivery/review.md)

## 必须完成常驻入口安装

仅复制 Skill 不等于默认每轮启用。Codex 安装或更新包后执行：

```bash
python3 ~/.codex/skills/readback-first/scripts/enable_always_on.py --skill-dir ~/.codex/skills/readback-first --rules-file ~/.codex/AGENTS.md
```

安装器保留原治理、修改前备份、重复运行不重复追加。WorkBuddy 等宿主需指定经过核实的常驻规则文件；仅提供规则界面的宿主粘贴 docs/always-on.md 的入口。不得猜测路径。重新加载或新建会话后生效；配置完成不等于已证明所有模型和界面的执行效果。
