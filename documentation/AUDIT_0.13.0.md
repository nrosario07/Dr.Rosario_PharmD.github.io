# Focused deployed audit and release verification

Review date: October 15, 2026 (America/Chicago).

## Deployment

GitHub Pages run 38827021626 completed successfully at 2026-10-16T00:02:16Z. Main commit: 92114d204634f33216dec1d673d4b1872a007c80. Browser footer: v0.12.1. No broad byte-parity claim or all-page visual acceptance is made. No remote changes were performed.

## Actual browser observations

- ClinicalRx Taper & Switch: entered fictional age55, hypertension, metoprolol tartrate IR50mg twice daily for12weeks, desired succinate ER, transition date2026-10-20 and explicit supported clinical facts. Generate returned LABEL_CONVERSION_SUGGESTED, target100mg once daily, dated replacement instructions, monitoring and a DailyMed source. Therefore the pure-rule example does work in deployed v0.12.1, but the UI provides weak feedback when inputs are incomplete and the result can be visually obscured. The prior v0.12.1 patch only repaired medication lookup; switch UX changes begin in this release.
- Anticoagulation: the dropdown contained nine bundled choices. Selecting major hip/knee replacement changed its displayed starting bleeding category to High. The reported empty list was not reproduced; do not claim its cause is fixed. No complete anticoagulation recommendation was retested this run.
- CMM/MTP documentation section explicitly said free-text MDM was not automatically validated. That requirement was incomplete in the deployed version.
- OpenRxData clinical reference was inspected directly after search retrieval succeeded. Useful patterns: visible search, common-drug entry points, organized label topics and clear provenance. This is a design comparator, not ClinicalRx's clinical evidence source.
- Medication live lookup was not repeated this run, since the user reports recovery and recent prior audit covered it. Full medication→cabinet→SOAP→patient plan was not retested this run.

## New local implementation / automated verification

254 tests pass, including local phrase-based MDM inference, two-of-three logic, negation/history/conditional refusal, Rx decision dose/rationale limits, unique-test counting, panel overlap, decimal doses, new/established mapping, payer separation, missing-input feedback, filtered switch targets and fictional example generation. Existing privacy/API/reporting regression tests also pass. DOM-harness tests are not a real browser and do not prove layout or print behavior.

JavaScript syntax and release integrity checks are run during packaging. New assets share v0.13.0; no new external script or clinical-text network endpoint is introduced.

## Still unverified / limits

New v0.13 deployed browser behavior, narrow-screen/keyboard/print layout, local MDM inference against an independent coding reviewer, complete clinical switch coverage and the user's intermittent empty-procedure condition. New local preview browser QA was unavailable under the supported environment workflow; no alternative preview browser/server was improvised.

MDM inference is an educational, unreviewed candidate, not an audited coding determination. The bounded vocabulary cannot understand arbitrary narrative, determine all unique tests, evaluate medical necessity, validate every active prescription decision or establish pharmacist payer recognition. No automatic high/straightforward level or fee increase. Do not add fictional work to obtain a higher candidate.

## Primary-source review

1. Centers for Medicare & Medicaid Services. Evaluation & Management Services. Accessed October15,2026. https://www.cms.gov/training-education/medicare-learning-networkr-mln/compliance/medicare-provider-compliance-tips/evaluation-management-services
2. First Coast Service Options. Medical decision making and the impact of prescription drug management. September23,2026. Accessed October15,2026. https://medicare.fcso.com/evaluation-and-management/medical-decision-making-and-impact-prescription-drug-management
3. American Medical Association. CPT E/M office revisions: medical decision making grid. Effective January1,2021. Accessed October15,2026. https://www.ama-assn.org/system/files/2019-06/cpt-revised-mdm-grid.pdf (public framework reference; verify current-year descriptor/requirements).

## Post-upload acceptance

Confirm v0.13.0. Load the fictional metoprolol example and submit; verify100mg once daily appears prominently. Remove a required fact and confirm the tool names it. Change the source and verify only reviewed target options appear. In SOAP, use fictional assessment “Hypertension stable. Diabetes at individualized goal.” and plan “Continue lisinopril10mg daily because blood pressure is at goal.” Set established patient status and verify provisional moderate/99214 with quoted evidence. Then remove one stable condition and verify Low/99213. Remove medication dose/rationale or leave only a diagnosis list and verify no unsupported level. Confirm payer reference remains separate. Finally test public drug shortcuts, topic buttons, cabinet sync and reviewed patient plan. Use no PHI.
