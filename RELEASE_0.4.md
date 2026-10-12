# Clinical tools 0.4 — compact workflows, working modules and public APIs

Prepared October11,2026 (America/Chicago). Supersedes the 0.3.1 upload package. Existing GitHub integration writes remain blocked; no live deployment is asserted. Remote main was rechecked at b698585 (Add files via upload); the professional profile, MTP labels and public CV match and are preserved. The update does not delete unrelated existing repository files.

## Fixed and simplified

Owner screenshots image4–7 were inspected locally. The general text-input width applied to radios, pushing labels beyond their fieldsets. A specific width/flex rule now keeps radio/checkbox controls small and labels wrapping within the card. Help text is compact. MTP shows essential clinical fields; encounter/teach-back detail, patient output, economics, coding, contract review and reporting expand on demand. Business shows six core planning sections, with financial/governance details expandable. Output includes concise improvement prompts; detailed evidence remains available in its panel.

## Working additions

- Four pillars: Clinical Care, Drug & Evidence Intelligence, Professional Practice, Education.
- Universal medication page: opt-in public RxNorm identity and selected-RxCUI openFDA labels, exact-label selection, retrieval timestamps, short label excerpts and original DailyMed/PubMed/MedlinePlus/PurpleBook links. No patient-note input is sent. DailyMed browser CORS was not confirmed, so direct links are used.
- Medication Adherence Toolkit: educational single-medication PDC and uncapped fixed-window MPR with explicit method/window, overlap handling and data-review gates; Rosario's original 0-to-10 question and observed study associations. No calibrated individual adherence probability is invented.
- Anticoagulation Command Center: CHA2DS2-VASc/HAS-BLED point calculations, unknown-factor gates and source-linked DOAC/procedure worksheet.
- Universal calculator library: BMI/CrCl index plus 2021 race-free CKD-EPI eGFR, percent total body-weight loss, PHQ-9 and adherence/AF links.
- ClinicalRx Taper & Switch: clinician-selected slow benzodiazepine dose-reduction arithmetic and a switch-review worksheet. No diazepam conversion, medication switch, formulation rounding or prescription.
- HEDIS/Stars Gap Closer: measure/year/source/eligibility/action/closure-evidence organizer. No licensed value sets, certified denominator or automatic closure.
- Education studio: original patient handout draft, reading-level estimate, SOAP memory palace and an MTP knowledge check. Validated bilingual workflows remain future work.
- Guideline Registry: twenty condition workspaces with explicit source edition, jurisdiction, review due date and readiness. Diabetes/insulin, obesity/GLP1, lipids, hypertension, COPD/asthma, psychiatric switching, CKD/HF/AF, smoking, vaccines, HIV/OIs, HCV, endocrinology, dermatology/biologics and devices have source-linked review sheets; full prescribing algorithms are not claimed complete.
- Structured E/M review: eligible commercial/MA established-patient candidate from user-reviewed MDM two-of-three or qualifying time, only after actual SOAP/author/scope/entity and written payer recognition are documented. Original Medicare pharmacist-only office E/M uses its separate rule. Missing higher-level criteria prompt actual-work review, never fabrication.

## Source monitoring

A ChatGPT source-change automation is enabled for Monday8am America/Chicago. It checks controlling public sources and distinguishes proposals, effective rules, safety changes and inaccessible sources. Alerts require review; they do not overwrite published clinical rules. Optional .github/workflows/source-monitor.yml runs Mondays14:00UTC after upload and retains a public-source hash/availability artifact. The source checker uses no patient/private files and never updates the clinical bundle. Hash changes may be cosmetic. The initial baseline is a byte comparison baseline, not evidence validation.

## Verification

97 automated tests passed at preparation: formula fixtures, score/unknown/exclusion boundaries, PDC overlap/window/duplicates, MPR semantics, owner-study interpretation, PHQ9 safety flag, taper limits, E/M gates, API consent/query isolation/cache/errors, radio-width contract, old and new routes and form events. Public API probes returned HTTP200 and Access-Control-Allow-Origin:* for RxNorm and openFDA. DailyMed returned HTTP200 without that CORS header. Browser layout/accessibility/download/print QA remains pending under this environment's browser-preview limitations. Tests are not independent clinical/payer certification.

## Upload

Extract ClinicalRx_0.4_GitHub_Update.zip. Upload docs, documentation, scripts, tests and README.md to the repository root, preserving paths. Optional automation files belong at .github/workflows/source-monitor.yml; Windows may hide that folder, and web upload may need a separate manual file creation at the exact path. Uploading only docs updates the public website but omits repository documentation/tests and source-monitor workflow. The rebuilt specification is documentation/BUILD_SPECIFICATION.md. Keep Pages main:/docs. Commit message: Fix compact workspaces and add ClinicalRx clinical modules.

## Fictional-case review after deployment

Check radios and long labels at desktop/mobile widths. Confirm essential-first screens and expansion of source/evidence panels. Load the fictional MTP case, generate/review the patient draft, and edit SOAP to verify review/evidence invalidation. Commercial MDM moderate/low/moderate with all actual eligibility evidence should yield conditional99214; missing criteria should block or show the lower conditional reference. Original Medicare must retain its separate office rule.

PDC January1–January31 with fills January1,30 and January20,30: coverage31/31, MPR60/31. Confirm possession is not ingestion or official Stars closure. Score9 on owner scale shows the study's48/61 group association, not a personalized79% prediction. eGFR age60/male coefficient/creatinine1/stable IDMS: about86.2mL/min/1.73m2. PHQ9 item9 positive must flag safety assessment even if total is low. Taper10mg/10%/2weeks: first illustrative9mg, next8.1mg, with no rounding or prescription.

Medication lookup must make zero requests while disabled. Enable public lookup, find a drug, select exact identity then label, and verify product/effective date against DailyMed. Changing identity or leaving the route must not display a stale label response. No clinical data may appear in a request. Review Guideline Registry overdue/readiness labels and source-monitor artifacts before updating rules.
