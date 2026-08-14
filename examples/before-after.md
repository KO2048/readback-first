# Same-source Before / After

## Original freeform input

> Help me revise the launch plan. We said Friday, but move it to Monday—wait,
> don't change the public date yet. Keep the internal beta on Friday. Do not
> email customers. Pricing probably needs another pass; I haven't decided it.
> I also want the support team prepared, but I'm still thinking about what
> that means.

## Without Readback First

> I'll update the launch plan: internal beta Friday, public launch Monday,
> customer email paused, pricing review added, and support training scheduled.

This sounds reasonable, but it silently:

- turns Monday into a confirmed public date after the user withdrew that change;
- turns an undecided pricing question into a planned review;
- invents support training;
- hides which parts were uncertain.

## With Readback First

```text
Readback

Received
- RBF-001: Revise the launch plan.
  source_state: active
  reception_state: shown
  decision_state: open
- RBF-002: Move the public launch from Friday to Monday.
  source_state: superseded
  reception_state: shown
- RBF-003: Do not change the public launch date yet.
  source_state: active
  reception_state: shown
  decision_state: open
- RBF-004: Keep the internal beta on Friday.
  source_state: active
  reception_state: shown
- RBF-005: Do not email customers.
  source_state: active
  reception_state: shown
  action_authority: not_requested
- RBF-006: Pricing may need more work; no decision yet.
  source_state: active
  reception_state: shown
  decision_state: open
- RBF-007: Prepare support, but the required preparation is not defined.
  source_state: active
  reception_state: shown
  decision_state: open

Relations
- RBF-003 supersedes RBF-002.

Source limit
- The current public launch date was not restated.

State: READBACK_SHOWN
response_route: proceed_with_provisional_response
```

The AI does not label the readback confirmed. Because the source is closed and
the next step is an in-chat draft, it continues with a provisional response:

```text
Provisional launch-plan revision

- DRAFT-01: Internal beta remains Friday.
- DRAFT-02: Public launch date remains open; do not set Monday.
- DRAFT-03: Do not send customer email.
- DRAFT-04: Keep pricing as an unresolved item; do not schedule a review yet.
- DRAFT-05: Keep support preparation open until its meaning is defined.
```

## User interrupt and correction

> The public date staying open is correct. For support, only draft a readiness
> checklist; do not schedule training. Keep everything else unchanged.

## Correction lineage and scoped revision

```text
Readback update

- Preserve RBF-007: the original support requirement was undefined.
- RBF-008 extends RBF-007: draft a support-readiness checklist only.
- RBF-009 extends RBF-008 with an action boundary: do not schedule support
  training.
- DRAFT-05 depends on RBF-007 and is now needs_revision.
- DRAFT-01 through DRAFT-04 remain active.

Reception update
- The user accepted the public-date item in the nearest clear scope.
- The user corrected the support item.
- No file write, message, publication, or other action was authorized.

response_route: proceed_with_provisional_response
```

The revised provisional output changes only the dependent line:

```text
- DRAFT-05-R1: Draft a support-readiness checklist; do not schedule training.
```

The earlier source remains traceable. The correction does not silently confirm
every item, and continuing the in-chat draft does not authorize editing files,
sending messages, or publishing.
