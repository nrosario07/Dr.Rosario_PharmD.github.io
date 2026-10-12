# Dr. Rosario — nrosario07.github.io

Dr. Rosario, PharmD — professional portfolio and free ClinicalRx tools for healthcare professionals and students.

Guided clinical tools release 0.4.0, October 11, 2026. ClinicalRx is a working platform name.

A free static professional portfolio and tools workspace. No build, account, database, API key, paid service, external font or CDN dependency is required. The profile is populated from the supplied September 2026 CV and VA resume. LinkedIn is the sole public contact method; a curated public CV summary is included. Clinical content is an educational/reference release requiring institutional clinical review before patient use.

## Run and verify

Open `docs/index.html` in a browser. All scripts and reference data are local. Copy may require HTTPS; download works locally in normal browsers. Run `node --test tests/*.test.js` with Node 18 or newer. No package installation is required.

## Publish on GitHub Pages

Repository: https://github.com/nrosario07/nrosario07.github.io
GitHub Pages site: https://nrosario07.github.io/

1. Open repository Settings → Pages.
2. Under Build and deployment, choose Deploy from a branch.
3. Select main and /docs, then Save.
4. Leave Custom domain blank and keep HTTPS enabled.
5. Open the deployment URL shown by GitHub and check all navigation, a fictional note, source filters and downloads.

The repository is the account-root site, nrosario07.github.io. Relative paths also support a project site if moved later. No custom GitHub Actions configuration, paid plan or custom domain is needed.

The files are prepared for this repository. The GitHub connector can read the repository but rejected a blob upload with HTTP 403, Resource not accessible by integration. No site files were uploaded through the connector. Upload this package through GitHub Add file → Upload files, or grant the connection repository-content write access. The existing 0.2 site was already published; the 0.3 update still needs upload and deployment verification.

Official instructions: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## Files

- `docs/index.html`: static entrypoint with restrictive content security policy.
- `docs/assets/styles.css`: responsive presentation, keyboard focus and print styles.
- `docs/assets/app.js`: navigation, forms and browser-memory workflow.
- `docs/assets/core.js`: pure note, financial and foundation economic functions.
- `docs/assets/clinical.js`: reviewed limited rules, calculators, patient generation and structured exports.
- `docs/assets/workspaces.js`: guided smart-note/business/calculator controls and local events.
- `docs/data/clinical-rules.json` and `docs/assets/rules.js`: matching offline reference subset and source hashes.
- `docs/data/registry.json`: canonical versioned source/rationale metadata.
- `docs/assets/content.js`: offline copy of the registry, avoiding any fetch requests.
- `docs/downloads/`: original generic note and EHR adaptation guide.
- `documentation/BUILD_SPECIFICATION.md`: architecture, contracts, limitations and next-release requirements.
- `tests/`: meaningful unit and route smoke tests.

## Edit and rebuild

Profile rendering is in `profile()` in `docs/assets/app.js`. Profile metadata is in `docs/data/registry.json`; rendered profile sections read it directly. LinkedIn is the sole public contact method. A curated public CV PDF/TXT is under `docs/downloads/`. Do not add the contact details or original CVs from the private source documents. Do not expose private credentialing packets.

Edit `docs/data/registry.json`, then regenerate its offline bundle:

```sh
node scripts/sync-registry.js
node --test tests/*.test.js
```

Do not alter monetary coefficients or introduce billing mappings without review, source provenance, applicable payer rules and validation. All 36 rationale coefficients default to null. The four historical E03 references are INACTIVE.

## Release limitations

Automated checks cover core calculations, unknown values, output separation, escaping, reference structure and route smoke behavior. Visual/browser QA was unavailable in this environment; a real browser and mobile accessibility review remain necessary before clinical release. This is plain-text EHR adaptation, not a certified integration, import format, authentication system or claims engine.

Patient inputs stay in tab memory; reload clears them. User-initiated clipboard/download/print operations create copies under the user's control. Native browser session/cache behavior and the user's institution still require assessment. There is no representation of HIPAA certification. The public demonstration requests fictional/de-identified inputs until institution approval.

Original materials remain subject to the owner's rights. External sources are linked and summarized, not relicensed or reproduced in full. No patient data or uploaded private forms are included.

## Public CV generation

The included public CV is an original selected summary. To regenerate it, run `python scripts/public-cv.py` in an environment with ReportLab and DejaVu fonts; adjust the font paths for other operating systems. These dependencies are only for document generation, never for site visitors. Run `python scripts/package.py` to create the standalone preview and ZIP.

## Guided clinical tools release 0.3

Guided MTP/SOAP and business sections now include educational help and sources. Both tools share economic event records. Patient drafts derive from agreed SOAP instructions and require explicit review before download. The limited service review uses Original Medicare office incident-to gates and a clinic-specific MD/DO sign-off control; it never assigns higher E/M levels from pharmacist note complexity. A small FY2027 ICD-10-CM subset supplies candidates for confirmation. CMS annual 2026 Texas benchmarks are historical published base references, not current claim quotes. Adult BMI and legacy Cockcroft–Gault calculators require explicit applicability inputs.

Run `node --test tests/*.test.js`. Read [the current implementation specification](documentation/BUILD_SPECIFICATION.md) and [release validation](documentation/RELEASE_0.4.md). The reference rebuild script is maintainer-only and verifies pinned CDC/CMS archive hashes. Encounter inputs are never sent to APIs; public medication lookups are opt-in and separate. No patient data is intended to leave the browser or persists after reload. Structured JSON/CSV exports require a de-identified encounter reference and approved storage. No vendor-certified EHR import is supplied.

### Payer clarification 0.3.1

Broader potential codes are retained for explicit payer/contract review: 48 reference identifiers across 14 families. Commercial higher E/M, MA negotiated terms, PartD MTM sponsor payment and Texas MCO arrangements are distinguished from Original Medicare PFS rules. No universal Medicaid APM requirement is asserted. The contract-review appendix records terms and unmet evidence without automatically converting them into claims or business collections. CMS May2026 deprescribing guidance and inactive CY2027 proposals are linked. See the current specification and release note.

## Clinical tools 0.4

Fixes full-width radio controls shown in owner screenshots and reduces MTP/business screens to essentials with collapsed optional sections. Restores the four pillars and adds public RxNorm/openFDA drug lookup, adherence/PDC/MPR/owner-scale review, AF scores, CKD-EPI eGFR, percent weight loss, PHQ-9, a mathematical taper aid, quality-gap organizer and twenty source-linked condition review worksheets. Readiness is explicit: worksheets are not completed prescribing algorithms. Structured payer-recognized E/M criteria may produce a conditional established-patient candidate after actual SOAP/performer/policy review; Original Medicare office limits remain separate.

Weekly ChatGPT source-change alerts were created separately for Monday8am America/Chicago. Optional GitHub source-monitor workflow runs Mondays14:00UTC after upload, writes a review artifact and never changes clinical rules. Public page hashes can change cosmetically; clinical rule updates require source/effective-date review and tests. No claim that everything is automatically current. DailyMed direct links are used because browser CORS was not verified. See RELEASE_0.4.md for the manual upload and fictional-case review checklist.
