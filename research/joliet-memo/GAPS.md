# GAPS — Joliet Technology Center

What could not be determined, what was tried, and what it would cost to close.
Nothing here is deleted, softened, or restated as a hedge. Per
`SOURCE_OF_TRUTH.md` §4, an unanswered question is recorded as unanswered.

Assembled 2026-08-20.

---

## G1 — Site control. **The largest gap, and the most valuable to close.**

**Unknown:** whether PowerHouse Hillwood Holding, LLC holds title, purchase
agreements, options, or nothing on the ~795-acre assemblage; who the current
record owners are; what encumbrances exist.

**What the record says instead:** annexation *"will take effect upon the
developer's acquisition of the property"*; $20M due *"within 30 days of closing on
the property."* Both imply acquisition had not occurred as of the memo.

**Tried:** the staff memo and the developer's site. Neither names a seller, a
closing date, or a contract.

**Cost to close:** **$0 in fees, operator time only.** Will County Recorder and
the county GIS/parcel viewer are public. The assemblage is identifiable by
geography — S. Rowell Road and Bernhard Road, south of Chicagoland Speedway, and
the Preliminary Plat identifies **Lot 3** specifically.

**This is the operator's home competence** — Cook County distressed property
records, contested claims, parcel and title work, applied one county west.
**Closing G1 is the single highest-value hour available on this site**, and it is
the part of the memo no search engine can produce.

### G1 addendum, 2026-08-20 — the parcel set, narrowed

*(Appended to G1 rather than written as a new file. The artifact-drift condition
was checked first, per the PP-014 amendment.)*

Will County's public GIS parcel layer was queried directly:
`gis.willcountyillinois.com/hosting/rest/services/Basemap/Parcels_LY_V/MapServer/0`.
It is open, needs no token, and carries **PIN, address, acreage, property class,
and equalized value — but no owner name field.** That is the boundary of what
GIS can answer; owners come from the Supervisor of Assessments portal or the
Recorder.

**Candidate assemblage: sections 10-11-01 and 10-11-02** — 37 parcels, 1,307.9
acres total, bounded by Rowell (west), Ridge (east), Schweitzer (north), with
Bernhard running through, which matches the staff memo's right-of-way language
(dedications to S. Rowell and S. Ridge; vacation of Bernhard between them;
Millsdale extension to the western property line).

**The eight largest class-F (farm) parcels in those two sections sum to 769.6
acres — within ~3% of the stated 795.** Not a confirmation; a candidate set.

| PIN (portal format) | raw | acres | address |
|---|---|---|---|
| 10-11-02-300-002-0000 | 1011023000020000 | 155.00 | V BERNHARD |
| 10-11-01-400-001-0000 | 1011014000010000 | 123.05 | V BERNHARD |
| 10-11-01-300-001-0000 | 1011013000010000 | 116.00 | 17415 BERNHARD |
| 10-11-01-100-001-0000 | 1011011000010000 | 85.91 | V SCHWEITZER |
| 10-11-01-200-001-0000 | 1011012000010000 | 81.70 | V CHERRY HILL |
| 10-11-02-100-018-0020 | 1011021000180020 | 72.96 | V ROWELL |
| 10-11-02-400-007-0000 | 1011024000070000 | 70.00 | V BERNHARD |
| 10-11-02-400-005-0000 | 1011024000050000 | 65.00 | V RIDGE |

### AND THE FINDING THAT MATTERS — existing utility parcels inside the site

Seven parcels in these two sections carry the address label **"UTILITY
BERNHARD"** and are classed **I (industrial)**:

| PIN (portal format) | raw | acres | EAV |
|---|---|---|---|
| 10-11-01-100-004-0000 | 1011011000040000 | 9.06 | 74,440 |
| 10-11-02-100-002-0000 | 1011021000020000 | 5.00 | 16,830 |
| 10-11-02-100-012-0000 | 1011021000120000 | 4.62 | 15,550 |
| 10-11-02-200-004-0000 | 1011022000040000 | 3.50 | 11,780 |
| 10-11-01-200-006-0010 | 1011012000060010 | 3.50 | 11,780 |
| 10-11-01-200-006-0020 | 1011012000060020 | 3.50 | 11,780 |
| 10-11-02-200-006-0000 | 1011022000060000 | 1.22 | 4,110 |

**~30.4 acres of existing utility-classed parcels strung along Bernhard Road,
through the middle of the proposed campus.** Their shape — a chain of small
industrial parcels following one road — is the signature of a **transmission or
pipeline right-of-way corridor**, not of standalone industrial sites.

**Why this is the most valuable thing found on this site so far:** the staff memo
describes the power path entirely in the future tense — substations "would
accompany" each phase, a switching station "would be situated," Lot 3 "would
eventually be conveyed." **These parcels already exist and are already utility.**
Whether the campus's interconnection depends on, crosses, or is constrained by an
existing ComEd corridor already running through the assemblage is **not mentioned
anywhere** in the annexation record, the staff memo, or the developer's material.

**Unknown, and the highest-value question now open:** who owns these seven
parcels, what is recorded against them, and does an easement or right-of-way
encumber the farm parcels around them. **If ComEd already holds a corridor
through this site, the site-control question and the power-path question are the
same question** — which is precisely the thesis, and it would be found in the
operator's own record system, not in any energy database.

**Cost: $0.** Same recorder search as the rest of G1, seven more PINs.

### How to run the search

The SOA portal takes PINs as **2-2-2-3-3-4**, dashes optional. **Two partial
searches return the entire candidate set with owner names** — far faster than
fifteen individual lookups:

```
101101      -> all 14 parcels in section 10-11-01
101102      -> all 23 parcels in section 10-11-02
```

Note `10-11-01-200-006-0010` and `-0020` are **splits of the same parent parcel
006**, both 3.50 ac — the signature of a strip carved out of a larger holding,
which is how an easement or a conveyed right-of-way often appears. Pull the
parent's history.

**Two-portal discipline, and it is the error-vs-empty rule again:** the SOA
portal shows the **assessed owner**, which lags recording and reflects the tax
roll rather than title. It answers "has anything changed hands." It does **not**
show recorded options or purchase-agreement memoranda — which are exactly how an
assembler ties up farmland without recording a deed, and therefore exactly what
this site would show if the developer has control but not ownership. **A `no` at
the assessor is not a `no` on a transaction.** Only the Recorder's
grantor/grantee index answers that.

---

## G1 — RESULT, 2026-08-20. Operator ran `101101` and `101102`.

**G1 is substantially CLOSED.** Findings below are from the Will County
Supervisor of Assessments roll, retrieved by the operator, observed 2026-08-20.
Tier: PRIMARY as to assessed ownership. **Assessed owner is not title** — the
recorder search is still owed.

### R1. The corridor hypothesis was WRONG. It is gas, not electric.

The G1 addendum above hypothesised that the seven "UTILITY BERNHARD" parcels were
*"the signature of a transmission or pipeline right-of-way corridor"* and asked
*"If ComEd already holds a corridor through this site..."*

**All seven return the assessed owner `NATURAL GAS PIPELINE`.** Not ComEd. Not
electric. **The electric-corridor reading is FALSE and is recorded as false, not
quietly restated as "utility corridor."**

| PIN | acres | assessed owner |
|---|---|---|
| 10-11-01-100-004-0000 | 9.06 | NATURAL GAS PIPELINE |
| 10-11-01-200-006-0010 | 3.50 | NATURAL GAS PIPELINE |
| 10-11-01-200-006-0020 | 3.50 | NATURAL GAS PIPELINE |
| 10-11-02-100-002-0000 | 5.00 | NATURAL GAS PIPELINE |
| 10-11-02-100-012-0000 | 4.62 | NATURAL GAS PIPELINE |
| 10-11-02-200-004-0000 | 3.50 | NATURAL GAS PIPELINE |
| 10-11-02-200-006-0000 | 1.22 | NATURAL GAS PIPELINE |

**INFERENCE, not fact:** "Natural Gas Pipeline Company of America LLC" (NGPL,
Kinder Morgan) is a real entity of that name whose **Chicago supply hub is at
Joliet**. The assessor string is consistent with NGPL but **is not confirmed to
be NGPL**, and the roll may carry a truncated or generic label. Classification:
**PLAUSIBLE.** Closing it: the recorder's grantee index on these seven PINs, or
FERC's index of NGPL certificated facilities.

**Why the wrong answer is still valuable — and this is not a rescue of a dead
hypothesis, it is a different fact:** an interstate natural gas pipeline
easement crossing a 795-acre campus is (a) a **construction constraint** — no-build
setbacks, crossing agreements, encroachment consent from a FERC-jurisdictional
operator; and (b) **the fuel path for on-site generation.** The developer states
*"There are no plans for any onsite generation assets."* A large interstate gas
line through the property is precisely what would make that statement
changeable — and Homer City is 4.5 GW of **new gas generation** built against a
reused site position. **What the record shows is a gas option nobody has priced,
sitting under a campus whose electric path is unexecuted.**

### R2. The developer owns nothing. Confirmed empirically.

**Not one parcel in either section is assessed to PowerHouse, Hillwood, or any
recognisable affiliate.** The site-control gap is no longer an inference from the
annexation language — it is confirmed against the roll.

### R3. But a contract purchaser exists, and it is a THIRD entity.

Press reporting attributes to the City of Joliet that **`HW Technology Park
Development, LLC` is the contract purchaser**, and that the current landowners
include **Bernhard Farms, Inc.**

So the structure has at least three names:
- **PowerHouse Hillwood Holding, LLC** — annexation petitioner (PRIMARY, staff memo)
- **HW Technology Park Development, LLC** — contract purchaser (SECONDARY, press citing the city)
- **Hillwood / PowerHouse Data Centers** — the JV parents (PRIMARY, developer site)

**This partially answers G1:** control is by **contract**, not ownership. It also
opens a new question — why the petitioner and the purchaser are different
entities, and which one the $100M community benefit and the annexation
obligations actually bind. **Not determinable from anything assembled here.**

### R4. The sellers are one extended family, fragmented across five vehicles.

| Vehicle | Parcels |
|---|---|
| BERNHARD FARMS INC | 10-11-02-200-007-0010, -0020, 10-11-02-400-003-0000 |
| BERNHARD FAMILY TRUST | 10-11-02-200-002-0000, 10-11-02-400-005-0000 |
| BERNHARD FAMILY LAND TRUST | 10-11-02-100-018-0010, -0020 |
| BERNHARD JAMES E TR | 10-11-01-200-001-0000, -007-0000, 10-11-01-400-005-0000 |
| BERNHARD LEONARD E | 10-11-02-300-002-0000 *(155 ac — largest parcel in the set)* |

Plus **`BERNARD FAMILY LAND TRUST`** at 10-11-02-400-007-0000 — **spelled without
the `h`**. Either an assessor typo for the same family or a distinct entity.
**Contradiction preserved, not resolved** (`SOURCE_OF_TRUTH.md` §6). It matters:
a misspelled grantor name is a title defect, and it is the kind of thing that is
found by looking rather than by asking.

Non-Bernhard holders of size: **RIDGE ROAD LLC** (10-11-01-300-001-0000, 116 ac —
an LLC named for a road, holding a large farm parcel, the classic holding-vehicle
or assembler pattern), **LESCH JO RITA TR** (123 ac + 1), **PLUNK RONALD A TR**
(85.91 ac + 1), **R&M LANDHOLDINGS LLC**, **MORGAN LAVERN FMLY PRTNRSHP LP**,
**RKG LAND GROUP LLC**, **RACE CAMP LLC**. And a **FOREST PRESERVE DISTRICT**
natural-trail parcel at 10-11-01-200-005-0000, inside the section.

### R5. A named plaintiff owns a parcel inside the footprint.

**`GARCIA PEDRO` is the assessed owner of 10-11-02-100-010-0000, 18041 W
Schweitzer Rd, ~5 acres.**

**Pedro Garcia is one of the three named plaintiffs** in the Will County action
(DOSSIER §6). This is a **verified link between the litigation and a specific
parcel inside the assemblage sections**, on the Schweitzer Road frontage the
staff memo identified as the residential edge requiring an *"additional
landscaping buffer."*

The Doorneweerds do not appear in either section — they are presumably in an
adjacent one. Not searched.

### R6. Reported conflict-of-interest allegation — recorded as reported

Press reporting (Patch, and DCD citing the City) states that **the landowning
family is that of Joliet's city planning director, Jayne Bernhard**, and reports
audience members at council meetings raising this during the hearings.

**What is verified here:** Bernhard-named entities are the assessed owners of the
core parcels. That is from the roll and is not in dispute.

**What is NOT verified and is not asserted:** any relationship between the
planning director and those entities; any recusal, disclosure, or failure of
either; and any impropriety. **This repository makes no such finding.** Whether a
conflict exists is a legal and ethical determination requiring the city's
disclosure records and the official's own filings — **none of which have been
looked at.**

**Recorded because it is material and because omitting it would be a choice**, and
because a memo that discusses this land without noting who is reported to own it
would be incomplete in a way a reader would resent discovering later. It is
recorded at the strength the sources support and no further.

### What G1 still owes

- **Recorder grantor/grantee index** on all fifteen PINs: deeds, **options and
  purchase-agreement memoranda**, and **easements** — particularly the gas
  easement's terms and whether it encumbers the farm parcels, not just the seven
  utility strips.
- Confirmation that `NATURAL GAS PIPELINE` is NGPL.
- Illinois SOS registered agents/managers for RIDGE ROAD LLC, R&M LANDHOLDINGS
  LLC, RKG LAND GROUP LLC, HW TECHNOLOGY PARK DEVELOPMENT LLC.
- The `BERNARD` / `BERNHARD` spelling discrepancy.

**Cost: still $0.**

## G2 — The complaint itself

**Unknown:** the actual pleadings in the Will County action. Everything in
DOSSIER §6 is press-derived and is recorded as allegation.

**Tried:** press only.

**Cost to close:** Will County Circuit Clerk. Likely **$0–$20** for copies, or
free at the counter. **The 2026-09-08 hearing is 19 days out** — the docket will
move before then, and a ruling changes what the memo must say. This is a
STOP CONDITION in the contract, not merely a gap.

## G3 — Which substation, which lines, which position

**Unknown:** what ComEd transmission facilities the 25-acre Lot 3 switching
station would connect to; voltage; whether the Wilton Center 765 kV node is
involved; the electrical distance to the nearest suitable point of
interconnection.

**Tried:** the staff memo (says only "dedicated infrastructure" and "isolation
from the broader ComEd network"); the developer's site (says only "served by
ComEd"); ComEd/Wilton Center press.

**No source assembled links this site to Wilton Center.** DOSSIER §3d records it
as a lead and explicitly not as a finding.

**Cost to close:** **$0.** The Preliminary PUD plan set and Preliminary Plat are
city records and will show the switchyard's connection geometry. Blocked by G6.

## G4 — Deposit applicability and phasing

**Unknown:** whether ComEd's large-load deposit attaches per project or per
phase; what "maximum known demand included in the load ramp" is for a four-phase
campus; whether any deposit has been posted; whether Constellation's pending
rehearing changes the formula.

**Consequence:** the $9,000,000 figure in DOSSIER §4a is **arithmetic on a rule
under three stated assumptions**, not the developer's actual exposure, and may
not be presented as such.

**Cost to close:** **$0.** ICC e-Docket 25-0677/25-0679 is public; the compliance
filing and the order itself resolve the mechanics. The rehearing status is on the
same docket.

## G5 — PJM's EL26-67-000 response, filed ~2026-08-17

**Unknown:** what PJM actually told FERC about large-load interconnection three
days ago. Directly overhead of this site and unread.

**Tried:** search only. The filing was not located; FERC's eLibrary was not
queried.

**Cost to close:** **$0.** FERC eLibrary, docket EL26-67-000. Note that
`ferc.gov` returned **HTTP 403** to WebFetch twice today on other pages — see G6.

## G6 — Machine access to the two most important portals

**joliet.gov returns HTTP 403** to WebFetch and to curl with a standard browser
user-agent. **ferc.gov returned 403** on its news pages, though PDFs under
`ferc.gov/sites/default/files/` were retrievable.

**Consequence, and it is a method finding, not a site finding:** the City of
Joliet's document portal — the authoritative source for the annexation agreement,
the two ordinances, the Preliminary PUD plan set, the Preliminary Plat, the plan
commission recommendation, and the meeting minutes — **was not reachable
programmatically from this machine.** The staff memo was obtained only because a
news organization rehosted it.

**Cost to close:** **$0.** A human browser session reaches these pages. This gap
closes with the operator opening the site, not with better tooling — and it is
worth recording that the highest-value primary source in this dossier came in
through a side door.

## G7 — Firmness, timing, and any executed agreement

**Unknown:** whether service will be firm or non-firm; MW by phase; in-service
dates; whether any interconnection agreement, service agreement, or construction
agreement exists.

**What the record says:** PJM *"must approve"* large loads; PJM and ComEd *"have
evaluated"* reliability impact. **Neither sentence asserts that approval was
granted.** No study, docket, queue position, or agreement is named anywhere.

**Cost to close:** partly $0 — PJM's public new-service-request queue and ComEd's
ICC compliance reporting on large-load clusters. Partly **not closeable from
public record at all**, since a bilateral retail supply agreement is private.

**This gap is the product.** It is the reason a buyer-side principal would pay
someone to look, and it should be stated in the memo as unresolved rather than
narrated around.

## G8 — The tax contradiction

**Unresolved by design.** $310M (city staff memo) vs ~$2.1B, incl. ~$462M city
share (developer). ~6.8× apart, and not explained by scope. See DOSSIER §5.

**Cost to close:** **$0** — the annexation agreement's fiscal exhibit, or the
city's underlying assumptions. Blocked by G6.

**Preserved, not resolved**, per `SOURCE_OF_TRUTH.md` §6. Whichever way it
resolves, the fact that the two governing documents disagree by ~7× on the
headline public benefit is itself a finding.

---

## Total cost to close every gap above

**$0 in fees.** Every remaining gap is operator time against public records —
county recorder, circuit clerk, city portal, ICC e-Docket, FERC eLibrary.

**No paid data source is required, and none was purchased.**

The `ROADMAP.md` 30-day kill criterion — *"the determination is not makeable in
principle from available sources"* — **does not fire.** It was makeable. Part came
back resolved (DOSSIER §3a), part came back NULL (G1, G7), and both are reportable.
