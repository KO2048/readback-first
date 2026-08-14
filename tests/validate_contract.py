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

    if failures:
        print("CONTRACT VALIDATION FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("CONTRACT VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
