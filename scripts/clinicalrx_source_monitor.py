#!/usr/bin/env python3
"""Allowlisted public-source availability/hash monitor. Does not publish data."""
import argparse, hashlib, json, sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
import requests

ALLOWED={"pfs.data.cms.gov","www.cms.gov","cms.gov","purplebooksearch.fda.gov","dailymed.nlm.nih.gov","rxnav.nlm.nih.gov","clinicaltables.nlm.nih.gov","medlineplus.gov","eutils.ncbi.nlm.nih.gov","eutilities.github.io","api.fda.gov"}

def main():
    p=argparse.ArgumentParser(); p.add_argument("--registry",required=True); p.add_argument("--report",required=True); a=p.parse_args()
    registry=json.loads(Path(a.registry).read_text(encoding="utf-8")); s=requests.Session(); s.headers["User-Agent"]="ClinicalRx-SourceMonitor/1.0"
    now=datetime.now(timezone.utc).isoformat(); results=[]
    for src in registry.get("sources",[]):
        url=src.get("url",""); host=urlparse(url).hostname
        row={"source_id":src.get("id"),"url":url,"checked_at":now,"status":"FAILED","http_status":None,"sha256":None,"etag":None,"last_modified":None,"error":None,"publication_status":"NOT_PUBLISHED"}
        if src.get("type") == "live_api":
            row["status"]="SKIPPED_LIVE_API"; row["error"]="Live API is checked by a functional endpoint test, not a generic page fetch"
        elif host not in ALLOWED: row["error"]="Host is not allowlisted"
        else:
            try:
                r=s.get(url,timeout=(5,25),allow_redirects=True); row["http_status"]=r.status_code; r.raise_for_status()
                if urlparse(r.url).hostname not in ALLOWED: raise ValueError("Redirected to non-allowlisted host")
                if not r.content: raise ValueError("Empty response")
                row.update(status="CHECKED",sha256=hashlib.sha256(r.content).hexdigest(),etag=r.headers.get("ETag"),last_modified=r.headers.get("Last-Modified"))
            except Exception as e: row["error"]=f"{type(e).__name__}: {str(e)[:250]}"
        results.append(row)
    report={"report_version":"1.0.0","checked_at":now,"source_count":len(results),"checked_count":sum(x["status"]=="CHECKED" for x in results),"skipped_live_api_count":sum(x["status"]=="SKIPPED_LIVE_API" for x in results),"failed_count":sum(x["status"]=="FAILED" for x in results),"publication_note":"Availability/hash check only. No data published.","results":results}
    out=Path(a.report); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(f"Checked {report['checked_count']}/{report['source_count']}; failures={report['failed_count']}")
    return 1 if report["failed_count"] else 0

if __name__=="__main__": sys.exit(main())
