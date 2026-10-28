# Audit — 0.26.0

Audit performed October 25–26, 2026. Deployed baseline v0.25.0; prepared release v0.26.0. Focus: Phase 01B/06 case separation and patient export, Phase 03 destination verification, Phase 09 progress accuracy.

## Deployment

48/48 public files matched v0.25.0. See DEPLOYED_0.25.0_INTEGRITY.json. The release-check workflow path returned 404 again. The prior audit found all three workflow paths absent and received a GitHub integration 403 on creation. No remote write was attempted again; no workflow is claimed operational.

## Browser evidence on deployed v0.25.0

- Calculator topic Mental health plus search MDCalc PHQ returned one PHQ-9 reference.
- An unmatched query returned zero results. Keyboard Enter on Clear filters restored 14/14.
- Confirmed defect: select Commercial payer, then Load fictional case. Commercial remained selected. The new case must not inherit preceding payer/cabinet context.
- Patient-plan review responded to keyboard Space. The earlier pointer timing observation was not reproduced as a persistent failure; it remains unverified rather than declared repaired.
- Loaded the built-in fictional case, confirmed patient review and de-identification, and downloaded the actual HTML handout. Its five sections, fictional label, restrictive CSP and absence of scripts/external resources/internal billing-economic appendices were inspected. See EXPORT_VERIFICATION_0.26.0.json.
- Local file rendering was denied by browser URL policy. No workaround attempted; print/PDF and downloaded-file visual checks remain open.

## Code fixes

Loading the fictional case now resets payer inputs, economic events, confirmed MTPs and medication cabinet along with encounter data. Unrelated business and clinical-workspace drafts are not cleared by this action; the separate Clear all action remains available.

Changing plan text in SOAP or the connected patient studio now revokes the prior agreed-plan status as well as review approval. Unagreed text is withheld from the patient preview until agreement is renewed; export still requires review and de-identification. This is an explicit review-state fix, not a clinical recommendation change.

## Source audit

All 14 directory destination URLs were retrieved from primary provider pages on October 25. Thirteen identified the expected calculator/instrument content; PREVENT returned the provider heading, with its embedded calculator unverified. The NIDDK page confirmed the adult/pediatric calculator directory. No numerical outputs or clinical validity were independently validated. Link-only use does not reproduce equations or instrument questions. See CALCULATOR_DESTINATION_AUDIT_0.26.0.json.

## Automated evidence and limits

All 408 JavaScript tests and 24 Python tests passed. AUTOMATED_TEST_RESULTS_0.26.0.txt records the full suite. New regressions cover previous payer/medication isolation, renewed plan agreement, cross-workspace changes and review/export gating. Packaging verifies hashes, ZIP integrity and every upload batch below 100 files.

New v0.26 fixes require deployed browser acceptance. This run does not certify all tools, mobile layouts, print/PDF, all source currency, clinical dosing, payer eligibility or the two unimplemented core applications. No full track is closed.
