# October14 audit request matrix

| Request |0.11 result|Limit / next step|
|---|---|---|
|Referral reason/physician; diagnosis before Subjective; ROS/PE; structured objective|Implemented|No PHI; actual work only; physician-established diagnosis input|
|Automatic MTP detection plus manual additions|Local explicit-phrase suggestions + confirmation; manual blank draft; source-edit reconfirmation|Not validated clinical NLP or comprehensive medication/lab inference|
|Economic estimates automated within MTP and total|16 intervention-type numeric historical benchmarks; AMA sources; illustrative subtotal with exclusions|Not every36 MTP rationale priced; inpatient/ICU context; no universal outpatient coefficient; no realized savings|
|Multiple studies range/average|Range available where matching intervention category has multiple analogous sources|No pooled mean for incompatible methods/price years/populations; original values/method visible|
|Remove intervention decision/implementation radios|Removed from CPA MTP form|Actual intervention and follow-up documentation still necessary; confirmation does not imply resolved outcome|
|Diagnosis search multi-select and no redundant review question|Implemented; diagnosis source identified as user-entered physician record|No diagnosis inferred from drug/lab; code specificity still clinician/coder responsibility|
|Quality goals/names/acronyms as bullets|CBP/GSD/KED/EED and selected PQA context|Limited reference leads, not certified eligibility, denominator or gap closure|
|Automatic E/M/service suggestion from actual encounter|Automatic qualifying-time code comparison + separate payer reference|Free-text MDM and other service-family autoassignment incomplete; cannot use historical history/exam counts|
|FQHC/locality labels; QP/assignment explanation|Implemented; nine-code annual schedule comparison|FQHC/facility/telehealth/year gaps return no office benchmark; contract collections not inferred|
|Remove repeated legal/prerequisite checkboxes|Removed from encounter UI; information retained in disclosure|Tool does not assume CPA/NPI automatically proves payer/incident-to eligibility|
|Supervision and >50% statement|Conditional on actual numeric time/education and incident-to supervisor/availability inputs|Audio-only not qualifying virtual direct supervision; no fabricated statement, signature or another practitioner's note|
|PartD vs PartB determination|Selected actual benefit controls PartD boundary/no office code|Payer name or drug coverage alone cannot prove which benefit funded the service; cannot infer prior duplicate payment|
|Payer/APM review informational|Encounter contracting steps provided|Business scenario inputs remain optional for planning, not payer approval|
|LAIs and oral antipsychotics + Submit and AMA|Oral pilot preserved; new two-product LAI initiation pilot; Submit invalidation/citations|Other LAIs/depot-to-depot/missed-dose, stimulants/BP/IR-ER pending validation|
|Anticoagulation Submit/rationale/calendar|Implemented for reviewed bounded pathway with standard AF/DOAC no-bridge rationale|No unrestricted procedure-name decision; bridge exceptions remain approved specialist plans; broader exports/monitoring validation pending|
|Adherence definitions, slider value, recommendation with either input|Implemented|Single unchanged medicine; claims coverage does not prove ingestion; no calibrated individual probability or certified measure|
|CPA builder/template and directory expansion|Original draft builder,25 opt-in grouped scopes; Child-Pugh/MELD external links|Not executed/legal approval; supplied2023 source not proof of current privilege; more directory work remains|
|Pharmacist Practitioner, credential size, clinical-practice scope|Implemented in source|New visual/mobile acceptance pending|
|Medication fetch failure|RxNorm and openFDA succeeded in live browser; host diagnostics/fallbacks added|Failure not reproduced, underlying cause unresolved; new error handling automated-tested|
|Historical coefficients inactive wording|Removed from public economics route; category evidence table replaces it|Legacy unused function remains in source history; public route uses new evidence view|
