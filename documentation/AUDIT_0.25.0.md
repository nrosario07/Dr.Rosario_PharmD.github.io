# ClinicalRx audit — 0.25.0

Date: October 25, 2026. Baseline: deployed v0.24.0. This is a focused audit and acceptance increment, not full validation of all 13 tracks.

## Deployment and repository

48/48 public files match v0.24.0 (DEPLOYED_0.24.0_INTEGRITY.json). The GitHub manifest also reports 0.24.0. The release-check, source-monitor and texas-data workflow paths returned 404. A direct attempt to create release-check.yml returned 403, Resource not accessible by integration. No remote mutation succeeded. Workflow copies under documentation do not activate GitHub Actions.

## Browser-tested on v0.24.0

- Texas directory renders nine source files; 340B search returns the formulary drug entry. Its singular count was grammatically wrong and is corrected in 0.25.0.
- Medication search for metformin returns 134 RxNorm identities. Select RxCUI 861007 (500 mg oral tablet), then Ascend label dated 20251218. Label sections and MedlinePlus/PubMed enrichment render.
- Add selected product to the cabinet, enter fictional regimen/use, and append to SOAP. The objective includes the exact identity, regimen and use status.
- Enter fictional assessment, agreed actions, monitoring, follow-up and education. Generated patient preview carries the entered actions. Review confirmation enables download controls; changing follow-up removes approval and disables them again.
- Clear all tab inputs removes the encounter fields.
- About profile visually inspected on desktop: credentials and four-pillar links render. Experience, Clinical Practice, Research, Publications, Teaching, Presentations and Projects reached their expected headings. CV reached Curriculum Vitae; Contact displayed LinkedIn as its only contact method. These are route/render checks, not verification of every profile claim.

An agreement-checkbox action immediately following a sequence of edits did not stick; a settled retry succeeded. Record as an unresolved timing/interaction observation, not a proven fixed defect. No real patient information was used.

## Improvements prepared

External calculator directory gains topic filter, local multi-word AND matching, live count, clear/reset, a recoverable empty state, compact source cards and reduced-motion support. The medication data guide and Texas directory gain direct second-pillar links. Historical checkpoint text is archived; current acceptance uses one 13-track table. No new clinical recommendations, pricing mappings or algorithms are introduced.

## Automated verification

See AUTOMATED_TEST_RESULTS_0.25.0.txt. Tests cover combined directory filters, aliases, empty/reset behavior, HTML injection resistance, source-directory count and hub discovery, plus the existing regression suite. Unit and route harness checks do not verify browser layout or clinical accuracy. Public manifest and ZIP/batch integrity are separately checked during packaging.

## Not verified in this release

New 0.25.0 UI in a deployed browser; mobile/print/PDF; actual exported files in this run; comprehensive keyboard and every-page visual acceptance; all medication API cases, switch pairs and clinical recommendations; current Texas schemas or price integration; successful hosted Actions runs. Texas source access was blocked in the preceding audit and has not been reverified here. No whole phase is closed.
