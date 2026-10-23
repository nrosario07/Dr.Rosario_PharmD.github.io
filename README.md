Current release: 0.18.2. Read UPLOAD_0.18.2.md and documentation/SOURCE_MONITOR_SETUP.md.

Current patch: 0.18.1. See UPLOAD_0.18.1.md and documentation/RELEASE_0.18.1.md.

Current release 0.18.0: progress dashboard and FDA fallback. Read UPLOAD_0.18.0.md.

Current release 0.17.0 (rebuilt). Read UPLOAD_0.17.0.md, especially missing workflow installation.

# ClinicalRx0.15.0 by Dr. Rosario

Free four-pillar professional and clinical resource. LinkedIn-only contact; fictional/de-identified cases only. No PHI or automatic clinical persistence. Public drug-name lookups reach public APIs; encounter drafts stay in tab memory. Exports require review.

Current phase:04 therapeutic switching. Adds nine GLP directions with evidence-tiered options, three formulation-conversion directions and a simpler conditional form. No universal equivalence or complete medication catalog. See documentation/BUILD_SPECIFICATION.md, PHASE_CHECKLIST.md and AUDIT_0.15.0.md.

337 automated tests pass. Browser-tested baseline0.14.2: task hub/four pillars, metoprolol example and corrected CSV-block feedback. New0.15.0 has not been deployed or browser-tested. Prior GitHub integration write403 remains unresolved. Automated tests do not replace independent clinical review.

Run `node --test tests/*.test.js`, `python scripts/validate-site.py` and `python scripts/package.py`. Pages remains main:/docs. Follow UPLOAD_0.15.0.md. Source monitoring queues review and never changes clinical recommendations automatically.
