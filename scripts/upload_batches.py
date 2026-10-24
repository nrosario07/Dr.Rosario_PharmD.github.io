"""Deterministic upload groups preserving every repository-relative path."""
def make_batches(paths, limit=90):
    paths=sorted(paths)
    if len(paths)!=len(set(paths)):raise ValueError('Duplicate input paths')
    if not 1<=limit<100:raise ValueError('Limit must be below 100')
    if any(p.startswith('/') or '..' in p.split('/') for p in paths):raise ValueError('Unsafe path')
    site=[p for p in paths if p.startswith('docs/')]
    if len(site)>limit:raise ValueError('Site exceeds one upload batch; use git deployment')
    if 'docs/index.html' not in site:raise ValueError('Missing site entrypoint')
    groups={'01_SITE':site}
    support=[p for p in paths if not p.startswith('docs/')]
    for start in range(0,len(support),limit):groups[f'{len(groups)+1:02d}_SUPPORT']=support[start:start+limit]
    return groups
