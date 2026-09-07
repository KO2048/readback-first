#!/usr/bin/env python3
"""Validate the public Readback First protocol and Skill contract."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(text: str, needle: str, source: str, failures: list[str]) -> None:
    if needle not in text:
        failures.append(f"{source}: missing {needle!r}")


def main() -> int:
    failures: list[str] = []
    protocol_path = ROOT / "PROTOCOL.md"
    skill_path = ROOT / "SKILL.md"
    example_path = ROOT / "examples" / "before-after.md"
    metadata_path = ROOT / "agents" / "openai.yaml"

    if not protocol_path.exists():
        failures.append("PROTOCOL.md: missing normative protocol")
    else:
        protocol = protocol_path.read_text(encoding="utf-8")
        for needle in (
            "Protocol Version: 0.2",
            "Readback is the core",
            "Visible working understanding",
            "Source state",
            "Reception state",
            "Decision state",
            "Action authority",
            "READBACK_SHOWN",
            "WAITING_FOR_RECEPTION_CONFIRMATION",
            "confirmation_depth",
            "reception_coverage",
            "minto_pyramid",
            "Current-session boundary",
        ):
            require(protocol, needle, "PROTOCOL.md", failures)

    skill = skill_path.read_text(encoding="utf-8")
    for needle in (
        "Protocol version: 0.2",
        "Readback shown is not reception confirmed",
        "source_state",
        "reception_state",
        "decision_state",
        "action_authority",
        "organization_method",
        "minto_pyramid",
        "WAITING_FOR_RECEPTION_CONFIRMATION",
        "reception_coverage",
    ):
        require(skill, needle, "SKILL.md", failures)

    example = example_path.read_text(encoding="utf-8")
    metadata = metadata_path.read_text(encoding="utf-8")

    forbidden = {
        "SKILL.md": (
            (skill, "WAITING_FOR_CONFIRMATION"),
            (skill, "source_coverage"),
            (skill, "[confirmed request]"),
            (skill, "[confirmed correction]"),
        ),
        "examples/before-after.md": (
            (example, "[confirmed request]"),
            (example, "[confirmed correction]"),
        ),
    }
    for source, checks in forbidden.items():
        for text, needle in checks:
            if needle in text:
                failures.append(f"{source}: forbidden legacy contract {needle!r}")

    for needle in (
        "visible working understanding",
        "confirmation",
        "authorization",
    ):
        require(metadata.lower(), needle, "agents/openai.yaml", failures)

    import json
    meta = json.loads((ROOT / "release.json").read_text())
    expected = meta["version"].rsplit(".", 1)[0]
    require(protocol, "Protocol Version: " + expected, "PROTOCOL.md", failures)
    require(skill, "Protocol version: " + expected, "SKILL.md", failures)
    actual_count = len(list((ROOT / "tests/fixtures").glob("*.json")))
    if actual_count != meta["fixture_count"]:
        failures.append("release.json: fixture count mismatch")
    for name in ("README.md", "README.zh-CN.md", "CHANGELOG.md"):
        require((ROOT / name).read_text(), meta["version"], name, failures)
    note = ROOT / "docs/releases" / (meta["version"] + ".md")
    if not note.exists():
        failures.append("missing version-specific iteration record")

    if failures:
        print("CONTRACT VALIDATION FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("CONTRACT VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
