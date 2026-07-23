# Changelog

Filter versions and the reasoning behind them. Record *why*, not just what —
the reasoning is what prevents relitigating settled decisions later.

---

## Unreleased — folded into v1.1.0

### Changed

- **Partner ascendancy confirmed: Disciple of Varashta** (Sorceress, added in
  0.4 Last of the Druids). Recorded in `references/characters.md`.

**No filter changes required — v1.0.0 already handles this build correctly.**
Verified rather than assumed:

- Energy Shield priority confirmed by the ascendancy's own design (Navira grants
  ES recovery; The Fourth Teaching grants 40% more ES Recharge Rate on low ES).
  Existing ES-first armour rules are right.
- **`Staves` must stay in her weapon rules.** An ascendancy node allows wielding
  a Staff and Focus *together*. This closes the v1.0.0 open question about
  trimming `Staves` for clutter reduction — the answer is no.
- `Sceptres` stay live; they grant Spirit, relevant if she leans summoner.
- One node converts Energy Shield to Armour. She would still want ES bases,
  which then convert — not Armour bases. The pure-Armour `Hide` remains correct.

### Still open

- Whether she plays summoner-leaning or pure caster. The ascendancy supports
  both (Instruments of Power / Baryanic Leylines allow skipping summons
  entirely), so it can't be inferred from the ascendancy alone.
- Scott's weapon (quarterstaff assumed) and which Hollow Technique he centres on.

---

## v1.3.1 — 2026-07-23

Hotfix — v1.3.0 (and v1.2.0) failed to load in-game.

### Fixed

- **Wombgift rule broke the whole filter.** The rule matched
  `BaseType "Wombgift" "Womb Gift"` — the two-word `"Womb Gift"` was a
  speculative hedge against an unknown spelling. It matches no real base, and
  **PoE2 hard-errors on a `BaseType` token that matches nothing** ("Unable to
  parse parameter for BaseType rule"), refusing to load the entire filter.
  Removed the bad token; the correct base is one word (`Wombgift`, substring-
  matching "Lavish Wombgift" etc.).

**Lesson for future rules:** `BaseType` is *not* like `Class`. A bad `Class`
name silently never matches (CLAUDE.md gotcha); a bad `BaseType` token **fails
the whole filter to load**. Never add speculative/unverified `BaseType` strings
as a hedge — verify the exact base first. `validate.py` does not catch this (it
checks Class names, not BaseType strings), so a bad BaseType passes validation
and only surfaces in-game.

---

## v1.3.0 — 2026-07-23

Two additions from play-test feedback. Both surface items that were being
hidden.

### Added

- **Ultimate life/mana flasks now show.** The filter had *no* flask rule, so
  every flask fell to the Normal/Magic map Hide. Added a Show rule for the two
  top-tier bases (`Ultimate Life Flask` / `Ultimate Mana Flask` — tier 9, lvl
  60), styled white = useful to both players. Lower flask tiers stay hidden on
  purpose; only the endgame bases are worth surfacing.

### Changed

- **High-ilvl crafting fodder now includes Armour/ES hybrid bases.** The fodder
  rule keyed on `BaseArmour 0` (pure ES/EV bases only), which excluded Str/Int
  hybrids like a **Hallowed Crown** (base armour *and* ES). A Normal/Magic one
  then fell to the map Hide and vanished — the reported symptom. Re-keyed on
  `BaseEnergyShield > 0` so any ES base shows, hybrids included. **Split into two
  blocks** (ES-keyed + Evasion-keyed) so pure-Evasion fodder for Scott is
  preserved — keying on ES alone would have silently dropped it. Rare hybrids
  were already shown by the `ES / EV-ES ARMOUR — rare` rule and are unaffected.

---

## v1.2.0 — 2026-07-23

Bug fix from actual play — a critical league item was silently hidden.

### Fixed

- **Breach Wombgifts were being hidden.** Genesis Tree crafting inputs
  (Lavish / Signet / Ornate / Banded / Revelatory Wombgift) are **not** item
  class `Stackable Currency`, so no Show rule matched them. A Normal-rarity
  Wombgift dropping in a map fell through to the blanket `Hide MAGIC / NORMAL —
  maps` rule and vanished, before even reaching the magenta unrecognised-item
  catch-all. Added a loud Show rule at the top of the currency section. The
  match is `BaseType "Wombgift" "Womb Gift"` — substring (no `==`) so all five
  variants and any future ones are caught, and no `Class` line so it is spelling-
  and class-robust. This is the exact silent-hide the catch-all is meant to
  prevent; a broad rarity Hide sitting above it created the gap.

---

## v1.1.0 — 2026-07-23

Scott's build confirmed: **unarmed**, Hollow Focus (bells) + Way of the Stone
Fist. This corrected a real bug.

### Fixed

- **Armour-base gloves were being hidden.** `Gloves` was included in the
  pure-Armour `Hide`, so normal and magic armour-base gloves below ilvl 81 never
  rendered. Way of the Stone Fist converts gloves into Fists of Stone, supplying
  its own Evasion and Energy Shield per level and rewriting all modifiers — so
  glove base defence type is irrelevant and every glove is a potential weapon
  upgrade. `Gloves` removed from that rule, with an inline comment so it is not
  re-added.

### Changed

- **Gloves promoted to weapon-tier priority.** Rare gloves now get sound, beam,
  minimap icon and font 45 — the same treatment as a weapon, because that is
  what they are. Previously font 40 with no sound or beam, treated as armour.
- **All gloves shown below AreaLevel 80** regardless of rarity or base, and any
  glove at ilvl 81+ shown at all levels.
- Quarterstaves left loud deliberately. Scott intends to switch to one, so they
  are an upgrade path rather than dead weight.

### Notes

- Runic Meridian (extra rune-only sockets on helmet, body armour, gloves, boots)
  is **not yet specced**. Socketable priority stays elevated regardless — the
  filter is already tuned for when he takes it.
- Facebreaker is a live chase target; covered by the existing uniques rule.

### Verified

9/9 behavioural tests against the compiled filter: all five glove cases now
show, and non-glove Armour bases still hide correctly at both levels 73 and 82.

---

## v1.0.0 — 2026-07-23

Initial shared filter. Monk/Martial Artist (73) + Sorceress (73), early maps.

### Added

- **AreaLevel banding** as the progression spine: `<65` campaign, `65–74` early
  maps, `75–79` mid, `80+` high, with a dedicated ilvl 81+ crafting tier.
  Filters cannot read character level, only zone level — and zone level is the
  better signal anyway, since loot relevance tracks where you are, not what you
  are. The filter self-adjusts on progression with no manual edits.
- **Per-player border colours.** Green = Monk gear, blue = Sorceress gear,
  white = useful to both. Lets either player identify whose upgrade dropped
  without reading the item mid-fight.
- **Socketable priority override.** Runes, soul cores, and idols elevated above
  stock tiering, using substring `BaseType` matching rather than an explicit
  list so future runes are caught automatically. Rationale: Martial Artist is
  the only ascendancy with extra body rune slots, so socketables are worth
  materially more to this party than to any other build.
- **Party-dead class purge.** Bows, Crossbows, Quivers, One/Two Hand Maces,
  Spears, and pure-Armour bases hidden. Monk is Dex/Int and Sorceress is pure
  Int, so nothing Strength-based serves either build. Largest single clutter
  reduction in the filter.
- **Magenta/cyan unrecognised-item catch-all** at the bottom, with sound and
  minimap icon. Guards against new league content being silently hidden.
- **`scripts/validate.py`** — catches unknown Class names, unconditional
  blocks, shadowed rules, and out-of-range colour/font values.

### Notes

- Currency and unique tiering is deliberately simple. Not competing with
  NeverSink's economy-driven valuation; competing on build specificity.
- Rare display is generous in the current band because both players are still
  gearing through early maps. Expect to tighten `65–74` once upgrades slow.

### Open

- Scott's weapon unconfirmed (quarterstaff assumed) and which Hollow Technique
  the build centres on.
- Sorceress ascendancy unconfirmed; low filtering impact.
- Whether the Sorceress uses Staves at all — if not, that class can be dropped
  for further clutter reduction.
