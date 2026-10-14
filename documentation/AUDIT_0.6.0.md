# ClinicalRx audit and corrections — v0.6.0

Audit date: October 12, 2026 (America/Chicago). Browser timestamps cross into October13 UTC. Live site: https://nrosario07.github.io/. Repository: https://github.com/nrosario07/nrosario07.github.io. Inspected main commit: ab9685ded0b92b8d4aada20947f7d8c6e00d58c1.

## Deployment and verification boundaries

The live index identifies v0.5.2. All16 referenced scripts/styles/icon fetched over HTTP matched the local v0.5.2 package before edits. The repository tree contains46 files and only README.md and START_HERE.txt as root files; the previously flattened root duplicates are gone. Required clinical assets are under docs/assets. Hidden .github source-monitor workflow and docs/.nojekyll are absent from the inspected remote tree; they are included in the full release package. The separate scheduled source-monitor task remains independent of GitHub Actions.

The cloud browser became available during this run. It was used for actual live-site interaction, including RxNorm/openFDA/MedlinePlus/RxClass/PubMed retrieval and fictional local encounter data. A browser attempt to open the new local HTML preview was rejected because file URLs are disallowed. No workaround or alternative hosting was used. Therefore browser findings below apply to DEPLOYED v0.5.2; new v0.6 corrections were verified through code inspection and automated tests, not a post-upload browser run.

## Browser-tested coverage

- All11 professional navigation pages rendered: About, Experience, Clinical Practice, Research, Publications, Teaching, Presentations, Projects, Clinical Tools, CV, Contact.
- All33 distinct tool/module links from the four-pillar hub rendered nonempty content. An additional six standalone calculator/taper routes were checked, for39 distinct tool routes total. This is a route smoke test, not full clinical validation of every algorithm.
- Public apixaban lookup returned16 RxNorm identities. Selected RxCUI1364435 produced six selectable openFDA label records. Selected the displayed Cardinal Health ELIQUIS record effective20260424, label set a454cd24-0c6d-46e8-b1e4-197388606175.
- Label sections and exact DailyMed link rendered. MedlinePlus returned Apixaban and Blood Thinners links; RxClass and PubMed links appeared. This verifies retrieval and rendering, not completeness/currentness of every record or the relevance of every citation.
- Added the selected product to the local cabinet, entered a fictional regimen, selected Patient reports taking, and explicitly transferred the cabinet to SOAP. Objective output retained RxCUI, regimen and reported-use status.
- Entered fictional assessment, agreed plan, monitoring, follow-up and education. Education Studio generated the same patient actions; output readability estimate was4.4. No billing/economic text was included in the patient plan. This is not a validated comprehension study.
- Browser-inspected the linked Andrew Tran diabetes tool's parameter, medication, insulin and SMBG organization. The business PDF and bridge workbook were independently downloaded and read.
- Browser screenshot of the completed fictional patient-plan workflow is provided separately. It shows live v0.5.2, not an unverified new-release screen.

## Findings and disposition

| Finding | Evidence | v0.6 action | Verification |
|---|---|---|---|
| SOAP initially collapsed despite the intended essential-section exception | Live accessibility tree; DOM serialization converts ampersand to &amp; and breaks the string comparison | Normalize ampersand before essential-section matching | Regression test models browser heading serialization; new browser run pending |
| Calculator values shared across unrelated tools | Source audit showed one state.clinical object for age/context and other inputs | Scope advanced inputs by tool route | Event test verifies FIB-4 age50 does not become anticoagulation age; both retain separate values |
| RxClass displays disease concepts as drug classes | Live apixaban list included hemorrhage, stroke and drug hypersensitivity among classes | Exclude DISEASE/CHEM/STRUCT categories; display classification type and vocabulary source; deduplicate identical labels | Source/API category inspection; new browser run pending |
| Module readiness claims stale after earlier upgrades | Live hub still says equivalence/device engines not released | Refresh status labels to distinguish working bounded references from unimplemented prescribing engines | Synced JSON/JS module registry; route tests |
| Raw JSON and generic input forms obscure calculator meaning | Browser/source audit | Human-readable advanced outputs, screening response cards and PREVENT endpoint cards | Code and route tests; visual review of new package pending |
| PHQ-9 safety item can be hidden by incomplete legacy scoring | Legacy function returns early for incomplete total | Dedicated PHQ-9/GAD-7 routes; positive item9 safety prompt appears even with remaining questions unanswered; legacy PHQ dropdown removed from calculator selector | Boundary and event tests |
| VAS neutral slider position can look like a recorded response | Browser-native range behavior and source audit | Explicit Record displayed VAS score action; initial position remains unrecorded | Source/route checks; new browser interaction pending |
| PREVENT is only a sparse result recorder | Live/source audit | Full eligibility/input/model form, official external links and separate10-/30-year CVD/ASCVD/HF result cards | Input validation tests; no native estimates implemented |
| Diabetes module remains a static worksheet | Live route smoke test | Stable adult T2D interactive review prompts with A1c/date, goals, kidney context, comorbidities, duplication, hypoglycemia and affordability | Boundary and provenance tests |
| Business workflow lacks a capacity/referral build | Current tool and2021 example review | Standalone launch/capacity planner with explicit business-outline transfer | Demand/time/completion arithmetic and transfer tests |
| Bridge workbook contains historical assumptions unsuitable for automatic reuse | Workbook text explicitly rounds SCr<1 to1 and uses a14-day print plan | Keep ClinicalRx's explicit CrCl method and no automatic SCr rounding; retain clinician-approved elective calendar and add manual approved clock-time recording | Existing renal/calendaring tests and timestamp validation tests |
| New-release browser preview blocked | Browser explicitly rejects file protocol | Do not claim new-release visual QA; package for GitHub upload and subsequent browser verification | Open item |

## Scope of the next phase delivered

This release completes a bounded calculator/workflow phase: full response-card PHQ-9/GAD-7, PREVENT input preparation and documented external results, original ADA2026 T2D review prompts, practice launch/capacity, tool-state isolation and clinician-reviewed screening/diabetes findings transfer to SOAP. It does not complete native PREVENT, comprehensive medication interactions, patient prices, autonomous insulin initiation/titration, complete cardiology algorithms, HAM-D, final anticoagulation prescribing orders or ASHP residency tooling.

## Primary clinical sources

- PREVENT UI/eligibility: https://professional.heart.org/en/guidelines-and-statements/prevent-calculator
- PREVENT access/licensing: https://professional.heart.org/en/guidelines-and-statements/about-prevent-calculator and https://ahahealthtech.org/prevent-risk-calculator/
- PHQ/GAD original developer instructions: https://www.uab.edu/medicine/pcp-sci/images/SCIMS/PHQ-9_Instruction_Manual.pdf
- ADA2026 section9: https://diabetesjournals.org/care/article/49/Supplement_1/S183/163934/9-Pharmacologic-Approaches-to-Glycemic-Treatment
- NLM terminology: https://rxnav.nlm.nih.gov/REST/rxclass/class/byRxcui.json?rxcui=1364435 (public example reviewed)
- Kidney-method context: https://www.niddk.nih.gov/research-funding/research-programs/kidney-clinical-research-epidemiology/laboratory/ckd-drug-dosing-providers

## Design and planning references — not controlling clinical/payer authority

- https://www.mdcalc.com/calc/10491/predicting-risk-cardiovascular-disease-events-prevent

No reference site's code, images, branding, PDF pages or workbook is redistributed with the site. Concepts inform original interfaces. Primary guidelines/labels govern clinical logic. Historical planning examples are not current payer policy or evidence of guaranteed revenue.

## Post-upload browser acceptance checklist

1. Footer0.6.0; no startup notice remains; four pillars present; About/Contact LinkedIn-only.
2. SOAP essential fields visible on first entry. Compare FIB-4 and anticoagulation inputs to confirm separation.
3. Repeat medication search → selected current exact label → cabinet editing → explicit SOAP sync. Verify typed regimen and source; check no disease terms appear as drug-class names.
4. PHQ-9: select item9 positive before remaining items; safety prompt appears without total. Complete questions; confirm totals and review-required SOAP transfer. GAD-7: verify0,5,10,15,21 boundary examples.
5. PREVENT: no risk percentage appears automatically. Known CVD/unknown facts/out-of-range inputs remain flagged. Document external result only with eligibility/model/date/source/review;30-year results suppressed above59.
6. Diabetes: reject incomplete/acute/pregnant/non-T2 cases; verify boundary A1c>10 and glucose>=300; prompts transfer only after review, without becoming patient medication instructions.
7. Practice capacity: time slots bounded by referrals, completed visits adjust for completion, transfer leaves collections unset unless user supplied them.
8. Print calendar and patient plan; mobile/narrow-screen and keyboard checks. These checks remain outstanding for the NEW release.
