# ROADMAP

Written by M-PP-00, 2026-08-20.

**The ladder is the plan.** See [`/contracts/LADDER.md`](../contracts/LADDER.md)
for all eighteen rungs and the three gate positions. It is not duplicated here.

This file adds only what the ladder does not carry: **dates, gate conditions, and
kill criteria.**

---

## The three gates

Gate positions are fixed by M-PP-BOOT and are not revisable by a later contract.

| Gate | Blocks | Required evidence | Status |
|---|---|---|---|
| **A** | M-PP-08 | ≥15 outreach messages sent and logged | **NOT MET** — 0 sent |
| **B** | M-PP-11 | 1 paid memo delivered, outcome logged | **NOT MET** |
| **C** | M-PP-16 | ≥10 delivered memos with logged outcomes | **NOT MET** |

**A gate is met by evidence in the repository, not by judgment.** If a gate's
evidence is not logged, the gated contract may not be authored — not in a reduced
form, not as a partial substitute, not "to have something ready."

The ERCOT episode produced a list of 15 named executives and a proposal to send.
**Zero were sent, correctly** (PP-006). Gate A counts messages actually sent to
real people, not messages drafted.

## Dates

Target dates, not commitments. A missed date is information about the estimate;
a missed **kill criterion** is information about the business.

| Window | Ends | Target |
|---|---|---|
| Immediate | **2026-08-27** | N2 answered (the UPL question, Illinois). M-PP-01 authored and executed against corrected municipal venues |
| 30-day | **2026-09-19** | M-PP-02 delivered — memo #1, one real site, unpaid, in a buyer's hands. M-PP-03/04 extracted from it |
| 90-day | **2026-11-18** | Gate A met (≥15 logged). M-PP-08 ICP verdict rendered. Gate B attempted |

Two fixed external dates land inside these windows and are not ours to move:

- **2026-09-08** — hearing in the Joliet rezoning challenge (Will County). The
  ruling changes what a memo about that market must say.
- **~2026-08-17, already passed** — the 60-day deadline on FERC's six §206 show
  cause orders (EL26-67-000 et al.). Six RTO responses have landed. **Reading
  PJM's and MISO's is the cheapest available input to memo #1 and to ASSUMPTIONS
  N4.**

## Sequenced next actions

Ordered by cost-to-test, cheapest first. This ordering is deliberate and is the
correction to the ERCOT failure mode, where the most expensive and least
reversible action was reached for first.

1. **Ask the UPL question (N2).** One conversation with one Illinois attorney.
   Free. Collapses most of the decision tree either way. **PP-011.**
2. **Ask the operator for assumptions A–N (PP-012)** and for the status of the
   warm pipeline (ASSUMPTIONS R3 — Nigel, the land-bank relationship, the
   291/9/70/35 audit, the Grandview deck, PPG-50, Deal One with a Kendall buyer).
   Free. **If that pipeline is warm, the path to Gate A does not start with cold
   outreach at all.**
3. **Ask three buyers whether copper-vs-paper is decision-relevant (N1).** Cheap.
   **This is the falsifier the ERCOT wedge died on without ever being checked.**
4. **Source the ComEd peak denominator (PP-010).** One document. Unblocks the
   thesis's most quotable number.
5. **Author and execute M-PP-01** — named prospect list, Illinois, municipal
   annexation/rezoning/PUD records with a county secondary sweep (PP-008).
6. **M-PP-02** — memo #1, hand-written.

Items 1–4 are conversations and lookups, not builds. **None of them requires a
contract, and none of them should wait for one.**

## Kill criteria

### 30-day window — ends 2026-09-19

**KILL if:** memo #1 cannot be completed on a real site because the public record
does not support the copper/paper determination at all.

Not "it was hard." Not "some fields were NULL" — NULL is an expected and
reportable finding, and a memo that says *this cannot be determined from public
record, here is what was searched* is a valid memo. The kill condition is that
**the determination is not makeable in principle from available sources**, which
would mean the product cannot exist in this form.

**KILL if:** the UPL answer (N2) is that this constitutes legal advice in
substance **and** no redesign of the deliverable avoids it. Note the conjunction:
an unfavourable answer alone triggers redesign, not death.

### 90-day window — ends 2026-11-18

**KILL if:** ≥15 messages logged (Gate A met) and **zero** responses indicate
willingness to pay at any price. Not "no one paid" — no one *would*. That is
M-PP-08's ICP verdict and it is a real kill, not a signal to lower the price.

**KILL if:** the copper/paper distinction proves not decision-relevant (N1) —
buyers already know it, their counsel already covers it, or it does not change
what they pay. **This is the ERCOT falsifier and it kills this wedge exactly as
it killed that one.**

**PIVOT, do not kill, if:** the ICP is wrong but a different profile buys. That
is PP-004 reversing, which is what a labelled hypothesis is for.

### Standing kill criterion, no window

**KILL — or more precisely, STOP AND REPORT — if the repository accumulates a
second episode of artifact production without a single customer conversation.**

The ERCOT episode ran four sessions, 152 entity records, an affiliation graph, an
exposure calculator and four commits with zero conversations. The decision record
named the mechanism: *"artifact volume feels like progress and is
self-justifying."*

The operational test: **at any point, count the days since the last conversation
with a person who could say no.** If that number exceeds the number of commits
since that conversation, work has drifted from selling to producing.

This criterion applies to Claude at least as much as to the operator. The ERCOT
decision named Claude as the first suspect, and it was right to.

## What "done" looks like at 90 days

Not a platform. Not a pipeline. Not a dataset.

**One person who paid for one memo, and a written record of why they did.**

Everything in rungs 11–17 exists to repeat that. Nothing in rungs 11–17 is worth
building if it has not happened once.
