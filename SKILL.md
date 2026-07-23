---
name: poe2-loot-filter
description: Maintain and iterate Scott's shared Path of Exile 2 loot filter for his duo with his friend. Use this skill whenever Scott mentions PoE2, loot filters, .filter files, item priorities, what to pick up or hide, FilterBlade, NeverSink, waystones, runes, or asks to adjust what his filter shows — and also when he reports a level-up, a build change, a new weapon, or a change in what he's farming, since all of those require filter revisions. Trigger this even if he doesn't say the word "filter."
---

# PoE2 Shared Loot Filter

Maintains one shared `.filter` file for Scott + his duo partner in Path of Exile 2.
This is a living document. Every session should leave `references/characters.md`
and `current-filter/shared.filter` more accurate than it found them.

## Start every session by doing this

1. **Read `references/characters.md`.** That's the source of truth for both builds.
2. **Refresh levels and gear.** Once both characters are level 80+, fetch their
   poe.ninja profiles (URLs stored in characters.md) — this gives level, gear,
   gems, and passives without asking. Below level 80 poe.ninja won't index them;
   just ask Scott directly.
3. **Ask what changed since last time.** Build swaps, new weapon, different
   farming strategy, "I keep missing X" — these are the actual drivers of edits.
4. **Read `current-filter/shared.filter`** before editing anything.

Do not regenerate the filter from scratch each session. Edit the existing draft.
The whole point of this skill is continuity.

## Locked design decisions

These were settled deliberately. Don't relitigate them without cause.

**One shared filter, not two.** They play together almost always and split loot
loosely by need. Two separate filters means each player is blind to half the
party's upgrades. One file shows both builds' gear, visually coded so you can
tell at a glance whose it is.

**Level awareness comes from `AreaLevel`, not character level.** Filters cannot
read character level — only the level of the zone the item dropped in. This is
better anyway: loot relevance tracks zone level, not player level. Build banded
rules and the filter adapts on its own as they climb tiers, with zero manual
edits. Character level only matters as context for tuning priorities.

**Trade softcore, "some of both" on crafting.** Keep ilvl 81/82 bases, essences,
and omens visible but tiered hard. Not the extremes of showing every white base
(clutter) or hiding all crafting fodder (missed value).

## AreaLevel bands

The spine of the filter. Every progression-sensitive rule belongs to a band.

| Band | Context | Posture |
|---|---|---|
| `< 65` | Campaign | Permissive. Keep minimal but functional so a fresh alt isn't blind. |
| `65–74` | Early maps | Permissive. **Both players are here now.** Show upgrades generously. |
| `75–79` | Mid maps | Tighten. Start hiding low-tier bases and common currency. |
| `>= 80` | High maps | Strict. Focus on ilvl 81/82 bases and top-tier drops. |
| `>= 82` | Peak bases | Special highlight — best crafting bases in the game. |

Precedent: NeverSink's PoE2 filter uses AreaLevel 65 as the campaign/endgame
boundary and gives dedicated treatment at 82. Following that convention keeps
our filter legible to anyone who knows the ecosystem.

When Scott says "I'm hitting T15s now," that does **not** mean edit the filter —
the bands already handle it. It means verify the 80+ band is tuned right.

## Character-specific overrides

The reason this filter exists rather than just using NeverSink stock. See
`references/characters.md` for the full build detail; these are the filter
consequences.

**Runes / socketables are elevated for Scott.** Martial Artist is the only
ascendancy that can house additional runes in his body. Stock filters tier
runes, soul cores, and talismans as one generic economy group — correct for
most classes, materially under-tuned for him. Socketables get a higher tier,
larger font, minimap icon, and beam than a default filter would assign.

**Armour-only bases are near-dead weight for Scott.** Monk is Dex/Int, so
Evasion and Evasion/Energy Shield hybrid bases matter; pure Armour (Str) bases
are effectively vendor trash for him. This kills a large slice of rare drops —
but only hide them if they're also dead for the partner's build. Check
characters.md before hiding any defence type.

**Gloves need special handling.** Martial Artist has a glove transformation
mechanic. Do not fold gloves into generic armour rules.

## Rule ordering discipline

**First match wins.** Rules evaluate top to bottom and stop at the first block
that matches, unless that block ends with `Continue`. This is the single most
common source of bugs.

Known trap, documented on NeverSink's own repo: FilterBlade's SIMULATE preview
can show a later custom Show rule making an item visible while the compiled
filter — and the actual game — stop on an *earlier* Hide rule that lacks
`Continue`. **The preview lies.** After any structural change, verify by reading
the compiled file top-down, not by trusting the simulator.

Ordering convention for this filter, top to bottom:

1. Safety net — quest items, anything unrecognised (loud pink/cyan so it's obvious)
2. Currency and socketables, highest tier first
3. Uniques
4. Waystones (banded by tier vs. current mapping tier)
5. Build-critical bases — Scott's, then partner's
6. Generic gear catch-alls, banded by AreaLevel
7. Explicit hides, most specific first

Decorator rules that only add a border or beam should use `Continue` so they
stack rather than terminating the match.

## Visual language

Keep it consistent and low-cognitive-load. Whoever's item it is should be
readable at a glance in a party.

- Reserve a distinct border colour per player for build-specific gear so they
  can tell whose upgrade dropped without reading the item.
- Beams (`PlayEffect`) and minimap icons (`MinimapIcon`) are for things worth
  crossing the room for. Overuse destroys their signal value.
- Sounds are for the top tier only. `PlayAlertSound` on too many rules is worse
  than none.

## Delivery

Three paths, in order of how much setup they need:

1. **Copy the file into the game folder.** On Scott's Mac (CrossOver), run
   `./scripts/install.sh` — it copies `shared.filter` into
   `~/Documents/My Games/Path of Exile 2/` (the CrossOver bottle symlinks its
   Documents there, so the game reads it straight from that Mac path). On
   Windows the folder is `%userprofile%\Documents\My Games\Path of Exile 2\`.
   Then in game: Options → Game → Item Filter → "shared" → Reload. The game
   does **not** hot-reload — hit Reload after every edit or you're testing the
   old file. Note: the game never reads filters from the install directory
   (`Program Files\...\Grinding Gear Games\`); a copy left there does nothing.
2. **FilterBlade** for visual preview and tweaking. Good for sanity-checking
   appearance; remember the SIMULATE caveat above.
3. **API push** (optional, needs OAuth setup Scott hasn't done):
   `POST /item-filter` with `realm: "poe2"` and `?validate=true` validates
   against the current game version and puts the filter on his account.
   `POST /item-filter/<id>` for partial updates.

In game, holding Alt reveals everything the filter is hiding — the fastest way
to check we haven't hidden something important.

## When to update what

| Scott says | Action |
|---|---|
| "I leveled" | Nothing. Bands handle it. Update characters.md. |
| "I'm in T15s now" | Verify the 80+ band, don't add rules. |
| "Swapped to X weapon" | Real edit. Update build-critical bases. |
| "I keep missing Y" | Find the rule that's hiding it — check ordering first. |
| "Too much clutter" | Tighten the *current* band only, not all bands. |
| "Friend rerolled" | Rewrite his half of characters.md, then his gear rules. |

## Files

- `references/characters.md` — both builds, levels, poe.ninja URLs, gear goals.
  Update this every session.
- `current-filter/shared.filter` — the working filter. Edit in place.
