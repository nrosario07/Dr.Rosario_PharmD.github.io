# Migration Checklist from Previous ClinicalRx Repository

## Profile and portfolio
- [ ] Review the previous `docs/assets/content.js` and migrate approved profile, education, experience, research, publication, teaching and presentation records.
- [ ] Verify all dates and current appointments.
- [ ] Migrate only a public CV summary/PDF. Never publish personal email, phone, license numbers, credentialing files or confidential peer-review details.
- [ ] Keep LinkedIn as the only public contact method.

## Clinical tools
- [ ] Inventory each prior workspace and its dependencies.
- [ ] Migrate only after unit, integration, privacy and browser tests exist.
- [ ] Restore/fix missing modules rather than deleting tests that expose missing dependencies.
- [ ] Review medication switch, anticoagulation, clinical decision support, SOAP/MTP and patient-plan workflows independently.
- [ ] Confirm all output review gates reset after route changes, case resets and any restore/import action.
- [ ] Do not migrate stale reference data without source/version review.

## Data and sources
- [ ] Retain Texas CPA laws and Texas pharmacist code-pathway references after legal review.
- [ ] Retain CMS PFS reference data only after provenance, year, locality, code and dependency audit.
- [ ] Revalidate Purple Book or other local datasets before reuse.
- [ ] Do not migrate Texas VDP, Texas Medicaid formulary/coverage, drug pricing/reimbursement, or NDC-HCPCS pipelines.
- [ ] Clearly label source monitoring as monitoring-only unless validated publication is implemented.

## Technical cleanup
- [ ] Resolve all HTML script and stylesheet references.
- [ ] Resolve all JS imports and dynamic module dependencies.
- [ ] Lazy-load large optional reference indexes.
- [ ] Check CSP, external links, downloads, responsive layout and accessibility.
- [ ] Reconcile README, release notes, roadmap, acceptance checklist and workflow descriptions.
- [ ] Test clean install, local preview, CI and deployed site.
