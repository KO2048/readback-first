# Readback First Protocol

**Protocol Version: 0.3**

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
       wait_for_reception_confirmation |
       host_authorization_required
```

`READBACK_SHOWN` means the user has been shown the working understanding. It is
not a claim of confirmation. Continuing does not change reception state from
`shown` to `confirmed`.

Blocking reception confirmation is required when any of the following applies:

- the user is still speaking, adding, correcting, or explicitly marks the input
  `in_progress`;
- the available source is inadequate for the requested transformation;
- a material ambiguity changes the next safe response or action;
- the user explicitly requests confirm-first, readback-only, or reception
  completeness checking;
- a persistent canonical artifact, formal handoff, or propagation requires
  confirmed reception coverage.

Host safety and action authorization remain a separate blocker. When the next
step is a file write, external message, system call, commit, push, publish,
purchase, or another consequential act, use `host_authorization_required` and
the host's normal gate even if reception was confirmed.

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

## 8. Adaptive readback presentation

The user may set a turn-level or session-level preference. The AI may select a
reasonable default from context, but must state the selected presentation
after the substantive readback and allow adjustment.

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
or handoff recompiles the full current view.

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

- `overview` confirms the displayed high-level working understanding and may
  support low-risk advisory discussion.
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

## 13. Migration from 0.1

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
