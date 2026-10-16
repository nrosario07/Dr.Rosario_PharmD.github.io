# ClinicalRx phase checklist — v0.14.0

**Current: Phase04 GLP-1 switching expansion + Phase01D MTP/MDM refinements + Phase02 reference design. Full platform incomplete;0.14 browser/independent review pending.**

| Phase | Completed in current build | Remaining / blocking evidence |
|---|---|---|
|00 Profile/foundation|Four pillars, free access, LinkedIn-only contact; Pharmacist Practitioner title; unified credentials;25 CPA scope groups|New mobile/accessibility/layout browser QA|
|01B Reporting/privacy|Tab-only input, no save/restore; no-PHI download/copy/print gates; current encounter structured exports|Governed longitudinal model intentionally absent; institutional EHR import approval|
|01D CPA SOAP/MTP — active|Referral and physician-established diagnoses first; ROS/PE/objective categories; confirmed local MTP suggestions; patient plan; time comparison; quality bullets; conditional incident-to fields|First bounded MDM evidence pilot delivered; independent narrative/coding validation remains; broader MTP inference; current licensed code/quality acceptance fixtures|
|01E Economics — partial|16 category-matched historical numeric benchmarks, AMA sources, methods/contexts; hypothetical deduplicated subtotal and business reference|All36 taxonomy-specific outpatient economic estimates; comparable multi-study pooling; local causal/overlap validation|
|02 Medication intelligence|RxNorm/openFDA/enrichment, exact-label provenance,16-topic coverage, cabinet/sync; source-host errors/fallback links; overflow CSS|RxTerms/FDA recovery and refined medication reference layout delivered; intermittent user fetch failure cause unresolved; complete monographs/DDI/prices; Orange Book/PMC/device integrations; broad identity coverage beyond RxTerms subset|
|03 External tools|One directory; Child-Pugh/MELD added; no hosted PREVENT/generic scores|More CPA-relevant validated destinations and continuing link checks|
|04 Clinical workflows — active pilot|Submit controls; oral switch pilot; ARISTADA/SUSTENNA label-initiation calendars; reviewed anticoagulation calendar/rationale; FDA relationship table|Additional stimulants/BP/IR-ER products beyond the exact-label pilots, broader oral and LAI/depot/missed-dose rules; unrestricted bridging; independent clinical/browser/print fixtures|
|04D Diabetes|Basic tool removed|Complete ADA app remains blocked on normalized sources, reviewed decisions and fixture validation|
|05 Professional practice|Prefilled CPA standard text, identity/term controls and annual review enforcement; scope/source limits; existing Texas authority/code inventory; FQHC/locality labels; informational contracting steps|Executed local agreements/privileges and product-specific contracts; legal/institutional review; FQHC payment modeling|
|06 Education|One SOAP-derived Patient Plan Studio and review gate|Bilingual/device handouts, quizzes, memory-palace studio|
|07 Adherence/quality|Defined PQA contexts, VAS number bubble, claims/self-report interpretation, limited SOAP measures|Licensed denominator/exclusions and current-year validation; no certified HEDIS/Stars output; completed MMAS-8 validation not supplied|
|08 Residency|Scope retained|Later ASHP program-type recruitment/orientation/audit build|
|09 Monitoring/release|Review-only source monitoring/rebuild scripts; manifest and CI packet supplied|Remote .github folder still absent: upload workflows; confirm first run; never auto-publish changed clinical rules|

Next: deploy v0.12 and complete the browser acceptance checklist in AUDIT_0.12.0.md. Then prioritize independent clinical review, broader exact-product switch fixtures and structured MDM/economic evidence gaps. No new clinical rule is auto-published from source monitoring. Workflow implementation is delivered; production acceptance and full-platform completion remain open.

### Focused defect sequence — v0.14.0

1. Medication identity availability: FDA fallback/direct action implemented; 241 automated tests and real FDA recovery runtime check passed. User-network root cause unresolved; post-upload browser acceptance open.
2. Anticoagulation procedure choices: reported by user; diagnosis/fix/browser acceptance pending. Prior generated-calendar unit tests do not establish that dropdown works for the user.
3. Taper & Switch result rendering: reported by user; diagnosis/fix/browser acceptance pending. All-inclusive drug coverage is not delivered and must not be claimed. Metoprolol pure-rule test passing does not prove the rendered workflow works.

No next phase is claimed complete by this patch.

### Current release acceptance and next work — v0.14.0

| Item | Status | Next / blocker |
|---|---|---|
| MDM candidate inference | First bounded local evidence pilot implemented; automated tested | Independent coding fixtures, broader vocabulary, deployed acceptance; no automatic high level |
| Switch workflow | Existing metoprolol example browser-passed; improved input/result UI implemented | New interface browser acceptance; pair coverage still limited |
| Anticoagulation procedure picker | Nine choices and selection/category worked in deployed audit | Original user failure not reproduced; monitor with exact search/device details if repeated |
| Medication lookups | User reports recovery; previous lookup fix preserved | New visual/topic/shortcut browser regression |
| Phase completion | Not complete | Do not expand into new disease algorithms before current-release acceptance |

Next ordered increment: deploy0.13 and run its acceptance checklist; address reproduced defects; then expand reviewed switch-rule coverage (with exact product, population, source date and boundary fixtures), followed by broader MDM audit evidence. Larger medication datasets/pricing and the full diabetes app remain separate incomplete phases.

### Current0.14 acceptance and build order

- Completed locally: seven GLP-1 switch directions with distinct label/expert/research provenance; broadened explicit MTP phrasing; clarified time/MDM separation; quieter medication styling;289 passing automated tests.
- Browser verified on deployed0.13: MDM candidate with evidence; reproduced three missed MTP phrases. No claim of new0.14 browser testing.
- Next: deploy0.14 and complete AUDIT_0.14.0.md acceptance; resolve reproduced defects; independent clinical/coding review; then additional exact-product switch families and structured medication/condition MTP checks.
- Still blocked/incomplete: all-inclusive switches, autonomous narrative coding, current licensed quality specifications, validated patient-specific economic avoidance, complete diabetes app and later residency platform.

No phase is declared complete from added dropdown entries or automated test count alone.
