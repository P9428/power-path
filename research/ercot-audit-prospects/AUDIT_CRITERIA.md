# ERCOT Large Load Audit Exposure — Compliance Criteria

**Primary source:** PUCT Project No. 58481, Proposal for Publication, filed **2026-03-12**,
proposed new 16 TAC §25.194. Item 122.
`https://interchange.puc.texas.gov/search/documents/?controlNumber=58481&itemNumber=122`
**observed_date:** 2026-08-20

**Status classification: PROPOSED RULE, not final.** Every figure below is from the
Proposal for Publication. Do not represent any of it as adopted law. Confirm current
status before it appears in a client deliverable.

**Context:** On 2026-08-03 Gov. Abbott directed PUCT and ERCOT to conduct a
"comprehensive verification and audit of all data centers advancing through ERCOT's
interconnection process," with denial of connection as the penalty for non-compliance,
and no additional data center advancing until the audit completes. ERCOT suspended the
Batch Zero classification notices scheduled for 2026-08-07 (market notice M-A080326-01)
and sought a good-cause exception at the PUCT's 2026-08-20 open meeting regarding
ERCOT Planning Guide Sections 5 and 9.

---

## Applicability — §25.194(b)

Applies to a large load customer seeking:

1. a new interconnection **≥ 75 MW**;
2. an expanded interconnection that **reaches 75 MW for the first time**;
3. an expanded interconnection that **exceeds 75 MW by 75 MW or more**.

---

## The three audit exposure axes

### Axis 1 — Site control · §25.194(d)(1)

A large load customer must demonstrate site control through **one** of exactly three
property interests, provided to the interconnecting DSP or TSP:

| | Instrument | Binding condition |
|---|---|---|
| (A) | Signed and executed **lease** | Parcels sufficient to accommodate planned facilities, for **at least five years from the date the customer is expected to reach contracted peak demand** |
| (B) | **Deed** | Parcels sufficient to accommodate planned facilities |
| (C) | Signed and executed **option** to purchase or lease | Parcels sufficient to accommodate planned facilities |

**Why this is auditable from outside:** deeds and most long-term leases are recorded in
Texas county real property records. The instrument either exists, covers sufficient
acreage, and runs long enough — or it does not. This is the most externally verifiable
of the three axes.

**Failure modes to test:** lease term expiring before five years past expected peak
demand date; acreage insufficient for stated MW; option expired or never exercised;
instrument held by an affiliate rather than the named applicant.

### Axis 2 — Substantially similar interconnection request · §25.194(d)(2)

> "A large load customer must **disclose** to the interconnecting DSP or the
> interconnecting TSP whether the customer is pursuing a substantially similar
> interconnection request for electric service, the approval of which would result in the
> customer materially changing, delaying, or withdrawing the interconnection request."

**"Material" is defined, not judgmental:**
- a delay of **one or more years** to the projected date to reach requested/contracted peak demand; **or**
- a **20% or greater change** in requested or contracted peak demand; **or**
- a **change in the location for the point of interconnection**.

**This is the axis the audit exists to find.** ERCOT's queue reached ~474.7 GW against a
~91,089 MW all-time peak. A queue five times system peak is not five times the demand;
it is substantially duplicated requests. §25.194(d)(2) is the disclosure hook that makes
non-disclosure a compliance failure rather than a negotiating posture.

**And the rule expressly makes the analysis permissible.** §25.194(c)(2) defines
competitively sensitive information to include exact parcel identifiers, pricing, and
financing structures — but expressly **excludes**:

> "the identity of a large load customer; general site location, such as load zone;
> requested or contracted peak demand; timing of energization; **or whether an
> interconnection request is associated with the same applicant or affiliated entities.**"

Affiliation between requests is, by the rule's own definition, not competitively
sensitive. The affiliation graph is legitimately constructible.

### Axis 3 — Financial security and credit quality · §25.194(d)(9)–(10)

**Study fee** — due to the interconnecting DSP/TSP:

| Requested peak demand | Minimum study fee |
|---|---|
| ≥ 75 MW and < 250 MW | **≥ $100,000** |
| ≥ 250 MW | **≥ $300,000** |

If combined DSP/TSP/ERCOT study costs exceed the fee, the customer pays actual costs.
Commission adjusts these values every five years starting 2027, indexed to Q3 CPI.

**Financial security** — **$50,000 per MW** of requested peak demand (or of the
incremental increase, for expansions), **due at the time the intermediate agreement is
executed.**

Acceptable forms are limited to:
- cash collateral;
- corporate or parental guaranty **only if** the corporation or parent holds a credit
  rating equivalent to **BBB-/Baa3 or higher** (S&P / Moody's);
- letter of credit from a major U.S. commercial bank (or U.S. branch of a major foreign
  bank) rated at least **A-** (S&P) or **A3** (Moody's).

**This is a hard credit screen.** A developer without an investment-grade parent posts
cash or an LC. At 300 MW that is $15,000,000 in cash or LC capacity, at intermediate
agreement execution — before the interconnection study is even performed.

---

## The consequence that makes this worth paying to understand

### Withdrawal · §25.194(g)

On withdrawal of all or part of requested/contracted peak demand:

1. DSP/TSP notifies ERCOT within 14 days.
2. DSP/TSP **draws down the financial security** against outstanding amounts owed —
   costs incurred, non-refundable equipment procured, non-cancellable construction
   started, non-cancellable services initiated.
3. **Only 20% of the remaining balance is refunded** to the customer, within 60 days.
4. **The remaining 80% is paid to the interconnecting TSP and applied as an offset to
   that TSP's rate base** at its next interim or comprehensive rate proceeding.
5. **CIAC is not refundable.**
6. ERCOT reallocates the withdrawn contracted peak demand.

### Non-utilized capacity · §25.194(h)

The same drawdown is triggered **without any withdrawal**: if a customer misses a
phased-energization milestone **by six months**, the DSP/TSP must notify ERCOT within
30 days and draw down the financial security within 60 days of that notice.

**A schedule slip, not a cancellation, starts the confiscation.**

---

## Worked exposure — the number a principal will react to

200 MW project, $50,000/MW security posted at intermediate agreement:

| Line | Amount |
|---|---|
| Financial security posted | $10,000,000 |
| Study fee (≥75 <250 MW) | $100,000 |
| Assume outstanding amounts owed at withdrawal | $2,000,000 |
| Balance after drawdown | $8,000,000 |
| **Refunded to customer (20%)** | **$1,600,000** |
| **Retained to TSP rate base (80%)** | **$6,400,000** |
| **Net loss** (security + fee − refund) | **$8,500,000** |

Against that, a fixed-fee diligence engagement is a rounding error. The decision the
memo informs is not "is this a good site" — it is **"what is my downside if this project
slips six months, and does my current documentation survive an audit that can deny me
connection outright."**

---

## What is NOT established and must not be asserted

- **This rule is proposed, not final.** Verify adoption status and any changes between
  the 2026-03-12 PFP and the current text before any client use.
- The Abbott audit's actual criteria have **not** been published in detail. Mapping the
  audit to §25.194 is **INFERENCE**, not fact. The audit letter references compliance
  with PUCT, ERCOT, and state law requirements generally, and self-supply versus grid
  dependence specifically.
- ERCOT publishes **no public named large-load queue**. Membership in the audited set
  (~250–300 projects, ~200 GW per ERCOT's 2026-08-14 statement) is **UNKNOWN** for every
  party in `PROSPECTS.md`.
- Whether any named party has failed any criterion above is **UNKNOWN**. Nothing here
  supports an assertion about a specific project.
- The 2026-08-20 open meeting outcome was not checked. Do so before relying on the
  Batch Zero timeline.

## Source tier

| Item | Tier |
|---|---|
| §25.194 text, thresholds, fees, security, withdrawal, non-utilized capacity | **PRIMARY** — PUCT filing |
| Abbott directive of 2026-08-03 | SECONDARY — press + four law-firm alerts; letter itself not retrieved |
| ERCOT 474.7 GW / 420.8 GW figures | SECONDARY — Vegas testimony 2026-07-29 as reported |
| ERCOT all-time peak 91,089 MW, 2026-07-22 | **PRIMARY** — U.S. EIA |
| Audit scope ~250–300 projects / ~200 GW | SECONDARY — reported ERCOT statement to PUCT 2026-08-14 |
