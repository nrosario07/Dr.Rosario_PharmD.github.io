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

