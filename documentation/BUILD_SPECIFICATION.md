# Dr. Rosario / ClinicalRx build specification — v0.26.0

## Current phase and acceptance

Phase02 medication intelligence and Phase09 acceptance are active. See RELEASE_0.24.0.md and CORE_ACCEPTANCE_PLAN.md. 11/13 tracks have initial implementations; 0/13 are fully accepted. This release adds paginated biosimilar browsing, exact reference/marketing filters, source-card clarity and fail-closed FDA import validation. Pricing and specialty-therapy product integrations remain pending. Earlier contracts below remain historical implementation detail where not superseded.

### Resources contract
Nine original source cards provide local search/filter/reset, links to specialist checkers and patient references, and explicit API/candidate status. External links never include cabinet or encounter data. Shortage API uses public medication names only, shows status/date/product/source, caps records at100 and displays total, uses a five-minute memory cache, and distinguishes no matches from network failure. Input edits invalidate results and stale replies cannot replace changed inputs. No general interaction clearance is inferred. No third-party clinical content is copied.

### Tool discovery contract

A local search covers all four pillars and the available condition modules, with a pillar selector, live result counts, keyboard-accessible controls, empty state and clear action. Search uses case-insensitive AND matching across titles, aliases and type labels. Search is not transmitted or persisted. The default view retains four pillars and task shortcuts; condition modules are collapsed initially. Result labels distinguish tool/reference entries from module readiness descriptions. No clinical capability is inferred from a search match. Responsive styles stack the finder and result cards on narrow screens; visual acceptance remains pending.

### Current switch contract

Nine exact-product adult-T2DM directions include Mounjaro as a source to Ozempic/Trulicity. UI defaults to evidence-informed review; conservative label initiation is explicitly selectable. Both modes validate product dose, frequency, last-dose date, current tolerance, adult context and safety findings. No GLP-1 overlap or universal equipotent conversion.

- Selected adults meeting implemented prospective-study screens can receive a tirzepatide5mg weekly off-label option. Screens: studied source/dose, stable3calendar months and at least13weeks (conservative implementation), A1c6.5–9%, BMI≥25 and explicit evidence/suitability review. This is not a complete trial-eligibility determination.
- Expert semaglutide0.5mg weekly option requires a tolerated maintenance regimen for at least4weeks. Implemented source thresholds: liraglutide1.8mg, dulaglutide≥1.5mg or tirzepatide≥5mg. These are conservative implementation boundaries. Tirzepatide→semaglutide is explicitly extrapolated, not a direct reverse-switch trial.
- Case-series higher starts are reference context only. The semaglutide2mg→tirzepatide10mg observation is not reversed into a tirzepatide10mg→semaglutide2mg recommendation. Indirect efficacy differences are presented separately from transition doses.
- Venlafaxine IR→ER capsules and bupropion HCl IR/SR→XL use bounded label-supported total-daily-dose formulation conversions. Adult MDD and reviewed normal renal/hepatic context required. Unsupported doses, formulations or indications return no regimen.
- Numeric age is no longer universally required. The explicit stable-adult context remains required. Exact age is retained for existing restricted CONCERTA, historical olanzapine and LAI pathways. Supplied invalid/pediatric ages are rejected. Age-related risks, frailty and organ function cannot be declared irrelevant.
- Every result is conditional, dated and source-linked in AMA format. Changed inputs clear prior output and privacy review. Changing source/target/evidence approach clears the evidence acknowledgement. No autonomous prescribing or automatic source-driven dose updates.

Form uses numbered treatment/context/GLP sections, conditional fields, collapsible evidence comparisons and monitoring details. No paid services, clinical input transmission or new persistence.

## Identity and architecture

Dr. Rosario, PharmD is the professional brand; ClinicalRx is separately branded. Keep About → Experience → Clinical Practice → Research → Publications → Teaching → Presentations → Projects → Clinical Tools → CV → Contact. Free access, no account/paid backend. LinkedIn https://www.linkedin.com/in/norbertrosario/ is the only public contact. Never publish private CV email/phone or credentialing documents.

Buildless HTML/CSS/classic JavaScript; GitHub Pages main:/docs. All entrypoint assets share version0.15.0. Four pillars: Clinical Care, Drug & Evidence Intelligence, Professional Practice, Education. Use original code/design and primary/professional provenance. Example colleague sites and the excluded CMM website are not sources or outbound links.

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

Historical v0.12.1 status: the Anticoagulation procedure dropdown and switch result display were open defects at that release; later increments supersede this status. No added drug-pair scope or changed dose rule is delivered in this focused patch. The v0.12.1 generated UI requires deployed browser acceptance; runtime recovery checks are not represented as browser validation.

## v0.13 MDM and usability contract

`ClinicalEncounterReview.mdmCandidate` returns unreviewed component candidates, exact quote/field evidence, missing requirements and a documentation-only level/code when at least two recognized components support it. It uses bounded chronic-condition and prescription vocabularies; no general language-model understanding is claimed. Stability/worsening must be explicit in assessment; medication decisions must identify a supported prescription/dose and reason in plan. Unique explicitly reviewed/ordered test names are deduplicated; BMP/CMP overlap is withheld. Negated, historical and hypothetical evidence is conservatively excluded. High/straightforward, independent historian/interpretation and full CPT auditing remain outside this pilot.

MDM candidates never silently replace actual-time references or override payer/fee eligibility. Missing patient status withholds code mapping. No new PHI persistence or clinical narrative transmission. Changes recompute candidates locally; exact quotes are escaped in HTML. Unrecognized work remains for human review and is not assumed absent.

Switch UI filters reviewed targets by current product, labels incomplete facts, hides SSRI-only hepatic inputs outside relevant source paths, gives a clearly fictional reproducible example, and places the generated target dose before the dated actions. It remains a bounded clinical workflow, not a complete drug-pair database. Existing clinical dose rules are unchanged.

Medication UI uses original ClinicalRx task flow, source badges, public-name shortcuts, topic buttons and readable label sections; the actual source APIs and uncertainty disclosures remain. OpenRxData is a visual comparator only, not copied code/data or a clinical source. No new capabilities are inferred from appearance.

## Historical v0.14 expanded coverage contract (GLP behavior superseded by v0.15)

`glpSwitch` supports seven exact-product adult-T2DM directions from Victoza, Ozempic and Trulicity into selected weekly targets including Mounjaro. Current dose/frequency/duration, last dose and clinical context must be supplied; first target date is derived from last dose. Generic transition-date input is hidden for this branch. Default schedule uses reviewed target-label starts and conditional titration/reassessment, not inferred equipotent doses. Safety, current GI tolerance and insulin/sulfonylurea context cannot default to absent. No overlapping full GLP-1 regimens, automatic hypoglycemia dose reduction or invented high-dose target. Tirzepatide5mg direct-switch research is an explicitly off-label alternative for full clinician appraisal, not generated calendar instructions. Timing guidance is expert-based; extension to tirzepatide is marked extrapolation. Sources, populations and maintenance limits remain visible.

MTP detection recognizes a wider bounded phrase vocabulary, excludes documented negatives/hypothetical/resolved findings, and requires confirmation. It is not comprehensive NLP or a clinical interaction/dose checker. Economic mapping remains a reviewed suggestion; ambiguous multi-action plans do not assign every finding one inferred action. The original36-category taxonomy/manual pathway remains.

Time-only text must not contradict the independent MDM evidence assistant. Incomplete encounter draft fields must be visible beside a component-based candidate. No new performer/payer eligibility or fee calculation from unreviewed MDM. Medication reference typography is compact and route-scoped, preserving professional profile design and working API recovery.

## v0.14.2 workflow contract

Section-jump controls use native buttons, focus the existing section and do not modify hash routes, note content or export-review state. Detailed switch coverage remains available in a native disclosure. GLP-1 paths omit irrelevant withdrawal inputs; LAI-specific inputs appear only for appropriate targets. Public release copy must reflect actual pilot status and identify later work without claiming independent validation. Preserve clinical algorithms, privacy gates, four pillars and free access through this UI-only increment.


## 0.18.0 progress contract
Sources & provenance renders two labeled native progress elements: initial implementation tracks (11/13) and documented full-track acceptance (0/13). All 13 tracks are expandable with remaining requirements and relevant links. No invented overall completion percentage or final date. Monitoring state is a dated manual repository observation, not a live health check. Clinical rules remain unchanged.


## 0.18.1 workflow checkpoint

- Local identity filter by name, strength, form or RxCUI; all terms must match. Selected identity stays available; no extra API request.
- Direct cabinet links to SOAP/MTP and patient plan; transfer confirmation beside cabinet.
- About introduction uses Pharmacist Practitioner terminology.
- No changes to dosing, clinical recommendations, payer rules or external data transmission.

## Verification
- GitHub manifest and live footer report 0.18.0. Full remote file-by-file hashing was not performed.
- Live browser: metformin returned 134 RxNorm identities. Selected RxCUI 861007 and Ascend label dated 20251218; added product, entered fictional regimen, synced cabinet to SOAP, entered fictional SOAP actions and verified generated patient plan. Review checkbox enabled patient download. An initial transfer was not observed; a settled retry succeeded, so no reproducible transfer defect is claimed.
- MedlinePlus and PubMed enrichment rendered. This is one successful query, not comprehensive API acceptance.
- 348 automated tests pass, including local filtering, selected-identity retention, cabinet-to-SOAP transfer and patient-plan generation.
- New 0.18.1 UI is not browser-tested until uploaded. Actual downloaded patient file, mobile layouts, broad drug coverage and external checker accuracy remain unverified this release.
- Source-monitor workflow path still returned GitHub 404. Install instructions remain required; no scheduled clinical auto-update is claimed.

## Phase progress
11/13 tracks have initial capabilities; 0/13 fully accepted. Remain in Phase02 connected medication workflows with Phase09 monitoring installation blocked. Successful fictional workflow is a partial acceptance checkpoint, not phase closure. Next: deployed filter/navigation acceptance, actual export and mobile regression, then broader normalized data and source-reviewed switch coverage.


## 0.18.2 requirements and acceptance checkpoint
# ClinicalRx 0.18.2 — workflow integrity and release governance

Date: October 21, 2026 (America/Chicago).

## Verified deployment
GitHub and the deployed footer report 0.18.1. The remote manifest matches all 40 hashes in the previously packaged local manifest. Individual remote files were not independently rehashed.

## Reproduced issue and fix
After syncing a fictional metformin regimen, editing it left the cabinet's synced message unchanged. SOAP retained the old regimen. New code compares the current cabinet with the linked snapshot and the reconciliation block, shows stale status on cabinet and SOAP, and blocks download/copy/print through the shared export controls for connected clinical workspaces until the cabinet is re-synced. Existing clinical prose outside the cabinet block is preserved. This does not synchronize treatment decisions or turn a medication list into patient instructions.

## Next phase increment: 09 governance
Added a read-only release-check workflow (bundle integrity, JS regressions, Python governance tests), a human-readable source review summary, and explicit per-source baseline approval with reviewer/rationale. No automatic clinical recommendations, doses or baseline approvals. The source-monitor workflow remains absent remotely; workflow installation and first successful hosted run remain blocked on repository setup. The test workflow does not automatically gate the separate Pages deployment.

## Browser-tested on deployed 0.18.1
- RxNorm metformin lookup: 134 identities; filter “500 oral”: 51 results.
- RxCUI 861007 remains selected when filtering for 1000.
- Selected Ascend FDA label, added/reconciled fictional cabinet, synced and used direct SOAP link.
- Reproduced stale synced status after regimen edit; re-sync placed corrected regimen in SOAP.
- Generated fictional patient plan, confirmed review/no-PHI gate, downloaded actual text and inspected it. File matches displayed plan and excludes RxCUI/internal coding text.

## Automated verification
349 JavaScript regression tests passed, including stale-cabinet export refusal and recovery after re-sync. Five Python governance tests passed, including refusal of unavailable/bad-hash sources and preservation of unrelated baseline entries. Final manifest and ZIP integrity results accompany packaging.

## Still unverified
New 0.18.2 browser behavior after upload; mobile/keyboard regression; broad drug and clinical coverage; hosted workflow execution; first reviewed monitoring baseline. No new clinical algorithm or dosing equivalence was released.

## Progress
Initial capability: 11/13 phase tracks. Full acceptance: 0/13. Phase02 connected workflows now has a completed desktop export checkpoint; Phase09 adds tested maintainer tooling. Entire phase completion still requires its broader acceptance criteria. Next: deploy/test this fix, install/run workflows, complete responsive regression, then normalized evidence and exact-product switch expansion.


## 0.19.0 implementation and acceptance
# ClinicalRx 0.19.0 — printable patient education

Assessment date: October 22, 2026 (America/Chicago).

## Delivered
- Printable patient handout from the same agreed SOAP plan used by the text draft. Large headings, five sections, readable spacing, responsive layout and print styles; open the downloaded HTML locally and use Print / Save as PDF.
- Requires a complete agreed plan, clinician review and the existing no-PHI export gate. Form edits revoke review; stale cabinet protection also applies. No medication instruction is inferred from the cabinet.
- Handout escapes entered text, loads no remote assets/scripts, preserves the existing plain-language transformation rules, and excludes billing/economic/assessment/objective metadata. No promised or independently validated reading grade.
- Education Studio fields now use explanatory labels and point to the reviewed handout export in SOAP.
- Mobile menu Escape closes the menu and returns keyboard focus to its button. Narrow-screen brand spacing and form-width constraints improved. Mobile behavior still needs device/browser acceptance.

## Deployed audit: v0.18.2
GitHub manifest and live footer report 0.18.2. This session did not independently hash every deployed asset.

Browser-tested fictional scenario: public metformin RxNorm lookup, selected RxCUI 861007 and Ascend label; added product and synced cabinet. Editing regimen produced the stale warning. SOAP showed its warning and refused Download .txt with an explicit mismatch message. Following the cabinet link, re-syncing and returning to SOAP cleared the warning. After no-PHI confirmation, Download .txt succeeded. Downloaded file was read and contains the updated fictional once-daily regimen. This is workflow verification, not a completed clinical encounter or dosing recommendation.

Both .github/workflows/source-monitor.yml and .github/workflows/release-check.yml returned 404 from GitHub. Neither workflow is active/verified. Installation instructions remain in SOURCE_MONITOR_SETUP.md. No remote writes or workflow installation occurred.

## Tests and limits
353 JavaScript tests passed; five Python governance tests passed. New tests verify handout completeness/review/privacy gates, HTML escaping, instruction preservation and exclusion of internal data. ZIP contents and public manifest checked during packaging.

Unverified: deployed v0.19.0 handout rendering/printing; mobile layout and Escape behavior; whole-site keyboard acceptance; hosted workflow execution and source baseline; broader drug/clinical coverage. No clinical algorithms, dosing rules or billing eligibility rules changed.

## Phase status
Phase02 connected workflow acceptance advanced: stale-cabinet refusal and recovery now browser-tested. Phase06 education implementation advanced: reviewed printable handout added. Phase00 responsive/keyboard refinements remain pending deployed acceptance. Phase09 blocked on workflow installation and hosted execution. 11/13 tracks have initial capabilities; 0/13 tracks fully accepted. No comprehensive completion claim or final completion date.

Next: upload and accept the handout and mobile changes; install/run both workflows; broaden switch and anticoagulation browser scenarios; then exact-product evidence/data expansion.

Visual audit follow-up: standardized medication/patient action buttons and next-step links after observing default browser button styling in the deployed cabinet. New styling requires deployed visual acceptance.


# ClinicalRx 0.19.1 — deployment reliability checkpoint

Audit date: October 24, 2026.

## Observed on deployed v0.19.0
- Footer and repository release manifest identify 0.19.0. Full deployed byte-for-byte parity was not established.
- Fictional case creates a complete patient plan; export remains disabled before review.
- After patient-plan and de-identification review, printable HTML downloads successfully.
- Editing follow-up invalidates review and disables handout download. Updated text appears in patient plan.
- Desktop patient-plan workspace visually inspected. Not an all-page/all-tool or mobile acceptance audit.
- Repository .github/workflows lookup returns 404. Hosted CI and scheduled monitoring remain unverified/uninstalled at this path.
- Browser policy prevents opening downloaded file URLs. Print/PDF rendering remains unverified; no workaround used.

## Changes
- Version-independent packager reads the release manifest, avoiding future preview version drift.
- One upload packet contains numbered batches with fewer than 100 files each. All 50 website files remain in one batch.
- Supporting files preserve repository-relative paths; no omissions, duplicates or flattened folders.
- ZIP integrity and every packaged file's bytes checked against source. SHA256 inventory included.
- Corrected a stale test expecting an older monitoring-status label; requirement remains installation-required.
- No clinical algorithms, dose recommendations, payer rules or source baselines changed.

## Phase status
Phase06 education: deployed download/re-review checkpoint passed; print and mobile acceptance open.
Phase09 release governance: bounded upload packaging implemented; hosted monitoring still blocked.
Initial capabilities: 11/13 tracks. Fully accepted tracks: 0/13. This is not an overall completion percentage.
Next: print/mobile and keyboard acceptance, install and verify workflows, broader switch/anticoagulation browser fixtures, then source-reviewed exact-product coverage.
No reliable all-phases completion date while independent review, data rights and later residency scope remain unresolved.


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


# Later enhancement: business education and video studio

Requested October 24, 2026. Deferred until the current platform phases are complete, per owner preference. This is planned scope, not a working AI/video product or a claim of free rendering capacity.

Audience: students and healthcare professionals. Journey: idea and problem discovery → customer validation → value proposition → market and competitive analysis → business model → operations and staffing → regulatory/payer considerations → financial assumptions and scenarios → implementation roadmap → CEO/board presentation.

Outputs: short cited educational video scripts, storyboards, captions/transcripts, consultation worksheets, business-plan sections, financial assumption tables and presentation outlines. Video generation, narration and rendering require a separately evaluated provider, cost/usage limits, rights and privacy review; do not promise perpetual free AI generation.

Start materials intake when core phase acceptance is complete and this enhancement is activated. First request: course inventory/syllabi, learning objectives, original notes and owner-created business plans/examples. Six remaining MBA courses may be added incrementally through December 2027. No need to wait for graduation once this enhancement begins.

Suggested future folder layout: 01_course_inventory, 02_original_notes, 03_reusable_templates, 04_permission_cleared_sources, 05_deidentified_examples, 06_video_topics. Read-only OneDrive access to the selected folder is sufficient if supported by the connected tools. Do not include student records, patient data, employer-confidential plans or exam banks. Record rights/permission for textbook excerpts and instructor slides before republishing or generating derivative public content.

Acceptance: cited claims and calculation assumptions; clear educational/consulting boundaries; owner review before publication; accessible captions/transcripts; separate learner and executive outputs; no automatic public posting. Each lesson carries source, date, permitted use and reviewer metadata. Materials optimize the business tool only after an explicit source-to-feature map and gap assessment.

Visual defect fixed: single-event transition cards now span the calendar width; dose-heading contrast improved. CSS changes await deployed visual acceptance.


# ClinicalRx 0.19.3 — release consistency and anticoagulation acceptance
Audit: October 24, 2026.

## Findings
Repository manifest and app.js identify v0.19.2. Latest inspected GitHub Pages build succeeded (run 40105291590). Direct HTTPS check matched 47/49 manifest entries; the two unavailable entries were deployment/build artifacts that should not have been tested as public URLs. All 47 intended public content files matched. The browser requested v0.19.2 assets but continued to display runtime v0.19.1 after one reload. Cause is not established; do not call this a complete browser acceptance of v0.19.2.

## Browser-tested on the observed runtime
- Anticoagulation procedure selector populated.
- Fictional AF/apixaban 5 mg twice daily, age65, CrCl80, elective inguinal hernia repair November10 generated the existing dated conditional calendar and no-bridge rationale with sources.
- Selecting an urgent/emergency procedure and submitting replaced that calendar with REVIEW_REQUIRED; no regimen remained.
These are software checks, not independent clinical validation or a new source review. No patient data entered.

## Changes
- Startup compares expected HTML version with the executing app version. A mismatch displays an explicit warning, instructing users to preserve reviewed de-identified work before a hard refresh; no automatic reload or storage added.
- Build validator rejects disagreement between HTML metadata, asset versions and app version.
- Public URL manifest excludes deployment controls; package excludes temporary build artifacts, while retaining required deployment configuration.
- Empty monitoring/source headings removed from unsupported decision outputs.
- Future AI/Canva studio requirements clarified in BUSINESS_EDUCATION_FUTURE.md.

## Verification
355 JavaScript tests and 9 Python tests passed. ZIP CRC, byte comparison and <100-file batching required. New startup warning and revised rendering are automated-tested, not deployed/browser-tested. Mobile, print/PDF, all-tool coverage, hosted monitoring and independent clinical validation remain open. No clinical algorithms or dose rules changed.

## Phase checkpoint
Phase09: release-consistency safeguards. Phase04: elective DOAC and urgent-context software checks. 11/13 tracks initially implemented, 0/13 fully accepted. No whole-platform completion date assigned. Next: accept consistent deployed runtime, activate missing monitoring/CI, finish mobile/print and broader clinical workflow acceptance before expansion.

## AI generation and Canva — clarified October 24
Owner intends AI to create outputs, not merely suggest topics. Inputs include permission-cleared uploaded materials, future MBA content, Zotero references/full text when accessible, PubMed/PMC and primary publications discovered through Google Scholar. Zotero/Scholar are discovery and organization layers, not automatic evidence validation. Each claim must retain primary source, publication/effective date, population/context, reuse rights and review status.

Planned flow: approved source collection → evidence extraction and claim/source map → AI-authored lesson/script → factual and rights review → Canva editable design → output QA/accessibility → owner-approved publication. Outputs include short videos, posters/infographics, presentations, audio/podcast scripts, resumes/CVs and consulting/business materials. Do not invent CV achievements. Keep clinician and patient-facing outputs distinct. Never send encounter drafts or patient information into Canva or an AI service.

Capability check of the installed Canva tools: create_design supports editable text/image layouts including presentations, posters, documents and resumes; it explicitly excludes video and whiteboards. The exposed tools can upload audio/video but upload is not generation. AI video rendering, narration/audio generation and final export therefore remain separately unverified integration capabilities. Do not equate this ChatGPT Canva connector with a public API available to every GitHub Pages visitor. Public-app OAuth/backend, licensing, quotas and cost model require a later design decision; never embed connector credentials/API secrets in the static site. Free ClinicalRx access remains required.

Canva can also create original website media and educational illustrations; keep interactive clinical forms, calculations and accessible navigation in repository code. This turn authorizes considering Canva, not replacing the working site with a Canva-hosted website. No Canva design or video has been created in this release. Materials intake remains deferred until current phases are complete, per owner preference; then start with course inventory, original notes/templates and permission-cleared examples. Six remaining courses may be added through December2027.


# ClinicalRx 0.19.4 — patient-plan readability and corrected release audit
October 24, 2026

## Correction to earlier reports
The old footer was hard-coded to 0.19.1. It was not evidence that an older app was executing. Earlier v0.19.2/0.19.3 reports overstated a runtime mismatch based on that footer. The actual cause was missed visible-label updates. The version-consistency guard remains useful, but is not evidence that a cache problem existed.

## Audit of deployed v0.19.3
- All 47 intended public files match the local v0.19.3 manifest.
- Browser HTML release metadata and application-rendered dashboard both show 0.19.3; startup mismatch warning is hidden. Footer/loading labels were stale.
- Keyboard Skip to content moves focus to main successfully.
- GitHub .github/workflows directory still returns404. Scheduled source monitoring/CI not verified installed.
- Focused audit, not all-tool clinical acceptance. Earlier workflow checks remain historical evidence.

## Implemented
- Footer/loading labels corrected to release0.19.4; build validator now checks these labels as well as metadata, asset URLs and app version.
- Patient-plan preview uses five readable numbered cards: health, plan, monitoring, follow-up and teaching. Plain text remains in an expandable view.
- Preview uses the same agreed SOAP-derived sections as the handout; pending recommendations are suppressed, text is escaped, medication quantities/negation preserved and clinician-only assessment is excluded.
- Existing completeness, review invalidation, cabinet consistency and no-PHI export safeguards retained. No storage, remote generation, clinical rule or dose changes.

## Testing
357 JavaScript tests and 9 Python tests passed. Tests cover preview escaping, pending-plan suppression and prior workflow gates. Manifest validation and ZIP CRC/byte/batch checks passed. New visual preview has not been browser-tested after deployment. Mobile/print/PDF, full keyboard audit, comprehensive clinical validation and monitoring runs remain open.

## Phase checklist
Phase00: version-label and keyboard acceptance checkpoint.
Phase06: patient-plan presentation improved; deployment visual acceptance remains required.
Phase09: integrity acceptance passed; monitoring installation blocked.
Initial capabilities 11/13; complete phase acceptance 0/13. Full platform incomplete; no defensible completion date yet.
Next: deploy and visually accept patient-plan cards; install workflows per SOURCE_MONITOR_SETUP.md; complete mobile/print and broader clinical workflow acceptance before expanding clinical rules.

## Upload
Extract the packet. Upload CONTENTS of each numbered batch at repository root, preserving paths. Commit each batch separately. Do not upload wrappers or ZIP itself. Do not delete repository. Pages remains main /docs. Each batch is below100files. Read START_HERE.txt for actual counts. No remote repository writes performed by this audit.


# ClinicalRx 0.19.5 — patient-plan readiness
Audit date: October 24, 2026

## Deployed v0.19.4 audit
All47 public files matched. Browser footer identifies0.19.4. Five numbered patient-plan cards rendered clearly in a fictional desktop case. Initial export disabled; review enabled the handout control; removing monitoring invalidated review and disabled export; restoring monitoring and reviewing again enabled it. This is control-state and visual acceptance, not a new downloaded-file or print/PDF test. Source-monitoring workflow directory still404.

## Defects fixed
The reading estimate previously counted care-team placeholder prompts, even in an empty note. It now waits for all required plan sections and excludes placeholders. A new readiness panel names missing agreed actions, monitoring, follow-up or education. Complete plans prompt review before export. Existing no-PHI/cabinet checks remain in the export handler; no patient information is transmitted or persisted.

## Tests
Full pre-final JavaScript suite:359passed. Added readiness/recovery workflow test then ran the workflow suite successfully, bringing the passing test inventory to360. Python9passed. Release manifest and packaged bytes/CRC/batch size checks passed. New readiness UI remains unverified in a deployed browser. No clinical treatment or billing rule changed.

## Phase position
Phase06 patient education: desktop card-preview acceptance completed; readiness feedback implemented. Whole Phase06 is not complete: print/mobile acceptance, bilingual/device education, teaching tools remain. Phase09 hosted monitoring/CI remains blocked on installation. Initial capabilities11/13; full track acceptance0/13. No overall completion percentage or completion date is claimed.

## Next concrete acceptance gates
1. Deploy readiness changes and verify missing-field/review prompts.
2. Install the two workflows using documentation/SOURCE_MONITOR_SETUP.md; a file under documentation alone does not activate GitHub Actions.
3. Finish mobile and print/PDF acceptance, followed by broader medication/anticoagulation/switching fixtures and independently reviewed expansion.

## Upload
Extract upload packet. Upload each numbered batch's CONTENTS to repository root, preserving folders. Commit separately. Do not upload wrapper folders or ZIP itself. All batches below100 files. Pages remains main /docs. No repository deletion required.

## Release 0.20.0 extension — October 24, 2026

Profile/repository clarity: one current README, repository-role map, four-pillar About entry points, original privacy/terms routes, root cleanup instructions preserving application paths. Added Phase 06N nutrition education pilot; scope and acceptance gates are in NUTRITION_AND_API_ROADMAP.md. No unreviewed claim of expert approval, under-two-minute completion, deficiency treatment or comprehensive interaction checks. Monetization must remain optional and independent of clinical selection; no shopping URLs carry health inputs. OpenMed/USDA are assessed candidates, not active services.

## 0.21.0 core acceptance priority

User priority: finish the original 13 tracks before expanding future-state applications. CORE_ACCEPTANCE_PLAN.md defines gates and sequencing. Phase04 now has a canonical 22-direction catalog and two bounded label-formulation references. SWITCH_DATA_REVIEW_0.21.0.md records evidence, limits and remaining normalization work. No automatic equipotence inference; clinical, API and source changes require review. Nutrition/affiliate implementation paused.

## v0.24.0 acceptance increment

Texas source directory and validated retrieval foundation delivered in Phases 02/09. Official field mapping, price normalization, deployed UI acceptance and unattended publication remain blocked/pending. See TEXAS_DATA_INTEGRATION.md and AUDIT_0.24.0.md. No additional track reaches full acceptance.

## 0.25.0 acceptance and discovery contract

The current 13-track status is maintained in PHASE_CHECKLIST.md; historical checkpoints do not define current acceptance. No future-state expansion precedes core acceptance. External calculator discovery combines local multi-word AND search with a topic filter, announces result counts, supports reset and an empty state, and links to original providers without transmitting encounter/cabinet data. Source registry dates are not live availability claims. The Texas data directory and medication-data guide are directly discoverable from the second pillar. Reduced-motion preference disables smooth page scrolling.

## 0.26.0 review-state and case-isolation contract

Loading the built-in fictional encounter must clear all preceding encounter, payer, MTP, economic-event and cabinet context. Independent practice/business drafts are not implicitly cleared. Changing patient action text in either connected workspace resets plan agreement and final review; those actions must remain withheld until agreement is renewed. Actual patient handout export remains gated by completeness, review, cabinet consistency and de-identification. Source-destination checks are separately dated from registry reviews and cannot be labeled external calculator validation. Progress counts fully accepted tracks; partial presence is not a sequential phase.
