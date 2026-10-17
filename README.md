# ClinicalRx0.14.2 by Dr. Rosario

Free four-pillar professional and clinical resource with LinkedIn-only contact. Fictional/de-identified cases only: no PHI or automatic clinical persistence. Public drug identifiers reach public APIs; clinical drafts remain in tab memory. Intentional exports require review.

Current increment: acceptance and usability—task entry points, note-section navigation, relevant switching controls, compact clinical headings and a public phase overview. Clinical algorithms are unchanged. Full platform incomplete. See documentation/PHASE_CHECKLIST.md, documentation/BUILD_SPECIFICATION.md and documentation/AUDIT_0.14.2.md.

293 local automated tests passed. Browser-tested deployed0.14: GLP-1 positive/GI refusal and medication→cabinet→SOAP→patient-plan review plus MTP candidates. New0.14.2 browser acceptance remains pending because GitHub rejected the source-write attempt with403 “Resource not accessible by integration.” No remote source change was made. Local/DOM tests are not independent clinical/coding validation.

Run `node --test tests/*.test.js`, `python scripts/validate-site.py` and `python scripts/package.py`. The packet preserves GitHub Pages main:/docs. Review UPLOAD_0.14.2.md only if an owner upload is needed. Source monitoring queues review and never automatically changes clinical recommendations.
