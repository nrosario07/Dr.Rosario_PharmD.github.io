"""Summarize public source monitoring; changed bytes are not a clinical-change decision."""
import collections
import html
import json
import os
from pathlib import Path

def summary(report):
    counts=collections.Counter(row['status'] for row in report['sources'])
    lines=['# ClinicalRx source review queue', '', 'Observed: '+report['checked'], '',
           'No clinical recommendations, dosing rules, patient data or contracts changed.',
           'A changed hash may be cosmetic. Verify publication/effective dates and whether guidance is final, proposed or withdrawn.', '',
           '| Status | Sources |', '|---|---|']
    lines += [f'| {status} | {count} |' for status,count in sorted(counts.items())]
    lines += ['', '## Sources requiring human review', '']
    for row in report['sources']:
        if row['status']!='UNCHANGED':
            safe=html.escape(row['url']).replace('|','%7C').replace('\n','')
            lines.append('- '+row['status']+': '+safe)
    if all(row['status']=='UNCHANGED' for row in report['sources']):
        lines.append('No byte changes detected in checked sources. This does not prove clinical currency.')
    lines += ['', 'Baseline approval is manual and per URL; use scripts/review-source-baseline.py only after inspecting the controlling source.']
    return '\n'.join(lines)+'\n'

if __name__=='__main__':
    report=json.loads(Path('source-monitor-report.json').read_text())
    text=summary(report)
    Path('source-monitor-summary.md').write_text(text)
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'],'a') as target: target.write(text)
    print('Source review summary written.')
