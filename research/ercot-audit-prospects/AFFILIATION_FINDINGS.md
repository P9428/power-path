# Affiliation Graph — Findings

**Built:** 2026-08-20
**Source:** Texas Comptroller Franchise Tax Account Status public API,
`https://comptroller.texas.gov/data-search/franchise-tax`
**Tier:** PRIMARY (state agency, public data)
**Corpus:** 152 entity records retrieved from 30 prospect-name queries.

## Why this analysis is permitted

16 TAC §25.194(d)(2) requires a large load customer to disclose a *substantially
similar interconnection request* whose approval would materially change, delay, or
withdraw its request — material meaning ≥1 year delay, ≥20% MW change, or a change in
point-of-interconnection location.

§25.194(c)(2) expressly excludes from "competitively sensitive information":

> "the identity of a large load customer; general site location, such as load zone;
> requested or contracted peak demand; timing of energization; **or whether an
> interconnection request is associated with the same applicant or affiliated
> entities.**"

The rule states that affiliation between requests is not confidential. This analysis
uses only that non-sensitive class, from a public state API.

## What the API returns

Per entity: legal name, DBA, FEI number, mailing address, right-to-transact-in-Texas
status, state of formation, SOS registration status and file number, effective SOS
registration date, registered agent name and office, and an `officerInfo` array of
officer/director names, titles, and addresses.

Endpoints: `?name=<QUERY>` for search (prefix match at word boundary),
`/<taxpayerId>` for the full record.

---

## Finding 1 — the false positive, and why it matters most

The first run produced this cluster and called it an affiliation:

```
CRUSOE DC EQUIPMENT HOLDCO LLC
CRUSOE TECHNOLOGIES LLC
EOLIAN METALS, LLC
SATOSHI ENERGY HOLDING COMPANY LLC     evidence: ADDRESS x6
```

Three separately-filing PUCT parties appearing to share a mailing address is exactly
the §25.194(d)(2) signal the product exists to find. **It is wrong.**

All four list `211 E 7TH ST STE 620, AUSTIN 78701`. That is the office of **Corporation
Service Company**, their common registered agent. The address is a vendor's, not a
place of business.

Two corrections went into the algorithm:

1. **Vendor-address suppression.** A mailing address equal to the entity's own
   commercial registered agent's office is suppressed and never forms a link. Seven
   suppressions in this corpus: the four above, plus Black Mountain Power Wash LLC,
   Hut 8 Infrastructure LLC, and Soluna Development LLC.
2. **Address normalization.** The same CSC office appears three ways in the corpus —
   `211 E 7TH ST STE 620`, `211 E. 7TH STREET, SUITE 620`, and
   `211 EAST 7TH STREET, SUITE 620`. Without USPS-style abbreviation collapse the
   suppression rule silently fails to fire.

Edges are typed and are not interchangeable:

| Type | Meaning | Use |
|---|---|---|
| OFFICER | shared officer/director name | STRONG — forms clusters |
| ADDRESS | shared mailing street | STRONG — forms clusters |
| AGENT | shared *non-commercial* registered agent | WEAK — recorded, never links |
| VENDOR | address is own commercial agent's office | SUPPRESSED |

**A shared commercial registered agent is not evidence of anything.** CT Corporation
and CSC serve tens of thousands of unrelated entities. Counting those edges would have
produced a memo asserting a relationship between Crusoe and Satoshi Energy that does not
exist — the precise failure mode the buyer is paying to avoid.

## Finding 2 — Lancium: one officer group, three West Texas sites

Ten entities, 85 shared-officer edges, all at `9002 SIX PINES DR # 134, SHENANDOAH`,
all Delaware-formed, all ACTIVE:

| Entity | SOS file | Effective | Officers |
|---|---|---|---|
| LANCIUM ABILENE II, LLC | 0804512315 | 03/21/2022 | Jennifer Kennedy, Michael McNamara |
| LANCIUM ABILENE REAL ESTATE, LLC | 0804512311 | 03/21/2022 | Jennifer Kennedy, Michael McNamara |
| LANCIUM CHILDRESS, LLC | 0804512310 | 03/21/2022 | Jennifer Kennedy, Michael McNamara |
| LANCIUM FORT STOCKTON, LLC | 0804512309 | 03/21/2022 | Jennifer Kennedy, Michael McNamara |
| LANCIUM FS 25, LLC | 0804487738 | 03/04/2022 | Jennifer Kennedy, Michael McNamara |
| LANCIUM POWER LLC | 0804569693 | 05/03/2022 | Jennifer Kennedy, Michael McNamara |
| LANCIUM QSE I, LLC | 0804712069 | 08/31/2022 | Jennifer Kennedy, Michael McNamara |
| LANCIUM, INC. | 0804698570 | 08/15/2022 | Ali Fenn, Brittany Doyle, Jason Marshall |
| LANCIUM LLC | 0802996561 | 04/23/2018 | Jason Marshall, Jennifer Kennedy, Keith Sigale |
| LANCIUM TECHNOLOGIES CORPORATION | NOT REGISTERED | — | Michael McNamara |

Four consecutive SOS file numbers (…309, …310, …311, …315) filed the same day name
three distinct West Texas locations: **Abilene** (Taylor Co.), **Childress**
(Childress Co.), **Fort Stockton** (Pecos Co.).

Lancium filed at PUCT jointly with Google LLC (4 filings in 58481) and, in one filing,
with TotalEnergies Renewables USA.

**What this is:** a site-specific SPV structure under one officer group across multiple
counties — the structural shape a substantially-similar-request analysis is looking for.

**What this is NOT, and must not be asserted:** evidence that Lancium holds multiple
interconnection requests, that any request is undisclosed, or that any §25.194(d)(2)
obligation was breached. Separate SPVs per site is ordinary and prudent project finance.
The affiliation is FACT; any inference about queue behavior is **UNKNOWN** and is not
supportable from this corpus.

## Finding 3 — five PUCT filers with no matching Texas entity

A name query returned **zero** Texas franchise-tax entities beginning with the filed
name for: **Tract** (and "Tract Holding"), **Provident**, **Rowan Digital**,
**Thor Equities**, **IREN**.

Match semantics were tested, not assumed: the API matches a prefix at word boundary
(`TRACTOR` → 148 hits; `TRACT` → 0; `ROWAN` → 191; `ROWAN DIGITAL` → 0).

**Classification: UNKNOWN, not FALSE.** These parties may be registered under a
different legal name, may hold Texas positions through an affiliate, or may not be
Texas-registered. The search is recorded rather than converted into a conclusion.

It is a question worth resolving because §25.194(d)(1) requires site control evidenced
by a lease, deed, or option — held by someone. If the filing entity has no Texas
presence, the instrument sits with an affiliate, and identifying that affiliate is the
same analysis as Finding 2. Resolving it requires a Texas Secretary of State check,
which is not free and was not performed.

## Other clusters found

| Family | Entities | Note |
|---|---|---|
| Crow Holdings | 11 | Fund/GP/realty-partner stack, `3819 MAPLE AVE` Dallas |
| CCNG | 10 | Real-estate GP/LP stack |
| EdgeConneX | 10 | Metro-named holdcos: Dallas, Houston, Austin property, fiber |
| Trammell Crow | 4 + 3 | Two separate clusters |
| DC Energy | 3 | DAKOTA, SOUTHWEST, TEXAS — multi-state SPVs |
| STACK Infrastructure | 3 | III TRC, USA, Inc. |
| Crusoe | 3 | Data Center Operations, Digital Infrastructure SPV, Energy Holdings |
| Enchanted Rock | 3 | Capital, Management, Reliability Services |

## Limits — read before using any of this

- **Name-match noise is present and was not fully cleaned.** The 152 records include
  unrelated companies that merely share a prospect's name — `CRUSOE ENTERPRISES, INC.`
  (San Antonio), `CRUSOE CHEEKS MEDIA GROUP LLC`, `INFINIUM SOFTWARE, INC.` have no
  established relationship to the PUCT filers. Clusters must be name-verified before
  use.
- Each name query was capped at 12 results, so large families are truncated.
- Officer data is as-reported to the Comptroller for the stated report year (2025 for
  most records) and may be stale.
- **No county real-property records were checked.** Site control under §25.194(d)(1)
  is a recorded instrument; nothing here verifies one exists, covers sufficient
  acreage, or runs long enough.
- **No link to ERCOT queue position exists.** ERCOT publishes no named large-load
  queue. Whether any entity here is among the ~250–300 audited projects is **UNKNOWN**.
- Nothing here establishes that any party failed any §25.194 criterion.

## Reproduce

```
python tx_entities.py qnames.json    # collect, cached, polite delay
python affiliation.py                # graph + typed edges + suppressions
```
