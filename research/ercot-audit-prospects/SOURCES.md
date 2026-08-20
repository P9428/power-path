# Source provenance — ERCOT audit exposure research

| Artifact | Source URL | Tier | observed_date |
|---|---|---|---|
| `sources_25194_PFP_2026-03-12.txt` | https://interchange.puc.texas.gov/Documents/58481_122_1600475.PDF | PRIMARY | 2026-08-20 |
| `docket_58481.json` | https://interchange.puc.texas.gov/search/filings/?UtilityType=A&ControlNumber=58481&ItemMatch=Equal&DocumentType=ALL&SortOrder=Ascending | PRIMARY | 2026-08-20 |
| `docket_55999.json` | https://interchange.puc.texas.gov/search/filings/?UtilityType=A&ControlNumber=55999&ItemMatch=Equal&DocumentType=ALL&SortOrder=Ascending | PRIMARY | 2026-08-20 |
| `contacts.json` | per-record `source_url` field | PRIMARY | 2026-08-20 |

Retrieval note: `interchange.puc.texas.gov` returns HTTP 402 through the WebFetch proxy.
Direct `curl` with a browser user-agent returns HTTP 200. Scripts in this directory
reproduce every dataset from the URLs above.

NULL stays NULL: `exposure.py` requires `--costs-incurred` rather than defaulting it,
because the rule supplies no value and inventing one would fabricate the headline number.
