#!/usr/bin/env python3
"""Validate Readback First failure fixtures with deterministic rules."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ALLOWED_OPEN_STATES = {
    "INPUT_OPEN",
    "RECEPTION_DRAFT",
    "WAITING_FOR_RECEPTION_CONFIRMATION",
}

ARTIFACT_STATE_RANK = {
    "proposed": 0,
    "generated_temp": 1,
    "written_canonical": 2,
    "verified_exists": 3,
    "accessible": 4,
    "published_live": 5,
}


def covered_ids(output: dict[str, Any]) -> set[str]:
    ids = set(output.get("covered_item_ids", []))
    item_range = output.get("covered_item_range")
    if item_range:
        start, end = item_range
        ids.update(f"INFO-{index:04d}" for index in range(start, end + 1))
    return ids


def evaluate(case: dict[str, Any], output: dict[str, Any]) -> set[str]:
    kind = case["failure_mode"]
    codes: set[str] = set()

    if kind == "unauthorized_compression":
        expected = {
            f"INFO-{index:04d}"
            for index in range(1, case["generated_atomic_item_count"] + 1)
        }
        if (
            not case["synthesis_authorized"]
            and covered_ids(output) != expected
        ):
            codes.add("UNAUTHORIZED_COMPRESSION")

    elif kind == "premature_closure":
        if case["input_stage"] == "open" and output["state"] not in ALLOWED_OPEN_STATES:
            codes.add("PREMATURE_CLOSURE")
        if case["input_stage"] == "open" and output.get("declares_complete", False):
            codes.add("PREMATURE_CLOSURE")

    elif kind == "correction_overwrite":
        if not set(case["required_raw_item_ids"]).issubset(
            set(output.get("preserved_raw_item_ids", []))
        ):
            codes.add("RAW_OVERWRITE")
        required_link = case["required_relation"]
        if required_link not in output.get("relations", []):
            codes.add("MISSING_CORRECTION_LINK")

    elif kind == "candidate_as_conclusion":
        if (
            case["source_status"] in {"candidate", "needs_review", "in_progress"}
            and output["rendered_status"] == "confirmed"
            and not output.get("explicit_confirmation_evidence")
        ):
            codes.add("CANDIDATE_PROMOTION")

    elif kind == "qualifier_omission":
        rendered = output.get("rendered_text", "")
        missing = [
            qualifier
            for qualifier in case["required_qualifiers"]
            if qualifier not in rendered
        ]
        if missing:
            codes.add("QUALIFIER_OMISSION")

    elif kind == "invented_intent":
        explicit = set(case["explicit_intents"])
        asserted = set(output.get("asserted_intents", []))
        if not asserted.issubset(explicit):
            codes.add("INVENTED_INTENT")

    elif kind == "summary_only_confirmation":
        if output.get("confirmation_target") != "source_coverage":
            codes.add("SUMMARY_ONLY_CONFIRMATION")
        if not output.get("coverage_item_ids"):
            codes.add("SUMMARY_ONLY_CONFIRMATION")

    elif kind == "direct_answer_gate_bypass":
        if (
            case["direct_answer_requested"]
            and case["high_risk_action"]
            and output.get("bypassed_gates")
        ):
            codes.add("DIRECT_ANSWER_AUTHORITY_BYPASS")

    elif kind == "unresolved_item_disappearance":
        previous = set(case["previous_unresolved_item_ids"])
        carried = set(output.get("carried_item_ids", []))
        resolved = {
            item["item_id"]
            for item in output.get("resolved_items", [])
            if item.get("resolution_evidence") and item.get("provenance")
        }
        if not previous.issubset(carried | resolved):
            codes.add("UNRESOLVED_ITEM_DROPPED")

    elif kind == "unverified_artifact_claim":
        claimed = output["claimed_artifact_state"]
        maximum = case["maximum_proven_state"]
        evidence = output.get("artifact_evidence", {})
        missing_evidence = False

        if ARTIFACT_STATE_RANK[claimed] > ARTIFACT_STATE_RANK[maximum]:
            missing_evidence = True
        if ARTIFACT_STATE_RANK[claimed] >= ARTIFACT_STATE_RANK["written_canonical"]:
            missing_evidence |= not (
                evidence.get("canonical_path") and evidence.get("write_evidence")
            )
        if ARTIFACT_STATE_RANK[claimed] >= ARTIFACT_STATE_RANK["verified_exists"]:
            missing_evidence |= evidence.get("exists_check") is not True
        if ARTIFACT_STATE_RANK[claimed] >= ARTIFACT_STATE_RANK["accessible"]:
            missing_evidence |= evidence.get("access_check") is not True
        if ARTIFACT_STATE_RANK[claimed] >= ARTIFACT_STATE_RANK["published_live"]:
            missing_evidence |= not (
                evidence.get("publish_gate")
                and evidence.get("publish_log")
                and evidence.get("live_hash_match") is True
            )
        if missing_evidence:
            codes.add("UNVERIFIED_ARTIFACT_CLAIM")

    elif kind == "confirmation_semantic_overreach":
        expected = case["expected_confirmation"]
        mismatched = (
            output.get("confirmation_target") != expected["target"]
            or output.get("confirmation_strength") != expected["strength"]
            or set(output.get("confirmation_scope", [])) != set(expected["scope"])
            or set(output.get("accepted_item_ids", []))
            != set(expected["accepted_item_ids"])
            or set(output.get("rejected_item_ids", []))
            != set(expected["rejected_item_ids"])
            or set(output.get("authorized_actions", []))
            != set(expected["authorized_actions"])
            or set(output.get("confirmation_evidence_spans", []))
            != set(expected["evidence_spans"])
        )
        if mismatched:
            codes.add("CONFIRMATION_SEMANTIC_OVERREACH")

    elif kind == "version_coordinate_collapse":
        required = case["required_coordinates"]
        collapsed = any(output.get(key) != value for key, value in required.items())
        collapsed |= output.get("document_version") == output.get("receipt_revision")
        if collapsed:
            codes.add("VERSION_COORDINATE_COLLAPSE")

    elif kind == "locator_scope_collapse":
        collapsed = (
            output.get("semantic_scope") != case["required_scope"]
            or output.get("scope_basis") == "locator"
            or output.get("scanned_full_source") is not True
        )
        if collapsed:
            codes.add("LOCATOR_SCOPE_COLLAPSE")

    elif kind == "ingestion_fidelity_overclaim":
        fidelity = output.get("ingestion_fidelity")
        overclaimed = fidelity not in set(case["allowed_fidelity"])
        if fidelity == "exact_diff" and not case["exact_diff_available"]:
            overclaimed = True
        if not output.get("ingestion_evidence"):
            overclaimed = True
        if overclaimed:
            codes.add("INGESTION_FIDELITY_OVERCLAIM")

    elif kind == "source_synthesis_trace_gap":
        source_ids = set(case["source_item_ids"])
        accounted: set[str] = set()
        trace_gap = False

        for row in output.get("trace_rows", []):
            row_source_ids = set(row.get("source_item_ids", []))
            accounted.update(row_source_ids)
            if row.get("transformation", "").startswith("merged"):
                trace_gap |= len(row_source_ids) < 2
            trace_gap |= not row.get("trace_id") or not row.get("synthesis_target")

        unpropagated = set(output.get("unpropagated_source_item_ids", []))
        exclusions = set(output.get("authorized_exclusions", []))
        accounted.update(unpropagated)
        accounted.update(exclusions)

        reasons = output.get("unpropagated_reasons", {})
        trace_gap |= any(not reasons.get(item_id) for item_id in unpropagated)
        trace_gap |= accounted != source_ids

        if trace_gap:
            codes.add("SOURCE_SYNTHESIS_TRACE_GAP")

    elif kind == "overblocked_closed_request":
        should_block = (
            case["input_state"] == "open"
            or case["unfinished_declared"]
            or case["explicit_reception_completeness_requested"]
            or case["retention_or_conversion_task"]
        )
        if (
            not should_block
            and output.get("gate_action") == "block_for_reception_confirmation"
        ):
            codes.add("OVERBLOCKED_CLOSED_REQUEST")

    else:
        raise ValueError(f"Unknown failure mode: {kind}")

    return codes


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
