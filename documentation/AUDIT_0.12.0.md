# Audit and verification — 0.12.0

Audit date: October 14–15, 2026. No remote repository write or deployment performed.

## Deployed version / browser-tested

Latest inspected Pages run succeeded: https://github.com/nrosario07/nrosario07.github.io/actions/runs/38657633381 ; main commit 469817cd3689cde76905c77400301fa891c3e0ff. Deployed interface identifies v0.11. Its anticoagulation form asks for a preselected bridge/interruption plan; switching asks for an approved starting dose. These are verified workflow-design defects addressed by the new public route implementations.

A browser search for the public name apixaban returned 16 RxNorm identities at 2026-10-15T00:36:56.478Z. The reported timeout was not reproduced. Full medication→cabinet→SOAP→patient export was not retested in this audit. No claim of byte-for-byte parity against a previous ZIP is made.

## Automated and runtime verification

235 Node tests pass, including existing routes, privacy, stale-request protection, encounter/export state, new procedure/renal/risk boundaries, generated target dosing, exact IR/ER label cases, LAI recommendation mode, CPA term/review validation, fallback response mapping and hard deadlines. DOM-harness checks exercise generated controls and events; they are not visual-browser tests.

Independent runtime check: forced RxNav failure plus real public NLM Clinical Tables/RxTerms returned five mapped rows for apixaban in approximately 6.3 seconds. A separate public endpoint check returned CORS access. This verifies fallback mechanics in that environment, not every user's browser/network or continuous service availability. v0.9 used the same RxNav endpoint and 15-second timeout.

## Not yet verified

New v0.12 deployed browser rendering, keyboard/mobile layout, generated calendar print/PDF, full cross-workspace live API workflow, independent pharmacist review and institutional CPA/legal approval. Broader switches/procedures and exact local-clock timing are not supported. Antipsychotic historical source maintenance warning is visible. Current AHA 2026 perioperative landing-page summary was located; its full guideline was not retrieved, so no new full-text recommendations were inferred.

## Acceptance after upload

Verify version 0.12.0; search apixaban; select a valid identity and label; add to cabinet; sync a fictional case into SOAP and create/review a patient plan. Generate routine no-bridge and high-risk conditional anticoagulation examples, then change an input and confirm old output clears. Generate an SSRI, exact-product IR/ER and LAI example. Test unsupported pairs. Generate a CPA with a 24-month agreement term and 12-month review, then verify a review interval over 12 months is rejected. Check printing, narrow screens and keyboard navigation. Do not enter real patient data.
