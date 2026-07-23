# Changelog

Filter versions and the reasoning behind them. Record *why*, not just what —
the reasoning is what prevents relitigating settled decisions later.

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
