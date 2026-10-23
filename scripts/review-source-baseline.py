"""Explicit maintainer approval of selected public-source fingerprints; no fetching or rule updates."""
import argparse
import datetime
import json
import re
from pathlib import Path


def approve(report, baseline, urls, reviewer, rationale):
    if not reviewer.strip() or not rationale.strip() or not urls:
        raise ValueError('Select URLs and provide a reviewer and review rationale.')
    indexed = {r['url']: r for r in report['sources']}
    result = dict(baseline)
    for url in urls:
        row = indexed.get(url)
        if not row or row.get('status') not in ('BASELINE_NEEDED', 'CONTENT_CHANGED_REVIEW', 'UNCHANGED'):
            raise ValueError('Source has no successful reviewable response: '+url)
        if not re.fullmatch(r'[a-f0-9]{64}', row.get('sha256', '')):
            raise ValueError('Invalid complete-body hash: '+url)
        result[url] = {key: row.get(key) for key in ('sha256', 'etag', 'lastModified', 'finalURL')}
        result[url].update(observedAt=report['checked'], reviewedAt=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                           reviewer=reviewer.strip(), rationale=rationale.strip())
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--report', type=Path, required=True)
    p.add_argument('--baseline', type=Path, default=Path('documentation/source-monitor-baseline.json'))
    p.add_argument('--url', action='append', required=True)
    p.add_argument('--reviewer', required=True)
    p.add_argument('--rationale', required=True, help='Record publication/effective dates, materiality and clinical follow-up.')
    a=p.parse_args()
    baseline=json.loads(a.baseline.read_text()) if a.baseline.exists() else {}
    result=approve(json.loads(a.report.read_text()), baseline, a.url, a.reviewer, a.rationale)
    a.baseline.parent.mkdir(parents=True, exist_ok=True)
    tmp=a.baseline.with_suffix('.json.part')
    tmp.write_text(json.dumps(result,indent=2)+'\n')
    tmp.replace(a.baseline)
    print('Selected source fingerprints approved. No clinical rules changed. Review the diff before committing.')

if __name__=='__main__':
    main()
