# ClinicalRx0.11.0 — CPA encounter and bounded workflow upgrade

Released for upload October14,2026. Not published by this work session. Full platform incomplete.

## Delivered
- CPA-specific referral reason and referring physician; physician-established multi-diagnosis search before Subjective; ROS/PE between Subjective and Objective; vitals/labs/imaging/procedures/screenings; actual qualifying time.
- Selected diagnoses remain when the assessment changes and appear in assessment/plan headings. This is management of user-entered physician-established diagnoses, not independent diagnosing or code inference from medicine/lab values.
- Local explicit-phrase MTP suggestions with supporting excerpts; clinician confirmation required. Manual additions remain. Encounter edits invalidate confirmed findings and related subtotal until re-review. Suggestions can be missed or wrong; this is not a validated NLP/clinical inference engine.
- Sixteen intervention categories with automatically attached historical numeric study values, methods/context and AMA references. Range shown for analogous studies; incompatible populations/methods/price years are not pooled into an average. Unmatched category has no value, not zero. Repeated event/type entries excluded from an explicitly hypothetical benchmark subtotal. Same subtotal available in business plan without copying patient text. No claim of realized savings, budget impact or billable receipts.
- Quality leads displayed as bullets with names/abbreviations/goals, including CBP, GSD, KED, EED and selected PQA adherence context. No certified denominator, exclusion or gap-closure calculation.
- Automatic documentation-time code comparison; independent payer/setting review. Incident-to fields conditional; actual counseling/supervision statement only when supported by entered minutes and availability. FQHC added. No fabricated >50% counseling statement or MD/DO authentication.
- Texas locality names;144 annual2026 code/locality/QP rows for nine office codes. Published participating base schedule comparison; direct payer recognition/contract rates are not inferred. PartD/FQHC/facility/telehealth/year gaps return no office benchmark. QP/non-QP explained. Contracting steps informational in encounter.
- Original CPA/CDTM draft builder with25 grouped scopes from supplied2023 protocol and current-source links. No personal credentials/signatures republished or delegated authority automatically granted.
- Oral switch and anticoagulation Submit controls; edits clear prior output. Bounded LAI label-initiation pilot: oral aripiprazole→ARISTADA with21-day oral overlap; oral risperidone/paliperidone→SUSTENNA with renal branch. Exact-source AMA references and calendar fixtures. Unsupported pairs/contexts return no schedule. No universal mg equivalence.
- Anticoagulation adds guideline rationale, standard AF/DOAC no-bridge reference logic and monitoring prompts; specialist bridge exception remains an approved-plan workflow. Procedure-specific interruption still requires review.
- Adherence measure definitions in dropdown, VAS value follows slider position, plain clinical interpretation for either source. No redundant claims-review selector; worksheet visibly restricted to complete paid/nonreversed fills for one unchanged medication. Dispensing does not prove ingestion; VAS<9 is an investigation flag.
- Sidebar “Pharmacist Practitioner”; PharmD, BCPS, BCACP unified in hero; clinical practice describes delegated scope instead of interests. Child-Pugh/MELD external directory entries added.
- Public drug API errors identify source host/timeouts and offer original-source links. Live lookup failure not reproduced; no claim that its underlying cause was fixed. Container/wrapping CSS addresses the visible overflow risk; new layout remains browser-unverified.

## Tests and limits
193/193 Node tests pass (pure calculations, boundary/negative fixtures and DOM event harness). Deterministic public-file manifest/package validation required. New0.11 browser appearance/interactions, mobile, print/PDF layout and all external failure modes are unverified until upload.

Browser-tested deployed0.10 only: public apixaban search returned16 identities; RxCUI1364435 labels returned6 records; exact ELIQUIS/Cardinal label effective2026-04-24 displayed coverage13 returned/2 broad/1 missing. Current Pages run38633744728 succeeded at119e039c71105e765f86378fbedd6656ce5866d3. No GitHub workflows uploaded in current103-entry tree; obsolete local-draft files remain unloaded.

## Incomplete
- Reliable free-text MDM classification or autonomous highest-code selection; this release automatically compares qualifying time only, not historical history/exam counts. Other service families remain source-linked inventory, not auto-assigned claims.
- All36 MTP types with validated outpatient-specific per-type economics. The16 intervention mappings are analogous study benchmarks; no universal coefficient for every MTP. Broad causal economic validation remains needed.
- Unrestricted procedure→interruption/bridge indication, high-risk exception selection, exact clock-time/dose rounding and complete calendar/print validation.
- Stimulants, antihypertensives, IR/ER, more oral pairs, LAI missed-dose/depot-to-depot switches. These remain planned and must not return invented schedules.
- Full ADA diabetes app, comprehensive interaction engine, prices, bilingual handouts and later residency platform.
