# ClinicalRx phase checklist —0.19.3

**Current: Phase02 medication/evidence intelligence, Phase06 education discovery and Phase09 monitoring installation readiness. Full platform incomplete.**

| Phase | Delivered | Remaining / blockers |
|---|---|---|
|00 Profile and foundation|Professional profile, four pillars, LinkedIn-only contact, task-oriented hub, unified local finder, pillar filtering, compact navigation and readable clinical headings|Narrow-screen/keyboard/visual regression across every tool|
|01B Privacy and reporting|Tab-only drafts, no automatic save/restore, no-PHI export gates, honest dispatch feedback and structured exports|Institutional EHR adoption/review; longitudinal data model intentionally absent|
|01D SOAP/MTP/MDM|Referral-first note, confirmed MTPs, expanded phrase recognition, evidence-backed provisional MDM, patient plan, section navigation|Broad clinical language validation, independent coding review and complete quality specifications|
|01E Economics|Historical intervention-category benchmarks and AMA references|Outpatient/type-specific causal estimates and overlap validation; no realized-savings claim|
|02 Medication intelligence|RxNorm/RxTerms/FDA recovery, labels, enrichment, cabinet, FDA shortage lookup and specialist source cards|Comprehensive interactions, prices, complete monographs and broader public data normalization|
|03 Calculator directory|Unified outbound calculators/conversions/screenings; no hosted PREVENT|Continuing destination/source checks|
|04 Clinical workflows|Bounded anticoagulation, oral/LAI/exact IR-ER switch pilots, nine GLP-1 directions, tiered off-label options and three new formulation directions; numbered conditional form|Independent clinical review, expanded exact-product pairs, device/clock-time complexities and broader browser fixtures|
|04D Diabetes application|Basic incomplete application removed|Complete current-source normalized decision application and independent validation|
|05 Professional practice|Prefilled Texas CPA, identity/term controls, annual review rule, readiness and practice planning|Local physician/legal approval, institutional privileges and payer-specific contracts|
|06 Education|SOAP-derived patient draft and reviewed printable HTML handout|Bilingual handouts, devices, quizzes and teaching studio|
|07 Adherence/quality|Public PQA context and VAS/claims interpretation; limited measure leads|Licensed denominator/exclusion rules and independent measurement validation|
|08 Residency|Later-build scope documented|Program-type standards/recruitment/orientation/audit implementation|
|09 Release/source governance|Local manifest/tests, atomic verified ZIP packaging, review-only monitoring scripts; public phase overview|GitHub CI/workflow installation and reliable source-review queue; independent clinical review; no automatic clinical-rule publication|

## Ordered next steps
1. Upload 0.19.1 in numbered batches; printable handout download and review invalidation passed on 0.19.0. Print/PDF and mobile acceptance remain open.
2. Install both missing workflows using SOURCE_MONITOR_SETUP.md and verify hosted runs/report.
3. Finish mobile/keyboard and broader switch/anticoagulation browser regression.
4. Expand exact-product normalized evidence and switching coverage after review.
5. Complete bilingual/device education and scoped diabetes application; residency remains later.

## October 22 checkpoints
- [x] Deployed 0.18.2 stale-cabinet warning and export refusal verified.
- [x] Re-sync/export recovery verified and actual downloaded SOAP text inspected.
- [x] Printable handout implemented and regression-tested.
- [ ] Deployed 0.19.0 handout and print visual acceptance.
- [ ] Mobile and keyboard acceptance.
- [ ] Both workflows installed and hosted runs verified.

## When is it complete?
A phase closes when its specified coverage, tests, deployed browser acceptance and required clinical/licensing review pass. No reliable calendar completion date exists while medication/condition coverage is open-ended, reviewer availability is unscheduled and residency scope is undefined. Maintenance continues after feature completion; no automatic background development is promised.

## Optional materials for later work
- Switching: 5–10 fictional cases specifying exact products, regimen, reason and expected source-supported outcome.
- Patient education: original handouts you have rights to adapt, preferred English/Spanish wording, priority devices.
- SOAP/MDM: fictional complete notes with independently reviewed expected coding/MTP outputs.
- Residency: program type and intended accreditation standards cycle.
No additional material blocks the current technical release.

## Public progress bars
11 of 13 tracks have initial capabilities (including pilot/reference/maintainer tools). 0 of 13 are formally closed with full documented acceptance. Equal-weight track counts are not overall percent complete, clinical validation or effort estimates. The dashboard lists every remaining gate. Current release adds progress visibility, not new clinical coverage.


## 0.18.1 workflow checkpoint

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

## October 24 checkpoints
- [x] Deployed handout download and review invalidation.
- [x] Upload batching below 100 files, all site assets together, byte and CRC validation.
- [ ] Print/PDF and mobile visual acceptance.
- [ ] Hosted monitoring/CI installation and successful runs.

## 0.19.2 checkpoint
- [x] Deployed 40-file integrity check.
- [x] Browser metoprolol generation and stale-result invalidation.
- [x] Full-public-file manifest and repeatable deployment verifier.
- [ ] Hosted monitoring/CI, print/mobile, comprehensive clinical review.
- [ ] Later business/video studio: deferred until current phases complete; see BUSINESS_EDUCATION_FUTURE.md.

## 0.19.3 checkpoint
- [x] 47 intended deployed public files match.
- [x] Procedure selector and elective DOAC/urgent-context browser checks on observed runtime.
- [x] Runtime mismatch detection and build version-consistency checks.
- [ ] Consistent deployed runtime acceptance; browser still displayed 0.19.1 during audit.
- [ ] Mobile/print, hosted monitoring, broad clinical acceptance.
- [x] Future AI/Canva source-to-content workflow specified; generation integrations not implemented.
