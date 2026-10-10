# UVCE Rocketry — Consolidated Technical Reference

**Purpose:** Working engineering reference for UVCE Rocketry Club, built from authoritative amateur
experimental rocketry sources. This is the document you design *from* — not a textbook to read once.

**Primary source:** Richard Nakka's Experimental Rocketry Site (nakka-rocketry.net) — the most
extensive public body of practical amateur solid-rocket knowledge in existence, and the origin of
much of the modern practical understanding of KNSB propellant.

**Retrieved so far:** Propellant (KNSB), Safety, Burn rate / strand burner, Ignition, Grain geometry,
Nozzle theory, Static testing. Raw source HTML cached in `nakka_src/`.

> **Status note:** Sections marked ✅ are extracted and verified from source. Sections marked ⏳ are
> pending retrieval. Never design against a ⏳ figure.

---

## PART 1 — PROPELLANT: KNSB ✅

### 1.1 What it is

**KNSB** = Potassium Nitrate / Sorbitol. Standard formulation **65% KNO₃ (oxidiser) / 35% sorbitol
(fuel + binder) by mass.**

- Sorbitol is a *hexahydric alcohol* ("alcohol sugar"), formula **C₆H₁₄O₆**, MW 182.2 g/mol.
- It is **not** a carbohydrate, unlike sucrose or dextrose.
- Commercial synonyms: Neosorb, Sorbite, Karion, Sorbit, D-Sorbol, D-Glucitol.
- Widely available: confectionery, toothpaste, chewing gum, ice cream, diabetic sweeteners, and
  online (eBay/Amazon).
- Potassium nitrate ("saltpetre") is sold as **14-0-45 fertiliser** at farm supply stores at
  98–99% purity — by far the most economical form. Performance is *generally* no different from
  purer grades. Note: sale of potassium nitrate is restricted in some jurisdictions.

### 1.2 Why KNSB rather than KNSU (sucrose) or KNDX (dextrose)

| Property | Sucrose (KNSU) | **Sorbitol (KNSB)** | Dextrose (KNDX) |
|---|---|---|---|
| Formula | C₁₂H₂₂O₁₁ | **C₆H₁₄O₆** | C₆H₁₂O₆ |
| Molecular weight (g/mol) | 342.3 | **182.2** | 180.16 |
| Melting point (°C) | 185 (decomposes) | **110–112** | 146 (decomposes) |
| Density (g/cm³) | 1.581 | **1.489** | 1.562 |
| Enthalpy of formation (kJ/mol) | −2221.2 | **−1353.7** | −1274.5 |
| Appearance | white granular | **white granular** | dry white powder |

**KNSB's practical advantages:**
- **No caramelisation** on normal heating → pot life is essentially unlimited → suitable for very
  large grains.
- **Lower casting temperature** → larger safety margin, and much less rapid freeze-up, giving
  fewer voids and air bubbles in the cast grain.
- Less hygroscopic than KNSU (slightly better than KNDX).
- Mechanical properties similar to KNSU/KNDX — rigid and brittle, but tensile strength is
  appreciable.

**Key sorbitol behaviour:** melted sorbitol does not harden immediately. It forms a soft transparent
mass that can be cut and stretched. Surface hardens after 2–3 days; fully hardens after ~5 days.
Cured material is non-hygroscopic at moderate humidity. **KNSB propellant cures faster — 
1 to 2 days.**

### 1.3 Handling the raw materials

**Potassium nitrate — grind it:**
- Electric coffee grinder, ~2 tablespoons (30 ml) per load, 15–30 s, slowly "gyrating" the grinder.
- Resulting sieve analysis: **50% of particles < 74 µm**, most of the remainder < 234 µm.
- ⚠️ **Grinding time controls slurry viscosity.** Finer grind = better performance but *thicker*
  slurry that must be scooped, not poured. Shorter grind (≤10 s) or "as obtained" fine granular KN
  gives a more fluid slurry — at the cost of reduced performance (less efficient combustion, lower
  chamber pressure, slightly longer burn).

**Sorbitol — sift it:**
- Powdered sorbitol cakes into hard clumps in storage. Break up with a flour sifter or by rubbing
  through a strainer.

**Dessication (only if maximising performance):**
- Sift sorbitol into a shallow pan, place in a desiccator for 1–2 days.
- A desiccator can be a Tupperware container lined with a few cm of **fresh calcium chloride**.
- ⚠️ Tradeoff: dessicated sorbitol gives a **stiffer, more viscous slurry** — harder to cast.

### 1.4 Mixing

1. Mill the KN; sift the sorbitol.
2. **Weigh both constituents accurately** — an accurate scale is mandatory.
3. Prepare **20–25% excess** for small batches to account for casting waste (less for larger
   batches).
4. Blend together in one container. **Complete mixing is required** for optimum and consistent
   performance.
5. Nakka's method: a rotating tumbler at 30 RPM for ≥30 min (later version ~100 RPM, 1 kg capacity).
6. ⚠️ **The mixed powder is readily combustible.** Transfer immediately to a closed container, and
   keep it away from all ignition sources.

### 1.5 Casting — the critical procedure

**Heating vessel — non-negotiable:**
> Use **only a thermostatically temperature-controlled heating vessel with no exposed elements** —
> e.g. a thermostatically controlled electric deep fryer or skillet. The critical intent: **no
> exposed heating surface significantly hotter than the propellant's melting point.**

⚠️ If the wrong vessel is used and surfaces get hot *before* adding powder, **ignition can occur
immediately.** The demonstrated tolerance of molten KNSB to overheating applies *only* to the
already-melted slurry — it is not a licence to use any heating vessel.

**Parameters:**

| Parameter | Value |
|---|---|
| **Casting temperature** | **120–130 °C** |
| Temperature control | ±5 °C |
| Auto-ignition temperature | **> 300 °C** |
| Decomposition onset (colour change) | ~175 °C |
| Visible smoking / strong odour | ~250 °C |

**Procedure:**
1. Preheat the vessel to the required temperature and hold ±5 °C. Monitor with a candy
   thermometer, a digital probe thermometer, or (most convenient) an **infrared thermometer**.
2. Add **about half** the powdered mix; stir often to assist melting.
3. Once melted, add the remaining half.
4. Colour starts nearly colourless, turns **white** as it becomes fully melted. If sorbitol has
   residual moisture, melting is rapid and the slurry looks pure white/almost translucent with tiny
   bubbles as water boils off. As water is driven off, colour shifts to **light ivory**.
5. Heat and stir an additional **5–10 minutes** to reach casting temperature and eliminate lumps.
6. ⚠️ **The slurry may not become fluid enough to pour.** In most cases consistency stays thick —
   **pour and scoop simultaneously** with a spoon or silicone spatula.
7. Load the mould, then **firmly tap the mould bottom against a hard surface repeatedly. This is an
   important step** — it forces trapped air to the surface.
8. Immediately insert the **lubricated** coring rod (silicone grease / Super Lube), making certain it
   is **fully inserted all the way down**.
9. Allow to cool and harden.

**Reading the colour:**
- **Pure white** = pure oxidiser, good.
- **Yellowish/amber** = impurities, commonly anti-caking agents in the KN. Test: a saturated aqueous
  solution (33 g KN in 100 ml water, at room temperature) should be **neutral, pH 6.5–7**. Impurities
  make it significantly alkaline (**pH > 8**), causing discolouration.
- Discoloured propellant is **more hygroscopic** than pure white KNSB. Performance is not seriously
  degraded.

### 1.6 The surfactant trick — makes KNSB pourable

Molten KNSB is normally too viscous to pour. A **tiny amount of surfactant** dramatically reduces
viscosity — Nakka reports it becomes "readily pourable, having a viscosity similar to maple syrup."

- **Use Sodium Laureth Sulfate (SLES)**, 70–80% liquid concentrate. Cheap and widely available
  (used in soaps/shampoos); ~500 ml for about $5 CAD.
- ⚠️ **Sodium Lauryl Sulfate (SLS) is a different product and may not work as effectively.**
- A retail **foaming bath gel** works if its main listed ingredient (other than water) is SLES — but
  it contains appreciable water, so more may be needed and extra heating is required to drive the
  water off.
- **Dosage: ~0.1% surfactant by mass of molten propellant.** Add to the fully molten KNSB and stir;
  viscosity drops immediately.

### 1.7 Curing and demoulding

- Cast KNSB stays **pliable** after cooling — a grain can deform if handled carelessly.
- After **one day**, exposed surfaces become quite hard; the inside stays "waxy" but is rigid enough
  to handle.
- **Cure 1–2 days before demoulding** (depends on residual moisture and grain size). Demoulding too
  soon distorts the grain when extracting the coring rod.
- Until fully cured, **KNSB chips easily** — take care. After full cure it is hard and relatively
  strong. Full cure may take a week, but **it is acceptable to fire a grain any time after
  demoulding.**
- ⚠️ In comparison with KNSU and KNDX, KNSB is **far more susceptible to chipping** — noticeable when
  cutting with a hand saw. A coarse blade causes chipping.

### 1.8 Quality control — two mandatory checks ✅

Perform these on **every** grain segment.

#### Check 1 — Density Check

Detects air bubbles and voids. Air inclusion of a few percent is negligible; **sizeable bubbles,
many bubbles, or trapped voids significantly increase burning surface area → over-pressurisation or
CATO.**

- Weigh the grain segment; measure its volume (calipers are more accurate than a ruler).
- Compute density = mass / volume.
- Compare against **ideal KNSB density = 1.841 g/cm³** (= 0.0665 lb/in³).
- The ratio of actual to ideal density is the quality benchmark.

Notes:
- Core diameter need not be measured explicitly — it equals the coring rod diameter.
- If the grain is integral with its casting tube, subtract the tube's mass and thickness.
- Nakka provides `Graindensity.xls` for this.

#### Check 2 — Tap Test (a.k.a. Coin Tap Test)

Applies **only to a grain with an integral casting tube as inhibitor.** The inhibitor **must** be
intimately bonded — any disbonding lets hot gas seep between inhibitor and propellant, increasing
burning area.

- Tap the inhibitor gently with a coin (larger coin works better) at points **all around** the
  segment.
- Sound and feel should be a **solid tap**, not a dull one.
- ⚠️ The difference is hard to describe in words and **takes experience to recognise.** Practise on
  good grains.
- **Best technique: listen to the *relative* tap sounds.** Every tap should sound identical. Any
  point that sounds distinctly different (duller, like tapping hard rubber vs hard plastic) signals
  possible disbonding.
- A single isolated odd spot is generally not a problem. A **different tap sound at the seam of a
  rolled casting tube is normal.**
- 🔴 **What to actually watch for: a different tap response *between grain segments of the same
  batch*.** If one segment sounds distinctly different and less solid, its inhibitor bond may be
  flawed. **Reject that segment.**
- **Only perform after full cure**, or disbonding indications may be false. Residual moisture in the
  bondline can also cause a false fail — a few days in a desiccator often converts it to a pass.
- On grains **cured under pressure**, tap test failure is very rare (a few out of ~200 segments).

### 1.9 Overheating — the actual safety margin ✅

A deliberate overheat experiment (16 g sample, forced-air heat gun, type-K thermocouple):

| Temperature | Observation |
|---|---|
| ~175 °C | slight yellowing at pan edges |
| ~225 °C (11 min) | greyish-amber colour |
| ~250 °C | bubbling begins, then puffs of smoke, strong burning-caramel odour |
| >300 °C | strong decomposition; heating terminated. Bottom layer severely charred — **yet failed to ignite** |

**Conclusion:** auto-ignition occurs at **> 300 °C**, while normal casting is **below 135 °C**. There
are obvious warning indicators of overheating (colour change, bubbling, smoke, strong odour).

> ⚠️ **This tolerance must never lead to lax standards.** Treat it only as a valuable *margin of
> safety*. Inadvertent ignition from other causes — electrical short, static, distraction — must be
> treated as a real possibility. **Wear face and hand protection as a minimum.**

### 1.10 Theoretical performance ✅

- KNSB performance is very similar to KNSU and KNDX.
- **Specific impulse less than 1% lower than sucrose-based.**
- **Combustion temperature about 100 °C lower** than sucrose-based.
- Combustion products very similar, including the mass fraction of particles in the exhaust.
- **Ideal density 2.5% lower** than sucrose-based propellant.

→ Full ideal-performance table (Isp, C*, chamber temperature, exhaust products) is on Nakka's
`techsht-knsb.htm` page. ⏳ *pending retrieval — use this table to set your design C\* and Isp.*

### 1.11 Burn rate 🔴 THE MOST IMPORTANT SECTION

> **✅ VERIFIED — replaces the earlier "numeric law pending" version of this section.**
>
> Burn rate is a **key parameter for rocket motor design** — and KNSB has genuinely awkward burn-rate
> behaviour that will complicate your first motor.
>
> **Source:** Nakka's strand-burner investigation (`bntest.html`), 65/35 O/F exclusively, pressures
> from 1 to >100 atm, burn rate timed over a gauge length with thermocouples at each end.
>
> #### The governing law
>
> $$r = r_o + a \cdot P_c^{\,n}$$
>
> - `r` = burn rate · `r_o` = constant, **usually taken as zero**
> - `a` = burn-rate coefficient · `n` = **pressure exponent** (slope of the log-log plot)
> - ⚠️ **`a` and `n` are empirical and CANNOT be theoretically predicted.**
> - ⚠️ **A given `a`, `n` pair is valid only over a distinct pressure range.**
>
> #### 🔴 KNSB IS A MESA PROPELLANT — a single power law will NOT describe it
>
> - **KNSU** follows classic **St. Robert** well — one power function over the full range.
> - **KNDX** is a **plateau** propellant.
> - 🔴 **KNSB is a *mesa* (inverted-mesa) propellant.**
>
> **Mesa behaviour** = over some pressure range `n` becomes very small or even **negative**, so burn
> rate stops responding to pressure — or *falls* as pressure rises.
>
> > **Nakka's design rule: the pressure exponent for a practical propellant should be between 0.3 and
> > 0.6 in the regime of the motor's steady-state operating condition.**
>
> **Consequence:** isolate the pressure regime your motor actually runs in and use the `a`, `n` pair
> valid **for that regime only.** Regime-by-regime tables are in `bntest.html`.
>
> #### Measured anchor points for KNSB
>
> | Pressure | Burn rate |
> |---|---|
> | 14.7 psia (1 atm, 0.101 MPa) | **0.102 in/s = 2.59 mm/s** |
> | 1000 psia (6.89 MPa) | **0.443 in/s = 11.25 mm/s** |
>
> A naive single power law through only these two points gives **a ≈ 1.99 mm/s/MPaⁿ, n ≈ 0.30.**
> ⚠️ **Illustrative only** — exactly the single-law fit that mesa behaviour invalidates.
>
> #### Startup sensitivity — the trap that will bite you
>
> - **Low `n` (~0.2)** → burn rate changes rapidly at low pressure → **excellent start-up.**
> - 🔴 **High `n`** → burn rate insensitive to pressure at the **low end** → **difficult starting.**
>   Nakka's words: *"the motor simply refusing to come up to pressure."*
> - **`n` near zero** → burning rate largely insensitive to pressure → **unstable combustion.**
>
> > 🔴 **This applies to you.** KNSB's low-pressure-regime exponent sits near **0.3 — the bottom of
> > the acceptable band. Your small motor may be reluctant to come up to design pressure.** Plan for
> > it with a proper black-powder igniter (Part 5), not a bare bridgewire.
> >
> > ⚠️ **Do not copy this idea:** Nakka's **burst diaphragm** (thin brass sheet blocking the throat to
> > force pressure build-up) **caused a motor failure** on Flight C-18 (July 1980). Sizing it to burst
> > reliably at the right pressure "was not simple to achieve, at least not so with my narrow-throated
> > motors."
>
> #### Erosive burning — and a KNSB-specific quirk
>
> - **Erosive burning** = gas flowing parallel to the burning surface increases burn rate.
> - Many propellants have a **threshold flow velocity**; below it there is either no augmentation or a
>   **decrease** (*negative erosive burning*).
> - 🔴 **"The KNSB propellant appears to be particularly susceptible to negative erosive burning."**
> - **Mitigation — port-to-throat area ratio (A_port / A_t): minimum 2** for a "typical" grain L/D of
>   **6**; larger ratios required for **larger L/D**.
>
> #### Particle size, moisture, temperature
>
> 1. **Larger oxidiser particle size → lower burn rate**, across the full pressure range.
> 2. **Granular** KN follows St. Robert reasonably well and **does not show mesa behaviour**.
> 3. **Residual moisture suppresses burn rate** by **reducing `a`** — **`n` unchanged** (identical
>    log-log slopes for fine-dessicated vs granular).
> 4. **Sorbitol** is the culprit: as-obtained it holds more moisture than sucrose or dextrose.
> 5. **Temperature:** only **minor** sensitivity over **0–40 °C**.
>
> #### Comparison values
>
> - **KNSU:** 3.8 mm/s at 1 atm → ~15 mm/s at 68 atm — a four-fold rise.
> - **KNSB:** 2.59 mm/s at 1 atm → 11.25 mm/s at 1000 psi — **lower than KNSU at both ends.**
>
> > 🔴 **Net consequence for your 24 N·s motor:** you cannot trust a single power law; your
> > low-pressure exponent sits at the bottom of the usable band (start-up risk); and as-obtained
> > materials give a **lower `a`** than any dessicated test data. **A strand burner is not optional —
> > it is the first piece of test equipment you should build.** Size the throat with margin and expect
> > the first firing to come up to pressure slowly.

#### Additional burn-rate notes (particle size & moisture record)

- Nakka's strand-burner work covered **KNSU, KNDX and KNSB** via a Strand Burner apparatus, burning
  thin propellant rods at **1 to >100 atm**.
- A separate 2010 Bachelor's thesis (Magnus Gudnason) characterised KNSB made with **as-obtained
  granular** KN, with excellent technique — and found **less scatter** than earlier work.
- **Improved experimental technique** measurably reduced scatter in the later results.

### 1.12 Grain mechanical properties ✅ — and why it dictates your grain geometry

| Property | Value |
|---|---|
| Elastic (bending) modulus, E | **~850,000 lb/in² = 5.84 GPa** |
| Modulus of rupture, F_b | **~1100 lb/in² = 7.6 N/mm²** |
| Tensile strength, F_tu | **~1050 lb/in² = 7.2 N/mm²** |

For comparison: E is similar to **bakelite**; F_tu is similar to **particleboard**.

**The critical design rule:**

> A propellant grain **should be designed to avoid subjecting the grain to tensile stress.** If that
> is not possible, **the allowable tensile stress must be taken as no greater than 20% of the F_tu
> of pristine material.**

**Why this decides your grain configuration:**
- A **freestanding** grain (not bonded to the case) is subjected almost exclusively to **compressive**
  loading. KNSB is **strong in compression and weak in tension** → freestanding grains perform very
  reliably with no structural problems. **This is why freestanding BATES grains are the standard
  amateur configuration.**
- A **case-bonded** grain with a central core is predominantly in **tension** → risky with a brittle
  propellant.
- Scatter in the tensile tests was large (436, 874, 1050 lb/in²) with no visible flaws — showing that
  **even tiny flaws act as stress raisers.** Hence the 20% allowable.

**Conclusion for your first motors:** use **freestanding** grains, in a casting tube that acts as the
inhibitor, sized with a **burst margin of 2.5× MEOP** (see Part 4 safety).

### 1.13 Special considerations — the KNSB "mountain" curve ✅ 🔴

This is the single most important practical KNSB finding, and it will affect your first motor.

**The symptom:** KNSB motors show chamber pressure and thrust curves that are **"triangular" or
mountain-shaped**, rather than the **flat or gently curved** profile predicted by design. KNSU and
KNDX do not do this.

**The cause:** **delayed ignition of the end faces of BATES grain segments.** Also, **KNSB is more
stubborn to ignite** than KNSU or KNDX (see `ignexp.html`).

**The solution — both parts are required:**
1. **Adequate inter-segment spacing.** Confirmed by motor testing varying spacing from 1.5 mm to
   18.5 mm.
   > **Rule of thumb: spacing = 10–20% of the grain diameter.** Rubber O-rings work well as spacers.
2. **Coat the grain segment end faces and core with a light coat of ignition primer.**
   > ⚠️ **Only a *thin* layer on the end faces.** A heavy coat **defeats the purpose and causes
   > delayed ignition.**

**Consequence for your 24 mm grain:** your single-grain design has no inter-segment gaps, so the
spacing rule does not apply — but **the primer coat absolutely does.** Prime the core and both end
faces thinly, and expect the pressure curve to be less flat than ideal. If you later go to
multi-segment BATES grains, apply **10–20% of grain diameter spacing** (2.4–4.8 mm for a 24 mm grain)
and use O-ring spacers.

### 1.14 Practical scale reference ✅

- Nakka's largest KNSB motor: **89 mm *Muon*, M-class**, six grain segments, **6 kg total
  propellant**.
- KNSB is suitable for casting very large grains (unlimited pot life).

---

## PART 2 — SAFETY FRAMEWORK ✅

Nakka's framing, worth internalising before anything else:

**Is amateur experimental rocketry hazardous?** No — otherwise sensible people wouldn't do it.
**Are there hazards to be concerned with?** Definitively yes. The responsibility is to *recognise*
potential hazards and take the necessary precautions. **Knowledge takes over where common sense
leaves off** — because some risk factors are not obvious.

### 2.1 Why propellants demand respect — the energy argument

- Sugar propellants release about **2.7 kJ per gram** on burning.
- **1 kg therefore holds 2.7 megajoules** of stored thermal energy.
- That is equivalent to a **1000 W heater running for 45 minutes** — released in **2–3 seconds.**
- AP-based propellants hold **nearly double** that energy density.

### 2.2 The author's own "don't bother" criteria

> - If you are a **risk taker**, don't bother reading further — amateur rocketry is not for you.
> - If you are a **careless person**, don't bother reading further.
> - If you are **not willing to religiously and without fail follow requisite safety practices**,
>   don't bother.
> - If you do not have **complete respect for the safety and property of yourself and others,
>   including the general public**, don't bother.

**Adopt these four as your club's membership filter.**

### 2.3 The safety rules ✅

1. **Wear appropriate safety apparel, including eye protection, at all times** when risk of personal
   harm is present — including workshop activities such as metal or wood working.
2. **Become familiar with the chemicals** used, in particular their **sensitivities and
   incompatibilities.**
3. When working with propellants, **always be alert and take the approach that such could ignite at
   any time.** Three items must **always** be present: **a dunk bucket full of water, a fire
   extinguisher, and a planned escape route.**
4. Use a **suitable work location** for propellant preparation and a suitable **storage location** for
   sensitive materials such as oxidisers.
5. **Keep batch sizes to the minimum needed for the job at hand.**
6. **Igniters must have their leads shunted at all times**, un-shunted only immediately before
   connecting to the ignition box. *(Shunting = twisting the bared leads together to prevent any
   current reaching the bridgewire.)* **This applies equally to parachute ejection charges.**
7. **If an igniter fails to initiate a motor: wait several minutes before cautiously approaching,
   then always disconnect the igniter leads first.**
8. **Use an ignition box with built-in safety checks** ensuring no current can inadvertently reach
   the igniter. **⚠️ A Safe/Arm switch represents only *partial* security.**
9. **Distance is your greatest assurance of safety** in case of catastrophic failure. Nakka positions
   himself and others **250–300 ft (75–100 m)** away for **proven** motors, and **even farther for new
   designs.**
10. 🔴 **Avoid "boilerplate" motor designs.** Thick-walled heavy-duty contraptions store an incredible
    amount of energy before bursting, *increasing* risk on failure.
    - Casings should be sized to burst at **no more than 2.5× MEOP** (maximum expected operating
      pressure).
    - **Minimum safety margin of 1.5 is appropriate** for motor design.
11. **Hydrostatic pressure test new motor designs.** Fill a completed, sealed motor with water,
    pressurise to **1.2× MEOP** with a grease gun or hydraulic jack fitted with a pressure gauge.
    ⚠️ Though compressed water stores little energy, **place a plywood shield between the motor and
    the operator** in case trapped air is present.
12. 🔴 **Beginners should stick to well-proven propellants and well-proven motor designs.**
    **Propellant development is best left to those with real experience and theoretical knowledge.**
    Even small amounts of certain additives can dramatically change burning characteristics, leading
    to catastrophic failure of otherwise well-proven designs.
13. **High-energy oxidisers (chlorates, perchlorates) for igniter pyrolants: limit to small
    quantities**, and use only proven formulations.
14. 🔴 **High-energy oxidisers for propellants (potassium perchlorate, ammonium perchlorate) should
    only be used by those with years of experience working safely with lower-energy oxidisers such as
    the nitrates.** Only proven methods and formulations. Perchlorates "have the potential to be
    frighteningly hazardous when combined with incompatible binders or additives, and even small
    motors can explode with shocking violence."

> **Interpretation for UVCE Rocketry:** rules 12 and 14 are a direct, explicit instruction to
> **stay with KNSB / nitrate-based propellants** and to **not invent formulations.** For a team with
> no experience, nitrate-based sugar propellants are the correct and only sensible choice. Do not
> "improve" the formula.

---

## PART 3 — MOTOR DESIGN METHOD (summary)

*Nozzle theory and grain geometry retrieved; **c\* / Cd values and two-phase corrections still
pending** (`th_pres.html`, `th_2phf.htm`).*

**What is already established from Part 1:**
- Use **freestanding grains** — KNSB is brittle, weak in tension, strong in compression.
- **Prime all burning surfaces thinly**; bare KNSB ignites reluctantly.
- Multi-segment grains need **10–20% of grain diameter** inter-segment spacing.
- Correct your burn-rate coefficient `a` for your actual (likely undessicated) materials.
- Target **burst margin 2.5× MEOP**, never below 1.5×.

---

## PART 4 — PROPULSION DESIGN CONSTRAINTS

### 4.1 The equation chain (why motor design is iterative)

```
grain geometry              →  burning surface area A_b
A_b × burn rate r(P)        →  mass flow ṁ
ṁ                           →  required throat area A_t
A_t                         →  chamber pressure P_c
P_c                         →  burn rate r(P)   ← feeds back to the top
```

And separately: **web thickness ÷ burn rate = burn time.** Burn time is fixed by geometry alone.

> **You cannot independently choose impulse, thrust, burn time and grain size. Pick two; the rest are
> determined.**

### 4.2 Burn rate law — and why KNSB breaks it

$$r = r_o + a \cdot P_c^{\,n} \qquad (r_o \text{ usually taken as zero})$$

- `r` = burn rate (mm/s) · `P` = chamber pressure
- `a` = burn-rate coefficient — **material *and moisture* dependent. Correct this for YOUR materials.**
- `n` = pressure exponent — material dependent, **NOT** affected by moisture

🔴 **KNSB is a mesa propellant**, so **a single `a`/`n` pair is not valid across all pressures.** Use
the pair valid for your motor's steady-state regime; `n` should land in **0.3–0.6**. See §1.11.

⚠️ **Stability:** if `n ≥ 1` the motor is inherently unstable — rising pressure raises burn rate
faster than it raises mass flow out of the nozzle, and the motor can burst. Sugar propellants keep
`n < 1`, which is why they are usable. **Never design with an assumed `n` — measure it.** Equally, if
`n ≈ 0` combustion may be unstable, and a high `n` at low pressure means the motor **refuses to come
up to pressure at all.**

### 4.3 Design constraints checklist for any motor

- [ ] `n` measured, and in the 0.3–0.6 band **for the operating regime**
- [ ] `a` corrected for **your** materials (as-obtained, undessicated) — via strand burner
- [ ] Casing burst pressure ≥ 2.5 × MEOP (absolute minimum 1.5×)
- [ ] Hydrostatic proof test at 1.2 × MEOP with a plywood shield
- [ ] Port area / throat area ≥ 2 **throughout** the burn (KNSB is prone to **negative** erosive burning)
- [ ] Grain **freestanding**, not case-bonded
- [ ] All burning surfaces **thinly** primed (heavy primer causes delayed ignition)
- [ ] Inter-segment spacing 10–20% of grain diameter (multi-segment grains)
- [ ] Igniter sized so it **cannot plug the throat**, and not so large it causes a startup spike
- [ ] Igniter adequate to **pressurise** the motor (KNSB starts reluctantly)
- [ ] Density check passed (close to 1.841 g/cm³)
- [ ] Tap test passed (no batch-to-batch inconsistency)
- [ ] Remote ignition, **leads shunted** until the moment of connection
- [ ] Firing distance ≥ 75–100 m for proven motors, **more for new designs**
- [ ] ❌ **No burst diaphragm** — documented cause of motor failure

---


## PART 5 — IGNITION ✅

KNSB is **stubborn to ignite** compared with KNSU and KNDX, and this is intimately tied to the
mountain-shaped pressure curve (§1.13). Ignition is not an afterthought on this propellant.

### 5.1 Why ignition matters so much

Nakka's early motors showed a serious problem: **the motor burned for several seconds "building up
pressure" before suddenly thrusting at full force** — propellant visibly wasted. The cause is the
pressure dependence of burn rate: at atmospheric pressure the propellant burns slowly and only
accelerates once sufficient pressure exists in the chamber.

**The fix he settled on:** an igniter that both **ignites the grain and simultaneously pressurises the
motor.** A black-powder charge in a sealed cartridge burns nearly instantly, releasing hot gas and
molten combustion products. Result: **the motor achieves full thrust almost immediately**, and across
many flights and static tests this proved **highly reliable and significantly boosted performance.**

> ❌ **First attempt — do not repeat:** he tried a **burst diaphragm** (thin brass sheet blocking the
> throat) to force pressure build-up. It **did not work satisfactorily** and **caused a motor failure**
> on Flight C-18 (July 1980). Sizing it to burst reliably at the right pressure "was not simple to
> achieve, at least not so with my narrow-throated motors." **Abandoned.**

### 5.2 The pyrotechnic "straw" igniter

The workhorse design (used for B-200, C-400 and similar sugar motors):

- A length of **polyethylene plastic drinking straw**, filled with **Ignition Powder**.
- **Sealed at both ends with polyethylene hot-melt glue.**
- **Nichrome (nickel-chromium, high-resistance) wire** as the heating filament (bridgewire), soldered
  to the copper lead ends.
- Nichrome is inexpensive (~$0.20/ft). **Alternatives:** a strand or two of coarse **steel wool**, or
  even a strand of fine copper "speaker" wire.

**Bridgewire construction (nichrome is tricky to solder — this method works):**
1. Strip insulation from the leads; form **closed loops** with needlenose pliers.
2. Thread the nichrome through the loops; set the **span between loops to about 5 mm.**
3. Brush the loops lightly with **acid soldering paste**; heat with a soldering gun and fill with
   solder. Capillary action does the work; the nichrome ends up embedded in solder.
4. **Inspect with a magnifying glass** to confirm the loops are fully filled.
5. Remove excess paste by **swirling the igniter in alcohol.**

**Power source:** originally four 1.25 V nicad cells; later **two NiMH cells (3.6 V, 300 mAh each) in
series = 7.2 V**, chosen for excellent current delivery and good cold-weather performance.

### 5.3 Ignition Powder ✅

**Modern formulation (what he currently uses):**

> **80% potassium nitrate / 20% charcoal by weight. NO sulphur.**

- Sulphur's role in conventional black powder is mainly to **facilitate easy ignition** — great for
  flintlocks, but **for safety reasons not a good feature in a rocket motor igniter, and not really
  necessary.**
- Traditional BP (for reference): **75% KNO₃, 15% charcoal, 10% sulphur.**
- **Charcoal must be "natural wood" variety — NOT briquettes.** Break into pieces wrapped in cotton,
  strike with a hammer, then pulverise in an electric coffee grinder.
- Grind the KNO₃ to a fine powder separately, weigh to 80/20, then blend thoroughly (he uses the same
  rotating mixer as for propellant).

### 5.4 🔴 Igniter size is safety-critical

> **"Use of an igniter containing a much greater charge of BP than shown may result in an initial
> pressure *spike*. This over-pressurisation of the rocket motor during startup may result in motor
> failure characterised by shearing of the safety bolts retaining the rocket motor head."**

Testing on a Ballistic Evaluation Motor compared **3 g, 7 g and 15 g** igniters and showed the effect
on the pressure-time trace and burn time is **significant for small motors** (A-100, B-200, C-400).

> 🔴 **For your 24 mm motor this is a real hazard.** Scale the igniter to the motor. Start small.
> An oversized igniter in a small motor is a plausible route to a burst case.

### 5.5 Grain primer (required for KNSB)

- Bare KNSB is **reluctant to ignite**; the remedy is an **ignition primer** coating on the exposed
  grain surfaces.
- Apply to the **core and both end faces.** 🔴 **Thin coat only** — a heavy coat **defeats the purpose
  and causes delayed ignition** (see §1.13).
- ⚠️ Nakka's documented pyrolant coating uses **potassium perchlorate + sulphur + epoxy** — a
  **perchlorate** formulation. Per Part 2 rule 14, perchlorates are for the experienced only.
  **Do not start here.** Retrieve `articles/Nitrate_based_igniters.pdf` for the nitrate-based
  alternative before building any primer.

---

## PART 6 — OPEN ITEMS / TO RETRIEVE ⏳

| Item | Source page | Why it matters |
|---|---|---|
| Regime-by-regime `a`, `n` tables for KNSB | `bntest.html` (image tables) | **Cannot size a throat without these** |
| KNSB ideal performance table (Isp, C\*) | `techsht-knsb.htm` (image tables) | Sets design Isp and C\* |
| Nitrate-based igniter / primer recipe | `articles/Nitrate_based_igniters.pdf` | **KNSB needs a primer; avoid perchlorates** |
| Nozzle design angles, expansion ratio | `th_nozz.html` (partially retrieved) | Nozzle geometry |
| c\* and Cd values for sugar propellants | `th_pres.html` | Chamber pressure prediction |
| Two-phase flow corrections | `th_2phf.htm` | Real vs theoretical Isp |
| Static test stand design | `static.html` (partially retrieved) | First hardware build |
| Pressure/load measurement detail | `pressure-measurement.html`, `strainlc.html` | Getting real data |
| Strand burner construction | `staburn.html` | **Highest-value first build** |
| Stability, fins, recovery | `rocket.html`, `fins.html`, `rtheory.html`, `paracon.html` | Airframe design |

**Local archive:** raw HTML for the retrieved pages is cached in `nakka_src/` alongside this document.

## PART 7 — THE 24 N·s FIRST MOTOR (working design — NOT YET VALIDATED)

Derived using the corrected sizing method, **before** Nakka's measured burn-rate data was available.

**Mission:** 200 m apogee, 40 mm airframe, ~250 g dry mass.
**Required burnout velocity: ~72 m/s** (vs 62.6 m/s vacuum ideal — drag costs ~15% at this scale).

| Parameter | Value |
|---|---|
| Propellant mass | 24 g KNSB |
| Total impulse | ~24 N·s (D/E class) |
| Burn time | ~2 s |
| Thrust | ~12 N |
| Grain OD | 24 mm |
| Core port | 7 mm |
| Grain length | ~31.5 mm |
| Web thickness | 8.5 mm |
| Throat diameter | ~2.2 mm |
| Port/throat ratio | 10 → 118 (safe) |

> ## 🔴 STATUS: SUPERSEDED — DO NOT BUILD FROM THIS TABLE
>
> This design was computed using a **single power-law burn rate** calibrated at 3 MPa. Nakka's
> strand-burner data (§1.11) shows **KNSB is a mesa propellant**, so **a single power law is invalid**.
> Three specific problems with the numbers above:
>
> 1. **Burn rate law invalid.** KNSB's exponent varies by pressure regime; a single `a`, `n` pair
>    cannot describe it. Burn time and chamber pressure are therefore **unreliable**.
> 2. **`a` is optimistic.** The calculation assumed dessicated materials. With **as-obtained**
>    sorbitol and granular KN, `a` will be **lower** → lower pressure, lower thrust, **longer burn**.
> 3. **Start-up risk not accounted for.** KNSB's low-pressure exponent near 0.3 (bottom of the usable
>    band) means the motor may **struggle to reach design pressure at all.**
>
> **The mass/impulse sizing (24 g propellant, ~24 N·s, ~72 m/s required burnout velocity) remains
> valid** — that comes from flight mechanics and drag, not from the burn-rate law. What must be
> re-solved is the **grain geometry, throat diameter and burn time**, once measured `a`/`n` data
> exists.
>
> ### Required before designing a throat
>
> - [ ] Build a **strand burner** (`staburn.html`) — the single highest-value first build
> - [ ] Measure `r` at **several pressures spanning 1–6 MPa** for **your** materials
> - [ ] Extract the regime-by-regime `a`, `n` pairs — **not** one global fit
> - [ ] Confirm `n` lands in **0.3–0.6** in your operating regime
> - [ ] Then re-solve grain geometry and throat size, with margin for start-up
>
> ### What is still trustworthy from this design
>
> - **Freestanding grain** — confirmed correct by KNSB's measured mechanical properties (§1.12)
> - **Port/throat ratio ≥ 2** — confirmed, and especially important given KNSB's susceptibility to
>   *negative* erosive burning (§1.11)
> - **Thin primer on all burning surfaces** — confirmed required (§1.13, §5.5)
> - **No single-grain inter-segment spacing needed** (rule applies to multi-segment BATES grains)
> - **Igniter must be small** — an oversized igniter in a small motor risks a startup pressure spike
>   and motor failure (§5.4)

**Throat sensitivity warning (why small motors are harder):**

| Throat dia | Drilling error | Δ Area | Δ Chamber pressure |
|---|---|---|---|
| **2.2 mm** | ±0.1 mm | ±9% | **±9%** |
| 22 mm | ±0.1 mm | ±0.9% | ±0.9% |

A 0.1 mm drilling wobble is routine and unremarkable on a 22 mm throat; on a 2.2 mm throat it is a
9% pressure swing. **This is the core difficulty of small motors, and the reason to keep throat
diameters as large as the design allows.**

---

*Compiled from Richard Nakka's Experimental Rocketry Site (nakka-rocketry.net). All safety-critical
figures should be verified against the original pages before use. This document is a study aid, not a
substitute for the source material.*
