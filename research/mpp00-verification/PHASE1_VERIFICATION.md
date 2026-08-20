# M-PP-00 Phase 1 — Verification of C1–C10

**Run:** 2026-08-20. **Status:** worksheet, uncommitted, PLAN GATE not yet cleared.
Nothing here has been written to `/docs`. `/docs` remains at the M-PP-BOOT stub line.

Tier rule applied: PRIMARY = the issuing body's own order, filing, tariff, docket
document, or press release. A docket filing by a party is PRIMARY as to what that
party asserted, and inherits the tier of what it cites. Law-firm alerts and trade
press are SECONDARY. Aggregators and forum posts are TERTIARY.

---

## Results

| # | Classification | Tier | Primary source | Observed |
|---|---|---|---|---|
| C1 | SUPPORTED, sharpened | PRIMARY | PJM OATT surplus-interconnection redline (pjm.com) | 2026-08-20 |
| C2a | SUPPORTED | SECONDARY | PJM's own summary deck of the 2025-12-18 order; ferc.gov 403 | 2026-08-20 |
| C2b | SUPPORTED | PRIMARY | ferc.gov E-7→E-12 SCO deck, Dkt EL26-67-000 et al. | 2026-08-20 |
| C3 | SUPPORTED, narrowed | PRIMARY | Governor's newsroom, 2026-06-05 | 2026-08-20 |
| C4 | SUPPORTED, corrected | PRIMARY (docket) | ICC Dkt 25-0677/25-0679 (consol.) | 2026-08-20 |
| C5a | SUPPORTED, corrected | PRIMARY (cited) | ComEd Ex. 1.0, Leichtmann direct, p.6 | 2026-08-20 |
| C5b | **UNKNOWN** | — | no current-vintage source found | 2026-08-20 |
| C6 | **PARTLY FALSE** | PRIMARY (company) | build.inc | 2026-08-20 |
| C7 | PLAUSIBLE | TERTIARY | Axial forum; McGuireWoods survey adjacent | 2026-08-20 |
| C8 | **CONTEXT-DEPENDENT** | SECONDARY | dcmap.us vs. Moratorium Nation — disagree 35x | 2026-08-20 |
| C9 | SUPPORTED, **venue corrected** | SECONDARY | Shaw Local / Farmers Weekly on council votes | 2026-08-20 |
| C10 | **SPLIT: 2 of 3** | mixed | HCR, TeraWulf, NC DEQ Brownfields | 2026-08-20 |

Counts: SUPPORTED 7 · UNKNOWN 1 · PARTLY FALSE 1 · CONTEXT-DEPENDENT 1 · PLAUSIBLE 1
(C2 and C5 each split into two rows; C10 splits three ways and is scored as one
FALSE component inside a SUPPORTED claim.)

---

## Corrections that change the wording

**C1 — the one-year clock, verbatim.**

> "b. Limited Operation. A Generating Facility receiving Surplus Interconnection
> Service may continue to receive Surplus Interconnection Service for a period not
> to exceed one (1) year after the existing Generating Facility's Deactivation Date
> under the following conditions: i. The surplus generating unit must have been
> studied by the Transmission Provider for the sole operation at the Point of
> Interconnection; and ii. The owner of the existing Generating Facility must agree
> in writing that the Surplus Interconnection Customer may continue to operate..."

Four corrections to the M-PP-BOOT wording:

1. The clock runs from the **Deactivation Date**, not from "retirement" loosely.
2. The one-year continuation is **conditional**, not automatic — it requires prior
   sole-operation study and the incumbent's written agreement.
3. The recipient must be **a Generating Facility**. This is the load-bearing point:
   a data center is load and cannot take Surplus Interconnection Service at all.
   "Generator-to-generator" is correct but understates it.
4. Not affiliate-restricted: the incumbent or an affiliate has priority, but an
   unaffiliated third party may take it with written permission.

**C2b — a live deadline nobody has looked at.**
FERC issued six FPA §206 show cause orders on 2026-06-18, Dockets EL26-67-000
(PJM), EL26-68-000 (SPP), EL26-70-000 (MISO), EL26-71-000 (CAISO), plus NYISO and
ISO-NE. Preliminary finding: the tariffs "appear to be unjust and unreasonable
because they do not adequately address the challenges associated with the
integration of large and co-located loads." Response deadline: **60 days** —
i.e. approximately **2026-08-17, three days ago.** A 30-day resource-adequacy
informational report was also required. Six RTO responses either just landed or
are landing. This is the freshest primary-source surface in the whole claim set
and it is unexamined.

**C3 — the two-year figure is not in the directive.**
The 2026-06-05 release states the directive and that "Existing incentive
agreements under the Data Center Investment Program, including those entered into
with DCEO before July 1, 2026, will be honored." It does **not** state a duration.
The two-year figure traces to the February 2026 budget address *proposal*. Do not
cite the directive for a two-year pause. Applicants had until 2026-07-01 to
finalize an agreement.

**C4 — the deposit formula's base.**
ICC order 2026-03-19, Dkt 25-0677/25-0679 (consol.). Deposit = $1,000,000 plus
$500,000 for each additional whole 100 MW of maximum known demand **above 200 MW**.
Deposits at or over $2,000,000 require an Acceptable Letter of Credit from a U.S.
financial institution. The BOOT wording "+$500k per additional 100 MW" omitted the
200 MW base and is arithmetically wrong below it.

**C5a — projects, not applicants.**
Constellation's application for rehearing, citing ComEd Ex. 1.0 (Leichtmann direct,
p.6): "more than 75 large load projects totaling over 28,000 MW of maximum demand
are in the pipeline." Same filing: Cluster 1's eleven LDPACs, at average load,
"could account for a max load of over 9200 MW" in a single cluster. **Projects is
not applicants** — one applicant can hold several.

**C5b — the denominator is UNKNOWN.**
The only peak figure found is 23,753 MW, in an undated CBS Chicago item describing
a record that topped 23,618 MW set 2006-08-01 — vintage most likely ~2011. Whether
it is still the all-time peak in 2026 is unverified. **The "1.2x all-time peak"
comparison must not be used until the denominator is sourced.** Search attempted:
ComEd/Exelon peak-demand records, EIA, PJM load forecast. Not found.

**C6 — three of four components fail or shift.**

- $8.5M seed led by Index Ventures: SUPPORTED, dated 2026-06-30. Pebblebed, Puzzle
  Ventures and Tiny Supercomputer also participated.
- "Dougie": SUPPORTED, but it is **the platform**, not a project or an agent —
  "Build's AI platform, Dougie, automates mission-critical CRE workflows including
  site selection, desktop due diligence, underwriting, investment committee memos..."
- "100+ projects": **FALSE as stated.** Company site claims "completed over 250
  projects in 17 countries."
- "hyperscaler client": **UNKNOWN.** Named on site: Tishman Speyer, Stack
  Infrastructure, UK Government. No hyperscaler named. One testimonial mentions the
  speaker's personal AWS background — that is not a client relationship.

**C7 — do not price off this.**
$25–50k light / $75–125k deeper traces to an Axial forum post. TERTIARY. The
$150–750k mid-market figure was not corroborated at all. The nearest credible
adjacent source is the McGuireWoods Independent Sponsor Deal Survey (>75% of
surveyed deals at $10–75M enterprise value). Sell-side QoE alone runs $25–50k.

**C8 — the trackers disagree by a factor of 35.**

- dcmap.us: 15 documented actions, 10 states, since 2025. Methodology stated:
  "records documented formal public actions only: council and board votes, enacted
  zoning ordinances, adopted moratoriums, and filed or passed state bills and
  regulatory rules," excluding "proposals with no formal action taken, rumors, and
  opinion pieces." Split: 3 in 2025, 12 in Jan–Jul 2026.
- Moratorium Nation: 533 moratoria, 42 states, 59 enacted 2025, 294 in the first
  seven months of 2026.

Both are non-governmental. The **direction** — more in Jan–Jul 2026 than in all of
2025 — is SUPPORTED by both and is the only part of C8 that should be relied on.
The absolute count is a definitional artifact. Two trackers is not two sources for
one number; it is one number each, and they conflict.

**C9 — the venue is municipal, not county. This breaks a stated method.**

- Yorkville **City Council** approved Project Cardinal — 1,037 acres, up to ~1,800 MW
  at full build-out, 14 buildings / 17M sq ft — at 12:51 a.m. on **2026-03-11**.
- Joliet **City Council** voted 8-1 on **2026-03-19** for conditional annexation of
  ~795 acres for the Joliet Technology Center, up to 1.8 GW, 24 two-story buildings;
  rezoned A-1 agricultural to I-1 light industrial.
- Also: Yorkville approved Project Steel (540 acres) on 2026-03-24. ~3,016 acres in
  Yorkville are now slated for data centers along the ComEd transmission line off
  Eldamain Road.
- **Live:** Joliet Residents For Responsible Growth filed suit 2026-05-18 in Will
  County claiming the rezoning is unconstitutional and that the city violated state
  law in the approval process. **Hearing set 2026-09-08.**

M-PP-01's stated method — "county rezoning dockets" — points at the wrong record
system. These are municipal annexation agreements, PUD ordinances, and city council
minutes. County boards are not where this lives.

**C10 — one of the three exemplars does not belong.**

- **Homer City:** SUPPORTED as site-and-interconnection reuse. 3,200-acre former
  1,884 MW coal site, decommissioned 2023-07-01, interconnections to both PJM
  (FirstEnergy Pennsylvania Electric) and NYISO. **But** HCR/Kiewit announced
  2025-04-02 up to **4.5 GW of new gas generation** on the site. The generation is
  new build. What is reused is the site, the switchyard, and the interconnection
  position — which is exactly the copper claim, but it must not be described as
  reusing the retired unit's capacity.
- **TeraWulf Lake Mariner:** SUPPORTED. 180 acres leased from the ~1,800-acre former
  Somerset/Kintigh coal campus, dual 345 kV transmission, NYISO Zone A.
- **Meta Forest City:** **FALSE as bundled.** This is a **brownfield** conversion —
  140 acres previously Burlington Industries textile (1970s–90s) then Tracker Marine
  boat manufacturing (2000s), vacant from 2008, redeveloped under a 2012 NC
  Brownfields Agreement. No retired power plant. No interconnection asset reused.
  It is a contaminated-land story, not a copper story, and including it inflated the
  apparent evidence for the thesis.

---

## The three reshapings

**1. "Power Access Diligence has no whitespace." — NOT ESTABLISHED.**
Build.inc is real, funded, and larger than the BOOT note said (250+ projects, not
100+). But its named customers are CRE and colo — Tishman Speyer, Stack
Infrastructure, the UK Government — and its product is *desktop* diligence
automation at speed ("cut due diligence timelines by more than 95%"). No hyperscaler
client is named. That is a competitor in an adjacent lane, not proof the lane is
closed. Downgrade from "no whitespace" to "at least one funded incumbent, adjacent
positioning, overlap unmeasured."

**2. "Copper, not queue position." — SURVIVES, and is now sharper than when written.**
This is the one that got stronger under primary sources. The PJM tariff says a
Generating Facility receiving Surplus Interconnection Service may hold it for no more
than one year past the incumbent's Deactivation Date, conditionally, and the
recipient must itself be a Generating Facility. A data center cannot inherit those
rights at all. Meanwhile Homer City and Lake Mariner both show the physical
assets — 345 kV lines, switchyard, site, dual-RTO position — carrying real value
across the ownership change. Rights evaporate on a one-year fuse; copper stays in
the ground. That is now a sourced claim rather than an intuition.

**3. "Illinois broke as the first geography; the same event created the first ICP."
— SURVIVES WITH A MATERIAL CORRECTION.**
What broke is the **tax incentive**, not siting. DCIP processing paused 2026-07-01;
ICC imposed real deposit exposure 2026-03-19; ComEd's pipeline is >75 projects and
>28,000 MW. But siting did not stop — Yorkville approved 1,037 and 540 acres in
March 2026, Joliet approved 795 acres, ~3,016 acres are slated in Yorkville alone.
The correct statement is that Illinois removed the subsidy and raised the deposit
while approvals continued and litigation began. That is a harder, more specific
environment than "Illinois broke," and it is a better one for an adversarial
diligence product.

---

## Search failures, recorded rather than deleted

- `ferc.gov/news-events/news/fact-sheet-ferc-directs-nations-largest-grid-operator...`
  returned **HTTP 403**. C2a rests on PJM's own summary deck and on law-firm alerts.
  Re-pull the 2025-12-18 order from FERC eLibrary before any FACT classification.
- ICC Dkt 25-0677 order text itself not retrieved; the deposit formula above comes
  from a party's rehearing application and from press. Pull the order.
- ComEd's own 2026-01-06 release (businesswire) failed twice — ECONNRESET, then
  60s timeout. C5a's underlying testimony was reached by another route.
- ComEd all-time peak: not found at current vintage. C5b left UNKNOWN.
