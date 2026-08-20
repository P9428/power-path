import re, json, glob, os
recs = {(r['docket'], r['item']): r for r in json.load(open('docket_58481.json'))+json.load(open('docket_55999.json'))}
EMAIL = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
PHONE = re.compile(r'\(?\b\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}\b')
TITLE = re.compile(r'\b(Chief [A-Z]\w+ Officer|C[EOTFR]O|VP|Vice President|President|General Counsel|Counsel|Director|Head of|Managing|Partner|Principal|Manager|Attorney|Founder|Sr\.? Director|Senior Director|EVP|SVP)\b', re.I)
out = []
for t in sorted(glob.glob('pdfs/item_*.txt')):
    m = re.match(r'item_(\d+)_(\d+)\.txt', os.path.basename(t))
    if not m: continue
    key = (int(m.group(1)), int(m.group(2)))
    rec = recs.get(key, {})
    txt = open(t, encoding='utf-8', errors='replace').read()
    tail = txt[-4000:]
    emails = [e for e in dict.fromkeys(EMAIL.findall(tail)) if not e.lower().endswith(('.gov',))]
    if not emails:
        emails = [e for e in dict.fromkeys(EMAIL.findall(txt)) if not e.lower().endswith(('.gov',))]
    phones = list(dict.fromkeys(PHONE.findall(tail)))
    titles = list(dict.fromkeys(x.strip() for x in TITLE.findall(tail)))
    names = []
    for e in emails[:3]:
        idx = tail.find(e)
        window = tail[max(0, idx-320):idx]
        for nm in re.findall(r'\b([A-Z][a-z]+(?:\s+[A-Z]\.)?\s+[A-Z][a-z]+(?:-[A-Z][a-z]+)?)\b', window):
            if nm.split()[0] not in ('Public','Texas','Project','Attorney','General','Commission','Suite','Austin','Dallas','Houston','North','South','New','United','Energy','Data','Center','Large','Load','Chief','Vice'):
                names.append(nm)
    out.append(dict(docket=key[0], item=key[1], party=rec.get('party',''), date=rec.get('date',''),
                    title_of_filing=rec.get('title','')[:80],
                    contact_names=list(dict.fromkeys(names))[:3], titles=titles[:3],
                    emails=emails[:3], phones=phones[:2]))
out = [o for o in out if o['emails']]
json.dump(out, open('contacts.json','w'), indent=1)
print(f"filings with contact data: {len(out)} of 33\n")
for o in out:
    print(f"{o['party']}  [{o['docket']}-{o['item']} {o['date']}]")
    if o['contact_names']: print(f"   name : {', '.join(o['contact_names'])}")
    if o['titles']:        print(f"   title: {', '.join(o['titles'])}")
    print(f"   email: {', '.join(o['emails'])}")
    if o['phones']:        print(f"   phone: {', '.join(o['phones'])}")
    print()
