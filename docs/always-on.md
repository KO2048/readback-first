# Mandatory every-turn host integration

This is a host configuration contract, not an optional invocation suggestion.
The KO deployment requires the host to apply Readback First on every user turn.
Install the Skill, then place this small adapter in the host's always-loaded
instructions. Installation alone is not evidence that the adapter is active.

> For every user input, apply the installed readback-first Skill before
> substantive response or action. Load its SKILL.md and normative PROTOCOL.md
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
> 应用已加载协议，不要求机械重复读文件。先让理解可核对，无阻塞则继续回应。
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
