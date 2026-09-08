# 候选版本读取复核

Issue #24. After the version-reference clarification, the same participant was
asked to read the candidate directory entry and its linked version material,
report package/protocol versions, and distinguish candidate from global install.
This was a targeted reference lookup, not an isolated efficacy test.

实际回复摘录（仅省略原回复中的本机绝对路径链接）：

> 候选安装包版本：0.8.2，依据 release.json。
> 协议版本：0.8，依据 SKILL.md；入口明确说明它与安装包版本是独立版本标识。
> 元数据虽写有 status: release 和发布链接，但这不足以证明候选目录已经发布或安装。
> 不能由该目录判断当前全局安装版本；需要另行核对全局安装位置的版本资料。

人工核对：候选release.json确为0.8.2，协议为0.8；没有把候选目录当成全局安装。
该复核只证明指定材料的读取结果；真实安装由发布后逐文件校验另行证明。
