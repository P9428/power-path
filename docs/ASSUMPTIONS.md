# ASSUMPTIONS — the falsification table

Written by M-PP-00, 2026-08-20. Verification worksheet with full quotes and
recorded search failures: `research/mpp00-verification/PHASE1_VERIFICATION.md`.

Classification scheme, tier hierarchy, and the mandatory-fields rule are defined
in `SOURCE_OF_TRUTH.md`. Every row below carries a change condition. A row
without one is not permitted in this file.

All rows observed **2026-08-20** unless stated otherwise.

---

## Part 1 — C1–C10, the M-PP-BOOT findings

These entered the repository as search-result summaries in a single session
transcript. None had been checked. All ten were re-run against primary sources
before this file was written. **Seven survived, one is unknown, one is partly
false, one is definition-dependent, and one was found to be three claims of
which two hold.**

---

### C1 — Surplus Interconnection Service mechanics

**SUPPORTED, and sharper than originally stated.** · PRIMARY · [PJM OATT surplus-interconnection tariff revisions](https://www.pjm.com/-/media/DotCom/committees-groups/committees/mc/2024/20241121/20241121-item-04a---3-surplus-interconnection-service-tariff-revisions-redline.pdf)

Tariff text, verbatim: *"A Generating Facility receiving Surplus Interconnection
Service may continue to receive Surplus Interconnection Service for a period not
to exceed one (1) year after the existing Generating Facility's Deactivation Date
under the following conditions: i. The surplus generating unit must have been
studied by the Transmission Provider for the sole operation at the Point of
Interconnection; and ii. The owner of the existing Generating Facility must agree
in writing..."*

Four corrections to the M-PP-BOOT wording:

1. The clock runs from **Deactivation Date**, not "retirement" loosely.
2. Continuation is **conditional**, not automatic.
3. **The recipient must be a Generating Facility.** Load cannot take SIS at all.
   This is stronger than "generator-to-generator" and is the single most useful
   sentence in this file.
4. **Not affiliate-restricted.** The incumbent or an affiliate holds priority;
   an unaffiliated third party may take it with written permission.

**Changes this row:** PJM tariff amendment altering the one-year limit, the
conditions, or the class of eligible recipient; a FERC order directing such a
change; or evidence that another RTO's tariff differs materially — **this row is
PJM-specific and has not been checked against MISO, SPP, CAISO, NYISO or
ISO-NE.**

---

### C2a — FERC's PJM co-located load order, 2025-12-18

**SUPPORTED.** · **SECONDARY only** · [PJM's own summary of the order](https://www.pjm.com/-/media/DotCom/committees-groups/workshops/cllsco/2026/20260109/20260109-item-02---summary-of-december-18-co-located-load-order---presentation.pdf)

FERC declared core portions of the PJM tariff unjust and unreasonable for failing
to address rates, terms and conditions for large loads co-located with
grid-connected generation, and directed expedited compliance filings (reported
as 2026-01-17 and 2026-02-16) creating new transmission services.

**Tier caveat, recorded rather than hidden:** ferc.gov returned **HTTP 403** on
the fact sheet. This row rests on PJM's characterization plus law-firm alerts —
and per `SOURCE_OF_TRUTH.md` §5, five alerts describing one order are one source.

**Changes this row:** pulling the order itself from FERC eLibrary (which would
promote it to PRIMARY, or contradict it); rehearing or judicial reversal;
PJM's compliance filings being rejected.

---

### C2b — Six FPA §206 show cause orders, 2026-06-18

**SUPPORTED.** · PRIMARY · [FERC, Items E-7 through E-12](https://www.ferc.gov/sites/default/files/2026-06/E-7%20to%20E-12%20SCO%20Presentation%20-%20June%20CM.pdf)

Six orders, one per RTO/ISO — PJM (EL26-67-000), SPP (EL26-68-000), MISO
(EL26-70-000), CAISO (EL26-71-000), plus NYISO and ISO-NE. Preliminary finding
that the tariffs *"appear to be unjust and unreasonable because they do not
adequately address the challenges associated with the integration of large and
co-located loads onto the transmission system,"* across five reform categories.
RTOs and transmission owners were directed to respond **within 60 days**, to file
a resource-adequacy informational report within 30 days, and were permitted to
request abeyance within 45 days.

**Live and unexamined:** 60 days from 2026-06-18 is approximately **2026-08-17 —
three days before this file was written.** Six RTO responses have just landed or
are landing. This is the freshest primary surface in the entire claim set and no
one has read it.

**Changes this row:** the actual responses (which may moot or redirect the
proceedings); abeyance grants; settlement; §205 filings that resolve FERC's
concerns before the §206 proceedings conclude.

---

### C3 — Illinois DCIP pause

**SUPPORTED, narrowed.** · PRIMARY · [Office of the Governor, 2026-06-05](https://gov-pritzker-newsroom.prezly.com/gov-pritzker-pauses-new-data-center-tax-incentives)

The Governor directed DCEO to pause processing Data Center Investment Program
agreements beginning **2026-07-01**. Verbatim: *"Existing incentive agreements
under the Data Center Investment Program, including those entered into with DCEO
before July 1, 2026, will be honored."* Applicants without an agreement had until
2026-07-01 to finalize one.

**Correction:** the release does **not** state a duration. The widely repeated
"two-year" figure traces to a February 2026 budget-address *proposal*, not to
this directive. **Citing the directive for a two-year pause is a factual error
and this repository will not make it.**

**Changes this row:** DCEO guidance or a subsequent executive action stating a
duration; legislative action restoring or replacing the program; the pause
lapsing or being lifted.

---

### C4 — ICC large-load deposit order

**SUPPORTED, formula corrected.** · PRIMARY (docket) · [ICC Docket 25-0677/25-0679 (consol.)](https://icc.illinois.gov/docket/P2025-0677/documents/379387/files/665477.pdf)

Order dated **2026-03-19**. Deposit equals **$1,000,000 plus $500,000 for each
additional whole 100 MW of maximum known demand above 200 MW**. Deposits at or
over $2,000,000 require an Acceptable Letter of Credit from a U.S. financial
institution. Deposits are refundable, applied to development cost on projects
that proceed, and returned on cancellation net of ComEd's incurred costs.

**Correction:** the M-PP-BOOT wording "+$500k per additional 100 MW" omitted the
**200 MW base** and is arithmetically wrong below it.

**Tier caveat:** the order text itself was not retrieved. The formula above comes
from a party's rehearing application in the docket plus press. Pull the order.

**Changes this row:** the rehearing (Constellation has applied, on jurisdictional
grounds among others); the ICC's follow-on investigation into large-load cost
risk; a compliance filing that alters the tariff language.

---

### C5a — ComEd large-load pipeline

**SUPPORTED, corrected.** · PRIMARY (cited) · ComEd Ex. 1.0, Direct Testimony of
Max Leichtmann, p.6, ICC Dkt 25-0677/25-0679, as quoted in Constellation's
[application for rehearing](https://icc.illinois.gov/docket/P2025-0677/documents/379387/files/665477.pdf)

Verbatim: *"more than 75 large load projects totaling over 28,000 MW of maximum
demand are in the pipeline."* Same filing: Cluster 1's eleven LDPACs, at average
load, *"could account for a max load of over 9200 MW."*

**Correction: projects, not applicants.** One applicant may hold several. The
M-PP-BOOT wording "~75 applicants" is not what the testimony says.

**Changes this row:** later ComEd testimony or compliance reporting with updated
cluster figures; large-scale withdrawal after the deposit tariff took effect —
which is precisely what the deposit was designed to cause and is worth watching.

---

### C5b — ComEd all-time peak demand

**UNKNOWN.** · no tier · not found

The only figure located is 23,753 MW, in an undated CBS Chicago item describing a
record that surpassed 23,618 MW set 2006-08-01 — vintage most plausibly ~2011.
Whether it remains the all-time peak in 2026 is unverified.

**Consequence, and it matters:** the comparison "28 GW of applications against a
~24 GW all-time peak" — the most rhetorically effective number in the entire
thesis — **rests on an unsourced denominator and may not be used** until the
denominator is sourced.

Searches attempted: ComEd/Exelon peak-demand records, EIA, PJM load forecast.

**Changes this row:** a ComEd, Exelon, PJM or EIA publication stating current
system peak.

---

### C6 — Build.inc

**PARTLY FALSE.** · PRIMARY (company site) · [build.inc](https://build.inc)

| Component | Verdict |
|---|---|
| $8.5M seed led by Index Ventures | SUPPORTED — announced 2026-06-30; Pebblebed, Puzzle Ventures, Tiny Supercomputer also participated |
| "Dougie" | SUPPORTED, reframed — it is **the AI platform**, not an agent or project |
| "100+ projects" | **FALSE as stated** — the company claims *"completed over 250 projects in 17 countries"* |
| "hyperscaler client" | **UNKNOWN** — named clients are Tishman Speyer, Stack Infrastructure, UK Government. No hyperscaler named. A testimonial mentions the speaker's own prior AWS work; that is a résumé, not a client |

**Changes this row:** Build.inc announcing a hyperscaler or utility client;
a later raise; a product move from desktop diligence into adversarial or
site-specific work, which would make it a direct rather than adjacent competitor.

---

### C7 — Independent sponsor diligence spend

**PLAUSIBLE.** · **TERTIARY** · Axial forum; [McGuireWoods Independent Sponsor Survey](https://media.mcguirewoods.com/publications/2022/Independent-Sponsor-Survey-May2022.pdf) as adjacent

$25–50k for search-phase and light diligence, $75–125k further along, traces to
an Axial forum post. The $150–750k mid-market figure was **not corroborated at
all**. Nearest credible adjacent data: >75% of surveyed independent-sponsor deals
involved targets at $10–75M enterprise value; sell-side quality-of-earnings alone
runs $25–50k.

**Do not price off this row.** Pricing is M-PP-10 and must be set from what
actual buyers say, not from a forum post.

**Changes this row:** a survey with stated methodology; or — far better — three
real quoted prices from the M-PP-07 outreach.

---

### C8 — Public actions restricting data centers

**CONTEXT-DEPENDENT.** · SECONDARY · two trackers, disagreeing by ~35×

| Tracker | Count | States | 2025 | Jan–Jul 2026 |
|---|---|---|---|---|
| [dcmap.us](https://dcmap.us/insights/policy/) | 15 | 10 | 3 | 12 |
| [Moratorium Nation](https://mjbommar.github.io/moratorium-data-2026/index.html) | 533 | 42 | 59 | 294 |

dcmap's stated methodology: *"records documented formal public actions only:
council and board votes, enacted zoning ordinances, adopted moratoriums, and
filed or passed state bills and regulatory rules,"* excluding *"proposals with no
formal action taken, rumors, and opinion pieces."*

Neither is governmental. Per `SOURCE_OF_TRUTH.md` §5 this is **not** two sources
for one number — it is two definitions, and the gap between them is a finding
about definitional instability, not about the world.

**Only the direction is usable: more restriction activity in Jan–Jul 2026 than in
all of 2025, on both counts.** The absolute number is not usable at all.

**Changes this row:** a governmental or academic count with published inclusion
criteria; or reconciling the two methodologies directly.

---

### C9 — Kendall and Will County approvals

**SUPPORTED as to facts. The venue in the M-PP-BOOT wording is WRONG, and that
error is methodological.** · SECONDARY

- **Yorkville City Council**, 2026-03-11 at 12:51 a.m. — Project Cardinal,
  1,037 acres, up to ~1,800 MW at full build-out, 14 buildings / 17M sq ft.
  [Shaw Local](https://www.shawlocal.com/kendall-county-now/2026/03/12/yorkville-data-center-approval-comes-after-nearly-6-hour-contentious-city-council-meeting/)
- **Yorkville City Council**, 2026-03-24 — Project Steel, 540 acres, 16 buildings.
- **Joliet City Council**, 2026-03-19, 8–1 — conditional annexation of ~795 acres
  for the Joliet Technology Center, up to 1.8 GW, 24 two-story buildings; rezoned
  A-1 agricultural to I-1 light industrial.
  [Farmers Weekly Review](https://fwrnews.com/2026/03/19/city-of-joliet-approves-conditional-annexation-for-proposed-data-center/)
- ~3,016 acres in Yorkville now slated for data centers along the ComEd
  transmission line off Eldamain Road.
- **Contested:** Joliet Residents For Responsible Growth filed suit 2026-05-18 in
  Will County alleging the rezoning is unconstitutional and that the city
  violated state law in the approval process. **Hearing set 2026-09-08.**
  [Shaw Local](https://www.shawlocal.com/the-herald-news/2026/08/18/lawsuit-against-joliet-data-center-heading-to-court-hearing/)

**The methodological correction:** these are **municipal** actions — city council
votes, annexation agreements, PUD ordinances, city minutes. M-PP-01's stated
method, "county rezoning dockets," points at the wrong record system entirely.
County boards are not where this lives. **Any prospect list built from county
records will systematically miss the largest approvals in the market.**

**Changes this row:** the 2026-09-08 ruling; project downsizing (the first
Yorkville approval is already reported to be halving building heights);
withdrawal; or discovery that some approvals in this market *do* run through
county boards, which would make the venue question site-by-site rather than
categorical.

---

### C10 — Retired-industrial conversions

**SPLIT: two of three support the claim; the third does not belong.** · mixed

| Site | Verdict |
|---|---|
| **Homer City, PA** | SUPPORTED **with a correction**. 3,200-acre former 1,884 MW coal site, decommissioned 2023-07-01, interconnected to **both** PJM (via FirstEnergy Pennsylvania Electric) and NYISO. HCR/Kiewit announced 2025-04-02 up to **4.5 GW of new gas generation**. What is reused is the site, switchyard and interconnection position — **not** the retired unit's capacity, and it must never be described that way |
| **TeraWulf Lake Mariner, NY** | SUPPORTED. 180 acres leased from the ~1,800-acre former Somerset/Kintigh coal campus; dual 345 kV transmission; NYISO Zone A |
| **Meta Forest City, NC** | **FALSE as bundled.** A brownfield conversion — 140 acres, Burlington Industries textile (1970s–90s), then Tracker Marine boat manufacturing (2000s), vacant from 2008, redeveloped under a 2012 [NC Brownfields Agreement](https://www.deq.nc.gov/about/divisions/waste-management/brownfields-program/program-information/success-stories). **No retired power plant. No interconnection asset reused.** A contaminated-land story, not a copper story |

**Why the third one matters more than it looks:** including Meta Forest City
inflated the apparent evidence for the central thesis by 50% — three exemplars
where there were two — by silently substituting "reused industrial land" for
"reused interconnection asset." That is the exact conflation the product exists
to catch, committed in our own founding document.

**Changes this row:** a systematic survey of retired-generation-site conversions
with stated inclusion criteria. **Two verified exemplars is two, not a pattern**,
and this repository will not call it a pattern until it counts them properly.

---

## Part 2 — the operator's original assumptions A–N

**STATUS: NOT RECOVERABLE FROM THIS REPOSITORY. This is a blocking gap and it is
recorded rather than filled.**

M-PP-00's acceptance criteria require this file to cover "the operator's original
assumptions A–N." Those assumptions exist only in the M-PP-BOOT session
transcript and are not present in any committed file, in `CLAUDE.md`, in
`LADDER.md`, or in any research artifact.

Per the NULL rule in `SOURCE_OF_TRUTH.md` §4, **they are not reconstructed from
memory, not inferred, and not replaced with plausible substitutes.** Fourteen
invented rows carrying the operator's initials would be worse than an empty
section, because they would look verified.

**Action required from the operator:** supply A–N verbatim. They will be added by
amendment to this file without opening a new contract, since M-PP-00's acceptance
already names them.

What *can* be stated: three assumptions are inferable from committed artifacts
and are recorded below as **RECONSTRUCTED** — a class that carries no confidence
and must be confirmed or retired.

| # | Reconstructed assumption | Source in repo | Changes this |
|---|---|---|---|
| R1 | Reality Infrastructure is imported as a library, never vendored, never edited — implying RI's neutrality covenant constrains what power-path may sell | `CLAUDE.md`; ERCOT decision §2 | The covenant being read and found not to constrain developer-side or buyer-side retainers |
| R2 | The operator's demonstrated competence is distressed property records, contested claims, and parcel/title work in Cook County, Illinois | ERCOT decision §3 | Any engagement demonstrating competence outside that domain |
| R3 | A warm pipeline already exists — Nigel, a land-bank relationship, a 291/9/70/35 audit, the Grandview deck, PPG-50, and a Deal One with a Kendall buyer — several with outreach GO gates pending | ERCOT decision §6 | The operator confirming, correcting, or closing these items |

R3 is the most consequential unconfirmed item in this file. **If that pipeline is
real and warm, the fastest path to Gate A does not begin with cold outreach at
all** — it begins with the conversations already pending. That question is
answered at M-PP-07 and it should be answered by the operator, not researched.

---

## Part 3 — assumptions created by this contract

| # | Assumption | Class | Changes this |
|---|---|---|---|
| N1 | The copper/paper distinction is decision-relevant to buyers — they do not already know it and their counsel does not already cover it | **UNKNOWN, untested** | Asking three buyers. **This is the same falsifier the ERCOT wedge died on, unchecked across four sessions. It gets checked before outreach, not after** |
| N2 | A non-lawyer may sell this analysis without it constituting legal advice | **UNKNOWN, untested** | One conversation with a practising attorney. Cheapest test in the repository and the most one-way if wrong |
| N3 | The ICP is the buyer-side principal (acquirer, independent sponsor, or lender) underwriting an asserted power path | **HYPOTHESIS, zero conversations** | M-PP-08's ICP verdict |
| N4 | PJM's SIS treatment is representative enough of other RTOs to generalize the copper/paper claim | **UNKNOWN** | Reading the MISO, SPP, CAISO, NYISO and ISO-NE tariffs — and the six §206 responses just filed are an unusually cheap way to do it |
| N5 | Illinois/Cook County is the right first geography because operator competence and the power-path question overlap there | PLAUSIBLE | An Illinois buyer declining while an out-of-state one buys |

---

## Standing rule

Every row in this file is a liability until it is tested against a person who can
say no. Verification against primary sources establishes that a claim is
**true**. It does not establish that anyone will **pay** for it. The ERCOT wedge
had a fully verified factual foundation and died anyway, on gates that no amount
of further verification could have addressed.
