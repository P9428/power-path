# CONTRACT M-PP-01 — Named Prospect List, Illinois

Status: OPEN — authored 2026-08-20
Rung: M-PP-01. Prior contract M-PP-00 closed 2026-08-20 and is in
`/contracts/closed/M-PP-00-foundation-docs.md`.
Gate status: no stophook gate blocks this contract. **Gate A blocks M-PP-08 and
is not touched by this contract — this contract sends nothing.**

Method amended from the ladder's original wording by **PP-008**: municipal
annexation, rezoning and PUD records are primary; county records are a secondary
sweep, not the starting point.

## OBJECTIVE

Produce a named, contactable, evidence-backed prospect list for **Illinois** —
built from public record, in the venues that actually hold the record, with every
row carrying `source_url` and `observed_date`, and with the copper-versus-paper
question asked of every site rather than assumed.

The output is a list a human can act on. It is not a graph, not a database, not
a scoring model, and not a pipeline.

## CONTEXT

This rung has been attempted once, against ERCOT, and killed — see
`research/ercot-audit-prospects/DECISION_2026-08-20.md` and DECISION_LOG PP-006
and PP-007. The method held up; the targeting did not. Two things from that
failure are load-bearing here:

1. **It failed on CIRCLE** — shared method, almost no shared domain. Illinois is
   chosen because the operator's demonstrated competence in property records,
   contested claims, and parcel/title work is in the same jurisdiction as the
   question being asked.
2. **It failed on OPPORTUNITY COST** — a warm pipeline lost four sessions to a
   cold one. **That pipeline is unresolved and is a Phase 0 blocker below.**

Three verified facts set the shape of the Illinois record (see `ASSUMPTIONS.md`):

- **DCIP is a closed set.** Processing paused 2026-07-01; agreements entered
  before that date are honored. Everyone who holds one is knowable, finite, and
  will not be joined by anyone new. **A closed list of named parties who already
  committed capital is the single most valuable artifact in this jurisdiction and
  it stops growing.**
- **Approvals are municipal.** Yorkville City Council 2026-03-11 (Project
  Cardinal, 1,037 ac) and 2026-03-24 (Project Steel, 540 ac); Joliet City Council
  8–1 on 2026-03-19 (~795 ac). County boards are not where this lives.
- **The market is contested.** Suit filed 2026-05-18 in Will County challenges the
  Joliet rezoning; **hearing 2026-09-08**, inside this contract's window.

## SCOPE

### Phase 0 — Two questions to the operator, before any research

**This contract does not proceed past Phase 0 without answers.** Both are free,
both were open at M-PP-00 close, and both can invalidate the work below.

1. **The warm pipeline (ASSUMPTIONS R3).** Nigel, the land-bank relationship, the
   291/9/70/35 audit, the Grandview deck, PPG-50, Deal One with a Kendall buyer.
   Which are live? Which have outreach GO gates pending? **If any of these is a
   buyer-side principal facing a power-path question, they are prospect #1 and a
   cold list is the second priority, not the first.**
2. **Assumptions A–N (PP-012).** Supply verbatim, or rule that they are lost. If
   lost, that is recorded and this contract proceeds on R1–R3 plus N1–N5.

If the operator's answer to (1) makes the cold list unnecessary, **say so and
stop.** A contract that discovers its own output is not needed has succeeded.

### Phase 1 — The closed set: DCIP agreement holders

Source: DCEO's own published record of Data Center Investment Program
certificates and agreements. PRIMARY.

For each holder: entity name as recorded, agreement or certification date,
location as recorded, and whether the agreement predates 2026-07-01 (all should;
any that does not is a finding). `source_url` and `observed_date` on every row.

**If DCEO does not publish the list, that is a finding, not a failure.** Record
what was searched, then note that the list is obtainable by FOIA and enter the
FOIA as a costed option for the operator to rule on. Do not substitute a
press-derived list and do not present it as equivalent.

### Phase 2 — Municipal approvals sweep

Municipalities in ComEd service territory with known or suspected large-load
activity. Start from the verified three — **Yorkville, Joliet** — and expand by
following the ComEd transmission corridors, not by guessing at town names.

For each project: municipality, approving body, action type (annexation, rezoning,
PUD, special use), date, vote, acreage, stated MW, applicant of record, and the
identity behind the applicant where the record shows it. Project code names
(Cardinal, Steel) are recorded as recorded — **an alias is not an owner.**

Sources are city council minutes, agendas, ordinances, and annexation agreements.
`source_url` to the specific document, never to a search page.

### Phase 3 — County secondary sweep

County board and county planning records for the same geography, run **as a
detector**: does any large-load approval in this market run through a county
board rather than a municipality? PP-008's reversal condition depends on this
answer.

A null result is a real result and is reported as one.

### Phase 4 — The copper column

For each project on the list, one field, from public record only:

**Is the asserted power path a physical interconnection asset, a contractual
interconnection right, or undetermined?**

Most rows will be **undetermined**, and undetermined is the correct entry when
the public record does not say. Per `SOURCE_OF_TRUTH.md` §4, undetermined is not
downgraded to "likely," not filled from the applicant's own marketing, and not
inferred from proximity to a transmission line. **Proximity to a line is not
interconnection and recording it as such would be the exact error this business
exists to catch.**

Where the record *does* resolve it — a named retiring generator, a referenced ISA,
a substation named in an annexation agreement — that row is worth more than the
rest of the list combined, and is flagged.

### Phase 5 — Segment and rank

Segment by who carries the risk, not by project size. Rank by the **buyer-side
principal** hypothesis (PP-004): who is being asked to underwrite an asserted
power path and carries non-refundable downside if it is wrong.

Deliver **no more than 25 named prospects.** This is a hard cap and it is a
feature. The ERCOT run produced 135 parties and 152 entity records and zero
conversations.

## PLAN GATE

After Phase 0 and Phase 1, before Phases 2–5, output:

- The operator's Phase 0 answers and what they changed.
- The DCIP closed-set count, or the recorded failure to obtain it.
- The municipality list about to be swept, with the reason each is on it.

**WAIT for "approved" before Phases 2–5.**

## CONSTRAINTS

- **NOTHING IS SENT.** No email, no call, no LinkedIn, no draft addressed to a
  named human. Outreach is M-PP-07 and it is behind the ICP verdict and the UPL
  answer. The ERCOT run reached the send proposal twice before being stopped.
- **No paid data.** No parcel subscription, no skip-trace, no enrichment service.
  Deferred, not rejected (PP-006) — if a specific site needs it, stop and report
  the cost.
- **No code beyond what a single throwaway parse requires.** No graph, no
  affiliation model, no scoring function, no schema. The schema is M-PP-04.
- Vendor addresses suppressed before any affiliation inference is written down.
- The **28 GW / 24 GW** comparison may not appear anywhere in the output (PP-010).
  The 28,000 MW figure may be used alone, as *projects*, not applicants.
- The PJM Surplus Interconnection Service finding is **PJM-specific** (N4). It
  applies in ComEd territory, which is in PJM. It may not be stated as general.
- No edits to `/research/ercot-audit-prospects/`. It is reference and it stays as
  written, including the parts that were wrong.

## ACCEPTANCE

- `research/illinois-prospects/PROSPECTS.md` — ≤25 named prospects, each with
  source_url, observed_date, segment, and the Phase 4 copper column.
- `research/illinois-prospects/SOURCES.md` — every source with tier and
  observed_date, per `SOURCE_OF_TRUTH.md`.
- `research/illinois-prospects/GAPS.md` — what could not be determined, what was
  searched, and what it would cost to close each gap. **Every search failure
  recorded, none deleted.**
- The county sweep's answer to PP-008's reversal condition, stated either way.
- One commit "M-PP-01: Illinois prospect list", pushed.
- This contract moved to `/contracts/closed/`.

## DONE

Print: prospect count by segment; the count of copper-column rows resolved versus
undetermined; the PP-008 answer; every gap that costs money to close, with the
cost; and the single next action.

## STOP CONDITIONS

- **Phase 0 answer makes the cold list unnecessary** → stop and report. This is
  success, not failure.
- **DCEO does not publish the DCIP list** → report the FOIA option and its cost;
  do not substitute a press-derived list.
- **Any temptation to send anything to a named human** → stop. That is M-PP-07,
  it is behind Gate A's predecessors, and it is the Type 1 boundary the ERCOT run
  crossed twice in proposal.
- **Artifact drift** — if this contract produces its third research file before a
  single prospect has been shown to the operator, stop and report. Standing kill
  criterion, `ROADMAP.md`. The named mechanism is that artifact volume feels like
  progress and is self-justifying.
- **The 2026-09-08 Joliet ruling lands mid-contract** → stop, record it, and
  reassess. It changes what the Will County rows mean.
