import re, html, sys, json, csv
def parse(path, docket):
    h = open(path, encoding='utf-8', errors='replace').read()
    rows = re.findall(r'<tr>\s*<td>\s*<strong>\s*<a href="/search/documents/\?controlNumber=\d+&amp;itemNumber=(\d+)">\d+</a>\s*</strong>\s*</td>\s*<td>\s*([^<]*?)\s*</td>\s*<td>\s*([^<]*?)\s*</td>\s*<td>\s*([^<]*?)\s*</td>\s*<td>\s*(.*?)\s*</td>\s*</tr>', h, re.S)
    out=[]
    for item, date, party, dtype, title in rows:
        out.append(dict(docket=docket, item=int(item), date=date.strip(),
                        party=html.unescape(party).strip(),
                        doctype=html.unescape(dtype).strip(),
                        title=re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>','',title))).strip()))
    return out
recs = parse(sys.argv[1], sys.argv[2])
print(f"filings parsed: {len(recs)}")
json.dump(recs, open(f'docket_{sys.argv[2]}.json','w'), indent=1)
