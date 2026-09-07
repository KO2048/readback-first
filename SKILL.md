---
name: readback-first
description: Use by default when relying on a user's expression to answer or act. Show what the AI is preparing to use, adapt the readback to the input, normally continue after it, and keep confirmation and action authorization as separate gates.
---

# Readback First

**Protocol version: 0.6**

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
| Continuing, unfinished, or explicitly open | Append the current batch, mark it `in_progress`, show the readback, and use `wait_for_input` to invite continuation, not confirmation. |
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

Check uncertainty in this order: input completion, source adequacy, semantic
ambiguity, then output-form uncertainty. For **low-impact uncertainty** that is
reversible and has a dominant contextual interpretation, state the working
assumption and what the alternative would change, then continue. For
**material uncertainty**, use a **recommendation-first** sequence after the
substantive readback: name the uncertainty, give the current judgment and
basis, explain the downstream difference, recommend a route, and ask only the
smallest question needed. Do not silently choose a materially different result.

## Adapt how the readback is organized

**Silent adaptation** is the default. Choose a reasonable presentation from
context and let the user adjust it when they ask. Do not routinely expose mode
names, parameters, a selected-view footer, or a configuration menu:

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

A session preference may change presentation, not required coverage. Re-evaluate
coverage when the task changes. Output-form uncertainty normally belongs to the
AI: choose and continue. Ask only when different forms materially change
coverage, task meaning, downstream use, or risk.

Use `minto_pyramid` only when it makes complex material easier to inspect. It
means grouping ideas of the same kind, deriving each upper point from the ideas
below it, keeping vertical support visible, and ordering sibling ideas with a
defensible horizontal logic. It is a method for improving a readback, not the
core of Readback First and not shorthand for a layered format. Never let the
organization hide source details, exceptions, corrections, or open items.

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

Use `overview` for low-risk orientation, `detailed` for material items and
qualifiers, and `traced` for formal retention or handoff when source trace is
available. **Overview is navigation**, not sufficient confirmation of
`reception_coverage` for material source units. Do not require traced
confirmation when the source is not available; report the fidelity limit
instead.

## Reader-facing response

Present the readback in the user's language as ordinary rendered Markdown in
the final answer body, before substantive advice or action. Tool traces,
collapsed status, and private reasoning alone do not satisfy visible readback.
For tool work, a short progress receipt may precede tools; the final answer must
still retain enough readback to stand alone. Never reveal private reasoning.

Do not wrap ordinary reception in a `text` code fence or mechanically print
English field names, IDs, state enums, or a fixed template. Schemas below and in
PROTOCOL.md are bookkeeping, not the default user interface. Show IDs only when
needed for source tracing or precise corrections; use natural status wording.
An explicit request for an exportable machine record can override presentation.

Readback is the beginning of a useful response. Once input is closed and no
named blocker applies, answer the actual question: give judgment, basis,
tradeoffs, a recommendation, or carry out the already authorized task. Do not
end with a receipt, a menu of design questions, or an offer to help with work
already requested. Do not invent extra recommendations for a simple fact.
Existing action authorization remains valid; this Skill adds no repeat approval.
Only block the dependent part of work when a missing answer materially matters.
For explicitly unfinished input or readback-only, respect that boundary.

Example — closed advisory request:

> 我觉得这个 Skill 的回讲格式生硬，而且回讲完就停了。你怎么看？

回讲：你指出两个问题：回讲像协议记录，且没有继续回答实际问题。

我同意，这分别是呈现和回应完整性的问题。建议把普通回讲改成自然
正文，并用完整的“回讲＋判断＋理由”示例替换日志式模板。先修这两项，
再考虑更复杂的表达方式；只改形式不能解决回应中途结束的问题。

See [complete examples](examples/before-after.md) and the
[WorkBuddy case](examples/workbuddy-case.md). These are authored reference
responses, not evidence of a model run.

## Multiple semantic views

Choose form from the relationship the user needs to inspect, not a fixed diagram
quota. Split multi-topic input into connected sections; use prose for intent and
qualifiers, tables for comparisons, and separate Mermaid diagrams for different
relationships. Keep shared object names and cross-section dependencies stable.

| Meaning to inspect | Suitable form |
| --- | --- |
| Simple fact, nuance, rationale, unfinished wording | Natural prose |
| Parallel alternatives or attributes | Markdown table |
| Steps, decisions, prerequisites | `flowchart` |
| Participants and ordered interactions | `sequenceDiagram` |
| States and transition conditions | `stateDiagram-v2` |
| Concept hierarchy | `mindmap` |
| Events and corrections over time | `timeline` |
| Known schedule and dependencies | `gantt` |
| Entities and their relationships | `erDiagram` |
| Technical classes and their structure | `classDiagram` |

Use a real mermaid fence when the host can render it, not an ASCII substitute or
one giant diagram containing every topic. If unsupported, use a readable table
or prose and describe the limitation. Do not claim render verification without
observing it. Do not invent dates, cardinalities, causes, ownership, or ordering
to populate a diagram. Label inferred or unresolved links; preserve source
qualifiers nearby. A diagram is an inspection view, not coverage proof or user
confirmation. For simple input, no diagram is normally needed.

## Precise waiting and continuation

Use `response_route` internally; explain them to the user in ordinary language:

- `wait_for_input`: an explicit unfinished utterance; preserve what arrived and
  invite continuation, without a premature implementation questionnaire.
- `wait_for_clarification`: missing source or material semantic ambiguity;
  preserve alternatives and ask only what changes the dependent next step.
- `wait_for_reception_confirmation`: explicit confirm-first/completeness check
  or a required scoped coverage confirmation for formal propagation.
- `readback_only`: the user asked for only a readback; do not turn that into an
  unsolicited question or further work.
- `host_authorization_required`: actual host authorization is missing.
- `proceed_with_provisional_response`: no blocker; continue while reception
  stays shown unless explicit scoped confirmation was supplied.

Inspect input completion before asking downstream design questions. Report
"the user stated" separately from "my interpretation" and "verified fact".
Never turn an ambiguous path such as “同级 dist” into a confirmed sibling path.
Keep unresolved items and correction lineage across any available document
versions or authorized handoff. Require provenance and resolution evidence to
mark an item resolved; do not claim durable storage that did not occur.

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
