#!/usr/bin/env python3
"""Install the persistent entry after installing/updating the Skill package."""
import argparse
import json
import os
from pathlib import Path
import tempfile
import time

START = '<!-- readback-first:begin -->'
END = '<!-- readback-first:end -->'


def enable(skill, rules):
    skill, rules = Path(skill).expanduser().resolve(), Path(rules).expanduser()
    # Do not silently redirect a managed host entry through a symlink.
    if rules.is_symlink():
        raise ValueError('Rules file is a symlink; select its managed source explicitly')
    rules = rules.resolve()
    for name in ('SKILL.md', 'PROTOCOL.md', 'release.json'):
        if not (skill / name).is_file():
            raise ValueError('Missing installed dependency: ' + name)
    version = json.loads((skill / 'release.json').read_text())['version']
    old = rules.read_text() if rules.exists() else ''
    if old.count(START) != old.count(END) or old.count(START) > 1:
        raise ValueError('Malformed adapter markers; refusing to replace existing rules')
    block = f'''{START}
## Readback First — mandatory every-turn entry
Installed Skill: {skill} (package {version}).
Before every substantive answer or task tool, apply this Skill. Load
{skill / 'SKILL.md'} and {skill / 'PROTOCOL.md'} on first use,
after updates or context loss; reuse the loaded rules on subsequent turns.
Begin with a substantive receipt in the user's language in the normal conversation
body: what the user requests, relevant constraints and material uncertainty.
Thinking, tool logs, collapsed progress and an action notice do not count.
Retain the necessary receipt in the final answer, then continue the authorized
work without requesting confirmation again unless a named blocker applies.
Respect explicit direct-answer and readback-only requests and host safety rules.
If loading fails, report the missing dependency; never claim the Skill ran.
If the host cannot render a persistent pre-tool message, state that limitation
in the normal answer before task execution; do not claim display compliance.
Preserve existing governance until replacement is independently validated.
每轮默认先在正式正文回讲，再继续；不得只在思考或折叠进度里回讲。
{END}'''
    if START in old:
        a, b = old.index(START), old.index(END)
        if b < a:
            raise ValueError('Reversed adapter markers')
        new = old[:a] + block + old[b + len(END):]
    else:
        new = old + ('\n\n' if old else '') + block + '\n'
    if new == old:
        return 'unchanged'
    rules.parent.mkdir(parents=True, exist_ok=True)
    mode = rules.stat().st_mode & 0o777 if rules.exists() else 0o600
    if rules.exists():
        backup = rules.with_name(rules.name + '.readback-backup-' + str(time.time_ns()))
        with backup.open('x') as f:
            f.write(old)
        backup.chmod(mode)
    fd, temp = tempfile.mkstemp(prefix='.readback-', dir=rules.parent)
    try:
        with os.fdopen(fd, 'w') as f:
            f.write(new)
        os.chmod(temp, mode)
        os.replace(temp, rules)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)
    return 'configured; reload/start a fresh session; runtime activation remains to be verified'


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--skill-dir', required=True)
    p.add_argument('--rules-file', required=True, help='Verified always-loaded host instruction file')
    args = p.parse_args()
    try:
        print(enable(args.skill_dir, args.rules_file))
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as e:
        p.exit(1, str(e) + '\n')
