# Publish v0.7.0

Plan Version: plan-v4. User explicitly requested latest default installation while
retaining separate iteration records. PR #2–#7 were merged in dependency order
using merge commits and exact-head guards, without force push or rule bypass.

Scope: latest-version installation docs and release metadata. No local global
Skill installation or governance replacement is performed by this publication.

Validation: contract and 39 fixture checks; fresh fetch from main and version/hash
verification required after merge. Runtime comparison remains pending. A 0.x
protocol release is not a claim of model quality equivalence.

Publication status is authoritative at the GitHub release URL; repository metadata
describes the artifact version and does not self-certify a network action.
Rollback uses a normal reviewed revert or a pinned earlier snapshot, not history rewrite.
