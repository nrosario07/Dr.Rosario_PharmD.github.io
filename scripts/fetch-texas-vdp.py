"""Retrieve official VDP files into an isolated staging folder. Never publish prices/rules.
Network errors and HTML responses do not replace any published or last-good data.
"""
import argparse,datetime,hashlib,io,json,zipfile,urllib.request,urllib.error
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parent.parent
MAX_BYTES=80*1024*1024
class OfficialRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,headers,newurl):
  u=urlparse(newurl)
  if u.scheme!='https' or u.hostname!='www.txvendordrug.com':raise ValueError('Unexpected redirect destination')
  return super().redirect_request(req,fp,code,msg,headers,newurl)
def validate_payload(data,kind,content_type=''):
 if not data or len(data)>MAX_BYTES:raise ValueError('Empty or oversized download')
 start=data[:2048].lstrip().lower()
 if 'html' in content_type.lower() or b'<!doctype html' in start or b'<html' in start or b'access denied' in start or b'accessdenied' in start:raise ValueError('Error/HTML response is not a data file')
 if kind=='zip':
  with zipfile.ZipFile(io.BytesIO(data)) as z:
   infos=z.infolist()
   if not infos or len(infos)>100 or sum(x.file_size for x in infos)>MAX_BYTES*3:raise ValueError('Unexpected archive size')
   for x in infos:
    if x.flag_bits&1 or x.filename.startswith(('/','\\')) or '..' in x.filename.replace('\\','/').split('/'):raise ValueError('Unsafe archive member')
   if not any(x.filename.lower().endswith(('.xlsx','.xls')) for x in infos):raise ValueError('Expected Excel member missing')
   if z.testzip():raise ValueError('Archive checksum failed')
  return {'container':'ZIP','members':len(infos),'schemaVerified':False}
 if b'\x00' in data:raise ValueError('Unexpected binary text payload')
 data.decode('utf-8-sig')
 return {'container':'TEXT','lines':len(data.splitlines()),'schemaVerified':False}
def fetch(feed):
 u=urlparse(feed['url'])
 if u.scheme!='https' or u.hostname!='www.txvendordrug.com' or not u.path.startswith('/sites/default/files/docs/data--'):raise ValueError('Source URL outside allowlist')
 req=urllib.request.Request(feed['url'],headers={'User-Agent':'ClinicalRx-PublicDataMonitor/0.24 (public data retrieval)'})
 with urllib.request.build_opener(OfficialRedirect()).open(req,timeout=30) as response:
  data=response.read(MAX_BYTES+1)
  details=validate_payload(data,feed['format'],response.headers.get('Content-Type',''))
  return data,{**details,'lastModified':response.headers.get('Last-Modified'),'etag':response.headers.get('ETag'),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
def run(out,feeds,retrieve=fetch):
 out=Path(out);out.mkdir(parents=True,exist_ok=True);records=[];blocked=False
 for feed in feeds:
  record={'id':feed['id'],'source':feed['url'],'checkedAt':datetime.datetime.now(datetime.timezone.utc).isoformat()}
  if blocked:record.update(status='NOT_ATTEMPTED_ORIGIN_ACCESS_FAILURE')
  else:
   try:
    data,meta=retrieve(feed);suffix='.zip' if feed['format']=='zip' else '.txt';name=feed['id']+'-'+meta['sha256']+suffix
    (out/name).write_bytes(data);record.update(meta,status='DOWNLOADED_SCHEMA_REVIEW_REQUIRED',stagedFile=name)
   except urllib.error.HTTPError as exc:
    record.update(status='UNAVAILABLE',httpStatus=exc.code)
    if exc.code in (401,403,429):blocked=True
   except Exception as exc:record.update(status='REJECTED_OR_UNAVAILABLE',errorType=type(exc).__name__)
  records.append(record)
 report={'checkedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'publishesSiteData':False,'records':records}
 (out/'report.json').write_text(json.dumps(report,indent=2)+'\n')
 return report
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',default='/tmp/clinicalrx-texas-vdp');a=p.parse_args()
 feeds=json.loads((ROOT/'documentation/texas-vdp-sources.json').read_text())['feeds'];r=run(a.output,feeds)
 print(json.dumps({x['id']:x['status'] for x in r['records']},indent=2))
 raise SystemExit(0 if all(x['status']=='DOWNLOADED_SCHEMA_REVIEW_REQUIRED' for x in r['records']) else 1)
