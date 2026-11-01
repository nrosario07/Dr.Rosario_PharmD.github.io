# Source Governance

Every source-backed record must identify:
- source organization and exact source URL;
- title and subject;
- publication, update and effective dates where available;
- retrieval date/time;
- version, identifier and checksum for snapshots;
- license/terms and redistribution decision;
- transformation steps and schema version;
- evidence limitations and applicable population;
- reviewer and approval status.

## Guideline update banner
The six-month banner must be calculated from verified publication/update metadata and a documented timezone/date policy. It must not infer freshness from retrieval date.

## Automated source workflow maturity
Stage 0: link registry only.
Stage 1: availability/hash monitoring, report only.
Stage 2: source-specific retrieval to a quarantined artifact.
Stage 3: schema, provenance, licensing and change validation.
Stage 4: human review and approval.
Stage 5: publish validated snapshot and display provenance.

Do not label a workflow "auto-refresh" until it reaches Stage 5 and a successful run is verified.
