# Nutrition and data integrations — Phase 06N

Decision date: October 24, 2026. Status: limited education pilot; not expert-reviewed or consumer-treatment ready.

## Implemented in 0.20.0

Five categorical questions select nutrient, clinical context, purpose, diet and a limited medication context. Vitamins D, B12 and B6 produce food information, cautions and questions for a clinician/dietitian. Special populations, symptoms, confirmed deficiency and restricted diets prompt individual review. No dosage, equivalence, diagnosis, lab interpretation, product ranking or shopping recommendation. Unknown inputs fail closed. Edits invalidate results. No inputs leave the tab or persist. No change to the original 13 phase-track denominator.

## Before personalized supplement routines

- Owner pharmacist and dietitian reviewers: names, relevant credentials, review date, scope, conflicts and approval record. Do not describe the pilot as expert-reviewed before this exists.
- Define adult scope, nutrient-specific eligibility/exclusions, laboratory units and thresholds, differential diagnoses, dosing limits, duration, retesting, medication interactions and red flags using primary guidelines.
- Define duplicate-ingredient totals and exact supplement formulation; distinguish intake recommendations from deficiency treatment.
- Validate clinical fixtures independently; test accessible mobile flow, patient understanding and completion time before claiming “under 2 minutes.”
- Public health-profile collection is a separate privacy decision. Current pilot retains fictional/de-identified use, no identifiers or free-text intake.
- Add affiliate product links only after valid owner-supplied Associate links, current program compliance and independent product-selection review. No health answers in URLs or analytics. Existing disclosure uses the user's stated Associate relationship; no account/enrollment verification performed.

## Candidate integrations

| Source | Role | State and constraints |
| --- | --- | --- |
| NIH Office of Dietary Supplements | Nutrient evidence and consumer education | Source-linked summaries in pilot; not a live API or prescribing engine |
| USDA FoodData Central | Food nutrient composition | Candidate, not integrated. Official API requires a key that must not be exposed publicly. Prefer reviewed public-data snapshots for static Pages; otherwise a separately designed server-side service |
| OpenMed | Biomedical entity extraction / local NLP experiments | Research candidate only. Documentation describes an Apache-2.0 SDK and platform-specific browser/REST paths; model licenses and availability need separate verification. Not a free hosted clinical knowledge API, medical truth source or guarantee of de-identification |
| RxNorm / DailyMed / openFDA | Public drug identity and label context | Existing lookups; not sufficient for complete supplement-drug interaction checking |
| PubMed / PMC | Source discovery and accessible literature | Evidence discovery, not automatically accepted recommendations |

OpenMed's docs describe 3.1.0 as a candidate; do not treat it as a verified published package. Before adoption: pin an available version/model, check all licenses, benchmark negation/temporality/errors on synthetic fixtures, test browser memory/download burden and network isolation. No health text is sent to OpenMed in this release.

## References

1. National Institutes of Health, Office of Dietary Supplements. Vitamin D: fact sheet for health professionals. Accessed October 24, 2026. https://ods.od.nih.gov/factsheets/VitaminD-HealthProfessional/
2. National Institutes of Health, Office of Dietary Supplements. Vitamin B12: fact sheet for health professionals. Accessed October 24, 2026. https://ods.od.nih.gov/factsheets/VitaminB12-HealthProfessional/
3. National Institutes of Health, Office of Dietary Supplements. Vitamin B6: fact sheet for health professionals. Accessed October 24, 2026. https://ods.od.nih.gov/factsheets/VitaminB6-HealthProfessional/
4. US Department of Agriculture. FoodData Central API guide. Accessed October 24, 2026. https://fdc.nal.usda.gov/api-guide/
5. OpenMed. Documentation. Accessed October 24, 2026. https://openmed.life/docs/
6. Amazon. Associates Program operating agreement. Accessed October 24, 2026. https://affiliate-program.amazon.com/help/operating/agreement
7. Federal Trade Commission. Disclosures 101 for social media influencers. Accessed October 24, 2026. https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers

Privacy and terms are original implementation-specific notices, not copied from another website and not legal certification. Owner/legal review remains a release gate for future affiliate commerce or broader consumer intake.
