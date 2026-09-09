# Mandatory every-turn host integration

This is a host configuration contract, not an optional invocation suggestion.
The KO deployment requires the host to apply Readback First on every user turn.
Install the Skill, then place this small adapter in the host's always-loaded
instructions. Installation alone is not evidence that the adapter is active.

> For every user input, apply the installed readback-first Skill before
> substantive response or task tool. The first task content MUST be a substantive
> receipt in the formal conversation body, visible without expanding thinking,
> progress, status or tool panels. An action notice is not a receipt. Load its SKILL.md and normative PROTOCOL.md
> before first use, and after version changes or context loss. Reuse the loaded
> contract on subsequent turns; every-turn application does not require redundant
> file reads. Make the user's meaning visibly checkable, then continue with the
> requested response when no named blocker applies. Follow explicit direct-answer
> or readback-only requests according to the Skill. Preserve host safety and
> existing authorization. If the required Skill cannot be loaded, report the
> missing dependency; do not silently downgrade to optional activation or claim
> that it ran. Retain the current governing reception rules until replacement
> has been validated.

中文等价入口：

> 每条用户输入都必须应用已安装的 readback-first，再进行实质回应或行动。
> 首次使用、版本变化或上下文丢失后读取 SKILL.md 与 PROTOCOL.md；后续每轮
> 应用已加载协议，不要求机械重复读文件。每轮首个任务内容必须在正式对话正文
> 回讲用户请求、范围与已知未决项，再调用任务工具或回答。思考区、工具日志、
> 折叠状态、仅进度区文字不算；“我先核对一下”不替代实质回讲。无阻塞则继续回应。
> 直答、只回讲按 Skill 处理，保留宿主权限与已有授权。加载失败应明确报告，
> 不得静默降为可选触发或声称已调用。替换验证通过前保留现有接收规则。

The readback Skill is the designated entry procedure, so loading it is permitted
before its first receipt; other autonomous tools follow the receipt. This removes
an accidental bootstrap cycle in rules saying 'read back before selecting any Skill'.

## Deployment evidence

Record Skill version/hash, host adapter text, host/model, fresh-session loading
trace, ordinary next-turn activation, direct-answer handling, context reload,
and a missing-Skill case. Test without competing legacy reception instructions,
then compare against the legacy arm in a separate session. Never claim a static
adapter proves turn-by-turn runtime compliance. This change supplies the adapter;
it does not install it globally or attest WorkBuddy/Codex behavior.

## Required delivery mapping / 正式消息映射

The adapter must deliver the initial receipt as an ordinary conversation message,
retain it visibly after tool work, and include necessary receipt content in the
final answer. Rendering a model commentary event only as a progress panel fails
this contract. Do not label it a formal message merely because the model emitted it.

适配器必须让前置回讲成为正式对话消息，工具执行后仍可直接查看，最终正文也保留
必要回讲。若只能输出折叠进度区，应先在正常答复里回讲并说明适配限制；不能暗中
先执行任务或宣称符合。不要要求用户反复说“先回讲”来弥补入口缺失。

| Host surface | Requirement | Evidence to retain |
| --- | --- | --- |
| Desktop / web chat | Normal assistant message before task tools, visible after completion | Rendered transcript or UI observation plus ordered events |
| CLI / IDE | Persistent conversation output, distinct from reasoning/debug/status | Normal output and ordered tool events |
| Agent wrapper / SDK | Route receipt to the end-user conversation before invoking task tools | Wrapper routing plus observed client display |
| Unknown or unsupported | Unverified/unsupported; never claim a pass | Exact limitation; receipt in normal answer before task execution |

These are requirements for all hosts, not claims that those hosts passed tests.
Use ordinary prompts without “read back” hints. Test first turn, follow-up,
context reload, task-tool use, final retention and explicit no-readback handling.
Record package hash, loaded contract, event order and actual display mapping.
Do not infer UI visibility from channel names or `readback_shown=true`.

## Required installation: global, default and persistent

Global deployment and persistent every-turn activation are REQUIRED parts of
installation, not optional modes. Install the package in the host's user-global
Skill location AND connect it to the verified user-global, always-loaded
instruction entry. A project-only copy or a one-session invocation does not
complete the default installation. An explicit user request for a narrower
scope is respected and reported as a scoped deployment, not global installation.

The installing agent MUST complete both steps within the user's authorized
installation scope, preserving unrelated rules and backing up edits. Do not stop
at downloading files or ask the user to invoke the Skill on each turn. For Codex,
run scripts/enable_always_on.py with the installed Skill directory and
~/.codex/AGENTS.md. For other hosts, verify the real global rule surface rather
than inventing a path. If permission or host support is missing, report the exact
incomplete step; never report installation complete.

Persistent means the global entry survives application restarts and applies to
new conversations and subsequent user turns without a wake phrase. It does not
mean a background daemon or guaranteed memory across conversations. Reload the
protocol when context is lost; honor explicit disable/direct-answer requests.

Installation acceptance requires a fresh ordinary conversation, a follow-up,
and a new conversation after restarting/reloading the host: observe formal-body
readback before task tools and useful continuation, without a Skill mention in
the test prompts. Record loading and visible-output evidence. Report package
installed, global entry configured, and behavior verified separately. Until the
last check succeeds, report setup as configured but activation unverified.
