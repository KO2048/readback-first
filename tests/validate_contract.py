#!/usr/bin/env python3
"""Validate the public Readback First protocol and Skill contract."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(text: str, needle: str, source: str, failures: list[str]) -> None:
    if needle not in text:
        failures.append(f"{source}: missing {needle!r}")


def read_required(path: Path, source: str, failures: list[str]) -> str:
    if not path.exists():
        failures.append(f"{source}: missing required file")
        return ""
    return path.read_text(encoding="utf-8")


def main() -> int:
    failures: list[str] = []
    protocol_path = ROOT / "PROTOCOL.md"
    skill_path = ROOT / "SKILL.md"
    example_path = ROOT / "examples" / "before-after.md"
    metadata_path = ROOT / "agents" / "openai.yaml"
    readme_path = ROOT / "README.md"
    readme_zh_path = ROOT / "README.zh-CN.md"
    changelog_path = ROOT / "CHANGELOG.md"
    tests_readme_path = ROOT / "tests" / "README.md"

    protocol = read_required(protocol_path, "PROTOCOL.md", failures)
    if protocol:
        for needle in (
            "Readback is the core",
            "Default readback",
            "Visible working understanding",
            "Source state",
            "Reception state",
            "Decision state",
            "Action authority",
            "READBACK_SHOWN",
            "response_route",
            "proceed_with_provisional_response",
            "dependent provisional output",
            "needs_revision",
            "re-evaluate the blocking predicates",
            "Silent adaptation",
            "recommendation-first",
            "low-impact uncertainty",
            "material uncertainty",
            "Overview is navigation",
            "WAITING_FOR_RECEPTION_CONFIRMATION",
            "confirmation_depth",
            "reception_coverage",
            "minto_pyramid",
            "Current-session boundary",
            "Migration from 0.2 to 0.3",
        ):
            require(protocol, needle, "PROTOCOL.md", failures)

    skill = read_required(skill_path, "SKILL.md", failures)
    for needle in (
        "Default readback",
        "Readback shown is not reception confirmed",
        "source_state",
        "reception_state",
        "decision_state",
        "action_authority",
        "organization_method",
        "minto_pyramid",
        "WAITING_FOR_RECEPTION_CONFIRMATION",
        "response_route",
        "proceed_with_provisional_response",
        "in-chat provisional",
        "dependent provisional output",
        "needs_revision",
        "re-evaluate the blocking predicates",
        "Silent adaptation",
        "recommendation-first",
        "low-impact uncertainty",
        "material uncertainty",
        "Overview is navigation",
        "reception_coverage",
    ):
        require(skill, needle, "SKILL.md", failures)

    example = read_required(example_path, "examples/before-after.md", failures)
    metadata = read_required(metadata_path, "agents/openai.yaml", failures)
    readme = read_required(readme_path, "README.md", failures)
    readme_zh = read_required(readme_zh_path, "README.zh-CN.md", failures)
    changelog = read_required(changelog_path, "CHANGELOG.md", failures)
    tests_readme = read_required(tests_readme_path, "tests/README.md", failures)

    forbidden = {
        "SKILL.md": (
            (skill, "WAITING_FOR_CONFIRMATION"),
            (skill, "source_coverage"),
            (skill, "[confirmed request]"),
            (skill, "[confirmed correction]"),
            (skill, "State the chosen presentation **after**"),
            (skill, "You can ask for compact/standard"),
            (skill, "Adjust: compact/standard"),
        ),
        "PROTOCOL.md": (
            (protocol, "must state the selected presentation"),
            (protocol, "still speaking, adding, correcting"),
        ),
        "examples/before-after.md": (
            (example, "[confirmed request]"),
            (example, "[confirmed correction]"),
            (example, " constrains "),
        ),
        "README.md": (
            (readme, "Confirm what AI will use"),
            (readme, "WAITING_FOR_CONFIRMATION"),
        ),
    }
    for source, checks in forbidden.items():
        for text, needle in checks:
            if needle in text:
                failures.append(f"{source}: forbidden legacy contract {needle!r}")

    for needle in (
        "visible working understanding",
        "default readback",
        "normally continue",
        "confirmation",
        "authorization",
    ):
        require(metadata.lower(), needle, "agents/openai.yaml", failures)

    for needle in (
        "proceed_with_provisional_response",
        "needs_revision",
        "reception_state: shown",
    ):
        require(example, needle, "examples/before-after.md", failures)

    require(changelog, "0.3.0 (candidate)", "CHANGELOG.md", failures)
    require(
        changelog,
        "0.2.0 (candidate)",
        "CHANGELOG.md",
        failures,
    )
    require(tests_readme, "39 deterministic fixtures", "tests/README.md", failures)

    import json
    meta = json.loads((ROOT / "release.json").read_text())
    expected = meta["version"].rsplit(".", 1)[0]
    require(protocol, "Protocol Version: " + expected, "PROTOCOL.md", failures)
    require(skill, "Protocol version: " + expected, "SKILL.md", failures)
    require(skill, "[release.json](release.json)", "SKILL.md", failures)
    require(protocol, "[release.json](release.json)", "PROTOCOL.md", failures)
    actual_count = len(list((ROOT / "tests/fixtures").glob("*.json")))
    if actual_count != meta["fixture_count"]:
        failures.append("release.json: fixture count mismatch")
    for name in ("README.md", "README.zh-CN.md", "CHANGELOG.md"):
        require((ROOT / name).read_text(), meta["version"], name, failures)
    note = ROOT / "docs/releases" / (meta["version"] + ".md")
    if not note.exists():
        failures.append("missing version-specific iteration record")
    for needle in ("wait_for_input", "wait_for_clarification", "readback_only"):
        require(skill, needle, "SKILL.md", failures)
    for needle in ("Reader-facing response", "user's language", "substantive"):
        require(skill, needle, "SKILL.md", failures)
    for needle in ("Multiple semantic views", "sequenceDiagram", "stateDiagram-v2"):
        require(skill, needle, "SKILL.md", failures)
    if not (ROOT / "docs/always-on.md").exists():
        failures.append("missing mandatory host adapter")

    if failures:
        print("CONTRACT VALIDATION FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("CONTRACT VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
