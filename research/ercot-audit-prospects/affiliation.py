#!/usr/bin/env python3
"""Affiliation graph over Texas Comptroller franchise-tax entity records.

Purpose: surface applicant families whose members hold separate interconnection
positions. 16 TAC 25.194(d)(2) requires a large load customer to disclose a
"substantially similar interconnection request" whose approval would materially
change, delay, or withdraw the request. 25.194(c)(2) expressly states that
"whether an interconnection request is associated with the same applicant or
affiliated entities" is NOT competitively sensitive -- so this analysis is
permitted by the rule it serves.

Edges are epistemically typed. They are not interchangeable:

  OFFICER   shared officer/director name          STRONG   forms clusters
  ADDRESS   shared mailing street                 STRONG   forms clusters
  AGENT     shared non-commercial registered agent  WEAK   recorded, never links
  VENDOR    address is the entity's own commercial
            registered agent's office            SUPPRESSED

The VENDOR rule is not defensive coding, it is a verified correction. Crusoe
Technologies LLC, Crusoe DC Equipment Holdco LLC, Satoshi Energy Holding
Company LLC and Eolian Metals, LLC -- three separately-filing PUCT parties --
all list 211 E 7TH ST STE 620, Austin. That is the office of Corporation
Service Company, their common registered agent. Linking on it would have
asserted an affiliation that does not exist.

Stdlib only. Input: tx_entities.json from tx_entities.py.
"""
import json
import re
import itertools
import collections

COMMERCIAL_AGENTS = re.compile(
    r'CT CORPORATION|C T CORP|CORPORATION SERVICE|CSC|VCORP|COGENCY|'
    r'REGISTERED AGENTS? INC|NATIONAL REGISTERED|INCORP|LEGALINC|'
    r'NORTHWEST REGISTERED|UNITED STATES CORPORATION|CAPITOL CORPORATE|'
    r'PARACORP|HARVARD BUSINESS|BIZFILINGS|WOLTERS', re.I)

_SUFFIX = re.compile(r'\b(STE|SUITE|UNIT|APT|FLOOR|FL|RM|ROOM|NO|#)\b.*$')
_ABBREV = [('EAST', 'E'), ('WEST', 'W'), ('NORTH', 'N'), ('SOUTH', 'S'),
           ('STREET', 'ST'), ('AVENUE', 'AVE'), ('DRIVE', 'DR'),
           ('BOULEVARD', 'BLVD'), ('ROAD', 'RD'), ('CIRCLE', 'CIR'),
           ('PARKWAY', 'PKWY'), ('HIGHWAY', 'HWY'), ('LANE', 'LN'),
           ('COURT', 'CT'), ('PLACE', 'PL')]


def norm_addr(rec, prefix):
    """Canonicalize a street address.

    Abbreviation collapse is mandatory, not cosmetic: one CSC office appears as
    '211 E 7TH ST STE 620', '211 E. 7TH STREET, SUITE 620' and
    '211 EAST 7TH STREET, SUITE 620' across three records in this corpus.
    """
    s = (rec.get(prefix + 'Street') or '').upper()
    s = re.sub(r'[^A-Z0-9 ]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    s = _SUFFIX.sub('', s)
    for long, short in _ABBREV:
        s = re.sub(r'\b' + long + r'\b', short, s)
    return re.sub(r'\s+', ' ', s).strip()


def norm_person(name):
    s = re.sub(r'[^A-Z ]', ' ', (name or '').upper())
    return re.sub(r'\s+', ' ', s).strip()


def is_vendor_address(rec):
    """True when the mailing address is the entity's own commercial agent's office."""
    if not COMMERCIAL_AGENTS.search(rec.get('registeredAgentName') or ''):
        return False
    mail = norm_addr(rec, 'mailingAddress')
    office = norm_addr(rec, 'registeredOfficeAddress')
    return bool(mail) and mail == office


def build(ents, max_share=25):
    officers = collections.defaultdict(set)
    addrs = collections.defaultdict(set)
    agents = collections.defaultdict(set)
    vendor = []

    for tid, rec in ents.items():
        for off in (rec.get('officerInfo') or []):
            person = norm_person(off.get('AGNT_NM'))
            if len(person.split()) >= 2:
                officers[person].add(tid)
        addr = norm_addr(rec, 'mailingAddress')
        if addr and len(addr) > 6:
            if is_vendor_address(rec):
                vendor.append((tid, rec.get('name', ''), addr))
            else:
                addrs[addr].add(tid)
        agent = (rec.get('registeredAgentName') or '').strip().upper()
        if agent and not COMMERCIAL_AGENTS.search(agent):
            agents[agent].add(tid)

    edges = collections.defaultdict(list)

    def link(kind, key, tids):
        # max_share guards against a shared key so common it carries no information
        if not 1 < len(tids) <= max_share:
            return
        for a, b in itertools.combinations(sorted(tids), 2):
            edges[(a, b)].append((kind, key))

    for k, v in officers.items():
        link('OFFICER', k, v)
    for k, v in addrs.items():
        link('ADDRESS', k, v)
    for k, v in agents.items():
        link('AGENT', k, v)

    # union-find over STRONG edges only -- WEAK edges never form a cluster
    parent = {t: t for t in ents}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for (a, b), ev in edges.items():
        if any(k in ('OFFICER', 'ADDRESS') for k, _ in ev):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

    groups = collections.defaultdict(list)
    for t in ents:
        groups[find(t)].append(t)
    clusters = sorted((g for g in groups.values() if len(g) > 1), key=len, reverse=True)
    return edges, clusters, vendor


def main():
    ents = json.load(open('tx_entities.json'))
    edges, clusters, vendor = build(ents)
    strong = sum(1 for ev in edges.values()
                 if any(k in ('OFFICER', 'ADDRESS') for k, _ in ev))

    print(f"entities {len(ents)} | strong edges {strong} | clusters {len(clusters)} "
          f"| vendor-address suppressions {len(vendor)}\n")
    if vendor:
        print("SUPPRESSED (mailing address == own commercial agent's office):")
        for _, name, addr in sorted(vendor, key=lambda x: x[1]):
            print(f"   {name[:44]:46s} {addr}")
        print()

    for c in clusters:
        names = sorted(ents[t]['name'] for t in c)
        ev = collections.Counter(
            k for a, b in itertools.combinations(sorted(c), 2)
            for k, _ in edges.get((a, b), []))
        print(f"--- {len(c)} entities | {dict(ev)}")
        for n in names:
            print(f"      {n}")
        print()

    json.dump({'clusters': [[ents[t]['name'] for t in c] for c in clusters],
               'vendor_suppressed': [v[1] for v in vendor]},
              open('affiliation.json', 'w'), indent=1)


if __name__ == '__main__':
    main()
