# CONTRACT M-PP-02 — Spec Memo v0, Joliet Technology Center

Status: OPEN — authored 2026-08-20
Rung: M-PP-02. Prior contract M-PP-00 closed 2026-08-20.
**M-PP-01 was authored and killed the same day at the judgement compounder** —
see `/contracts/closed/M-PP-01-KILLED-2026-08-20.md` and DECISION_LOG PP-013.
The rung is skipped, not deferred in place.
Gate status: no stophook gate blocks this contract. **Gate A is untouched — this
contract sends nothing and delivers to no one.**

## OBJECTIVE

One memo. One real site. Hand-written. Unpaid.

**Site: the Joliet Technology Center** — ~795 acres, up to 1.8 GW, conditionally
annexed by Joliet City Council 8–1 on 2026-03-19, rezoned A-1 agricultural to
I-1 light industrial, **and under constitutional challenge with a hearing on
2026-09-08.**

Chosen over Project Cardinal and Project Steel because it is the only one of the
three where the power path, the land-use grant, and a live adversarial proceeding
sit on the same parcel. **The memo is about a question that is open, not one that
is settled.**

The memo answers one question and refuses to answer it vaguely:

> **Is the power path asserted for this site a physical interconnection asset, a
> contractual interconnection right, or undetermined on the public record — and
> what would it take to determine it?**

## WHY THIS RUNG, AND NOT A PROSPECT LIST

M-PP-01 was going to spend two weeks producing named sites. Three named,
primary-sourced sites already existed as a by-product of M-PP-00's verification
of C9. The compounder killed it at OPPORTUNITY COST. The full run is in
`/contracts/closed/M-PP-01-KILLED-2026-08-20.md` and it should be read before
this contract is executed, because it also records why the agent proposed the
wrong rung and would do so again unprompted.

## WHO WRITES IT

**The operator writes the memo. By hand. End to end.**

`ARCHITECTURE.md` states this and it is not negotiable at this rung: the memo is
hand-written *specifically* so that the cost of each step is learned rather than
predicted, because M-PP-11 chooses the first automation target from that data and
M-PP-12 is the first rung permitted to act on it.

**Claude's role is bounded to three things and nothing else:**

1. Assemble a **source dossier** — every primary document the memo may need,
   tiered and dated per `SOURCE_OF_TRUTH.md`, with search failures recorded.
2. Run an **adversarial pass on the operator's draft** — attack the memo's own
   claims the way the memo attacks the site's.
3. Record **time-per-step**, as reported by the operator, for M-PP-11.

**Claude does not draft the memo, does not outline it, and does not supply
sentences for it.** If this interpretation is wrong — if the operator wants
drafting help — that is a ruling to make explicitly, and it amends
`ARCHITECTURE.md` rather than being assumed into existence mid-contract.

## SCOPE

### Phase 1 — Source dossier (Claude)

Primary documents only, each with `source_url`, `source_tier`, `observed_date`:

- **Land use.** The Joliet annexation agreement, the rezoning ordinance, the
  8–1 council vote record, and the staff report / plan commission recommendation.
- **The challenge.** The complaint filed 2026-05-18 in Will County by Joliet
  Residents For Responsible Growth, and the docket entries to date.
- **The power path.** Whatever the public record actually contains: any
  substation, transmission line, or interconnection referenced in the annexation
  agreement or staff report; the ComEd corridor the site sits on; and — if the
  applicant has an ICC or PJM footprint — the corresponding filings.
- **The rules that bind it.** ComEd's large-load deposit tariff as approved
  2026-03-19 (ICC 25-0677/25-0679). PJM's Surplus Interconnection Service
  provisions. **PJM's response in EL26-67-000, filed on or about 2026-08-17** —
  three days old at authoring and directly on point.
- **Title.** What the public record shows about ownership and encumbrances on the
  ~795 acres. This is the operator's home competence; Claude assembles, the
  operator judges.

`research/joliet-memo/DOSSIER.md` and `research/joliet-memo/SOURCES.md`.
Every failure recorded in `GAPS.md` with what it would cost to close.

### Phase 2 — The memo (operator)

Hand-written. Structure is the operator's. The only mandatory elements:

- The one question above, answered — including "undetermined," which is a valid
  and often correct answer.
- Every claim carrying `source_url` and `observed_date`.
- **A section stating what would have to be true for the applicant's power-path
  story to hold, and whether it is.** This is the adversarial content and it is
  what distinguishes the artifact from a broker's summary.
- NULLs shown as NULLs.

### Phase 3 — Adversarial pass (Claude)

Attack the draft. Specifically: every place the memo asserts more than its source
supports; every place a contractual right is described in physical-asset language
or the reverse; every place a PJM-specific finding is stated generally (N4);
every NULL that has been softened into a hedge. Findings go to the operator; the
operator decides what changes.

### Phase 4 — Step costs (Claude records, operator reports)

Time per step, for M-PP-11. Recorded as reported, not estimated.

## CONSTRAINTS

- **NOTHING IS DELIVERED.** The memo is written and held. Delivery to any named
  human is blocked on **N2 — the Illinois UPL question** (PP-011). Writing is
  Type 2. Delivering is Type 1.
- No paid data. If title work requires a purchase, **stop and report the cost.**
- No template, no memo generator, no schema, no extraction pipeline. Schema is
  M-PP-04 and it is extracted *from* this memo, not designed before it.
- The **28 GW / 24 GW** comparison may not appear (PP-010). The 28,000 MW figure
  may be used alone, as *projects*.
- The SIS finding is PJM-specific. Joliet is in ComEd territory, which is in PJM,
  so it applies **here** — and the memo says "in PJM," not "generally."
- Proximity to a transmission line is not interconnection and is not recorded as
  such.

## ACCEPTANCE

- `research/joliet-memo/DOSSIER.md`, `SOURCES.md`, `GAPS.md`.
- The memo itself, at `deals/joliet-technology-center/MEMO_v0.md`.
- The adversarial pass recorded, with what the operator accepted and rejected.
- Step costs recorded.
- One commit "M-PP-02: spec memo v0, Joliet Technology Center", pushed.
- This contract moved to `/contracts/closed/`.

## DONE

Print: the answer to the one question; the count of claims by classification; the
gaps that cost money to close, with cost; the step-cost table; and the single next
action.

## STOP CONDITIONS

- **The public record does not permit the copper/paper determination at all** —
  not "it was hard," not "fields were NULL," but *not determinable in principle*.
  That is the 30-day kill criterion in `ROADMAP.md` and it fires here.
- **Title or docket access requires payment** → stop, report cost, await ruling.
- **The 2026-09-08 hearing lands mid-contract** → stop, record the ruling,
  reassess what the memo must say.
- **Any move to deliver the memo before N2 is answered** → stop. Type 1.
- **Any move by Claude to draft memo prose** → stop. That is the operator's rung
  and the reason it is his is written into `ARCHITECTURE.md`.
- **Artifact drift** — if this contract produces a fourth research file before a
  single memo paragraph exists, stop and report. Standing kill criterion.
