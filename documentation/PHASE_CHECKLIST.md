# ClinicalRx phase acceptance checklist — 0.26.0

Updated October 26, 2026. This is the current acceptance record. Earlier checkpoint text is archived under documentation/history; release-specific audit files remain the evidence source.

**11/13 initial capabilities; 0/13 fully accepted.** Initial delivery is not percent complete. Future nutrition, affiliate, AI/video and separate-app expansion is paused until these tracks are accepted. Residency and diabetes remain part of the existing 13-track scope.

| Track | Scope | Current state | Required acceptance evidence | Remaining gate |
|---|---|---|---|---|
|00|Profile/navigation|Pilot|Every professional route, keyboard focus, 360/768/1280px layouts and no-overflow checks.|Technical acceptance|
|01B|Privacy/reporting|Pilot|Download and inspect SOAP, patient and reporting exports; verify clear/reload and no encounter data in outbound requests.|Technical acceptance|
|01D|SOAP/MTP/MDM|Pilot|Positive/negative language fixtures, confirmed MTP handling, quality leads, coding disagreement tests.|Independent clinician/coder review|
|01E|Economics|Reference|Trace each value to population/year/currency; test overlap and explicitly noncausal summaries.|Economic evidence review|
|02|Medication intelligence|Pilot|Exact identity/label recovery matrix, connected workflow and normalized public datasets.|Texas layouts/access; broader data coverage|
|03|Calculator directory|Reference|14 destination/version checks, topic/search/reset and keyboard/mobile acceptance; no duplicated calculators.|Current destination and permission ledger|
|04|Clinical workflows|Pilot|Enumerate supported product pairs and procedure scenarios, boundary tests and per-direction evidence.|Expanded coverage and independent clinical review|
|04D|Diabetes application|Not implemented|Define finite indication/population scope, verified guideline/label rules, exceptions and user workflows.|Application implementation and clinical validation|
|05|Professional practice|Pilot|Reconcile CPA clauses and billing references with current sources; separate eligibility from note complexity.|Texas professional review; local use requires approval/contracts|
|06|Education|Pilot|Inspect downloaded/printed plans; check completeness, teach-back, devices and bilingual materials.|Comprehension and language review|
|07|Adherence/quality|Pilot|Claims edge cases and VAS provenance; clearly distinguish public educational context from certified measures.|Measure specification/license and research review|
|08|Residency|Not implemented|Define initial program type; map lifecycle templates to current accreditation requirements.|Implementation and program-director review|
|09|Release/source governance|Maintainer tooling|Commit active workflow files, verify hosted release-check, source-monitor and Texas-data run artifacts, and inspect source review queue.|Hosted GitHub Actions runs still require owner verification after upload|

## Verified acceptance checkpoints in 0.26.0

- [x] v0.25.0 deployment: 48/48 public files match.
- [x] Phase 03 desktop topic/search/empty/reset controls, including keyboard reset.
- [x] Phase 03 primary-provider destination inventory: 14 URLs retrieved; PREVENT embedded content remains unverified.
- [x] Phase 01B/06 actual fictional HTML handout downloaded and its content inspected.
- [x] Phase 01B previous-payer carryover reproduced in browser and fixed with regression tests.
- [x] Phase 06 plan edits revoke agreement in both connected workspaces; automated tests verify review/export restrictions.
- [ ] Deployed browser acceptance of new fixes.
- [ ] Phase 00/03 mobile/responsive checks and complete keyboard path.
- [ ] Phase 06 visual print/PDF and comprehension/device/bilingual review.
- [ ] Phase 09 hosted workflow runs and successful artifacts (the active workflow files are included in this remediation package; hosted execution is not verifiable from the ZIP alone).

These completed checkpoints are not whole-phase completion. No clinical, licensing or institutional approval is inferred. The 11/13 figure described partial presence, not a sequential phase or 85% completion.

## Next work in order

1. Finish Phase 00/03 navigation, responsive and external-destination acceptance; inspect exported patient plans for Phase 01B/06.
2. Install/verify Phase 09 workflows. A documentation YAML copy does not activate GitHub Actions.
3. Expand Phase 04 exact-product switch evidence and boundary fixtures, then clinically review supported directions.
4. Complete data, economic, SOAP and adherence validation; implement the scoped diabetes and residency tracks.

External professional approval for a specific clinic is a deployment prerequisite, not a claim that software can approve a CPA, payer contract or billing eligibility. Continuous source monitoring continues after feature acceptance. No completion date is assigned until coverage and review capacity are fixed.
