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

- Not submitted yet — awaiting Joni's 'Setuju'. (Blind rounds: no live
  rank/score shows until a round is judged; check
  GET /api/competitions/<slug>/rounds after R1.)
