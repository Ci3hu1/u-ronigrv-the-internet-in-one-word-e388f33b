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

## v2 bundle + kit check (26 Nov 2026 ~14:22 WIB)

- Commit: 3f48468 "The Internet in One Word v2: Groupchat" (5 files, +165/-72).
  Local HEAD verified. **PUSH FAILED — commit NOT on remote.**
  - `git push origin main` failed 3x: "error: RPC failed; curl 56 Connection
    died, tried 5 times before giving up / send-pack: unexpected disconnect
    while reading sideband packet / fatal: the remote end hung up
    unexpectedly". `git ls-remote origin HEAD` also failed (exit 128,
    "fatal: expected flush after ref listing"). SSH to github.com also
    blocked (proxy 198.19.0.1:3128 resets connection). Plain HTTPS works
    (curl github.com 200; gh API works).
  - Verified via `gh api repos/Ci3hu1/u-ronigrv-the-internet-in-one-word-e388f33b/git/refs/heads/main`:
    remote HEAD is still 6566e175b1f83802f619170b6c8db66c53a33443 (v1).
    **Parent must retry the push before submit** (git protocol worked
    earlier today for v1 + news-image v5, so this is likely transient).
  - commit_in_repo (submission phase) confirms: 3f48468 must be pushed
    before submit.
- Bundle: ~/workspace/tools/makefun/bundles/u-ronigrv-the-internet-in-one-word-e388f33b-v2-bundle.tar.gz
  — 127,054 B, sha256 8f8f803d0e95ebdf1c0ee860174a8ee9891fc01a683cb6920902f345e0419864.
  Built with --session <this session file> --no-discover --prompt-file
  (verbatim standing order) --prompt-origin scheduled --prompt-via
  'scheduled 30-min check run' --mcp none --provider meta --effort default.
  (First bundle attempt refused: missing --mcp/--provider/--effort; the
  flags above fixed it. Harness/version/model were recorded by the session.)
- Kit check (commit 3f48468 + bundle, --transcripts): **13 pass / 1 fail /
  5 skip / 5 submission** (24 total). Pass: competition_open, snapshot,
  license_osi, entrypoint, transcripts_present, transcripts_recorded,
  thinking_wellformed, thinking_in_window, thinking_reproduces,
  thinking_turns, thinking_revised, transcripts_run_record,
  thinking_own_work (126/225 lines authored = 56%, 0 from other entries).
  Skip: strategy_note, committed_secret, thinking_committed,
  thinking_on_task, thinking_fresh. Submission (site checks at submit):
  repo_public, repo_owner, repo_created_after_open, commit_in_repo,
  duplicate_snapshot. **FAIL: thinking_priced only** — "1 Muse app session
  carries 0 usage rows, at least 1 required" (expected: usage rows appear
  only when this subagent run completes; parent re-bundles with
  --muse-usage after this run, as with v1).
- NOT submitted. Awaiting Joni's 'Setuju' on v2 'Groupchat' before submit.
  v1 claim file untouched.

## v2 re-bundle + kit check (parent, 26 Nov 2026 ~14:47 WIB)

- Push blocker RESOLVED: `git push origin main` succeeded on retry (6566e17..3f48468 main -> main). Verified via `git ls-remote origin HEAD` = 3f48468bb2c23718a34b181cc48db9f7c6fa7a7d. The earlier proxy/connection failure was transient.
- Builder identified: agent efcaff5a-9b0f-4ee6-b749-4ec5a983a969 (model ipnext/avocado-5.17-v2); usage row from muse.db (1 row: input 3,985,044 / output 28,653, message 58070ad8-e8c2-4c4b-8e30-fb1ce085dd97) written to ~/.makefun/muse-usage-u-ronigrv-the-internet-in-one-word-e388f33b-v2.jsonl (0600).
- Re-bundle (parent): same flags as builder + --muse-usage. New bundle ~/workspace/tools/makefun/bundles/u-ronigrv-the-internet-in-one-word-e388f33b-v2-bundle.tar.gz — 137,435 B, sha256 28bb925e93dd23bb008287e6c6e9434ed35e03bb641d769777e43b3bd089472f (was 127,054 B / 8f8f803d). Usage row attached (1 row).
- Kit check (commit 3f48468 + new bundle, --transcripts): **failed [] / ok true — thinking_priced now PASSES.** All 14 local checks pass; 5 submission-phase checks (repo_public, repo_owner, repo_created_after_open, commit_in_repo, duplicate_snapshot) are server-verified at submit. Note: kit copy level 50 vs site level 53 — check still passes; no re-download needed.
- NOT submitted. Awaiting Joni's 'Setuju' on v2 'Groupchat' before submit. R2 cutoff 18:14 WIB 26 Nov; entries close 27 Nov 00:15 WIB.

## v2 SUBMITTED — 26 Nov 2026 ~14:39 WIB (Joni: 'Ya, submit v2 Groupchat' 14:38:10 WIB)

- Submission **01a216cb-20cb-75dd-91e9-83b4c21a65b4**, title 'Groupchat', round 2 of 3 (counts from R2). Repo https://github.com/Ci3hu1/u-ronigrv-the-internet-in-one-word-e388f33b, commit 3f48468bb2c23718a34b181cc48db9f7c6fa7a7d. Bundle 137,435 B, sha256 28bb925e93dd23bb008287e6c6e9434ed35e03bb641d769777e43b3bd089472f (parent re-bundle).
- Stage check: **stage 'scored', problem null — 29 checks: 27 pass / 2 skip (thinking_on_task, thinking_fresh) / 0 fail.** thinking_priced PASS, thinking_reproduces PASS, commit_in_repo PASS, duplicate_snapshot PASS. Entry accepted, will be judged in R2.
- Blind rounds: no live score/rank yet — score shows after R2 is judged (cutoff 18:14:52 WIB 26 Nov). Check via `makefun rounds u-ronigrv-the-internet-in-one-word-e388f33b` after R2.
- Claim saved to NEW versioned file ~/.config/makefun/u-ronigrv-the-internet-in-one-word-e388f33b-v2-submission.json (0600). v1 claim file untouched (01a215c7).
- Deadlines: entries close 27 Nov 00:15 WIB (2026-11-26T17:15:00Z); results due 18 Dec 2026. Payout wallet h7aEYozd3ouRt11uqdJC8cQ42hHRckuFotiEvuJbuhE.

## 26 Nov 18:30 WIB — R2 rank check (job runonce)
- `makefun.mjs rounds` — R2 masih judging (cutoff 18:14 WIB). judged=1, ranked=[398, null, null]. R2 belum ada rank/score untuk v2 'Groupchat' (01a216cb). Tidak ada pesan ke Joni; hasil final 18 Des.

## v3 — "Ghosted" (build 26 Nov 2026 ~19:35 WIB)

- WHY v3: v1 word "Receipts" (01a215c7) was EXCLUDED from R1 and v2
  "Groupchat" (01a216cb) was EXCLUDED from R2 — in both cases another
  account submitted the same word earlier. v3 enters from R3 (final
  round). v3 must use a DIFFERENT word, checked against the field
  first: 0 of 2,978 submission titles contain "Ghosted".
- v3 word: "Ghosted" (7 chars, Python len 7). One specific detail no
  other entry has: the read receipt ("Seen 23:41" — and then nothing,
  forever). See STRATEGY.md for the full judge-criteria case.
- Fresh re-authoring (NOT a one-word edit of v2): main.py, tests,
  STRATEGY.md, README.md rewritten for Ghosted.
- Local verify: python3 main.py writes exactly b'Ghosted' (7 bytes, no
  trailing newline); 6/6 unit tests pass; stdlib only.
- Entries close 27 Nov 2026 00:15 WIB; R3/final cutoff 27 Nov 00:15 WIB.
  v3 built for Joni's 'Setuju' BEFORE submit — do NOT submit without it.
- v1/v2 claim files untouched; v3 gets its own versioned claim file
  only AFTER submit.
