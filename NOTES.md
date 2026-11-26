# NOTES — The Internet in One Word (u-ronigrv-the-internet-in-one-word-e388f33b)

- Bounty: "The Internet in One Word", $10 total ($5/$3/$2), free entry.
- Opened 26 Nov 2026 06:14 WIB. Entries close 27 Nov 2026 00:15 WIB.
- Blind rounds (3): R1 cutoff 26 Nov 12:14 WIB, R2 18:14 WIB, R3/final 27 Nov 00:15 WIB.
- Field at build time: 45 entries. Harness program/v1; program writes one
  word to /output/entry.txt (UTF-8, 1–30 chars). Judge z-ai/glm-5.3-flash,
  pairwise, no ties; 3 Swiss rounds + top-5 playoff.
- Quota at build (06:3x WIB 26 Nov): entries_made 0, day cap 5 left,
  hard limit 40 left, can_submit true, blind_round_slot available.
- Entry word: "Receipts" (see STRATEGY.md). v2 candidate if R1 ranks low:
  "Groupchat".

## Build log

- 26 Nov 2026 ~06:35 WIB: repo created (after opening), v1 built in a
  fresh in-window session. main.py + tests + STRATEGY.md + README + LICENSE.
- Kit: fresh download, u-ronigrv-the-internet-in-one-word-e388f33b-kit.
- 26 Nov 2026 ~06:38 WIB: pushed commit
  dc6ea45d3f942b5f0a6f25694ed7e95d656203b6 (main). Repo About set
  (website = bounty page; topics makefun, ai-agents, bounties, growth).
- Local verify: python3 main.py writes exactly b'Receipts' (8 bytes);
  4/4 unit tests pass; stdlib only.
- Kit check (no transcripts): 4 pass (competition_open, snapshot 6 files /
  9,371 bytes, license_osi MIT, entrypoint main.py python3.13), 1 fail
  (transcripts_present — no bundle yet), 14 skipped, 5 at-submission.
- Bundle --dry-run: 11 Muse app sessions found, 0 usage rows attached.
  NOT bundled for real — parent re-bundles with --muse-usage after this
  subagent run completes (its usage row is written only then).
  Pre-opening sessions correctly left out (thinking_in_window).

## Live score / rank

- SUBMITTED 26 Nov 2026 ~09:56 WIB on Joni's 'Setuju, submit Receipts'
  (09:51:14 WIB). Submission 01a215c7-d8d4-702d-86d0-9a067e1b5d51,
  commit 6566e175, title "Receipts", stage checked (all checks pass).
  Claim saved to ~/.config/makefun/u-ronigrv-the-internet-in-one-word-e388f33b-submission.json (0600).
- source_withheld: FALSE (open) — the repo has no .makefun/freshness.json
  beacon root (not created with `makefun init`), so a --source submit was
  impossible; submitted via --repo-url. Future entries that must withhold
  source need a repo created with `makefun init` (root commit holds only
  the freshness file).
- Blind rounds (3): R1 cutoff 26 Nov 12:14:44 WIB, R2 18:14:52 WIB,
  R3/final 27 Nov 00:15 WIB. Judged: 0 so far; entry counts from R1.
  No score/rank yet; check GET /api/competitions/<slug>/rounds after R1.
  Blind rounds carry no written judge reasons (scores: [] at submit).

## v2 — "Groupchat" (build 26 Nov 2026 ~14:20 WIB)

- WHY v2: v1 word "Receipts" (submission 01a215c7-d8d4-702d-86d0-9a067e1b5d51)
  was EXCLUDED from R1 — another account submitted "Receipts" earlier, so
  our entry takes no place in any round. v2 must use a DIFFERENT word.
- v2 word: "Groupchat" (9 chars, Python len 9). Pre-chosen v2 candidate from
  v1 STRATEGY.md. One specific detail no other entry has: the typing dots
  ("Someone is typing…" — three dots that appear, vanish, reappear, never
  send). See STRATEGY.md for the full judge-criteria case.
- Fresh re-authoring (NOT a one-word edit of v1): main.py restructured into
  check_word / resolve_output / write_word helpers; tests rebuilt (6 tests:
  exact word, no trailing newline, gate, single word, argv override,
  deterministic two runs); STRATEGY.md + README.md rewritten for Groupchat.
  Each file written in 2 messages (thinking_revised).
- Local verify: python3 main.py writes exactly b'Groupchat' (9 bytes, no
  trailing newline); 6/6 unit tests pass; stdlib only.
- Entries close 27 Nov 2026 00:15 WIB; R2 cutoff 26 Nov 18:14:52 WIB.
  v2 built for Joni's 'Setuju' BEFORE submit — do NOT submit without it.
- v1 claim file ~/.config/makefun/u-ronigrv-the-internet-in-one-word-e388f33b-submission.json
  untouched; v2 gets its own versioned claim file only AFTER submit.
