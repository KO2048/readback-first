# Evidence for 0.7.0

39 deterministic fixtures validate named semantic invariants on authored
good/bad records. Some delivery cases use narrow text checks and reviewer-assigned
annotations. Passing them is not a model evaluation or proof of faithful reception.

Run python3 tests/validate_contract.py and python3 tests/validate_fixtures.py.
See runtime-matrix.md for observed behavior still requiring evaluation.

The three-turn runtime scenario and source responses are linked from
[the observation report](../docs/evaluation/three-round/report.md).
[Diagram consistency](../examples/diagram-consistency.md) is an authored reference;
manual semantic review must inspect every arrow, not merely the presence of a
Mermaid fence. Neither file adds to the 39 deterministic fixture count.

[Eight history-derived scenarios](history/README.md) extend manual evaluation coverage; they are not additional deterministic fixtures or eight runtime passes.
