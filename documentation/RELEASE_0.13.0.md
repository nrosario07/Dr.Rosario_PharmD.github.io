# Release 0.13.0

## New capability: MDM evidence assistant

SOAP assessment/plan and explicit test-review/order phrases are scanned locally. The service-code section shows separate Problems, Data and Risk candidates with exact supporting passages, missing evidence, a provisional MDM level/code when two components support it, and AMA-format primary references. This pilot recognizes a bounded disease/medication/test vocabulary; unrecognized text is not proof of absent work. High/straightforward MDM, independent interpretation, historian credit and a complete audit are not inferred. Diagnosis lists, raw laboratory values, medication lists, hypothetical/negated statements and prescription management alone do not create an overall moderate level. Potential duplicate tests are deduplicated; overlapping BMP/CMP panels are withheld for review.

MDM suggestions are unreviewed documentation candidates, kept separate from time, payer recognition and fee calculations. No new billing eligibility, claim, automatic payment or licensed full CPT encoder is introduced. Current source references are linked; older public AMA grid is explicitly identified as framework context with current-year verification still required.

## Workflow usability

Switch targets follow the current supported source product; irrelevant hepatic fields are hidden outside SSRI paths. Missing required facts are listed before a schedule is attempted. A clearly fictional metoprolol example makes the supported pathway reproducible. Generated target dose appears prominently; submission moves focus to the result. Existing dose rules are unchanged. The tool is not all-inclusive; more drugs are a reviewed-rule expansion, not just a larger dropdown.

## Medication reference design

Added original ClinicalRx search steps, source badges, public-drug shortcut buttons, label topic navigation and more readable selected-label sections. Raw cabinet JSON is tucked behind technical details. Working RxNorm/RxTerms/FDA recovery, source warnings and privacy boundaries remain. OpenRxData was inspected as a design reference only; no code/data was copied and no new pricing, interaction or monograph completeness claims were added.

## Verification

254 automated tests passed. Deployed v0.12.1 metoprolol conversion and procedure dropdown were browser-tested; new v0.13 visual/mobile/print/browser acceptance remains pending. No remote write or deployment performed. Full platform incomplete.
