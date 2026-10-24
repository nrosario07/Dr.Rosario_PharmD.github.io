# ClinicalRx 0.19.2 audit and release — October 24, 2026

## Deployed audit (v0.19.1)
- Repository manifest and live footer confirm v0.19.1.
- All 40 files in that manifest matched live HTTPS bytes. See DEPLOYED_0.19.1_INTEGRITY.json. This did not cover every public download in the older manifest.
- Four-pillar tool navigation and progress dashboard rendered.
- Browser: fictional metoprolol example submitted successfully; result displayed 100 mg daily ER conversion, dated action, monitoring and source. Changing input to 25 mg removed the prior recommendation and required resubmission. This verifies software behavior, not independent clinical validation.
- Repository .github/workflows returned 404. No hosted source-monitoring/CI run verified.
- No all-page, mobile, print/PDF, or all-pathway clinical acceptance claim.

## Implemented
- Expanded manifest from selected assets/data to every public file except the manifest itself, including downloadable files.
- Added read-only scripts/verify-deployment.py: compares deployed bytes with the local release manifest, reports missing/changed/unreachable files and fails incomplete deployment. Never sends encounter information.
- Simplified the progress dashboard to one current checkpoint plus expandable release details; removed contradictory historical pending statements.
- Corrected a stale source-directory description that referred to the removed Gap Closer.
- Preserved four pillars, free access, local-only drafts, source provenance, LinkedIn contact and existing clinical algorithms.
- Numbered upload batches remain below 100 files; complete site is in batch 01.

## Verification and limits
JavaScript regression suite passed. Python suite: 9 tests passed, including mixed deployment, unreachable files and unsafe paths. Public manifest and ZIP file/CRC checks passed. New v0.19.2 code has not yet been deployed/browser-accepted. Historical source claims were not comprehensively re-reviewed in this engineering increment.

## Current phase
Phase09 release governance advances; Phase00 usability and Phase04 switching receive focused acceptance evidence. Phase06 print/mobile acceptance remains open. Initial implementations 11/13; fully accepted tracks 0/13. The platform is not complete.

## Next
1. Upload numbered batches; verify deployment with `python scripts/verify-deployment.py --output deployment-report.json` after Pages finishes.
2. Install missing workflows using SOURCE_MONITOR_SETUP.md and confirm successful Actions runs. Hidden .github files often need manual creation via Add file → Create new file with the exact path.
3. Finish mobile/keyboard and print/PDF acceptance; expand anticoagulation and switching browser scenarios before adding clinical rules.
4. Independent review, normalized data and remaining education/diabetes/residency scope follow the phase checklist.

Visual defect fixed: single-event transition cards now span the calendar width; dose-heading contrast improved. CSS changes await deployed visual acceptance.
