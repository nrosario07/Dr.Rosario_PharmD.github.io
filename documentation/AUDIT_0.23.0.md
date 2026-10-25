# ClinicalRx 0.23.0 — focused evidence browsing and import validation

October 25, 2026. Active: Phase02 medication intelligence and Phase09 source/release governance. 11/13 tracks have initial implementations; 0/13 complete acceptance. This is a focused improvement, not completion of the 13-track platform.

## Audit of uploaded 0.22.0
- Public deployment: all 48 manifest files matched (DEPLOYED_0.22.0_INTEGRITY.json).
- Browser: Ahzantive search yielded 2 presentations; interchangeable filter yielded 0. Abrilada yielded 5 presentations. Desktop view inspected; all 246 records were on one long results page.
- Browser: metformin lookup succeeded; selected RxCUI861007 (500mg oral tablet), selected Ascend label, added to cabinet and appended to SOAP. SOAP retained the identity and explicitly showed regimen not entered / not reconciled.
- Browser: entered fictional nonprescribing SOAP actions, monitoring, follow-up and education. Confirming agreed actions generated the corresponding patient plan. It did not convert the unreconciled cabinet into medication instructions. Clear-all removed the fictional encounter content.
- Repository connector: .github/workflows/source-monitor.yml and release-check.yml both returned404. Workflow installation remains unverified/not found. No scheduled monitoring claim.
- This was not an exhaustive audit of every clinical algorithm. Downloads/print output, narrow-screen behavior, and independent clinical/coding review remain open.

## Changes in 0.23.0
- Biosimilar explorer: 12 presentations per page; next/previous with boundaries; alphabetic product ordering; exact reference and reported marketing filters; reset filters; count of distinct BLA identifiers. Changing any filter resets to page1; empty results disable pagination.
- Responsive presentation labels for narrow screens; scoped table styling, visible focus indicators and collapsible designation explanation. Original FDA statuses and dates are preserved.
- Medication data guide uses distinct descriptive links, responsive cards and same-tab navigation for local tools. No external-source link masquerades as a local feature.
- FDA importer validates columns, identifiers, designation values, date formats, month/source, and conflicting BLA/product records before writing. Exact duplicates are counted and removed. Successful staging creates a review-required report; nothing is automatically published.
- Official September CSV passed the new parser:246 records,0 exact duplicates, SHA256 b9d04a8b1ea9c6605fdeff01127f0de32cb092534a40441b036e39c9665974e6. Published snapshot was not changed.

## Validation boundaries
400 JavaScript tests and16 Python tests pass. Includes simulated-DOM pagination/filter/navigation checks and seven import-validation cases. Packaging checks file hashes and ZIP integrity. Automated DOM tests are not browser visual tests. New 0.23 styles and controls await deployed browser/mobile acceptance; 0.22 workflow observations do not certify the new layout.

## Next ordered work
1. Install both supplied Actions workflows and verify successful manual runs; setup instructions included.
2. Browser-accept 0.23 paging, filters, keyboard navigation and narrow-screen cards; inspect exported patient handout.
3. Proceed with normalized public NADAC/HCPCS data ingestion, carrying identifiers, units, effective dates, source hashes and review gates. No invented AWP/WAC/MAC/340B feed.
4. Expand exact-product switching only with reviewed evidence and boundary tests. Product-level orphan and gene/cell catalogs remain pending.
5. Complete independent clinical/coding reviews and larger diabetes/residency implementations before closing those tracks. No reliable full-completion date yet.
