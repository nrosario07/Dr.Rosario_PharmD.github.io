# ClinicalRx 0.19.0 — printable patient education

Assessment date: October 22, 2026 (America/Chicago).

## Delivered
- Printable patient handout from the same agreed SOAP plan used by the text draft. Large headings, five sections, readable spacing, responsive layout and print styles; open the downloaded HTML locally and use Print / Save as PDF.
- Requires a complete agreed plan, clinician review and the existing no-PHI export gate. Form edits revoke review; stale cabinet protection also applies. No medication instruction is inferred from the cabinet.
- Handout escapes entered text, loads no remote assets/scripts, preserves the existing plain-language transformation rules, and excludes billing/economic/assessment/objective metadata. No promised or independently validated reading grade.
- Education Studio fields now use explanatory labels and point to the reviewed handout export in SOAP.
- Mobile menu Escape closes the menu and returns keyboard focus to its button. Narrow-screen brand spacing and form-width constraints improved. Mobile behavior still needs device/browser acceptance.

## Deployed audit: v0.18.2
GitHub manifest and live footer report 0.18.2. This session did not independently hash every deployed asset.

Browser-tested fictional scenario: public metformin RxNorm lookup, selected RxCUI 861007 and Ascend label; added product and synced cabinet. Editing regimen produced the stale warning. SOAP showed its warning and refused Download .txt with an explicit mismatch message. Following the cabinet link, re-syncing and returning to SOAP cleared the warning. After no-PHI confirmation, Download .txt succeeded. Downloaded file was read and contains the updated fictional once-daily regimen. This is workflow verification, not a completed clinical encounter or dosing recommendation.

Both .github/workflows/source-monitor.yml and .github/workflows/release-check.yml returned 404 from GitHub. Neither workflow is active/verified. Installation instructions remain in SOURCE_MONITOR_SETUP.md. No remote writes or workflow installation occurred.

## Tests and limits
353 JavaScript tests passed; five Python governance tests passed. New tests verify handout completeness/review/privacy gates, HTML escaping, instruction preservation and exclusion of internal data. ZIP contents and public manifest checked during packaging.

Unverified: deployed v0.19.0 handout rendering/printing; mobile layout and Escape behavior; whole-site keyboard acceptance; hosted workflow execution and source baseline; broader drug/clinical coverage. No clinical algorithms, dosing rules or billing eligibility rules changed.

## Phase status
Phase02 connected workflow acceptance advanced: stale-cabinet refusal and recovery now browser-tested. Phase06 education implementation advanced: reviewed printable handout added. Phase00 responsive/keyboard refinements remain pending deployed acceptance. Phase09 blocked on workflow installation and hosted execution. 11/13 tracks have initial capabilities; 0/13 tracks fully accepted. No comprehensive completion claim or final completion date.

Next: upload and accept the handout and mobile changes; install/run both workflows; broaden switch and anticoagulation browser scenarios; then exact-product evidence/data expansion.

Visual audit follow-up: standardized medication/patient action buttons and next-step links after observing default browser button styling in the deployed cabinet. New styling requires deployed visual acceptance.
