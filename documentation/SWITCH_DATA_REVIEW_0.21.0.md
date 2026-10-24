# Switch data review — 0.21.0

## Changes

One canonical, immutable direction catalog now supplies the source choices, target choices and displayed exact coverage list. It contains 22 directions. Target choices are empty until a source is selected, eliminating unrelated initial choices. Changing source clears product-specific safety review. Existing algorithms are retained; this is not a claim that all existing pairs were clinically re-reviewed this release.

Two new one-way product-specific branches:

| Source | Target | Bounded scope | Evidence |
| --- | --- | --- | --- |
| Carvedilol IR tablets | COREG CR capsules | Stable adult hypertension, exact BID table; no interpolation/reverse rule. Older high-dose or increased hypotension risk returns individual-review guidance | Label section 2/Table 1; product availability must be checked |
| Glipizide IR tablets | GLUCOTROL XL tablets | Adult 18–64 T2DM pilot, once/twice-daily IR, exactly achievable daily XL dose ≤20 mg. No rounding or high-risk conversion | Label section 2.1; age restriction is conservative app scope, not a universal contraindication |

Both require exact obtainable product, organ-function/safety review and existing common clinical-context checks. Results contain dose, frequency, dated transition action, monitoring and AMA citation. No automatic prescription or bidirectional cross-drug equivalence. Age and risk cannot be dismissed where they change safe conversion.

## Provenance

1. Woodward Pharma Services LLC. COREG CR (carvedilol phosphate) extended-release capsules. Prescribing information. Section 2, Table 1; sections 4–5. DailyMed version 2; effective September 12, 2025. Accessed October 24, 2026. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=9008ede8-3e53-4061-ae4c-c51cbbb56ef2
2. Pfizer. GLUCOTROL XL (glipizide) extended-release tablets. Prescribing information. Revised August 2023. Sections 2.1, 3, 5.1. Accessed October 24, 2026. https://labeling.pfizer.com/showlabeling.aspx?id=585
3. Food and Drug Administration. Determination that COREG CR extended-release capsules were not withdrawn from sale for reasons of safety or effectiveness. Federal Register. May 30, 2025;90:23056. https://www.federalregister.gov/documents/2025/05/30/2025-09772/determination-that-coreg-cr-carvedilol-phosphate-extended-release-capsules-10-milligrams-20

Important source distinction: COREG CR label package records include a March 31, 2025 marketing end date. This is disclosed; the label conversion is not represented as proof of current brand supply. The FDA withdrawal finding does not guarantee product availability. Generic substitutions require the actual target label and equivalence verification; they are not silently added.

## Remaining quality work

A canonical direction catalog is only the first normalization step. Existing algorithms still contain distinct source structures; a complete typed rule schema with source hashes, ingredient identifiers, indication sets and reviewer approvals remains open. More medications require independent verification; unsupported pairs must stay unsupported rather than inherit another formulation's dose relationship. Browser acceptance and independent pharmacist review of the new branches remain pending.
