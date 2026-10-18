# Audit — October 17, 2026

Repository manifest reports 0.16.0. Before edits, all 40 recorded public-file hashes matched the fetched manifest. Seven current source/documentation files were restored from GitHub. The browser displays 0.16.0 and all four pillars.

Browser tested this run: SOAP + Professional practice filter produced an explicit empty result; reset restored the directory; Find a medicine navigated to the engine. Metformin lookup returned 134 RxNorm identities. Product labels for metformin 500mg oral tablet were retrieved and a selected product appeared in the cabinet. The later SOAP navigation did not establish retained cabinet-to-note data; full cross-workspace acceptance remains unverified. This is targeted testing, not all-page/all-workflow acceptance.

346 automated Node tests pass, including existing clinical boundary fixtures and new resource filters, aliases, reset, safe empty states, shortage query privacy, 404-vs-error distinction, output escaping and asynchronous stale-result protection. Tests use deterministic fixtures/event-DOM harness and do not establish clinical validity or browser layout correctness. Manifest and full ZIP extraction are checked during packaging.

New UI/live shortage browser acceptance and mobile/keyboard regression remain pending. Local preview is unavailable under the Sites environment workflow; no alternate preview server was started. Independent clinical/coding review remains pending. No code was published remotely.

Monitoring: GitHub content query for .github/workflows/source-monitor.yml returned 404 again. Included workflow installation instructions; installed/running status cannot be claimed. The monitor compares source hashes and queues human review, not automatic clinical updates.
