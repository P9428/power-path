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
