# Dr. Rosario / ClinicalRx build specification — v0.13.0

## Current phase and acceptance

Current delivered increment: Phase01D MDM evidence inference pilot, Phase04 switch-workflow usability, Phase02 medication-reference design. Full platform incomplete. Deployed v0.12.1 metoprolol conversion and procedure controls were browser-tested. New v0.13 has254 automated tests; deployed-browser acceptance remains pending. See AUDIT_0.13.0.md, REQUEST_MATRIX_0.13.0.md and PHASE_CHECKLIST.md.

## Identity and architecture

Dr. Rosario, PharmD is the professional brand; ClinicalRx is separately branded. Keep About → Experience → Clinical Practice → Research → Publications → Teaching → Presentations → Projects → Clinical Tools → CV → Contact. Free access, no account/paid backend. LinkedIn https://www.linkedin.com/in/norbertrosario/ is the only public contact. Never publish private CV email/phone or credentialing documents.

Buildless HTML/CSS/classic JavaScript; GitHub Pages main:/docs. All entrypoint assets share version0.13.0. Four pillars: Clinical Care, Drug & Evidence Intelligence, Professional Practice, Education. Use original code/design and primary/professional provenance. Example colleague sites and the excluded CMM website are not sources or outbound links.

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


## 0.11 implementation contract
- Keep four pillars, free access, LinkedIn-only personal contact and no automatic patient-data persistence. Public medication names/RxCUIs only to existing allowlisted sources; clinical text never to an LLM or drug API.
- CPA encounter begins with referral reason/referring physician; selected physician-established diagnoses precede Subjective and flow into assessment/plan headings. Preserve diagnoses during edits. ROS/PE reflects only actual work; objective has distinct vitals/labs/imaging/procedure/screening fields.
- Local MTP phrase candidates are suggestions, not validated diagnosis/interaction/dose detection. Confirm actual category/supporting facts. Manual records start blank/unconfirmed. Changes to source encounter invalidate confirmations across routes. Never infer implementation/resolution merely from confirmation. Actual-intervention text can support an implemented-process record, not a resolved outcome.
- Economic type mapping is visible before confirmation and editable. Source records include original metric, USD/price-year limits, population, setting, method, citation and URL. Sixteen reviewed intervention categories currently available. Display ranges of analogous historical means/coefficients, not pooled estimates or confidence intervals; no average of incompatible studies. Hypothetical subtotal excludes unconfirmed/unmatched/repeated event/type. Category sums and overall study means must not be combined; no receipts or causal patient-savings claim.
- Automatic E/M comparison currently uses actual qualifying time and new/established status. No MDM level inferred from text volume, diagnosis count, medicine count or historical history/exam counts. Free-text MDM automation requires independent fixtures before release. Medicare pharmacist-only office reference remains distinct from higher documentation candidates and payer-specific performer recognition.
- Fee subset is144 rows for nine office codes×eight Texas localities×QP/non-QP from hash-reviewed2026 annual carrier files (updated2025-12-29, rechecked2026-10-14). Annual base comparisons only; no FQHC/facility/telehealth or unavailable-year office benchmark. No contractual rate inferred.
- Generate >50% counseling statement only from valid actual face-to-face/total minutes and documented education. Include actual MD/DO availability only for an entered incident-to pathway and qualifying availability; never generate signatures/authentication or assert all billing prerequisites were satisfied.
- Switching Submit generates a conditional supported plan; edits clear old plans. New LAI pilot covers only stated exact oral/product initiation pairs; requires adult stable schizophrenia context, documented tolerability, label/interaction review, date and renal context where relevant. No missed-dose, depot-to-depot or unsupported agent schedule. Stimulants, antihypertensives and IR/ER expansion remains planned.
- Anticoagulation Submit can supply standard AF/DOAC no-bridge rationale but still requires procedure-specific interruption/risk review. High-risk bridge selection remains an explicitly approved-plan exception; no unrestricted procedure-name inference or dose rounding.
- PDC/MPR remains an educational single-unchanged-medication claims worksheet. Explain PQA abbreviations, VAS displayed/unrecorded distinction and separate claims/self-report interpretations; no certified measure or ingestion claim.
- CPA builder outputs original unexecuted draft with explicit action/drug/setting limits; supplied2023 protocol is structural input, not proof of current authority. All25 grouped scopes are opt-in. No private personal credentials, signatures or contact information copied.
- New-release acceptance includes automated tests, manifest/ZIP structure, and separately labeled browser/live evidence. Do not label a new local release browser-tested until actually deployed and tested.

## v0.12 recommendation-first acceptance contract

Anticoagulation asks for clinical facts, exact medication/regimen, procedure/date and risk context. A searchable procedure catalog supplies initial bleeding classification; overrides require rationale. Submit generates interruption/continuation and bridge reasoning, a conditional calendar, monitoring and AMA sources. It never asks for a prewritten interruption/bridge decision. DOACs do not receive a therapeutic bridge. High-risk warfarin exceptions are conditional, not automatic; dosing is withheld outside supported renal/weight/HIT contexts. No exact local clock interval is inferred. Neuraxial, urgent, actively bleeding and unstable cases require separate review.

Switching asks for current exact product/dose/frequency/duration, target and pertinent clinical facts, not a preapproved target starting dose. Supported paths: sertraline/escitalopram adult MDD, a historical olanzapine-to-risperidone strategy explicitly marked no longer maintained by its publisher, metoprolol tartrate IR-to-succinate ER for stable hypertension, methylphenidate IR-to-CONCERTA using its exact label table, and bounded oral-to-ARISTADA/SUSTENNA initiation. Unsupported pairs, depot conversions and complex contexts return review limits rather than invented schedules. All results require clinician review.

Medication lookup races RxNav with an independent NLM Clinical Tables/RxTerms request after a short delay. RxTerms is a named subset fallback with aligned RxCUI/form mappings; it is not represented as complete RxNorm coverage. Controls recover after success/failure and stale requests cannot overwrite a newer search. Public names/identifiers only are sent. The original v0.9 also used the same RxNav endpoint and 15-second timeout; the cause of the user-specific intermittent timeout is unresolved.

CPA builder preloads ten standard sections and 25 grouped scopes/classes paraphrased from the supplied CPA, without publishing its identifiers. Professional identities, degrees/training, physicians, setting and effective date are local inputs. Agreement term may be fixed, renewable or ongoing. Protocol review remains at least annual under Texas §295.13; a longer agreement term does not permit a longer review interval. Drafts are unexecuted and require local physician/legal/institutional review, exact clinical appendices and signatures. Two-business-day documentation is labeled sample institutional policy, not a universal statutory deadline. Dangerous-drug signing is a separate setting-specific notification/protocol-copy branch; ordinary CPA practice is not conflated with that branch.

## v0.12.1 medication recovery contract

Scope is limited to medication lookup. Automatic mode starts NLM RxTerms after 2.5 seconds and independent openFDA label-linked search after 5 seconds, or immediately after both NLM sources fail. An explicit Search FDA directly action bypasses NLM. Only validated public drug terms are transmitted. No proxy or clinical-text forwarding is introduced. Errors identify all failed hosts and leave controls retryable; no match does not produce an invented identity.

FDA harmonized RxCUIs are label-associated candidates, not an exact ingredient/strength/form relationship. Every candidate is marked accordingly; a visible warning accompanies label details and cabinet entries, and mapping limits remain in structured encounter metadata. Users must reconcile exact salt, strength, release form and actual regimen against the product label. FDA result limits and truncation are stated. FDA is not an exhaustive RxNorm replacement or an independent clinical recommendation source.

The reported Anticoagulation procedure dropdown and switch result display remain open defects. No added drug-pair scope or changed dose rule is delivered in this focused patch. The v0.12.1 generated UI requires deployed browser acceptance; runtime recovery checks are not represented as browser validation.

## v0.13 MDM and usability contract

`ClinicalEncounterReview.mdmCandidate` returns unreviewed component candidates, exact quote/field evidence, missing requirements and a documentation-only level/code when at least two recognized components support it. It uses bounded chronic-condition and prescription vocabularies; no general language-model understanding is claimed. Stability/worsening must be explicit in assessment; medication decisions must identify a supported prescription/dose and reason in plan. Unique explicitly reviewed/ordered test names are deduplicated; BMP/CMP overlap is withheld. Negated, historical and hypothetical evidence is conservatively excluded. High/straightforward, independent historian/interpretation and full CPT auditing remain outside this pilot.

MDM candidates never silently replace actual-time references or override payer/fee eligibility. Missing patient status withholds code mapping. No new PHI persistence or clinical narrative transmission. Changes recompute candidates locally; exact quotes are escaped in HTML. Unrecognized work remains for human review and is not assumed absent.

Switch UI filters reviewed targets by current product, labels incomplete facts, hides SSRI-only hepatic inputs outside relevant source paths, gives a clearly fictional reproducible example, and places the generated target dose before the dated actions. It remains a bounded clinical workflow, not a complete drug-pair database. Existing clinical dose rules are unchanged.

Medication UI uses original ClinicalRx task flow, source badges, public-name shortcuts, topic buttons and readable label sections; the actual source APIs and uncertainty disclosures remain. OpenRxData is a visual comparator only, not copied code/data or a clinical source. No new capabilities are inferred from appearance.
