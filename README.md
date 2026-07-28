# Readback First

**The confirmation layer between human expression and AI action.**

> Speak freely. Confirm what AI will use.

[中文](README.zh-CN.md) · [Example](examples/before-after.md) ·
[Behavior fixtures](tests/README.md) · Apache-2.0

## The idea, in one scene

At a restaurant, the server does not send a complicated order straight to the
kitchen:

> “Two burgers instead of the steaks, one fries, two drinks, one mushroom
> soup, and one corn soup. About eight minutes. Is that correct?”

The customer confirms. Then the kitchen starts.

Working with AI should be similar. Before answering or acting, the AI should
show the **working understanding it is preparing to rely on** so the user can
check and correct it.

That is Readback First.

## Why

People should not need to become prompt engineers before they can think out
loud.

Long messages, voice transcripts, corrections, uncertain ideas, references
like “the previous version,” and last-minute constraints are normal human
expression. An AI can produce a polished, plausible response while silently
dropping a qualifier, merging two ideas, accepting a candidate as a decision,
or acting on the wrong interpretation.

The problem is not only what the user said. It is whether the user and AI are
aligned on what the AI is about to use.

## Same input, different outcome

```text
User:
"Move the launch to Monday—wait, don't change the public date yet.
Keep Friday for the internal beta. Don't email customers.
Pricing is still undecided."

Without Readback First:
"I'll update the public launch to Monday, keep the Friday beta,
pause customer email, and add a pricing review."

With Readback First:
- Public launch → keep unconfirmed; Monday change was withdrawn
- Internal beta → Friday
- Customer email → do not send
- Pricing → unresolved, not a decided review
```

See the complete
[original → plausible failure → readback → correction → confirmed input](examples/before-after.md).

## What the Skill does

Readback First:

- preserves the source before transforming it;
- reconstructs facts, requests, reasons, constraints, corrections, questions,
  and unfinished content;
- exposes ambiguity, possible omission, and low-confidence terms;
- keeps correction and supersession links;
- lets the user confirm reception coverage before sensitive synthesis;
- separates semantic confirmation from factual verification and action
  authorization;
- uses a lightweight path for simple, closed requests.

It is not:

- a chain-of-thought viewer;
- a speech-to-text engine;
- a generic summarizer;
- proof that user claims are factually true;
- permission for an agent to write, send, purchase, push, or publish.

## Install

### Codex

Ask Codex to install the Skill from the repository root:

```text
$skill-installer install --repo KO2048/readback-first --path . --name readback-first
```

Or clone it manually:

```bash
git clone https://github.com/KO2048/readback-first.git \
  ~/.codex/skills/readback-first
```

Restart Codex after installation.

### Other Agent Skills-compatible runtimes

Clone the repository into the runtime's skills directory. The Skill uses the
portable `SKILL.md` format; runtime-specific discovery and invocation may vary.

## Quick start

Invoke it explicitly:

```text
Use $readback-first.

I am going to describe a product change freely. Preserve corrections,
constraints, unresolved points, and anything you may have missed.
Do not act until the input is aligned.
```

Or ask naturally:

```text
Read this back before you answer.
```

For a simple closed request, the Skill uses a one-line readback and continues.
For unfinished or retention-bound input, it can stop at
`WAITING_FOR_CONFIRMATION`.

## Protocol

```text
free expression
  → source preservation
  → visible working understanding
  → ambiguity / omission / correction links
  → user correction or confirmation
  → confirmed input
  → risk-appropriate authorization
  → answer or action
```

The key boundary:

```text
semantic reception confirmation
  ≠ factual truth confirmation
  ≠ authorization to act
```

## Tests

The repository ships deterministic fixtures for the failure modes that
motivated the Skill:

```bash
python3 tests/validate_fixtures.py
```

They cover unauthorized compression, premature closure, correction overwrite,
candidate promotion, qualifier omission, invented intent, summary-only
confirmation, unresolved-item loss, confirmation overreach, direct-answer
authority bypass, and overblocking.

## Status

`v0.1.0` is the protocol/Skill release.

The current release does not include voice recognition, a desktop input method,
plugins, external actions, or a hosted service. Voice input is an important
future application, not a capability claimed by this version.

## Roadmap

- Strengthen same-source evaluation cases.
- Test the Skill across compatible agent runtimes.
- Explore a visual Readback Receipt for voice and long-form input.
- Evaluate input-method adapters only after the confirmation interaction is
  proven useful.

## Contributing

Useful contributions include:

- minimal examples where an AI produced a reasonable but wrong interpretation;
- fixtures for corrections, qualifiers, ambiguity, and continuing input;
- runtime installation verification;
- clearer language that preserves protocol boundaries.

If this solves a problem you have experienced, try it on a real freeform input,
share the before/after, and star the repository to follow the next iteration.

## License

Apache License 2.0.
