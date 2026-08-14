# Readback First

**See what AI is about to use—before it keeps going.**

> Speak freely. AI reads it back, then normally continues.

Readback First is a protocol and reference Agent Skill that makes **default readback**
visible before an AI relies on a user's expression. It shows the AI's visible
working understanding, continues when the next step is safe, and lets the user
interrupt and correct it at any time.

**Delivery boundary:** When loaded by a compatible host, the Skill treats
readback as the default behavior. Automatically loading it on every meaningful
turn still requires host integration.

[中文](README.zh-CN.md) · [Same-source example](examples/before-after.md) ·
[Protocol 0.3](PROTOCOL.md) · [33 deterministic fixtures](tests/README.md) ·
Apache-2.0

## The idea, in one scene

At a restaurant, the server reads a changed order back before sending it to the
kitchen:

> “Two burgers instead of the steaks; one fries, two drinks, one mushroom soup,
> and one corn soup. About eight minutes. Is that right?”

The readback makes the working order visible before a consequential action.
Readback First applies the same idea to AI: **show what will be used before
answering or acting**. For an ordinary in-chat response, the AI can continue
after the readback and the user can interrupt. For consequential actions, the
host's normal confirmation and authorization gates still apply.

## Same input, different outcome

```text
User:
"Move the launch to Monday—wait, don't change the public date yet.
Keep Friday for the internal beta. Don't email customers.
Pricing is still undecided."

Without Readback First:
"I'll move the public launch to Monday, keep the Friday beta,
pause customer email, and add a pricing review."

With Readback First:
- Public launch: keep open; the Monday change was withdrawn
- Internal beta: Friday
- Customer email: do not send
- Pricing: unresolved, not a decided review

Then the AI continues with a provisional plan. If the user corrects one item,
only dependent provisional output is revised.
```

See the complete
[original → plausible failure → readback → provisional response → correction → revision](examples/before-after.md).

## Why it exists

People should not need to become prompt engineers before they can think out
loud.

Long messages, voice transcripts, corrections, uncertain ideas, references
like “the previous version,” and last-minute constraints are normal human
expression. An AI can produce a polished, plausible response while dropping a
qualifier, merging two ideas, accepting a candidate as a decision, or acting on
the wrong interpretation.

The problem is not only what the user said. It is whether the user can inspect
what the AI says it is preparing to use.

## What the Skill does

Readback First:

- reads back meaningful input by default before a substantive response;
- preserves facts, requests, reasons, qualifiers, corrections, questions, and
  unfinished content instead of replacing them with a summary;
- normally continues after readback for closed, source-adequate, in-chat work;
- lets user corrections interrupt provisional work and invalidate only
  dependent output;
- chooses readback density and organization without showing a standing mode
  menu;
- handles low-impact uncertainty with a visible working assumption and uses a
  recommendation-first question only when ambiguity materially changes the
  result;
- separates reception state, decision state, factual truth, and action
  authorization.

It waits when the input is still open, the source is inadequate, a material
ambiguity blocks the next safe step, the user asks for confirm-first/readback-
only behavior, formal propagation requires confirmed coverage, or the host
requires safety/action authorization.

It is not:

- a chain-of-thought viewer;
- a speech-to-text engine;
- a generic summarizer;
- proof that user claims are factually true;
- permission for an agent to write, send, purchase, commit, push, or publish.

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

Clone the repository into the runtime's skills directory. The reference Skill
uses the portable `SKILL.md` format, but discovery, invocation, and enforcement
vary by runtime.

## Quick start

```text
Use $readback-first.

I am going to describe a product change freely. Read back what you are
preparing to use, then continue unless a named blocker applies. I will
interrupt if the readback is wrong. Do not perform external actions.
```

Or ask naturally:

```text
Read this back, then keep going unless you need a material clarification.
```

A simple settled request gets a one-line readback and same-turn answer. A long
or voice-like input gets a more inspectable readback, followed by a provisional
response when safe. A direct-answer request may shorten or omit visible
readback, but never bypasses safety or action authority.

### Important host boundary

The reference Skill specifies behavior **when the host loads it**. Making it run
automatically on every meaningful turn requires compatible **host integration**;
installing `SKILL.md` alone cannot prove default delivery across every runtime.

## Protocol

```text
free expression
  → visible working understanding (readback shown)
  → provisional response OR named blocking gate
  → user interruption, correction, or scoped confirmation when needed
  → risk-appropriate authorization for consequential action
  → answer, revision, or action
```

The key boundaries:

```text
readback shown ≠ reception confirmed
semantic reception confirmation ≠ factual truth confirmation
semantic reception confirmation ≠ authorization to act
```

## Tests and evidence

```bash
python3 tests/validate_fixtures.py
python3 tests/validate_contract.py
```

The repository includes **33 deterministic fixtures** for compression,
premature closure, correction lineage, qualifier loss, invented intent,
confirmation overreach, default-readback omission, proceed/wait routing,
interrupting corrections, mode-menu fatigue, uncertainty handling, and action-
authority bypass.

These fixtures validate named protocol invariants against hand-authored JSON.
They do not run a model or prove cross-runtime reliability. Broader product
claims require fixed prompts, raw runtime outputs, repeated runs, and declared
model/host versions.

## Status

Protocol 0.3 is a **public candidate** and is **not a tagged stable release**.
The protocol, Skill contract, and fixtures are implemented in this candidate;
broader runtime evidence and host integrations are still being validated.

This project does not include voice recognition, a desktop input method,
plugins, external actions, or a hosted service. Voice input is an important use
case, not a capability claimed by this repository.

## Roadmap

- Publish reproducible same-source runtime evaluations.
- Test verified compatibility across agent runtimes.
- Design a visual Readback Receipt for voice and long-form input.
- Evaluate input-method adapters only after the interaction proves useful.

## Contributing

Useful contributions include:

- minimal examples where an AI produced a reasonable but wrong interpretation;
- fixtures for corrections, qualifiers, ambiguity, and continuing input;
- runtime installation and behavior verification;
- clearer language that preserves protocol and authority boundaries.

Try it on one real freeform input. If the readback reveals a mismatch—or misses
one—share the same-source case. Star the repository to follow new evaluations,
runtime adapters, and interaction experiments.

## License

Apache License 2.0.
