"""Read-only public deployment integrity check; never sends encounter information."""
import argparse, concurrent.futures, hashlib, json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

def compare(expected, actual):
    return 'MATCH' if hashlib.sha256(actual).hexdigest()==expected else 'MISMATCH'

def check(base, manifest, fetch):
    def one(item):
        path, expected=item
        if path.startswith('/') or '..' in path.split('/') or ':' in path:
            return {'path':path,'status':'INVALID_PATH'}
        try:
            data=fetch(base.rstrip('/')+'/'+path)
            return {'path':path,'status':compare(expected,data)}
        except Exception as exc:
            return {'path':path,'status':'UNREACHABLE','error':str(exc)}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        rows=list(pool.map(one,manifest['sha256'].items()))
    return {'version':manifest['version'],'checkedAt':datetime.now(timezone.utc).isoformat(),'base':base,'passed':all(r['status']=='MATCH' for r in rows),'files':rows,'limits':'Byte integrity only. Does not certify clinical accuracy, API availability, browser behavior or source monitoring.'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--base',default='https://nrosario07.github.io');p.add_argument('--manifest',type=Path,default=Path(__file__).resolve().parents[1]/'docs/data/release-manifest.json');p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if not a.base.startswith('https://'):p.error('Use a public HTTPS site')
    def fetch(url):
        with urlopen(Request(url,headers={'User-Agent':'ClinicalRx-release-integrity/1.0','Cache-Control':'no-cache'}),timeout=25) as response:return response.read()
    result=check(a.base,json.loads(a.manifest.read_text()),fetch)
    a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(f"{sum(x['status']=='MATCH' for x in result['files'])}/{len(result['files'])} public files match release {result['version']}")
    raise SystemExit(0 if result['passed'] else 1)
if __name__=='__main__':main()
