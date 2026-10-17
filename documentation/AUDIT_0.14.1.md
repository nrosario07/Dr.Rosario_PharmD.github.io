# Focused audit — October16,2026

## Verified baseline

Deployed entrypoint identifies0.14.0. GitHub main baseline9083614deb44f4feb9ac1305520f457cc975e245. Critical local source hashes matched repository blobs before editing: app.js, cpa-workspace.js, decision-support.js, decision-workspaces.js, styles.css and release-manifest.json. No full all-file byte-parity claim.

## Browser tests before this change

Fictional adult-T2DM Ozempic1mg weekly→Mounjaro generated2.5mg weekly start on2026-10-23 from last dose2026-10-16 and conditional four-week review. Changing GI tolerance cleared the result; active GI symptoms caused review-required with no calendar. No real patient data.

Public metoprolol lookup returned36 RxNorm identities; selecting866514 retrieved ten FDA label choices. Label selection and cabinet addition worked. The first attempted note-navigation verification used a browser navigation command that may reload the document, so full cross-route state acceptance was not established by that attempt. Follow-up must use the application's own links.

Source inspection found a stale0.4/0.6 provenance header and inactive-coefficient wording on the active source route. A hosted-calculator description was also stale in an inactive profile template (the live four-pillar hub overrides that template); it was removed for consistency without claiming it was displayed live.

## Change and local verification

293 Node tests pass, including section navigation preserving route/encounter, four-pillar/task hub, phase/status descriptions and conditional switch controls. DOM-harness tests are not browser visual tests. No clinical rule was altered. New workflow/source-status copy preserves explicit pilot limits rather than implying phase completion.

The new UI requires deployed acceptance: task hub, Sources phase overview, CMM jump focus/state preservation, relevant switch controls, medication→cabinet→SOAP→patient plan using app links, browser-console errors and layout overflow. Print/mobile and independent clinical/coding review remain separate unless explicitly recorded as completed.

The connected GitHub change will preserve the baseline tree and modify only selected files. Remote CI workflow is absent in the inspected baseline; local293-test success must not be labeled GitHub CI success. Clinical source monitoring and independent clinical validation are not completed by this UI patch.

## Follow-up browser acceptance and publication result

Using the app's own links, the public metoprolol identity→FDA label→cabinet→SOAP objective flow passed. Cabinet medicine, actual fictional regimen and use status survived routing. A completed fictional plan/monitoring/follow-up/education draft generated the patient plan and enabled its download control after explicit patient-plan review. Actual download/print were not exercised in this run. Three ordinary adherence/cost/access phrases produced the expected unconfirmed MTP candidates. These observations are on deployed0.14, not new0.14.1.

The earlier synchronization ambiguity was resolved by observing the explicit sync confirmation and the resulting SOAP cabinet block. No cabinet-loss defect was established. Browser navigation commands are not a substitute for testing the application's own links.

GitHub create-tree write was rejected with HTTP403, “Resource not accessible by integration.” No branch, commit, PR or deployed source change was created. The rejection is a connector authorization limitation, not evidence that local tests failed. Publication and new0.14.1 browser acceptance remain blocked on an authorized write path or owner upload. The package is the completed reviewable result; no additional issue reports are needed to reproduce this work.
