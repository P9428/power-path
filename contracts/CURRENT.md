# CONTRACT M-PP-00 — Foundation Docs

Status: OPEN — authored 2026-08-20
Rung: M-PP-00 (first rung). Prior contract M-PP-BOOT closed 2026-08-20.
Gate status: no stophook gate blocks this contract.

## OBJECTIVE

Populate the six `/docs` stubs with what is actually known, actually
uncertain, and actually decided as of today. The centerpiece is
`ASSUMPTIONS.md` — a falsification table in which every load-bearing claim
carries a primary `source_url` and an `observed_date`, and every claim not
verified against a primary source is labelled as such rather than softened.

This contract writes documents. It writes no code, no schemas, no data.

## CONTEXT

The M-PP-BOOT research pass produced ten load-bearing findings. They exist
only as search-result summaries in a single 2026-08-20 session transcript and
in one memory file. **None have been verified against a primary source.**
That makes them INFERENCE, not FACT, and they must not enter `/docs` as FACT
until re-checked.

The findings reshaped the thesis in three ways, and M-PP-00 is where those
reshapings become canon or get rejected:

1. "Power Access Diligence" appears to have no whitespace — several funded
   competitors already sell it.
2. The surviving edge appears to be **copper, not queue position**: physical
   interconnection assets are reusable, contractual interconnection rights
   largely are not.
3. Illinois appears to have broken as the first geography, while the same
   event appears to have created the first ICP.

Each "appears to" above is the thing this contract must resolve.

## SCOPE

### Phase 1 — Verification (before any doc is written)

Re-verify these ten claims against a **primary source** — the issuing body's
own order, filing, press release, tariff, or docket. A law-firm client alert,
a trade-press article, or a search-result summary is SECONDARY and does not
promote a claim to FACT.

| # | Claim to verify | Expected primary source |
|---|---|---|
| C1 | FERC Surplus Interconnection Service is generator-to-generator; rights are tied to the original resource and terminate within one year of its retirement; SIS is not generator replacement | FERC order / PJM tariff |
| C2 | FERC found PJM's tariff unjust and unreasonable for co-located load (Dec 18 2025) and directed all six RTOs to justify or reform large-load interconnection terms (Jun 18 2026) | ferc.gov orders / news releases |
| C3 | Pritzker directed DCEO to pause Data Center Investment Program agreements effective 2026-07-01, two years, existing agreements honored | Governor's office / DCEO |
| C4 | ICC approved increased ComEd large-load deposits, $1M at 50–200 MW, +$500k per additional 100 MW | ICC order / docket |
| C5 | ComEd holds ~28 GW of large-load applications from ~75 applicants against a ~24 GW all-time peak | ComEd or ICC filing |
| C6 | Build.inc raised $8.5M led by Index Ventures; "Dougie"; 100+ projects; hyperscaler client | Build.inc / Index |
| C7 | Independent sponsor diligence spend: $25–50k light, $75–125k deeper; mid-market $150–750k | best available; likely SECONDARY only |
| C8 | ≥15 public actions restricting or rejecting data centers across ≥10 states since 2025; more in Jan–Jul 2026 than all of 2025 | tracker with a stated methodology |
| C9 | Kendall County (Yorkville) ~1,800 MW / ~1,037 ac and Will County (Joliet) ~1,800 MW / ~795 ac approvals | county board records |
| C10 | Homer City, TeraWulf Lake Mariner, Meta Forest City are genuine retired-industrial-to-data-center conversions reusing physical interconnection assets | PNNL / EPA / operator filings |

For each: record `claim`, `classification`, `source_url`, `source_tier`
(PRIMARY / SECONDARY / TERTIARY), `observed_date`, and — where the primary
source contradicts or narrows the M-PP-BOOT wording — the corrected wording.

**A claim that cannot be verified is recorded as UNKNOWN with the search
already attempted. It is not deleted, and it is not restated more weakly to
make it survive.**

### Phase 2 — Write the six documents

**`docs/THESIS.md`** — the thesis as currently believed, in plain language:
what the company is, what the first wedge is, why the component sequence was
inverted from the operator's original ordering, and the falsification
condition for the thesis as a whole.

**`docs/ASSUMPTIONS.md`** — the falsification table. Columns: assumption,
classification (SUPPORTED / PLAUSIBLE / UNKNOWN / FALSE / CONTEXT-DEPENDENT),
evidence, `source_url`, `source_tier`, `observed_date`, and **what evidence
would change this row**. The last column is mandatory on every row.

**`docs/SOURCE_OF_TRUTH.md`** — the evidence protocol, not yet a source
catalog (the catalog is M-PP-03). Must state: the source tier hierarchy;
the claim classification scheme; the required fields on every claim; the NULL
rule; the "repetition never increases confidence" rule; and the capacity
vocabulary — the explicit, non-interchangeable definitions of generation,
transmission, distribution, substation, transformer, and interconnection
capacity, plus firm vs non-firm, historical load vs deliverable load, and
physical interconnection asset vs contractual interconnection right.

**`docs/DECISION_LOG.md`** — append-only, entries `PP-001` onward, each with
date, decision, rationale, and reversal condition. Seed with the decisions
already made: the SSH-instead-of-gh ruling; the ladder title amendment;
the inverted component sequence; the ICP hypothesis; the geography finding.

**`docs/ARCHITECTURE.md`** — at this rung, primarily a **deferral list**:
what is deliberately not being built yet and which rung earns it. Must state
that the first memo (M-PP-02) is hand-written by a human, and that no schema,
store, agent, or pipeline is authorized before the rung that names it.

**`docs/ROADMAP.md`** — points at `/contracts/LADDER.md` rather than
duplicating it. Adds only: target dates, the three gate conditions, and the
kill criteria for the 30/90-day windows.

## PLAN GATE

Before writing any document, output the Phase 1 verification results as a
table: each of C1–C10 with its classification, source tier, URL, and any
correction to the M-PP-BOOT wording. Then state plainly which of the three
thesis reshapings survived.

WAIT for "approved" before writing to `/docs`.

## CONSTRAINTS

- Documents only. No code, no schemas, no data files, no dependencies.
- Do not build the prospect list — that is M-PP-01.
- Do not write the spec memo — that is M-PP-02.
- Do not build the source catalog — that is M-PP-03.
- No edits to any other repo.
- No claim enters `/docs` as FACT on the strength of a search summary.
- Do not restate a failed claim more weakly so that it survives.

## ACCEPTANCE

- All six `/docs` files no longer contain the M-PP-BOOT stub line.
- `ASSUMPTIONS.md` covers C1–C10 plus the operator's original assumptions
  A–N; every row has a classification and a change-my-mind condition.
- Every FACT-classified row cites a PRIMARY source with an `observed_date`.
- `SOURCE_OF_TRUTH.md` contains the capacity vocabulary.
- `DECISION_LOG.md` has at least PP-001 through PP-005.
- One commit "M-PP-00: foundation docs", pushed.
- This contract moved to `/contracts/closed/`.

## DONE

Print the count of claims by classification, the list of any claim that
failed verification, and the single next action.

## STOP CONDITIONS

- A load-bearing claim (C1, C3, or C5 especially) is contradicted by its
  primary source → stop, report, await ruling. Do not rewrite the thesis
  unilaterally.
- Verification would require a paid or credentialed source → stop, report
  the cost, await ruling.
- Any temptation to write code, schemas, or a source catalog → stop; out of
  scope, and it belongs to a later rung.
