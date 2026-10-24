# Release 0.21.0 — core switch coverage and data consistency

- Audited deployed 0.20.0: all 48 public files match; README release updated; About/four pillars inspected.
- Browser-tested fictional metoprolol 50 mg BID → 100 mg ER daily, edited to 25 mg BID → stale result cleared → regenerated 50 mg ER daily. Software behavior only.
- Centralized 22 directional switch pairs for source/target controls and visible coverage; initial target list no longer lists unrelated products.
- Added bounded carvedilol IR → COREG CR and glipizide IR → GLUCOTROL XL label references, with explicit risk/age/formulation checks and source limitations.
- Clear product-specific review when current product changes.
- Restored core-13-track priority; future nutrition/commerce/AI-studio expansion deferred.

Verification: 395 JavaScript tests and 9 Python tests passed. Site manifest and upload archive verified by packaging. New 0.21.0 UI has automated simulated-DOM coverage, not deployed browser acceptance. No full clinical, mobile, print/PDF or entire-platform acceptance claimed. GitHub workflows remain absent (404); remote repository not modified.
