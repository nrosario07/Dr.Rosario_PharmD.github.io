# Calculator-policy update — ClinicalRx0.6.1

The user's link-first policy supersedes native generic-calculator development. Completed: curated exact links; local result documentation and reviewed SOAP transfer; removal of hosted PREVENT and local questionnaire/conversion/calculator interfaces from their public routes.130 automated tests pass. PREVENT native licensing/source acquisition is no longer a task or blocker. HAM-D now links to its external tool. New custom calculator development requires documented lack of a suitable validated online tool.

The historical phase table below describes0.6 capabilities. Native generic-scoring entries are retired in0.6.1, not scheduled for further development. Custom clinical/professional workflow phases remain active. Current priority is post-upload browser verification of the external directory and result→SOAP flow, then medication intelligence and unique calendar/reporting workflows.

# ClinicalRx phase checklist — v0.6.0

Statuses describe delivered capability, not clinical certification. A release is not browser-verified merely because its prior version was tested.

| Phase | Completed | Remaining / blocked | Status |
|---|---|---|---|
| 00 Professional brand and deployment | Eleven profile sections, public CV summary, LinkedIn-only contact, free GitHub Pages structure, versioned assets, four-pillar hub | Review real-world mobile accessibility and visual refinement after each deployment | Foundation complete; live0.5.2 browser-smoke-tested |
| 01 CMM/MTP and practice foundation | Guided SOAP, structured MTPs, coding/payer review, reviewed patient drafts, economic scenarios, credentialing/source tools | Local import/export restore, richer data reporting, reviewed dated payer records, EHR-specific governed mappings | Delivered with limits |
| 02 Medication Intelligence | Default public RxNorm search, selected openFDA/DailyMed labels, RxClass/MedlinePlus/PubMed provenance, local cabinet, explicit SOAP sync | Comprehensive validated DDI source, retail/benchmark price source, pediatric/organ section normalization, literature appraisal | Retrieval and cabinet workflow live-tested; class-display fix pending new browser check |
| 03 Interactive calculators and screening | BMI/CrCl/eGFR, FIB-4, AF scores, PDC/MPR/VAS, conversions; new response-card PHQ-9/GAD-7 and SOAP transfer | HAM-D17 clinician-rating protocol/source verification and additional validated screeners; native PREVENT | v0.6 implementation complete for listed bounded tools;137 tests pass across release |
| 03A Native PREVENT | Complete input/eligibility/model preparation and external endpoint-result recording | Owner accepts free AHA license and obtains approved R/STATA source package; implement exact version and independently verify official fixtures before enabling results | Native equation blocked on source/license package; no native probabilities |
| 04 Clinical pathways | Reviewed elective anticoagulation dated calendar; inhaler symptom/COPD/device review; new adult T2D review prompts | Exact interval-aware bridge orders and final patient/clinician exports; insulin initiation/titration; product-specific comorbidity therapy; HF/CKD/lipid/HTN pathways | Bounded review tools; not complete prescribing algorithms |
| 05 Practice development | Existing business outline/payer/economic review; new staffing/referral capacity and launch planner | Denials/collection-delay/working-capital model; versioned local contract evidence; governed CPA template authoring | Capacity phase implemented; full cash-flow model pending |
| 06 Education | SOAP-derived patient plans, device teaching source links, approximate readability prompts | Reviewed Spanish, device-specific handouts, protected medication/dose editing, memory-palace/quiz studio restoration | Shared patient-plan workflow live-tested; broader education studio incomplete |
| 07 Quality and reporting | Measure-title selectors, educational adherence calculation and reviewed gap-action records | Licensed/authorized measure specifications, calibrated adherence predictor, denominator/exclusion validation, institution-approved reports | Organizer only; no certified HEDIS/Stars result |
| 08 Residency development | Scope retained in specification | ASHP-current program-type standards, evidence matrix, recruitment/interview/orientation/competency/audit workflows | Later phase |
| 09 Continuous audit and monitoring | Source-change queue and separate scheduled checks; this live-site audit; release report | Publish GitHub monitoring workflow through supported upload; dated document-level guideline change comparisons; new0.6 browser acceptance run | Monitoring alerts do not publish clinical rules |

## Current next action

Deploy0.6.0 using the correctly structured packet, then run the post-upload checklist in AUDIT_0.6.0.md. Continue with medication provenance/normalization and approved final calendar exports before expanding dose engines. Native PREVENT remains independently gated; other phases can proceed without it.
