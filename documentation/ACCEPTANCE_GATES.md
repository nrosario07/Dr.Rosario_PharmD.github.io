# Acceptance Gates

A phase is not complete because files exist or a deployment succeeded.

| Gate | Required evidence |
|---|---|
| Static foundation | Local preview, valid assets, responsive layout, keyboard navigation |
| Privacy | Tests prove no persistence and no outbound transmission of clinical drafts |
| Drug Intelligence | Source terms, license, request payload, error handling, provenance and test fixtures |
| Medication Review | Case isolation, reconciliation logic, discrepancy evidence, review gates, export controls |
| Guidelines | Source metadata, version history, six-month update calculation, historical lookup |
| CPA/practice | Primary legal sources, effective dates, legal review and institutional caveats |
| Billing | CMS source year/locality, Texas pathways, payer/product caveats, independent coding review |
| Source automation | Successful retrieval, schema validation, diff, human approval and published artifact |
| Release | All tests pass, deployed smoke test, accessibility and content acceptance |

Software tests do not establish clinical validity. Clinical, legal and coding review must be recorded separately.
