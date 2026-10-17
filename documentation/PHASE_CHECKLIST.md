# ClinicalRx phase checklist —0.14.2

**Current: acceptance/usability pass across Phases00,01D,02,04 and09. Full platform incomplete.** Prior historical release details remain in their release/audit documents; this is the current checklist.

| Phase | Delivered | Remaining / blockers |
|---|---|---|
|00 Profile and foundation|Professional profile, four pillars, LinkedIn-only contact, task-oriented hub and readable clinical headings|Narrow-screen/keyboard/visual regression across every tool|
|01B Privacy and reporting|Tab-only drafts, no automatic save/restore, no-PHI export gates, honest dispatch feedback and structured exports|Institutional EHR adoption/review; longitudinal data model intentionally absent|
|01D SOAP/MTP/MDM|Referral-first note, confirmed MTPs, expanded phrase recognition, evidence-backed provisional MDM, patient plan, section navigation|Broad clinical language validation, independent coding review and complete quality specifications|
|01E Economics|Historical intervention-category benchmarks and AMA references|Outpatient/type-specific causal estimates and overlap validation; no realized-savings claim|
|02 Medication intelligence|RxNorm/RxTerms/FDA recovery, labels, enrichment, cabinet, topic navigation and quieter reference UI|Comprehensive interactions, prices, complete monographs and broader public data normalization|
|03 Calculator directory|Unified outbound calculators/conversions/screenings; no hosted PREVENT|Continuing destination/source checks|
|04 Clinical workflows|Bounded anticoagulation, oral/LAI/exact IR-ER switch pilots, seven GLP-1 directions; clearer context-sensitive forms|Independent clinical review, expanded exact-product pairs, device/clock-time complexities and broader browser fixtures|
|04D Diabetes application|Basic incomplete application removed|Complete current-source normalized decision application and independent validation|
|05 Professional practice|Prefilled Texas CPA, identity/term controls, annual review rule, readiness and practice planning|Local physician/legal approval, institutional privileges and payer-specific contracts|
|06 Education|SOAP-derived patient draft|Bilingual handouts, devices, quizzes and teaching studio|
|07 Adherence/quality|Public PQA context and VAS/claims interpretation; limited measure leads|Licensed denominator/exclusion rules and independent measurement validation|
|08 Residency|Later-build scope documented|Program-type standards/recruitment/orientation/audit implementation|
|09 Release/source governance|Local manifest/tests, atomic verified ZIP packaging, review-only monitoring scripts; public phase overview|GitHub CI/workflow installation and reliable source-review queue; independent clinical review; no automatic clinical-rule publication|

## Ordered next steps

1. Accept deployed0.14.2 using actual app navigation; record browser, automated and unverified results separately.
2. Fix reproduced defects and simplify remaining long workflows before new clinical algorithms.
3. Expand exact-product switch coverage and structured medication/condition MTP checks with controlling sources and boundary fixtures.
4. Continue richer medication data and education; complete diabetes and later residency work only after their own acceptance gates.

No phase is complete merely because the interface renders or tests pass. Human clinical, coding, legal and institutional reviews remain named blockers where applicable.

## Current run result

- Browser accepted on deployed0.14: GLP-1 positive/GI refusal, public medication→cabinet→SOAP→patient-plan review, and three MTP phrase candidates.
- Local0.14.2:295 automated tests, syntax and manifest checks passed; task navigation, compact clinical UI and phase overview implemented.
- Publication blocked: GitHub write returned403 “Resource not accessible by integration.” No remote source changes. New0.14.2 browser acceptance remains open.
- Next owner-independent work after write access is available: deploy this prepared release, verify new UI, then proceed through the ordered coverage/validation backlog. Do not claim another clinical phase complete.

## October 17 acceptance update

Browser reproduced on deployed0.14.0: reporting claimed CSV creation while no-PHI gate blocked it. Fixed locally in0.14.2 with blocked, successful-dispatch and failure fixtures. Combined packet includes previously unpublished0.14.1 UI improvements. Phase01B reliability and Phase00 usability remain in progress; next gate is deployed browser acceptance, then structured MTP and exact-product coverage. No new clinical phase is complete.
