# ClinicalRx 0.18.1 — connected workflow usability

Assessment: October 18, 2026 (America/Chicago).

## Delivered
- Local identity filter by name, strength, form or RxCUI; all terms must match. Selected identity stays available; no extra API request.
- Direct cabinet links to SOAP/MTP and patient plan; transfer confirmation beside cabinet.
- About introduction uses Pharmacist Practitioner terminology.
- No changes to dosing, clinical recommendations, payer rules or external data transmission.

## Verification
- GitHub manifest and live footer report 0.18.0. Full remote file-by-file hashing was not performed.
- Live browser: metformin returned 134 RxNorm identities. Selected RxCUI 861007 and Ascend label dated 20251218; added product, entered fictional regimen, synced cabinet to SOAP, entered fictional SOAP actions and verified generated patient plan. Review checkbox enabled patient download. An initial transfer was not observed; a settled retry succeeded, so no reproducible transfer defect is claimed.
- MedlinePlus and PubMed enrichment rendered. This is one successful query, not comprehensive API acceptance.
- 348 automated tests pass, including local filtering, selected-identity retention, cabinet-to-SOAP transfer and patient-plan generation.
- New 0.18.1 UI is not browser-tested until uploaded. Actual downloaded patient file, mobile layouts, broad drug coverage and external checker accuracy remain unverified this release.
- Source-monitor workflow path still returned GitHub 404. Install instructions remain required; no scheduled clinical auto-update is claimed.

## Phase progress
11/13 tracks have initial capabilities; 0/13 fully accepted. Remain in Phase02 connected medication workflows with Phase09 monitoring installation blocked. Successful fictional workflow is a partial acceptance checkpoint, not phase closure. Next: deployed filter/navigation acceptance, actual export and mobile regression, then broader normalized data and source-reviewed switch coverage.
