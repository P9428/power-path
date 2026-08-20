# ERCOT Audit Exposure — Named Prospect List

**Built:** 2026-08-20
**Source:** PUC of Texas Interchange, dockets **58481** (rulemaking to implement large
load interconnection standards, 16 TAC §25.194) and **55999** (ERCOT large load
interconnection process).
**Method:** every filing in both dockets parsed from the public filings index; parties
deduplicated and segmented; contact blocks extracted from filing PDFs via `pdftotext`.
Scripts in this directory reproduce the whole thing from the two source URLs.

- `https://interchange.puc.texas.gov/search/filings/?UtilityType=A&ControlNumber=58481&ItemMatch=Equal&DocumentType=ALL&SortOrder=Ascending`
- `https://interchange.puc.texas.gov/search/filings/?UtilityType=A&ControlNumber=55999&ItemMatch=Equal&DocumentType=ALL&SortOrder=Ascending`

**Corpus:** 475 filings, 2023-12-15 → 2026-08-20 (both dockets are live; the most
recent filing is dated the day this list was built). 135 distinct parties.

## Why these are the prospects

Every party below chose to spend money on counsel or staff time to comment on the rule
that sets their own interconnection exposure. Under §25.194 as proposed (2026-03-12)
that exposure is a **$100,000 flat screening study fee plus $50,000/MW non-refundable**,
a 5-year operational requirement, and site control demonstrable to PUCT standard. At
200 MW that is $10M non-refundable.

On **2026-08-03** Gov. Abbott directed PUCT and ERCOT to audit every data center project
advancing through interconnection, with denial of connection as the penalty for
non-compliance. ERCOT suspended Batch Zero classification notices scheduled for
2026-08-07 and sought a good-cause exception at the PUCT's **2026-08-20** open meeting.

These parties are self-identified, named, contactable, and have eight-figure exposure
to a compliance review that is live right now.

## Segments (135 parties)

| Segment | Count |
|---|---|
| **Data center / digital infrastructure** | **29** |
| Utility / TSP | 26 |
| Generation / behind-the-meter | 26 |
| Agency / ISO / legislative | 16 |
| Trade association | 13 |
| Individual / other | 11 |
| Industrial load | 10 |
| Advisor / competitor | 2 |
| Advocacy | 2 |

## Tier 1 — named principal, direct contact, no procurement committee

Ranked by fit to the ICP: decision-maker reachable directly, company small enough that
a $7,500 engagement needs one signature, and exposure large enough to care.

| Party | Contact | Title | Email | Phone |
|---|---|---|---|---|
| Skybox Datacenters LLC | Haynes Strader | Chief Development Officer | haynes@skyboxdatacenters.com | — |
| Soluna Digital | John Belizaire | CEO | john@soluna.io | 516-216-9257 |
| Cormint Data Systems | Jamie (CEO) | CEO | JAMIE@CORMINT.COM | 203-536-7863 |
| Cipher Digital | Lee Bratcher | Head of Government Affairs | lee.bratcher@cipherdigital.com | (512) 963-5250 |
| Tract / Tract Holding Company I | Orijit Ghoshal | Vice President | Orijit.ghoshal@tract.com | 303-276-7950 |
| DC Energy Texas, LLC | Cockrell | General Counsel | cockrell@dc-energy.com | 703.506.3901 |
| Provident, Inc. | J. Hawes | President / Managing | jhawes@provident.net | (214) 215-1203 |
| Leaptran, Inc. | Tyler Xu | Product Lead | tyler@leaptran.com | — |
| CCNG, Inc. | Daniel Porter II | — | daniel.porter.ii@ccng-ing.com | — |
| Crow Holdings | K. McMeans | — | Kmcmeans@crowholdings.com | 214-922-8406 |

## Tier 2 — reachable only through outside counsel

Gated, slower, but the counsel relationship is itself a channel.

| Party | Counsel | Contact |
|---|---|---|
| Crusoe Energy Systems / Crusoe Technologies | Husch Blackwell | Carrie.CollierBrown@huschblackwell.com, Holly.Heinrich@huschblackwell.com, (512) 703-5723 |
| Hut 8 Corp | Troutman Pepper Locke | casey.bell@troutman.com, emily.meier@troutman.com, (512) 305-4731 |

## Tier 3 — named in docket, contact not yet extracted

Filed in 58481/55999 but the signature block did not yield a direct address on the
filings pulled. Each has additional filings not yet fetched.

Rowan Digital Infrastructure LLC (3 filings) · EdgeConneX (2) · STACK Infrastructure ·
CloudHQ LLC · Thor Equities LLC · Trammell Crow Company · Agentic Infrastructure LLC ·
IREN · Google LLC + Lancium LLC (4) · Lancium LLC · Tesla, Inc. (2) · Engine 1 ·
Data Center 3 Way Rd. · Soluna Digital · Provident Inc.

## Competitive intelligence from the same corpus

Two incumbent advisors are filing in this docket — they are already selling into this
buyer set and are the realistic competition for an audit-readiness engagement:

- **Schaper Energy Consulting LLC** — 6 filings across both dockets
- **Priority Power Management, LLC** — 1 filing

Neither is Build.inc, Paces, LandGate, Enverus, or Acres. **None of the funded
AI site-selection companies appear anywhere in either docket.** They sell site
discovery to developers; they are not in the compliance proceeding.

## Provenance

Every row traces to a filing item with a stable URL of the form
`https://interchange.puc.texas.gov/search/documents/?controlNumber={docket}&itemNumber={item}`.
Per-contact `source_url` and `observed_date` are in `contacts.json`.

`observed_date` for the entire dataset: **2026-08-20**.

## Known gaps — do not treat this list as complete

- **ERCOT publishes no public named large-load queue.** This list is a proxy built from
  who commented on the rule, not the audited project set. The ~250–300 projects under
  audit are NOT publicly enumerated. Overlap between this list and the audited set is
  **UNKNOWN**.
- Filing in a docket proves regulatory attention, not that the party has a project in
  Batch Zero. Do not assert queue position for any party here.
- Contact blocks were extracted from one filing per party. Parties with multiple filings
  may have better contacts in the others.
- 11 parties classified "individual/other" were not investigated.
- Name extraction is heuristic; verify a name before using it in a message.
