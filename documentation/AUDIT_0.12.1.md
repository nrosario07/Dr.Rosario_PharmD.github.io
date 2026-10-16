# Focused medication audit — October 14, 2026 (America/Chicago)

## Observed in deployed browser

Repository docs/index.html uses v0.12.0 assets and allows both NLM API hosts in its CSP. A fresh deployed medication search for metoprolol returned 36 RxNorm identities at 2026-10-15T01:24:37.024Z. Selecting RxCUI 866514 retrieved 10 FDA label candidates; selecting the Lopressor record and Add selected product added metoprolol tartrate 50 MG Oral Tablet to the cabinet. Enrichment also rendered RxClass, MedlinePlus and PubMed results. These are public medication terms, not a patient case.

The user's timeout/CORS-like failure was not reproduced. This browser is separate from the user's browser; success here cannot rule out user-network, extension, DNS, regional routing or intermittent service problems. No specific cause is asserted and no instruction to disable protections is given.

## New patch verification

241 automated tests passed, including FDA-only bypass, both-NLM-unreachable/stuck recovery, cancellation, malformed/no-match refusal, HTTP 429 retry, public-term consent and UI control recovery. A real FDA request with both NLM hosts deliberately failed returned 19 metoprolol RxCUIs in 5.47 seconds. See MEDICATION_RECOVERY_RUNTIME_0.12.1.json. This is fault injection plus a real FDA response, not a new-release browser test. The original FDA response endpoint returned HTTP 200 with Access-Control-Allow-Origin: * in a separate runtime check.

## Primary technical sources

- FDA. Drug labeling API: harmonized RxCUI/generic/brand/substance fields. https://open.fda.gov/apis/drug/label/
- FDA. Drug labeling API query examples. https://open.fda.gov/apis/drug/label/example-api-queries/
- NLM. RxTerms Clinical Tables API. https://clinicaltables.nlm.nih.gov/apidoc/rxterms/v3/doc.html

FDA labeling/harmonization can be incomplete; a label may cover multiple strengths. Candidates are not an exact strength/form crosswalk, and returned labeling is not independently clinically appraised by this app.

## Post-upload acceptance still required

Confirm version 0.12.1. Search metoprolol using Look up, then use Search FDA directly. Confirm FDA mode returns candidates with mapping warnings and a source/retrieval time. Select a candidate, load/select an FDA label, inspect its exact product, add to cabinet, enter a fictional actual regimen and append to SOAP. Confirm no stale candidate survives a new search and no PHI is sent. FDA mode must work even when NLM is unavailable; if FDA also fails, retain the exact error and public drug term for investigation. All-external-host failure cannot be made functional by a static client alone.

## Open defects

Procedure dropdown and switch-result rendering remain unresolved in this focused release. No all-inclusive switch coverage or full-platform completion is asserted. No remote changes/deployment performed.
