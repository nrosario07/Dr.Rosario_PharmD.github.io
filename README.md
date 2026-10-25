# ClinicalRx · Dr. Norbert Rosario

**PharmD, BCPS, BCACP · Pharmacist Practitioner, educator and researcher**

Free educational tools connecting medication evidence, clinical documentation and professional practice.

[Visit the site](https://nrosario07.github.io/) · [Build specification](documentation/BUILD_SPECIFICATION.md) · [Phase checklist](documentation/PHASE_CHECKLIST.md) · [LinkedIn](https://www.linkedin.com/in/norbertrosario/)

## Current release

**0.22.0 — biosimilar designation clarity and medication data guide.**

[Release notes](documentation/RELEASE_0.22.0.md) · [Audit and verification limits](documentation/AUDIT_0.22.0.md) · [Upload instructions](UPLOAD.md)

The deployed 0.21.0 baseline matched all 48 public files. New 0.22.0 changes require deployed browser acceptance. Automated tests are software checks, not clinical validation.

## Four pillars

| Pillar | Capabilities |
| --- | --- |
| Clinical care | SOAP/MTP drafts, bounded switching and anticoagulation support, adherence education |
| Drug & evidence intelligence | Public medication identities and labels, source provenance and external references |
| Professional practice | Texas CPA drafts, credentialing preparation and business planning |
| Education | Patient-plan drafts, external calculators and a limited nutrition discussion-guide pilot |

## Typical workflow

1. Look up a public medication term and verify the exact product source.
2. Review a fictional/de-identified medication cabinet and synchronize it to the SOAP workspace.
3. Review MTP suggestions, documented actions and the patient plan.
4. Confirm the output contains no identifiers before exporting.

## Privacy and clinical limits

- Do not enter PHI. Clinical drafts use tab memory; no automatic save/restore.
- Public API requests send medication terms/identifiers and normal network metadata, not SOAP text.
- No account, analytics scripts or affiliate shopping links in this release.
- Outputs require professional review. A CPA, NPI or code suggestion does not establish billing eligibility.
- Source monitoring flags changes for review; it does not automatically change clinical recommendations.
- Nutrition is an education pilot, not a diagnostic or supplement-prescribing application. Expert review is pending.

## Repository map

| Path | Purpose |
| --- | --- |
| `docs/` | GitHub Pages site; entry point `docs/index.html` |
| `docs/assets/` | Browser application code and visual styles |
| `docs/data/` | Versioned reference data and release manifest |
| `documentation/` | Specification, audits, evidence review and release history |
| `scripts/` | Validation, deployment verification and packaging |
| `tests/` | Automated software regression tests |
| `.github/workflows/` | Release checks and source-monitor automation; installation must be verified |

The site is a static application, not an analytics notebook project. Its structure separates published assets from supporting evidence and tests without adding unused directories.

## Validate and package

Requirements: Node.js and Python 3. Tests use standard libraries.

```sh
node --test tests/*.test.js
python -m unittest discover -s tests -p 'test_*.py'
python scripts/validate-site.py
python scripts/package.py
```

GitHub Pages serves **main → /docs**. Browser-upload packets are split below the 100-file limit. Upload each batch's contents, preserving paths; do not upload wrapper folders or packet manifests.

## Roadmap and review

Initial capability exists in **11 of 13 original tracks**; **0 complete tracks have final acceptance**. These counts do not measure overall completion. The nutrition extension is tracked separately in Phase 06N and does not inflate that count.

Next: deployed UI acceptance, verified source-monitor installation, independent clinical/coding review, and broader workflow coverage. See the phase checklist for remaining gates. Report issues or collaborate through LinkedIn without patient information.

Core acceptance first: [13-track acceptance plan](documentation/CORE_ACCEPTANCE_PLAN.md). Future nutrition/affiliate expansion is paused. Current switch catalog has 22 directional pathways, not a comprehensive formulary.
