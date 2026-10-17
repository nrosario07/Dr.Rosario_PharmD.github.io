# ClinicalRx assessment — October17,2026

## Deployment and browser observations
GitHub docs/index.html and docs/data/release-manifest.json report0.14.2. Manifest matches the prepared local baseline. The live footer also shows0.14.2. No assertion of freshly byte-comparing every public asset.

Browser-tested on deployed0.14.2:
- Clinical Tools task hub and all four pillars render, with navigation into switch and reporting.
- Fictional metoprolol50mg twice daily example generates100mg succinate ER once daily with a dated action and provenance.
- Reporting review checked with no-PHI gate unchecked correctly says CSV download not requested; the previous misleading-success defect is fixed.
- Switch source dropdown omits Mounjaro and universal age input remains. These observed limitations are addressed in local0.15.0.

## New local tests
337 Node tests pass, including42 added cases for studied GLP eligibility boundaries, Mounjaro reverse direction, explicit extrapolation/no2mg inverse, formulation dose/frequency/organ restrictions, conditional age and UI stale-result invalidation. Existing tests were updated where the intentional default changed to evidence-informed review. Event-capable DOM harness is not a rendering engine.

Syntax, release hashes and ZIP extraction are checked during packaging. No clinical notes leave the browser. No new external scripts or runtime services.

## Not verified
No browser visual/interactive test of new0.15.0; no all-page/mobile/print audit this run; no full trial eligibility engine; no independent clinical reviewer; no broad language-model MTP understanding or payer eligibility verification. Source checks are point-in-time October17, not a promise of continuously updated clinical rules. Prior GitHub write403 remains unresolved; no remote update attempted or claimed this run.

## Deployment acceptance checklist
1. Footer0.15.0 and matching asset versions; four pillars retained.
2. Metoprolol example with age cleared still yields100mg; CONCERTA path requires age.
3. Ozempic1mg weekly,16weeks, stable≥3months, A1c7.5,BMI30, no limiting GI symptoms, reviewed safety/context and evidence produces the explicitly off-label tirzepatide5mg option; changing A1c10 blocks it and clears prior output.
4. Mounjaro10mg→Ozempic: evidence mode labels0.5mg as expert/extrapolated, never2mg as proven equivalent. Label mode shows0.25mg separately. Active GI symptoms block a calendar.
5. Venlafaxine37.5mg BID→ER75mg daily and bupropion SR150mg BID→XL300mg daily work only in supported normal-organ adult MDD context; impairment/unsupported regimens produce no dose.
6. Check keyboard focus, narrow screen, evidence expansion, monitoring and no-PHI export gates. Confirm source/target edits invalidate output. Use fictional cases only.
