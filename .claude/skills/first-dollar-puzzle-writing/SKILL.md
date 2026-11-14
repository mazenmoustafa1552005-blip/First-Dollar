---
name: first-dollar-puzzle-writing
description: Use when writing or revising a printable kids' mystery game (ages 8-12) for the studio - story, suspects, clue logic, timed hints and solution - and when running the independent blind-solve check.
---

# Mystery game writing and puzzle logic

## Content module
Each game is one Python data module `scripts/mystery_content_<key>.py` (copy `mystery_content_bday.py`). Register it in `GAMES` inside `scripts/mystery_build.py`. Build: `python3 scripts/mystery_build.py --game <key>`.

## Logic rules (must hold before build)
- Write the logic design in the module docstring: culprit, the 3 hard clues (K1-K3) and, for EVERY innocent, at least one hard clue that eliminates them.
- No colour-only clues: every colour is also written in words (B&W ink-saver version must be equally solvable).
- Round 1 alone must not identify the culprit for ages 11-12; the decisive combination should need Round 2 or 3.
- Red herrings must be resolvable by evidence, never by "the host says so".
- Hints are ordered gentle to strong, minute-stamped (15/30/40 for a 45-60 min game).
- Kid-safe: no murder, no injury, no scary content; motive is gentle (protecting, surprising, mix-up).
- US English spelling for the international catalog.

## Variety across the line
Each new game must change: setting/occasion, culprit archetype (not always the youngest child), the clue mechanics (e.g. timeline, measurement, code/cipher, map, sound) and the solution location. Record the mechanics in the backlog to avoid repeats.

## Independent blind solve (required)
1. `pdftotext -layout` the PrintPack and the host-guide intro page into the scratchpad.
2. Spawn a fresh subagent that may read ONLY those text files and must solve WHO/WHERE/3 clues, judge uniqueness, flag colour-only clues and confusing wording, and play round by round.
3. Record the result in `products/<SKU>/qa/blind-solve.md`. Fix issues, rebuild, re-run with a NEW subagent.
4. A blind solve is not a playtest. Status "playtested" requires a real group session logged by the owner.
