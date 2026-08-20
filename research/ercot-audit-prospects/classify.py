import json, re, collections, datetime
recs = json.load(open('docket_58481.json')) + json.load(open('docket_55999.json'))
def norm(p):
    s = re.sub(r'[.,]', ' ', p.upper())
    s = re.sub(r'\b(LLC|L L C|INC|LP|L P|CORP|CORPORATION|COMPANY|CO|LTD|HOLDINGS|USA|US)\b', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()
AGENCY = re.compile(r'PUC |PUC$|OPUC|OPDM|RULES & PROJECTS|ERCOT$|COMMISSION|STATE OF TEXAS|ATTORNEY GENERAL|COUNTY|COUNCIL OF GOVERNMENTS|PUBLIC WORKS|BUREAU OF ECONOMIC')
UTILITY = re.compile(r'ONCOR|CENTERPOINT|AEP TEXAS|TEXAS-NEW MEXICO|TNMP|LCRA|SHARYLAND|CROSS TEXAS|ELECTRIC COOPERATIVE|GOLDEN SPREAD|EL PASO ELECTRIC|SOUTHWESTERN|TEXAS ELECTRIC COOP|TRANSMISSION')
TRADE = re.compile(r'COALITION|COUNCIL|ALLIANCE|ASSOCIATION|TCPA|TPPA|TIEC|TEXAS OIL & GAS|CHAMBER|NETWORK$|DIGITAL POWER NETWORK|BLOCKCHAIN')
ADVOCACY = re.compile(r'SIERRA CLUB|ENVIRONMENT|CONSUMER|PUBLIC CITIZEN|CLEAN AIR|EARTHJUSTICE|NRDC')
ADVISOR = re.compile(r'CONSULTING|PRIORITY POWER|ADVISOR|LAW |LLP|ANALYTICS')
GENCO = re.compile(r'NRG|VISTRA|CALPINE|LUMINANT|TALEN|CONSTELLATION|ENGIE|TENASKA|EOLIAN|ENCHANTED ROCK|MONARCH|SERENA|BLACK MOUNTAIN|SATOSHI|WISE ENERGY|ENEUS|SPLIGHT|APERTURE')
DC = re.compile(r'DATA ?CENTER|DIGITAL|EDGECONNEX|SKYBOX|ROWAN|CRUSOE|LANCIUM|GOOGLE|MICROSOFT|AMAZON|META|ORACLE|CIPHER|SOLUNA|CORMINT|TESLA|RIOT|CORE SCIENTIFIC|GALAXY|TERAWULF|HUT 8|MARA|BITDEER|APPLIED DIGITAL|VANTAGE|QTS|STACK|ALIGNED|COMPASS DATA|PRIME DATA|SWITCH')
INDUSTRIAL = re.compile(r'STEEL|DOW CHEMICAL|BASF|EXXON|OCCIDENTAL|TARGA|FREEPORT|INFINIUM|CHOLLA|LNG|REFIN|PETROLEUM|CHEMICAL|AIR LIQUIDE|LINDE')
def seg(p):
    u = p.upper()
    if AGENCY.search(u): return 'AGENCY/ISO'
    if UTILITY.search(u): return 'UTILITY/TSP'
    if TRADE.search(u): return 'TRADE ASSOC'
    if ADVOCACY.search(u): return 'ADVOCACY'
    if DC.search(u): return '** DATA CENTER / DIGITAL **'
    if INDUSTRIAL.search(u): return 'INDUSTRIAL LOAD'
    if GENCO.search(u): return 'GEN / BEHIND-METER'
    if ADVISOR.search(u): return 'ADVISOR/COMPETITOR'
    return 'UNCLASSIFIED'
agg = {}
for r in recs:
    k = norm(r['party'])
    if not k: continue
    a = agg.setdefault(k, dict(names=set(), filings=0, dockets=set(), dates=[], titles=[]))
    a['names'].add(r['party']); a['filings'] += 1; a['dockets'].add(r['docket'])
    a['dates'].append(r['date']); a['titles'].append(r['title'][:90])
def d(s):
    try:
        m,dd,y = s.split('/'); return datetime.date(int(y),int(m),int(dd))
    except Exception: return datetime.date(1900,1,1)
rows=[]
for k,a in agg.items():
    disp = sorted(a['names'], key=lambda x:(x.isupper(), -len(x)))[0]
    rows.append(dict(party=disp, segment=seg(k), filings=a['filings'],
                     dockets=','.join(sorted(str(x) for x in a['dockets'])),
                     last=max(d(x) for x in a['dates']).isoformat(),
                     sample=a['titles'][0]))
rows.sort(key=lambda r:(-r['filings'], r['party']))
json.dump(rows, open('parties.json','w'), indent=1)
c=collections.Counter(r['segment'] for r in rows)
print('distinct parties across both dockets:', len(rows), '| filings:', len(recs))
print('date range:', min(d(x['date']) for x in recs).isoformat(), '->', max(d(x['date']) for x in recs).isoformat())
print()
for s,n in c.most_common(): print(f'{n:4d}  {s}')
