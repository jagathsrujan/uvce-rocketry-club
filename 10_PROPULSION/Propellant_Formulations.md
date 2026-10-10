# UVCE Rocketry Club — Propellant Formulations

**Document:** `10_PROPULSION/Propellant_Formulations.md`
**Applies to:** All KNSB propellant prepared by UVCE Rocketry Club
**Status:** 🟢 Baseline formulation locked. Change control in force (§9).
**Parent references:** `Technical_Reference_Nakka.md` Part 1 and Part 2; `40_SAFETY/Safety_Manual_Master.md`

> 🔴 **THE ONE RULE OF THIS DOCUMENT**
> **You will make exactly one propellant: KNSB 65/35.** You will not modify it, "improve" it,
> substitute an ingredient, or add anything to it — not metal powders, not sulphur, not a different
> sugar, not a burn-rate catalyst. Every number in your motor design assumes this exact formulation.
> If you change the formulation, every number becomes fiction. See §9.

---

## 1. Formulation selection — why KNSB

### 1.1 The candidates

Three nitrate/sugar propellants are in common amateur use, all melt-cast, all in the same performance
family. They differ almost entirely in their **fuel's melting behaviour**, and that single difference
decides everything about how pleasant they are to cast.

| Property | KNSU (sucrose) | **KNSB (sorbitol)** | KNDX (dextrose) |
|---|---|---|---|
| Fuel formula | C₁₂H₂₂O₁₁ | **C₆H₁₄O₆** | C₆H₁₂O₆ |
| Fuel molecular weight (g/mol) | 342.3 | **182.2** | 180.16 |
| Fuel melting point (°C) | 185 (**decomposes**) | **110–112** | 146 (**decomposes**) |
| Fuel density (g/cm³) | 1.581 | **1.489** | 1.562 |
| Fuel enthalpy of formation (kJ/mol) | −2221.2 | **−1353.7** | −1274.5 |
| Fuel appearance | white granular | **white granular** | dry white powder |
| **Ideal cast propellant density (g/cm³)** | **1.888** | **1.841** | **1.879** |
| **Practical casting temperature** | **~160–170 °C** | **120–130 °C** | **~140–150 °C** |
| Caramelisation / pot life | Yes — **finite pot life** | **None — pot life effectively unlimited** | Some |
| Burn rate @ 1 atm | 3.8 mm/s | **2.59 mm/s** | ~3.4 mm/s |
| Burn rate @ ~6.9 MPa (1000 psi) | ~15 mm/s | **11.25 mm/s** | ~13 mm/s |
| Burn-rate character | Classic **St. Robert** (one power law fits) | 🔴 **MESA** (no single power law) | **Plateau** |
| Hygroscopicity of fuel | High | **Moderate — lower than KNSU** | Moderate–high |
| Handling of raw fuel | Free-flowing | **Cakes into hard clumps — must be sifted** | Free-flowing powder |
| Mechanical: rigid/brittle? | Yes | **Yes** | Yes |
| Chip resistance when sawn | Moderate | 🔴 **Poor — chips easily** | Moderate |
| Cure to handleable | ~1–2 days | **1–2 days (faster than the sugars)** | ~1–2 days |

> **Density note.** The three figures above (1.888 / **1.841** / 1.879 g/cm³) are *ideal cast
> densities* — the void-free value a good casting should approach. The club's QC benchmark for KNSB
> is **1.841 g/cm³**, and every grain density check is a ratio against that number.

### 1.2 The decision, point by point

**1. Casting temperature is the safety argument.** KNSB casts at **120–130 °C**; KNSU needs **~160–170 °C**
and decomposes at 185 °C. That 40–50 °C difference is the entire margin between "a controlled
melt-cast operation" and "a process running within a few tens of degrees of runaway." KNSB's
auto-ignition temperature is **> 300 °C** (verified by deliberate overheat test), so at a casting
temperature of 125 °C you hold a safety factor better than 2.4 on ignition temperature. With KNSU you
do not.

**2. No caramelisation means unlimited pot life.** Sucrose begins to caramelise on prolonged heating;
the slurry darkens, thickens, and eventually becomes uncastable. That puts a hard clock on your
casting operation and makes **large grains impractical**. Sorbitol does not caramelise at casting
temperature — you can hold the melt and take as long as you need. This is why KNSB is the standard for
large amateur grains up to M-class (Nakka's 89 mm *Muon*, six segments, 6 kg propellant).

**3. Slow freeze-up means fewer voids.** Sorbitol does not harden instantly on cooling. It forms a
soft transparent mass that can be cut and stretched, and only reaches full hardness after about five
days (KNSB propellant cures faster — 1 to 2 days to handleable). A slow, forgiving freeze gives
trapped air time to rise before the grain sets — directly attacking the **single largest CATO cause in
amateur sugar motors, which is voids and cracks**. KNSU's rapid freeze-up traps bubbles where they
form.

**4. Hygroscopicity.** Sorbitol as-obtained holds **more moisture than sucrose or dextrose**, but the
cast KNSB propellant itself is **less hygroscopic than KNSU** and is non-hygroscopic at moderate
humidity once cured. Net: raw-material drying matters more, finished-grain storage matters less.

**5. Mechanical properties.** All three are rigid, brittle, and weak in tension — this is a family
trait, not a KNSB defect. KNSB's measured properties are in §1.4, and they are the reason the club
uses **freestanding grains**. KNSB's one genuine mechanical liability is that it is **far more
susceptible to chipping than KNSU or KNDX** — obvious when cutting with a hand saw, and worse with a
coarse blade. Plan for this: use fine-tooth tooling, and never use the cut face as a burning surface
without inspecting it.

**6. Performance.** KNSB's specific impulse is **less than 1% below** sucrose-based propellant, its
combustion temperature is about **100 °C lower** (easier on nozzles and liners), its ideal density is
**2.5% lower**, and its combustion products are very similar. **You give up almost nothing for a much
safer and much easier casting operation.**

### 1.3 The one thing you are buying with that trade

🔴 **KNSB is a *mesa* propellant, and that is the price.** Over part of its pressure range the
pressure exponent `n` becomes very small or even negative. A single power law `r = a·Pⁿ` **does not
describe KNSB across all pressures.** KNSU follows St. Robert well; KNDX plateaus; KNSB is worse than
both to model.

**You are trading model simplicity for casting safety, and that is the correct trade for a beginner
club.** The cost is that you must measure your own burn rate (§`Motor_Test_Program.md`) instead of
copying a published exponent. That is a build cost, not a risk — and you were going to have to
measure it anyway, because your as-obtained materials will not match anyone else's data.

### 1.4 Locked material properties (design constants)

Every motor design in this workspace uses these figures.

| Property | Value | Source |
|---|---|---|
| Formulation | **65% KNO₃ / 35% sorbitol by mass** | verified |
| Ideal cast density | **1.841 g/cm³** (0.0665 lb/in³) | verified |
| Elastic (bending) modulus E | **5.84 GPa** (~850,000 lb/in²) | verified |
| Modulus of rupture F_b | **7.6 N/mm²** (~1100 lb/in²) | verified |
| Tensile strength F_tu | **7.2 N/mm²** (~1050 lb/in²) | verified |
| **Allowable tensile stress** | **≤ 0.20 × F_tu = 1.44 N/mm²** | verification rule |
| Auto-ignition temperature | **> 300 °C** | verified |
| Decomposition onset (colour change) | ~175 °C | verified |
| Visible smoking / strong odour | ~250 °C | verified |
| Casting temperature | **120–130 °C, ±5 °C** | verified |
| Burn rate @ 0.101 MPa | **2.59 mm/s** | measured (Nakka) |
| Burn rate @ 6.89 MPa | **11.25 mm/s** | measured (Nakka) |
| Burn energy | **~2.7 kJ/g** | verified |

> For comparison: E is similar to **bakelite**; F_tu is similar to **particleboard**. Neither is a
> compliment to a structural material.

---

## 2. The formulation table

### 2.1 Baseline — KNSB 65/35

| Component | Role | Mass fraction | Mass per 100 g |
|---|---|---|---|
| **Potassium nitrate, KNO₃** | Oxidiser | **0.650 (65.0%)** | 65.00 g |
| **Sorbitol, C₆H₁₄O₆** | Fuel + binder | **0.350 (35.0%)** | 35.00 g |
| **Sodium Laureth Sulfate (SLES)**, 70–80% concentrate | Casting surfactant | **0.001 (0.1%)** *of molten propellant mass* | 0.10 g |
| **Total** | | **1.000** | **100.10 g** |

**Notes on the table:**

- **O/F ratio by mass = 65/35 = 1.857.** This is the single fixed ratio. Do not vary it.
- **The SLES is added *after* melting**, as a fraction of the **molten propellant mass** — i.e. 0.1 g
  of SLES per 100 g of already-melted KNSB. It is not part of the dry blend. See §6.
- **Percentages are by mass, not volume.** Sorbitol (1.489 g/cm³) and KNO₃ (~2.11 g/cm³) differ
  enough in density that volume-based batching produces a badly wrong formulation. **Weigh everything.**
- **No other ingredient is permitted.** No sulphur, no charcoal, no metal powder, no iron oxide, no
  burn-rate catalyst, no plasticiser, no curing agent, no dye. See §8 and §9.

### 2.2 Raw material specification

| Item | Acceptable | Unacceptable |
|---|---|---|
| **Potassium nitrate** | 14-0-45 agricultural fertiliser, **98–99% purity**; or technical/lab grade | Anything with a stated anti-caking or dye additive you cannot identify |
| **Sorbitol** | Confectionery / diabetic-sweetener grade powder, **or** the SLES-free food grade | Any sorbitol product with added anti-caking agent, flavour, or lubricant |
| **SLES** | 70–80% **liquid concentrate**, or a foaming bath gel whose **first listed ingredient after water is Sodium Laureth Sulfate** | 🔴 **Sodium Lauryl Sulfate (SLS)** — a different chemical (§6.3) |
| **Water** | — | Any water intentionally added. Water is driven off, never added. |

**KN purity check — do this on every new bag.** Dissolve **33 g of KNO₃ in 100 ml of room-temperature
water**. Test with pH paper. The solution should be **neutral: pH 6.5–7.0.**

- **pH > 8 is a FAIL.** It means alkaline impurities (typically anti-caking agents). Alkaline KN
  produces **yellow/amber discoloured propellant**, which is **more hygroscopic** than white KNSB.
  Performance is not seriously degraded, but the grain will absorb moisture in storage and the
  discolouration itself is a visible sign your process is off.
- Colour guide during casting: **pure white = correct.** Yellow or amber = impurities. Track down the
  KN source.

**Sorbitol must be sifted, always.** Powdered sorbitol cakes into hard clumps in storage. Break the
clumps up with a flour sifter or by rubbing through a kitchen strainer before weighing. **Unsifted
sorbitol will not blend and will not melt uniformly** — you get lumps in the slurry and density
variation in the grain.

---

## 3. Batch scaling — worked examples

### 3.1 The excess rule

> **Prepare 20–25% excess for small batches.** The excess covers the propellant that stays on the
> stirring spoon, on the vessel wall, and in the pour path. Large batches need proportionally less —
> reduce the excess toward **10%** as the batch grows past about 1 kg.

| Batch scale | Recommended excess | Reason |
|---|---|---|
| 50–250 g | **+25%** | Large fraction of the batch is lost to vessel and utensil wetting |
| 250–1000 g | **+20%** | Standard |
| > 1000 g | **+10%** | Surface-to-volume losses become small |

### 3.2 Scaling table

| Target cast mass | 100 g | 250 g | 500 g |
|---|---|---|---|
| Excess applied | +25% | +20% | +20% |
| **Batch to prepare** | **125 g** | **300 g** | **600 g** |
| **KNO₃ (65.0%)** | **81.25 g** | **195.0 g** | **390.0 g** |
| **Sorbitol (35.0%)** | **43.75 g** | **105.0 g** | **210.0 g** |
| Dry blend total | 125.00 g | 300.0 g | 600.0 g |
| **SLES (0.1% of melt)** | **0.125 g** | **0.300 g** | **0.600 g** |
| Expected cast yield (void-free) | 125 g → grain mass ≈ **100 g** at 1.841 g/cm³ | ≈ **250 g** | ≈ **500 g** |
| Expected cast volume (void-free) | **54.3 cm³** | **135.8 cm³** | **271.6 cm³** |

**Volume check formula.** Void-free cast volume is simply:

$$V_{\text{cast}} \;=\; \frac{m_{\text{KNSB}}}{\rho_{\text{ideal}}} \;=\; \frac{m_{\text{KNSB}}}{1.841\ \text{g/cm}^3}$$

At **100 g**: V = 100 / 1.841 = **54.32 cm³**. Use this to check that your mould actually holds the
batch — a very common first-run error is preparing a batch larger than the mould.

### 3.3 Worked example — the 24 N·s motor grain (read this one carefully)

The club's first grain is a **33.0 mm long hollow cylinder, 24.0 mm OD, 9.0 mm core**. Work out its
mass *before* deciding how much to mix:

| Step | Calculation | Result |
|---|---|---|
| Grain cross-sectional area (annulus) | A = π/4 × (24.0² − 9.0²) mm² = π/4 × (576 − 81) | **388.77 mm²** |
| Grain volume | V = 388.77 mm² × 33.0 mm | **12,830 mm³ = 12.83 cm³** |
| Ideal mass | m = 12.83 cm³ × 1.841 g/cm³ | **23.62 g** |
| Allow for 3–5% voidage (realistic) | m ≈ 23.62 × 0.96 | **≈ 22.7 g** |
| 🔴 **Critical:** design propellant mass | The motor's impulse comes from the mass that is actually there | **Design assumption: 22.7–23.6 g** |

**But the *batch* is sized on the casting operation, not the grain:**

| Step | Calculation | Result |
|---|---|---|
| Grain volume | (above) | 12.83 cm³ |
| Casting loss factor (+25%, small batch) | 12.83 × 1.25 | 16.04 cm³ |
| Batch mass to prepare | 16.04 × 1.841 | **29.5 g cast mass** |
| Dry blend to weigh (same number, before melting) | Must be **≥ 29.5 g** plus melt-loss allowance | **Prepare 35 g dry blend** |
| → KNO₃ | 35 × 0.65 | **22.75 g** |
| → Sorbitol | 35 × 0.35 | **12.25 g** |
| → SLES (after melting) | 29.5 × 0.001 | **0.030 g** |

> ⚠️ **Do not round the SLES to zero.** 0.030 g of SLES in 29.5 g of melt is what turns a
> scoop-and-scrape operation into a pour. Measure it on a **0.001 g resolution scale**. If your only
> scale resolves to 0.1 g, weigh a larger batch, or make a premix: 1 g SLES in 99 g water, then dose
> 3.0 g of premix and heat off the water. (The premix route adds water you must then boil off — see
> §5.3. Prefer the 0.001 g scale.)

> 🔴 **The 35 g blend produces a ~23 g grain, not a 35 g grain.** Roughly a quarter of the batch is
> designed to be lost. If you need a 35 g grain, prepare ~52 g of blend. **Always compute the required
> blend from the grain volume first.** Casting short means re-melting and re-pouring, which ruins the
> grain; casting long means leftover propellant you must dispose of safely.

### 3.4 Dry-blend worksheet (photocopy this)

```
BATCH RECORD — KNSB 65/35
Date: __________   Operator: __________   Witness: __________

Target grain mass            m_grain  = _______ g
Target grain volume          V_grain  = _______ cm^3   (= m_grain / 1.841)
Excess factor                f        = _______       (1.25 / 1.20 / 1.10)
Blend mass required          m_blend  = V_grain * 1.841 * f  = _______ g

  KNO3      = m_blend * 0.650 = _______ g      Weighed: _______ g
  Sorbitol  = m_blend * 0.350 = _______ g      Weighed: _______ g
  Sum                          = _______ g      Scale check: OK / NOT OK

  SLES      = m_blend * 0.001 = _______ g      (added AFTER melting)

KN purity check:  33 g KN / 100 ml water, pH = _______   PASS (6.5-7.0) / FAIL
KNO3 mill time: _______ s        Sorbitol sifted: Y / N
Desiccated: Y / N   Days: _______   Desiccator charge date: __________

Casting vessel preheated to: _______ C     Target 120-130 C +/- 5 C
Melt start time: ________   Casting temp reached: ________   Pour time: ________
Tap-out performed: Y / N     Coring rod lubricated: Y / N     Fully seated: Y / N

Cure start: ________   Demoulded: ________   Density check: _______ g/cm^3  Ratio: _______
Tap test: PASS / FAIL     Segment ID: ________     Outcome: ____________________
```

---

## 4. Oxidiser particle size — the performance/viscosity trade

### 4.1 The grinding procedure

| Step | Detail |
|---|---|
| Equipment | **Electric coffee grinder** (blade type). Dedicate one grinder to KNO₃ and label it permanently. **Never grind sorbitol or any other material in it afterwards.** |
| Charge | **~2 tablespoons (≈30 ml) per load.** Do not overfill — the grinder needs headspace to circulate. |
| Time | **15–30 seconds**, **slowly "gyrating" the grinder** while it runs. Gyration keeps the charge moving so it does not pack into a dead zone under the blades. |
| Result | **50% of particles below 74 µm**, most of the remainder below 234 µm. |

### 4.2 What particle size actually does

| Effect | Coarse / short grind | Fine / long grind |
|---|---|---|
| **Burn rate** | **Lower** — across the entire pressure range | Higher |
| **Chamber pressure at a given throat** | Lower | Higher |
| **Burn time** | Longer | Shorter |
| **Combustion efficiency** | Lower | Higher |
| **Slurry viscosity** | **Fluid — pourable, even without much surfactant** | **Thick — must be scooped, not poured** |
| **Void risk** | Lower (better flow) | **Higher** (trapped air in a thick slurry) |
| **Consistency between batches** | Depends on grind repeatability | Depends on grind repeatability |

> **Verbatim from the reference:** *"Grinding time controls slurry viscosity. Finer grind = better
> performance but thicker slurry that must be scooped, not poured. Shorter grind (≤10 s) or 'as
> obtained' fine granular KN gives a more fluid slurry — at the cost of reduced performance."*

### 4.3 The trade, stated plainly

You are choosing between **performance** and **castability**, and **castability wins**.

A thick, un-pourable slurry is a slurry you cannot de-air. Every extra bubble you trap is a local
burning-surface multiplier (bubbles are internal free surfaces — when the flame front reaches one, the
burning area jumps) and a local stress raiser in a material whose tensile strength scatters from 436
to 1050 lb/in² with no visible flaw. **A 3% denser grain with 1% voidage beats a 5% higher burn rate
with 6% voidage, every time.**

**Club policy:**

1. **Standard grind: 20 s with gyration**, single pass, 30 ml loads. This is the baseline. Record it.
2. **Do not chase a finer grind for more performance at the 24 mm scale.** You have almost no
   performance margin to spend and a large castability margin to lose.
3. **If you change grind time, you have changed the formulation.** Grind time is a **process
   parameter under change control** (§9). A grind change requires re-measurement on the strand burner.
4. 🔴 **Grind repeatability is what makes your burn-rate data meaningful.** A random grind means a
   random burn rate means an unpredictable chamber pressure. Time every load with a stopwatch. Do not
   grind "until it looks right."
5. **Record the sieve result once per grinder setting.** A 10-minute sieve analysis on a 100 g sample
   (stack of 74 µm and 234 µm sieves, shaken by hand for 10 minutes) tells you whether your 20 s is
   actually producing the same distribution as last month.
6. **Granular (unground) KN will behave differently and better-modelled** — granular KN follows
   St. Robert reasonably well and **does not show mesa behaviour**. If your strand-burner data comes
   back ugly, this is a legitimate, controlled fallback, and it is the route Gudnason's 2010 thesis
   used with less scatter than earlier work.

### 4.4 Milling hazards

| Hazard | Control |
|---|---|
| **Dust explosion** — fine KNO₃ dust is an oxidiser; fine organic dust is a fuel; mixtures are worse | Grind KNO₃ **alone**. Never grind a KNO₃/sorbitol blend. Never grind in a confined space. Work in a ventilated area. |
| **Static discharge** | Ground the grinder body. Avoid plastic containers that hold charge. Never use a vacuum to clean up powder. |
| **Cross-contamination** | The grinder is dedicated to KNO₃ for the life of the club. Label it. Store it with the propellant equipment, not in the kitchen. |
| **Ignition source** | The grinder's own motor brushes can spark. Never operate a grinder with the lid off or a damaged cord. |

---

## 5. Moisture and dessication

### 5.1 Why moisture matters — the verified mechanism

> ✅ **Residual moisture in the sorbitol suppresses burn rate by reducing the burn-rate coefficient
> `a`. It does NOT change the pressure exponent `n`.** Fine-dessicated and granular KNSB show
> **identical log-log slopes**.

This is a very useful fact, because it splits the problem cleanly:

- **`n` (the slope) is a material property.** You measure it once and it holds.
- **`a` (the coefficient) is a process property.** It depends on how wet your sorbitol is, and
  therefore on *your* storage, *your* dessication, and *your* batch.

**The practical consequence for your design:** the two anchor points in §1.4 come from dessicated
materials run with excellent experimental technique. **Your as-obtained materials will give a lower
`a`.** Lower `a` means lower chamber pressure, lower thrust, and a longer burn than a dessicated
design predicts — at the same throat area. Your motor will under-perform its prediction, not
over-pressurise. That is the safe direction to be wrong, but it is still wrong, and it is why
**`a` must be measured for your materials, not borrowed.**

**Sorbitol is the culprit** — as-obtained sorbitol holds more moisture than sucrose or dextrose. The
KNO₃ is comparatively dry.

**What moisture does in the melt:** if sorbitol has residual moisture, melting is **rapid**, and the
slurry looks **pure white / almost translucent with tiny bubbles as the water boils off**. As the
water is driven off, the colour shifts to **light ivory**. You can literally watch your moisture
content leave the pot. If your slurry goes white-and-bubbly and then ivory, you had moisture. If it
goes straight to ivory, your sorbitol was dry.

### 5.2 The calcium chloride desiccator

**Build:**

1. **Container:** an airtight plastic storage box or large Tupperware with a well-sealing lid.
2. **Desiccant bed:** a layer of **a few centimetres of fresh calcium chloride** (CaCl₂) in the
   bottom. CaCl₂ is cheap, available at hardware/chemical suppliers, and is strongly hygroscopic.
3. **Barrier:** a perforated plate, mesh, or a few layers of paper towel over the desiccant so the
   sorbitol does not touch the CaCl₂ directly. **CaCl₂ will deliquesce into a brine puddle** — you do
   not want your sorbitol sitting in it.
4. **Sample:** **sift the sorbitol into a shallow pan** to give a large surface area. A 2 cm deep
   layer of sifted powder dries far faster than a 10 cm heap.
5. **Time:** **1–2 days** in the desiccator.

**Maintenance — this is where clubs fail:**

| Task | Frequency |
|---|---|
| Inspect the CaCl₂ | Every use. If it is wet, clumped, or sitting in liquid, it is spent. |
| Replace the CaCl₂ | **Monthly**, or whenever it shows wetness. **Fresh CaCl₂ is not optional** — spent desiccant is worse than none because it gives false confidence. |
| Label the charge date | On the lid, in marker. Anyone can then tell at a glance whether the bed is fresh. |
| Keep the lid closed | Seconds of open lid in a Bengaluru monsoon re-wets the bed. |

> **Bengaluru-specific:** relative humidity swings hard with the monsoon (June–October) and sits
> high year-round relative to continental climates. **Assume your sorbitol is wet.** Dessicate as the
> default, not the exception, and re-dry the desiccant on a monthly clock. If you skip dessication in
> July, your burn rate will not match your March data, and you will chase a phantom.

### 5.3 The tradeoff — dessication makes casting harder

> ⚠️ **Dessicated sorbitol gives a stiffer, more viscous slurry — harder to cast.**

Drying the sorbitol raises the melt viscosity. You are trading:

| | Dessicated sorbitol | As-obtained sorbitol |
|---|---|---|
| Burn-rate coefficient `a` | **Higher** (better performance) | Lower |
| Slurry viscosity | 🔴 **Stiffer — harder to pour, harder to de-air** | More fluid |
| Void risk | Higher (unless SLES is used) | Lower |
| Batch-to-batch consistency | Good (if dessication is consistent) | Poor (varies with weather and storage) |

**How the club resolves this — three controls, used together:**

1. **Dessicate, always, and always for the same time (2 days).** Consistency matters more than the
   absolute dryness. A constant `a` you have measured beats a higher `a` you have not.
2. **Use the SLES surfactant (§6) to buy the pourability back.** This is precisely what the surfactant
   is for — it decouples "dry propellant" from "uncastable slurry."
3. **Never add water back.** If the slurry is too stiff, the fix is more SLES, more heat soak within
   the 120–130 °C band, or more stirring time — never water.

### 5.4 Moisture in the finished grain

| Stage | Behaviour |
|---|---|
| Freshly cast | Surfaces are soft; grain is pliable and deforms if handled carelessly |
| After 1 day | Exposed surfaces quite hard; interior still waxy but rigid enough to handle |
| **Demould** | **After 1–2 days of cure** — demoulding too soon distorts the grain when extracting the coring rod |
| Full cure | May take a week (surface hardens ~2–3 days, fully hard ~5 days) |
| **Firing** | ✅ **It is acceptable to fire a grain any time after demoulding.** You do not have to wait for full cure. |
| Tap test | **Only after full cure** — residual moisture in the bondline causes false disbonding indications |

> **Tap-test false-fail recovery:** if a segment fails the tap test, a few days in a desiccator often
> converts it to a pass. That is a moisture artefact in the bondline, not a real disbond.

---

## 6. The surfactant casting aid — SLES

### 6.1 What it does

Molten KNSB at the correct formulation is **too viscous to pour**. It must be scooped with a spoon or
silicone spatula and pressed into the mould. That is workable for a 33 mm grain; it is miserable for
a 500 g grain and unworkable for a multi-segment BATES stack.

A **tiny amount of surfactant** changes this completely — Nakka reports the melt becomes
**"readily pourable, having a viscosity similar to maple syrup."** The viscosity drop is immediate on
stirring.

### 6.2 Specification

| Item | Value |
|---|---|
| Chemical | **Sodium Laureth Sulfate (SLES)** |
| Form | 70–80% liquid concentrate |
| Dosage | **~0.1% by mass of the molten propellant** |
| When to add | **To the fully molten KNSB**, then stir |
| Effect | **Immediate viscosity drop** |
| Availability | Cheap and widely available (soap/shampoo base ingredient); ~500 ml lasts the club years |

**Retail substitute:** a **foaming bath gel** works **if its main listed ingredient (other than water)
is SLES**. Caveat: it contains appreciable water, so **more may be needed and extra heating is
required to drive the water off.** Extra heating means extra time near the top of the 120–130 °C band,
which is extra risk. **Prefer the concentrate.**

### 6.3 🔴 SLS is NOT SLES

> **Sodium Lauryl Sulfate (SLS) is a different product and may not work as effectively.**

They are different molecules with different hydrophilic–lipophilic balance and different behaviour in
a molten sugar melt. **Read the label. If it says Sodium Lauryl Sulfate, put it back.** This is a
trivially avoidable mistake that will lead to a wasted batch and — worse — a batch where you do not
know whether the viscosity problem was the surfactant or your process.

**Label the container at the club as "SLES — CASTING AID ONLY" and store it separately from SLS if
anyone brings SLS in for other purposes.**

### 6.4 Dosage discipline

- **0.1% is the number.** Not "a squirt." Not "a bit more for luck."
- **Overdosing is a formulation change** (§9). Excess surfactant is an organic additive in the
  propellant; it will shift the burn rate and the mechanical properties, and you have no data for
  what it does.
- **Weigh it.** 0.030 g for a 30 g batch requires a 0.001 g scale.
- **Add after melting, never to the dry blend.** The dry blend is **readily combustible** — do not
  add liquids to it, do not add it to hot surfactant, do not agitate it unnecessarily.

---

## 7. Storage, shelf life, and hygroscopicity

### 7.1 Raw materials

| Material | Storage | Shelf life | Notes |
|---|---|---|---|
| **Potassium nitrate** | Airtight container, cool, dark, dry. **Stored separately from fuels and from all organics.** | Effectively indefinite if kept dry and sealed | 🔴 **Oxidiser. Never store it in the same cabinet as sorbitol, charcoal, sulphur, or any fuel.** Segregate. This is a fire-load rule, not tidiness. |
| **Sorbitol** | Airtight container. It **cakes** — expect it. | 2+ years | Re-sift before every use. Dessicate before use (§5.2). |
| **SLES concentrate** | Sealed, room temperature | 2+ years | Keep water out. |
| **Mixed dry blend (KNO₃ + sorbitol)** | 🔴 **Airtight, immediately, and use the same day.** Keep away from **all** ignition sources. | 🔴 **Hours, not days.** Do not store mixed blend. | **The mixed powder is readily combustible.** Blend it, then melt it. Do not leave a bowl of it on the bench overnight. |
| **Calcium chloride** | Sealed when not in the desiccator | Replace monthly in service | Deliquesces; spent desiccant is a trap. |

### 7.2 Finished grains

| Item | Guidance |
|---|---|
| **Cure before demould** | 1–2 days |
| **Full cure** | Up to a week (surface 2–3 days, through-hard ~5 days) |
| **Fireable** | ✅ Any time after demoulding |
| **Storage container** | Airtight, with a desiccant charge inside. Sealed ammo can or a Tupperware with fresh CaCl₂ in a perforated bag. |
| **Storage location** | 🔴 **Only in the club's licensed/approved propellant store. NEVER in a hostel room, lab, workshop, or vehicle.** |
| **Storage temperature** | Cool and stable. Avoid vehicles and direct sun — thermal cycling cracks brittle grains. |
| **Shelf life of a good grain** | **Months**, if sealed and dry. Practically, **fire grains within 3 months** and re-inspect. |
| **Failure modes in storage** | Moisture uptake (softening, tacky surface); chipping and cracking from handling; **inhibitor disbond** from moisture in the bondline; sag/deformation if stored on its side unsupported. |
| **Pre-fire inspection** | Visual: no cracks, no chips on burning surfaces, no discolouration. **Density check and tap test re-run** if the grain has been stored more than a month. |

### 7.3 Hygroscopicity — the honest picture

| Material | Hygroscopicity |
|---|---|
| Sorbitol (raw) | **High — worse than sucrose or dextrose as-obtained.** This is the single biggest source of batch-to-batch burn-rate scatter. |
| Cast KNSB, pure white | **Less hygroscopic than KNSU.** Non-hygroscopic at moderate humidity once cured. |
| **Discoloured (yellow/amber) KNSB** | 🔴 **More hygroscopic than pure white KNSB.** Caused by alkaline impurities (anti-caking agents) in the KN. Performance is not seriously degraded, **but the grain will pick up moisture in storage.** Reject or use first. |
| KNSU | More hygroscopic than KNSB |
| KNDX | Intermediate |

> **The colour of your propellant is a moisture specification.** White = sealed and stable.
> Ivory = normal process endpoint. **Yellow/amber = hygroscopic, investigate the KN source, and
> prioritise firing that batch rather than storing it.**

---

## 8. Hazard review of the process

### 8.1 The energy argument — internalise this before melting anything

| Quantity | Value |
|---|---|
| Burn energy of sugar propellants | **~2.7 kJ per gram** |
| Energy in 1 kg of KNSB | **2.7 megajoules** |
| Equivalent | **A 1000 W heater running for 45 minutes** |
| Released in | **2–3 seconds** |
| AP-based propellants | **Nearly double** this energy density |

Your 23 g first grain holds about **62 kJ** — the energy of a 1000 W heater running for a full
minute, released in under two seconds. Your 500 g batch holds **1.35 MJ**. Treat the melt accordingly.

### 8.2 The three items that must ALWAYS be present

Per the club safety framework, before any propellant work begins:

1. **A dunk bucket full of water**
2. **A fire extinguisher**
3. **A planned escape route**

If any one is missing, **the work does not start.** No exceptions, no "it's only a small batch."

### 8.3 Process hazards and controls

| Hazard | When | Control |
|---|---|---|
| **Ignition from an exposed heating element** | Melting | 🔴 **Only a thermostatically temperature-controlled heating vessel with NO exposed elements** — a thermostatically controlled electric deep fryer or skillet. **The critical intent: no exposed heating surface significantly hotter than the propellant's melting point.** ⚠️ If surfaces get hot *before* the powder is added, **ignition can occur immediately**. |
| **Overheating the melt** | Casting | Hold **120–130 °C, ±5 °C**. Monitor with a candy thermometer, digital probe, or (most convenient) an **infrared thermometer**. Watch for the warning indicators: **colour change ~175 °C, smoking and strong odour ~250 °C.** Auto-ignition **> 300 °C**. |
| **Static / electrical discharge** | Grinding, blending, pouring | Ground equipment. No synthetic clothing. No vacuum cleaning. Non-sparking tools. |
| **Dust ignition** | Grinding KN, blending, filling the igniter straws | Grind KN alone. Blend in a closed tumbler. Keep quantities minimal. |
| **Slurry splash / boil-over** | Casting, especially wet sorbitol | Face shield and apron. Wet sorbitol boils violently as water flashes off. Add powder in two halves, per procedure. |
| **Burns** | Everything | 🔴 **Face and hand protection as a minimum.** Long sleeves, no synthetics, leather or heat-resistant gloves for the pour. |
| **Fume inhalation** | Melting, casting | Ventilated area or fume extraction. KNO₃/sugar melts give off irritant fumes well before they ignite. |
| **Product left unattended** | Any stage | **No member works on energetic materials alone. Ever.** |
| **Residual melt in the vessel** | Cleanup | Let it cool and set. **Scrape it out — never re-melt a scraped crust you cannot identify.** Dispose per the club's propellant disposal SOP, not down a drain. |

### 8.4 🔴 Perchlorate propellants — explicitly out of scope

**This is not a "later, when we're experienced" item. It is a "not in this club, on this programme" item.**

> **Club safety framework, rule 14:** *"High-energy oxidisers for propellants (potassium perchlorate,
> ammonium perchlorate) should only be used by those with years of experience working safely with
> lower-energy oxidisers such as the nitrates. Only proven methods and formulations. Perchlorates
> 'have the potential to be frighteningly hazardous when combined with incompatible binders or
> additives, and even small motors can explode with shocking violence.'"*

**Justification, stated for the record:**

1. **Energy density.** AP-based propellants hold **nearly double** the energy of a nitrate/sugar
   propellant per gram. **A small APCP motor contains as much energy as a KNSB motor roughly twice its
   size** — so "we'll only make a small one" does not bound the hazard the way it does with KNSB.
2. **Sensitivity and violence of failure.** Perchlorates combined with incompatible binders or
   additives can detonate rather than deflagrate. The failure mode is not a split case; it is an
   explosion. The reference's words are "shocking violence," and they are not rhetorical.
3. **Incompatibility complexity.** APCP is a *composite* system — oxidiser, binder, plasticiser,
   curative, burn-rate modifier, bonding agent. Every pairwise compatibility is a materials-science
   question. Getting it wrong is not a performance penalty; it is a detonation.
4. **Propellant development is explicitly out of scope for beginners.** The reference is unambiguous:
   *"Beginners should stick to well-proven propellants and well-proven motor designs. Propellant
   development is best left to those with real experience and theoretical knowledge."*
5. **You gain nothing you need.** Amateur KNSB motors reliably deliver 115–130 s of delivered Isp.
   That is entirely sufficient for your entire roadmap — through 38 mm, 54 mm, 75 mm and 94 mm
   motors. The performance gain from APCP is not the constraint on any mission this club has.
6. **Regulatory and institutional exposure.** Perchlorate oxidisers draw a materially harder
   regulatory and institutional-permission burden, and would put the club's charter, its college
   relationship, and its members at risk in a way nitrate propellants do not.

**If a future member proposes APCP: the answer is no, and the answer is recorded here so that the
argument does not have to be had again.** A perchlorate proposal requires, at absolute minimum, a
documented programme at the scale below it, a written institutional safety review, and a change to
this document approved by the same process as §9 — which for perchlorates includes an external
qualified reviewer. Not one of those can be satisfied by a student team in its first years.

> ✅ **Update — the grain primer is RESOLVED. Do not use the perchlorate version.**
>
> The documented KNSB **grain primer** in Nakka's *igniter* page uses potassium perchlorate.
> **Do not use it.** A **nitrate-based primer is fully documented** in
> [`Ignition_System_Design.md`](Ignition_System_Design.md) **§2**:
>
> - **Recipe:** finely ground Ignition Powder (80% KNO₃ / 20% charcoal, no sulphur) + **70%
>   isopropyl alcohol** to a thick-paint consistency
> - **Application:** a **single thin coat** with a fine paintbrush — measured **200 µm (0.0075 in)**
> - **Coverage:** the core and both end faces
> - **Drying:** 24 h, or ~30 min air then desiccator
> - **Measured effect:** KNSB time-to-ignition improves from **19.9 s bare to 5.8 s primed**
>
> The perchlorate rule still applies to pyrolants, just at a different scale threshold (rule 13
> permits *small quantities* of high-energy oxidisers in igniter pyrolants, but only with proven
> formulations — and a nitrate-based primer is both proven and available, so there is no reason to
> take the perchlorate risk).

---

## 9. Formulation change control

### 9.1 Why beginners must not invent or modify formulations

> **Club safety framework, rule 12:** *"Beginners should stick to well-proven propellants and
> well-proven motor designs. Propellant development is best left to those with real experience and
> theoretical knowledge. **Even small amounts of certain additives can dramatically change burning
> characteristics, leading to catastrophic failure of otherwise well-proven designs.**"*

The operative phrase is **"even small amounts."** Consider the scale of the effect you are playing
with:

| "Small" change | What it actually does |
|---|---|
| 0.1% SLES | Viscosity drop from "unpourable" to "maple syrup" — a **process-changing** effect at one part in a thousand |
| 0.1% iron oxide | A classic burn-rate catalyst. Can shift `a` and **`n`** materially. |
| 1% metal powder | Raises combustion temperature, raises Isp, and **raises the thermal load on your nozzle and liner beyond their design point** |
| 5% O/F shift | Moves you off the optimum; changes flame temperature, c*, and the exhaust's condensed-phase fraction |
| 2% sulphur | Classic black-powder ingredient. **Dramatically increases ignition sensitivity** — which is exactly what you do *not* want in a propellant grain. |
| A different KN grind | Changes `a` and `n` and the slurry rheology |

Now the critical point: **your motor design is a single, coupled system.** Throat area was sized from
a mass-flow balance that contains `a` and `n`. Burn time came from web thickness divided by `r(P)`.
Chamber pressure came from `Kn`. **Change `a` upward by 20% and your chamber pressure rises by
`1.20^(1/(1−n))` — at `n = 0.3`, that is a 30% pressure increase.** Your case was sized with a 1.5×
minimum margin. You have just eaten a third of it with a change nobody costed.

**And an increase in `a` is not the only bad direction.** Change `a` downward and the motor will not
come up to pressure — KNSB's low-pressure exponent already sits at the bottom of the usable band
(`n ≈ 0.3`), and the documented failure mode is *"the motor simply refusing to come up to pressure."*
You will have built a motor that chuffs, dribbles propellant out of the nozzle, and slumps the grain.

**A third failure mode is worse than either:** a change that pushes `n` above about 0.6. Above that,
the motor's response to a pressure perturbation grows faster than the nozzle can relieve it. You are
now on the wrong side of a stability boundary, and the outcome is a pressure spike and a burst case.
**You cannot see `n` change by looking at the propellant.** It looks identical.

**Therefore:** the formulation is **frozen**. You are not doing propellant development. You are doing
**process control** on a known formulation, which is a completely legitimate and much more valuable
first-year activity — and it produces the strand-burner data you actually need.

### 9.2 What counts as a change (all of these are changes)

| Category | Examples |
|---|---|
| **Composition** | Any O/F variation. Any additive. Any removal. Any substitution of a raw material grade or supplier. |
| **Particle size** | Grind time, grinder type, sieve fraction, or switching to as-obtained granular KN |
| **Moisture** | Starting or stopping dessication; changing dessication duration; a change of desiccant or desiccator |
| **Surfactant** | SLES concentration; switching to SLS; switching to a bath gel; using a different concentrate strength |
| **Process** | Casting temperature, hold time, stirring method, tap-out procedure, coring-rod lubricant, cure time before demould, cure environment |
| **Geometry interaction** | Changing the coring rod diameter or the mould — these change `Kn`, which is a *motor* change even though the propellant is identical |

### 9.3 The change-control process

**No formulation change proceeds without all six steps. Steps 4 and 5 are the expensive ones, and they
are what makes this a real process rather than a formality.**

| # | Step | Evidence required |
|---|---|---|
| **1** | **Written proposal** | One page: what changes, why, the suspected mechanism, and the *predicted* direction and magnitude of the effect on `a`, `n`, and Isp. **A prediction is mandatory** — a change with no prediction cannot be falsified, and a change that cannot be falsified is not engineering. |
| **2** | **Hazard review** | Signed review against §8. New chemical? New incompatibility? New sensitivity? New thermal load? Review by at least two members plus the faculty advisor. |
| **3** | **Batch documentation** | Prepare a full batch record (§3.4) for both the baseline and the modified formulation, from the same raw-material lots. |
| **4** | 🔴 **Strand-burner measurement** | **Measure `r(P)` for the modified formulation over at least 1–6 MPa, and extract regime-by-regime `a` and `n`.** Compare against the baseline curve measured on the same apparatus. **A change with no strand data does not pass.** This is non-negotiable. See `Motor_Test_Program.md` §4. |
| **5** | 🔴 **Three identical motors** | **Fire three motors with the modified formulation, plus three with the baseline, and demonstrate overlapping thrust curves.** The acceptance test is *repeatability*, not peak performance. See `Motor_Test_Program.md` §8. |
| **6** | **Design impact assessment** | Re-solve the motor design with the new `a`/`n`: throat area, chamber pressure, burn time, MEOP, case margin, port-to-throat ratio throughout burn. **If MEOP rises, the case must be re-analysed and re-proof-tested.** |

**Only after all six steps** is the change accepted, and it is accepted by **amending this document
with a revision number and a date**, never by word of mouth. "We changed it last month" is not a
change record.

### 9.4 The default answer

> **The default answer to any formulation proposal is NO, and the burden of proof is entirely on the
> proposer.**
>
> A proposal that cannot produce step-4 and step-5 evidence is not rejected on opinion — it is
> **deferred until the club has a strand burner and three-motor repeatability at the current scale.**
> That is the honest reason most proposals will wait: **you do not yet have the instruments to
> evaluate them.**

### 9.5 What you *are* allowed to improve

Frozen formulation does **not** mean frozen process. The following are **process improvements**, and
they are actively encouraged because they reduce scatter without changing the propellant:

| Allowed, encouraged | Why it is safe |
|---|---|
| Better grind **repeatability** at the fixed 20 s setting | Tightens the particle-size distribution going *into* the same formulation. Measure and record the sieve result. |
| Consistent 2-day dessication | Removes a weather-dependent variable. Same formulation, lower variance. |
| Better mixing (longer tumble, better tumbler) | Attacks the "complete mixing is required" requirement. Reduces density and burn-rate scatter. |
| Better de-airing (tap-out technique, vibration, vacuum degassing if you have it) | Directly attacks the #1 CATO cause — voids. |
| Better mould release and coring-rod lubricant technique | Reduces surface defects, which are stress raisers. |
| Slower, more controlled cooling | Reduces thermal cracking. **Cracks are the #1 CATO cause.** |
| Better QC records | Makes every future investigation possible. |

> **The unifying principle:** you may change **how consistently you make the same thing**. You may not
> change **what the thing is**.

---

## 10. Quick reference card

**Print this and put it on the wall of the propellant preparation area.**

```
=============================================================================
 KNSB 65/35  --  UVCE ROCKETRY CLUB  --  ONE FORMULATION ONLY
=============================================================================
 COMPOSITION (by MASS)          KNO3  65.0 %   |   SORBITOL  35.0 %
 SURFACTANT                     SLES   0.1 % of MOLTEN mass  (after melting)
                                *** NOT SLS ***  read the label
 NO OTHER INGREDIENT IS PERMITTED.

 IDEAL CAST DENSITY             1.841 g/cm^3      QC ratio = measured/1.841
 CASTING TEMPERATURE            120 - 130 C  +/- 5 C
 AUTO-IGNITION                  > 300 C     (colour change ~175 C, smoke ~250 C)
 HEATING VESSEL                 THERMOSTATIC, NO EXPOSED ELEMENTS.  NO EXCEPTIONS.

 KN GRIND                       15-30 s, ~30 ml/load, gyrate  (50 % < 74 um)
 SORBITOL                       SIFT it.  DESSICATE it 1-2 days over FRESH CaCl2.
 KN PURITY CHECK                33 g KN / 100 ml water  ->  pH 6.5 - 7.0
 EXCESS BATCH                    +25 % small batches, +20 % large
 CURE                           1-2 days before demould; fireable any time after

 MASS CHECK                      V_cast = m / 1.841    (cm^3 per gram x 0.5432)

=============================================================================
 BEFORE YOU START -- ALL THREE, EVERY TIME:
     [ ] DUNK BUCKET FULL OF WATER
     [ ] FIRE EXTINGUISHER
     [ ] PLANNED ESCAPE ROUTE
     [ ] FACE + HAND PROTECTION
     [ ] NO MEMBER WORKS ALONE.  EVER.
=============================================================================

 PERCHLORATES (AP / KP):  NOT IN THIS CLUB.  See Propellant_Formulations.md section 8.4.

 FORMULATION IS FROZEN.  Process improvement yes.  Recipe change: change control, section 9.
=============================================================================
```

---

## 11. Cross-references

| For | See |
|---|---|
| Why `a` and `n` must be measured for your materials | `Motor_Test_Program.md` §4 (strand burner) |
| How `a` and `n` enter the motor design | `Motor_Design_Guide.md` §2–§4 |
| The mesa-propellant consequence | `Technical_Reference_Nakka.md` §1.11 |
| Grain QC (density check, tap test) | `Technical_Reference_Nakka.md` §1.8 |
| Ignition powder and grain primer | `Ignition_System_Design.md` |
| Scale-up sequence and gate criteria | `Propulsion_Roadmap.md` |
| Safety framework (rules 1–14) | `Technical_Reference_Nakka.md` Part 2 |

---

*UVCE Rocketry Club — `10_PROPULSION/Propellant_Formulations.md`. Baseline formulation locked at
KNSB 65/35, ideal cast density 1.841 g/cm³. All values traceable to `Technical_Reference_Nakka.md`
Part 1 unless marked as club policy. This document is subordinate to
`40_SAFETY/Safety_Manual_Master.md`.*
