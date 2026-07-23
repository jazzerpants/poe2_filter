# PoE2 Shared Duo Filter

Version-controlled loot filter for a Monk/Martial Artist + Sorceress duo.
League: Runes of Aldur (0.5), Trade Softcore.

Filters are code. This repo exists so that "I liked it better before" is a
one-line fix instead of a rebuild.

## Layout

```
.
├── current-filter/
│   └── shared.filter        <- the live filter. This is the deliverable.
├── references/
│   ├── characters.md        <- both builds. Update every session.
│   └── item-classes.txt     <- verified PoE2 Class names (validator input)
├── scripts/
│   └── validate.py          <- pre-commit sanity check
├── SKILL.md                 <- workflow + design decisions
└── CHANGELOG.md             <- what changed in each filter version, and why
```

## Install

Copy `current-filter/shared.filter` into:

```
%userprofile%\Documents\My Games\Path of Exile 2\
```

In game: **Options → Game → Filters →** select it **→ Reload**.

The game does **not** hot-reload. Every edit needs a Reload or you are testing
the previous file. Hold **Alt** in game to reveal everything the filter hides —
the fastest way to confirm nothing important vanished.

## Live preview

`index.html` is an interactive viewer, published via GitHub Pages:

**https://jazzerpants.github.io/poe2_filter/**

It fetches `current-filter/shared.filter` at load time, so **the preview can
never drift from what is committed** — push a filter change and the preview
updates itself.

What it does:

- **Area level slider (60–84).** Scrub it and watch rules band in and out. This
  is the one thing that cannot be tested in game without physically travelling
  to differently-levelled zones.
- **Real rule engine.** Parses the filter and evaluates top-down with genuine
  first-match-wins and `Continue` semantics — so a broad `Hide` above a narrow
  `Show` shadows it here exactly as it does in game.
- **Tap any item** to see the rule block that caught it and its verdict.
- **"Show hidden (Alt)"** mirrors the in-game Alt key: hidden drops ghost out
  rather than disappearing.
- **Paste-to-test drawer** — preview a filter edit before committing it.

Source resolution order: same-origin relative path (Pages) → raw.githubusercontent
(CORS-enabled) → bundled fallback copy for offline use. The status dot under the
header shows which loaded.

### Enabling Pages (one time)

Repo **Settings → Pages → Source: Deploy from a branch → `main` → `/ (root)` → Save.**
First build takes a minute or two.

### Fidelity limits

PoE's Fontin typeface is not available on the web, so the viewer uses a serif
approximation and scales the 1–45 font range for screen. Relative sizes are
faithful; absolute pixels are not. Colours, borders, backgrounds, minimap icons
and beams are read verbatim from the filter.

The preview is a convenience. Ground truth is in game: drop the filter in,
Reload, run a map, hold Alt.

## Versioning workflow

Every meaningful filter change gets a tag, so any past version can be restored
and dropped straight into the game folder.

```bash
# after editing
python3 scripts/validate.py          # must pass before committing
git add -A
git commit -m "tighten rare display in 80+ band"
git tag -a v1.1.0 -m "Mid-map clutter pass"
```

### Rolling back

See what versions exist:

```bash
git tag -l -n1
```

Restore a previous filter *without* disturbing current work:

```bash
git show v1.0.0:current-filter/shared.filter > /tmp/rollback.filter
# then copy /tmp/rollback.filter into the PoE2 folder and Reload
```

Or go back properly:

```bash
git checkout v1.0.0 -- current-filter/shared.filter
```

Compare two versions to see exactly what changed:

```bash
git diff v1.0.0 v1.1.0 -- current-filter/shared.filter
```

### Version numbering

- **Major** (v2.0.0) — restructure, or a player rerolls
- **Minor** (v1.1.0) — new rules, retuned bands, changed priorities
- **Patch** (v1.0.1) — colour tweaks, font sizes, typo fixes

## Validation

`scripts/validate.py` catches the failure modes that break filters *silently* —
where the game throws no error and items simply stop appearing:

| Check | Why it matters |
|---|---|
| Unknown `Class` names | Typo = rule never matches, item invisible |
| Unlisted `BaseType` tokens | Bad token = game refuses to load the **whole** filter (not silent — this one is loud) |
| Unconditional `Show`/`Hide` | Swallows every rule below it |
| Broad `Hide` above narrow `Show` | First-match-wins shadowing |
| RGB outside 0–255 | Malformed colour |
| `SetFontSize` outside 1–45 | Clamped or ignored |

`BaseType` tokens are checked against an allowlist, `references/base-types.txt`,
because there is no ground-truth base list the way there is for classes. Adding
a new `BaseType` rule means verifying the exact spelling and adding the token to
that file — the guard exists so a speculative/unverified base can never ship
(it broke v1.2.0/v1.3.0; see `CHANGELOG.md` v1.3.1).

Run it before every commit. Wire it as a hook if you want it enforced:

```bash
printf '#!/bin/sh\npython3 scripts/validate.py || exit 1\n' > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

Refresh the class list when a new league lands and item classes change:

```bash
curl -sL "https://raw.githubusercontent.com/NeverSinkDev/NeverSink-Filter-for-PoE2/main/NeverSink's%20filter%202%20-%202-SEMI-STRICT.filter" -o /tmp/ns.filter
grep -oP '^\s*Class\s+[=!]*\s*\K.*' /tmp/ns.filter | grep -oP '"[^"]+"' | sort -u | tr -d '"'
```

## Working with Claude across sessions

The container Claude runs in resets between conversations — it cannot hold this
repo itself. Two things make continuity work anyway:

1. **Push this repo to GitHub.** Claude can read `raw.githubusercontent.com`
   directly, so at the start of any session it can fetch the current filter and
   `characters.md` without you re-explaining anything.
2. **Once both characters hit level 80**, add their poe.ninja URLs to
   `characters.md`. Claude can then pull live level, gear, gems, and passives.

With both in place, a session starts with Claude already knowing the current
state of the filter *and* both builds.

## Known caveats

- **FilterBlade's SIMULATE preview can lie.** It may show a later custom rule
  making an item visible while the compiled filter — and the game — stop on an
  earlier `Hide` without `Continue`. Verify structural changes by reading the
  file top-down, not by trusting the simulator.
- **Currency and unique tiering here is functional, not economy-accurate.**
  NeverSink runs live price data across ~5,300 lines. This filter's advantage is
  build specificity, not valuation. If currency handling becomes the weak point,
  restructure to run NeverSink as a base with these rules as an `Import`
  overlay.
- **The magenta/cyan catch-all at the bottom is deliberate.** Anything the
  filter does not recognise screams pink with a sound. That is the early warning
  that new league content is unhandled — do not silence it.
