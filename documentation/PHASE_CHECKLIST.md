# ClinicalRx phase checklist — v0.11.0

**Current: Phase01D CPA encounter/MTP redesign + Phase04 LAI initiation pilot. Phase02 remains in progress. Full platform incomplete.** New0.11 browser acceptance awaits upload; deployed0.10 public lookup passed this audit.

| Phase | Completed in current build | Remaining / blocking evidence |
|---|---|---|
|00 Profile/foundation|Four pillars, free access, LinkedIn-only contact; Pharmacist Practitioner title; unified credentials;25 CPA scope groups|New mobile/accessibility/layout browser QA|
|01B Reporting/privacy|Tab-only input, no save/restore; no-PHI download/copy/print gates; current encounter structured exports|Governed longitudinal model intentionally absent; institutional EHR import approval|
|01D CPA SOAP/MTP — active|Referral and physician-established diagnoses first; ROS/PE/objective categories; confirmed local MTP suggestions; patient plan; time comparison; quality bullets; conditional incident-to fields|Validated narrative MDM inference; broader MTP inference; current licensed code/quality acceptance fixtures|
|01E Economics — partial|16 category-matched historical numeric benchmarks, AMA sources, methods/contexts; hypothetical deduplicated subtotal and business reference|All36 taxonomy-specific outpatient economic estimates; comparable multi-study pooling; local causal/overlap validation|
|02 Medication intelligence|RxNorm/openFDA/enrichment, exact-label provenance,16-topic coverage, cabinet/sync; source-host errors/fallback links; overflow CSS|Intermittent user fetch failure not reproduced; complete monographs/DDI/prices; RxTerms/Orange Book/PMC/device integrations|
|03 External tools|One directory; Child-Pugh/MELD added; no hosted PREVENT/generic scores|More CPA-relevant validated destinations and continuing link checks|
|04 Clinical workflows — active pilot|Submit controls; oral switch pilot; ARISTADA/SUSTENNA label-initiation calendars; reviewed anticoagulation calendar/rationale; FDA relationship table|Stimulants, BP agents, IR/ER, broader oral and LAI/depot/missed-dose rules; unrestricted bridging; independent clinical/browser/print fixtures|
|04D Diabetes|Basic tool removed|Complete ADA app remains blocked on normalized sources, reviewed decisions and fixture validation|
|05 Professional practice|CPA builder, scope/source limits; existing Texas authority/code inventory; FQHC/locality labels; informational contracting steps|Executed local agreements/privileges and product-specific contracts; legal/institutional review; FQHC payment modeling|
|06 Education|One SOAP-derived Patient Plan Studio and review gate|Bilingual/device handouts, quizzes, memory-palace studio|
|07 Adherence/quality|Defined PQA contexts, VAS number bubble, claims/self-report interpretation, limited SOAP measures|Licensed denominator/exclusions and current-year validation; no certified HEDIS/Stars output; completed MMAS-8 validation not supplied|
|08 Residency|Scope retained|Later ASHP program-type recruitment/orientation/audit build|
|09 Monitoring/release|Review-only source monitoring/rebuild scripts; manifest and CI packet supplied|Remote .github folder still absent: upload workflows; confirm first run; never auto-publish changed clinical rules|

Next: deploy0.11 and run the documented browser workflow/visual checklist. Then prioritize more LAI coverage with exact product fixtures, structured MDM evidence review, and outpatient economics. Do not silently replace this roadmap with unrelated new tools.
