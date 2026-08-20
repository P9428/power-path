# SOURCE OF TRUTH — evidence protocol

Written by M-PP-00, 2026-08-20. This is the **protocol**, not the catalog.
The source catalog is M-PP-03 and does not exist yet.

This file governs every claim that enters this repository. If a claim in any
other document conflicts with this file, this file wins and the other document
is wrong.

---

## 1. Source tier hierarchy

| Tier | Definition | Examples |
|---|---|---|
| **PRIMARY** | The issuing body's own instrument, published by that body | FERC order or docket item; a tariff as filed; an ICC order; a county or municipal ordinance, annexation agreement, or meeting minutes; a governor's own press release; an SEC filing; a company's statement about its own business; a recorded deed |
| **SECONDARY** | A named party's characterization of a primary source | Law-firm client alerts; trade press; an RTO's summary deck of someone else's order; analyst notes |
| **TERTIARY** | Aggregation, forum, or unattributed content | Trackers without stated methodology; forum posts; blog roundups; search-result summaries |

**A filing by a party in a docket is PRIMARY as to what that party asserted,
and inherits the tier of whatever it cites.** Constellation's rehearing
application is primary evidence that Constellation said something. It is not
primary evidence that the something is true — for that, follow the footnote.

**A search-result summary is not a source.** It is a pointer to a source. It
may be used to find the source and may never be cited in its place.

## 2. Claim classification

| Class | Meaning |
|---|---|
| **SUPPORTED** | A PRIMARY source states it, and the wording here matches the wording there |
| **PLAUSIBLE** | Consistent with available evidence, but the best source is SECONDARY or TERTIARY |
| **UNKNOWN** | Searched for and not found, or found only in a form that cannot be tiered. The attempted search is recorded |
| **FALSE** | A PRIMARY source contradicts it |
| **CONTEXT-DEPENDENT** | The claim's truth turns on a definition that sources do not share. The competing definitions are recorded |
| **RECONSTRUCTED** | Inferred from repository artifacts rather than stated by a source. Carries no confidence and must be confirmed by the operator or retired |

A claim moves between classes only when new evidence arrives. It never moves
because time passed, because it was repeated, or because it would be
inconvenient if it were false.

## 3. Required fields on every claim

Every claim, everywhere in this repository, carries:

- `claim` — the assertion, in the source's own scope, not broadened
- `classification` — from §2
- `source_url` — resolvable, and to the specific document, not a search page
- `source_tier` — from §1
- `observed_date` — when *we* looked, not when the source was published
- `change_condition` — what evidence would move this row. **Mandatory.**

A claim missing `change_condition` is not a claim. It is an opinion, and it
does not enter `/docs`.

## 4. The NULL rule

**NULL stays NULL.**

Not zero. Not "approximately." Not the midpoint of a range. Not the last known
value. Not the industry average. Not a placeholder to be corrected later.

An absent value is recorded as absent, with the search that failed to find it.

**Corollary — the error-vs-empty rule.** An error response is not an empty
result set. A 400, a 403, a timeout, or a 172-byte error object means *the
question was not answered*. It never means *the answer is none*. This rule
exists because it was nearly violated on 2026-08-20: a parcel query returned an
error object, was read as `parcels: 0`, and was briefly treated as evidence that
a company owned no land. See `research/ercot-audit-prospects/SITE_CONTROL_GAP.md`.

## 5. Repetition never increases confidence

Two copies of one source are one source.

Five law-firm alerts describing the same FERC order are five secondary
restatements of one primary document. They do not corroborate each other. They
share a single point of failure — the order — and if the order is misread, all
five are wrong together.

**Two trackers reporting different numbers for the same phenomenon are not
corroboration and not contradiction.** They are usually two different
definitions, and the correct response is to record both definitions and classify
the claim CONTEXT-DEPENDENT. On 2026-08-20 two data-center-restriction trackers
differed by a factor of 35 for this reason.

**Independence test:** if source B would still say what it says had source A
never existed, B is independent. Otherwise B is a copy.

## 6. Contradiction is preserved, never resolved silently

When two sources conflict, both are recorded, with tiers and dates. The conflict
is a finding. It is not cleaned up, averaged, or decided by whichever source is
more convenient. If one is later shown wrong, the record shows both and shows
why.

## 7. Capacity vocabulary

These six words are not interchangeable. Most bad power-path diligence is one of
them being silently substituted for another.

**Generation capacity** — the maximum electrical output a generating facility
can produce, in MW. A property of the machine. Says nothing about whether that
output can reach anyone.

**Transmission capacity** — the maximum power that can flow across high-voltage
lines (in this work, generally >69 kV) between two points, in MW. Constrained by
thermal limits, stability limits, and contingency planning. A property of the
network, not of any one line.

**Distribution capacity** — the maximum power deliverable across the
lower-voltage system that serves end customers. Distinct from transmission in
ownership, tariff, regulator, and planning horizon. A site adjacent to a
transmission line may have no distribution path, and vice versa.

**Substation capacity** — the maximum power that can pass through a specific
substation, set by its transformers, breakers, buswork, and protection scheme.
A real, physical, location-specific number. This is copper.

**Transformer capacity** — the nameplate rating of an individual transformer, in
MVA, with a distinct thermal rating that varies by ambient conditions and
loading history. Transformers are the single longest-lead item in most
interconnection paths. **Availability of a transformer is a schedule fact, not a
capacity fact, and the two are routinely conflated in marketing materials.**

**Interconnection capacity** — the amount of service established in an executed
Interconnection Service Agreement at a specific Point of Interconnection. A
**contractual** quantity that references physical facilities. It is not the
physical capability of those facilities, and it is not transferable merely
because the facilities are.

### Firm vs non-firm

**Firm** service is not curtailable except under defined emergency conditions
set out in the tariff. **Non-firm** service is curtailable at the transmission
provider's discretion under conditions the tariff defines. The MW number can be
identical and the asset value can differ by an order of magnitude. **A capacity
figure without its firmness is not a capacity figure.**

### Historical load vs deliverable load

**Historical load** is what a site actually drew, as metered, over a stated
period. It is evidence about the past.

**Deliverable load** is what a site may draw today under current agreements and
current system conditions.

These are routinely conflated in the retired-industrial reuse story — "this mill
drew 200 MW" is offered as though it means "this site can serve 200 MW." It does
not. The mill's service may have been terminated, the interconnection agreement
surrendered, the transformers removed, the line rebuilt to a lower rating, or the
surrounding network reconfigured so the same injection point now creates a
constraint it did not create before. **Historical load is a lead, not a
finding.**

### Physical interconnection asset vs contractual interconnection right

This distinction is the thesis. It gets the most words.

A **physical interconnection asset** is matter: the switchyard, the breakers,
the transformers, the takeoff structure, the conductor, the right-of-way, the
graded and permitted land under all of it, and the studied electrical position
in the network. It does not expire. It is not assignable in the contractual
sense because it does not need to be — it is conveyed with the real property,
subject to whatever easements and agreements encumber it.

A **contractual interconnection right** is a promise: service established in an
executed ISA or GIA at a Point of Interconnection, in a stated MW quantity, at a
stated firmness, subject to the tariff.

They are usually described with the same number and they behave completely
differently:

- **Rights are tied to a named resource, and they can die on a clock.** PJM's
  tariff, verbatim: *"A Generating Facility receiving Surplus Interconnection
  Service may continue to receive Surplus Interconnection Service for a period
  not to exceed one (1) year after the existing Generating Facility's
  Deactivation Date"* — and only if the surplus unit was studied for sole
  operation at the Point of Interconnection *and* the incumbent owner agrees in
  writing.
- **Rights, under Surplus Interconnection Service, run to generators only.** The
  tariff's recipient is *"A Generating Facility."* A data center is load. **Load
  cannot take Surplus Interconnection Service at all.** Any pitch that a site
  "inherits the plant's interconnection" for a data center is, on its face,
  describing something the tariff does not provide.
- **Copper does not care who owns it.** Homer City's 3,200-acre former coal site
  retained interconnections into both PJM and NYISO, and the redevelopment is
  building 4.5 GW of *new* gas generation against that position. TeraWulf's Lake
  Mariner leases 180 acres of a former coal campus for its dual 345 kV lines.
  In both cases what carried across was the physical position, not the retired
  unit's service.

**Operating rule:** when a document says "interconnection," determine which of
the two it means before doing anything else. If it means the right, find the
agreement and read its termination and assignment provisions. If it means the
asset, go look at the asset. If the document does not permit the distinction to
be made, that ambiguity is itself the finding.

## 8. Vendor-address suppression

Entity records frequently list a registered agent's address, a law firm's
address, or a filing service's address rather than the entity's own. An address
shared by many unrelated entities is a vendor address and is suppressed rather
than treated as a location. Failing to suppress produces false affiliation
clusters. See `research/ercot-audit-prospects/AFFILIATION_FINDINGS.md`.

## 9. What this file does not do

It does not catalog sources — that is M-PP-03. It does not define a claim
schema in machine-readable form — that is M-PP-04. It does not specify storage.
Nothing in this repository is authorized to build any of those before the rung
that names them.
