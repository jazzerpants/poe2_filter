# CLAUDE.md

Orientation for Claude Code sessions on this repo. Read this first, then
`references/characters.md`.

## What this is

A shared Path of Exile 2 loot filter for Scott and one duo partner. They play
together almost always and split loot loosely by need, so this is **one filter
serving two builds**, not two filters.

The deliverable is `current-filter/shared.filter`. Everything else exists to
keep that file correct and to make its behaviour inspectable.

## Current state

| | |
|---|---|
| League | Runes of Aldur (0.5), Trade Softcore |
| Scott | Monk / **Martial Artist**, level 73 |
| Partner | Sorceress / **Disciple of Varashta**, level 73 |
| Progress | Just hit endgame, early waystones |
| Filter | v1.0.0 — **written but not yet play-tested** |

**v1.0.0 has never been run in a map.** No tuning feedback exists yet. The first
real session should be about what felt wrong in game, not about adding features.

## Start a session by doing this

1. Read `references/characters.md` — the source of truth for both builds.
2. **Refresh levels.** Once either character reaches 80 they get indexed on
   poe.ninja and their profile URL should be added to `characters.md`; fetch it
   for live level, gear, gems, and passives. Below 80, just ask.
3. Ask what changed and what felt wrong in game.
4. Read `current-filter/shared.filter` before editing it.

Edit the existing filter. **Do not regenerate it from scratch** — the reasoning
behind its current shape is in `CHANGELOG.md` and is easy to destroy by rewriting.

## Non-negotiables

Settled deliberately. Don't relitigate without new information.

- **One shared filter.** Separate filters would leave each player blind to half
  the party's upgrades.
- **Progression comes from `AreaLevel`, not character level.** Filters cannot
  read character level. Bands (`<65` / `65–74` / `75–79` / `80+`) mean the filter
  self-adjusts as they climb, with no manual edits. A level-up is **not** a
  reason to change the filter.
- **Socketables are elevated for Scott.** Martial Artist is the only ascendancy
  with extra body rune slots. Rune rules use substring `BaseType` matching (no
  `==`) deliberately, so runes added in future patches are caught automatically.
  Do not "tidy" this into an explicit list.
- **Str/Armour purge is safe *only* because both builds are Int-side.** Monk is
  Dex/Int, Sorceress is pure Int. If either player rerolls to a Strength build,
  the `Hide` rules on Armour bases and Strength weapon classes must be revisited
  first — they are the most aggressive rules in the file.
- **The magenta catch-all at the bottom stays.** Unrecognised items scream pink
  with a sound. That is the early warning that new league content is unhandled.

## Commands

```bash
python3 scripts/validate.py          # must pass before any commit
git add -A && git commit -m "..."
git tag -a v1.1.0 -m "..."           # tag every filter change
git push --follow-tags
```

A pre-commit hook is *not* installed on fresh clones. Install it once:

```bash
printf '#!/bin/sh\npython3 scripts/validate.py || exit 1\n' > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

Rolling back a filter without disturbing current work:

```bash
git show v1.0.0:current-filter/shared.filter > /tmp/rollback.filter
```

### Versioning

- **Major** — restructure, or a player rerolls
- **Minor** — new rules, retuned bands, changed priorities
- **Patch** — colours, font sizes, typos

Docs-only changes get a normal commit and **no tag**.

## Open questions — ask Scott

These are genuinely unresolved and affect filter tuning:

- **Scott's weapon.** Quarterstaff is *assumed* and baked into ~4 rules. Not
  confirmed. Martial Artist also has a glove transformation mechanic, so the
  assumption is not free.
- **Which Hollow Technique** Scott's build centres on — bells, clones, or the
  rune-defensive path. Determines crit-heavy vs defensive base priorities.
- **Partner: summoner-leaning or pure caster?** Disciple of Varashta supports
  both — some nodes let her skip summoning entirely. Affects how hard to
  prioritise Sceptres and Spirit-granting gear.

A Path of Building 2 export code from either player would answer most of this at
once. A passive tree URL (`pathofexile2.com/game/passive-skill-tree/...`) is a
weaker second option — it decodes to node *hashes*, which need a lookup table to
become names.

## Gotchas

- **First match wins.** Rules evaluate top-down and stop at the first matching
  block unless it ends with `Continue`. This is the most common source of bugs
  in this file. Decorator rules that only add a border or beam must use
  `Continue` or they will terminate the match.
- **FilterBlade's SIMULATE preview can lie.** It may show a later rule making an
  item visible while the compiled filter and the actual game stop on an earlier
  `Hide` without `Continue`. Verify structural changes by reading the file
  top-down.
- **The game does not hot-reload.** Every edit needs Options → Game → Filters →
  Reload, or the previous file is still active. Filter lives in
  `Documents\My Games\Path of Exile 2\`.
- **Holding Alt in game reveals everything hidden.** Fastest way to confirm
  nothing important vanished. This is ground truth; the preview is convenience.
- **Item Class names must be exact.** A typo produces no error — the rule simply
  never matches and the item silently disappears. `validate.py` checks these
  against `references/item-classes.txt`. Refresh that list when a new league
  changes item classes (command in `README.md`).

## Files

| Path | Purpose |
|---|---|
| `current-filter/shared.filter` | The deliverable. Edit in place. |
| `references/characters.md` | Both builds. **Update every session.** |
| `references/item-classes.txt` | Verified Class names; validator ground truth. |
| `scripts/validate.py` | Pre-commit checks. Run before every commit. |
| `index.html` | Live preview, served via GitHub Pages. |
| `SKILL.md` | Fuller workflow and design rationale. |
| `CHANGELOG.md` | What changed per version and **why**. Keep the why. |

## Preview

`index.html` is published at **https://jazzerpants.github.io/poe2_filter/**
(Settings → Pages → Deploy from branch → `main` → `/ (root)`).

It fetches `current-filter/shared.filter` at load, so it cannot drift from what
is committed. The area-level slider is the point of it — it makes the band
system visible, which is the one behaviour that cannot be tested in game without
travelling to differently-levelled zones.

## Scope

This filter competes on **build specificity**, not economy valuation. NeverSink
runs ~5,300 lines with live price data; don't try to match that. If currency or
unique tiering becomes the weak point, the right move is restructuring to run
NeverSink as a base with these rules as an `Import` overlay — not hand-tiering
currency here.
