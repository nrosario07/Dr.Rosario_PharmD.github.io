# Dr. Rosario / ClinicalRx build specification — v0.9.0

## Current phase and acceptance

Phase 01C (evidence-linked SOAP/MTP, documentation and quality review) is implemented with explicit limits. Phase 02 medication intelligence continues; Phase 04 therapeutic switching and FDA relationships has a bounded pilot. The full platform is incomplete. Public diabetes app is removed pending a complete independently validated replacement. See PHASE_CHECKLIST.md and AUDIT_0.9.0.md.

## Identity and architecture

Dr. Rosario, PharmD is the professional brand; ClinicalRx is separately branded. Keep About → Experience → Clinical Practice → Research → Publications → Teaching → Presentations → Projects → Clinical Tools → CV → Contact. Free access, no account/paid backend. LinkedIn https://www.linkedin.com/in/norbertrosario/ is the only public contact. Never publish private CV email/phone or credentialing documents.

Buildless HTML/CSS/classic JavaScript; GitHub Pages main:/docs. All entrypoint assets share version0.9.0. Four pillars: Clinical Care, Drug & Evidence Intelligence, Professional Practice, Education. Use original code/design and primary/professional provenance. Example colleague sites and the excluded CMM website are not sources or outbound links.

## Privacy

Fictional or approved de-identified cases only; no PHI. Inputs exist in tab memory, with no automatic storage, backend, analytics or clinical-text API requests. Refresh/clear-all discards tab state. No-PHI review is required before in-app copy/download/print and clears when output changes. Intentional files remain on the user’s device and require approved handling; the website cannot detect every identifier or control operating-system/browser behavior. Remove local draft import/save/restore completely. Old #draft shows removal notice. Native browser printing cannot be prevented by this application. Public drug names/RxCUI and normal network metadata reach public APIs; no clinical facts are transmitted. Public lookup caches are distinct from patient draft storage.

## Modules and state

app/core: professional routes, transient state, escaped text, privacy export gate and SOAP generation. workspaces: clinical/subjective/objective/assessment/plan, actual history/exam, structured MTPs, agreed plan, teaching/monitoring/follow-up, diagnosis/payer/economic review. mtp-taxonomy: 36 supplied category/rationale labels, stable IDs; original prompts. clinical-support: independent documentation comparison, quality references, analogous economic benchmarks, public PQA threshold review and bounded switching. support-platform: switching, exact FDA relationships, legal/code tables and readiness/visual wrappers. purple-data: reviewed monthly FDA inventory. reporting: current-encounter process counts/CSV. calculator-links: one directory only; legacy calculator/conversion/screening routes alias it. drug-api/advanced-platform: existing public medication lookup/cabinet and reviewed calendar/inhaler flows. Generic score/conversion algorithms may remain as inactive pure code but no public scoring forms. Tests must cover absence of retired interfaces.

## SOAP/MTP documentation

One stable record per problem: domain/category/rationale, supporting facts/goal/alternative, action category, actual intervention, decision, implementation evidence and follow-up resolution. Acceptance is not implementation or resolution. Notes retain clinical reasoning and actual education/teach-back. No automatic diagnosis or clinical finding is invented.

Documentation-only office E/M comparison uses clinician-reviewed two-of-three MDM components or full qualifying reporting-practitioner time. New patient minima15/30/45/60 map99202–99205; established minima10/20/30/40 map99212–99215. No level from note volume/history/exam counts; no99201/prolonged/add-on inference. Missing actual SOAP/evidence stays flagged. Performer/payer recognition is a separate gate; Original Medicare pharmacist-only office E/M remains99211 incident-to if eligible. No eligibility from CPA or documentation level alone.

Quality: confirmed ICD references may produce limited diabetes/BP/lipid/ASCVD/COPD/HIV measure leads. Preserve source and year; mark potential only. Eligibility requires licensed/authorized specifications, age/enrollment/exclusions/medication/setting and measurement year. No certified HEDIS/Stars calculation or autonomous gap closure. Standalone Gap Closer retired.

Economics: each MTP has two-study historical analogous benchmark range with full AMA provenance and nonadditivity warnings. This does not complete per-rationale patient avoidance. Keep actual savings, modeled avoidance and practice receipts distinct. Local risk/direct comparison inputs remain independently reviewable. Never sum repeated/overlapping events.

## Medication, switching and FDA data

Existing medication engine uses RxNorm, exact openFDA/DailyMed label links, RxClass, MedlinePlus Connect and PubMed. Retrieval is not a synthesized prescribing monograph, complete DDI screen or price engine. Label set/effective/retrieval dates retained. Cabinet synchronization is explicit and clears clinical review gates. Visual improvements must not hide missing sections or provenance.

Switch pilot supports only declared oral adult pairs with prescriber-reviewed interaction/withdrawal/relapse/formulation and label-approved target dose. Dose/frequency/duration inputs are explicit; unsupported pairs receive no numeric plan. No autonomous orders, equivalence, MAOI/clozapine/depot/pregnancy/acute/complex-organ schedules. Table references are independent of the interactive pilot.

Purple Book: ingest full inventory section, not monthly change rows; retain exact product presentation, BLA, license type, reference name, strength/route, approval and interchangeability dates, marketing/license status. Filter351(k) Interchangeable + Licensed + explicit reference relationship. No biosimilar-to-biosimilar inference. September2026 snapshot includes246 biosimilar presentations,146 interchangeable presentations (not unique drug counts); SHA in data file. Source page checked October14; September was latest listed month. Monitor newer monthly files; reviewed rebuild script requires exact month/source/structure, tests and maintainer review before publication.

## Professional practice

Provide searchable service-code inventory and downloadable code/authority charts. Distinguish pharmacist direct benefit, clinical-staff contributions, reporting-practitioner-only services and facility claims. Show exact product/contract evidence; no universal Medicare cap applied to recognized commercial products, and no negotiation bypass of Original Medicare law. Medicaid benefit/enrollment needs actual policy; no blanket requirement that every arrangement be an APM. CPA notification branch: signing pharmacist submits LIC-1209/protocol before dangerous-drug signing in eligible settings; do not classify every nonsigning CPA as requiring the form. Current TMB rule location reviewed with reorganization matrix; historical slides are not controlling sources.

## Education and calculator policy

One Patient Plan Studio entry. Output comes only from agreed SOAP actions, monitoring, follow-up and education with preserved drug/dose/negation. Approximate grade3–5 readability, clinician review and no-PHI confirmation required. No automatic translation or invented action. All established calculators/conversions/screenings use one external directory; no embedded PREVENT, PHQ/GAD scoring or generic conversions. Adherence toolkit remains as the specifically requested research/claims educational workflow.

## Source monitoring and future API matrix

Public APIs/data never automatically change treatment rules. Source hashes/version metadata create review queues; GitHub workflow activation still needs deployment verification. Add monthly Purple Book page and FDA/NLM service sources; compare publication/effective dates, cosmetic versus material change, proposals versus effective guidance. Source monitoring failures cannot imply no changes. RxTerms, Orange Book and broad AccessGUDID/PMC normalized integrations are not delivered merely because they are linked. A complete ADA app needs source-versioned decision tables, exact label constraints, independent clinical fixtures and review governance; APIs alone cannot supply that logic.

## Delivery/testing

Reproducible tests: node --test tests/*.test.js. Packaging: python scripts/package.py. One ZIP with docs/source/tests/documentation/scripts/.github at root; exclude private uploads, caches, git and clinical drafts. External-public data only. Distinguish new automated results, deployed browser evidence and pending new-release/mobile/print verification. Update release notes/audit/checklist on each release; preserve documented limits rather than presenting all modules as complete.


## 0.10 implementation acceptance and source coverage
Current implementation phase:02; full platform incomplete. Deployed0.9 received documented browser acceptance on2026-10-14;0.10 is automated-tested, browser acceptance pending deployment. Medication sections expose actual API field names and one of FIELD_RETURNED/BROADER_SECTION_REVIEW/NOT_RETURNED. Counts are API coverage, never safety/completeness scores. No topic-specific claims are inferred from broader sections. A new query or blank exact-label choice must invalidate prior selection. Stale errors must not overwrite a newer request/view. Public package hashes live in docs/data/release-manifest.json; scripts/validate-site.py verifies loaded files/version/hash parity. Rebuild the manifest intentionally after edits, then test/package; never bypass failure to ship a partial upload. See RELEASE_0.10.0.md and AUDIT_0.10.0.md.
