# Characters

Living document. Update every session. Last updated: 2026-07-23.

**League:** Runes of Aldur (0.5 — Return of the Ancients)
**Mode:** Trade, Softcore
**Play pattern:** Almost always partied together. Loot split by need, loosely.
**Crafting posture:** Some of both — crafting *and* drop-hunting/selling.

---

## Scott — Monk / Martial Artist

| Field | Value |
|---|---|
| Level | 73 (as of 2026-07-23) |
| Class | Monk |
| Ascendancy | Martial Artist |
| poe.ninja | *not yet — needs level 80 for ladder indexing* |
| Progression | Just hit endgame, early waystones |

### Build notes — CONFIRMED 2026-07-23

**Currently UNARMED.** Running **Hollow Focus** (bells) + **Way of the Stone
Fist**. Intends to switch to a quarterstaff later, so quarterstaff rules stay
loud even though they are currently aspirational.

- **Way of the Stone Fist converts equipped Gloves into "Fists of Stone"** — a
  base not obtainable by normal means. It grants Evasion Rating and Energy
  Shield per level and replaces all modifiers with stronger variations.
  **Gloves are therefore his weapon, not armour**, and glove base defence type
  is irrelevant — the affixes are what convert.
- **Hollow Focus** summons bells that are always treated as in Culling Strike
  range, primed for stun, and guaranteed to take critical hits. Crit-centric.
- **Has NOT yet taken Runic Meridian** — the node granting extra rune-only
  sockets tied to helmet, body armour, gloves, and boots. This is the
  ascendancy's signature advantage and he is not using it yet.

### Filter implications

- **Gloves = top-tier priority.** Sound, beam, minimap icon, largest font.
  They are the weapon slot. Never fold them into generic armour rules, and
  **never** add `Gloves` back to the pure-Armour `Hide`.
- **Quarterstaves stay loud** — planned upgrade path, not current gear.
- **Crit chance on gear matters.** Guides note the common mistake is stacking
  crit damage before crit chance.
- **Socketables stay elevated** even though Runic Meridian is not yet specced.
  When he takes it the payoff is immediate and the filter is already tuned.
- Dex/Int → Evasion and EV/ES bases for non-glove slots.

### Chase item

**Facebreaker** (unique gloves, returned in 0.5) is a genuine target — GGG
confirmed Way of the Stone Fist works on unique items. Already covered by the
`ALL UNIQUES` rule at the top of the filter.

### Open questions

- [ ] Nothing blocking. Next input should be in-game feedback on v1.1.0.

---

## Partner — Sorceress / Disciple of Varashta

| Field | Value |
|---|---|
| Level | 73 (as of 2026-07-23) |
| Class | Sorceress |
| Ascendancy | Disciple of Varashta |
| poe.ninja | *not yet — needs level 80 for ladder indexing* |
| Progression | Same as Scott, early waystones |

### Build notes

Disciple of Varashta was added in 0.4 (Last of the Druids). It is a
"build your own summoner" ascendancy built around commanding three invulnerable
Djinn — Ruzhan (fire, heavy damage), Kelari (crit burst and corpse mechanics),
and Navira (support: Energy Shield recovery, flask generation, sustain).

The ascendancy is *flexible*: nodes such as Instruments of Power and Baryanic
Leylines let her skip summoning entirely and play as a straight spell caster,
using the Djinn only for buffs and debuffs. **Confirmed (2026-07-23): she is
going pure caster, not a minions build.** The Djinn are buff/debuff support,
not the damage engine.

### Filter implications

- **Pure Int** → Energy Shield bases. Confirmed by the ascendancy's own design:
  Navira provides ES recovery, and The Fourth Teaching grants 40% more ES
  Recharge Rate on low ES. ES is unambiguously her defensive layer.
- **Staves AND Foci both stay live.** One ascendancy node lets her *wield a
  Staff and Focus together* — an unusual combination. This resolves the earlier
  open question: do **not** trim `Staves` from her weapon rules.
- **Sceptres stay live even though she's not a summoner.** They are the main
  source of **Spirit**, and Spirit is universal in PoE2 — it powers auras,
  heralds, and persistent buffs, not just minions. A pure caster running
  heralds/auras still wants it. Do **not** hide or demote Sceptres.
  *Only reconsider if play-test shows she runs zero Spirit-reserved skills* —
  a tuning call, not a preemptive edit.
- Damage element (fire via Ruzhan, etc.) has **no filter impact**. Filters key
  off item class, defence type, and item level — not what element a build
  scales.

### Watch item

One ascendancy node reportedly **converts Energy Shield into Armour**. If she
takes it, she still wants *ES bases* (which then convert) — she does **not**
want Armour bases. The existing `Hide` on pure-Armour gear stays correct either
way. Flagged only so it isn't mistaken for a reason to unhide Armour.

### Open questions

- None. Build confirmed pure caster as of 2026-07-23. (Was: summoner vs caster,
  which affected Sceptre/Spirit prioritisation — resolved, Sceptres stay live.)

---

## Party-level conclusion — the big win

Monk is **Dex/Int**, Sorceress is **pure Int**. Neither is Strength-based.

That means **pure Armour bases and all Strength weapon classes are dead for the
entire party** — Bows, Crossbows, Quivers, One/Two Hand Maces, Spears, and
Armour-only body/boots/helmets/shields. This is by far the largest clutter
reduction available, and it is only safe *because* both builds sit Int-side.

**If either player ever rerolls to a Strength build, these hides must be
revisited first.** They are the most aggressive rules in the filter.

---

## Shared decisions log

Record why things were decided, so we don't relitigate.

- **2026-07-23** — One shared filter rather than two. Rationale: they play
  together almost always; separate filters mean each is blind to half the
  party's upgrades.
- **2026-07-23** — Level awareness via `AreaLevel` bands, not character level.
  Filters can't read character level. Bands mean the filter self-adjusts on
  progression with no manual edits.
- **2026-07-23** — Socketables elevated above stock tiering for Scott, due to
  Martial Artist's unique extra rune slots.
