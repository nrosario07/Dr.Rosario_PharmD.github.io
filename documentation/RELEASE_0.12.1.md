# 0.12.1 — medication lookup recovery only

Added independent FDA label-linked identity candidates to the automatic lookup race and a Search FDA directly button. Delays are 2.5 seconds for RxTerms and 5 seconds for FDA; immediate source failures accelerate fallback. Original public-name validation, credentials omission, no-referrer requests, source-host allowlist, stale-result guards and tab-only handling are preserved.

FDA identifiers are explicitly label-linked with unresolved strength/form, never presented as an exact RxNorm strength mapping. Warnings remain visible in results/cabinet and metadata. No source result means no selected medication. All three failures produce host-specific errors and permit retry. FDA rate-limit responses are not concealed.

241 tests passed. Forced two-host NLM failure plus a real FDA request retrieved 19 metoprolol candidates in 5.47 seconds. Existing deployed v0.12 lookup → identity → label → cabinet was browser-tested. New v0.12.1 UI and FDA mode have not yet been browser-tested after deployment. No root cause of the user's intermittent network issue was established.

Reported anticoagulation dropdown and switch-result defects remain open for the next focused fixes. No clinical dose rules changed. Full platform incomplete.
