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

### Build notes

Martial Artist is the third Monk ascendancy, added in 0.5 Return of the
Ancients. Core mechanics as understood:

- **Crit-centric loop:** summon bell → strike bell (guaranteed crit) →
  trigger resonance → spend combo points on finishers.
- **Hollow Techniques** — three of seven, chosen via ascendancy nodes:
  Hollow Focus (summons ethereal bells), Hollow Form (channels illusory
  clones that perform a socketed attack), Hollow Resonance (permanent bell
  that resonates on every critical hit).
- **Melee-focused**, with a glove transformation mechanic.
- **Energy Shield sustain** primarily via combo cycling through Martial Adept.
- **Unique to this ascendancy: extra rune slots housed in the body.** No other
  ascendancy can do this. Gets stronger with every rune GGG adds.

### Filter implications

- **Socketables (runes, soul cores, talismans) = elevated priority.** More
  slots to fill and more value per rune than any other class. Override stock
  economy tiering upward.
- **Dex/Int class** → Evasion and Evasion/ES hybrid bases matter. Pure Armour
  (Str) bases are near-vendor-trash. *Check partner's build before hiding.*
- **Crit and attack speed** weigh heavier than flat physical damage.
- **Gloves** get their own rules, not folded into generic armour.

### Open questions

- [ ] **Weapon:** quarterstaff, or leaning into the glove/unarmed side?
      (Sources note it's not really a hand-to-hand subclass despite the name,
      so quarterstaff is likely — but unconfirmed.)
- [ ] **Which Hollow Technique** is the build centred on — bells, clones, or
      the rune-defensive path? Determines crit-heavy vs. defensive base
      priorities.
- [ ] Current gear pain points / what he's actively shopping for.

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

Crucially it is *flexible*: ascendancy nodes such as Instruments of Power and
Baryanic Leylines let her skip summoning entirely and play as a straight spell
caster using the Djinn only for buffs and debuffs. So "summoner" is not a safe
assumption — the same ascendancy supports a pure caster.

### Filter implications

- **Pure Int** → Energy Shield bases. Confirmed by the ascendancy's own design:
  Navira provides ES recovery, and The Fourth Teaching grants 40% more ES
  Recharge Rate on low ES. ES is unambiguously her defensive layer.
- **Staves AND Foci both stay live.** One ascendancy node lets her *wield a
  Staff and Focus together* — an unusual combination. This resolves the earlier
  open question: do **not** trim `Staves` from her weapon rules.
- **Sceptres stay live** — they grant Spirit, which matters if she leans into
  the summoner side.
- Damage element (fire via Ruzhan, etc.) has **no filter impact**. Filters key
  off item class, defence type, and item level — not what element a build
  scales.

### Watch item

One ascendancy node reportedly **converts Energy Shield into Armour**. If she
takes it, she still wants *ES bases* (which then convert) — she does **not**
want Armour bases. The existing `Hide` on pure-Armour gear stays correct either
way. Flagged only so it isn't mistaken for a reason to unhide Armour.

### Open questions

- [ ] Summoner-leaning or pure caster? Affects how hard to prioritise Sceptres
      and any Spirit-granting gear.

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
