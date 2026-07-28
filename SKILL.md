---
name: readback-first
description: Use when a user provides freeform, dictated, long, continuing, corrective, ambiguous, or retention-bound input and needs to verify what the AI is preparing to answer or act on before synthesis, insertion, or execution.
---

# Readback First

## Overview

Readback First aligns a user's expression with the AI's visible working
understanding before the AI answers or acts.

> Speak freely. Confirm what AI will use.

The readback shows the interpretation the AI is preparing to rely on. It does
not expose hidden reasoning, prove factual truth, or authorize external action.

## Core distinction

| Readback | Summary |
| --- | --- |
| Optimizes for coverage and correction | Optimizes for compression |
| Preserves facts, constraints, reasons, corrections, and open items | Merges, ranks, and omits detail |
| Shows ambiguity and possible omission | Usually presents a clean result |
| Happens before answering or acting | Happens only when requested or authorized |

Never replace reception confirmation with a shorter summary.

## Choose the lightest safe mode

| Input state | Required behavior |
| --- | --- |
| Simple, closed, low risk | Use a one-line readback, then answer. |
| Long or freeform but closed | Show a structured readback, then answer unless the user asked to confirm first. |
| Continuing, unfinished, or explicitly retention-bound | Preserve and expand the current batch, then stop at `WAITING_FOR_CONFIRMATION`. |
| Corrective | Preserve both versions and link what corrects or supersedes what. |
| High-risk action | Read back scope and intent, then obtain the action-specific authorization separately. |
| Explicit `direct answer` or equivalent | Shorten or omit the visible readback, but keep authority and safety gates. |

Length alone does not require a blocking confirmation. Do not create an
infinite confirmation loop: confirmation is scoped to the current batch.

## Protocol

For complex, open, corrective, or retention-bound input:

1. **Preserve the source**
   - Keep the original batch and its order.
   - Append new input; do not overwrite earlier input.
2. **Reconstruct with high coverage**
   - Capture facts, opinions, requests, reasons, examples, counterexamples,
     constraints, alternatives, corrections, questions, and unfinished parts.
   - Do not select a few "key points" as a substitute.
3. **Create an atomic ledger**
   - Give independently checkable items stable identifiers.
   - Record meaning, type, status, qualifiers, context, provenance, and links.
4. **Report uncertainty**
   - List ambiguous spans, possible omissions, low-confidence terms,
     unfinished spans, and unmapped source material.
   - Do not silently complete the user's intent.
5. **Link corrections**
   - Preserve the earlier and later expressions.
   - Use `corrects`, `supersedes`, `contradicts`, or `depends_on`.
6. **Confirm reception**
   - Ask the user to check source coverage, qualifiers, and relationships.
   - Do not ask them to confirm only a compressed summary.
7. **Synthesize only when allowed**
   - Confirmation of reception does not automatically authorize summarizing,
     merging, prioritizing, deciding, or publishing.
8. **Keep action authority separate**
   - Semantic confirmation does not authorize files, messages, purchases,
     external calls, commits, pushes, publishing, or other consequential acts.

## Structured readback contract

Use only the sections that add information:

```text
Readback

Received
- RB-001 [status]: ...
- RB-002 [status]: ...

Corrections and relations
- RB-003 corrects RB-001: ...

Constraints and qualifiers
- ...

Ambiguities or possible omissions
- ...

Open or unfinished
- ...

State: WAITING_FOR_CONFIRMATION | READY_TO_RESPOND
```

Recommended statuses:

- `in_progress`
- `candidate`
- `needs_review`
- `confirmed`
- `superseded`
- `resolved`

If the user confirms an older batch and adds new material in the same message,
advance the confirmed batch and append the new material as a new batch. Do not
restart the entire conversation.

## Confirmation semantics

Bind confirmation to an explicit target and scope:

```text
confirmation_target: reception_coverage | interpretation |
  product_decision | action_authority
confirmation_strength: acknowledges | accepts | corrects | rejects | partial
confirmation_scope: batch IDs, item IDs, sections, or actions
confirmation_evidence: the user's exact confirming span
```

A bare "yes" inherits only the nearest clear confirmation target. If that
target contains several claims, allow partial acceptance and correction.

## What Readback First is not

- Not a chain-of-thought viewer.
- Not a speech-to-text engine.
- Not a generic cleanup or summarization prompt.
- Not proof that the user's claims are factually true.
- Not approval for an agent to act.
- Not a requirement to block every simple request.

## One representative example

User:

> Use the previous launch plan, but remove the Friday release. Keep the beta
> invite, and don't email customers yet. I may change the pricing section
> later. Can you prepare it?

Readback:

```text
Received
- RB-001 [candidate]: Reuse the previous launch plan.
- RB-002 [confirmed request]: Remove the Friday release.
- RB-003 [confirmed request]: Keep the beta invite.
- RB-004 [constraint]: Do not email customers yet.
- RB-005 [in_progress]: Pricing may change later; no new pricing decision yet.

Ambiguity
- "Prepare it" could mean draft the revised plan or modify an existing file.

State: READY_TO_RESPOND
```

Then ask the smallest necessary question or provide a draft. Do not edit a file
or send an email without separate authorization.

See `examples/before-after.md` for a complete same-source comparison.

## Common failures

| Failure | Required correction |
| --- | --- |
| Compressing 1,000 information points into 10 | Show item-level coverage; allow long output. |
| Closing while the user is still speaking | Mark the batch `in_progress` and wait. |
| Replacing old text with a correction | Preserve both and add a correction link. |
| Treating a candidate as a decision | Keep `candidate` or `needs_review`. |
| Dropping qualifiers | Keep conditions, exceptions, negation, and timing. |
| Inventing intent | Mark ambiguity and ask or preserve alternatives. |
| Treating reception as authorization | Run the separate action gate. |
| Blocking a clear one-line request | Use the simple direct path. |

## Final check

Before responding or acting, verify:

1. Can the user see what the AI is preparing to rely on?
2. Are facts, constraints, reasons, corrections, and unresolved items covered?
3. Are ambiguity and possible omission visible?
4. Is the confirmation scoped to the right batch and target?
5. Is synthesis separately authorized when needed?
6. Is external action separately authorized?
7. Is a simple request still simple?
