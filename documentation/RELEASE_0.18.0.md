# Release 0.18.0 — October 18, 2026

Adds an accessible build-progress dashboard under Sources & provenance, with a hub shortcut. Separates initial implementation (11/13 equal-weight tracks) from full documented acceptance (0/13 tracks closed). Shows all tracks, remaining work, next three steps and the monitoring installation blocker. These are milestone counts, not overall percentage complete or clinical-validity scores.

No clinical algorithms, dose mappings, payer rules or source content changed. Four pillars and privacy constraints preserved. Source-monitor workflow remains absent in the remote repository. New progress UI awaits deployed browser acceptance.

Added an always-visible official FDA fallback after deployed browser lookup returned a network/CORS/service error. This mitigates access failure; it does not claim to repair external connectivity.
