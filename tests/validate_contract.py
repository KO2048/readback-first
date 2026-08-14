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
            "Protocol Version: 0.3",
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
            "WAITING_FOR_RECEPTION_CONFIRMATION",
            "confirmation_depth",
            "reception_coverage",
            "minto_pyramid",
            "Current-session boundary",
        ):
            require(protocol, needle, "PROTOCOL.md", failures)

    skill = skill_path.read_text(encoding="utf-8")
    for needle in (
        "Protocol version: 0.3",
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

    if failures:
        print("CONTRACT VALIDATION FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("CONTRACT VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
