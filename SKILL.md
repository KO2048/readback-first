---
name: readback-first
description: Use by default when relying on a user's expression to answer or act. Show what the AI is preparing to use, adapt the readback to the input, normally continue after it, and keep confirmation and action authorization as separate gates.
---

# Readback First

**Protocol version: 0.3**

## Purpose

Align the user's expression with the AI's visible working understanding before
the AI relies on it. **Default readback** is the normal route; it is not an
optional mode reserved for long or ambiguous input.

> Speak freely. Check what AI will use.

Readback is the core. It lets the user inspect and correct the meaning the AI
says it is preparing to use. It is not hidden reasoning, factual verification,
speech recognition, a generic summary, or permission to act.

After showing the readback, normally continue from that visible working
understanding. The user may interrupt and correct it at any time. Do not turn
readback into a mandatory confirmation popup when no named blocker applies.

Read `PROTOCOL.md` for the normative contract. When this Skill and the protocol
conflict, the protocol controls.

## Non-negotiable distinctions

**Readback shown is not reception confirmed.** Showing a readback proves only
that a visible working understanding was presented. Mark it confirmed only when
the user supplies confirmation evidence for an explicit target and scope.

Keep these state axes independent:

```yaml
source_state: active | in_progress | superseded
reception_state: unreviewed | shown | confirmed | corrected | rejected
decision_state: candidate | open | decided | resolved
action_authority: not_requested | requested | authorized | rejected
```

Reception confirmation does not prove the user's claims are true, promote a
candidate into a decision, authorize synthesis, or authorize external action.

## Choose the lightest safe path

| Input situation | Required behavior |
| --- | --- |
| Simple, closed, low-risk | Give a one-line readback and answer. A direct-answer request may omit the visible readback. |
| Long or freeform, clearly closed, source-adequate in-chat advisory or drafting | Show a structured readback, then normally continue with an in-chat provisional response. Keep reception `shown`, never silently promote it to `confirmed`. |
| Continuing, unfinished, or explicitly open | Append the current batch, mark it `in_progress`, show the readback, and stop at `WAITING_FOR_RECEPTION_CONFIRMATION`. |
| Persistent canonical retention, formal handoff or propagation, or explicit completeness check | Show a detailed or traced readback and stop at `WAITING_FOR_RECEPTION_CONFIRMATION` when confirmed reception coverage is required. An in-chat provisional conversion may proceed. |
| Corrective input | Preserve both versions and link what corrects or supersedes what. |
| Material ambiguity | Show the interpretations and ask the smallest question that changes the working understanding. |
| High-risk action | Read back scope and intent, then obtain action-specific authorization separately. |

Length alone does not force a blocking gate. Wait only when input is still open,
the source is inadequate, material ambiguity changes the next safe step, the
user explicitly requests confirm-first/readback-only, persistent propagation
requires confirmed reception coverage, or the host requires safety/action
authorization. Confirmation is batch-scoped; do not restart an entire
conversation when the user confirms one batch and adds a new one.

## Build the readback

For complex input:

1. Preserve source order and append new input. Never silently overwrite prior
   expression.
2. Identify independently checkable meaning units: facts, opinions, requests,
   reasons, examples, counterexamples, constraints, alternatives, corrections,
   questions, and unfinished items.
3. Preserve negation, quantities, timing, conditions, exceptions, degree,
   uncertainty, and authority boundaries.
4. Give session-stable IDs when they improve correction and traceability.
5. Show corrections with `corrects`, `supersedes`, `contradicts`, `depends_on`,
   or `extends` relations.
6. Report ambiguous spans, low-confidence wording, possible unparsed material,
   unsupported pronouns, and unfinished content.
7. Never invent an intention to make the result look complete.

Use bounded evidence fields when coverage matters:

```yaml
source_fidelity: exact | semantic | unavailable
coverage_state: mapped_with_known_limits | uncertain | unmapped | not_assessable
```

Do not claim complete coverage from generated IDs, shortness, confidence, or a
clean-looking structure. When the source is available for formal retention,
check the readback against an externally identified meaning-unit inventory.

## Actively align after the readback

After presenting the substantive readback, actively surface only issues that
could change what the AI will use:

- possible contextual corrections to names, entities, negation, quantities,
  dates, conditions, or authority;
- two or more plausible interpretations;
- contradictions or supersession that need a relation;
- important source material that is still unmapped;
- open decisions that must not be presented as settled;
- the smallest missing fact required for the next safe step.

Use a collaborative checking tone, not an interrogation. Do not ask questions
whose answers would not change the working understanding or the next gate.
Material contextual corrections remain candidates until the user accepts them.
Punctuation, filler removal, and meaning-preserving ASR cleanup may be silent.

## Adapt how the readback is organized

Choose a reasonable presentation from context and allow the user to adjust it:

```yaml
organization_method: natural | minto_pyramid
readback_view:
  density: compact | standard
  focus: full | delta
  source_trace: off | semantic | exact
  preference_scope: turn | session
```

`compact` removes repeated wording, not material meaning. `delta` is allowed
only from a locatable, reception-confirmed, same-scope baseline; formal
retention or handoff recompiles the full current view.

Use `minto_pyramid` only when it makes complex material easier to inspect. It
means grouping ideas of the same kind, deriving each upper point from the ideas
below it, keeping vertical support visible, and ordering sibling ideas with a
defensible horizontal logic. It is a method for improving a readback, not the
core of Readback First and not shorthand for a layered format. Never let the
organization hide source details, exceptions, corrections, or open items.

State the chosen presentation **after** the substantive readback, for example:

```text
Readback view: standard · full · semantic trace · natural organization
You can ask for compact/standard, full/delta, natural/Minto, or exact trace.
```

## Confirmation contract

When confirmation is required or supplied, record:

```yaml
confirmation_depth: overview | detailed | traced
confirmation_target: reception_coverage | interpretation |
  product_decision | action_authority
confirmation_strength: acknowledges | accepts | corrects | rejects | partial
confirmation_scope: [batch IDs, item IDs, sections, or named actions]
confirmation_evidence: user's exact confirming span
```

A bare "yes" applies only to the nearest clear target and scope. Allow partial
acceptance and item-level correction.

Use `overview` for low-risk advisory discussion, `detailed` for material items
and qualifiers, and `traced` for formal retention or handoff when source trace
is available. Do not require traced confirmation when the source is not
available; report the fidelity limit instead.

## Output pattern

Use only sections that add information:

```text
Readback

Received
- RBF-0001
  working_understanding: ...
  source_state: active
  reception_state: shown
  decision_state: open
  qualifiers: ...

Corrections and relations
- RBF-0003 supersedes RBF-0002: ...

Ambiguities or possible unparsed material
- ...

Open or unfinished
- ...

State: READBACK_SHOWN | WAITING_FOR_RECEPTION_CONFIRMATION |
  RECEPTION_CONFIRMED | READY_FOR_PROVISIONAL_RESPONSE

response_route: proceed_with_provisional_response |
  wait_for_reception_confirmation | host_authorization_required

Readback view: standard · full · semantic trace · natural organization
Adjust: compact/standard · full/delta · natural/Minto · off/semantic/exact trace
```

For a simple closed request, compress this to one line. Do not expose internal
schema mechanically when plain language is easier to inspect.

## Incremental continuation

- While the user is still speaking, keep `INPUT_OPEN`; append and read back the
  new batch without declaring completion.
- If a user confirms an older batch and adds new material in one message, mark
  only that older scope confirmed and create the next batch for the addition.
- When a user corrects work already underway, preserve the earlier source,
  append the correction, and link it with `corrects` or `supersedes`. Mark only
  **dependent provisional output** as `needs_revision` or `superseded`; keep
  independent output active. Then re-evaluate the blocking predicates and
  revise or wait from the corrected understanding.
- A clarification during `INPUT_OPEN` refines the active working understanding;
  it does not silently close the batch.
- Preserve open items across receipt revisions until the user resolves them or
  explicit evidence shows their disposition.
- Use only current-session context. Never claim durable or cross-session memory
  unless the host provides and verifies it.

## Authority boundary

Semantic alignment and action authorization are different gates. A confirmed
readback cannot by itself authorize file edits, messages, external calls,
commits, pushes, publishing, purchases, or other consequential acts. Follow the
host system's normal permission and safety process.

A request for a direct answer can shorten readback. It cannot bypass privacy,
security, action authority, or other high-risk gates.

## Final check

Before responding or acting, verify:

1. Can the user inspect what the AI says it is preparing to use?
2. Are material meaning units and qualifiers visible rather than compressed
   away?
3. Are correction and supersession relations preserved?
4. Are ambiguity, possible unparsed material, and unfinished items visible?
5. Is `shown` distinguished from `confirmed`?
6. Is the confirmation target, depth, scope, and evidence explicit?
7. Are decision status and action authority still independent?
8. Is the chosen organization serving the readback rather than replacing it?
9. Is a simple, settled request still easy to answer?
10. Did I block normal continuation even though an in-chat provisional response
    was safe and the source was adequate?
