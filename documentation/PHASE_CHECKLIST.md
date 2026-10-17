# ClinicalRx phase checklist —0.16.0

**Current: Phase00 navigation refinement delivered; Phase04 clinical workflow expansion remains partial. Full platform incomplete.**

| Phase | Delivered | Remaining / blockers |
|---|---|---|
|00 Profile and foundation|Professional profile, four pillars, LinkedIn-only contact, task-oriented hub, unified local finder, pillar filtering, compact navigation and readable clinical headings|Narrow-screen/keyboard/visual regression across every tool|
|01B Privacy and reporting|Tab-only drafts, no automatic save/restore, no-PHI export gates, honest dispatch feedback and structured exports|Institutional EHR adoption/review; longitudinal data model intentionally absent|
|01D SOAP/MTP/MDM|Referral-first note, confirmed MTPs, expanded phrase recognition, evidence-backed provisional MDM, patient plan, section navigation|Broad clinical language validation, independent coding review and complete quality specifications|
|01E Economics|Historical intervention-category benchmarks and AMA references|Outpatient/type-specific causal estimates and overlap validation; no realized-savings claim|
|02 Medication intelligence|RxNorm/RxTerms/FDA recovery, labels, enrichment, cabinet, topic navigation and quieter reference UI|Comprehensive interactions, prices, complete monographs and broader public data normalization|
|03 Calculator directory|Unified outbound calculators/conversions/screenings; no hosted PREVENT|Continuing destination/source checks|
|04 Clinical workflows|Bounded anticoagulation, oral/LAI/exact IR-ER switch pilots, nine GLP-1 directions, tiered off-label options and three new formulation directions; numbered conditional form|Independent clinical review, expanded exact-product pairs, device/clock-time complexities and broader browser fixtures|
|04D Diabetes application|Basic incomplete application removed|Complete current-source normalized decision application and independent validation|
|05 Professional practice|Prefilled Texas CPA, identity/term controls, annual review rule, readiness and practice planning|Local physician/legal approval, institutional privileges and payer-specific contracts|
|06 Education|SOAP-derived patient draft|Bilingual handouts, devices, quizzes and teaching studio|
|07 Adherence/quality|Public PQA context and VAS/claims interpretation; limited measure leads|Licensed denominator/exclusion rules and independent measurement validation|
|08 Residency|Later-build scope documented|Program-type standards/recruitment/orientation/audit implementation|
|09 Release/source governance|Local manifest/tests, atomic verified ZIP packaging, review-only monitoring scripts; public phase overview|GitHub CI/workflow installation and reliable source-review queue; independent clinical review; no automatic clinical-rule publication|

## Ordered next steps

1. Deploy 0.16.0; browser-test finder search/filter/reset, mobile layout and keyboard navigation. Finish 0.15.0 positive/negative switch and export browser acceptance. Clinical logic still needs independent clinical review.
2. Expand exact-product antidepressant/antipsychotic and other switch coverage only with direction-specific rules, source dates and boundary fixtures. No assumed inverse dose maps.
3. Broaden structured medication/condition MTP checks; validate coding candidates independently.
4. Continue medication-data normalization and education; full diabetes and residency applications remain later phases.

## October17 release evidence

- Repository index and release manifest identify0.14.2; manifest matches the local baseline. This is not an independent fetch/hash of every remote asset.
- Browser verified0.14.2: four-pillar/task navigation; fictional metoprolol50mg BID→ER100mg daily; reporting privacy gate correctly states download not requested.
- Local0.15.0:337 automated tests pass. New UI and clinical options are not yet browser accepted. No direct GitHub publication performed; prior integration write403 remains an unresolved access blocker.
- No complete-platform or complete-drug-catalog claim. Phase04 progresses; it is not complete. Public-source monitoring queues human review and never publishes new dosing automatically.
