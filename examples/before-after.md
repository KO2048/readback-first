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
- RB-001 [confirmed request]: Revise the launch plan.
- RB-002 [superseded]: Move the public launch from Friday to Monday.
- RB-003 [confirmed correction]: Do not change the public launch date yet.
- RB-004 [confirmed request]: Keep the internal beta on Friday.
- RB-005 [constraint]: Do not email customers.
- RB-006 [needs_review]: Pricing probably needs another pass; no decision yet.
- RB-007 [in_progress]: Prepare support, but the required preparation is not
  defined yet.

Relations
- RB-003 supersedes RB-002.

Possible omission
- The current public launch date was not restated.

State: WAITING_FOR_CONFIRMATION
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

Only after this alignment should the AI draft the revised plan. Editing files,
sending messages, or publishing still requires separate authorization.
