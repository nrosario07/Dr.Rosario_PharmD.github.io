# ClinicalRx0.6.0 — audited workflow and calculator phase

Browser-audited live0.5.2 and corrected verified workflow/state/provenance problems. New0.6 features: response-card PHQ-9/GAD-7 with reviewed SOAP transfer, complete PREVENT input/result-recording interface, bounded adult T2D review, practice launch/capacity planner, manual approved procedure clock-time recording, module filtering/readiness and professional-page tool links.

Corrections: essential SOAP section no longer accidentally folds after DOM serialization; unrelated calculators no longer reuse age/context; RxClass disease/chemical/structure concepts no longer appear as drug-class names; VAS initial slider position is not silently recorded; raw advanced JSON output becomes readable text; calendar moved outside hidden print-input container; patient-plan display uses readable prose typography. Existing free/local/LinkedIn-only boundaries retained.

137 automated tests pass. Browser-tested coverage applies to deployed0.5.2, including the full fictional medication→SOAP→patient-plan workflow and11 professional/39 tool-route smoke checks. New0.6 local preview browser QA was blocked by file-URL policy; run the post-upload acceptance checklist. No claim of complete mobile/print/API validation of the new release.

PREVENT remains without a native equation until AHA's free licensed source package is obtained and validated. HAM-D, comprehensive DDI/prices, autonomous dose algorithms, final anticoagulation orders and ASHP residency tools remain incomplete. See PHASE_CHECKLIST.md for specific status and blockers.
