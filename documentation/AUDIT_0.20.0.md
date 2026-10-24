# Audit — October 24, 2026

## Verified deployed baseline

Release 0.19.5: `DEPLOYED_0.19.5_INTEGRITY.json` records 47/47 matching public files. Browser showed release 0.19.5 and missing-section panel. Load fictional case → check patient review → handout enabled. Clear monitoring → missing monitoring listed → handout disabled. This verifies control state, not a new download/print test.

About inspected visually; prominent tools repeated before profile recognition. README contained contradictory “current” releases 0.19.0, 0.18.2, 0.18.1, 0.18.0 and 0.17.0 plus an old 0.15.0 heading. Replaced in 0.20.0. Repository root includes old upload guides and mistakenly uploaded packet metadata; safe cleanup instructions supplied, no deletion performed.

## Reference assessment

Reviewed the example analytics repository README: adopt clear overview, limitations, repository map and reproducible checks, without copying its project claims or imposing notebook/data folders on a static site. Reviewed buildmyroutine's visible home/privacy/terms; its accounts, analytics and persistence differ from ClinicalRx. Notices written for actual ClinicalRx behavior. Andrew Tran site was inaccessible to the search tool in this run; no new comparison claim and no links added to ClinicalRx.

OpenMed, NIH ODS, USDA and affiliate guidance reviewed; see NUTRITION_AND_API_ROADMAP.md. OpenMed not installed or used to process text. USDA key not requested or exposed.

## Boundaries

Focused audit, not an exhaustive revalidation of every tool. New 0.20.0 About/nutrition/privacy/terms UI remains unverified in a deployed browser. No mobile, print/PDF or independent clinical/legal acceptance claimed. Remote writes blocked by GitHub integration 403. Automated tests are reported in AUTOMATED_TEST_RESULTS_0.20.0.txt.

Automated verification: 368 JavaScript tests and 9 Python tests passed. Route/event tests use a simulated DOM, not a real browser. Historical root upload guides are archived under documentation/history/upload-guides in the package; obsolete remote copies require the exact cleanup list after upload.
