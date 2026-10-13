# ClinicalRx v0.5.2 usability update

This release improves existing workflows without changing clinical reference coefficients or adding unvalidated treatment rules.

- Taper & Switch shows only medications from the selected conversion family, with insulin-specific units and fields and antipsychotic-specific population confirmation. Changing conversion families clears dose, medication selections and review attestations.
- Cabinet entries have editable actual regimen and actual-use status, plus individual removal. These are local user-entered observations, not prescriptions or verified adherence. Selected product/identity/source remain attached.
- Explicit cabinet-to-SOAP sync preserves other objective text, replaces a marked cabinet block on repeated sync, and copies a compact structured cabinet snapshot into encounter JSON. Changing or clearing the cabinet requires a new explicit sync; previously exported files do not update automatically. Sync invalidates billing documentation/co-sign/MDM evidence. Encounter clear and fictional-case loading clear the cabinet and shared clinical form state.
- Education Studio renders the patient plan body as readable text, followed by reading-grade and warning prompts, rather than a JSON object. It remains a draft requiring clinician review; agreed versus pending plan handling is unchanged.
- Medication-source responses are guarded against attaching to a subsequently reopened medication page. Tab-memory-only and public-medication-query-only network boundaries remain unchanged.

Validation: 115 automated tests, including cabinet idempotent sync, missing-regimen behavior and existing clinical/privacy/payer rules. Route harness is not real-browser visual QA.

## Next build priorities

1. Real-browser workflow verification: medication search → exact label → cabinet editing → SOAP → patient plan; keyboard/mobile layout, API errors and printing. Fix observed defects before broadening algorithms.
2. Unified structured encounter: import/export reconciliation snapshots, per-field source dates and review status, and clinician-approved pulmonary/anticoagulation findings transfer. All patient-specific transfers remain local.
3. Medication intelligence normalization: section-by-section label provenance, interpretable RxClass/MedlinePlus/PubMed displays and evidence appraisal status. Comprehensive DDI and price data require a validated lawful data source; current label mentions are not a complete interaction checker.
4. Anticoagulation: approved exact-clock-time inputs and interval checks, explicit final clinician/patient export review, INR/hemostasis checkpoint handling and calendar-print layout. No guessed stop date or projected INR.
5. Expand bounded clinical modules using current primary guidelines, with population/exclusion guards, dated citations and calculation/workflow tests. Priorities: diabetes/insulin, HTN/lipids, HF/CKD and disease-specific inhaler follow-up. Existing source worksheets are not complete prescribing algorithms.
6. Native PREVENT only after the owner obtains the free AHA licensed source package. Review implementation rights and official reference fixtures before enabling native results.
7. Practice/billing: payer-specific reviewed rule records and current fee benchmarks; maintain separate eligibility, performed service and payment evidence. Do not infer a reimbursable code from narrative length.
8. Education expansion: reviewed device-specific handouts, plain-language editing with protected medicine/dose/timing fields, then reviewed Spanish content. ASHP residency-development tooling remains later scope.

# ClinicalRx v0.5.1 deployment correction

This release preserves v0.5 features and fixes deployment clarity: all entrypoint scripts/styles/icons use `?v=0.5.1` to avoid reusing cached older assets. A startup status and resource/runtime-error notice replace silent failed initialization. Clinical algorithms and their stated limits are unchanged. Four-pillar hub is at `#clinical-tools`.

Canonical public site folder: `docs/`. Older flattened root-level site files are duplicates and are not deployment inputs when Pages uses main:/docs. Replace files together, preserving directory structure. Do not upload extracted individual files from multiple subfolders into the repository root. See `documentation/CLEAN_REINSTALL.md` for browser and GitHub Desktop procedures. Repository name and Pages address remain unchanged.

# ClinicalRx v0.5 build specification

Owner: Dr. Norbert Rosario, PharmD. Professional profile and separately branded free ClinicalRx tools. Contact: LinkedIn only. GitHub Pages serves `docs/`; no paid services, account requirement or backend.

## Current release and shared state

The four pillars have independent routes and use one in-memory encounter. Education Studio reads and edits the same assessment, agreed plan, monitoring, follow-up, education and teach-back as MTP/SOAP. Patient drafts use the existing readability and pending-versus-agreed action guards. Editing invalidates prior review. Medication cabinet reconciliation can be explicitly appended to SOAP objective; it does not assume actual adherence, dispense a prescription or establish a diagnosis.

`advanced.js` holds pure conversion, FIB-4, perioperative calendar, inhaler review and limited interaction-review rules. `advanced-platform.js` supplies route overrides. `platform.js` keeps AF scores, taper planning, adherence, quality and condition worksheets. `workspaces.js` handles SOAP, billing and business. `app.js` passes shared state. Public clinical content is separate from private uploads and CV contact details.

## Medication Intelligence Engine

Medication name search is public and default-enabled, on Enter or Look up. RxNorm returns available IN/PIN/MIN/SCD/SBD/GPCK/BPCK identities without the previous 80-result truncation. User chooses the exact RxCUI and one openFDA label record. Label set UUID, effective date and exact DailyMed URL are displayed. Sections expose returned label text for indication, mechanism, adult/pediatric dosage, strengths, boxed warning, contraindications, warnings, adverse reactions, interactions, special populations and counseling. Missing text is explicitly unavailable, not a declaration of safety. Adult/pediatric and renal/pregnancy sections require reading the complete selected source.

RxClass enriches classification. MedlinePlus Connect returns patient-information links with attribution. PubMed ESearch returns up to ten public medication search matches; these are unappraised citations, not automatically accepted guideline evidence. DailyMed links open original product labels because direct browser API CORS cannot be assumed. APIs use no credentials, no-referrer, 15-second timeout and a bounded 24-hour in-memory cache. CSP allows only four source origins. Only a drug term/RxCUI is transmitted; cabinet combinations, encounter text and patient factors are never sent. Public clinical queries reject obvious encounter identifiers/text, but the user must enter a medication name only.

Prices, comprehensive interaction severity, synthesized clinical pearls and guideline-specific medication roles are not supplied by this engine. Retail prices are not fabricated. The local cabinet review detects duplicate RxCUIs and selected-label ingredient mentions. A mention can describe no interaction; it never automatically means avoid or change a dose. No flags does not establish safety. RxNav's interaction API was discontinued; a comprehensive institutional checker is still required.

## Calculators and clinical workflow boundaries

- FIB-4: age × AST / (platelets × sqrt(ALT)); adult stable-lab context, AST/ALT U/L and platelets 10^9/L. No universal cutoff or fibrosis diagnosis. AASLD provenance appears in output.
- Steroid: approximate oral anti-inflammatory reference ratios, not mineralocorticoid replacement or taper instructions; Endotext source.
- Benzodiazepine: approximate oral equivalent ratios from SPS; patient response and withdrawal require individualized assessment. The existing taper worksheet remains separate.
- Antipsychotic: Leucht2014 primary minimum-effective-dose ratio, oral adult non-first-episode/nonrefractory schizophrenia only; no LAI, clozapine or automatic cross-taper.
- Insulin: supported LANTUS label starting-dose rules only: once-daily NPH 1:1; twice-daily NPH total 80%; once-daily TOUJEO 80%. Units are not mL; no arbitrary concentration conversion, U-500 or titration.
- PREVENT: official AHA calculator link and externally calculated endpoint/date documentation. Native risk equation is NOT implemented; AHA requires acceptance of its free code license and access to its approved source package. Do not substitute an older ASCVD equation or inferred coefficients.
- Adherence: clinician-recorded patient self-report VAS0–10, with study 9–10 versus 0–8 associations, educational PDC and MPR. Combined output flags concordance/discordance, not a validated joint predictor or calibrated patient probability. Record patient interaction rather than substitute a clinician guess for the validated question.

## Anticoagulation calendar

Inputs include indication, medication/dose, adult age/sex, weight, SCr, verified CrCl, INR, procedure/date, bleeding/thrombotic risk, mechanical valve, stroke/VTE history, kidney stability and plan reference. The rule requires an explicit clinician-reviewed elective interruption decision. It excludes urgent, neuraxial, HIT, unstable kidney function/dialysis, CrCl<30 and unreviewed active-bleeding situations. Very-high/recent-event cases require a specialist exception. It does not select a DOAC dose or automatically bridge warfarin.

Calendar renders dated action rows. For the approved standard warfarin hold pathway, last scheduled dose is D−6 and hold begins D−5. DOAC full-calendar hold intervals reflect selected drug, bleeding risk and verified CrCl. Exact last-dose clock time is NOT computed; the team must confirm prescribed frequency and procedure time. Warfarin bridge exception requires specialist rationale, an explicitly approved enoxaparin reference regimen, INR start threshold, postoperative approval and stop criteria. Future INR and hemostasis remain conditional; no fixed bridge-stop date is predicted. High-risk DOAC restart reference uses a conservative D+3, subject to team approval. Print/Save as PDF and text export retain conditional draft language. Separate final patient instruction approval and clock-time automation remain future work.

## Inhalers, code selectors and measures

Asthma/COPD/device routes open an assessment and teaching workflow. Adult COPD: confirmed diagnosis, CAT, treated exacerbations, eosinophils/current therapy, coexisting asthma, technique and device-fit prompts. GOLD2026 initial grouping uses one moderate/severe exacerbation for E; follow-up is not automatically treated as initial selection. Asthma age12+ uses four-week symptoms, activity and SABA-frequency context; ICS-formoterol reliever is not scored using the SABA-frequency item. No brand/dose prescription is generated. Source links include current GOLD/GINA, Allergy & Asthma Network device videos, CDC and the owner-supplied UseInhalers channel. Previous failure needs distinction from technique, access or adherence.

Offline ICD-10-CM FY2027 bundle contains 74,879 billable descriptions, effective2026-10-01 to2027-09-30. Search is local, returns at most60 matching choices and requires explicit provider-documentation/index/tabular review; it does not infer disease from medication. CPT/HCPCS selector exposes the existing48 reference identifiers; choosing a code does not assign a claim or bypass payer/role/criteria requirements. HEDIS MY2026 and CMS Stars2027 reference-title dropdowns do not include licensed specifications/value sets and do not certify eligibility/closure. Generic dermatology/biologic modules remain review worksheets, with source links labeled as references, not complete treatment algorithms.

## Verification, maintenance and remaining work

106 automated tests pass: existing note/billing/privacy/export cases, route smoke rendering, conversion arithmetic/population guards, FIB-4, calendar dates/exclusions and pulmonary assessments. Minimal DOM harness is not browser visual or live endpoint QA. Live browser testing is still required on GitHub Pages for CORS, selected-product metadata, keyboard behavior and printing.

Weekly source monitoring flags source-byte changes for human review; it does not publish clinical rules automatically. Source retrieval/effective date, formula method and rule-version assumptions must remain visible. Changes require applicable guideline/label review and tests. Outstanding work includes a licensed native PREVENT implementation, validated comprehensive DDI data, verified price benchmarks, exact approved perioperative dose-time and separate final patient/clinician exports, structured cabinet regimen editing, automated reviewed transfer of pulmonary findings, additional drug-label section normalization and completed condition-specific therapeutic algorithms.

## Upload

Unzip the update and upload the contents of `docs/` into repository `docs/`, replacing same-name assets. Keep Pages main:/docs. Upload `documentation/`, `tests/`, `scripts/` and `.github/` to their matching repository directories if maintaining the build and monitoring. The standalone preview is for local review and is not the deployed entrypoint. Preserve unrelated files and private materials outside the public repo.

---

## Previous specification history

# Implementation specification — ClinicalRx 0.4

Prepared October11,2026, America/Chicago. This section supersedes 0.3.1/0.3/0.2 behavior below. Professional identity, LinkedIn-only public contact and free GitHub Pages hosting remain. Repository nrosario07/nrosario07.github.io publishes main:/docs. Source archive contains only public site/code, original summaries and curated metadata; original private uploads remain excluded.

## Product model and release status

ClinicalRx has four pillars: Clinical Care; Drug & Evidence Intelligence; Professional Practice; Education. The tools hub is the professional site's Clinical Tools route. Available functions are distinguished from source-linked clinician worksheets and unreleased prescribing engines. Twenty condition workspaces cover the requested clinical breadth, including HIV/OIs, HCV, hormones, dermatology, biologics and devices. Their source editions/jurisdictions/readiness are explicit; directory inclusion is not complete rule validation.

Working calculation/review modules: adult BMI, Cockcroft–Gault, CKD-EPI2021 eGFR, percent total body-weight loss, CHA2DS2-VASc/HAS-BLED, PHQ9, educational PDC/MPR, owner adherence-scale context, slow-taper arithmetic, quality-gap organizer, structured E/M criteria, medication identity/label retrieval and guided care documentation. Automated DOAC dosing/bridging, insulin conversions/titration, disease treatment selection, dose equivalence/cross-taper, vaccine catch-up, certified HEDIS/Stars closure and calibrated adherence prediction remain unreleased. No placeholder is represented as a completed recommendation engine.

## Compact workflows and screenshot correction

Owner screenshots4–7 revealed radios inheriting the global100% text-input width. CSS now explicitly makes choice-set radio/checkbox width automatic with a16px flex basis and wrapping labels. Essential SOAP fields and six business-plan sections remain visible; metadata, teach-back evidence, economics, coding, contracts, handouts and exports expand on demand. Guidance becomes a compact disclosure. No hidden input is deleted, and route changes preserve draft state in memory. Essential note output includes actual facts, concise code-review status and improvement prompts; detailed evidence stays in its expandable panel. Business drafts omit unused advanced sections and embedded long instructional prose.

## Architecture, routes and data authority

Deferred classic script order: content.js, core.js, rules.js, clinical.js, module-data.js, modules.js, drug-api.js, platform.js, workspaces.js, app.js. Existing profile metadata remains in registry.json; sync-registry.js generates content.js. modules.json is the condition/education/readiness authority; sync-modules.js generates module-data.js. clinical-rules.json/rules.js remain the limited pinned code/fee subset. Pure modules.js contains new formulas and review logic; platform.js contains the four-pillar routes, condition worksheets and public drug view. Existing core.js/clinical.js retain notes/economics/payer gates and structured exports. Schema/reference version is0.4.0; JSON service.levelReference records the conditional E/M review independently of the office pathway and contract terms.

New routes: medicine, adherence, anticoag, library, taper, quality, guidelines, education, care-{known module ID}. clinical-tools opens the four-pillar hub. Unknown route identifiers fall back safely. Route hashes contain no patient facts. Tools remain framework-free and require no account, API key, database, cloud model or paid subscription.

## Public APIs and privacy boundary

Default medication lookup is off. An explicit checkbox enables public medication-name requests to RxNorm and selected-RxCUI requests to openFDA. Encounter/SOAP/MTP, quality, adherence and calculator inputs are never bound to API queries. Public-name validation limits length/characters and rejects obvious encounter terms; users must still enter only a public medication name. Selected identifiers must come from returned RxNorm choices. Fixed HTTPS endpoints, credentials:omit, no-referrer,15second aborts, busy guards and HTTP-error handling are used. Patient data must never be included in the public lookup field.

Host CSP connect-src allows only rxnav.nlm.nih.gov and api.fda.gov; other input workflows remain local. No persistence, analytics, remote script or server-side clinical storage exists. Public response cache is memory-only, expires after24hours and retains original retrieval timestamp. Changing medication identity clears old labels. Async route/request checks prevent an old response from attaching to a different identity/route. Unknown/missing/rate-limited data stay unavailable; there is no proxy/API-key workaround.

Public API probes succeeded with CORS* for RxNorm and openFDA. DailyMed answered without a browser CORS header, so the browser uses original DailyMed SPL links rather than an assumed direct API. Labels are retrieved by selected RxCUI, then the clinician selects an exact returned product; manufacturer, set ID and effective date accompany short excerpts. Retrieval time differs from label effective time. Excerpts are not complete contraindication/dose instructions and never drive therapy. openFDA's unvalidated-data warning is displayed. Original DailyMed, PubMed, MedlinePlus and PurpleBook links support review. These latter links are not claimed as implemented API integrations.

## New clinical calculation contracts

CKD-EPI2021 creatinine:142×min(SCr/k,1)^alpha×max(SCr/k,1)^-1.2×0.9938^age×1.012 if the female equation coefficient is selected. k=.7/.9 and alpha=-.241/-.302 for female/male coefficients. Adults18–120, positive mg/dL, explicit coefficient and stable/IDMS context required. Result mL/min/1.73m2, not CrCl or a diagnosis from one value; AKI/dialysis/unknown contexts excluded.

Percent total body-weight loss:100×(starting−current)/starting, positive weights in one explicit kg/lb unit. Retain negative values for gain; no pharmacotherapy target is inferred.

CHA2DS2-VASc sums original components and mutually exclusive age bands; HAS-BLED counts eight explicitly reviewed non-age factors and age>65. All factors require yes/no, not unchecked-as-no. Adult clinical AF/no mechanical valve or moderate/severe mitral stenosis context required. Source definitions must be reviewed for renal/liver/BP/alcohol/INR factors. No annual risk probability, treatment threshold, DOAC dose or withholding decision is inferred.

PHQ9 scores nine past-two-week symptom items0–3, requires all responses, and produces a screening/severity total0–27. Standard severity bands are descriptive, not diagnostic. Positive item9 flags a clinical safety assessment irrespective of total; zero does not exclude risk. Permission-to-display attribution is retained from the NIH instrument resource. No antidepressant recommendation is generated.

Taper illustration accepts a clinician-selected current dose, reduction>0–10% and interval2–4weeks with planning attestation. It computes four successive current-dose percentage reductions. It does not round to available formulations, convert drugs, reach an automatic zero endpoint, choose the correct pace or prescribe. ASAM2025 source, withdrawal/seizure/monitoring considerations, pause/slow review and no-abrupt-stop context accompany the output. Other individualized schedules remain outside this limited illustration.

## Adherence and quality contracts

Educational PDC uses one unchanged medication, complete nonreversed dated fills, explicit inclusive window, early-refill carry-forward and clipping to the window. Prior fills may carry coverage into the window; overlapping coverage is counted once. Invalid dates/supply, duplicate identical fills, empty history, unknown review or oversized windows stay unavailable. MPR here is specifically uncapped days supply dispensed inside the fixed window divided by window days; end stock can inflate it. No therapeutic-class switching, hospitalization, enrollment/exclusion logic or copyrighted annual value-set specification is implemented. Possession is not ingestion, and neither result is certified Stars/HEDIS closure.

The owner-supplied adherence manuscript and supplement were read locally. Original question11 is displayed with DOI/PMID. Integer0–10 score categories show observed study associations:48/61 at scores9–10 and16/34 at scores≤8 had MPR≥.80. These95-person cohort results are not individualized probabilities or an externally calibrated predictor. No missing regression equation is invented. Barriers, shared action and follow-up remain clinician documentation.

Quality Gap Closer records measure/product/year, exact controlling source/version, eligibility/exclusions, gap, action owner/date, status and closure evidence. Marking an action complete does not close a measure. Only explicit user-entered eligibility/source/closure evidence can be described as user documented, never independently certified. CMS current annual Stars files and NCQA references remain controlling; copyrighted measure definitions are not reproduced.

## E/M and improvement prompts

Original Medicare pharmacist-only office E/M remains the separate99211 incident-to review, not a universal commercial cap. Other service families require their own rules. Conditional established-patient commercial/MA level reference requires written policy accepting the lawful performer and eligible MDM/time, documented recognition, actual SOAP/author/scope/billing-entity evidence and a reviewed patient category. MDM uses the middle of three user-assessed component levels (two-of-three). Eligible-time thresholds are10/20/30/40minutes for the limited99212–99215 reference. Current licensed descriptors and payer criteria remain necessary; no word count, number of medicines or inferred time establishes a level. Output identifies the next level's criteria for review without recommending manufactured work. Clinical edits clear actual E/M evidence. These are conditional references, not approved claims or automatic contract recognition.

Note improvement prompts identify missing reasoning/findings/actions/monitoring/education/follow-up and connect facts→rationale→action. Business prompts identify missing need, payer evidence, outcomes, milestones and budget. These are original teaching prompts, not patient-specific prescribing recommendations. Sources remain adjacent in the UI and output when a code reference is produced.

## Provenance and automated source monitoring

Each clinical formula/output links its controlling reference; care worksheets require source section/date/applicability/reviewer. The guideline registry shows source edition, US/source-specific jurisdiction, readiness, registry-entry check date and review due date. A source lead with unverified edition is never labelled a completed rule. Overdue labels appear after the review date. Complete recommendation provenance should include source locator, edition/effective dates, population, jurisdiction, formula/rule version, reviewer and limitations before a future rule is enabled.

A weekly ChatGPT condition-watch automation was created and timezone-corrected for Monday08:00 America/Chicago, with change-only notifications and primary-source links. It checks CMS/Texas/FDA/API and major guideline sources, distinguishes proposals/final changes, and never auto-publishes clinical decisions. The GitHub workflow source-monitor.yml, once uploaded, runs Monday14:00UTC, retains an availability/hash report and has contents:read permission only. check-sources.py reads public registries/URLs only; no patient/private data or credentials. Initial hashes are byte baselines, not evidence validation; cosmetic content changes require triage. Unavailable, changed or unbaselined sources enter a review queue. Approved rule updates require source review and tests. Thus monitoring is automated, clinical currency is not guaranteed by a timer.

## Verification and deployment

97 automated tests passed, including public API opt-in/query isolation/cache/errors, pure clinical formulas, score exclusions/unknowns, owner-scale boundaries, refill overlap/gaps/windows/duplicates, PHQ9 safety signal, taper and E/M gates, radio-width rule, old/new routes and event-capable form tests. Public endpoint probes confirmed responses/CORS as described. Browser visual/mobile/screen-reader/download/print QA remains pending because the supported browser-preview capability was unavailable. No institutional clinical/payer certification is implied.

Run node --test tests/*.test.js after changes. Run sync-registry.js/sync-modules.js for their corresponding metadata. The pinned-reference maintainer script rebuilds reviewed code/fee sources. package.py generates the0.4 source ZIP, portable preview and current specification copy. GitHub integration uploads previously returned403; manual upload remains the supported handoff in this session. Upload docs/documentation/scripts/tests/README and optional .github workflow at their existing paths. Preserve main:/docs and inspect newer repository changes before replacing files.

See RELEASE_0.4.md for readiness and the fictional-case checklist. The next clinical rules must be delivered in small evidence-reviewed modules with exact labels, contraindications, dosing units/populations/exclusions, meaningful fixtures and source-change handling. The twenty worksheets are an organized starting point for that work, not a substitute for it.

---

Historical specifications follow; their privacy/API and module-status statements are superseded by0.4 above.

# Implementation specification — guided clinical tools 0.3.1

Date: October 11, 2026. Professional owner: Dr. Norbert Rosario, PharmD. Working platform name: ClinicalRx. Repository: https://github.com/nrosario07/nrosario07.github.io. Site: https://nrosario07.github.io/. Deploy `main:/docs` through GitHub Pages. The 0.3.1 payer clarification below supersedes earlier narrow billing descriptions; this current section supersedes the historical 0.2 specification below; master specification 1.3 remains the requirements baseline.

## Delivered scope

The eleven professional routes, curated public CV and LinkedIn-only contact remain. The tools are free, account-free and run locally in the browser. This release adds guided smart-note controls, integrated economic evidence, a teaching-focused practice plan, patient visit-plan drafts, a limited diagnosis-reference matcher, an office service review, and adult BMI/legacy Cockcroft–Gault calculators. Texas readiness and the searchable provenance directory remain available. No original private attachments are published.

| Workspace | Behavior | Explicit boundary |
|---|---|---|
| MTP/SOAP | Section help, original examples, source links, action/status radio controls, stable problem identifiers and outcome evidence | A note does not establish scope, diagnosis, claim eligibility or authentication |
| Patient plan | Generates from agreed SOAP plan, monitoring, follow-up, education and clinician-reviewed condition references | Clinician review required; readability estimate cannot guarantee grades 3–5 or comprehension |
| Diagnosis references | Twelve FY2027 ICD-10-CM references matched locally against reason/assessment; explicit confirmation | Not exhaustive; no drug-to-diagnosis inference, final sequencing or automatic coding of uncertain diagnoses |
| Service review | Structured payer/product inputs and a narrow in-person nonfacility Original Medicare office 99211 incident-to checklist | Original Medicare office limit is separate from commercial policy/contracts; broader families remain reference candidates |
| Fee reference | Sixteen published annual CY2026 Texas rows: eight localities × Medicare QP/non-QP | Not a current claim quote; annual data have not been reconciled to quarterly revisions or claim adjustments |
| Economic evidence | Shared event records inside MTP/business; risk models and direct comparator costs | No universal coefficients, causal realized-savings claim, automatic aggregation or inclusion in revenue |
| Business plan | Thirteen narrative sections with guidance/sources plus monthly collections arithmetic | Not a payer contract, CPA, full cash-flow projection or certification |
| Clinical calculators | Adult BMI and legacy Cockcroft–Gault with units/context checks | No diagnosis, dosing, pediatric, pregnancy BMI or unstable-kidney inference |

## Payer and code-family clarification — 0.3.1

This revision preserves broader possibilities rather than applying an Original Medicare office E/M limit to all payers. The tools now include 48 CPT/HCPCS reference identifiers in fourteen original service-family summaries. Families cover office E/M 99211–99215, MTM 99605–99607, self-management education, DSMT, CGM setup, wellness, CCM/PCM, TCM, BHI/CoCM, RPM including CY2026 updates, facility and vaccine services. Related practitioner-personal references are marked as role-restricted. These are candidate references, not an exhaustive licensed CPT database or a list of codes a pharmacist can independently report. Unknown additional identifiers can be entered for explicit current code/coverage review; they remain unverified.

Commercial products may have explicit policy/contract recognition permitting higher E/M or other services, subject to lawful scope, performer qualifications, service criteria, enrollment and the actual agreement. The tool no longer treats the absence of a Medicare-style rule as a universal prohibition. It still does not infer a level or timed units from SOAP prose, pharmacist minutes or MTP count.

Negotiation must name the payer and benefit. Medicare Advantage network payment terms and PartD sponsor MTM fees are distinct from Original Medicare physician-fee-schedule payment. A private agreement cannot negotiate away Original Medicare statutory provider recognition, coverage or service requirements. An approved CMS model/waiver, if relevant, needs its own verified authority; no model exception is presumed.

PartD MTM services may be paid through the sponsor's program/contract, with MTM CPT identifiers if the sponsor accepts that reporting method. CMS October2026 RVU file R04 (updated 2026-08-26) lists 99605, 99606 and 99607 with PFS status X: no physician-fee-schedule payment for these codes. This is not a statement that Medicare has no MTM benefit. PartB eligible-practitioner/team care-management work and PartD MTM must not be paid twice for the same work.

Texas Medicaid FFS clinical pharmacist E/M recognition must not be assumed. Pharmacy/provider enrollment for covered pharmacy benefits is distinct from independent clinical visit eligibility. Medicaid is state/program-specific; the site does not assert that all Medicaid programs exclude pharmacists or that every Texas payment arrangement must be an APM. For Texas MCOs, verify the specific benefit/contract and eligible billing entity; MTM, negotiated per-visit, PMPM, bundled or value-based arrangements may be strategies if permitted. A contract/APM does not automatically expand legal provider status or scope.

CMS May4,2026 guidance specifically discusses pharmacist participation in deprescribing under existing qualifying care-management families, including CCM/PCM, and related BHI/CoCM/TCM contexts. This is published guidance about existing services, not a newly created pharmacist-specific CPT code. CPT is maintained by AMA; CMS may establish HCPCS LevelII codes and determine Medicare payment. CY2027 PFS proposals are tracked separately, inactive until finalized with applicable effective dates. No unverified future pharmacist code is invented.

The shared contract-review schema adds contractCodes, planName, contractReference, contractBenefit, effective start/end, contractRecognition, contractCriteria, actual serviceElements, contractPayment, contractRate and rateUnit. Billing role can be a payer-recognized pharmacist contract role; this does not establish PartB recognition. All terms are user-entered review evidence, not independently verified approval. Missing recognition/evidence/dates/code validity/rate/unit yields PENDING_REVIEW and no amount. Completed documented terms yield USER_DOCUMENTED_CONTRACT_SCENARIO, never a claim or collection prediction. Original Medicare selection suppresses a private negotiated-rate scenario. PartD MTM does not approve non-MTM codes through that benefit. Practitioner-personal codes are blocked from pharmacist-only contract scenarios. Contract amounts never automatically fill business collected receipts.

MTP and business outputs include the same contract-review appendix. Business has an explicit planned/actual service date shared with encounter date; planning is not a claim. Structured JSON separates contract inputs/review, narrow office incident-to checklist, annual PFS benchmarks and economic evidence. Reference source R04 contains pinned October2026 PFS statuses for all 48 identifiers; status alone is not coverage or performer eligibility. Other benefits (for example vaccines or facility payment) require their own files/rules. The maintainer rebuild script verifies the R04 archive hash and extracts status identifiers only, not copyrighted descriptors.

## Code architecture and reproducible build

No framework, package installation, cloud language model or paid service is needed. Load these deferred classic scripts in order: `content.js`, `core.js`, `rules.js`, `clinical.js`, `workspaces.js`, `app.js`. `app.js` owns the portfolio/router and creates the workflow factory. `workspaces.js` renders guided inputs and binds memory state. Pure calculations and reference checks live in `clinical.js`; `core.js` retains note formatting, process counts and monthly finance arithmetic.

`docs/data/registry.json` is the source-directory/profile authority. Run `node scripts/sync-registry.js` after editing it. `docs/data/clinical-rules.json` is the small executable reference subset. Its JSON copy and `rules.js` must remain identical. `scripts/rebuild-clinical-references.py` downloads fixed public CDC/CMS archives, verifies SHA-256 pins, extracts only the approved diagnosis descriptions and Texas 99211 rows, and fails closed if upstream bytes change. This maintainer operation never runs in a patient workflow. A new source edition requires review, updated rules/tests, version and effective dates; do not update hash pins merely to bypass an error.

Run `node --test tests/*.test.js`. `python scripts/package.py` creates a portable single-file preview and source ZIP. The hosted site preserves a restrictive CSP with `connect-src 'none'`; the portable preview only permits its own inline script/style bundle. All downloaded reference archives are public-source maintenance intermediates and are excluded from site publication.

## State and exports

Memory state keys: `encounter`, `billing`, `mtps`, `events`, `business`, `checks`, `bmi`, `cg`. Route changes retain drafts; refresh clears everything. There is no fetch, account, database, analytics, localStorage, sessionStorage, IndexedDB or service worker. Hash routing contains only route names. External source links are user initiated, no-referrer and noopener. Patient text is never sent to a terminology service, PubMed, Google Scholar or a model.

Encounter schema includes de-identified encounterId, date, setting, reason, actual author/role, authority reference, subjective, objective, assessment, plan, planStatus, monitoring, followup, education, teachback, teachbackEvidence, confirmedCodes and diagnosisReview. The synthetic flag labels learning cases. IDs and source references are documentation inputs, not authentication or primary-source credential verification.

MTP schema includes immutable session-stable id, medication/indication, original rationale label, supporting facts, structured actionType, narrative action, decision, implementation, actual implementation details, resolution and follow-up evidence. IDs increase monotonically across additions/removals; an encounter reference namespaces exported records. Existing 36 original labels remain unpriced, with monetaryCoefficient null. Accepted is not implemented. Implemented counts require actual details; resolved counts require follow-up evidence. Prevented theoretical harm is not an observed outcome.

Structured JSON schema version 0.3.1 separates encounter/MTP inputs, reviewed diagnosis references, service inputs/checklist/benchmark and economic inputs/review. It contains draft clinical data: download only into an institution-approved location. MTP CSV includes schema version, encounter reference, date, MTP ID, rationale, action category, decision, implementation evidence, resolution evidence and nonduplicate related event IDs. Cells are quoted and spreadsheet formula prefixes are escaped. Exports require a nonblank de-identified encounter reference; no patient ID validation is implied. Stable IDs are session-scoped, not a cross-organization master patient index. No generated physician signature, credential approval, performed minutes or outcome is included.

## Guided documentation and patient generation

Each SOAP section explains what to record and why: subjective reports/barriers; objective dates/units/source; assessment status versus goal, cause, alternatives, benefit/risk and medical necessity; plan actual versus pending actions; monitoring thresholds/timing/owner; follow-up access; education and actual teach-back/show-me results. Guidance draws from CMS documentation principles, AHRQ teach-back and Texas scope references. Completing these local quality fields is not a claim that every field is separately required for CMS 99211.

Patient draft headings use simple language. Conditions use plain labels only after diagnosis-reference review. Plan is reused automatically only when the user marks the SOAP plan as agreed patient actions with no pending recommendations. Monitoring, follow-up and education are reused automatically. A small reviewed phrase list simplifies common wording, such as “Monitor your” to “Check your”; medication names, doses, numbers, units, negation and conditions are preserved. No medication instructions or return precautions are invented. Complex prose and abbreviations trigger review warnings. Approximate Flesch–Kincaid grade uses a basic syllable heuristic and is not validated patient comprehension; medical names can increase scores. The target is grades 3–5, not a guarantee or forced rewrite.

User reviews the entire generated draft against SOAP before download. Missing agreed plan/monitoring/follow-up/education blocks patient export. Every form edit clears the patient-review attestation; re-rendering the workspace also clears it. A pending/mixed plan never becomes instructions. The plan remains a draft even after a user review checkbox; final distribution belongs in the approved clinical workflow. Internal assessment rationale, billing and economic records do not flow into the patient document.

## Diagnosis and service reference logic

The diagnosis subset is FY2027, effective 2026-10-01 through 2027-09-30. Invalid/missing/out-of-window dates yield unavailable. Phrase matching uses only reason and assessment; conservative sentence suppression handles negatives, uncertain, family-history, prior-history and resolved terms. This is not a complete language-understanding engine. It never infers disease from medication or laboratory values. A diagnosing-provider record, specificity/complications, current index/tabular instructions and sequencing must be reviewed. Confirmation accepts only present candidates. Conflicting alternatives within one bundled code family produce no confirmed codes. Changing reason, assessment or date clears prior review. Other diagnoses/editions require manual coding review outside the subset.

Original Medicare Part B is distinct from Medicare Advantage, Texas Medicaid FFS/MCO, commercial, Part D MTM, APM arrangements and self-pay. Unknown or non-Medicare products yield product-specific review guidance without automatic codes or Medicare payment assumptions. APM participation needs an executed arrangement; it is not created by credentialing, and private APM terms do not establish Medicare QP status.

The one automated office path requires an in-person pharmacist medication follow-up, nonfacility office, established patient/initial eligible practitioner plan, active involvement, state scope/privileges, medical necessity, billing-practice expense, qualifying supervision, no Part D payment, actual EHR authentication and evidence references. CMS pharmacist auxiliary office E/M clarification limits this pathway to 99211. No number of MTPs, amount of prose, pharmacist minutes or clinical complexity creates higher E/M levels. Eligible billing practitioner work or other services need independently reviewed rules. This is a checklist, not a claims engine.

A supervising MD/DO sign-off with evidence is the user's clinic-specific control. It is not asserted as a universal CMS rule; CMS recognizes certain NPP supervisors. A later signature cannot substitute for applicable supervision. CY2026 qualifying direct supervision can use real-time audio/video for applicable services, subject to exceptions, state rules and clinic requirements; audio-only is not accepted. Clinical changes and changes to payer/service/site/modality/entity/supervision invalidate recorded authentication/sign-off attestations. The tool does not sign an EHR record.

## Fee benchmarks and economic integrity

Annual CMS files updated 2025-12-29 are pinned separately for QP and non-QP. Texas carrier 04412 has localities 09, 11, 15, 18, 20, 28, 31, 99. County mapping must be checked; 99 includes Bexar. The bundle retains facility and nonfacility published amounts for provenance, but this workflow only displays the nonfacility benchmark. A 2026 service date, Original Medicare pathway, locality, actual QP status, participating/assignment status and eligible billing-practitioner role are required. Eligible NPP role-adjusted reference uses 85%; MD/DO uses the published base. This is not payment to the PharmD and is not automatically collected revenue. Quarterly revisions, MIPS/other adjustments, deductible, coinsurance, charges, contractual terms and actual eligibility are not calculated. A blocked service checklist can still show a clearly labeled educational annual benchmark; it is never represented as an approved patient payment.

Economic records require an event ID, population/setting, horizon, perspective, USD price year, primary source/input locator, evidence design/uncertainty and local applicability. Method is risk-difference model or direct cost comparison. Risk net = (baseline absolute risk − after absolute risk) × event cost − incremental cost; direct net = complete comparator cost − complete intervention cost. Blank costs are unknown, not zero; out-of-range/overflow inputs are invalid. Negative differences remain visible. Coefficients are never loaded by MTP category.

Shared event IDs link multiple MTPs to one outcome. Repeated IDs are flagged and excluded from reporting, with no automatic cross-event total because horizons/perspectives/overlap may differ. Links require actual implementation evidence before being described as implemented; an unlinked/business-only record remains proposed. Even implemented-intervention modeled risk differences are not causally observed savings. Do not add drug savings already included in total claims costs. Four historical E03 amounts remain inactive; a literature link alone is not coefficient validation.

Business plan sections cover executive summary, need, service scope, CPA/credentialing/privileges, payer/APM strategy, operations, staffing/capacity, quality/equity, budget/cash flow, economic justification, milestones/governance, risks/audit evidence, and sources. Original guidance links SBA, CMS, Texas and AHRQ materials. Monthly collections = completed visits × collected receipts; expense = completed visits × variable cost + fixed cost; break-even = ceiling(fixed / positive contribution). Zero requires explicit entry. Modeled cost avoidance never enters collections/profit. A full multiscenario cash-flow and contract-specific financial engine remains future work.

## First clinical calculation rules

Adult BMI uses kg / m², with Metric kg/cm or US pounds/inches converted using 2.2046226218487757 lb/kg and 0.0254 m/in. Positive finite measurements and completed adult age 20–120 with nonpregnant/checked context are required. Result is kg/m², a screening measure; no category-derived diagnosis or dosing is emitted. Body composition and fluid context require clinician judgment.

Legacy Cockcroft–Gault uses (140 − age) × selected weight kg / (72 × serum creatinine mg/dL), multiplied by 0.85 for the explicitly selected legacy female coefficient. Accept adult ages 18–139, positive finite kg/creatinine, explicit weight policy and stable kidney function/no AKI or dialysis. Weight selection is clinical, not automatically ideal/adjusted. Low creatinine is not rounded upward. Result mL/min is not indexed eGFR. Legacy assay/population/body-composition limitations and contemporary kidney-function guidance are displayed. Follow drug labeling and clinical review; no medication dose is generated.

## Validation, release and next extensions

68 automated tests cover pure clinical/financial rules, unknown/zero/range states, negation/edition checks, code confirmation, payer/supervision/sign-off gates, official row dimensions, patient draft/dose preservation, review invalidation, shared economics, stable IDs, CSV injection defenses, structured output, formulas/unit conversion, all routes and privacy controls. Event-capable simulated DOM tests exercise form bindings. They do not substitute for real browser, keyboard, screen-reader, mobile, clipboard/download or print review. Browser QA was unavailable under this environment's preview rules; perform the fictional-case checklist in RELEASE_0.3.md before institutional clinical use. No claim of validated clinical deployment is made.

Keep a named clinical/billing maintainer and review sources whenever editions, laws, contracts or service rules change. Disable or leave unknown any unreviewed path. Next extensions require primary-source validation: device-specific inhaler competencies/handouts, diabetes education, broader payer/service rules, reviewed economic study coefficient records, business scenarios/cash-flow, EHR-native governed templates and later ASHP residency workflows. No audit-passing or accreditation guarantee is supplied.

---

The following historical 0.2 text records the earlier foundation; current behavior is specified above.

# Historical foundation specification — 0.2

Date: October 11, 2026. Master specification baseline: 1.3. Source inputs: Dr Rosario Clinical Tools Master Specification; MTP Note Template and Economic Evidence guide; original blank MTP note. This implementation addendum explains how to recreate and extend this first build.

## Purpose and ownership

The professional identity is Dr. Norbert Rosario, PharmD. The professional site owns a distinct tools experience, provisionally named ClinicalRx by Dr. Rosario. Final platform naming remains pending. The profile now uses the supplied September 2026 detailed CV and VA resume. LinkedIn is the only public contact method. All tools are free for healthcare professionals and students. Patient-facing text must be entered and reviewed by a healthcare professional.

Navigation order is About, Experience, Clinical Practice, Research, Publications, Teaching, Presentations, Projects, Clinical Tools, CV, Contact. Professional sections use curated profile metadata from both CVs. Two journal publications have publisher-verified metadata; textbook contributions are labeled as supplied-CV entries. Historical manuscript affiliations are not used to establish current appointments.

## Architecture and deployment

Use semantic HTML, responsive CSS and classic JavaScript with no framework or package dependency. This intentionally smaller foundation differs from the optional React/TypeScript approach in the master specification: it can be opened locally, inspected easily and hosted directly on GitHub Pages. A later framework migration must preserve data contracts, privacy constraints and test cases.

The repository uses GitHub Pages branch publishing from `main:/docs`. Hash routing avoids server rewrites and works at both root and project URLs. Asset and downloadable-template paths are relative. `.nojekyll` disables unintended Jekyll processing. No GitHub Actions workflow or installation is necessary.

The HTML loads content.js, core.js and app.js in that order using deferred scripts. Registry JSON is the editable authority; sync-registry.js generates its offline JavaScript copy. Pure functions in core.js support Node testing independently of the DOM. app.js owns route rendering, state, event handlers and user-initiated exports.

## Functional inventory

| Component | Foundation behavior | Release boundary |
|---|---|---|
| Professional profile | All eleven routes, populated portfolio, LinkedIn contact and curated public CV | Full source CVs stay private; credential status is reported from the supplied CV, not primary-source verification |
| MTP note | Encounter/SOAP sections, repeating problems, decision/implementation/resolution states, internal service review | No treatment inference, coding assignment, claim or authentication |
| Patient summary | Separate reviewed action and follow-up fields, text export | Does not derive instructions from clinician reasoning |
| Economic scenario | Explicit risk difference, event cost and incremental cost | User assumptions; no validated coefficients automatically applied |
| Business outline | Original service/workflow/payer/outcome/milestone outline and monthly scenario | Contract, privilege and reimbursement eligibility are external |
| Texas organizer | Prepared-item checklist with institutional examples and official reference links | Not a payer decision engine or universal credentialing standard |
| Source directory | Local search/category filtering, original summaries, identifiers and direct links | Inclusion is not validation or a license to republish source content |

Future diabetes and inhaler handouts, clinical calculators, payer-specific billing matrices and residency tools are marked planned. No completed module is implied by a roadmap card.

## State and output contracts

All form inputs live in one memory object for the current page session. Route changes preserve the draft; reload clears it. No persistent input storage, server calls, analytics, account or AI service exists. Hashes contain route identifiers only; patient inputs are never encoded in URLs. External public reference links are user-initiated and use no-referrer/noopener behavior.

Encounter fields: date, setting, reason, author, authority, subjective, objective, assessment, plan, monitoring, education, patientActions, patientFollowup. An optional synthetic flag adds an explicit fictional-case label.

MTP fields: id, medication, rationale, facts, action, decision, implementation, resolution, implementedDetails, followup. The 36 original rationale labels retain domain and research lead metadata; they are not reproduced licensed PQA value sets. Labels have no automatic billable-code or monetary mapping.

Decision states: Pending, Accepted, Declined. Implementation states: Not implemented, Implemented. Resolution states: Open, Resolved. An implemented count requires actual-action details. A resolved count requires follow-up evidence. The UI flags unsupported status selections; exported notes still reflect the entered status transparently and require review. Future clinical release should add stronger review gates and provenance timestamps.

Internal service-review fields: actual service, payer product/benefit, performer and billing entity, candidate code/units, referral/consent/supervision/time evidence, reviewer decision/source. This optional section is a review record only. Counting problems does not assign codes or justify a higher E/M level.

Blank fields render as `[not entered]`. No signer, time, result, treatment response, authorization or payer decision is invented. Patient outputs include only patientActions and patientFollowup, never billing text, economic outputs or clinician assessment. Note copy, TXT download and browser print are user initiated. The application does not transmit or sign an EHR note.

## EHR adaptation

The blank note and generated output are generic plain text for eClinicalWorks, Epic, Oracle Health/Cerner, athenahealth and Elation. Institutions adapt headings and repeated sections through approved note editors. No universal SmartPhrase, SmartText, dot phrase, macro, import package or FHIR integration is claimed. Retain native encounter identity, authentication and signatures inside the EHR. Test formatting and clinically required fields with a fictional case before use. The exported draft is not the final legal record until reviewed and entered through the approved workflow.

## Economic and business formulas

Economic fields baseline and after are probabilities from zero to one. Event cost and incremental cost must be nonnegative. All four inputs are required, including explicitly entered known zeros. Missing or nonnumeric inputs produce UNPRICED; invalid ranges produce INVALID. Gross modeled avoided-event cost equals `(baseline − after) × eventCost`. Net modeled difference equals gross minus incremental. Negative outputs remain visible. Units are per modeled individual over the stated horizon; source, perspective, population, event identity and price-year inputs accompany the output. These metadata are descriptive, not automated validation. Event overlap and cohort multiplication are not calculated.

Four historical E03 values appear only in an INACTIVE reference table. Their missing price-year metadata and unresolved transferability prevent automatic activation. Every rationale monetaryCoefficient is null. A future reviewed coefficient requires study design, population, comparator, event definition, effect uncertainty, currency/price year, cost perspective, eligibility, deduplication rules and clinical/research approval. Validated clinical effectiveness does not by itself validate an economic coefficient.

Business monthly revenue equals visits × collected receipts per visit. Expense equals visits × variable cost per visit plus monthly fixed cost. Operating difference equals revenue minus expense. Break-even visits are ceiling(fixed cost / positive per-visit contribution); nonpositive contribution has no finite break-even. Visits must be a nonnegative integer; all financial values must be nonnegative and explicitly entered. These are scenario arithmetic, not reimbursement forecasts. Cost avoidance is excluded from clinic collections.

## Texas / billing boundaries

Clinic credentialing, hospital/clinic privileges, Texas delegated authority and payer contracting are distinct. A CPA does not independently confer provider payment eligibility or authorize a code. Incident-to prerequisites, E/M performer rules, actual services, Medicare/Medicaid/commercial product requirements, plan recognition, billing entities, supervision and contract terms require current source review. This foundation supplies reference links and organization fields rather than asserting an exhaustive reimbursable-code matrix.

Three references and five progress notes reflect the user's clinic example; they are not stated as universal Texas requirements. MDAPP is a credentialing submission workflow, not evidence of approval. License, CE, references, note samples and certificates remain in an approved institutional system; no uploading UI exists here.

A future payer matrix needs effective dates, service definitions, source excerpts with locators, policy versions, code licensing review, supervising clinician requirements, enrollment/contract status, reviewer ownership and a conservative unknown state. APM participation requires an actual contractual model, not a checkbox or credentialing inference.

## Source layer and maintenance

Each reference has an identifier, title, category, URL, status, original summary, metadata-check date, review status, rights statement and bundle version. The layer links official Texas rules and statutes, CMS/TMHP/TDI materials, medication/terminology resources, owner publication metadata and economic research leads. Search operates locally without sending query text outward. Bundled summaries do not replace source inspection.

Before a reviewed clinical release, distinguish link/metadata checks from full evidence validation, add effective-version locators and applicability reviews, implement review-due dates, designate an owner, and retain change history. CMS policies and payer materials need timely rechecking. Broken links, withdrawn guidance or materially revised rules should move affected functions to unavailable/unverified. Do not imply all reference metadata was freshly clinically validated.

## Security, accessibility and quality

Dynamic form values are escaped before HTML interpolation; draft output uses textContent. No eval, remote script, storage API, fetch, XMLHttpRequest or service worker is used. The published entrypoint uses a restrictive CSP including connect-src none, object-src none and form-action none. The downloadable single-file preview permits inline scripts/styles solely to contain the bundle and uses no network-input connection. No secrets or original private uploads belong in the repository.

Use responsive navigation, visible keyboard focus, explicit labels, a skip link, polite status announcements, semantic headings, reduced-motion support and print styling. Current automated checks cannot establish accessibility conformance. Real keyboard, screen-reader, mobile layout, clipboard, TXT export and print QA remain required before release.

## Acceptance checks and extension process

Run the Node tests after every logic or source change. Confirm unknown values remain unknown, confirmed zero works, risks are bounded, negative scenarios are retained, acceptance is not implementation, resolved outcomes require evidence, patient output excludes internal content, all 36 coefficients stay null, historical values stay inactive, local links exist and every requested route renders.

Use real-browser fictional-case tests on desktop and mobile before publishing a clinical release. Test root and project GitHub Pages URLs. Verify relative paths, focus, menu behavior, sources, output transitions, patient-export separation and reload clearing. No browser visual QA was performed in the build environment.

For additions: define the intended audience, collect primary-source evidence, write explicit applicability/unknown rules, specify input/output units, test edge cases, review clinical and payer assumptions, document limits, and then enable the module with a version and review date. Residency development is a later build requiring the applicable current ASHP standards, program-specific context and confidentiality controls; no accreditation guarantee is implied.

## Profile revision 0.2

Profile metadata is now data-driven through registry.json. Personal email addresses and phone numbers are not used. LinkedIn contact URL: https://www.linkedin.com/in/norbertrosario/. The public CV is an original selected summary, not the uploaded full CV or federal-style resume. License/board credential identifiers, supervisors and confidential peer-review details are omitted from public assets. Original attachments remain unchanged.

Where the documents differ, the public summary uses the shared period and a broader title: University Health ambulatory clinical pharmacy service, January 2023–present, with the VA resume indicating a per-diem transition in July 2024; Assistant Professor role, 2020–2021, avoiding the June/July start-date disagreement. Spanish is listed without an inconsistent proficiency rating. Ongoing MBA study is not presented as an earned degree. A November 2026 newsletter entry is not presented as an already published item. The two Rosario N authors in the 13th-edition textbook entry reflect the explicit explanation in the full CV, not a deduplication error.

The user-suggested Optimizing Medications reference is a homepage link only. Its acceptable-use policy restricts copying, derivative tools and deep links. No assessment, framework, artwork, logo or tool is embedded; the original existing note workflow is retained. Source directory metadata does not grant content reuse permission.

GitHub repository selected by the owner: nrosario07/Dr.Rosario_PharmD.github.io. The prepared code targets main; publish through Settings → Pages → Deploy from a branch → main:/docs. The default project URL is https://nrosario07.github.io/Dr.Rosario_PharmD.github.io/. Repository read access is confirmed. A blob upload was rejected with HTTP 403, Resource not accessible by integration; no site files were uploaded. Manual browser upload or repository-content write access is required before Pages activation. A live deployment still requires verification.
