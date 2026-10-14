# ClinicalRx v0.8.0 reassessment

Assessment: 2026-10-13 UTC (2026-10-12 America/Chicago). Repository main: 3161325731bf30a2e0a52ceb617afabf707c84b6. Public site and repository index both still reference/display v0.6.1. However all 19 loaded assets exactly match the v0.7.0 release archive. This is a mixed deployment, not a successful complete v0.7 update. Comparison details: DEPLOYMENT_CHECK_0.8.0.json.

## Browser-tested this reassessment

About, four-pillar hub and diabetes review were inspected. Diabetes still displays the prohibited example-site link. Hub has a save/restore link; clicking it produces #draft URL but About heading, because old index does not load local-draft.js. This defect is resolved in the complete new index, but new release remains browser-unverified until deployment. Prior complete fictional medication/cabinet/SOAP/patient-plan testing is historical evidence in AUDIT_0.7.0.md, not a newly repeated full regression this turn.

## Fixed and implemented

Complete v0.8 entrypoint includes local-draft.js and reporting.js with matching release queries. Removes excluded example-portfolio domain from all distributed website/source documentation; replaces business-plan reference with primary SBA planning guidance. No example site's code, branding or clinical claims are adopted. Clarifies external calculator readiness.

Phase 01B adds current-encounter structured MTP reporting: separate accepted/implemented/resolved counts, action categories, missing/duplicate IDs and evidence-completeness flags. Default reviewed CSV excludes medicine/narratives; optional detail clears review. Formula-like spreadsheet fields are neutralized. Includes v0.7 local draft save/preview/restore and review reset. No new dose, clinical recommendation or payer eligibility algorithms.

## Automated / archive evidence

144 tests pass, zero fail. Includes pure report counts/flags/CSV/privacy, excluded-domain regression across docs/documentation, route rendering and shared MTP → report → review → export data-flow test. Prior draft validation/restore and clinical/reference tests pass. Archive integrity and required paths verified at packaging. These tests do not verify browser layout, guideline currency, legal/payer acceptance or clinical certification.

## Outstanding

New v0.8 browser regression pending upload; cloud browser cannot open local file previews. Current turn did not test every tool, mobile layout, print or all external destinations. Full longitudinal reporting, medication-section completeness, comprehensive validated interactions/prices, complete prescribing pathways, authorized HEDIS/Stars specifications, validated VAS prediction and residency tools remain incomplete. Status counts remain unverified user-entered records; no clinical effectiveness or savings inferred. Primary clinical rules were not expanded or newly revalidated this release.

## Upload acceptance

Extract package and replace the entire docs folder at repository root, including index.html; preserve assets/data/downloads nesting. Do not upload ZIP itself or patient files. Pages main:/docs. Confirm footer v0.8.0, no example links, working #draft and #reporting. Repeat fictional medication → cabinet → SOAP → patient plan and draft roundtrip; reviews must reset. Add MTP statuses, check report count and CSV default excludes narratives; changing detail option must clear export confirmation. Verify mobile/print and no clinical text network requests. Install current documentation/scripts/tests/.github via clone to retain reproducibility.
