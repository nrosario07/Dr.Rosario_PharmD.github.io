# ClinicalRx v0.13.0 by Dr. Rosario

Free four-pillar professional and clinical resource; LinkedIn-only contact. Fictional/de-identified cases only. No PHI, automatic clinical persistence or clinical-text API transmission. Reviewed intentional exports remain local files.

Current: Phase 01D MDM evidence inference pilot; Phase 04 recommendation-workflow usability; Phase 02 medication-reference design. Full platform incomplete. Read documentation/PHASE_CHECKLIST.md, documentation/BUILD_SPECIFICATION.md and documentation/AUDIT_0.13.0.md.

254 automated tests passed. The deployed v0.12.1 metoprolol example generated a 100 mg once-daily succinate ER suggestion from tartrate 50 mg twice daily in the bounded hypertension pathway; all nine procedure options appeared and selecting a major-joint procedure updated its category. These browser observations do not verify the new v0.13 interface. New-release browser acceptance remains pending.

Run `node --test tests/*.test.js`, `python scripts/validate-site.py`, and `python scripts/package.py`. Upload the extracted packet per UPLOAD_0.13.0.md; GitHub Pages remains main:/docs. Never automatically publish clinical rule changes from monitoring.
