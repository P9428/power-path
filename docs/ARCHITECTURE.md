# ARCHITECTURE

Written by M-PP-00, 2026-08-20.

At this rung this document is **primarily a deferral list**. Its job is to say
what is deliberately not being built, and which rung earns it.

---

## The governing rule

**No schema, store, agent, pipeline, adapter, or eval harness is authorized
before the rung that names it.**

Not prototyped. Not "just a quick version." Not scaffolded so it is ready later.
If a rung has not been reached, the thing that rung builds does not exist, and a
contract that tries to build it early is out of scope and must stop.

## The first memo is hand-written by a human

**M-PP-02 — the spec memo, one real site, unpaid — is written by a human, by
hand, end to end.** No template, no generator, no extraction pipeline, no agent.

This is not a stylistic preference. It is the only way to learn which step
actually costs the most, and that question is not answerable by prediction. It is
asked with data at M-PP-11 and answered at M-PP-12.

The second memo is also hand-written. **Automation is authorized after two, not
after one** — one memo teaches what the work is; two teach what repeats.

## Current state of the codebase

There is no product code in this repository and none is authorized.

What exists in `/research/ercot-audit-prospects/` — `parse.py`, `classify.py`,
`contacts.py`, `tx_entities.py`, `affiliation.py`, `exposure.py` — is **research
scaffolding for a wedge that was killed on 2026-08-20** (PP-006). It is kept as
reference. It is not a foundation, not a dependency, and nothing may import it.
Its method is the transferable part; its targeting was wrong.

Every other top-level directory is an empty `.gitkeep` and is expected to stay
that way until its rung.

## Deferral list

| Component | Earned at | Not before, because |
|---|---|---|
| Source registry / provenance capture | **M-PP-03** | It is built from what the memo actually used. Designing it first produces fields nobody needs and omits the ones the work demanded |
| Claim/evidence schema | **M-PP-04** | Extracted from the memo, not designed ahead of it. A schema written before a real claim exists encodes guesses about shape |
| Copper-vs-rights rule set | **M-PP-05** | The distinction is stated in `SOURCE_OF_TRUTH.md` §7 as vocabulary. Turning it into a *rule set* requires having applied it to a real site once |
| Adversarial checklist / kill-condition library | **M-PP-06** | A checklist written before the first memo is a list of things that sound like they matter |
| Response instrumentation | **M-PP-08** | Behind Gate A. There is nothing to instrument until ≥15 messages are logged |
| Automation of any memo step | **M-PP-12** | Behind Gate B, and behind M-PP-11's retro. The step to automate is chosen from measurement, not from which step felt tedious |
| Eval harness | **M-PP-13** | Requires known ground truth. Ground truth requires delivered memos with outcomes |
| Monitoring (FERC / tariff / queue change tracking) | **M-PP-14** | The perishable asymmetry is real and this is the most tempting thing in the ladder to build early. It monitors for customers who do not exist yet |
| Batch delivery | **M-PP-15** | Behind Gate C |
| Permission-assembly design | **M-PP-16** | Behind Gate C, and requires counsel |

## Reality Infrastructure

**RI is imported as a library. Never vendored, never edited, never forked.**

RI is not currently imported anywhere in this repository and no rung before
M-PP-12 requires it.

**Unresolved and load-bearing:** RI's neutrality covenant. The ERCOT decision
recorded that developer-side retainers damage it and that the question was never
settled. It is recorded as ASSUMPTIONS R1. **It must be resolved before any
paid engagement is accepted (M-PP-10), not after** — an engagement signed against
an unresolved covenant is not reversible by discovering the covenant later.

## Things that will feel urgent and are not

Recorded here because each has already been proposed once, or is the obvious next
thought after reading the thesis:

- **A monitoring service for FERC and tariff changes.** The perishable asymmetry
  is genuine and the six §206 responses that landed ~2026-08-17 are genuinely
  interesting. It is still M-PP-14. Reading those responses as *research input to
  a memo* is in scope. Building a system that watches for them is not.
- **A parcel/title data subscription.** Deferred, not rejected (PP-006). Type 2,
  cheap to revisit, and it should be revisited when a specific site needs it —
  not on a monthly subscription bought in advance of a customer.
- **An entity/affiliation graph for Illinois.** The ERCOT version worked. That is
  precisely why it is tempting. It is M-PP-01 scaffolding at most, and M-PP-01 is
  a *named prospect list*, not a graph.
- **Generalizing the copper/paper claim across all six RTOs.** Recorded as
  ASSUMPTIONS N4. The verified tariff text is **PJM-specific**. Generalizing it in
  a memo without checking MISO/SPP/CAISO/NYISO/ISO-NE would be exactly the error
  this repository sells the correction to.

## Design constraints that outlive every rung

1. **NULL stays NULL.** No imputation anywhere, in any file, ever.
2. **An error is not an empty result.** A 400, a 403, a timeout, or an error
   object means the question was not answered — never that the answer is none.
3. **Every claim carries `source_url` and `observed_date`.**
4. **Repetition never increases confidence.** Two copies of one source are one
   source.
5. **Contradictions are preserved, not resolved silently.**
6. **Vendor addresses are suppressed** before any affiliation inference.

These are stated in full in `SOURCE_OF_TRUTH.md` and repeated here because they
constrain design, not just data entry. Any component that cannot represent NULL
distinctly from zero, or an error distinctly from an empty set, is the wrong
component.
