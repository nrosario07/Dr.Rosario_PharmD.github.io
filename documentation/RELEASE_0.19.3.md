# ClinicalRx 0.19.3 — release consistency and anticoagulation acceptance
Audit: October 24, 2026.

## Findings
Repository manifest and app.js identify v0.19.2. Latest inspected GitHub Pages build succeeded (run 40105291590). Direct HTTPS check matched 47/49 manifest entries; the two unavailable entries were deployment/build artifacts that should not have been tested as public URLs. All 47 intended public content files matched. The browser requested v0.19.2 assets but continued to display runtime v0.19.1 after one reload. Cause is not established; do not call this a complete browser acceptance of v0.19.2.

## Browser-tested on the observed runtime
- Anticoagulation procedure selector populated.
- Fictional AF/apixaban 5 mg twice daily, age65, CrCl80, elective inguinal hernia repair November10 generated the existing dated conditional calendar and no-bridge rationale with sources.
- Selecting an urgent/emergency procedure and submitting replaced that calendar with REVIEW_REQUIRED; no regimen remained.
These are software checks, not independent clinical validation or a new source review. No patient data entered.

## Changes
- Startup compares expected HTML version with the executing app version. A mismatch displays an explicit warning, instructing users to preserve reviewed de-identified work before a hard refresh; no automatic reload or storage added.
- Build validator rejects disagreement between HTML metadata, asset versions and app version.
- Public URL manifest excludes deployment controls; package excludes temporary build artifacts, while retaining required deployment configuration.
- Empty monitoring/source headings removed from unsupported decision outputs.
- Future AI/Canva studio requirements clarified in BUSINESS_EDUCATION_FUTURE.md.

## Verification
355 JavaScript tests and 9 Python tests passed. ZIP CRC, byte comparison and <100-file batching required. New startup warning and revised rendering are automated-tested, not deployed/browser-tested. Mobile, print/PDF, all-tool coverage, hosted monitoring and independent clinical validation remain open. No clinical algorithms or dose rules changed.

## Phase checkpoint
Phase09: release-consistency safeguards. Phase04: elective DOAC and urgent-context software checks. 11/13 tracks initially implemented, 0/13 fully accepted. No whole-platform completion date assigned. Next: accept consistent deployed runtime, activate missing monitoring/CI, finish mobile/print and broader clinical workflow acceptance before expansion.
