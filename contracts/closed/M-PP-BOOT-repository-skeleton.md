# CONTRACT M-PP-BOOT — Repository Bootstrap (pre-Rung-0)

Status: CLOSED 2026-08-20

## OBJECTIVE
Create the power-path repository skeleton: git, GitHub remote, directory
structure, lean CLAUDE.md, and empty gated doc stubs. NO product code,
NO schemas, NO dependencies. M-PP-00 lands on this skeleton next session.

## CONTEXT
- Solo founder, contract-driven development, fresh session per contract.
- Sibling repo pattern: the-registry-signal (same owner P9428).
- This repo will import Reality Infrastructure (RI) as a library later;
  do NOT vendor or install it now.
- Ladder: M-PP-00 -> M-PP-17 with sales stophook gates A/B/C.

## SCOPE
1. git init, branch main.
2. Create GitHub repo, private, push.
3. Directory skeleton, each with .gitkeep: /agents /workflows /tools /data
   /sources /evals /prompts /schemas /models /research /reports /deals
   /monitoring /tests /docs /scripts /contracts /contracts/closed
4. /docs stubs, one line each: "Populated by M-PP-00. Do not edit before
   that contract." Files: THESIS.md, ASSUMPTIONS.md, DECISION_LOG.md,
   SOURCE_OF_TRUTH.md, ARCHITECTURE.md, ROADMAP.md
5. /contracts/LADDER.md: M-PP-00 -> M-PP-17 with three gates marked:
   GATE A (before M-PP-08): >=15 outreach messages sent and logged
   GATE B (before M-PP-11): 1 paid memo delivered, outcome logged
   GATE C (before M-PP-16): >=10 delivered memos with logged outcomes
6. CLAUDE.md - lean IF-ELSE directory only, max ~25 lines.
7. .gitignore: node_modules, .env*, __pycache__, .venv, *.log, .DS_Store
8. README.md: name, one-sentence purpose, pointer to /contracts/LADDER.md.

## CONSTRAINTS
- No package.json, no requirements.txt, no migrations, no source code.
- No edits to any other repo.
- Nothing in /docs beyond the stub lines specified.

## CLOSEOUT NOTES
- STOP CONDITION HIT: `gh` CLI was not installed on this machine. SSH to
  GitHub authenticated as P9428 and `git ls-remote` confirmed no name
  collision. Operator ruled option 2 on 2026-08-20: operator created the
  empty private repo in the GitHub UI; skeleton pushed over SSH. The
  `gh repo view` acceptance check was replaced by `git ls-remote`.
- Rung titles in LADDER.md were set from the M-PP-BOOT research pass, not
  supplied by the contract. Gate positions are as specified.
- This file is an in-scope addition: prior precedent (M-RI-12) recorded a
  contract whose text existed only in-session and was nearly lost.
