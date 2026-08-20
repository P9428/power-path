# power-path — Contract Ladder

18 contracts, M-PP-00 → M-PP-17, with three sales stophook gates.
ONE contract at a time, completed end-to-end. A contract is closed when its
text is moved to `/contracts/closed/`.

Gate positions are fixed by M-PP-BOOT. Rung titles were set at bootstrap
from the M-PP-BOOT research pass and are revisable by contract.

## Rungs 00–07 — evidence and first contact

| Rung | Contract |
|---|---|
| M-PP-00 | Foundation docs — populate the six `/docs` stubs, including the falsification table |
| M-PP-01 | Named prospect list from public record (DCIP agreements, **municipal** annexation/rezoning/PUD records; county records as secondary sweep — amended by PP-008) |
| M-PP-02 | Spec memo v0 — one real site, hand-written, unpaid. The sales asset |
| M-PP-03 | Source registry + provenance capture, built from what the memo actually used |
| M-PP-04 | Claim/evidence schema — extracted from the memo, not designed ahead of it |
| M-PP-05 | Copper-vs-rights rule set — physical interconnection assets vs contractual rights |
| M-PP-06 | Adversarial checklist / kill-condition library |
| M-PP-07 | Outreach run — send and log ≥15 messages |

### 🚧 GATE A — blocks M-PP-08
**Required evidence:** ≥15 outreach messages sent and logged.
Until logged, M-PP-08 may not be authored.

## Rungs 08–10 — first revenue

| Rung | Contract |
|---|---|
| M-PP-08 | Response instrumentation + ICP verdict — did the ICP hypothesis survive? |
| M-PP-09 | Memo hardening from outreach feedback |
| M-PP-10 | Pricing and delivery mechanics; close and deliver paid memo #1 |

### 🚧 GATE B — blocks M-PP-11
**Required evidence:** 1 paid memo delivered, outcome logged.
Until logged, M-PP-11 may not be authored.

## Rungs 11–15 — repeatability

| Rung | Contract |
|---|---|
| M-PP-11 | Paid-memo retro — which step to automate first |
| M-PP-12 | Automate the highest-cost memo step |
| M-PP-13 | Eval harness — memo quality against known ground truth |
| M-PP-14 | Monitoring — FERC/tariff/queue change tracking (the perishable asymmetry) |
| M-PP-15 | Repeatable batch delivery to ≥10 delivered memos |

### 🚧 GATE C — blocks M-PP-16
**Required evidence:** ≥10 delivered memos with logged outcomes.
Until logged, M-PP-16 may not be authored.

## Rungs 16–17 — control

| Rung | Contract |
|---|---|
| M-PP-16 | Permission-assembly design + questions for counsel |
| M-PP-17 | Ownership path decision — fee, control, promote, or stop |

## Closed

| Contract | Closed |
|---|---|
| M-PP-BOOT | repository skeleton |
| M-PP-00 | foundation docs (2026-08-20) |

## Note on ladder state

M-PP-01, M-PP-05/06, M-PP-01b and M-PP-01c appear in commit history executed
against ERCOT while M-PP-00 was still open. That wedge was killed (PP-006) and
the out-of-order execution is recorded at PP-007. **Those rungs are NOT closed.**
The artifacts are kept as reference in `/research/ercot-audit-prospects/`;
the rungs must be authored fresh against Illinois.
