# power-path — operating rules

Adversarial power-path diligence on physical infrastructure, RI-backed.

- IF authoring or executing a contract → read `/contracts/LADDER.md` first.
  Verify the prior contract is closed (moved to `/contracts/closed/`).
  If it is not closed, STOP and say so.
- IF a stophook gate (A/B/C) is not evidence-logged → REFUSE to author the
  gated contract. Say so plainly; do not author a partial substitute.
- IF touching schemas or data → read `/docs/SOURCE_OF_TRUTH.md` first.
- IF doing claim/evidence work →
  - NULL stays NULL. Never impute, never fill.
  - Every claim carries `source_url` + `observed_date`.
  - Repetition never increases confidence. Two copies of one source is one source.
- ONE contract at a time, completed end-to-end. No parallel rungs.
- Rules are preferences; skills are recipes. Inject only what the task needs.
- Reality Infrastructure is imported as a library, never vendored, never edited.
