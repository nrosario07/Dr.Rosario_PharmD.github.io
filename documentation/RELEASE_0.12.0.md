# Release 0.12.0 — recommendation-first workflows

- Replaced public anticoagulation plan-entry worksheet with procedure-led recommendations, reasons, conditional date cards, monitoring and AMA references. Added corrected mechanical-mitral risk caveat and explicit limits.
- Replaced public switch worksheet with target-start recommendations for bounded SSRI, oral antipsychotic, metoprolol IR/ER, CONCERTA and LAI initiation paths. Unsupported requests explain their limits.
- Added independently hosted NLM RxTerms fallback for slow/failed RxNav requests, source labeling, mapping validation, cancellation and recovered controls.
- Prefilled CPA standard clauses and clinical scope from the supplied agreement; added professional identity, term and review controls. Annual protocol review is enforced independently of longer agreement duration.
- Preserved four pillars, free access, LinkedIn-only profile contact, no-PHI gates and tab-only clinical handling.

235 automated checks passed. Public v0.11 lookup succeeded in the browser. A runtime test with deliberately unavailable RxNav retrieved real RxTerms data in about six seconds. New v0.12 browser/print/mobile acceptance and independent clinical/legal review remain pending; this release is not full-platform completion. The intermittent user's RxNav failure was not reproduced and its root cause is unproven.
