# ClinicalRx 0.22.0 — medication data clarity

Date: October 25, 2026. Focus: Phase02 medication intelligence and Phase09 acceptance. Original 13 tracks: 11 have initial implementations; 0 have full documented acceptance. No track is closed by this release.

## Delivered
- Biosimilar explorer now includes 246 licensed product-presentation relationships: 146 FDA-interchangeable and 100 biosimilar without interchangeability designation. Search brand, proper name, reference or BLA; filter designation. Counts distinguish presentations from BLAs.
- Explicit discontinued-marketing labels, separate approval/interchangeability dates, empty results feedback, and dated snapshot provenance.
- Medication data guide accessible from the four-pillar finder and medication workspace: NADAC, AWP/WAC, MAC, 340B, ASP, HCPCS, orphan status and in vivo/ex vivo/other cell-therapy distinctions. These are source references, not integrated live prices or a comprehensive therapy catalog.
- Corrected stale current-release specification header. Preserved four pillars, free access, LinkedIn contact and tab-only case handling.

## Audit and test boundaries
- Deployed v0.21.0: 48/48 manifest files match (DEPLOYED_0.21.0_INTEGRITY.json).
- Browser tested deployed biosimilar search: Ahzantive returned zero rows because the old page excluded non-interchangeable biosimilars. Fixed in this package; new filter covered by automated simulated-DOM tests.
- FDA September CSV independently downloaded and SHA-256 matched bundled source: b9d04a8b1ea9c6605fdeff01127f0de32cb092534a40441b036e39c9665974e6. September is the latest month observed on the official download listing during this review. This does not assert all live FDA changes through October are in the snapshot.
- New release layout and keyboard/mobile behavior are NOT browser-accepted yet. Full medication → cabinet → SOAP → patient-plan workflow was not repeated in this release. No comprehensive new clinical validation is claimed.
- No new dosing or switching algorithm. No clinical recommendations automatically updated.

## Next ordered acceptance work
1. Deploy and browser-accept the new filter, clear empty state and data guide on desktop and mobile.
2. Implement dated NADAC NDC/unit matching and HCPCS quarterly ingestion with schema checks, hashes, rejected-record reporting and explicit coverage boundaries.
3. Build reviewed product-level in vivo/ex vivo/other-cell and orphan records with FDA approval/indication identifiers; do not infer classification from names.
4. Continue exact-product switch coverage and independent clinical review; repeat the connected medication/encounter/export workflow.
5. Verify the repository source-monitor workflows actually run. A configured script alone is not continuous monitoring.

## Not complete / blocked
Full AWP/WAC/MAC/340B pricing is not an open national feed in this build. 340B ceiling prices require authorized access. Product-level therapy and orphan catalogs, HCPCS and NADAC integration remain pending. No honest completion date can be set until data and clinical acceptance gates are met. Future nutrition commerce and AI studio remain deferred behind core acceptance.
