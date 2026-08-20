#!/usr/bin/env python3
"""Collect Texas Comptroller franchise-tax entity records for prospect names.

Source: https://comptroller.texas.gov/data-search/franchise-tax
  ?name=<QUERY>            -> [{name, taxpayerId, mailingAddressZip}]
  /<taxpayerId>            -> full record incl. registeredAgentName + officerInfo[]
Public data. Read-only. Polite delay between calls. Caches to disk.
"""
import json, os, time, urllib.request, urllib.parse, sys

BASE = "https://comptroller.texas.gov/data-search/franchise-tax"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"
CACHE = "tx_cache"
os.makedirs(CACHE, exist_ok=True)


def get(url, key):
    p = os.path.join(CACHE, key + ".json")
    if os.path.exists(p):
        return json.load(open(p))
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.loads(r.read().decode("utf-8", "replace"))
    except Exception as e:
        d = {"success": False, "error": str(e)}
    json.dump(d, open(p, "w"))
    time.sleep(0.35)
    return d


def search(name):
    return get(f"{BASE}?name={urllib.parse.quote(name)}", "s_" + "".join(c if c.isalnum() else "_" for c in name)[:60])


def detail(tid):
    return get(f"{BASE}/{tid}", "d_" + tid)


if __name__ == "__main__":
    queries = json.load(open(sys.argv[1]))
    out = {}
    for q in queries:
        s = search(q)
        hits = s.get("data") or []
        print(f"{q:38s} -> {len(hits)} hit(s)")
        for h in hits[:12]:
            tid = h["taxpayerId"]
            if tid in out:
                continue
            d = detail(tid).get("data")
            if d:
                out[tid] = d
    json.dump(out, open("tx_entities.json", "w"), indent=1)
    print(f"\nentity records collected: {len(out)}")
