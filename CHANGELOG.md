# Changelog

Filter versions and the reasoning behind them. Record *why*, not just what —
the reasoning is what prevents relitigating settled decisions later.

---

## Unreleased

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
