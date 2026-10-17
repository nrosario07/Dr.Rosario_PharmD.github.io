# Focused audit — October 17, 2026

## Browser-tested deployed version
The public site and GitHub entrypoint remain0.14.0. On #reporting, checking report review but leaving the no-PHI review unchecked and pressing Download reviewed MTP CSV displays both “Local CSV created” and “Confirm the no-PHI review before downloading.” This is a verified misleading-success defect; code returns before creating a Blob. Tested with zero records and no patient data.

## Local correction
Download returns true only after browser dispatch, false when privacy-blocked or on exception. Reporting distinguishes those outcomes and does not claim a file was saved. Changing export options invalidates review and clears stale success. The existing no-PHI gate remains required. Includes the unpublished0.14.1 task hub, section navigation, compact clinical styling and conditional switch controls.

## Verification boundaries
295 automated Node tests pass, including blocked export without a Blob, successful dispatch, option-change invalidation and dispatch failure. These are event-capable DOM-harness tests, not browser rendering tests. Syntax and release manifest checked during packaging. ZIP CRC and extracted bytes checked separately.

New0.14.2 UI/export behavior is not yet browser-tested on a deployed version. Mobile, print, all-page visual regression, independent clinical/coding review and broad natural-language MTP validation remain open. No clinical algorithms changed. GitHub write previously returned403 Resource not accessible by integration; no deployment claim is made. Do not broaden permissions automatically or bypass the denial through browser writes.
