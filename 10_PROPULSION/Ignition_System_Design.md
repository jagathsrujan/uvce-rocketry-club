# UVCE Rocketry Club — Ignition System Design

**Document:** `10_PROPULSION/Ignition_System_Design.md`
**Applies to:** every igniter, grain primer and firing circuit used on a UVCE Rocketry motor
**Status:** 🟢 Buildable. Every number in §1–§6 is traceable to the source reference.
**Parent references:** `Technical_Reference_Nakka.md` Part 5; `80_REFERENCE/nakka-technical-reference.md`
§1–§3; `Propellant_Formulations.md` §8.4; `40_SAFETY/Static_Test_Procedure.md` §4

> 🔴 **THE ONE SENTENCE THAT JUSTIFIES THIS DOCUMENT**
> **KNSB does not caramelise.** Every other sugar propellant gives you a free ignition aid — it partially
> decomposes on heating and lights itself. KNSB does not, and it is therefore **4.15× harder to ignite**
> than KNSU under identical conditions. **On this propellant, the igniter is not an accessory. It is the
> difference between a motor and a motor that chuffs, slumps its grain and burns a third of its
> propellant at atmospheric pressure.**

---

## 1. Why ignition is a first-class problem for KNSB specifically

### 1.1 The measured data — Nakka's Propellant Igniteability Experiment

**Method.** Slugs cast in **1 in PVC pipe rings** onto galvanised sheet steel (giving one smooth "test"
surface). **0.931 in (24 mm) diameter × 0.40 in (10 mm) long, 8 g each.** Batches of **123 g
(80 g oxidiser / 43 g fuel)**. Dextrose oven-dried to anhydrous; all constituents coffee-ground and
**blended 3 hours** before casting. **KNSB cured ≥ 24 h after casting.** Ignition source: **butane "BBQ"
lighter held 25 mm from the surface**, flame normal to the surface, maximum flowrate. A steel flame
shield was withdrawn to start timing; timing by videotape. **n = 5 specimens per propellant.**

**Result — time to ignition, seconds (uncoated):**

| Test # | KN-Sucrose (KNSU) | KN-Dextrose (KNDX) | **KN-Sorbitol (KNSB)** |
|---|---|---|---|
| 1 | 4.7 | 7.4 | 17.7 |
| 2 | 5.9 | 8.0 | 22.0 |
| 3 | 4.3 | 8.1 | 16.4 |
| 4 | 4.8 | 7.2 | 22.8 |
| 5 | 4.3 | 8.6 | 20.4 |
| **Average** | **4.8** | **7.9** | **19.9** |

**Normalised to KNSU:**

| Propellant | Average time to ignition | **Ratio vs KNSU** |
|---|---|---|
| KN-Sucrose | 4.8 s | **1.00** |
| KN-Dextrose | 7.9 s | **1.64** |
| 🔴 **KN-Sorbitol (KNSB)** | **19.9 s** | 🔴 **4.15** |

> 🔴 **Read the number again. Nineteen point nine seconds of continuous direct butane flame before KNSB
> does anything at all.** A bare bridgewire inside a motor core delivers a few tens of joules and is
> extinguished by the surrounding cold propellant in well under a second. **A bare bridgewire is not an
> igniter for KNSB. It is a wish.**

### 1.2 The exact same specimens, primed

**Part B of the same experiment** took five more KNSB slugs and coated the test surface with the
**Combustion Primer** of §2. Results:

| Test # | Primed KN-Sorbitol, time to ignition (s) |
|---|---|
| 1 | 2.9 |
| 2 | 4.8 |
| 3 | 5.0 |
| 4 | **12.8** ← aberrant |
| 5 | 3.3 |
| **Average (all 5)** | **5.8** |
| **Average (excluding the aberrant point)** | **4.0** |

**Stated result: igniteability was increased, on average, by nearly a factor of 5.**

> **What that 12.8 s point actually means.** Do not discard it as noise — it is the most useful datum in
> the set. **The primer is a coating, not a guarantee.** One specimen in five still behaved like bare
> KNSB. The likely causes are **coating thickness variation, a missed patch, or a contaminated surface**
> (§3). **That is exactly why §3 — cleaning the grain — is a procedure and not a suggestion.** An
> incompletely cleaned or incompletely coated grain reverts to a 20-second ignition time.

### 1.3 The mechanism — why the difference exists at all

The three propellants differ in **one** respect: what their fuel does on the way up to ignition
temperature.

| Propellant | Fuel behaviour during casting | Fuel behaviour during heating | Time to ignition |
|---|---|---|---|
| **KNSU** | **Partly caramelises during casting** | Decomposes **most readily** — already partly decomposed before you light it | **4.8 s** |
| **KNDX** | **Slight caramelisation during casting** | Decomposes **quite readily** | **7.9 s** |
| 🔴 **KNSB** | **Does not caramelise at all** | 🔴 **Does not readily decompose. Only after sustained heating does decomposition occur** | **19.9 s** |

**The observed sequence for each propellant, in the experiment's own words:**

1. Heating produces **no visible effect** for most of the duration.
2. A few seconds before combustion, a **"blister"** forms at an isolated, seemingly random point on the
   surface.
3. **Caramelisation begins at the blister**, darkening in colour until **a small spot of carbon**
   appears.
4. **Nearly immediately after the carbon spot appears, combustion initiates at that location.**
5. **Flame spread over the entire surface is then nearly instantaneous**, because the surface layer is
   already hot.

**The one thing that differs is step 2–3:**

> **KN-Sorbitol's blister is "significantly larger" than the other two propellants', and its
> decomposition is "somewhat different than caramelization (perhaps better described as
> carbonization)."**

**Why that matters, stated plainly:**

- **Caramelisation is a partial decomposition.** The molecule is already coming apart below its ignition
  temperature. **The activation energy has been partly paid in advance — partly, in KNSU's case, during
  casting itself.**
- **KNSB skips this entirely.** Sorbitol does not caramelise during casting, and does not readily
  decompose during heating. **The full activation energy must be supplied by the igniter, from cold, over
  a large surface area, in a very short time.**
- Carbonisation is a **higher-energy, later** process than caramelisation. The blister has to grow
  larger and hotter before carbon appears — **and carbon is what actually initiates combustion.**

> 🔴 **THEREFORE: the ignition problem is a HEAT-TRANSFER problem, not a chemistry problem.**
> You cannot make KNSB easier to ignite by changing the propellant (and you must not —
> `Propellant_Formulations.md` §9). **You can only make the heat arrive faster, over more of the surface,
> and more evenly.** That is what §2 (primer) and §4 (igniter) do.

### 1.4 What "successful ignition" has to mean

> **Ideally, ALL initially exposed grain surfaces start burning immediately and simultaneously upon
> activation of the igniter.**

**Why the word "simultaneously" is doing all the work:**

| If ignition is not simultaneous... | ...this is what you get |
|---|---|
| End faces ignite late | **The "mountain" pressure curve** — KNSB's signature defect. Chamber pressure and thrust go triangular instead of flat |
| Part of the core ignites late | **Extended tail-off** — visible directly in the pressure trace |
| The motor takes seconds to build pressure | **Propellant burned at atmospheric pressure**, where `C*` and `C_F` are both poor. **Impulse lost that you paid mass for** |
| Only some surfaces light at all | **A `Kn` far below design**, so the motor "refuses to come up to pressure" — the documented KNSB failure mode |

> **Both parts of KNSB's ignition problem must be solved at once: the grain must be LIT, and the motor
> must be PRESSURISED.** The pyrotechnic straw igniter of §4 does both. A bare bridgewire does neither.
> A pyrogen does both brilliantly but is out of scope for the club's first motors (§5.4).

### 1.5 The honest counter-evidence — and why it does not change anything

**Chuck Knight's analysis of sorbitol propellants argues that ignition is *not* the cause of KNSB's odd
behaviour:**

- The **"knee" on the leading edge of almost every published sorbitol thrust curve** is evidence of
  **fast, complete ignition**.
- **Nakka's KSB-002 ignition-initiator experiment, compared to KSB-001, showed little difference in
  thrust-curve shape** — "further evidence that ignition spreads quickly to all exposed surfaces."
- Knight's alternative explanation is **flushing** (see `Propulsion_Roadmap.md` §4.1): a mechanism that
  **erodes the grain surface faster than the burn rate**, expelling unburned propellant.

**This is a genuine disagreement in the source material, and the club's position is:**

1. **Knight is probably right about the steady-state shape of the curve.** Flushing explains the
   progressive character and the low Isp better than delayed ignition does.
2. **This does not make ignition unimportant — it makes it *more* important.** If flushing is the
   dominant loss mechanism, then **anything that lengthens the low-pressure start-up phase gives
   flushing more time to work.** A slow start is a slow start; the propellant being expelled does not
   care whether the pressure was late because of a weak igniter or a stubborn surface.
3. **Both sources agree on the practical action.** Knight's own model puts **flush rate = 1.37×** the
   initial burn rate at the K1000's nozzle end. **Getting to full pressure fast is the mitigation either
   way.**
4. **The club builds a proper igniter and a proper primer, and treats Knight's finding as a second,
   independent reason to do so.**

> **Do not use this disagreement as an excuse to skip the primer.** The primer is cheap, it is proven, it
> is measurable (§3.6), and the worst case if Knight is entirely right is that you spent twenty minutes
> and a gram of ignition powder.

---

## 2. THE GRAIN PRIMER — the critical missing piece

> **This section is the reason this document exists.** The workspace's earlier notes said "primer
> formulation pending." **It is not pending. It is here, it is nitrate-based (no perchlorate), and it is
> the single highest-value twenty minutes of work in the club's entire motor programme.**

### 2.1 Recipe

| Component | Specification |
|---|---|
| **Ignition Powder** | **80% potassium nitrate / 20% charcoal by weight. NO SULPHUR.** Preparation per §6 |
| **Solvent** | **70% isopropyl alcohol** (rubbing alcohol). Do not substitute 99% IPA without re-checking consistency — the water fraction is part of what makes the mix behave |
| **Consistency** | **"Thick paint"** — see §2.2. This describes the **mix**, not the applied coat |
| **Prep step** | **Pulverise the Ignition Powder granules with a mortar and pestle FIRST**, then add the IPA |

**Procedure:**

1. **Pulverise** the Ignition Powder granules with a **mortar and pestle** until they are a fine powder.
   Do not skip this — you are making a paint, and paint needs pigment, not granules.
2. **Add 70% IPA a little at a time**, stirring, until the consistency is **that of thick paint**.
3. **Cover the container.** IPA evaporates and the mix thickens as it sits; you will be re-wetting it
   repeatedly if you leave it open.
4. **Make only what you need for one session.** A few grams goes a long way. Leftover mix is a
   flammable-solvent item to be disposed of, not stored.

### 2.2 What "thick paint" means as a target

| Too thin | **Correct — "thick paint"** | Too thick |
|---|---|---|
| Runs off the brush; pools in the core; drips off the end faces | **Clings to the brush. Leaves a continuous film. Does not run.** | Will not flow off the brush; goes on lumpy and streaky |
| Result: an uneven coat with thick pools and bare patches | Result: a **single thin, even, continuous coat** | Result: a thick, lumpy coat and poor adhesion |

> ⚠️ **If in doubt, err toward slightly thin and apply TWO passes rather than one heavy pass.**
> The measured target is 200 µm (§2.3). A brush-loaded with thick mix will put down 500 µm without
> trying.

### 2.3 Application — and the measured thickness

> ### 🔴 **THIN COAT ONLY. A SINGLE COAT. A FINE PAINTBRUSH.**
>
> **Measured average coating thickness in the controlled experiment: 0.0075 in = 200 micron.**

**Method:**

1. Use a **fine paintbrush** — a small artist's brush, not a 2-inch decorating brush.
2. Apply a **single coat**. **One pass, one direction, then stop.**
3. Cover the **core** and **both end faces** (§2.4 covers the source discrepancy on surface coverage).
4. Work the brush **into the core** with a twisting motion so the whole bore is wetted. The core is the
   primary burning surface — it is the surface you most need lit.
5. **Do not re-brush a tacky area.** Re-brushing partially-dried primer lifts it and leaves a bare patch.
6. **Inspect under good light** for bare patches, especially at the core/end-face corner and at the
   outside diameter where the casting tube was peeled off.

> ### ⚠️⚠️ **WARNING — DO NOT APPLY A THICK COAT** ⚠️⚠️
>
> **A thin coat is not a suggestion. It is the requirement.**
>
> - The **only** documented thickness-linked failure mode in the source material belongs to a different
>   formulation entirely: the **perchlorate "Ferocious" epoxy/KP pyrolant**, where the coating **must be
>   no greater than 3 mm to prevent fracture of the pyrolant coating upon firing**, and **no more than
>   ~2 mm** when pressed as a disc for outside-surface installation. **A thicker coating of THAT material
>   cracks off the surface when it fires.**
> - **There is no "thick coat" variant of the IP/IPA primer in the source. None. Do not invent one.**
> - **The source material specifies a *thin*, *light*, *single* coat, uniformly, everywhere it discusses
>   this primer.**
> - **A thick coat defeats the purpose.** The primer's job is to get the surface hot *fast*. A thick layer
>   of low-conductivity powder is a **thermal insulator** between the flame and the propellant, and it
>   has to be heated through before anything underneath sees heat. **A heavy coat causes delayed
>   ignition, which is the exact opposite of what you are buying.**
>
> **If your primer is not working, the fix is a cleaner grain and a better igniter — never a thicker
> coat.** See §1.2: the aberrant 12.8 s specimen in the primed set is a warning about *coverage*, not
> about thickness.

### 2.4 Which surfaces to coat — the source disagreement, stated honestly

**The club's two source pages do not say the same thing.** This is recorded rather than papered over,
because a member who reads the source will find the discrepancy and needs to know the club's ruling.

| Source | What it says |
|---|---|
| **`ignexp.html`** (the igniteability experiment) | Coated the **test surface** with a **single coat**. In its design guidance: for a BATES grain, **"the segment ends would be coated, and the central core may be coated part way (near the segment ends)."** |
| **`casting1.html`** (the A-100M casting page) | "A brush is then used to apply a light coating over the **entire outer surface**. **It is not necessary to coat the core.**" **And** `Technical_Reference_Nakka.md` §1.13 records the motor-testing rule: **"Coat the grain segment end faces and core with a light coat of ignition primer."** |

> ### ✅ **CLUB RULING**
>
> **Coat the core, the forward end face and the aft end face. Do not coat the outer cylindrical surface
> — that surface is covered by the inhibitor.**
>
> **Reasoning:**
>
> 1. **`ignexp` is the experiment that produced the 200 µm number and the ~5× improvement.** It is the
>    more directly evidenced of the two for this purpose.
> 2. **`casting1`'s "outer surface" instruction is written for a specific motor** (the A-100M) and
>    describes a grain whose outer surface is a burning surface at that point in the procedure. **On the
>    club's grain the outer surface is bonded to the casting-tube inhibitor** and never burns.
> 3. **Coat what burns.** The club's single tubular grain burns on the **core** and **both end faces**.
>    Priming an inhibited surface is wasted material, adds mass, and risks primer being dragged into the
>    inhibitor bondline during insertion.
> 4. 🔴 **The end faces are the surfaces that cause the mountain curve.** The reference is explicit:
>    `Technical_Reference_Nakka.md` §1.13 attributes KNSB's triangular pressure curve to **"delayed
>    ignition of the end faces of BATES grain segments"**, and prescribes the primer for exactly that.
>    **Even on a single-grain motor, the end faces are the surfaces most likely to be late.**
>
> **Whichever you choose, record it.** Primer coverage is a **process parameter under change control**
> (`Propellant_Formulations.md` §9.2 — "Process"). Changing primer coverage changes `Kn(t)` and therefore
> changes the motor.

### 2.5 Drying

**Two accepted routes:**

| Route | Procedure | Use when |
|---|---|---|
| **Full air dry** | **Minimum 24 hours** in open air, out of sunlight, in a ventilated space away from ignition sources | Default. **Use this for anything that will be fired.** |
| **Air + desiccator** | **~30 minutes in open air**, then into a **desiccator** to complete drying | When you need the grain dry the same day, or when ambient humidity is high |

**Desiccator construction (from the casting procedure):** a sealed container — a Tupperware with a
well-sealing lid — containing a layer of **calcium chloride, silica gel, or other desiccant pellets**.

> ⚠️ **The desiccant pellets must NOT contact the grains.** They dissolve and stick to the grain, and
> they will take the primer off with them when you pull the grain out.

### 2.6 Durability — what to expect in handling

> **The dried coating is very durable and will not rub off by normal handling or storage. It "adhered
> very well."**

**Practical consequences:**

- **You can handle a primed grain normally** — insert it, seat it, adjust its position, remove and
  re-inspect it.
- **The primer is not a fragile coating that needs protecting with a bag.** Do not wrap a primed grain
  in plastic for transport; the plastic will lift the primer and trap solvent.
- **It is still a coating.** Do not scrape it, do not wipe it, and **do not clean the grain with acetone
  after priming** — the solvent will remove the primer you just applied.
- **Re-inspect after inserting the grain into the case.** Sliding a grain into a case can shave primer
  off the end-face edges. If you see bare propellant at an end-face edge, **touch it up and re-dry before
  firing.**

### 2.7 Why it works — the mechanism, quoted

The source's explanation, in full:

1. **On heating, the coating melts rapidly over much of the surface with highly agitated bubbling.**
   Combustion then initiates.
2. **Potassium nitrate melts at 333 °C**, and **no energy is absorbed by decomposition or melting of the
   "fuel" (charcoal)** in the coating mixture at that temperature.
3. **Only slightly further heating decomposes the potassium nitrate at 400 °C**, **with the evolution of
   oxygen and subsequent combustion of the charcoal particles in the coating matrix.**
4. **The black colour / high emissivity of the coating facilitates radiant heat transfer from the
   flame.**

**Translate that into why a 200 µm film beats 20 seconds of bare KNSB:**

| Mechanism | What it buys you |
|---|---|
| **KN melts at 333 °C, charcoal does not melt at all** | The coating has a **low, well-defined ignition threshold with no melting-energy penalty.** It needs to reach ~400 °C, not the full activation energy of sorbitol decomposition |
| **Oxygen is supplied internally** | The KN **decomposes to release oxygen**, which then burns the charcoal **in the same matrix**. No waiting for oxygen to diffuse in from the igniter flow |
| **It is essentially a solid monopropellant film** | Once any small region reaches ~400 °C, it is **self-sustaining and spreads** |
| **High emissivity (it is black)** | **Radiant heat from the igniter flame is absorbed instead of reflected.** A white KNSB surface reflects a large fraction of the incident radiation; a black primed surface absorbs it |
| **It is bonded to the propellant** | There is **no thermal contact resistance** between the burning primer and the grain. The primer's own combustion products are directly against KNSB at ignition temperature |

**The honest caveat from the experiment, stated so nobody is surprised:**

> **"Flame spread over the entire surface was somewhat LESS rapid than for the bare specimens."**

**Interpretation:** the primer makes ignition **initiate** far sooner, but the flame front then moves
across the primed surface a little more slowly than across a bare, already-hot KNSB surface. This is
consistent with the primer burning as a film and depositing ash, and it **in no way negates the result** —
total time to ignition fell from 19.9 s to 4.0 s. **But it does mean the primer is not a licence to
ignore igniter placement.** Get the igniter's hot gas to the surfaces you care about.

### 2.8 The one documented "too thick" failure mode — for completeness

**This is a perchlorate formulation and the club does not use it. It is recorded here so that nobody
misattributes it to the club's primer, and so the mechanism is understood.**

| Property | "Ferocious" epoxy/KP pyrolant |
|---|---|
| Oxidiser | **Potassium perchlorate (KP)**, very finely ground |
| Binder | **High-grade epoxy** (e.g. West System). **"Adhesive grade is not satisfactory."** |
| Form | Peeled from two 1 in × 1 in (25 × 25 mm) polyethylene squares, **~pencil-eraser-sized dab** |
| 🔴 **Thickness limit** | **No greater than 3 mm to prevent fracture of the pyrolant coating upon firing** |
| 🔴 **Disc form limit** | **~2 mm maximum** when installed at the **grain outside surface** |
| Burn duration | **~2 seconds**, hot |
| Reliability | **Over 30 motor firings, zero misfires** |

> 🔴 **The lesson generalises even though the formulation does not: a brittle energetic coating has a
> thickness above which it fractures instead of burning.** A fractured coating is a bare patch plus a
> loose fragment of pyrolant rattling around in a motor. **This is another reason the club's primer is
> thin, and another reason not to invent a thick-coat variant.**

---

## 3. Cleaning and drying the grain BEFORE priming

> ### 🔴 **IF YOU SKIP THIS SECTION, THE PRIMER WILL NOT WORK.**
>
> **A primed but grease-contaminated grain is worse than a bare grain**, because you will have spent
> twenty minutes and a gram of ignition powder convincing yourself the ignition problem was solved.

### 3.1 The contamination, and where it comes from

**After demoulding, the grain has a thin residual coating of grease on the outer surface and on the
surface of the core.**

**Where it comes from:**

| Source | Surface affected |
|---|---|
| **Coring-rod lubricant** (silicone grease / Super Lube) | **The core bore** — the primary burning surface |
| **Grease applied to the casting tube interior** | **The outer cylindrical surface** |
| **Grease applied to the nozzle convergent area** (mould assembly step) | **The aft end face** at the nozzle end |

**Why it is fatal to ignition:** the grease is a **hydrocarbon film** sitting between the primer and the
propellant. It **burns and gasifies at a low temperature**, lifting the primer off the surface **before
the primer reaches its own ignition threshold**. The result is a bare KNSB surface that now has to be
ignited **without** the primer you thought was there.

> **Source wording, which the club adopts verbatim as a rule:**
> **"This must be cleaned off completely to prevent delayed or failed ignition."**

### 3.2 The cleaning procedure

**Solvent: acetone or lacquer thinner.** Both work. **Acetone is preferred** — it is less aggressive on
the club's equipment and evaporates cleanly.

| Step | Action | Notes |
|---|---|---|
| 1 | **Do this immediately after demoulding**, before the grain cures hard | Grease lifts far more easily from a fresh surface |
| 2 | Work in a **ventilated area, no ignition sources**, with **nitrile gloves** and **eye protection** | Acetone is flammable and a respiratory irritant |
| 3 | **Wipe the core bore** with a lint-free cloth or a swab **dampened** (not soaked) with acetone, working **end to end** | Do not flood the bore — solvent running into the inhibitor bondline can attack it |
| 4 | **Wipe both end faces** with a fresh dampened cloth | Use a fresh area of cloth each pass |
| 5 | **Wipe the outer surface** where it is accessible | The inhibitor will cover most of it, but residual grease at the ends causes disbonding |
| 6 | **Repeat with a clean cloth** until the cloth comes away clean | Two passes is normal; three is not unusual |
| 7 | **Allow the solvent to flash off completely** before priming | Acetone flashes off in seconds to a minute or two at room temperature. **Do not prime a wet surface** |
| 8 | ⚠️ **Do NOT soak the grain in solvent** | This is a surface wipe, not a bath. Soaking drives solvent into the propellant and into the inhibitor bondline |

> 🔴 **Do not use a cloth that has been used for anything else.** Acetone lifts grease from the cloth as
> well as from the grain. **Dedicate clean lint-free wipes to this step and throw them away after.**

### 3.3 Drying the grain — the sticky-surface problem

**After cleaning, the grain may be somewhat sticky to the touch.** This is **not** grease. It is **residual
moisture**:

- Water present in the propellant mix is **"forced" out of the propellant by the heat of casting**.
- It then gets **trapped at the interface with the casting tube**.
- It migrates to the free surfaces over the following hours.

**Fix: a desiccator.** A sealed container with **calcium chloride, silica gel or other desiccant pellets**.
**Pellets must not contact the grain.**

| Step | Detail |
|---|---|
| Container | Sealed Tupperware or similar, well-sealing lid |
| Desiccant | A few cm of **fresh** calcium chloride (or silica gel) |
| Barrier | Perforated plate or paper towel so pellets cannot touch the grain |
| Time | Long enough for the stickiness to go — **typically overnight, occasionally a few days** |
| 🔴 Maintenance | **Replace the desiccant monthly, or whenever it shows wetness.** Spent desiccant is worse than none: it gives false confidence |

### 3.4 🔴 The over-drying hazard — read this before you leave a grain in a desiccator

> ### **A DESICCATOR IS A DRYING TOOL. IT IS NOT A STORAGE CONTAINER.**
>
> **"For long term storage, a dessicator should not be used. There is evidence that suggests that the
> grain get overly dry, the result of which may be a burn rate greater than normal. This could result in
> a CATO."**

**Why over-drying is dangerous, mechanically:**

| Step | What happens |
|---|---|
| 1 | Residual moisture in the propellant **suppresses burn rate by reducing the burn-rate coefficient `a`** |
| 2 | Remove too much of it and **`a` rises above the value your motor was designed around** |
| 3 | Chamber pressure scales as roughly `a^(1/(1−n))` — at `n ≈ 0.3` that is `a^1.43`. **A 20% rise in `a` is a ~30% rise in chamber pressure** |
| 4 | Your case was sized with a **1.5× minimum margin** and a **2.5× target**. **You have just spent a third of the minimum margin on a storage decision** |
| 5 | 🔴 **CATO** |

> **Note the direction of the danger.** As-obtained (wet) materials give a **lower** `a` than design —
> that is the safe direction to be wrong (`Propellant_Formulations.md` §5.1). **Over-drying pushes you
> the other way, into the unsafe direction.** The desiccator is the only tool in the club's kit that can
> make a grain *more* dangerous than it was designed to be.

### 3.5 Long-term storage — the correct method

> **For long-term storage (if required): place the grains into a zip-lock bag, then place into a
> freezer.**

| Step | Detail |
|---|---|
| 1 | Ensure the grain is at **ambient temperature and touch-dry** before bagging |
| 2 | **Zip-lock bag**, air expressed |
| 3 | **Freezer** |
| 4 | **Allow to return to room temperature *inside the sealed bag* before opening** | Opening a cold bag in Bengaluru humidity condenses water **directly onto the grain surface** |
| 5 | After removal: **inspect, re-run the density check and tap test if stored more than a month**, and **re-prime if the primer is disturbed** |

> ⚠️ **Does the freezer damage the primer?** The primer is a dried powder film bonded to the surface and
> described as very durable. **Store primed grains in the freezer and inspect on removal.** If the
> coating shows cracking, flaking or blistering after a freeze-thaw cycle, **re-prime.** Record the
> observation — it is a real data point the club does not have yet.

### 3.6 The sequence — get this order right

```
    DEMOULD
       |
       v
  1. CLEAN        acetone / lacquer thinner wipe, core + both end faces
       |          (remove ALL casting grease)
       v
  2. DRY          desiccator until not sticky   <-- NOT long-term storage
       |
       v
  3. TRIM         cut to length, finish end faces
       |
       v
  4. RECORD       mass, dimensions -> DENSITY CHECK (>= 90% of 1.841 g/cm3)
       |
       v
  5. TAP TEST     after FULL cure only
       |
       v
  6. PRIME        thin IP/IPA coat, core + both end faces, ~200 micron
       |
       v
  7. DRY PRIMER   24 h air  OR  30 min air + desiccator
       |
       v
  8. STORE        zip-lock bag -> freezer  (NOT the desiccator)
```

> 🔴 **Two order-of-operations rules that people get wrong:**
> 1. **Clean BEFORE you prime.** Always. There is no version where you prime first.
> 2. **Density check and tap test BEFORE you prime.** Primer adds mass and a surface coating, both of
>    which corrupt the density measurement, and the tap test needs an uncoated inhibitor surface to give
>    a clean reading.

---

## 4. The pyrotechnic "straw" igniter — full construction

**This is the club's baseline igniter.** It is the design used for the B-200, C-400 and similar
sugar-propellant motors, and it is the design this document standardises on.

### 4.1 What it is and why it works

> **A length of polyethylene plastic drinking straw, filled with Ignition Powder, sealed at both ends
> with polyethylene hot-melt glue, with a nichrome bridgewire soldered to the lead ends.**

**It performs two functions simultaneously, and both are required:**

1. **Generate a heat flux** in the form of **hot, dense gases** which rapidly ignite the propellant on all
   exposed surfaces. **Convective heat transfer, from gases flowing at high velocity over the grain
   surface toward the nozzle exit, is what does the ignition.**
2. **Pressurise the chamber** to a level at which **the burn rate of the propellant is sufficient to
   maintain that pressure** — i.e. **the design pressure of the motor.**

> **A BP charge in a sealed cartridge burns nearly instantly, releasing a sizeable volume of hot gases and
> molten combustion products. This serves to pressurise the motor while very effectively lighting the
> grain. The motor then achieves full thrust almost immediately.**
>
> **"Over several flights and static tests, this pyrotechnic igniter proved to be highly reliable and
> significantly boosted the performance of the rocket motors."**

### 4.2 Bill of materials

| Item | Specification | Notes / India sourcing |
|---|---|---|
| **Straw** | **Polyethylene** plastic drinking straw | Must be **polyethylene** — the hot-melt glue bonds to it. Paper straws do not seal with hot-melt glue. **Check by feel: PE straws are waxy and flexible** |
| **Ignition Powder** | 80% KNO₃ / 20% charcoal, no sulphur | §6. **Make in ≤ 10 g batches** |
| **Hot-melt glue** | **Polyethylene** hot-melt sticks, low-temperature gun | Standard craft/stationery hot-melt is polyethylene-based |
| **Bridgewire** | **Nichrome (nickel-chromium, high resistance) wire** | **≈ $0.20/ft** in the source. In India: **₹15–40 per metre** for 30–32 AWG nichrome from an electronics supplier |
| **Alternative bridgewire 1** | **One or two strands of coarse steel wool** | Free, available everywhere, **works**. Less consistent resistance |
| **Alternative bridgewire 2** | **A strand of fine copper "speaker" wire** | Last resort. **Low resistance = high current demand** |
| **Leads** | **2-core copper hookup wire**, ~0.5–1 mm² | Long enough to reach the motor's head end plus slack |
| **Solder** | Rosin-core electronics solder | |
| **Flux** | **Acid soldering paste** | 🔴 **Required for nichrome.** Must be cleaned off afterwards |
| **Alcohol** | **Isopropyl alcohol** or ethanol | For **removing excess acid paste** |
| **Magnifier** | A **magnifying glass** or loupe | 🔴 **Mandatory inspection step** |
| **Tools** | **Needlenose pliers**, **soldering gun** (not a low-power iron), scissors, ohmmeter | |

> ### ⚠️ **Never use a lead-acid/acid-core plumbing flux or a corrosive flux on the leads themselves.**
> **Acid soldering paste** is used **only on the loop joints**, and **must be swirled off in alcohol
> afterwards** (§4.4 step 6). Residual acid flux on copper leads corrodes them, and a corroded lead is a
> misfire.

### 4.3 Selecting and preparing the straw

| Step | Action |
|---|---|
| 1 | Cut the straw to length. **Long enough to reach from the head end to at least the middle of the grain core**, plus enough to exit the motor |
| 2 | **Test-fit it through the nozzle and into the core before you load it** | 🔴 **The igniter must not plug the throat.** Verify the straw passes freely and that the assembled igniter will pass |
| 3 | Seal the **lead end** first: a dab of hot-melt glue, allowed to cool | Hold the straw upright so gravity helps |
| 4 | **Record the straw length** on the igniter's batch record | |

> 🔴 **THE THROAT-PLUGGING RULE**
> **An igniter that plugs the throat turns the motor into a closed pressure vessel with a burning charge
> inside it.** The nozzle is the only pressure relief the motor has. **Check the fit before the igniter
> is loaded, and check it again before insertion.**

### 4.4 Bridgewire construction — the exact soldering method

> **Nichrome wire can be tricky to solder.** This method works, and it works repeatably. Follow it in
> order.

```
   STEP 1: STRIP THE LEADS              STEP 2: FORM CLOSED LOOPS
                                        
   ============------------------       ============----(@)     (@)----
        insulation   bare copper              bare     loop      loop
                                        
   STEP 3: THREAD NICHRONE THROUGH BOTH LOOPS, SPAN = ~5 mm
   
        ========---(@)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~(@)---========
                     |<---------- ~5 mm ----------->|
                          nichrome bridgewire
   
   STEP 4: ACID PASTE -> SOLDER GUN -> FILL LOOPS (capillary action)
   STEP 5: INSPECT UNDER MAGNIFICATION
   STEP 6: SWIRL IN ALCOHOL TO REMOVE EXCESS PASTE
```

| Step | Action | Detail |
|---|---|---|
| **1** | **Strip the insulation** from the electrical leads | Expose **8–10 mm** of clean copper on each lead |
| **2** | **Form closed loops** using **needlenose pliers** | A **closed** loop, not a hook. The loop is what the solder fills and what holds the nichrome mechanically |
| **3** | **Thread the nichrome wire through the loops** | One pass through each loop |
| **4** | **Adjust the spacing so the nichrome span between the loops is about 5 mm** | 🔴 **This is the dimension that matters.** 5 mm is the target. See §4.5 for why |
| **5** | **Brush the loops lightly with acid soldering paste** | **Lightly.** Paste on the wire itself is a liability; paste on the joint is the point |
| **6** | **Using a soldering gun, heat the loops and fill with solder** | 🔴 **A soldering gun, not a low-wattage iron.** Nichrome conducts heat away fast and a weak iron will not wet the joint. **Capillary action will make this easy to do.** The nichrome wire ends up **embedded in solder**. **Do not pull on the nichrome while the solder is molten** |
| **7** | **Use a magnifying glass to inspect** and make certain the loops are **fully filled with solder** | A partially-filled loop is a **high-resistance joint** that will heat instead of the bridgewire, or fail open |
| **8** | **Remove excess solder paste by swirling the igniter in alcohol** | 🔴 **Do not omit this.** Acid paste left on the joint corrodes it |
| **9** | **Ohm the bridgewire** and record the reading | A nichrome bridgewire should read **a few ohms**. **Open = remake it. Zero = the leads are shorted** |
| **10** | 🔴 **Shunt the leads immediately** — twist the bared far ends together | **Before the igniter goes anywhere.** This is the step people skip and it is the step that saves hands |

### 4.5 Why the 5 mm span — and what happens if you get it wrong

The **span between the solder loops** sets the **length of nichrome that must be heated to fire the
igniter**.

| Span | Consequence |
|---|---|
| **Too short (< 3 mm)** | **Low resistance, high current.** The bridgewire may be **mechanically fragile** and is easily broken during loading. Also **less contact area** with the Ignition Powder |
| ✅ **~5 mm** | **The documented working value.** Enough nichrome to reach ignition temperature at 7.2 V, enough length for robust handling, enough surface in contact with the powder |
| **Too long (> 8 mm)** | **Higher resistance.** At a fixed supply voltage the wire may not reach ignition temperature promptly, or at all with a weak battery. **This is the "propellant ball chars but does not ignite" failure mode** |

> **The classic igniter failure, described by the source from his early motors:**
> **"If the power supply was, for some reason low (or if it was cold, such as during a winter launch), the
> propellant ball on the igniter would char, but not ignite."**
>
> **And the second classic failure: "since the nichrome wire is brittle, breakage would sometimes
> occur."**
>
> **Both are addressed by (a) the 5 mm span, (b) the correct power supply (§5.1), and (c) the shunt
> rule.**

### 4.6 Loading the Ignition Powder

| Step | Action | Detail |
|---|---|---|
| 1 | Stand the straw upright with the lead end down | The sealed end is at the bottom |
| 2 | **Load the Ignition Powder** | Pour in small increments through a small funnel or a folded card |
| 3 | **Tamp periodically to eliminate voids** | A wooden dowel or a trimmed matchstick. **Gentle taps, not hard packing.** Hard packing can crush the powder and **can damage the bridgewire** |
| 4 | **Position the bridgewire in the powder** | The bridgewire must be **surrounded by powder**, not lying against the straw wall with air on one side |
| 5 | Fill to within ~5 mm of the open end | Leave room for the glue plug |
| 6 | **Seal the open end with hot-melt glue** | A generous dab that fully encapsulates the powder surface and grips the straw wall |
| 7 | **Record the charge mass** | Mass of the loaded igniter minus the mass of the empty straw + wire assembly. **This number goes in the test report** |
| 8 | 🔴 **Re-shunt the leads** | Twisted together, every time the igniter is set down |

> ⚠️ **The reference gives a nominal full-size charge of "approximately 1 gram" for the mini-bulb
> version of this igniter. That is NOT the club's number for a 24 mm motor. See §5.**

### 4.7 Where the igniter goes

| Placement rule | Detail |
|---|---|
| **The igniter must be positioned to ignite the CORE and the FORWARD END FACE** | It is the core and end faces that are primed (§2.4). Put the heat where the primer is |
| **The igniter must NOT plug the throat** | Verified by test-fit before loading |
| **The igniter must not block the port** downstream of itself | The whole point is hot gas **flowing over the grain surface at high velocity toward the nozzle exit**. An igniter that fills the port stops the convection that does the work |
| **Consider the pyrogen principle even with a straw igniter** | The reference notes that for a **single-grain motor with a central core, a pyrogen igniter would prove most effective for rapid startup** — precisely because it delivers a **high-velocity, particle-laden flame** down the core |
| **For a multi-segment BATES stack the problem is harder** | **Segment ends sit "pretty much in a region of stagnant flow"** and reliable ignition "may pose a problem, regardless of igniter design." **The primer is the proposed solution** — this is the whole reason §2 exists |

---

## 5. Igniter sizing — safety-critical

> ### 🔴 **THE MOST IMPORTANT SAFETY FACT IN THIS DOCUMENT**
>
> **"Use of an igniter containing a much greater charge of BP than shown may result in an initial pressure
> 'spike'. This over-pressurization of the rocket motor during startup may result in motor failure
> characterized by shearing of the safety bolts retaining the rocket motor head."**

### 5.1 The BEM charge-size comparison — the evidence

A **Ballistic Evaluation Motor** was fired with three different igniter charges, and the effect on the
**pressure–time trace and burn time** was recorded:

| Case | Charge | Observed effect |
|---|---|---|
| **(a)** | **3 g** | Reference trace |
| **(b)** | **7 g** | Clearly altered trace and burn time |
| **(c)** | **15 g** | 🔴 **Startup pressure spike. Over-pressurisation at startup** |

**Source attribution:** *Rocket Propulsion Technology, Vol. 1 — "A Technique for Measurement of Rate of
Burning and Specific Impulse of Solid Propellants."*

> **"The effect of igniter size on the motor chamber pressure curve can be significant for 'small' rocket
> motors (such as the A-100, B-200 & C-400)."**

### 5.2 Why this is worse for a small motor than the BEM numbers suggest

The BEM is a **development motor, built to survive instrumentation and abuse.** The A-100, B-200 and C-400
are **flight-representative small motors** — and the reference singles them out as the ones where the
effect is significant.

**The scaling argument, which is not in the source but follows directly from it:**

| Quantity | Behaviour as motor size falls |
|---|---|
| **Chamber free volume** | Falls as **length³** |
| **Throat area** | Falls as **length²** |
| **Igniter charge needed to reach a given pressure** | Tracking the free volume, falls as **length³** |
| **But a "small" charge is hard to make smaller** | A gram of BP is a gram of BP. **Below about a gram, handling and tamping become unreliable** |

> **The consequence: your 24 mm motor has a chamber free volume roughly an order of magnitude smaller than
> an A-100's, and a throat area more than an order of magnitude smaller.** The 3 g / 7 g / 15 g series was
> run in a motor far larger than yours. **You cannot scale those masses down by the volume ratio and
> expect the result to be manufacturable — but you can and must scale them DOWN.**

### 5.3 Sizing guidance for the club

**Estimate the pressure your charge will produce before you load it.** The reference gives the method
(from **NASA SP-8051, *Solid Rocket Motor Igniters***):

$$P \;=\; \text{function of}\;\; \left(\rho,\; D=\frac{C}{V},\; \lambda=\frac{RT}{M},\; G,\; P_a\right)$$

| Symbol | Meaning | Value / note |
|---|---|---|
| `C` | **Original mass of charge** | Your igniter charge, in lbₘ (or work in SI consistently) |
| `V` | **Free volume of the combustion chamber at time `t`** | 🔴 **For the club's 24 mm motor this is TINY — measure it, do not guess** |
| `D = C/V` | **Loading density** | The number that governs everything |
| `λ = RT/M` | **"Effective force"** | See below |
| `G` | **Fraction of original charge consumed by time `t`** | Dimensionless |
| `P_a` | **Atmospheric pressure** | ~90.5 kPa at Bengaluru's ~920 m elevation |

**The effective force (impetus):**

| Material | Impetus | `λ` |
|---|---|---|
| **Commercial-grade black powder** | **≈ 100 000 ft·lb_f/lbₘ** | **1 200 000 in·lb_f/lbₘ** |
| 🔴 **Home-made Ignition Powder** | 🔴 **Only ~70–80% of that** | 🔴 **Scale accordingly — this is a real derating** |

> 🔴 **Do not size the igniter using commercial-BP impetus.** The club's IP is home-made and its impetus
> is **70–80% of commercial**. **That means a given charge mass produces LESS pressure than the
> commercial-BP figure predicts — which is the safe direction, but only if you know it.**
>
> 🔴 **And the inverse is the trap: if you size for a target pressure using the home-made impetus, you
> will use a LARGER charge than the commercial-BP tables suggest.** Larger charge = larger spike if your
> estimate is wrong. **A spreadsheet implementation of this method is available as `IGNITER.XLS`.**

**Club procedure:**

| Step | Rule |
|---|---|
| 1 | **Measure the motor's actual chamber free volume** with the grain installed. Record it in the test report |
| 2 | **Compute the predicted peak pressure** using the method above with **λ derated to 70% of commercial** |
| 3 | **Target: the igniter charge should not, by itself, exceed a modest fraction of MEOP.** The charge exists to **reach** design pressure, not to **exceed** it |
| 4 | **START SMALL.** The reference's own instruction, for a motor far larger than ours: **start at 3 g and work down from there for a small motor** |
| 5 | 🔴 **For the club's 24 mm, ~23 g KNSB grain: start at 0.5 g of Ignition Powder and work up in 0.25 g steps.** **Three reasons:** (a) the free volume is small, (b) the throat is small, (c) the KNSB's own burn rate will take over from the igniter very quickly once any pressure exists |
| 6 | **Never increase the charge to "make it light better."** If the motor is reluctant, the problem is **igniter placement, primer coverage, or bridgewire heat** — not charge mass. **Adding charge adds a spike; it does not add ignition reliability per unit of risk** |
| 7 | **Record every charge mass and the resulting pressure trace.** After three motors you will have the club's own charge-vs-spike curve |

> ### ⚠️ **"Start small" does NOT mean "use a weak igniter"**
> **An underpowered igniter is also a documented failure mode.** From the static-test diagnostics:
> **"Slow ramp-up is often a consequence of an underpowered igniter."**
>
> **You are looking for the narrow band between:**
> - **Too little** → slow ramp → propellant burned at atmospheric pressure → lost impulse → possibly the
>   motor refusing to come up to pressure at all
> - **Too much** → **startup pressure spike** → **sheared safety bolts retaining the motor head** → burst
>   case
>
> **The primer (§2) is what lets you use a SMALL charge and still get a fast light.** That is the whole
> strategy: **buy ignition speed with surface chemistry, not with charge mass.**

---

## 6. Ignition Powder preparation

> **Formulation: 80% potassium nitrate / 20% charcoal by weight. NO SULPHUR.**

### 6.1 Why no sulphur — the safety argument

**Sulphur's function in conventional black powder is mainly to facilitate easy ignition.** This is great
for flintlock guns, but **for safety reasons it is not such a good feature for rocket motor igniters, nor
is it really necessary.**

**For reference, traditional black powder is 75% KNO₃ / 15% charcoal / 10% sulphur.** The club does not
make that.

> 🔴 **The club's Ignition Powder contains NO SULPHUR, and that is a safety decision, not a performance
> one.** Sulphur **dramatically increases ignition sensitivity** — which is exactly what you do *not*
> want in a material that is being stored, handled, tamped into straws, and carried to a launch site.
> It also lowers the ignition temperature, which means it is easier to set off by friction, impact, or a
> stray spark during manufacture.
>
> **This is consistent with the club's propellant rule** (`Propellant_Formulations.md` §2.1): **no
> sulphur anywhere.**

### 6.2 The exact procedure

| # | Step | Detail | Why |
|---|---|---|---|
| **1** | **Source the charcoal** | **"Natural wood" variety only. NOT briquettes.** | 🔴 **Charcoal briquettes contain binders, fillers, coal dust and often ignition accelerants.** They are a different material with a different burn behaviour and unknown additives. **Do not use them** |
| **2** | **Break up the charcoal** | Wrap pieces **within a sheet of cotton**, then **strike with a hammer** | The cotton contains the fragments. Fine charcoal dust is a nuisance and a mess |
| **3** | **Pulverise the charcoal** | **Electric coffee grinder** | Dedicate a grinder. **Label it permanently.** Do not then use it for food |
| **4** | **Grind the potassium nitrate separately** | **Electric coffee grinder**, to a **fine powder** | 🔴 **NEVER grind KNO₃ and charcoal together.** Grinding a blended oxidiser/fuel mix is how people ignite grinders |
| **5** | **Weigh out 80/20** | **80 parts KNO₃ / 20 parts charcoal by mass.** **Weigh, do not estimate** | Percentage by **mass**, not volume. Charcoal is far less dense than KNO₃ |
| **6** | **Blend thoroughly** | **Rotating mixer. Recommended blending time: 3 hours per 100 grams** | 🔴 **This is not a "stir it for a minute" step.** Complete mixing is what makes the powder behave predictably |
| **7** | **Wet it** | Place the blended powder in a **plastic bowl** and add **enough water to form a fluid paste** | The water **granulates** the mix and, critically, **de-dusts it** |
| **8** | **Mix the paste by hand** | Well mixed, until uniform | |
| **9** | **Spread onto parchment paper and allow to dry completely** | Thin layer, out of sunlight, away from ignition sources | |
| **10** | **Break up the clumps** | **Mortar and pestle**, into **coarse granular form** | |
| **11** | **Sift to the required particle size** | **A flour sifter** | Particle size controls how the powder tamps, how it pours, and how fast it burns |
| **12** | **Store sealed, in small quantity** | See §6.4 | |

> ⚠️ **Why the wet-and-dry step exists, mechanistically.** Grinding produces an extremely fine,
> air-borne, intimately-mixed oxidiser/fuel dust. That dust is **the most dangerous form this material
> takes.** Adding water **kills the dust**, agglomerates the particles into granules, and gives you a
> material you can **handle, pour, tamp and store** without a cloud of it hanging in the air around you.
> **Do not skip it, and do not shortcut it by "just grinding it finer."**

### 6.3 Blend time — 3 hours per 100 g, and why

**Recommended blending time: 3 hours per 100 grams.**

| Batch | Minimum blend time |
|---|---|
| **25 g** | **45 minutes** |
| **50 g** | **1.5 hours** |
| **100 g** | **3 hours** |
| **> 100 g** | 🔴 **Do not.** See §6.4 |

> **Use the same rotating mixer as for propellant blending** — and **separate containers**, or a full
> clean-down between IP and propellant. **Cross-contaminating charcoal into your KNSB blend is a
> formulation change** (`Propellant_Formulations.md` §9.2), and it is one nobody will be able to explain
> three months later.

### 6.4 Batch discipline

| Rule | Value |
|---|---|
| 🔴 **Maximum batch** | **10 g** of finished Ignition Powder at any one time, in preparation or in storage |
| **Storage** | Sealed container, **away from all ignition sources**, **stored separately from the KNO₃ bulk** |
| **Storage location** | 🔴 **The club's approved propellant/pyrotechnic store. NEVER a hostel room, lab, workshop, or vehicle** |
| **Labelling** | Every container: **material, mass, date, maker.** Unlabelled energetic material is a stop-work finding |
| **Transport** | 🔴 **Shunted-equivalent discipline applies**: sealed, separated from the igniters it will load, and never in the passenger compartment |

> **Batch sizes of propellants and pyrotechnic materials are to be kept to the minimum needed for the job
> at hand.** For the club's igniter consumption, **a 5–10 g batch loads five to twenty igniters.** That is
> a season's worth. **There is no reason to make more.**

---

## 7. Firing power supply

### 7.1 What the club uses, and why

| Generation | Supply | Why it changed |
|---|---|---|
| **Original** | **4 × 1.25 V NiCad cells** (5.0 V nominal) | — |
| ✅ **Current club standard** | **2 × 3.6 V NiMH cells, 300 mAh each, in series = 7.2 V** | **"Due to the excellent current delivery capability."** |

> **The pair consists of two 3.6 V cells (300 mAh each) wired in series which deliver a generous current
> at 7.2 V. These cell phone batteries also have excellent cold-weather performance.**

**Why 7.2 V rather than the old 5.0 V:**

| Reason | Detail |
|---|---|
| **Current delivery** | Nichrome is a **low-resistance, high-current** heating element. **Voltage alone does not fire it — current does.** A cell chemistry that sags under load will heat the bridgewire to charring temperature and no further |
| **Cold-weather performance** | 🔴 **The classic failure: "if it was cold... the propellant ball on the igniter would char, but not ignite."** Battery internal resistance rises sharply as temperature falls |
| **Cell phone batteries are designed for pulse current** | A phone transmits in bursts drawing amps. **The cell is built for that**, unlike a general-purpose AA |

### 7.2 The cold-soak test — the evidence, in full

**Test:** a **semi-dead 9 V battery** (**5.1 V under a mini-Xmas-bulb load** before freezing — "nearly
dead, not good for smoke detectors") was placed in a **freezer at −4 °F (−20 °C) for 6 hours.**

| Reading | Value |
|---|---|
| Under a mini-Xmas-bulb load **after freezing** | **2.5 V** — "It was very dim using the mini x-mas bulb" |
| Reference loads quoted | **New 9 V**: no-load 9.8 V, loaded 8.2 V. **Used 9 V**: no-load 8.8 V, loaded 5.1 V. **Cold used**: no-load 5 V, loaded 3 V |
| 🔴 **Result** | **Connecting an "Ultra-low Current Igniter" to this dead frozen battery and it EXPLODED INSTANTLY** |

> **What this test actually proves — read it carefully.**
>
> **It proves that a CELL THAT APPEARS DEAD still holds enough energy to fire a suitably-designed
> igniter.** The battery read **2.5 V** under a bulb load and **still fired the igniter instantly.**
>
> **Two consequences:**
> 1. ✅ **A 7.2 V NiMH pack is enormous overkill for a bridgewire igniter, which is exactly what you want
>    in a power supply.** Margin on the firing circuit is free reliability.
> 2. 🔴 **A "dead" battery is not a safe battery.** An ignition circuit that is not physically
>    disconnected, key-removed, and shunted is a live circuit. **Never treat a flat battery as a
>    discharged hazard.** This is the electrical case of the general principle: **the igniter leads are
>    shunted at all times.**

### 7.3 Battery specification for the club

| Requirement | Value |
|---|---|
| **Chemistry** | **NiMH** (or Li-ion with a metal case, per competition rules) |
| **Configuration** | **2 cells in series** |
| **Nominal voltage** | **7.2 V** (2 × 3.6 V) |
| **Capacity** | **300 mAh minimum** |
| **Key property** | **Current delivery capability** — this is the selection criterion, not capacity |
| **State check** | **Verify the pack voltage *under load* before every session.** Not open-circuit. **A pack that reads 7.2 V open-circuit and 4 V under load will char your bridgewire** |
| **Prohibited** | 🔴 **LiPo** — prohibited by competition rules and unnecessary here |
| **Charge discipline** | Charged the night before, **never charged at the pad**, stored at storage voltage |

---

## 8. Advanced igniter options — DOCUMENTED BUT NOT FOR BEGINNERS

> ### 🚫 **THE FOLLOWING DESIGNS ARE REFERENCE MATERIAL, NOT CLUB PROCEDURE.**
>
> **Do not build these until the club has: (a) three consistent motors at the current scale, (b) a
> strand burner and a documented burn-rate law, and (c) a written hazard review signed off for the
> specific design.** They are documented here because a member will encounter them and needs to know what
> they are, why they exist, and what the risks are.

### 8.1 Mini-bulb / "exploding bridgewire" (EBW) igniter

| Item | Detail |
|---|---|
| **Principle** | A **Xmas-tree mini-bulb** replaces the nichrome bridgewire. **The tiny tungsten filament is instantly vaporised when current (e.g. from a 9 V battery) is applied** |
| **Credit** | Concept pioneered by rocketry experimenter **Rob Furtak** |
| **Build** | Pull off and discard the plastic base. Scrape the two copper leads clean of oxide. **Break the glass open by slowly squeezing the upper half in a bench vise** with the bulb **wrapped in a tissue** to catch shards. 🔴 **Safety glasses mandatory** |
| 🔴 **The shunt trap** | Most Xmas bulbs have a **very fine wire or foil wrapped around the base of the two leads.** Its purpose is to maintain continuity in a string of bulbs. 🔴 **This shunt must be removed with a toothpick or tweezers — otherwise an ohmmeter test FALSELY INDICATES that the filament is intact** |
| **Continuity check** | "Infinite" resistance = open circuit (filament or solder joint broken). **Zero = shorted leads.** 🔴 **The actual measured value may be anywhere from a couple of ohms to more than a hundred ohms, and as such does NOT provide any useful information other than to indicate an "OK" condition** |
| **Soldering** | Use **acid flux**. Then insert into a **2 in (5 cm) length of polyethylene soda straw**, seal the lead end with hot-melt glue, load **≈1 g of Ignition Powder, tamping periodically to eliminate voids**, then **tamp in a small ball of glass wool** and seal with hot-melt glue |
| **Robustness** | **20 bulbs mounted radially on an 8 in (20 cm) disc spun on a lathe at >120 g — all functioned normally afterwards** |

> 🔴 **THE LESSON THAT APPLIES EVEN IF YOU NEVER BUILD ONE:**
> **A resistance reading on an EBW confirms "OK", not a value.** The range is so wide — a couple of ohms
> to over 100 ohms — that the number tells you nothing about whether the igniter will fire or how much
> current it needs. **Do not build an ignition circuit around a measured resistance on this type of
> igniter.** Test-fire on the bench, or don't use it.

### 8.2 Ultra-low current igniter (Ken Tucker, for EARco)

**Purpose: increase the safety of rocketry by making a highly reliable, redundant igniter that fires on
almost nothing.** Developed by **Ken Tucker for EARco (Experimental Aerospace Research)**.

| Item | Detail |
|---|---|
| **Base part** | **RadioShack Part # 272-1139 Mini Lamp** (or equivalent), supplied **with pre-attached wire leads** |
| **Rating** | **1.5 V, 25 mA** |
| ✅ **In practice fires at** | 🔴 **1.2 V, 20 mA = 25 mW** |
| **Why it matters** | **"Exceptionally reliable and especially useful in cold weather operation, which greatly reduces a typical battery's available power"** |
| **Step 1** | **Record the bulb resistance** with an ohmmeter. **20–30 Ω is usual** |
| **Step 2** | **Grind a hole through the glass** on a **fine file or polishing stone**. **A magnifying glass helps check progress. ~5 minutes with practice.** 🔴 **Grind with the filament PERPENDICULAR to the hole** so glass shards do not strike the filament |
| **Step 3** | When the hole breaks through, **the vacuum draws in air and some glass shards.** **Re-check the ohms — it should be unchanged** |
| **Step 4** | **Place black powder loosely into the hole.** 🔴 **Do NOT pack — packing can damage the bridgewire.** **The bridgewire explodes when heated and lands on the powder, so the powder does not need to be in direct contact** |
| **Step 5** | **Ohm again** to confirm no damage. **A little Scotch tape over the hole keeps the powder in** |
| **Step 6 (amplifier)** | Output is **match-like**. To amplify: **place the igniter in a tube ~1 in long of similar diameter, fill with black powder, seal the ends** |
| ✅ **Redundancy** | **3 igniters in parallel require only 1.2 V and 60 mA (3 × 20 mA)** |
| **Shock resistance** | **Survives being thrown against concrete (a few hundred g's of deceleration)** — hard data lacking |

### 8.3 "Ferocious" and "Spitfire" pyrolants — 🔴 PERCHLORATE-BASED

> ### 🔴🔴 **CLUB POSITION: DO NOT USE THESE.**
>
> **Both use potassium perchlorate (KP).** The club's safety framework is unambiguous:
>
> - **Rule 13 (igniter pyrolants):** high-energy oxidisers (chlorates, perchlorates) **should be limited
>   to small quantities, and only proven formulations used.**
> - **Rule 14 (propellants):** perchlorates **"should only be used by those with years of experience
>   working safely with lower-energy oxidisers such as the nitrates."** They **"have the potential to be
>   frighteningly hazardous when combined with incompatible binders or additives, and even small motors
>   can explode with shocking violence."**
>
> 🔴 **The club does not use perchlorates, at any scale, for any purpose.**
> See `Propellant_Formulations.md` §8.4 for the full recorded justification.
>
> **The reason this matters here:** the reference material presents these as excellent, proven,
> high-reliability igniters — and they are. **They are also unnecessary, because the club's IP/charcoal
> igniter with a proper grain primer solves the KNSB ignition problem without them.** The club is not
> trading safety for capability; it is declining a capability it does not need.

**Recorded for reference only — DO NOT BUILD:**

| Formulation | Composition | Notes |
|---|---|---|
| **"Ferocious"** | **KP** (very finely ground, mortar & pestle) + **sulphur** (finely ground) + **high-grade epoxy** (West System; **"adhesive grade is not satisfactory"**). **0.5 g of epoxy is sufficient for 4–5 igniters.** Add sulphur until distinctly yellow/light amber; blend ≥2 min with a wooden craft stick; add KP gradually **"until the resulting mixture resembles a stiff paste."** | Burns hot **~2 seconds**. 🔴 **≤3 mm thick, ≤2 mm as a disc.** Cure overnight, or **65 °C for ~½ hour**. **Over 30 motor firings, zero misfires.** For small throats use **30 AWG "wrapping wire" (RS p/n 278-501)** |
| **"Spitfire" / Thermex** | **65% KP** (200 mesh) / **20% charcoal** (ball milled) / **10% Al** (400 mesh) / **5% red iron oxide.** Blended in a rotating tumbler 1–2 h. Pyrolant = Thermex + **neoprene contact cement at ≈2:1 by mass**, "as stiff as toothpaste" | Working time only minutes. **Theoretical flame temperature 3180 °C** (Spitfire II) |
| **"Spitfire II" / Thermex II** | **66% KP** / **16% charcoal** / **12% Al** / **6% red iron oxide.** Blended with **20% by mass** neoprene contact cement, fully dried, granulated for a standard straw igniter, or dissolved in **MEK or acetone** for dipping | Developed for hard-to-light composite propellants |

---

## 9. Remote ignition hardware

> **You are not near the motor when it fires.** Not behind a shield three metres away, not "just to the
> side." **There is no version of this where a person stands near the motor with a battery and a switch.**
>
> This section is the ignition-system view of the rules in `40_SAFETY/Static_Test_Procedure.md` §4.
> **Where the two documents differ, the Safety Manual governs.**

### 9.1 Cable

| Requirement | Standard | Why |
|---|---|---|
| **Length** | **100 m minimum** — the club's standard reel. **Longer for new designs and larger motors** | Matches the **75–100 m** personnel distance for proven motors, and the **150 m** minimum for new designs |
| **Specification** | **2-core copper, 1.5 mm² minimum** | 🔴 **Thin cable over 100 m loses voltage and gives unreliable ignition.** This is the electrical version of the "char but not ignite" failure |
| **Continuity** | **Tested end-to-end before every session** | A hidden break means **a misfire you then have to walk up to** |
| **Routing** | **Away from the plume path, away from foot traffic, NOT across the escape route, secured against being pulled** | |
| **Spare** | **Carry a spare** | A damaged cable found after everyone is in position costs the whole test |

### 9.2 Relay or MOSFET switching — why the high current is switched at the pad

**The firing cable carries the CONTROL signal, not the igniter current.** The high-current igniter circuit
is **local to the pad**, switched by a **relay** or a **MOSFET**.

| Reason | Detail |
|---|---|
| **Voltage drop** | **A low-current control line over 100 m loses far less voltage than a high-current line.** The igniter gets the current it needs |
| 🔴 **Galvanic isolation** | **A relay gives POSITIVE galvanic isolation when open** — the igniter is **genuinely disconnected** from the firing line, **not merely switched off by a semiconductor that may leak.** This is the single strongest argument for a relay over a MOSFET in this application |
| **Immunity to induced current** | **A relay that is open cannot be closed by an induced current in the control line** at field levels |
| **Audible confirmation** | **A relay audibly clicks.** That click is a physical confirmation of state that you can hear **from the firing point** |
| **Specification** | 🔴 **Specify the relay or MOSFET to carry at least 2× the igniter current.** Mount it at the pad end, protected from plume, dust and moisture |

> **Club preference: RELAY.** The galvanic isolation and the audible click are worth the coil current.
> A MOSFET with a documented, verified low leakage is acceptable, but **the isolation argument is real**
> and the click is the only state indication you can perceive from 100 m away through ear defenders.

### 9.3 The ignition box

> **"Use an ignition box that has built-in safety checks ensuring that no current can inadvertently be
> supplied to the igniter."**

| Feature | Purpose |
|---|---|
| **Removable key switch** | Physically breaks the arming circuit. 🔴 **The key is held on the Test Director's person — never left in the box, never on a lanyard by the box, never "on the table"** |
| **SAFE / ARM selector** | Two-position, detented, clearly labelled, with a **visible and preferably audible ARMED indication** |
| **Momentary-contact FIRE button** | Spring-return, so **the circuit cannot be left energised** |
| **Continuity check, current-limited below 50 mA** | Verifies the igniter circuit **without delivering enough current to fire the bridgewire**. 🔴 **A continuity check that can fire the igniter is not a safety feature — it is a hazard** |
| **Visible ARMED indicator** (LED and/or buzzer) | So anyone looking at the box knows its state |
| **Series redundancy** | Key **AND** arm switch **AND** fire button in series. **Any one open = no current** |
| **Battery state indication** | 🔴 **A flat battery means a misfire and an approach.** Display voltage **under load** |
| **Enclosure** | Rigid, closed, **no exposed terminals when in the SAFE state** |

### 9.4 🔴 A Safe/Arm switch is only PARTIAL security

> ### **Nakka's words, and the club's position: "A Safe/Arm switch represents only partial security."**
>
> It is **one layer**. **Treat it as though it might fail, because it might** — through a wiring fault, a
> stuck contact, an induced current, a misread switch position, or simple human error.

**The complete defence is layered, and the layers are in order of how much they actually protect you:**

| # | Layer | Why it is where it is in the list |
|---|---|---|
| 1 | 🔴 **SHUNTED igniter leads** — twisted together, removed only at the moment of connection | **This is the layer that actually protects you, and it is the one people skip** |
| 2 | **Physical disconnection of the power source** when the system is not in use | Removes the energy source entirely |
| 3 | **Key removed and on the Test Director's person** | Physical, verifiable, not defeatable by a wiring fault |
| 4 | **Safe/Arm switch in series with the key and the fire button** | One layer among several |
| 5 | **Redundant series elements** so no single failure arms the system | |
| 6 | **Continuity check current-limited below 50 mA** | |
| 7 | **Distance and hard cover** — so that even a total failure of every electrical safeguard, you are not next to the motor | 🔴 **The foundation. Distance is never traded for convenience** |
| 8 | **The igniter connected LAST**, after everyone is at distance | |

> ### 🔴 **SHUNTING — THE RULE THAT ACTUALLY SAVES HANDS**
>
> **"Igniters should have their leads shunted at all times, and should only be un-shunted just prior to
> connecting to the ignition box."** *(Also applies to parachute ejection charges.)*
>
> **Shunting = twisting the bared ends of the igniter leads together** so that any stray current — induced
> from nearby wiring, static discharge, or a fault in the firing box — **flows through the short circuit
> instead of through the bridgewire**.
>
> | Rule | |
> |---|---|
> | 1 | **Every igniter is shunted the moment it is built.** Not later. Not after testing. Immediately |
> | 2 | **The shunt stays on during storage, transport, mounting, and setup** |
> | 3 | **The shunt is removed only at the moment of connection to the firing cable** — and that connection is the **last** step before everyone withdraws |
> | 4 | **If you stop for any reason** — a break, a question, a phone call, a weather check — **the leads are re-shunted and the firing cable is disconnected** |
> | 5 | **If a shunt is found off and nobody knows why, the test STOPS.** Re-shunt, re-verify, restart the arming sequence |
> | 6 | **This applies equally to parachute ejection charges and any other pyrotechnic device** |
>
> **A shunt costs two seconds.** And per §7.2, **a "dead" battery is still a live hazard** — the cold-soak
> test proved a cell reading 2.5 V under load fired an igniter instantly.

### 9.5 Misfire — the ignition-system view

> **"If an igniter fails to initiate a rocket motor, wait several minutes before cautiously approaching,
> then ALWAYS disconnect the igniter electrical leads first."**

**The order is not negotiable:**

```
   MISFIRE
      |
      v
  1. Hold FIRE for the full expected burn + 5 s.  Then release.
  2. Call "MISFIRE" loudly.
  3. Switch to SAFE.  Remove the key.  Disconnect the battery.
  4. Announce "SYSTEM SAFE. HOLDING."  NOBODY MOVES.
      |
      v
  5. WAIT.  (5 min unburned / 15 min partial / 30 min unknown -- see Safety Manual §6.2)
      |
      v
  6. Two persons approach, from the SIDE, never in front of the nozzle.
      |
      v
  7. 🔴 DISCONNECT THE IGNITER LEADS FIRST -- BEFORE ANYTHING ELSE.
      |
      v
  8. THEN disconnect the igniter from the motor.
  9. IMMEDIATELY RE-SHUNT the free leads.
 10. Only now inspect anything else.
```

**And the diagnosis, before any re-fire:**

| Symptom | Likely cause | Fix |
|---|---|---|
| **Bridgewire intact, powder unburned** | No current reached it, or current too low | Check cable continuity, battery under load, relay function, shunt actually removed |
| **Powder charred but not ignited** | 🔴 **Underpowered supply** — the classic cold/low-battery failure | Verify the pack **under load**. Increase bridgewire current (shorter span) |
| **Bridgewire burned through, powder partly burned, motor did not light** | **Igniter not in contact with / not adjacent to primed surface**, or **charge too small**, or **primer missing/contaminated** | Re-check placement, primer coverage (§3.6), charge mass |
| **Motor lit then chuffed and died** | 🔴 **Motor would not come up to pressure** — KNSB's low-pressure exponent near 0.3 | **Bigger primer, better placement — not necessarily a bigger charge** |

> 🔴 **"Two consecutive misfires on the same motor = the motor is retired pending investigation."**
> **"If the cause of the misfire is not understood, there is no re-fire."**
> **The igniter is replaced, never reused, and never "topped up" with more powder.**

---

## 10. The historical failure — the burst diaphragm

> ### ❌ **DO NOT COPY THIS. IT CAUSED A MOTOR FAILURE.**

**The problem it was trying to solve was real.** Nakka's early motors burned for **several seconds
"building up pressure"** before suddenly thrusting at full force, with **propellant visibly wasted**. The
cause is the pressure dependence of burn rate: **at atmospheric pressure the propellant burns slowly, and
only accelerates once sufficient pressure exists in the chamber.**

**His first attempt:**

> **A "burst diaphragm" — a thin sheet of brass that blocks the nozzle throat**, allowing pressure to
> build up in the motor to achieve efficient burning. **At that point the diaphragm should burst and be
> ejected out of the nozzle.**

**The result:**

> 🔴 **"I experimented with such a concept, but this did not work satisfactorily. In fact, such an
> arrangement caused a motor failure on one of my flights (Flight C-18, July 1980)."**
>
> 🔴 **"The problem was in sizing the diaphragm to burst (reliably) at exactly the right pressure, which
> was not simple to achieve, at least not so with my narrow-throated motors."**

**He abandoned it and went to the alternative approach that became §4 of this document:**

> **Devise an igniter that would more reliably and effectively ignite the propellant, and would serve an
> additional function — to simultaneously pressurise the motor.** A black powder charge in a sealed
> cartridge achieves this.

| ❌ Burst diaphragm (abandoned) | ✅ Pyrotechnic straw igniter (adopted) |
|---|---|
| Blocks the throat **mechanically** | **Generates pressure chemically** |
| **Requires precision sizing to a burst pressure** — failed on narrow-throated motors | **Sizing is a mass of powder**, adjustable in 0.25 g steps |
| **One failure mode: does not burst** → closed pressure vessel | **Cannot "fail closed"** — the straw is consumed |
| **Another: bursts early** → back to the original problem | |
| 🔴 **Caused a motor failure (Flight C-18, July 1980)** | ✅ **Proven highly reliable over many flights and static tests** |

> ### 🔴 **CONSEQUENCE FOR THE CLUB**
> **The throat is the motor's only pressure relief. Never obstruct it, deliberately or accidentally.**
> - **Do not install a burst diaphragm, a burst disc, a plug, or any other throat obstruction.**
> - **This is why §4.3 requires you to test-fit the igniter through the throat before loading it.**
> - **This is why §4.6 requires the igniter to be sealed and secure — a loose wad of glass wool or tissue
>   working its way into the throat is the same failure, delivered by accident.**
>
> **Put into the Design Constraints checklist** (`Technical_Reference_Nakka.md` Part 4):
> **❌ No burst diaphragm — documented cause of motor failure.**

---

## 11. Pre-ignition checklist

**Print this. Fill it in. Sign it. Attach it to the test report.**

```
=============================================================================
 UVCE ROCKETRY CLUB -- IGNITION PRE-FIRE CHECKLIST
 Motor ID: ____________  Test #: ______  Date: __________  Batch: ________
 Test Director: ________________  Safety Officer: ________________
=============================================================================

 SECTION A -- GRAIN PREPARATION (completed before the day of the test)
 [ ] A1  Grain cleaned with acetone / lacquer thinner -- core + BOTH end faces
 [ ] A2  Cleaning repeated until the cloth came away clean
 [ ] A3  Grain dried in desiccator until no longer sticky
 [ ] A4  Desiccant inspected; replaced if wet or clumped; charge date: ________
 [ ] A5  *** GRAIN REMOVED FROM DESICCATOR -- NOT STORED THERE ***
 [ ] A6  Grain trimmed; mass = ______ g; dimensions recorded
 [ ] A7  Density check: measured ______ g/cm3  =  ______ % of 1.841   PASS >= 90%
 [ ] A8  Tap test performed AFTER FULL CURE:  PASS / FAIL
 [ ] A9  Batch-relative tap comparison done (odd segment rejected)
 [ ] A10 Primer mixed: IP pulverised with mortar & pestle FIRST, then 70% IPA
 [ ] A11 Primer consistency = THICK PAINT (not runny, not lumpy)
 [ ] A12 *** THIN SINGLE COAT APPLIED -- TARGET 200 micron ***
 [ ] A13 Coated surfaces: CORE [ ]  FWD END FACE [ ]  AFT END FACE [ ]
 [ ] A14 Inspected under good light for bare patches / missed corners
 [ ] A15 Dried: 24 h open air  OR  30 min air + desiccator.  Method: ____________
 [ ] A16 Grain stored in zip-lock bag -> freezer (NOT desiccator)
 [ ] A17 On removal from freezer: bag opened only at room temperature
 [ ] A18 Primer condition after storage: INTACT / RE-PRIMED / REJECTED

 SECTION B -- IGNITER (completed at the bench, SHUNTED throughout)
 [ ] B1  Ignition Powder: 80% KNO3 / 20% charcoal, NO SULPHUR
 [ ] B2  Natural-wood charcoal (NOT briquettes); KN ground SEPARATELY
 [ ] B3  Blend time >= 3 h per 100 g        Actual: ______ h for ______ g
 [ ] B4  Water paste -> parchment dry -> mortar & pestle -> sifted
 [ ] B5  Batch mass <= 10 g.  Actual: ______ g
 [ ] B6  Straw test-fitted through the throat and into the core
 [ ] B7  Straw is POLYETHYLENE; lead end sealed with hot-melt glue
 [ ] B8  Bridgewire: nichrome ( / steel wool / copper speaker wire )
 [ ] B9  *** BRIDGEWIRE SPAN BETWEEN SOLDER LOOPS = ~5 mm ***  Actual: _____ mm
 [ ] B10 Loops brushed with ACID soldering paste; filled with solder using a GUN
 [ ] B11 Loops inspected under MAGNIFICATION and fully filled
 [ ] B12 Excess acid paste removed by swirling in alcohol
 [ ] B13 Bridgewire resistance measured: ______ ohms   OPEN / SHORT / OK
 [ ] B14 *** LEADS SHUNTED IMMEDIATELY AFTER BUILD ***
 [ ] B15 Powder loaded and tamped in increments; bridgewire surrounded by powder
 [ ] B16 Open end sealed with hot-melt glue; glass wool ball if used
 [ ] B17 *** IGNITER CHARGE MASS RECORDED:  ______ g ***
 [ ] B18 Charge sized by calculation (IGNITER.XLS method), home-made impetus
         derated to 70% of commercial BP
 [ ] B19 Charge is at the SMALL end of the club range (start 0.5 g, step 0.25 g)
 [ ] B20 Igniter cannot plug the throat -- VERIFIED BY TEST FIT

 SECTION C -- FIRING CIRCUIT (at the firing point)
 [ ] C1  Firing cable: 100 m min, 2-core copper >= 1.5 mm2
 [ ] C2  Cable continuity tested end-to-end this session
 [ ] C3  Cable routed away from the plume and NOT across the escape route
 [ ] C4  Relay / MOSFET rated >= 2x igniter current; mounted at the pad, protected
 [ ] C5  Relay gives POSITIVE galvanic isolation when open
 [ ] C6  Battery pack: 2 x 3.6 V NiMH in series = 7.2 V, 300 mAh
 [ ] C7  *** BATTERY VOLTAGE MEASURED UNDER LOAD:  ______ V ***
 [ ] C8  Ignition box: key switch present, key REMOVED and on the Test Director
 [ ] C9  Ignition box: SAFE/ARM detented, labelled, with visible ARMED indication
 [ ] C10 Ignition box: momentary spring-return FIRE button
 [ ] C11 Ignition box: continuity check CURRENT-LIMITED BELOW 50 mA
 [ ] C12 *** NO CURRENT AT THE IGNITER TERMINALS WITH THE BOX IN "SAFE" ***
 [ ] C13 Key + arm switch + fire button in SERIES; any one open = no current
 [ ] C14 *** A SAFE/ARM SWITCH IS ONLY PARTIAL SECURITY -- ALL 8 LAYERS IN PLACE ***

 SECTION D -- FINAL SEQUENCE (announced aloud, in order)
 [ ] D1  RANGE IS CLEAR announced by Range Safety (nobody else may say it)
 [ ] D2  All personnel counted; nobody downrange; nobody in the exclusion zone
 [ ] D3  Everyone behind hard cover; eye protection and ear defenders on
 [ ] D4  Data logging running; cameras running; SYNC MARK captured
 [ ] D5  "INSERTING KEY -- SYSTEM STILL SAFE"
 [ ] D6  "REMOVING SHUNT -- STAND BY"
 [ ] D7  Shunt removed and igniter connected to the firing cable -- LAST physical act
 [ ] D8  Switch to ARM; ARMED indicator confirmed BY A SECOND PERSON
 [ ] D9  "SYSTEM IS ARMED. RANGE IS CLEAR. COMMENCING COUNTDOWN."
 [ ] D10 T-0: press and HOLD the FIRE button for the full burn + 5 s

 SECTION E -- IMMEDIATELY AFTER
 [ ] E1  Observe, do not move. Note plume, sound, stand, smoke AS IT HAPPENS
 [ ] E2  No ignition within 5 s? -> call MISFIRE -> Safety Manual section 6
 [ ] E3  Switch to SAFE, remove key, disconnect battery
 [ ] E4  "SYSTEM SAFE. HOLDING FOR TEN MINUTES."
 [ ] E5  WAIT TEN MINUTES. No approach. No exceptions
 [ ] E6  Approach from the SIDE. DISCONNECT THE IGNITER LEADS FIRST
 [ ] E7  THEN disconnect the igniter from the motor. IMMEDIATELY RE-SHUNT
 [ ] E8  Record igniter condition, position, residue in the throat
 [ ] E9  Measure post-fire throat diameter -- record erosion

=============================================================================
 IGNITER CHARGE MASS:  ______ g     BRIDGEWIRE SPAN:  ______ mm
 PRIMER:  thin single coat, 200 micron target, core + both end faces
 -----------------------------------------------------------------------
 NEVER: a thick primer coat | a burst diaphragm | a perchlorate pyrolant
 NEVER: an un-shunted igniter | a charge mass increase to "make it light"
=============================================================================
```

---

## 12. Cross-references

| For | See |
|---|---|
| Propellant formulation, perchlorate prohibition, change control | `Propellant_Formulations.md` §8.4, §9 |
| Grain QC: density check, tap test | `Propellant_Formulations.md` §5, §7; `Technical_Reference_Nakka.md` §1.8 |
| Why end-face ignition causes the "mountain" curve | `Technical_Reference_Nakka.md` §1.13 |
| Burn rate, mesa behaviour, `a` and `n` | `Technical_Reference_Nakka.md` §1.11; `Motor_Design_Guide.md` §2.2 |
| Strand burner and how to measure ignition quality | `Motor_Test_Program.md` §4, §5 |
| Full firing procedure, distances, misfire, NO-GO list | `40_SAFETY/Static_Test_Procedure.md` |
| Scale-up sequence and gate criteria | `Propulsion_Roadmap.md` |
| The flushing phenomenon | `Propulsion_Roadmap.md` §4.1 |

---

*UVCE Rocketry Club — `10_PROPULSION/Ignition_System_Design.md`. All quantitative data traced to Richard
Nakka's Experimental Rocketry Site (`igniter.html`, `ignexp.html`, `casting1.html`, `safety.html`,
`static.html`, `pressure-measurement.html`) as extracted in `80_REFERENCE/nakka-technical-reference.md`
§1–§3, §6, §7. Source disagreements are flagged in §2.4 and §1.5 rather than resolved silently. This
document is subordinate to `40_SAFETY/Safety_Manual_Master.md`.*
