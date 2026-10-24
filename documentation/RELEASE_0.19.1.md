# ClinicalRx 0.19.1 — deployment reliability checkpoint

Audit date: October 24, 2026.

## Observed on deployed v0.19.0
- Footer and repository release manifest identify 0.19.0. Full deployed byte-for-byte parity was not established.
- Fictional case creates a complete patient plan; export remains disabled before review.
- After patient-plan and de-identification review, printable HTML downloads successfully.
- Editing follow-up invalidates review and disables handout download. Updated text appears in patient plan.
- Desktop patient-plan workspace visually inspected. Not an all-page/all-tool or mobile acceptance audit.
- Repository .github/workflows lookup returns 404. Hosted CI and scheduled monitoring remain unverified/uninstalled at this path.
- Browser policy prevents opening downloaded file URLs. Print/PDF rendering remains unverified; no workaround used.

## Changes
- Version-independent packager reads the release manifest, avoiding future preview version drift.
- One upload packet contains numbered batches with fewer than 100 files each. All 50 website files remain in one batch.
- Supporting files preserve repository-relative paths; no omissions, duplicates or flattened folders.
- ZIP integrity and every packaged file's bytes checked against source. SHA256 inventory included.
- Corrected a stale test expecting an older monitoring-status label; requirement remains installation-required.
- No clinical algorithms, dose recommendations, payer rules or source baselines changed.

## Phase status
Phase06 education: deployed download/re-review checkpoint passed; print and mobile acceptance open.
Phase09 release governance: bounded upload packaging implemented; hosted monitoring still blocked.
Initial capabilities: 11/13 tracks. Fully accepted tracks: 0/13. This is not an overall completion percentage.
Next: print/mobile and keyboard acceptance, install and verify workflows, broader switch/anticoagulation browser fixtures, then source-reviewed exact-product coverage.
No reliable all-phases completion date while independent review, data rights and later residency scope remain unresolved.
