# ClinicalRx0.6.1 — use existing calculators

Removed hosted PREVENT forms and input-preparation logic. Replaced public generic scoring, screening and conversion routes with reviewed external links to AHA, NIDDK, ClinCalc and MDCalc. Added HAM-D link and optional locally recorded external-result→SOAP transfer with review gates. Existing unique ClinicalRx clinical/professional workflows remain.

130 automated tests pass, including no PREVENT form/scoring UI, external-only directory routes and review-required external-result transfer.12 destinations checked:11 returnedHTTP200; AHA direct checker returned403, but its public calculator page was retrievable through search. Link results are in CALCULATOR_LINK_CHECK.json. New release is not deployed or browser-verified.

Development policy: create a new interactive calculator only after a documented search shows no suitable validated online calculator exists and the primary method can be verified. PREVENT native licensing implementation is retired, not blocked. No patient inputs are automatically transmitted by link-out navigation.
