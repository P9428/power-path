# DECISION LOG

Append-only. Entries are never edited or deleted. A decision that is reversed
gets a **new** entry recording the reversal and pointing back; the original
stays exactly as written, including the parts that turned out to be wrong.

Every entry carries a **reversal condition** — the observation that would make
this decision wrong. An entry without one is not a decision, it is a preference.

---

## PP-001 — SSH instead of `gh` for GitHub operations
**Date:** 2026-08-20 · **Contract:** M-PP-BOOT · **Decided by:** operator

The `gh` CLI is not installed on this machine. The BOOT contract's acceptance
check `gh repo view` could not run. Rather than install a dependency mid-contract,
the operator created the empty private repository in the GitHub UI and the
skeleton was pushed over SSH authenticated as P9428. The acceptance check was
replaced with `git ls-remote`, which also confirmed no name collision.

**Rationale:** a stop condition was hit and reported rather than worked around
silently. Installing tooling mid-contract is scope creep, and the substitute
check answered the same question.

**Reversal condition:** `gh` becomes available and a contract needs an operation
SSH cannot perform (PR creation, issue management, releases).

---

## PP-002 — Ladder rung titles set from research, not from the contract
**Date:** 2026-08-20 · **Contract:** M-PP-BOOT · **Decided by:** Claude, ratified by operator

M-PP-BOOT specified eighteen rungs and three gate positions but did not supply
rung titles. Titles for M-PP-00 through M-PP-17 were written from the M-PP-BOOT
research pass. Gate positions were taken as specified and not altered.

**Rationale:** an unlabelled ladder is not usable, and inventing titles is a
smaller error than shipping a skeleton nobody can navigate. Recorded here
specifically because the titles carry assumptions that were never separately
verified — including M-PP-01's "county rezoning dockets," which PP-008 below
finds to be wrong.

**Reversal condition:** any rung title found to encode a false assumption. Titles
are revisable by contract. **Partially triggered — see PP-008.**

---

## PP-003 — The component sequence is inverted from the operator's original ordering
**Date:** 2026-08-20 · **Contract:** M-PP-BOOT · **Decided by:** operator

The original ordering built capability first and sold second. The ladder inverts
it: evidence → one hand-written memo → one conversation → one sale, and only then
schema, pipeline, eval harness, monitoring. Three stophook gates enforce it —
no automation rung may be authored before delivery evidence is logged.

**Rationale:** every automation decision made before the second delivered memo is
a guess about which step is expensive. M-PP-11 asks that question with data;
M-PP-12 is the first rung permitted to answer it.

**Reversal condition:** a memo step is discovered to be so expensive that a human
cannot complete memo #1 at all. Cost, not tedium — tedium is the point at this
stage.

---

## PP-004 — The ICP is a hypothesis, and is labelled as one
**Date:** 2026-08-20 · **Contract:** M-PP-BOOT → M-PP-00 · **Decided by:** operator

The hypothesized ideal customer is the buyer-side principal — acquirer,
independent sponsor, or lender — underwriting a site whose power path is asserted
rather than proven, who now carries real non-refundable downside if the assertion
is wrong. **Zero conversations have been held with anyone in this profile.**

**Rationale:** naming an ICP focuses the memo. Labelling it a hypothesis prevents
the far more expensive error of treating a guess as a finding — which is exactly
what happened in the ERCOT episode (PP-006).

**Reversal condition:** M-PP-08's ICP verdict. Also reversed if the warm pipeline
in ASSUMPTIONS R3 turns out to contain a different profile that buys first.

---

## PP-005 — Illinois is the first geography
**Date:** 2026-08-20 · **Contract:** M-PP-BOOT → M-PP-00 · **Decided by:** operator

Illinois, Cook County first — chosen because the operator's demonstrated
competence (distressed property records, contested claims, parcel and title work)
is in the same jurisdiction as the power-path question.

**Rationale, corrected at M-PP-00:** the original framing was "Illinois broke as
the first geography." Primary sources do not support that. The *subsidy* broke —
DCIP processing paused 2026-07-01, ICC deposits imposed 2026-03-19 — while siting
continued (Yorkville 1,037 and 540 acres; Joliet 795 acres; ~3,016 acres slated
in Yorkville) and litigation began (Joliet hearing 2026-09-08). **The correct
statement is that Illinois stopped being easy, which is the only kind of market
that pays for adversarial diligence.**

**Reversal condition:** an out-of-state buyer paying while Illinois buyers
decline; or the DCIP pause being lifted and the market reverting to easy.

---

## PP-006 — Kill the ERCOT audit-readiness wedge as first revenue product
**Date:** 2026-08-20 · **Contract:** (none — ran outside the ladder) · **Decided by:** operator

Full record: `research/ercot-audit-prospects/DECISION_2026-08-20.md`.

Run against the eight-gate framework, failed on three: **REALITY** (the falsifier
— that these parties' counsel already owns this work — was never checked across
four sessions), **CIRCLE** (Texas energy regulatory practice is outside
demonstrated competence; shared method, almost no shared domain), and
**OPPORTUNITY COST** (a warm Cook County pipeline with GO gates pending for weeks
lost attention to it).

Actions: do not buy parcel data (deferred, not rejected — Type 2, cheap to
revisit); do not send the 15 messages (Type 1, unrecoverable); ask one Texas
energy attorney the UPL question first, because it collapses most of the tree;
point the same typed-evidence stack at Cook County.

**Rationale:** the process was good — primary sources, two false positives caught
and documented, refusals recorded. The targeting was bad. **Good process, wrong
county.**

**Reversal condition:** all three of — an energy attorney confirming the work is
non-legal advisory and saleable by a non-lawyer; **and** one named prospect
stating their counsel is not covering audit-exposure analysis; **and** evidence
the audit reaches well-papered projects rather than only speculative ones. Any
one alone is insufficient.

---

## PP-007 — Four rungs were executed while rung zero was open. Recorded, not erased.
**Date:** 2026-08-20 · **Contract:** M-PP-00 · **Decided by:** Claude, reported to operator

At the start of the M-PP-00 execution session, `contracts/CURRENT.md` showed
M-PP-00 **OPEN** and all six `/docs` files still carried the M-PP-BOOT stub line
— while commits `476369c`, `5e9cb0f`, `a03b0c3` and `721963c` had already
executed M-PP-01, M-PP-05/06, M-PP-01b and M-PP-01c against ERCOT.

`CLAUDE.md` requires one contract at a time and requires verifying the prior
contract is closed before authoring or executing. **That rule was broken four
times, in the direction of producing artifacts.**

**Decision:** the out-of-order work is **kept as reference and not deleted** —
it is paid for, the method in it is sound, and deleting it would destroy the
evidence of how the failure happened. It is **not** counted as ladder progress.
M-PP-01 remains unexecuted; when authored, it must be authored fresh against
Illinois with the corrected venue (PP-008).

**Rationale:** the ERCOT decision record already identified the mechanism —
"artifact volume feels like progress and is self-justifying." This entry exists
so the mechanism has a name in the log and not only in a research folder.

**Reversal condition:** none. This is a record of what happened.

---

## PP-008 — M-PP-01's method points at the wrong record system
**Date:** 2026-08-20 · **Contract:** M-PP-00 · **Decided by:** Claude, ratified by operator

M-PP-01's rung title specifies "DCIP agreements, county rezoning dockets."
Verification of C9 found that the largest Illinois approvals were **municipal**
actions: Yorkville City Council on 2026-03-11 and 2026-03-24; Joliet City Council
8–1 on 2026-03-19. The records are annexation agreements, PUD ordinances, and
city council minutes.

**Decision:** M-PP-01's method is amended, under the PP-002 revisability clause,
from county rezoning dockets to **municipal annexation, rezoning and PUD records,
with county records retained as a secondary sweep.**

**Rationale:** a prospect list built from county records would systematically miss
the largest approvals in the target market. This is a silent-miss failure — it
produces a plausible-looking list with the important names absent, which is worse
than producing nothing.

**Reversal condition:** discovery that some Illinois data-center approvals do run
through county boards, which would make venue a site-by-site question rather than
a categorical one. The secondary county sweep exists to detect this.

---

## PP-009 — "No whitespace" is downgraded to an open question
**Date:** 2026-08-20 · **Contract:** M-PP-00 · **Decided by:** Claude, ratified by operator

M-PP-BOOT concluded that Power Access Diligence "appears to have no whitespace —
several funded competitors already sell it." Verification found **one** named
funded competitor (Build.inc, $8.5M seed, 2026-06-30), with adjacent positioning
— desktop diligence automation sold on speed — and named clients in CRE, colo and
government, no hyperscaler.

**Decision:** the claim is restated as "at least one funded incumbent exists,
positioning is adjacent, **overlap is unmeasured**," and measuring it is entered
as real, unfinished work.

**Rationale:** "no whitespace" is a conclusion that would justify abandoning the
business. It was carrying the weight of a conclusion on the evidence of one
company found in a search. **A claim that would change the whole strategy needs
better evidence than a claim that would not.**

**Reversal condition:** finding two or more competitors selling adversarial,
site-specific, copper-versus-paper diligence to the hypothesized ICP; or Build.inc
moving into that positioning.

---

## PP-010 — The 28 GW / 24 GW comparison is retired until its denominator is sourced
**Date:** 2026-08-20 · **Contract:** M-PP-00 · **Decided by:** Claude, ratified by operator

"28 GW of applications against a ~24 GW all-time peak" is the most rhetorically
effective figure in the thesis. The numerator verified to primary source (ComEd
Ex. 1.0 — though as *projects*, not applicants). **The denominator did not.** The
only peak figure found is 23,753 MW in an undated item describing a record set
against a 2006 mark, most plausibly ~2011 vintage.

**Decision:** the comparison may not appear in any memo, deck, or outreach
message until the denominator carries a current primary source. The numerator may
be used alone.

**Rationale:** it is the number most likely to be repeated back by a prospect and
most likely to be checked. Being wrong on the most quotable figure in the first
sales conversation is a Type 1 error — first impressions do not get a second
pass. This is the same reasoning that stopped the ERCOT sends.

**Reversal condition:** a ComEd, Exelon, PJM or EIA publication stating current
system peak.

---

## PP-011 — The UPL question is tested before any outreach, in Illinois too
**Date:** 2026-08-20 · **Contract:** M-PP-00 · **Decided by:** operator, extended by Claude

The ERCOT decision made "ask one energy attorney whether a non-lawyer may sell
this analysis to a regulated party" the free-and-first action for Texas.

**Decision:** the question is not Texas-specific and the answer is not
transferable between states. It is asked for **Illinois**, before M-PP-07 outreach
and ideally before M-PP-02's memo is delivered to anyone. It is entered as
ASSUMPTIONS N2 and as the first item on the 30-day roadmap.

**Rationale:** it is the cheapest test in the repository — one conversation — and
the most one-way if wrong. A wrong memo delivered to a named executive is
reputationally unrecoverable, and no volume of correct primary-source work
mitigates it.

**Reversal condition:** an Illinois attorney confirming the work is non-legal
advisory as scoped. Note that a *favourable* answer reverses the constraint;
an unfavourable one requires redesigning the deliverable, not abandoning it.

---

## PP-012 — Assumptions A–N are recorded as missing rather than reconstructed
**Date:** 2026-08-20 · **Contract:** M-PP-00 · **Decided by:** Claude, reported to operator

M-PP-00's acceptance requires `ASSUMPTIONS.md` to cover the operator's original
assumptions A–N. They exist only in the M-PP-BOOT session transcript and are in no
committed file.

**Decision:** they are recorded as a blocking gap. **Not reconstructed, not
inferred, not replaced with plausible substitutes.** Three items inferable from
committed artifacts are recorded separately as RECONSTRUCTED (R1–R3), a class
carrying no confidence.

**Rationale:** the NULL rule. Fourteen invented rows carrying the operator's
initials would be worse than an empty section, because they would look verified —
and this repository's entire product claim is that it does not do that.

**Reversal condition:** the operator supplies A–N verbatim. They are added by
amendment to `ASSUMPTIONS.md` without opening a new contract, since M-PP-00's
acceptance already names them.
