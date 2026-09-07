#!/usr/bin/env python3
"""Run deterministic Readback First good/bad protocol fixtures."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from protocol_rules import evaluate


def validate_case(path: Path) -> list[str]:
    case = json.loads(path.read_text(encoding="utf-8"))
    failures: list[str] = []

    for variant_name in ("bad_output", "good_output"):
        variant = case[variant_name]
        actual = evaluate(case, variant)
        expected = set(variant["expected_failure_codes"])
        if actual != expected:
            failures.append(
                f"{case['id']}:{variant_name}: expected={sorted(expected)} "
                f"actual={sorted(actual)}"
            )

    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--fixtures",
        type=Path,
        default=Path(__file__).parent / "fixtures",
    )
    args = parser.parse_args()

    fixture_paths = sorted(args.fixtures.glob("*.json"))
    if not fixture_paths:
        print("FAILED: no fixtures found")
        return 1

    failures: list[str] = []
    for path in fixture_paths:
        failures.extend(validate_case(path))

    if failures:
        print("FIXTURE VALIDATION FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"FIXTURE VALIDATION PASSED: {len(fixture_paths)} cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
