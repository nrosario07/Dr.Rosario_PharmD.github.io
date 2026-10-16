# Focused audit — October16,2026

## Deployed/source observations

GitHub docs/index.html identifies0.13.0. Retrieved cpa-workspace.js and encounter-review.js contain the MDM assistant; cpa-workspace.js does not contain “Free-text MDM level is not automatically validated.” A fresh deployed browser confirmed the MDM assistant. No mixed-version root cause was established. A stale user view remains possible, not proven.

In a fictional browser test, assessment “Hypertension stable. Diabetes at individualized goal.” and plan “Continue lisinopril10mg daily because blood pressure is at goal.” plus established status produced Moderate MDM/99214 with quoted Problems and Risk evidence. This is a component-based candidate; the test was not a complete authenticated note or billable encounter. Other note fields were incomplete. The new release flags those missing fields explicitly.

The old time-only message still said no MDM was inferred, which was misleading next to the MDM result. Reworded it to describe only time and direct users to separate MDM evidence.

The deployed MTP detector missed the fictional wording “Misses three doses each week. Copay is too high. Pharmacy is out of stock.” The new source matches these phrases with unconfirmed findings. The user screenshot confirms short switching coverage; this is an actual incomplete scope, not a missing dropdown repair.

## New implementation verification

289 automated tests pass. Added seven exact GLP-1 directions, label starting-dose assertions, next-dose dates/year-boundary calculations, refusal of unknown safety/GI/hypoglycemia contexts, unsupported doses/frequency/age/products and no automatic off-label5mg escalation. MTP tests cover ordinary wording, negation, hypothetical counseling, resolved findings and no inference from raw results. Existing privacy/API/cabinet/MDM/switch/reporting tests remain passing.

All scripts are syntax checked; release manifest validates entrypoint versions/hashes. ZIP integrity and complete extraction/source comparison are checked. These are not Windows Explorer UI tests, new-release browser tests or independent clinical validation.

## Clinical source review and boundaries

1. Novo Nordisk Inc. OZEMPIC prescribing information. Revised May2026. Accessed October16,2026. https://www.novo-pi.com/ozempic.pdf
2. Eli Lilly and Company. TRULICITY prescribing information. DailyMed. Accessed October16,2026. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=463050bd-2b1c-40f5-b3c3-0a04bb433309
3. Eli Lilly and Company. MOUNJARO prescribing information. Revised August2026. Accessed October16,2026. https://pi.lilly.com/us/mounjaro-uspi.pdf
4. Jain AB, Ali A, Gorgojo Martinez JJ, et al. Switching between GLP-1 receptor agonists in clinical practice: expert consensus and practical guidance. Int J Clin Pract. 2021;75:e13731. doi:10.1111/ijcp.13731. https://pmc.ncbi.nlm.nih.gov/articles/PMC7900946/
5. Jabbour S, Paik JS, Aleppo G, Sharma P, Gomez Valderas E, Benneyworth BD. Switching to tirzepatide5mg from glucagon-like peptide-1 receptor agonists: clinical expectations in the first12weeks of treatment. Endocr Pract. 2024;30(8):701-709. doi:10.1016/j.eprac.2024.05.005. https://pubmed.ncbi.nlm.nih.gov/38723893/

Labels define starting doses, not a universal switch/equipotence table. Expert timing is separate, and tirzepatide timing is extrapolated from earlier guidance. The Jabbour study is prospective selected-population research, not a general equivalence trial; full protocol/exclusion appraisal is not complete, so5mg is not generated as a prescription/calendar. Its abstract describes adult T2DM with prior stable GLP-1 treatment at least3months, HbA1c6.5–9% and BMI≥25. No patient eligibility is inferred from those abstract criteria alone. The tool does not cover obesity brands, oral semaglutide, compounded products, interruptions/restarts, pediatric transitions or Mounjaro as the source agent.

## Acceptance still needed after upload

Confirm0.14.0, hard refresh and test fictional cases. Switch Ozempic1mg weekly (last dose2026-10-16) to Mounjaro with required clinical facts: expect label start2.5mg weekly on2026-10-23, conditional four-week reassessment, and a distinctly labeled off-label research alternative. Active GI symptoms or unknown safety must withhold the schedule. Test Victoza daily timing independently. Verify all doses/device/source details before use.

Enter the three fictional MTP phrases above and verify unconfirmed suggestions; add negated/raw-lab statements and verify no unsupported findings. Confirm manual additions still work and no unconfirmed findings enter final note/subtotal. Test MDM and time independently; stale quoted wording should be absent after the complete upload. Verify medication page readability, keyboard navigation, narrow screens, lookup→cabinet→SOAP→patient plan and printing. New0.14 browser acceptance remains open; no full all-page audit is claimed.
