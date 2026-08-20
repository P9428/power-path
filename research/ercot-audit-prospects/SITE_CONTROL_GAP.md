# Site Control Layer — access findings

**Attempted:** 2026-08-20. Goal: verify §25.194(d)(1) site control for the three
Lancium West Texas locations (Abilene / Taylor Co., Childress / Childress Co.,
Fort Stockton / Pecos Co.) against public property records.

**Result: NOT VERIFIED.** No site-control instrument was confirmed or refuted for any
parcel. This file records what was tried, what it costs, and what the failure means.

---

## A methodology correction, recorded because it nearly became a finding

The first parcel query returned a 172-byte response. The parser read it as
`parcels: 0` and it was briefly treated as "Lancium owns no Texas land."

It was an **error object**, not an empty result set:

```json
{"error":{"code":400,"extendedCode":-2147220222,
 "message":"Requested operation is not supported by this service.",
 "details":["The requested capability is not supported."]}}
```

An empty result and a failed query are different states and must never share a code
path. "Lancium owns no land in Taylor County" and "the server refused the question" are
opposite findings, and only one of them is about Lancium.

**Rule for the evidence protocol (belongs in `SOURCE_OF_TRUTH.md` at M-PP-00):**
before recording any negative result, prove the query executed. A zero is a claim about
the world; an error is a claim about the pipeline. Absence of evidence is not evidence
of absence — including when the absence is produced by your own broken request.

This is the second null-that-was-a-failure in two work sessions. It gets a rule, not a
mental note.

---

## What is freely reachable, and what is not

| Layer | Source | Status | Cost |
|---|---|---|---|
| Regulatory filings, party names | PUCT Interchange dockets | **WORKS** — full docket parse | free |
| Rule text, thresholds, fees | PUCT filing PDFs | **WORKS** | free |
| Entity identity, officers, agents, SOS file | TX Comptroller franchise-tax JSON API | **WORKS** | free |
| Contact blocks | filing PDFs via `pdftotext` | **WORKS** | free |
| **Parcel ownership / acreage / legal description** | TxGIO StratMap, county CADs | **BLOCKED** | see below |

### What was tried on the parcel layer

**1. TxGIO StratMap statewide parcels — ArcGIS REST**
`feature.geographic.texas.gov/arcgis/rest/services/Parcels/stratmap_land_parcels_48_most_recent/MapServer/0`

Layer metadata is public and confirms the schema carries exactly the needed fields:
`owner_name`, `legal_area`, `gis_area`, `legal_desc`, `mkt_value`, `situs_addr`,
`mail_addr`, `date_acq`, `fips`. Declared capabilities are `Query,Map`.

**Every query returns HTTP 200 with a 400 error body** — including `where=1=1`.
`returnCountOnly` and `returnDistinctValues` are likewise unsupported. Metadata is open;
the query endpoint is gated. Alternate service names (`stratmap25_land_parcels_48`,
`.../FeatureServer/0`) return "Service not found" or a server object error.

**2. County appraisal districts**
Taylor CAD (`esearch.taylor-cad.org`) and Pecos CAD (`pecoscad.org`) both run the
Pritchard & Abbott *eSearch* platform. Direct result URLs return **"Your search session
has expired"**; there is no `__RequestVerificationToken` in the page and a form POST
returns 411. The platform requires an interactive browser session.

### What that leaves

- **TxGIO DataHub bulk download** — shapefile / geodatabase, license cost listed as
  **None**. Statewide, so large, and needs GIS tooling. TxGIO states data is received
  from appraisal districts **as-is**: coverage varies by county, and missing fields mean
  the county did not share them. **Whether Taylor, Childress, and Pecos are present, and
  whether `owner_name` is populated for them, is UNKNOWN and is the next thing to check.**
- **Manual CAD lookup** — free, interactive, roughly one parcel at a time.
- **Commercial parcel data** — TexasFile, TaxNetUSA, Regrid, LightBox, ATTOM. Not
  priced here; pricing was not requested and is not guessed.

---

## Why this is a moat finding, not just an obstacle

Three of four layers in this stack are free and now automated: who filed, who they are
corporately, and what the rule requires. Anyone can rebuild those in a day.

**The site-control layer is where free public data stops.** It is also the layer
§25.194(d)(1) actually turns on — a lease running five years past expected peak demand,
a deed, or an option, covering acreage sufficient for the stated MW. That instrument is
recorded, and confirming it requires either paid data or per-parcel manual work.

That cost is the barrier to entry. If parcel ownership were a free API, the audit-
readiness memo would be a commodity by Friday. It is not, so the question becomes
whether the layer is worth buying — a pricing decision, not a research one, and one
that belongs in the unit-economics work rather than here.

---

## Explicitly NOT established

- Whether any Lancium entity holds any Texas parcel. **UNKNOWN.**
- Whether any prospect satisfies or fails §25.194(d)(1). **UNKNOWN.**
- Whether the three Lancium SPV counties appear in StratMap at all. **UNKNOWN.**
- Fee ownership is only one of three acceptable instruments. Even a complete parcel
  dataset showing no ownership would **not** establish absence of site control, because
  a lease or an option satisfies the rule and neither reliably appears in an appraisal
  roll. A parcel search can confirm site control; it cannot refute it.

## Next check, in order

1. Pull the TxGIO DataHub bulk parcel file and test whether FIPS 48441 / 48075 / 48371
   are present with populated `owner_name`. Free, and settles the coverage question.
2. If covered: query offline for the prospect entity families from
   `AFFILIATION_FINDINGS.md`.
3. If not covered: manual CAD lookup for the three Lancium counties, and price the
   commercial alternatives before committing to any.
