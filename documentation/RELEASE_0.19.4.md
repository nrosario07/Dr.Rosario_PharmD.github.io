# ClinicalRx 0.19.4 — patient-plan readability and corrected release audit
October 24, 2026

## Correction to earlier reports
The old footer was hard-coded to 0.19.1. It was not evidence that an older app was executing. Earlier v0.19.2/0.19.3 reports overstated a runtime mismatch based on that footer. The actual cause was missed visible-label updates. The version-consistency guard remains useful, but is not evidence that a cache problem existed.

## Audit of deployed v0.19.3
- All 47 intended public files match the local v0.19.3 manifest.
- Browser HTML release metadata and application-rendered dashboard both show 0.19.3; startup mismatch warning is hidden. Footer/loading labels were stale.
- Keyboard Skip to content moves focus to main successfully.
- GitHub .github/workflows directory still returns404. Scheduled source monitoring/CI not verified installed.
- Focused audit, not all-tool clinical acceptance. Earlier workflow checks remain historical evidence.

## Implemented
- Footer/loading labels corrected to release0.19.4; build validator now checks these labels as well as metadata, asset URLs and app version.
- Patient-plan preview uses five readable numbered cards: health, plan, monitoring, follow-up and teaching. Plain text remains in an expandable view.
- Preview uses the same agreed SOAP-derived sections as the handout; pending recommendations are suppressed, text is escaped, medication quantities/negation preserved and clinician-only assessment is excluded.
- Existing completeness, review invalidation, cabinet consistency and no-PHI export safeguards retained. No storage, remote generation, clinical rule or dose changes.

## Testing
357 JavaScript tests and 9 Python tests passed. Tests cover preview escaping, pending-plan suppression and prior workflow gates. Manifest validation and ZIP CRC/byte/batch checks passed. New visual preview has not been browser-tested after deployment. Mobile/print/PDF, full keyboard audit, comprehensive clinical validation and monitoring runs remain open.

## Phase checklist
Phase00: version-label and keyboard acceptance checkpoint.
Phase06: patient-plan presentation improved; deployment visual acceptance remains required.
Phase09: integrity acceptance passed; monitoring installation blocked.
Initial capabilities 11/13; complete phase acceptance 0/13. Full platform incomplete; no defensible completion date yet.
Next: deploy and visually accept patient-plan cards; install workflows per SOURCE_MONITOR_SETUP.md; complete mobile/print and broader clinical workflow acceptance before expanding clinical rules.

## Upload
Extract the packet. Upload CONTENTS of each numbered batch at repository root, preserving paths. Commit each batch separately. Do not upload wrappers or ZIP itself. Do not delete repository. Pages remains main /docs. Each batch is below100files. Read START_HERE.txt for actual counts. No remote repository writes performed by this audit.
