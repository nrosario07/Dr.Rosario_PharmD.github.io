# Dr. Rosario / ClinicalRx build specification — v0.6.0

## Product and audience

Dr. Norbert Rosario, PharmD, BCPS, BCACP owns the professional brand. ClinicalRx is the separately presented free platform for healthcare professionals and students, with reviewed patient-facing materials derived from clinical encounters. Professional navigation: About → Experience → Clinical Practice → Research → Publications → Teaching → Presentations → Projects → Clinical Tools → CV → Contact. LinkedIn https://www.linkedin.com/in/norbertrosario/ is the only public contact method. Do not expose personal CV phone/email, license identifiers or private credentialing documents.

Four pillars work independently and through explicit local transfers: Clinical Care; Drug & Evidence Intelligence; Professional Practice; Education. Keep every module's actual readiness visible. A source-linked worksheet is not a finished treatment algorithm.

## Architecture and deployment

Buildless HTML/CSS/classic JavaScript, served from main:/docs by GitHub Pages. No paid backend, account, cloud LLM, analytics or persistent patient storage. Hosted index uses CSP self-only script/style plus specific public API origins. Release asset query0.6.0 prevents cached older scripts. startup.js provides visible resource/runtime initialization errors.

Source modules:

- app.js: professional profile, navigation, shared state, route marker, output/copy/download/print helpers.
- core.js: note and simple financial primitives.
- clinical.js/rules.js: guided clinical/reference/payer/economic/readability logic and pinned reference bundle. Existing0.4 reference version is distinct from release0.6.
- workspaces.js: SOAP/MTP, business outline, diagnosis/service references, review gates and exports. Essential SOAP section handles browser-serialized ampersands correctly.
- platform.js/module-data.js/modules.js: four-pillar hub, module filter/readiness, adherence, quality, reference worksheets and older pure calculations.
- drug-api.js: public medication-only API client, origin allowlist, omitted credentials/referrer, bounded24-hour tab cache and15-second timeout.
- advanced.js/advanced-platform.js: bounded conversions, FIB-4, perioperative calendar, inhaler review, cabinet review and medication retrieval UI. Calculator inputs scoped by route, not one shared age/context form.
- next-phase.js/next-platform.js: PHQ-9/GAD-7, PREVENT readiness, stable adult T2D review, practice capacity, reviewed findings-to-SOAP transfer.
- icd-index.js:74,879 FY2027 billable ICD-10-CM descriptions; local search only.
- docs/data: public registries and provenance; documentation: current specification, audit, phase checklist and historical specifications; scripts/tests/.github: reproducible packaging, tests and source monitoring.

Shared encounter, billing, MTPs, economics, business, cabinet and tool form state remain in memory. Advanced calculators and next-phase tools have per-tool namespaces. Clear encounter also clears cabinet and shared tool-state namespaces; refresh clears the complete tab. The older independent adherence/quality worksheet form memories are not a cross-patient record store; review/reset their contents separately or refresh before a new case. No claim of HIPAA-compliant hosting or institutional approval is made.

## Medication intelligence and cabinet

Public search on Enter or Look up resolves returned RxNorm identities. Choose the exact RxCUI, then one product label; label set UUID/effective date and exact DailyMed link accompany the sections. Labels expose returned text for indication, MOA, dose/administration, strengths, boxed warning, contraindications, warnings, adverse effects, interactions, populations and counseling. Missing sections remain unavailable and require original-label review; absent API text does not establish absence of risk.

RxClass classification type/vocabulary is displayed; disease/chemical/structure classes are excluded from the drug-class presentation. MedlinePlus Connect supplies attributed patient links. PubMed supplies unappraised citation matches. Direct DailyMed browser API CORS is not assumed; exact label links are used. Only public medication name/RxCUI leaves the tab; cabinet combinations, note text, patient facts and calculator inputs are not sent.

Cabinet entries include selected identity/product provenance plus editable reported regimen/use status. Local duplicate and label-mention review is limited, never comprehensive DDI clearance; a label mention can describe no interaction. No flags means no flags within this scope, not safety. Prices and automatically synthesized guideline roles/clinical pearls are not supplied.

Explicit cabinet sync preserves objective text and replaces its marked cabinet block on repeated sync. A compact cabinet snapshot is included in encounter JSON. Later cabinet edits require a new sync; exported files do not update. Sync resets billing documentation/co-sign/MDM evidence. No prescription, diagnosis or adherence is inferred from adding a medicine.

## Calculator and assessment interfaces

Use explicit units, required population/context, missing-versus-zero distinction, source/method, clear result status and clinical limits. New PHQ-9/GAD-7 use original response items over the past two weeks, four selectable0–3 response cards and answered-count feedback. All items are required for total. GAD-7 totals0–21 with5/10/15 severity boundaries. PHQ-9 totals0–27 with existing severity bands; positive item9 prompts timely local-protocol suicide-risk assessment even before total is complete. Difficulty is recorded separately and does not change the score. Neither tool diagnoses a disorder or selects medication. Transfer to SOAP requires explicit clinician review and preserves source/result in encounter.toolFindings; it does not become an agreed patient medication plan.

PREVENT now has eligibility, cardiovascular/kidney/metabolic inputs, Base/uACR/HbA1c/SDI/Full model preparation, external links and separately recorded10-/30-year CVD/ASCVD/HF results. Unknown history and out-of-range values are flagged without clipping. SDI is a decile, not ZIP code. External result cards require verified user-entered results with date/source and eligible inputs;30-year results above59 are suppressed. No native PREVENT risk equation, PREVENT-age or percentile is implemented. The owner must accept the free AHA license and provide the approved versioned source package; then implement exact coefficients/method and verify official fixtures before enabling native calculation. MDCalc informs interaction design, not a license to copy its code or bypass AHA access requirements.

HAM-D remains planned pending verification of a specific clinician-rated17-item version, response anchors and training protocol. Do not substitute PHQ/GAD responses or infer a HAM-D score from free text.

Existing calculators retain their documented bounds: adult BMI, explicit-weight Cockcroft–Gault without empiric SCr rounding, race-free eGFR, FIB-4 stable adult screening without universal fibrosis classification, AF risk-point totals, PDC/MPR educational fixed-window calculations, patient-report VAS associations and scoped conversions. VAS has explicit record action so neutral slider position is not silently scored. Its association and combined PDC/MPR flags are not a validated individual probability model.

## Clinical pathways

Anticoagulation Command Center provides a clinician-reviewed elective dated calendar, not independent prescribing. Explicit interruption, medication/dose, indication/risk/history, adult/kidney/INR/procedure inputs and plan reference are required. Urgent/neuraxial/HIT/active-bleeding/AKI/dialysis/CrCl<30 cases are outside this model. Warfarin bridging is not automatic; specialist exceptions need rationale, approved regimen, INR start criterion, postoperative approval and stop criteria. Future INR/hemostasis stays conditional and no fixed bridge-stop date is predicted. New approved clock-time fields RECORD manually verified last-dose/procedure times and time zone; they do not derive safe drug hold intervals or resolve DST. Original spreadsheet's SCr rounding and automatic syringe assumptions are not copied. Calendar is outside the input section so print CSS can retain it; print layout still needs post-upload verification. Separate finalized clinician/patient orders remain future work.

Adult stable nonpregnant established T2D review collects A1c/date, individualized goal, glucose where known, kidney data, assessed comorbidities, hypoglycemia, current class use, regimen/trials/preferences and affordability. Original ADA2026 prompts identify clinician review priorities for marked hyperglycemia, duplication and risk/access; no product or insulin dose is selected. Acute, unsupported or incomplete contexts remain gated. Every prompt has a source locator. Reviewed findings can be explicitly transferred to assessment, with diagnosis/billing review invalidated. Proposed review prompts are not patient instructions.

Asthma/COPD/device tools retain current-source symptom/grouping/device/teaching review, not brand/dose prescription. Original educational summaries reference primary GINA/GOLD and exact devices; no proprietary figures are redistributed. Other disease modules remain clearly labeled worksheets until their algorithms are verified and implemented.

## Practice development

Business outline keeps six essential teaching sections visible with additional staffing/budget/governance details available. Payer eligibility, scope/CPA, clinic privileges, performed service, documentation, coding and payment are separate. Potential higher commercial E/M and other service families remain reference candidates subject to actual payer recognition/criteria/contracts. Medicare Advantage/PartD/APM are not conflated with Original Medicare PFS. The annual fee subset is not a current claim quote or guarantee of payment. Texas Medicaid benefit/MCO arrangements require actual review; do not claim every pharmacist must use one universal payment route.

New launch/capacity planner uses weekly staff/nonvisit hours, slot minutes, modeled working weeks, referral demand and completion rate. Monthly slots are time-bounded; scheduled visits are the lesser of slots and referrals; completed visits apply completion percentage. Explicit transfer updates completed-visit/staffing/workflow/outcome/milestone assumptions in the business outline without inventing receipts. The2021 Waco example informs onboarding, referral operations, measurable objectives and launch organization; its historical economic/billing assumptions are not current payer authority. Revenue remains supported collections; cost avoidance is modeled evidence, not cash receipts. Full collection-delay/denial/working-capital forecasting remains future.

## Education, reporting and source governance

Education Studio reads/edits shared SOAP assessment, agreed plan, monitoring, follow-up, education and teach-back. Patient plan generation retains clinical medication/dose/timing/negation/conditions, only uses agreed actions, and flags estimated reading grade. Human review is mandatory; grade3–5 is an aim, not a guaranteed result. PHQ/GAD/diabetes findings stay clinician-facing until a separate agreed plan is written. Reviewed Spanish/device handouts, memory palaces, quizzes and ASHP residency-development suite remain later phases.

ICD selection requires encounter date within FY2027 and provider-documentation/index/tabular attestation. Search suggestions are not diagnoses. CPT/HCPCS and measure titles are reference choices, not assigned claims or certified HEDIS eligibility/closure. Local structured JSON/CSV are drafts for institution-approved mapping, not vendor-certified EHR imports.

Source monitoring flags public changes for review and never silently alters clinical rules. Keep jurisdiction/effective/edition/retrieval dates distinct. Clinical rules require primary-source review, provenance and appropriate tests. Preserve review status and explicit unavailable data. Design examples are not controlling medical/payer sources. Do not publish private credentialing/CPA documents or patient records.

## Validation and release management

Read AUDIT_0.6.0.md and PHASE_CHECKLIST.md. Live v0.5.2:16 assets matched package; eleven profile pages and39 distinct tool routes browser-smoke-tested; full public medication→cabinet→SOAP→patient-plan workflow tested with fictional data. New v0.6:137 automated tests passed; local new-release browser preview blocked by cloud file-URL policy. New visual/mobile/keyboard/print/live API regression checks must occur after upload. Do not describe route smoke checks as complete algorithm validation.

Deliver one archive with docs, documentation, scripts, tests and .github kept intact, plus START_HERE instructions. Site-only browser upload uses the ENTIRE docs folder at repository root, never flattened individual files or the ZIP itself. Full GitHub Desktop upload also preserves the source-monitor workflow. Keep Pages main:/docs. No repository deletion is needed. Preserve unrelated owner files and review same-name replacements.

This specification supersedes earlier prose. Historical specification is retained under documentation/history for provenance, not as current behavior. Release versions, reference-bundle versions and clinical-source editions are independent.
