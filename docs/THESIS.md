# THESIS

Written by M-PP-00, 2026-08-20. Revisable only by contract.

---

## What the company is

power-path sells **adversarial diligence on the power path of a specific
physical site**: the chain from a parcel to actual, firm, deliverable
electricity, examined by someone whose job is to find the place it breaks.

The deliverable is a memo about one site. It says what is proven, what is
asserted, what is unknown, and — the part nobody else writes down — what would
have to be true for the seller's story to hold, and whether it is.

Two things distinguish it from what a developer, a broker, or a law firm
produces:

1. **It is adversarial by construction.** It is not written to close the deal.
   Its value is highest when it kills one.
2. **It separates copper from paper.** See §"The edge" below and the capacity
   vocabulary in `SOURCE_OF_TRUTH.md` §7. Most power-path claims in the market
   are contractual rights described with the vocabulary of physical assets, or
   physical assets described with the vocabulary of contractual rights.

## The edge: copper, not queue position

This is the load-bearing claim of the business, and as of 2026-08-20 it is the
only one of three original reshapings that got **stronger** under primary-source
verification rather than weaker.

**Contractual interconnection rights are perishable, resource-bound, and mostly
non-transferable to load.** PJM's tariff provides that a Generating Facility
receiving Surplus Interconnection Service may continue to receive it *"for a
period not to exceed one (1) year after the existing Generating Facility's
Deactivation Date"* — conditional on the surplus unit having been studied for
sole operation at the Point of Interconnection, and on the incumbent owner
agreeing in writing. And the recipient must itself be **a Generating Facility**.
A data center is load. Load cannot take Surplus Interconnection Service.

**Physical interconnection assets are durable and convey with the land.** Homer
City's 3,200-acre retired coal site kept its interconnections into both PJM and
NYISO; the redevelopment is building 4.5 GW of new gas generation against that
position. TeraWulf leases 180 acres of the former Somerset/Kintigh coal campus
for its dual 345 kV lines and NYISO Zone A position.

So the market's shorthand — "this retired plant comes with its
interconnection" — is two different statements wearing one sentence. One of them
is usually true and one of them is usually false, and which is which decides
whether a site is worth eight figures or nothing. **That gap is the product.**

Note what does *not* support this: Meta's Forest City campus, previously cited
as a third exemplar, is a brownfield conversion of a textile plant and a boat
factory under a 2012 NC Brownfields Agreement. No power plant, no
interconnection reuse. It was removed from the evidence base on 2026-08-20.

## What the first wedge is

**One hand-written memo on one real site, unpaid, for one buyer-side principal.**
That is M-PP-02 and it is the next substantive rung.

It is hand-written by a human, deliberately. Nothing is automated before a human
has produced the artifact twice and knows which step actually costs the most.
See `ARCHITECTURE.md`.

**Geography: Illinois, Cook County first.** Not because Illinois is the biggest
market but because it is the one where the operator's demonstrated competence —
distressed property records, contested claims, title and parcel work — is in the
same jurisdiction as the power-path question. On 2026-08-20 an attempt to run
this method in ERCOT was killed for exactly this reason: shared method, almost
no shared domain.

**ICP: HYPOTHESIS, not finding.** The current hypothesis is the buyer-side
principal — an acquirer, an independent sponsor, or a lender — who is being
asked to underwrite a site whose power path is *asserted* rather than proven,
and who now carries real, non-refundable downside if the assertion is wrong.
This hypothesis has not been tested against a single real buyer. It is tested at
M-PP-07/08, and it is the single most likely thing in this document to be wrong.

## Why Illinois, specifically

Three things happened in Illinois between March and July 2026, all verified
against primary sources on 2026-08-20:

- **2026-03-19** — the ICC approved ComEd's large-load deposit tariff. Deposit is
  $1,000,000 plus $500,000 per additional whole 100 MW above 200 MW; deposits at
  or over $2,000,000 require an acceptable letter of credit. Real money now sits
  at risk before a project is certain.
- **2026-06-05 / effective 2026-07-01** — the Governor directed DCEO to pause
  processing Data Center Investment Program agreements. Agreements entered before
  July 1 are honored. *(The frequently-repeated "two-year" duration is not in the
  directive; it traces to a February 2026 budget proposal. Do not cite it.)*
- **Pipeline pressure** — ComEd's own testimony puts more than 75 large load
  projects totaling over 28,000 MW in the queue.

**But Illinois did not "break," and the earlier framing that it did was wrong.**
The *subsidy* broke. Siting continued: Yorkville's city council approved Project
Cardinal (1,037 acres, ~1,800 MW) on 2026-03-11 and Project Steel (540 acres) on
2026-03-24; Joliet's council approved a ~795-acre annexation for up to 1.8 GW on
2026-03-19. About 3,016 acres in Yorkville alone are slated along the ComEd
transmission line off Eldamain Road. And it is now contested — a suit filed
2026-05-18 challenges the Joliet rezoning as unconstitutional, with a hearing set
**2026-09-08**.

Subsidy withdrawn, deposits raised, approvals continuing, litigation started.
That is not a market that broke. **That is a market that stopped being easy** —
which is the only kind of market that pays for adversarial diligence.

## Why the component sequence was inverted

The operator's original ordering built capability first and sold second. The
ladder inverts it: evidence, one memo, one conversation, one sale — and only then
schema, pipeline, eval harness, monitoring.

The reason is that **every automation decision made before the second delivered
memo is a guess about which step is expensive.** M-PP-11 exists to ask that
question with data. M-PP-12 is the first rung permitted to answer it.

The ERCOT episode is the case in point and the reason this is written down
rather than assumed. Four sessions produced 152 entity records, an affiliation
graph, an exposure calculator, and a criteria document — before a single
conversation with a single buyer. The artifacts were competent. The targeting was
not, and no amount of artifact quality could have revealed that. Only the
conversation could.

## Competitive position

**"No whitespace" is NOT established, and was overstated.**

Build.inc is real: $8.5M seed led by Index Ventures announced 2026-06-30, with a
platform called Dougie, and the company claims over 250 completed projects in 17
countries. Its named customers are Tishman Speyer, Stack Infrastructure, and the
UK Government. No hyperscaler client is named on its own site.

That is a funded incumbent in an **adjacent** lane — desktop diligence
automation sold on speed ("cut due diligence timelines by more than 95%"). It is
not proof that adversarial, site-specific, copper-versus-paper diligence is
occupied. **The honest statement is: at least one funded incumbent exists,
positioning is adjacent, overlap is unmeasured.** Measuring it is a real task and
it has not been done.

## Falsification condition for the thesis as a whole

The thesis is dead if, by **2026-11-18** (90 days):

1. **No buyer-side principal will pay for a memo** — after ≥15 logged outreach
   messages (Gate A) and the ICP verdict at M-PP-08, no one in the hypothesized
   ICP will pay for the artifact at any price; **or**
2. **The copper/paper distinction turns out not to be decision-relevant** —
   buyers already know it, their counsel already covers it, or it does not change
   what they pay. This is the same falsifier the ERCOT wedge died on and it was
   never checked there. It gets checked here, early and cheaply, by asking; **or**
3. **The work cannot be sold by a non-lawyer** — if analyzing a party's
   contractual position and telling them what it means is legal advice in
   substance, the product cannot be delivered in this form regardless of demand.

Condition 3 is the cheapest to test and the most one-way if wrong. **It is
tested first.** See `ROADMAP.md`.

## What this thesis explicitly does not claim

- That queue position is worthless. It is claimed to be *perishable and
  resource-bound*, which is different.
- That retired industrial sites are generally good data center sites. Two
  verified exemplars is two, not a pattern.
- That the ICP is known. It is a hypothesis with zero conversations behind it.
- That Illinois is the best market. It is the market where the operator's
  existing competence and the power-path question overlap.
