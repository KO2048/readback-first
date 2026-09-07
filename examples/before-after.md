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
- RBF-006: Pricing probably needs another pass; no decision yet.
  source_state: active
  reception_state: shown
  decision_state: open
- RBF-007: Prepare support, but the required preparation is not defined yet.
  source_state: in_progress
  reception_state: shown
  decision_state: open

Relations
- RBF-003 supersedes RBF-002.

Possible omission
- The current public launch date was not restated.

State: WAITING_FOR_RECEPTION_CONFIRMATION

Readback view: standard · full · semantic trace · natural organization
```

## User correction

> Correct. The public date stays unconfirmed. For support, only draft a
> checklist; don't schedule training.

## Confirmed input

```text
- Revise the launch plan.
- Keep the internal beta on Friday.
- Leave the public launch date unconfirmed.
- Do not email customers.
- Keep pricing as an unresolved item.
- Draft a support-readiness checklist; do not schedule training.
```

Confirmation record:

```yaml
confirmation_depth: detailed
confirmation_target: reception_coverage
confirmation_strength: corrects
confirmation_scope: [RBF-001, RBF-003, RBF-004, RBF-005, RBF-006, RBF-007]
confirmation_evidence: >
  Correct. The public date stays unconfirmed. For support, only draft a
  checklist; don't schedule training.
```

Only after this alignment should the AI draft the revised plan. Editing files,
sending messages, or publishing still requires separate authorization.
