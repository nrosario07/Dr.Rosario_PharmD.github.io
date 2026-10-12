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

