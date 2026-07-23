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
| Scott | Monk / **Martial Artist**, level 73 — **UNARMED**, Hollow Focus (bells) + Way of the Stone Fist |
| Partner | Sorceress / **Disciple of Varashta**, level 73 |
| Progress | Just hit endgame, early waystones |
| Filter | v1.1.0 — **still not play-tested** |

**No version has been run in a map yet.** No tuning feedback exists yet. The first
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
- **Gloves are Scott's weapon, not armour.** Way of the Stone Fist converts them
  to Fists of Stone with its own Evasion/ES and rewritten modifiers, so base
  defence type is irrelevant. **Never add `Gloves` to the pure-Armour `Hide`** —
  that was a real bug fixed in v1.1.0.
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
./scripts/install.sh                 # copy filter into the live PoE2 folder, then Reload in-game
git add -A && git commit -m "..."
git tag -a v1.1.0 -m "..."           # tag every filter change
git push --follow-tags
```

`install.sh` copies to `~/Documents/My Games/Path of Exile 2/` (Scott's
CrossOver bottle symlinks its Documents there). The game does **not** hot-reload
— always Reload in-game after running it. Override the destination with
`POE2_FILTER_DIR=... ./scripts/install.sh`.

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

Both builds are confirmed as of 2026-07-23. No open build gaps.

- Scott — unarmed, bells (Hollow Focus), Way of the Stone Fist; quarterstaff later.
- Partner — Sorceress / Disciple of Varashta, **pure caster, not minions**.
  Sceptres stay live regardless: they grant Spirit, which casters use for
  auras/heralds. Only revisit if play-test shows she reserves zero Spirit.

The next input the filter needs is **play-test feedback**, not more build info.
If a deeper question ever arises, a Path of Building 2 export answers most at
once; a passive tree URL (`pathofexile2.com/game/passive-skill-tree/...`) is a
weaker second option — it decodes to node *hashes* needing a lookup table.

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
- **`BaseType` is the opposite of `Class` — a bad token is FATAL.** A `BaseType`
  string that matches no real base makes PoE2 refuse to load the *entire* filter
  ("Unable to parse parameter for BaseType rule"). So never add a speculative or
  unverified BaseType as a hedge; verify the exact base first. This shipped as a
  real bug in v1.2.0/v1.3.0 (`"Womb Gift"` two-word hedge) — see CHANGELOG v1.3.1.
  `validate.py` now guards against it: every BaseType token must be in the
  verified allowlist `references/base-types.txt`, or validation errors. Adding a
  new base means adding its verified token to that file.

## Files

| Path | Purpose |
|---|---|
| `current-filter/shared.filter` | The deliverable. Edit in place. |
| `references/characters.md` | Both builds. **Update every session.** |
| `references/item-classes.txt` | Verified Class names; validator ground truth. |
| `references/base-types.txt` | Verified BaseType tokens; validator allowlist. |
| `scripts/validate.py` | Pre-commit checks. Run before every commit. |
| `scripts/install.sh` | Copy the filter into the live PoE2 folder. Reload in-game after. |
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
