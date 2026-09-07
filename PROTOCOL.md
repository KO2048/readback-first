# Readback First Protocol

**Protocol Version: 0.4**

**Status:** public candidate; implementation and runtime evidence are still being validated

## 1. Central contract

**Readback is the core. Default readback is the normal route.** Before an AI
relies on a user's expression to answer or act, it makes its **Visible working understanding**
inspectable. The user can interrupt and correct that working
understanding at any time. When no named blocker applies, the AI continues from
the readback instead of turning it into a mandatory confirmation popup.

```text
user expression
  -> visible working understanding
  -> proceed with a provisional response, or wait at a named gate
  -> user correction or scoped confirmation when required
  -> risk-appropriate authorization for consequential action
  -> answer, revision, or action
```

The protocol aligns user expression with what the AI says it is preparing to
use. It cannot expose all hidden model state, prove factual truth, or authorize
an external action merely because the user confirms the readback.

## 2. Readback is not summary

Readback is optimized for inspection and correction. It preserves material
facts, requests, reasons, qualifiers, alternatives, corrections, relations,
questions, and unfinished items. It may be concise only when the source is
simple enough that concision does not hide material meaning.

Summary is optimized for compression. It can merge, rank, and omit material.
A summary may follow a readback when requested or authorized, but it cannot
substitute for source-coverage confirmation.

No conformance claim may be based on compression ratio, short length, or a
model's self-reported coverage IDs. Coverage must be checked against externally
identified meaning units when the source is available.

## 3. Independent state axes

Never overload one label such as `confirmed` across different concerns.

### Source state

Describes the user's expression itself:

- `active`: still part of the current source baseline;
- `in_progress`: explicitly incomplete or still being dictated;
- `superseded`: preserved source whose role changed through a later correction.

### Reception state

Describes the user's review of the visible working understanding:

- `unreviewed`: not yet shown to the user;
- `shown`: visible, but not confirmed;
- `confirmed`: accepted for the specified target and scope;
- `corrected`: the user supplied a correction;
- `rejected`: the displayed interpretation was rejected.

### Decision state

Describes whether a proposition has become a decision:

- `candidate`;
- `open`;
- `decided`;
- `resolved`.

### Action authority

Describes authority for consequential execution:

- `not_requested`;
- `requested`;
- `authorized`;
- `rejected`.

Reception confirmation never promotes fact truth, decision status, or action
authority on its own.

## 4. Lifecycle and gates

Reception state and response routing are independent. The reference lifecycle
is:

```text
INPUT_OPEN
  -> RECEPTION_DRAFT
  -> READBACK_SHOWN
  -> optional ACTIVE_ALIGNMENT
  -> response_route:
       proceed_with_provisional_response |
       wait_for_input | wait_for_clarification | readback_only |
       wait_for_reception_confirmation |
       host_authorization_required
```

`READBACK_SHOWN` means the user has been shown the working understanding. It is
not a claim of confirmation. Continuing does not change reception state from
`shown` to `confirmed`.

Waiting reasons are distinct. Select the route that matches the actual blocker:

- `wait_for_input`: explicitly unfinished input; invite continuation, not approval.
- `wait_for_clarification`: inadequate source or material semantic ambiguity.
- `wait_for_reception_confirmation`: explicit confirm-first/completeness checking
  or scoped coverage confirmation required for formal propagation.
- `readback_only`: explicit instruction to deliver only the receipt.

Do not print route enums as the default user interface. Do not make an unfinished
utterance trigger a design questionnaire. A long but closed request does not by
itself require waiting. If multiple blockers exist, retain them separately and
address only the currently relevant one; clearing one does not clear the others.

A closed addition or correction is not a blocker by itself. Append it, update
its relations, and re-evaluate the predicates against the revised working
understanding.

Host safety and action authorization remain a separate blocker. When the next
step is a file write, external message, system call, commit, push, publish,
purchase, or another consequential act, use `host_authorization_required` and
the host's normal gate if authorization is missing, even if reception was confirmed.
Previously granted authorization remains valid; do not ask for it again.

A simple, closed, low-risk question may receive a one-line readback followed by
an answer. A longer but clearly closed, low-risk advisory request may receive a
structured readback followed by an **in-chat provisional response**. A closed,
source-adequate in-chat analysis or draft also proceeds after readback,
especially when the user explicitly asks the AI to continue after showing the
readback. In all of these cases the reception state remains `shown`, not
`confirmed`, unless the user actually confirms it. The response must not erase
open items or pretend alignment was completed.

If the user confirms one batch and adds another, advance only the confirmed
batch and append the new batch. Do not restart the entire conversation or make
every addition re-confirm all prior material.

## 5. Readback record

For complex input, assign stable IDs within the session and preserve source
order. A record can include:

```yaml
item_id: RBF-0001
batch_id: B-001
source_span: exact text when available
working_understanding: what the AI is preparing to use
item_type: fact | opinion | request | reason | example | constraint |
  alternative | correction | question | open_item
source_state: active | in_progress | superseded
reception_state: unreviewed | shown | confirmed | corrected | rejected
decision_state: candidate | open | decided | resolved
qualifiers: []
relations: []
ambiguity: null
```

Required relations include, where applicable, `corrects`, `supersedes`,
`contradicts`, `depends_on`, and `extends`. A later correction never deletes
the earlier expression.

## 6. Coverage, uncertainty, and source fidelity

Use bounded evidence labels:

```yaml
source_fidelity: exact | semantic | unavailable
coverage_state: mapped_with_known_limits | uncertain | unmapped |
  not_assessable
```

Report ambiguous spans, possible unparsed material, low-confidence
transcription, ungrounded pronouns, and unfinished content. Do not claim
"nothing was omitted" when the protocol has not compared the readback with an
available source inventory.

For a retained or formally compiled artifact, maintain source-to-output trace
or explicitly list unpropagated items and reasons. Stable IDs help inspection;
they are not proof of semantic coverage by themselves.

## 7. Corrections and contextual interpretation

Material corrections must show:

- the original expression;
- the candidate corrected interpretation;
- why the interpretation was proposed;
- what downstream meaning would change;
- the user's confirmation or rejection when required.

Meaning-preserving punctuation, filler removal, and obvious ASR cleanup may be
applied silently. A wording change that could alter a fact, entity, negation,
quantity, condition, time, authority, or decision must remain visible as a
candidate interpretation.

AI-generated grouping or induction must be labeled as organization or
interpretation, never presented as if the user stated it verbatim.

### Correction during provisional continuation

A user correction may interrupt an answer or draft that followed a readback.
Preserve the earlier expression, append the correction, and link it with
`corrects` or `supersedes`. Trace which provisional claims depend on the
corrected item: mark only **dependent provisional output** as `needs_revision`
or `superseded`, while leaving independent output active. Then
re-evaluate the blocking predicates against the corrected working
understanding. Continue with a revision when no new blocker exists; otherwise
wait at the newly applicable gate. A correction does not silently reopen
unrelated confirmed scope.

## 8. Adaptive readback presentation

**Silent adaptation** is the default. The AI selects a reasonable presentation
from the content, task, consequence, and current-session preference without
showing a parameter footer or asking the user to configure a mode. A user may
still request a different density, organization, focus, or source trace.

```yaml
organization_method: natural | minto_pyramid
readback_view:
  density: compact | standard
  focus: full | delta
  source_trace: off | semantic | exact
  preference_scope: turn | session
```

`compact` may reduce repeated wording, never material coverage. `delta` is
allowed only when the prior baseline is locatable, reception-confirmed for the
relevant scope, and unchanged source items remain traceable. Formal retention
or handoff recompiles the full current view. A session preference changes
presentation, not required coverage; re-evaluate coverage when the task changes.

Evaluate uncertainty in this order:

1. Is the user still speaking or is the input complete?
2. Is the available source adequate for the requested result?
3. Is there semantic ambiguity that could change the result?
4. Is there genuine output-form uncertainty that changes coverage, task nature,
   or risk?

For **low-impact uncertainty** that is reversible and has a contextually
dominant interpretation, show the working assumption and the alternative's
effect, then continue. Do not make the user answer a question that would not
change the next safe step.

For **material uncertainty**, use a **recommendation-first** sequence after the
substantive readback: identify the uncertain point, show the current judgment
and its basis, explain the downstream difference, recommend a route, and ask
only the smallest scoped question needed before proceeding. Do not silently
choose between materially different interpretations.

Output-form uncertainty normally belongs to the AI: choose and proceed. Ask
only when different forms would materially change source coverage, task
meaning, downstream use, or risk. Never replace that judgment with a standing
menu of presentation parameters.

### Optional Minto Pyramid Principle method

`minto_pyramid` is an organization method for making a complex readback easier
to inspect; it is not the product core and it is not shorthand for "layers."
When used, the AI groups ideas of the same kind, derives an upper-level point
from the grouped ideas below it, keeps vertical support visible, and orders
sibling ideas with a defensible horizontal logic. Source details, exceptions,
corrections, and unresolved items remain available for checking.

Natural organization remains the default when it better preserves the user's
expression. Readback quality is judged by inspectability and semantic coverage,
not by whether a pyramid-shaped format was used.

## 9. Confirmation contract

Bind every confirmation to explicit fields:

```yaml
confirmation_depth: overview | detailed | traced
confirmation_target: reception_coverage | interpretation |
  product_decision | action_authority
confirmation_strength: acknowledges | accepts | corrects | rejects | partial
confirmation_scope: [batch IDs, item IDs, sections, or named actions]
confirmation_evidence: user's exact confirming span
```

- `overview` acknowledges a high-level orientation and may support low-risk
  advisory discussion. **Overview is navigation**, not sufficient evidence for
  `reception_coverage` of material source units.
- `detailed` confirms the material items and qualifiers in the named scope.
- `traced` confirms a source-linked view appropriate for formal retention,
  conversion, or handoff when the source is available.

A bare "yes" inherits only the nearest clear target and scope. It does not
authorize a file write, message, external call, commit, push, publish,
purchase, or other consequential act unless that named action was separately
presented and authorized under the host system's safety rules.

## 10. Current-session boundary

The public Skill may rely only on context visible in the current host session.
It may maintain `batch_id`, `receipt_revision`, `baseline_revision`, relations,
confirmation records, and open items inside that session. It must not claim
cross-session memory, durable retention, source recovery, or access to a prior
conversation unless the host actually provides and verifies that capability.

## 11. Direct-answer escape hatch

When the user asks for a direct answer, the AI may shorten or omit the visible
readback for a simple, settled request. It still must preserve material
ambiguity internally and must not bypass action authority, privacy, security,
or other host gates. If directness conflicts with a consequential unresolved
ambiguity, state the smallest blocking issue.

## 12. Conformance evidence

Three evidence levels must remain distinct:

1. **Protocol fixture:** deterministic good/bad examples validate named
   invariants.
2. **Runtime transcript:** a fixed input, runtime, model/version, Skill state,
   raw output, and human-scored result demonstrate observed behavior.
3. **Product claim:** broader reliability claims require repeated runtime
   results across representative cases and declared environments.

Passing protocol fixtures alone does not prove that a model will follow the
Skill at runtime.

## 13. Migration

### Migration from 0.2 to 0.3

- Make visible readback the default for meaningful input when the Skill is
  loaded; adaptation changes presentation, not whether readback occurs.
- After `READBACK_SHOWN`, normally use
  `response_route: proceed_with_provisional_response` for closed,
  source-adequate, non-consequential in-chat work. Do not treat continuation as
  reception confirmation.
- Replace the absolute "retention or conversion always waits" rule with precise
  predicates: in-chat provisional conversion may continue, while persistent
  canonical retention, formal handoff, and propagation may still require
  confirmed coverage.
- Allow corrections to interrupt provisional work, preserve source lineage,
  and invalidate only dependent output before re-evaluating blockers.
- Choose presentation silently by default. Remove standing view footers and
  parameter menus; use recommendation-first clarification only when uncertainty
  materially changes the result.
- Treat `overview` as navigation, not sufficient confirmation of material
  `reception_coverage`.
- Keep automatic default delivery as a host-integration responsibility; the
  reference Skill alone cannot prove turn-by-turn activation.

### Migration from 0.1 to 0.2

- Replace `WAITING_FOR_CONFIRMATION` with
  `WAITING_FOR_RECEPTION_CONFIRMATION`.
- Replace `source_coverage` with `reception_coverage` as the confirmation
  target.
- Replace mixed labels such as `confirmed request` with independent source,
  reception, decision, and authority fields.
- Treat readback-followed-by-answer as `READBACK_SHOWN` plus a scoped
  provisional response, not completed user confirmation.
- Treat Minto Pyramid Principle organization as an optional method for complex
  readback, not as Readback First's core or as a generic "layered structure."

## 14. Reader-facing delivery and substantive continuation (0.4)

The normative delivery rules in SKILL.md sections "Reader-facing response",
"Multiple semantic views", and "Precise waiting and continuation" implement this
contract: natural rendered Markdown in the user's language, visible in the final
answer body; trace schemas are not default response templates. IDs are optional
inspection aids. Explicit structured exports may use machine records.

Once input is closed, continue with the requested answer, reasoned judgment,
recommendation, draft, or authorized action. Receipt-only endings are appropriate
only for an explicit readback-only instruction, unfinished input, or an applicable
blocker. Do not replace the response with a questionnaire or an offer to start.
Keep user statements, AI interpretation, and verified evidence distinguishable.

A response may contain multiple semantic sections and Mermaid types. Select
views by meaning; preserve cross-section identity, qualifiers, uncertainty,
provenance, and correction links. Unsupported renderers require readable
fallbacks. No diagram may invent relationships or claim complete coverage.

Unresolved items must survive revisions and authorized handoffs with provenance,
status, and correction links. Resolve only with resolution evidence and preserve
the resolution chain. This requirement does not imply unavailable durable memory.

### Migration from 0.3 to 0.4

- Replace the default machine-record example with natural complete responses.
- Split waiting for input and clarification from reception confirmation.
- Make useful continuation explicit; keep readback-only and actual blockers.
- Add content-driven multi-section, multi-diagram presentation.
- Preserve existing 0.3 source, reception, decision, and authority distinctions.
- Apply on every user turn through the host integration in docs/always-on.md;
  activation is mandatory in that profile, while presentation remains adaptive.
- Keep candidate status until real runtime and rendering evidence are recorded.
