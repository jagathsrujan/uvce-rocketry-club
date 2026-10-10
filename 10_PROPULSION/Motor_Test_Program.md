# UVCE Rocketry Club — Motor Test Program

**Document:** `10_PROPULSION/Motor_Test_Program.md`
**Applies to:** every strand burner run, every inert cast, every static firing, every grain QC check
**Status:** 🟢 Procedure complete. **The club's `a` and `n` are still unknown — §4 is the highest-priority build in the programme.**
**Parent references:** `Technical_Reference_Nakka.md` §1.8, §1.11, §1.13, Part 3; `80_REFERENCE/nakka-technical-reference.md` §6–§9, §11; `Propellant_Formulations.md` §3.4, §9; `40_SAFETY/Static_Test_Procedure.md`

> 🔴 **THE ONE SENTENCE THAT JUSTIFIES THIS DOCUMENT**
> **One motor proves nothing.** A single successful firing is consistent with a good motor, a lucky
> motor, and a motor that was one grain defect away from a CATO. **Only repeatability distinguishes
> them — and repeatability is measured, not felt.**

---

## 1. Test philosophy

### 1.1 One motor proves nothing

**The acceptance test for a motor design is not a successful firing. It is an overlapping set of
successful firings.**

| What you have | What it proves |
|---|---|
| **One firing** | That one motor, on one day, with one grain, did not fail. **It says nothing about the next one** |
| **Two firings** | That the design can work twice. **Still consistent with one good grain and one bad one** |
| **3–5 firings with overlapping thrust curves** | ✅ **That the design is repeatable.** This is the club's acceptance criterion |

**Why the emphasis on *overlapping curves* and not just "three successes":**

- **A design with a 20% unit-to-unit thrust scatter is not a design.** It is three separate motors that
  happened to work. Your flight simulation assumes a thrust curve; if the real curve wanders ±20%, your
  apogee prediction is fiction and your recovery deployment timing is a guess.
- **Overlapping curves demonstrate that you control the process**, not just the drawing. Motor design is
  the easy half. **Process control — grind, dessication, mix, cast, cure, throat diameter — is the hard
  half**, and it is what the overlapping-curve test actually measures.
- **The scatter is itself a result.** From `Motor_Design_Guide.md` §6.5: a **5% pressure scatter across
  three motors is a *result*, not a failure.** Quantify it, report it, and then decide whether to reduce
  it.

> ### 📏 **THE ACCEPTANCE CRITERION**
> **Three to five motors of identical design, identical propellant batch, identical throat diameter
> (measured), and identical igniter charge, producing thrust curves that overlap within your stated
> tolerance band.**
>
> **State the tolerance band before you fire.** Deciding what counts as "overlapping" after you have seen
> the data is not a test — it is a rationalisation.

### 1.2 Change one variable at a time

> **Between tests, change exactly ONE variable. Document it. Predict its effect before you fire.**

| If you change | You have invalidated |
|---|---|
| Two things at once | **Both results.** You cannot attribute the change to either |
| The throat diameter | Any comparison of chamber pressure with the previous motor |
| The propellant batch | Any comparison of burn rate, Isp, `c*` |
| The igniter charge | Any comparison of the pressure **rise time** and the start-up transient |
| The primer coverage | Any comparison of start-up behaviour |
| The nozzle material | Any comparison of throat erosion and `C_F` |

**The one-variable rule applies inside a batch too.** Three motors built from one propellant batch, cast
on the same day, with the same coring rod, and throats reamed in one setup, **isolate motor-to-motor
variation from batch-to-batch variation.** That is the comparison that tells you which of the two is your
problem.

### 1.3 Predict before you fire

**Every test is preceded by a written prediction.** For a static fire, that means a predicted
thrust–time and pressure–time curve, generated from your current burn-rate law.

**Why this is not bureaucracy:**

- **A prediction that is wrong is the most valuable data you will get all year.** It tells you *which*
  input is wrong.
- **Without a prediction you cannot distinguish "worked" from "differed from design but did not
  explode."** Those are very different outcomes and they look identical from behind a berm.
- **It forces you to write down your assumptions**, which is the only way they ever get checked.

| Observation | What it implicates |
|---|---|
| Pressure lower than predicted, burn longer | 🔴 **`a` too high in your law** — your materials are wetter/coarser than the reference. **This is the expected first result** |
| Pressure higher than predicted | 🔴 **`a` too low in your law, or over-dried grain, or throat smaller than measured.** **Dangerous direction — stop and investigate** |
| Pressure correct, thrust low | **Nozzle problem** — `C_F`. Check expansion ratio, divergence angle, throat erosion |
| Pressure correct, thrust correct, Isp low | **`c*` problem** — propellant preparation. Mixing, particle size, moisture |
| Rise time far longer than predicted | **Igniter underpowered, or primer inadequate** |
| Mountain-shaped curve | **Delayed end-face ignition** — primer and inter-segment spacing |

### 1.4 Test order — cheap and non-destructive first

> **The order is set by cost and by destructiveness. Do the cheap, repeatable, non-destructive
> measurements first. Only fire a motor when there is nothing left to learn on the bench.**

| Order | Activity | Cost | Destructive? | What it de-risks |
|---|---|---|---|---|
| **1** | **Inert grain casting practice** (§3) | ₹ | No | **Casting technique. Castability. Demoulding. The single largest source of rejected grains** |
| **2** | **Strand burner** (§4) | ₹₹ | Consumes ~10 g per run | 🔴 **`a` and `n`. Without these you cannot size a throat** |
| **3** | **Hydrostatic proof test** (§6) | ₹ | No (usually) | **Case burst margin. Threads. Seals. Closures** |
| **4** | **Pressure-only static fire** (§5.4) | ₹₹₹ | Yes (motor) | **Chamber pressure, `c*`, burn time, ignition quality — WITHOUT risking a load cell** |
| **5** | **Instrumented static fire** (thrust + pressure) | ₹₹₹₹ | Yes | **`C_F`, delivered Isp, total impulse, nozzle performance** |
| **6** | **Multi-unit repeatability series** (§8) | ₹₹₹₹₹ | Yes ×3–5 | **Repeatability. This is the gate** |
| **7** | **Flight** | ₹₹₹₹₹ | Yes | **Everything else** |

> **Note where the strand burner sits: position 2, before any motor is fired.** It is the **highest-value
> first build in the entire propulsion programme**, and the club's `a` and `n` are currently **UNKNOWN**
> (`config/engineering_constants.md` §3, marked 🔴 BLOCKING). **No throat may be finalised until this is
> done.**

### 1.5 What "success" and "failure" mean

| Outcome | Verdict |
|---|---|
| Overlapping curves, prediction matched within tolerance | ✅ **Success.** Scale up |
| Overlapping curves, prediction missed but consistently | ✅ **Success.** **You just measured your materials.** Update `a` and re-predict |
| Non-overlapping curves, one outlier | 🟡 **Mixed.** Investigate the outlier before firing more. One outlier is a process finding |
| Non-overlapping curves, all different | ❌ **Process control failure.** Stop. Go back to §3 and §9. **Do not fire more motors to "see if it was a fluke"** |
| CATO | ❌ **Failure, but the most informative one.** Full forensic teardown per `Static_Test_Procedure.md` §8. **Do not clear the debris until it is photographed and mapped** |
| Motor worked, data lost | ❌ **Total failure.** You spent a motor and learned nothing |

---

## 2. The scaling ladder

### 2.1 Why a ladder at all

**Every scale teaches something the previous scale could not, and every scale has a failure mode that
only appears at that scale.** You cannot learn 94 mm lessons on a 38 mm motor, and you cannot afford to
learn 38 mm lessons on a 94 mm motor.

| Scale | Propellant per motor | Impulse class | What it costs to fail | What it is for |
|---|---|---|---|---|
| **24 mm** (current) | ~23 g | D/E, ~24 N·s | Cheap — a tube and a grain | 🔴 **Learning to cast, prime, ignite and fire at all** |
| **38 mm** | ~150–250 g | G/H, ~300–600 N·s | Moderate | **Learning to measure. Repeatability. Process control** |
| **54 mm** | ~500–900 g | I/J, ~1000–2500 N·s | Expensive | **Learning to design for structure and thermal load** |
| **75 mm** | ~1.5–2.5 kg | J/K, ~3000–6000 N·s | Very expensive | **BATES stacks, spacing, inhibitors, multi-segment ignition** |
| **94 mm** | ~3–6 kg | K, ~6000–12000 N·s | 🔴 **Severe** | **The competition scale. Full system integration** |

> **The 24 mm step is not optional and cannot be skipped.** Its purpose is not to produce a useful
> motor. **Its purpose is to make every mistake that is cheap to make, before the mistakes get
> expensive.** See §4.2 for why the 24 mm motor is, counterintuitively, **harder to cast** than the
> 94 mm one.

### 2.2 What each step teaches — and the gate to advance

> ### 🔴 **THE UNIVERSAL GATE**
> **You may not scale up until you have THREE CONSISTENT MOTORS at the current scale, with overlapping
> thrust curves, a documented throat diameter, and a test report for each.**
>
> **"Consistent" means: same design, same propellant batch discipline, measured throat diameters
> within your stated tolerance, and overlapping curves.** A motor that worked once is not a gate pass.

#### Stage 0 — 24 mm (D/E, ~24 N·s)

| | |
|---|---|
| **What it teaches** | **Casting at all.** Grain QC. Priming. Igniter construction and sizing. The firing procedure. Data capture. **That a motor you built can fire** |
| **What it cannot teach** | Repeatability (the sample is too small and too scattered), structural design (there is no structural load worth the name), thermal design (burn is short and the case is thick relative to size) |
| **Primary risks** | Void-driven CATO; ignition failure; **throat-tolerance pressure scatter** (a 2.5 mm throat with ±0.05 mm is ±4% pressure) |
| **Gate to advance** | ✅ **3 motors, overlapping curves, all three test reports filed.** Density check ≥ 90% of ideal on every grain. Ignition time documented |

#### Stage 1 — 38 mm (G/H, ~300–600 N·s)

| | |
|---|---|
| **What it teaches** | **Real measurement.** This is the first scale where the strand-burner data and the static-fire data can be meaningfully compared, because the burn is long enough and the throat large enough that measurement noise stops dominating. **Process control: can you make the same grain twice?** |
| **Why 38 mm specifically** | **Throat tolerance stops being the dominant error** (an 8 mm throat with ±0.05 mm is ±1.3%). **Whatever scatter remains is YOUR process**, and that is exactly what you need to see |
| **New failure modes** | **Thermal.** Burn times get long enough for case heating to matter. **Inhibitor bond quality** becomes a real variable — the tap test earns its keep here |
| **Gate to advance** | ✅ **3 motors, overlapping curves within a stated band (target ≤10% peak pressure scatter).** Strand burner data at ≥5 pressures, 1–6 MPa, with regime-by-regime fits. Measured throat erosion recorded for every burn. Delivered `c*` and `C_F` computed for every burn |

#### Stage 2 — 54 mm (I/J, ~1000–2500 N·s)

| | |
|---|---|
| **What it teaches** | **Structural design.** At this scale the case is a pressure vessel you must actually analyse, not a tube you bought. **Thermal protection decisions** — insulation, ablatives, heat-sink mass. **Nozzle material performance**: graphite erosion rate, throat growth over a real burn |
| **What changes fundamentally** | **The propellant mass per motor is now large enough that a CATO is a serious event.** Standoff distances, exclusion zones, and the test stand itself need engineering |
| **New failure modes** | **Case heating reducing material strength mid-burn.** Grain web cracking from thermal gradients. **Port-to-throat ratio becoming binding** as grain L/D rises |
| **Gate to advance** | ✅ **3 motors, overlapping curves.** A hydrostatic proof test certificate for the case at **1.2 × MEOP**. A written stress analysis with the **2.5 × MEOP burst target** and the **1.5 × absolute minimum**. Measured insulation performance (post-fire case temperature or wall condition) |

#### Stage 3 — 75 mm (J/K, ~3000–6000 N·s)

| | |
|---|---|
| **What it teaches** | 🔴 **Multi-segment BATES.** This is the scale at which a single grain becomes impractical and the club must learn **inter-segment spacing (10–20% of grain diameter)**, **inhibitor bonding on multiple segments**, and **ignition of surfaces sitting in stagnant flow** |
| **Why it is a step and not a jump** | 🔴 **KNSB's "mountain" pressure curve is caused by delayed end-face ignition of BATES segments.** At 75 mm you have enough segments for this to dominate the curve shape, and enough instrumentation heritage to see it clearly |
| **New failure modes** | **Inter-segment gap too small → delayed ignition → mountain curve → over-pressure.** Inhibitor disbond on a long stack. **Grain mass now large enough that a casting defect is a very large amount of stored energy** |
| **Gate to advance** | ✅ **3 motors, overlapping curves. BATES spacing verified experimentally** (vary spacing across the series and document the effect). **Igniter sized and verified not to cause a startup spike**, with the charge-vs-peak-pressure relationship measured. **A pyrogen or equivalent ignition system qualified** if the straw igniter is no longer adequate (see `Ignition_System_Design.md` §8) |

#### Stage 4 — 94 mm (K, ~6000–12000 N·s)

| | |
|---|---|
| **What it teaches** | **Full system integration at competition scale.** Case design, closures, thermal protection, nozzle life, ignition, handling, transport, storage, and the entire ground operation |
| **What is different** | **You are now handling kilograms of propellant per motor.** Failure consequence is qualitatively different. **Every process step needs a written procedure and a second person** |
| **Gate to flight** | ✅ **3 motors, overlapping curves. Full design documentation. Institutional and regulatory position confirmed** (`00_ADMINISTRATION/Institutional_Approvals_and_Compliance.md`). **Note: IN-SPACe authorisation is not required below 40,960 N·s combined impulse, but prior intimation and local administration approval still apply** |

### 2.3 The gate table — one page

```
=============================================================================
 SCALE-UP GATE -- UVCE ROCKETRY CLUB
=============================================================================
 You may NOT advance a scale until ALL of the following are true:

 [ ] 3 motors of IDENTICAL design, from one propellant batch discipline
 [ ] Overlapping thrust curves within a PRE-STATED tolerance band
 [ ] Every motor has a filed test report (24 h rule)
 [ ] Every grain passed the density check (>= 90% of 1.841 g/cm3)
 [ ] Every grain passed the tap test AFTER full cure
 [ ] Throat diameter measured with a pin gauge BEFORE and AFTER every burn
 [ ] Throat erosion rate for YOUR graphite recorded
 [ ] Delivered c* and C_F computed for at least the last 3 burns
 [ ] Strand burner data at >= 5 pressures over 1-6 MPa, regime fits extracted
 [ ] Case proof-tested hydrostatically to 1.2 x MEOP (new designs)
 [ ] Case burst margin documented: target <= 2.5 x MEOP, absolute min 1.5 x
 [ ] Igniter charge mass vs peak pressure relationship documented
 [ ] A written hazard review signed off for the NEW scale
 [ ] NO unexplained anomalies outstanding from the previous scale

 IF ANY BOX IS UNCHECKED, THE ANSWER IS NO.
=============================================================================
```

---

## 3. Inert grain practice

> ### 💡 **THE HIGHEST-VALUE-HOURS ACTIVITY IN THE CLUB'S PROPULSION PROGRAMME**
>
> **Casting is the skill that fails most often, costs the most propellant, and is the least forgiving of
> the club's activities. And it can be practised for almost nothing, with almost no risk, using table
> salt.**

### 3.1 The recipe

> **INERT propellant is prepared in EXACTLY THE SAME MANNER as genuine propellant, except that COMMON
> TABLE SALT (sodium chloride) is substituted for potassium nitrate as the oxidiser.**
>
> **The O/F ratio remains the same — 65/35 — as do all other aspects of preparation.**

| Component | Genuine KNSB | **INERT (simulated)** |
|---|---|---|
| Oxidiser | **Potassium nitrate (KNO₃)** | 🔵 **Common table salt (sodium chloride, NaCl)** |
| Fuel | **Sorbitol** | **Sorbitol — same** |
| **Ratio** | **65 / 35 by mass** | 🔵 **65 / 35 by mass — SAME** |
| SLES surfactant | 0.1% of melt | 🟡 **Optional.** See §3.4 |
| **Casting temperature** | **130 °C / 265 °F** | **Same procedure. Verify the slurry behaves as expected** |
| Cure before demould | 24 h | 24 h |
| Identification additive | **NONE** | 🔴 **FOOD DYE OR PIGMENT — MANDATORY** |

**Everything else is identical.** Same grinding of the "oxidiser," same sifting and dessication of the
sorbitol, same weighing, same tumbler blending, same thermostatically controlled vessel, same
pour-and-scoop, same plungers, same coring rod, same cure, same demould.

> 🔴 **If you change the process for the inert grain, you are not practising the real process.**
> Run inert casts as **dry runs of the exact procedure**, timed with a stopwatch, with the batch record
> filled in as if it were real.

### 3.2 Why it works — the fidelity evidence

> **"Both the melting rate and the viscosity of the melted slurry of the INERT propellant has been found
> to be QUITE SIMILAR to genuine propellant."**

**That is the whole basis for using it.** The two properties that make sugar propellant casting hard —
**how fast it melts** and **how fast it thickens as it cools** — are reproduced. Since the difficulty of
casting is almost entirely those two properties plus the stickiness, **the practice transfers.**

**The one observed difference, and why it is a feature:**

> **Both the sucrose-based and the dextrose-based INERT propellants tend to CARAMELISE TO A GREATER
> EXTENT than the genuine propellants.** This is attributed to differences in thermochemical properties
> between KN and NaCl.
>
> **"This tendency to caramelize to a greater degree does not adversely affect the simulated behaviour of
> the INERT propellant. In fact, this feature is BENEFICIAL since it allows for the INERT propellant to be
> readily identified."**

**The physical explanation, if you want to understand it rather than just accept it:**

| Compound | Specific heat capacity `C_s` vs KNO₃ | Caramelisation observed |
|---|---|---|
| **Sodium chloride (NaCl)** | **Lower over the full temperature range of interest** | **Greater than genuine** |
| **Potassium chloride (KCl)** | **Notably lower still** | **More severe than NaCl** |
| **Magnesium sulphate (MgSO₄)** | May be an even better match — **but it is hydrated, containing ~30% molecular-bound water, and must first be dessicated** | Not tried |
| **Potassium nitrate (KNO₃)** | Reference | Genuine KNSB behaviour |

**Why lower `C_s` means more caramelisation:** the substitute oxidiser **stores less thermal energy per
degree**, so for the same heat input the mixture reaches a **higher temperature** — and higher temperature
means more caramelisation of the sorbitol.

> **And the crucial detail: KNO₃ experiences a STEP INCREASE in `C_s` at approximately 125 °C due to a
> phase change of the solid material.** That step makes the difference between KNO₃ and NaCl **even more
> pronounced right in the middle of your casting temperature band.** This is not a subtle effect and it
> is why the inert grain looks and smells different while behaving similarly.

### 3.3 🔴 Identification — a safety requirement, not a nicety

> ### **"It'd not bode well to inadvertently load an INERT grain into a rocket motor. Of more serious concern, A GRAIN OF GENUINE PROPELLANT MUST NEVER BE INADVERTENTLY MISTAKEN AS A SIMULATED GRAIN!"**

**Note the direction of the concern.** The dangerous mistake is not accidentally firing an inert grain —
which does nothing. **The dangerous mistake is treating a REAL grain as inert, handling it casually, or
storing it in the wrong place.**

**Therefore both directions must be controlled:**

| Control | Requirement |
|---|---|
| 🔴 **Add a drop of food dye or a pigment to the INERT mixture** | This is the source's explicit recommendation and the club adopts it as mandatory |
| **Colour the inert grain a colour that does not occur naturally** | **Genuine KNSB is white to light ivory.** Use **blue, green or a strong red** — never anything in the white/cream/ivory range |
| **Label the mould, the batch record, and the storage bag** | `INERT — DO NOT FIRE` in marker, on the container |
| **Never store inert grains in the same container as genuine grains** | 🔴 **Separate storage. Physically separate. No exceptions** |
| **Never leave an inert grain loose on the bench** | Loose grains get picked up. **Loose grains get confused** |
| **Dispose of inert grains at the end of the session** | 🔴 **An inert grain that no longer exists cannot be mistaken for anything.** Break it up and bin it, or keep it labelled in a marked container for tap-test practice |

> **The caramelisation difference (§3.2) is a second, independent identification cue — but it is not
> guaranteed for KNSB.** The source says the greater caramelisation was observed for **sucrose- and
> dextrose-based** inert propellants. **Do not rely on colour change as your only marker. Use the dye.**

### 3.4 What to practise on inert grains — the drill

**Run this as a timed exercise, at least five times, before you cast your first real grain.**

| # | Skill | Success criterion |
|---|---|---|
| 1 | **Rolling the tagboard casting tube** | Tube ID equals mandrel diameter; no unrolling; glued surface fully bonded by pressing with a pen |
| 2 | **Mould assembly** | Casting tube fully inserted; temporary epoxy dab through the bulkhead holes; nozzle greased only on the convergent area; closing pin protrudes exactly half way up the throat |
| 3 | **Weighing and blending** | Batch record complete; 65/35 within 0.1 g; excess factor correctly applied |
| 4 | **Melting to temperature and holding** | Slurry reaches casting temperature and is held **within ±5 °C** without exceeding it |
| 5 | 🔴 **Pour-and-scoop speed** | **Total transfer time from vessel to mould, measured with a stopwatch.** This is the skill. Getting faster at this is the single largest improvement available to a new club |
| 6 | **Plunging sequence** | Solid plunger to bottom **without pressing hard enough to push propellant past the closing pin**; coring rod fully seated; hollow plunger final pack with the rod held to stop it being forced out |
| 7 | **Cooling and demoulding** | Coring rod removed by twisting then pulling; casting tube slit and peeled without chipping the grain |
| 8 | 🔴 **Density check** | **Compute the inert grain's density and its ratio to the NaCl/sorbitol ideal.** If you cannot achieve ≥90% on a salt grain you will not achieve it on a propellant grain |
| 9 | **Inhibitor bond** | Tap test the inert grain. **Learn what a good tap sounds like on a material where being wrong costs nothing** |

> **Skill 5 is the one to obsess over.** The source is explicit: a smaller quantity of slurry **cools more
> quickly, becoming even more viscous**, and the casting process is **"a combination of precise pouring,
> hurried scooping and careful packing."** Against a thickening slurry, **seconds are percent density.**

### 3.5 Inert grains and the density check — a free calibration exercise

**The density check is the club's primary void-detection tool**
(`Propellant_Formulations.md` §3.3, `Technical_Reference_Nakka.md` §1.8). **Inert grains let you practise
it and calibrate your ear and your eye against a known outcome:**

1. Cast an inert grain **deliberately badly** — under-tamp it, pour it slow, don't tap the mould.
2. Run the density check. **You now know what a 78% grain looks like and how it measures.**
3. Cast a good one. **You now know what a 95% grain looks like.**
4. **Cut them both open.** See the voids. **This is the single most instructive afternoon available**,
   because after it you will never again wonder whether a grain is "probably fine."

> ⚠️ **Inert grains are NOT proof-tested in a motor.** They are not propellant, they do not burn
> usefully, and firing one produces molten salt spray and almost no impulse. **The purpose of an inert
> grain is to be cast, measured, tapped and cut open.**

---

## 4. Strand burner design and construction — the highest-value first build

> ### 🔴 **BUILD THIS BEFORE YOU BUILD ANYTHING ELSE.**
>
> **The club's burn-rate coefficient `a` and pressure exponent `n` are currently UNKNOWN for the club's
> materials.** `config/engineering_constants.md` §3 marks them 🔴 **BLOCKING**, and
> `Motor_Design_Guide.md` states the consequence directly: **"You cannot design a throat without it."**
>
> **The strand burner is how you get it. It is cheap, it is safe relative to a motor, and it produces the
> single input the entire motor design chain depends on.**

### 4.1 What a strand burner is

**A pressure vessel in which a thin, inhibited rod of propellant is burned from one end, at a controlled
and measured pressure, with the burn time measured over a known length.**

```
        STRAND BURNER -- CONCEPT
   ============================================================
                        pressure gauge / transducer
                                 ||
                                 \/
    +--------------------------------------------------+
    |                                                  |
    |   N2 / inert gas pressurisation ------->         |
    |                                                  |
    |      +-------------------------------+           |
    |      |  INHIBITED PROPELLANT STRAND   |          |
    |      |                                |          |
    |   TC>|===============================>|  burn    |
    |      |   ^                     ^      |  front   |
    |      |   |<---- gauge length ->|      |  travels |
    |      |  TC #1                TC #2    |  upward  |
    |      +-------------------------------+           |
    |                                                  |
    |         ^                    ^                   |
    |      thermocouple         thermocouple           |
    |      #1 (start)           #2 (finish)            |
    |                                                  |
    |                    vent / burst disc             |
    +--------------------------------------------------+
                                 ||
                                 \/
                          to exhaust / water

   burn rate  r  =  gauge length / ( t2 - t1 )
```

### 4.2 The apparatus, in detail

| Element | Specification / note |
|---|---|
| **Pressure vessel** | A steel tube rated well above the maximum test pressure (the reference work covered **1 to >100 atm**, i.e. **>10 MPa**). **Fit a burst disc or relief valve** — this is a pressure vessel containing burning propellant |
| **Gas supply** | **Nitrogen or other inert gas** to pressurise the vessel to the target test pressure. **Do not pressurise with air unless you have thought about it** — a vessel full of propellant and oxygen is a different hazard |
| **Pressure measurement** | A **calibrated pressure gauge or transducer**. **Record the pressure during the burn, not just before it** — a strand burner that loses pressure during the burn has a `P(t)` you have not measured |
| **Thermocouples** | 🔴 **Two, at each end of the gauge length.** Type K is adequate. The **first** detects the arrival of the flame front at the start of the gauge length; the **second** detects it at the end |
| **Strand** | 🔴 **A thin, straight rod of propellant with its sides INHIBITED so it burns only at the end face.** This is what makes it a *strand* burner and not a "burn a lump and see" device |
| **Gauge length** | The distance between the two thermocouples, **measured accurately**. Burn rate = **gauge length ÷ (t₂ − t₁)** |
| **Ignition** | A small igniter at the strand's lower end — **the club's Ignition Powder and bridgewire**, scaled down. **The strand must be primed the same way the grain is** (`Ignition_System_Design.md` §2), or you are measuring the ignition delay, not the burn rate |
| **Data capture** | 🔴 **Thermocouple time-of-arrival, logged.** Two timestamps per run is all you need; a simple DAQ or a storage oscilloscope is enough. **The thermocouple traces also show you whether the burn front was planar** — a ragged trace means a channelled or cracked strand and the run is void |
| **Vent / exhaust** | The vessel must be vented safely. **Do not point it at anything you value** |

### 4.3 The measurement

**Burn rate is timed over a gauge length with thermocouples at each end.**

$$r \;=\; \frac{L_{\text{gauge}}}{t_2 - t_1}$$

| Symbol | Meaning |
|---|---|
| `L_gauge` | Distance between thermocouple #1 and thermocouple #2, measured to ±0.5 mm |
| `t₁` | Time thermocouple #1 sees the flame front |
| `t₂` | Time thermocouple #2 sees the flame front |
| `r` | **Linear burn rate at the vessel pressure** |

**Pressure range to cover: 1 atm to over 100 atm (0.1 to >10 MPa).**

> **For the club's operating regime the useful window is 1 to 6 MPa** — the design chamber pressure band
> for KNSB is **2–6 MPa** (`Motor_Design_Guide.md` §3), and you must also characterise the **low-pressure
> start-up region below 2 MPa** because that is where your motor either lights or does not.

### 4.4 🔴 KNSB IS A MESA PROPELLANT — one power law is invalid

> **This is the single most important thing to understand before you fit anything.**

$$r \;=\; r_o \;+\; a\,P_c^{\,n} \qquad (r_o \text{ usually taken as zero})$$

| Behaviour class | Propellant | Log-log plot |
|---|---|---|
| **Classic St. Robert** | **KNSU** | **A straight line over the full range.** One power function fits |
| **Plateau** | **KNDX** | `n` drops toward zero over a pressure band |
| 🔴 **MESA (inverted-mesa)** | 🔴 **KNSB** | 🔴 **Over some pressure range `n` becomes very small or even NEGATIVE — burn rate stops responding to pressure, or FALLS as pressure rises** |

> ### **CONSEQUENCE: A GIVEN `a`, `n` PAIR IS VALID ONLY OVER A DISTINCT PRESSURE RANGE.**
>
> **You do not fit one line through all your data. You identify the pressure regimes, and you fit each
> one separately.**
>
> **The plotted `log r` vs `log P` curve for KNSB will not be straight. Fitting a single straight line
> through it and calling the residuals "scatter" is the specific mistake this section exists to prevent.**

### 4.5 Extracting `a` and `n` — the procedure

| Step | Action |
|---|---|
| **1** | **Run the strand burner at many pressures, not a few.** Minimum **5 points**, ideally **8–10**, **logarithmically spaced** across **0.5–8 MPa**. Concentrate points in **1–6 MPa** — your operating band |
| **2** | **Run each pressure at least twice.** Scatter between repeat runs at the same pressure is your **measurement uncertainty**, and you cannot interpret the fit without it |
| **3** | **Plot `log r` against `log P`** | 
| **4** | 🔴 **LOOK AT THE PLOT BEFORE YOU FIT ANYTHING.** Identify the regimes by eye: where is the slope steep, where is it flat, where does it turn over? |
| **5** | **Fit a straight line to EACH regime separately.** The slope of the log-log line **is** `n`. The intercept gives `a` |
| **6** | **Convert `a` to the club's unit convention.** 🔴 **`a` carries the units of `P^(−n)`.** **Quote `a` in mm/s/MPaⁿ with `P` in MPa, every single time.** Fitting with pressure in MPa and then feeding pressure in Pa into the same equation gives an answer wrong by `10^(6n)` — about **63×** at `n = 0.3` — and it will not look obviously wrong |
| **7** | **Check `n` against the acceptable band.** > **The pressure exponent for a practical propellant should be between 0.3 and 0.6 in the regime of the motor's steady-state operating condition.** **If your fit lands outside 0.3–0.6 in your operating band, stop and investigate before designing a motor** |
| **8** | **Record the regime boundaries and the fit quality.** Publish the regime table, not a single pair |
| **9** | **Repeat the whole exercise whenever a process parameter changes** — grind time, dessication, raw material lot, mixing time. See `Propellant_Formulations.md` §9.2 |

### 4.6 The measured anchor points you are trying to reproduce

**These are Nakka's numbers, from dessicated materials with excellent experimental technique.**

| Pressure | Burn rate |
|---|---|
| **14.7 psia (1 atm, 0.101 MPa)** | **0.102 in/s = 2.59 mm/s** |
| **1000 psia (6.89 MPa)** | **0.443 in/s = 11.25 mm/s** |

**A naive single power law through only these two points gives `a ≈ 1.99 mm/s/MPaⁿ`, `n ≈ 0.30`.**

> ⚠️ **That is ILLUSTRATIVE ONLY. It is exactly the single-law fit that mesa behaviour invalidates.**
> It is the placeholder currently in `config/engineering_constants.md`, marked ⏳. **It is not a design
> value and no throat may be cut from it.**
>
> **A single-power-law fit constrained to pass through these two anchor points cannot reproduce the shape
> of the curve between them.** Do not be tempted to use it "just to get started." You will cut a throat
> that is wrong, and you will not know by how much.

### 4.7 What you are looking for, and what to do when it comes back ugly

| Observation | Interpretation | Action |
|---|---|---|
| Two clean regimes, `n` in 0.3–0.6 in the operating band | ✅ **Design it.** Use the high-pressure fit for `P_c` and the low-pressure fit for the start-up transient | Proceed to motor design |
| `n` very small or negative over part of the range | ✅ **Expected — that is mesa behaviour.** Not a mistake | Size the throat **with margin** and expect the start-up to be reluctant. Use the regime that applies |
| **`n` > 0.6 in the operating band** | 🔴 **Stability concern.** Above ~0.6 the motor's response to a pressure perturbation grows faster than the nozzle can relieve it | **Do not fire. Re-examine the technique and the data before anything else** |
| **`n` ≥ 1 anywhere** | 🔴 **Inherently unstable.** Rising pressure raises burn rate faster than it raises mass flow out of the nozzle | **Redesign. This cannot be flown** |
| **`a` much LOWER than the reference values** | ✅ **Expected.** As-obtained, undessicated materials give **lower `a`** | **This is the safe direction.** Lower pressure, longer burn. **But it is still wrong, and it must go into the design** |
| **`a` much HIGHER than reference** | 🔴 **Investigate immediately.** Over-dried grain? Different grind? Contaminated batch? | Stop. Check the dessication record and the grind record |
| **Huge scatter between repeat runs** | **Technique, not propellant.** Strands not inhibited properly; gauge length wrong; thermocouples loose; ignition delay included in `t₁` | Fix the technique and re-run. **Improved experimental technique measurably reduces scatter — this was demonstrated in the 2010 Gudnason thesis versus earlier work** |

> **Note the moisture split, which makes your life easier:**
> **Residual moisture suppresses burn rate by reducing `a`. It does NOT change `n`** — fine-dessicated
> and granular KNSB show **identical log-log slopes**.
>
> **So: `n` is a material property — measure it once and it holds. `a` is a process property — it depends
> on your dessication, your storage, and your batch.**
>
> 🔴 **Measure `a` on every new raw-material lot. Re-check `n` only when the formulation or the process
> changes.** `Propellant_Formulations.md` §5.1 has the full treatment.

---

## 5. Instrumented static fire

> **This section covers the instrumentation and the data reduction. The PROCEDURE — distances, arming,
> countdown, misfire, NO-GO criteria — is in `40_SAFETY/Static_Test_Procedure.md` and is not repeated
> here. Where the two documents touch, the Safety Manual governs.**

### 5.1 Thrust measurement — load cell

#### 5.1.1 Why the club can build its own

> **A basic (single-gauge) load cell built by the reference method costs no more than $10–20 USD; a
> four-gauge version about double.**

**And there is a second, better reason than cost:**

> **The value proposition: an inexpensive "dispensable" load cell for MAIDEN FIRINGS of new or modified
> designs that might CATO, saving the commercial unit for proven designs.**

#### 5.1.2 The design concept — a bending-beam cell

**A block of metal (steel, aluminium or brass) with a single hole drilled through it and a slit cut on one
side**, creating a **bending "bridge"** on the opposite side to which the strain gauges are bonded.

**Force is applied at the bridge**, producing **combined bending and axial compressive stress, with
bending dominant.** The stress/strain relationship is **linear**, hence the **output is linearly
proportional to applied load.**

> 🔴 **Key advantage: total displacement under load is very small.** This **"nearly eliminates unwanted
> dynamic effects associated with mass and large displacement (e.g. spring) systems."** This was the
> specific lesson from the reference's earlier spring-and-deflection-bar rig, which suffered **severe
> underdamped oscillation** and needed a hydraulic damper.

**Gauge arrangements:**

| Arrangement | Gauges | Output | Use |
|---|---|---|---|
| **Single gauge** | 1 | Basic | Minimum viable |
| **Two gauges side-by-side** | 2 active | **Double the output** (double sensitivity and resolution) | Good compromise |
| **Full bridge** | **2 active + 2 passive** | **Excellent sensitivity, and when properly designed minimises adverse effects of temperature changes** | ✅ **Club standard** |

**Mounting: a single bolt into a tapped hole at the base of the load cell.**

**The five geometrical variables:**

| Variable | Meaning | Design limit |
|---|---|---|
| **`B`** | Body width | — |
| **`t`** | Body thickness | **B/8 ≤ t ≤ B/2** |
| **`D`** | Hole diameter | **B/3 ≤ D ≤ 2B/3** |
| **`b`** | Location of applied load | **b ≥ B/2** |
| **`e`** | Location of the hole | — |
| **`H`** | Body height | **B ≤ H ≤ 1.75B** |

**Stress limits:**

- **Maximum stress occurs at the curved surface of the bridge and is COMPRESSIVE.** A **stress
  concentration factor `k`** is read from a chart.
- ✅ **Design so that the maximum body stress under full load is approximately HALF the yield stress
  (`F_ty`)** of the body material. This (1) prevents permanent strain affecting calibration and (2) ensures
  good linear response.
- 🔴 **The body stress is the limiting factor, NEVER the strain gauge.** A typical foil gauge takes **1%
  strain (or more) without damage** — **at least double** what a steel or aluminium body can take without
  permanent deformation.
- ✅ **For best results, maximum gauge strain should be less than 2000 microstrain. A good design target is
  1500 microstrain.**

> 🔴 **`LOADCELL.XLS` is the design aid.** Enter the desired load capacity, body dimensions and material,
> then choose hole diameter, hole location and load application point such that the maximum body stress
> does not exceed the recommended values. **Use it. Do not guess these five variables.**

#### 5.1.3 Construction — the exact sequence

| Step | Action | Note |
|---|---|---|
| 1 | **Choose the body material from what is on hand** | Minimises cutting. A bar of aluminium cut to length may be all you need |
| 2 | 🔴 **Mark out the body hole location accurately** | Then **drill a series of progressively larger holes** | **This prevents the location "drifting" during drilling.** A drifting hole changes `e`, which changes the calibration |
| 3 | **Drill and tap the mounting hole** at approximately mid-width | |
| 4 | **Cut the slot with a hacksaw** | Yes, a hacksaw. It is not a precision feature |
| 5 | **Drill a shallow hole for the ball bearing** | |
| 6 | 🔴 **Epoxy a hardened steel ball bearing into the shallow hole** | It **"precisely determines the load application point"** and **has the strength to handle large loads without damage.** If damaged, remove it by **moderately heating the ball to soften the epoxy** |
| 7 | **Lightly sand the gauge bonding surface with 600-or-finer grit** | |
| 8 | **Clean with acetone or lacquer thinner** | Same discipline as the grain primer |
| 9 | **Bond the gauges with cyanoacrylate or epoxy** | **Epoxy is easier and perhaps more reliable** |
| 10 | 🔴 **Active gauges: grid lines running PARALLEL to the long edge** | Orientation matters |
| 11 | **Passive gauges (4-gauge version): mount anywhere, but grid lines PERPENDICULAR to the active gauges** | The recommended location is near the active gauges — this is what gives temperature compensation |
| 12 | **Cover the gauge with a protective layer of epoxy**, immersing a portion of the lead wires | |
| 13 | **Wire the four gauges as a Wheatstone bridge** | See §5.1.4 |

**Strain gauges used by the reference:**

| Gauge | Part number | Cost |
|---|---|---|
| No lead wires (solder pads only) | **OMEGA SG-3/350-LY43** | **$45 USD per package of 10** |
| **With lead wires attached** ✅ | **KFG-5-120-C1-11L1M2R** | **$59 USD per package of 10** |

> **If using the no-lead version, 30 AWG wire-wrap wire is soldered to the pads with an illuminated
> magnifier lamp.** That is a fiddly job. **Pay for the leaded version if the budget allows.**

**Prototype performance, for calibration of your expectations:** a **250 lb (1100 N) capacity** cell in
**6061 aluminium** with dual active gauges and two dummy gauges achieved a **maximum deflection under full
load of a mere 0.0035 inch (0.09 mm)**, measured with a feeler gauge.

#### 5.1.4 The amplifier circuit — exact topology and parts

**Topology:** the four strain gauges **SG1–SG4** form a **Wheatstone bridge**. The bridge output goes to
the **Vin+ and Vin− terminals of an INA122 instrumentation amplifier**. The amplifier output (**Vo and
ground**) feeds an **A/D converter**. **Power: two 9 V batteries**, with the INA122 supply rails regulated
by **+5 V and −5 V regulators**; a single **DPST switch** powers the amplifier.

**Parts list (Digi-Key P/N):**

| Item | Digi-Key P/N | Qty |
|---|---|---|
| Instrumentation Amplifier | **INA122PA-ND** | 1 |
| Positive Voltage Regulator, 5 V | **LM78L05ACZFS-ND** | 1 |
| Negative Voltage Regulator, 5 V | **LM320LZ-5.0-ND** | 1 |
| 1.0 µF capacitor | **P2105-ND** | 2 |
| Switch (or similar DPDT/DPST) | **SW102-ND** | 1 |
| Fixed resistor `R_G` (sets the gain) | — | 1 |
| 9 V battery strap connector | **2243K-ND** | 2 |

**Gain-setting procedure:**

| Step | Action |
|---|---|
| 1 | **Calculate the maximum gauge strain** — from the design equation or `LOADCELL.XLS` |
| 2 | **Bridge output:** `e = (E/4)·GF·(ε₁ − ε₂ + ε₃ − ε₄)` | `GF` = the gauge's **Gage Factor**; `E` = the **excitation voltage** |
| 3 | **Required gain:** `G = Vo / e` | `Vo` = the desired amplifier output voltage |
| 4 | **`R_G`** from the INA122 datasheet relation |

**Worked example (the reference's 200 lb cell):**

| Quantity | Value |
|---|---|
| Maximum expected gauge strain | **1778 microstrain** |
| **`GF`** | **2.06** |
| **Excitation `E`** | **5.0 V** |
| Note | **SG2 and SG4 are passive, so their strain is always zero** |
| 🔴 **Bridge maximum output voltage** | **0.009157 V** |
| Output range chosen | **0 to +5 V** |
| **Required gain `G`** | **5.0 / 0.009157 = 546** |

**Bridge balance:** with zero strain the bridge output is ideally zero. **In reality small resistance
differences give a small output that may be positive or negative.** **This is not a problem — the output
can simply be ZEROED using the analysis software.** Alternative: **"balancing resistors" in the Wheatstone
bridge**.

**Reference gauge specifications (the 350 Ω type):**

| Parameter | Value |
|---|---|
| Resistance | **350 ohm** |
| Type | **Constantan metal foil, phenol resin backing** |
| Grid length | **3 mm** |
| Compensation | **Self-temperature compensation for aluminium** |
| Operational temperature | **−10 °C to 70 °C** |
| **Gage Factor** | **2.06** |
| Strain limit | **2%** |

**Load-cell connector:** **RadioShack 274-001 (plug) / 274-002 (receptacle)**. Digi-Key alternatives:
**CP-1040-ND / CP-1240-ND**; locking versions **CP-1034-ND / CP-1234-ND**.

**Verification:** 3-D FEM models with **more than 1000 tetrahedron elements** (NASTRAN) showed
**predicted gauge stress agreed well with FEM**, and **prediction of maximum body stress tended to be
conservative by about 10 percent.**

#### 5.1.5 DAQ hardware

| Item | Specification |
|---|---|
| **Reference unit** | **DATAQ DI-154RS** — **4 channel, 12-bit, up to 250 samples/second**, with **WINDAQ** software |
| **Alternative** | **DATAQ DI-194RS** — also suitable and affordable |
| **Club approach** | Any logger meeting **≥100 Hz per channel, ≥12-bit** is adequate for pressure; see §5.3 for thrust |

### 5.2 Chamber pressure measurement

#### 5.2.1 Two methods — and when to use the cheap one

| Method | Description | Use when |
|---|---|---|
| **(a) Analog gauge + video camera** | An appropriate analog pressure gauge, read by a video camera recording the gauge | ✅ **Cheaper, and used when testing motors with a HIGHER RISK OF CATO** — new designs, uncharacterised propellants |
| **(b) Pressure sensor + electronic DAQ** | A pressure sensor interfaced to a data acquisition system | Proven designs where you want the full trace |

> 🔴 **Club rule: first firing of any NEW design uses method (a).** It is the instrumentation equivalent of
> the dispensable load cell (§5.1.1). **Do not put a transducer you cannot replace into a motor you have
> never fired.**

#### 5.2.2 🔴 Sensor protection — the copper tube

> **Sensor protection is essential and is achieved with a length of copper tubing. The COOL TRAPPED AIR in
> the tube compresses on firing and isolates the sensor from the hot gases. Additionally, copper absorbs
> some of the heat.**

**Additional protection for a sensor: pack the inlet port with grease** — this (1) protects the element
from direct exposure to hot corrosive combustion gases and (2) keeps it cool.

> 🔴 **"A heated pressure sensor may give erroneous readings."**

#### 5.2.3 Plumbing — flare fittings, not compression

> **"In the aerospace field, flare fittings are used exclusively."** Compression fittings are simpler, but
> **flare gives a much more reliable, leak-free connection that withstands repeated use.** A **flaring
> tool** is required.

**Exact plumbing, component by component:**

| # | Component | Detail |
|---|---|---|
| 1 | **Threaded hole in the bulkhead** | Tapped **1/8 NPT or 1/4 NPT** |
| 2 | **Male adapter fitting** | One end **flared**, other end **NPT**. Screws into the bulkhead with **teflon tape or pipe sealant** |
| 3 | 🔴 **A small ball of medium steel wool inserted into the hole in the bulkhead** | **Acts as a filter to stop liquid combustion residue entering.** Without it, the residue **cools, solidifies and BLOCKS THE LINE** — and you lose the line mid-burn |
| 4 | **Copper tubing** | **Three-foot (1 metre) length, 1/4 inch diameter**, **flared at both ends** — slip the **flare nuts** on **before** forming the second flare |
| 5 | **A full loop bent in the tube** | For compactness and joint flexibility. **The loop also traps the air that does the protecting** |
| 6 | **Flare female adapter** | One end flared, other end **female NPT**. The gauge or sensor screws into this adapter with **teflon tape/sealant on the NPT threads** |
| 7 | 🔴 **Teflon tape/sealant is NOT used on the flared joint** | It is a metal-to-metal seat. Tape there causes leaks, not prevents them |

**Combined thrust + pressure setup:**

| # | Component |
|---|---|
| 1 | Replace the bulkhead male adapter with a **short steel nipple (1/8 NPT or 1/4 NPT)** |
| 2 | A **Tee** connects to the other end of the nipple |
| 3 | A **square-head plug** screws into the opposite end of the Tee — 🔴 **the square head of the plug butts against the load cell, transferring the motor's thrust load** |
| 4 | The third Tee connection goes to the copper tube via a **flare male adapter and flare nut** |
| 5 | All three Tee joints sealed with teflon tape or pipe sealant |

> **Pipe fitting rating note:** **standard pipe fittings can be used even if their "pressure rating" is
> well below the motor's expected MEOP.** For small fittings the **actual burst pressure is much greater
> than rated**, because the rating incorporates a large safety factor for wear, corrosion and rough
> handling. ✅ **Use only undamaged (preferably new) fittings.**

### 5.3 Sampling rate — what to actually use

> ### ✅ **"100 samples per second is just right" for pressure.**

| Measurement | Recommended rate | Why |
|---|---|---|
| **Chamber pressure** | ✅ **100 samples per second** | 🔴 **"Too high a sampling rate can result in 'noisy' data that needs to be software filtered to be usable."** |
| **Video / gauge reading** | ✅ **30 frames per second is "perfectly fine for most cases"** | A gauge read by camera needs only enough frames to resolve the transient |
| **Thrust** | 🟡 **100 Hz minimum; higher if the stand is stiff and the cell is fast** | Total impulse is the **area under the curve**. 100 Hz on a 2 s burn is 200 samples — enough for the integral, marginal for resolving the ignition transient. **The club's Safety Manual requires ≥100 Hz and prefers 1000 Hz; take the higher number if your logger supports it** |
| **Post-processing** | **Filter only what you must, and say what filter you used** | **The raw file is the record.** Never overwrite it |

**Club resolution:** run at **100 Hz for pressure** (per the reference) and **≥1000 Hz for thrust** (per the
Safety Manual), on the same time base, with a **sync marker** captured in both.

### 5.4 🔴 Strategy note — measure pressure ONLY on a new design

> ### **"Measuring solely chamber pressure is a good strategy for new motor designs, as it avoids potentially destroying an expensive load cell if the motor should overpressurize and blow out the nozzle or bulkhead."**

**This is the single most useful piece of test-programme strategy in the reference, and it is
counterintuitive** — the instinct is to measure everything the first time.

**The argument in full:**

| Reason | Detail |
|---|---|
| **1. A pressure-only setup cannot destroy a load cell** | If the motor **over-pressurises and blows out the nozzle or the bulkhead**, the load cell is in the blast path. With pressure-only plumbing, there is nothing expensive there |
| **2. Pressure gives you a good thrust estimate anyway** | **"As chamber pressure and thrust are directly proportional, related by the thrust coefficient and throat area (both of which may be considered constant), a preliminary estimate of thrust over the full duration of the burn can be obtained."** |
| **3. For an assumed `C_F`, you get the whole thrust curve** | `F = C_F · P_o · A_t`. **For a well-designed, reasonably well-made steel nozzle, `C_F` can conservatively be taken as 1.5 for sugar propellant.** Throat area from the measured diameter |
| **4. Everything you need to catch a failure is in the pressure trace** | See §5.5 |

> ### ✅ **CLUB POLICY**
> **First firing of a new motor design: PRESSURE ONLY.**
> **Second and subsequent firings of a design that has survived the first: thrust AND pressure.**
> **The dispensable home-made load cell (§5.1.1) is for the in-between case — where you want thrust on a
> design that is not yet proven but is no longer a total unknown.**

**The reference nozzle specification for taking `C_F = 1.5` conservatively:**

| Parameter | Value |
|---|---|
| Operating pressure | **1000 psi** |
| **Convergent half-angle** | **30°** |
| **Divergent half-angle** | **12°** |
| **Expansion ratio** | **> 8** |
| Material | **Steel** |

### 5.5 Diagnostics from the pressure trace

> **The chamber pressure trace is the single most diagnostic measurement in the entire test.** Four
> patterns, four causes:

| Pattern | Documented cause | What to check |
|---|---|---|
| 🔴 **SLOW RAMP-UP** | **"Slow ramp-up is often a consequence of an UNDERPOWERED IGNITER."** | Bridgewire span; battery voltage **under load**; igniter charge mass; igniter placement; **primer coverage** (see `Ignition_System_Design.md` §2) |
| 🔴 **EXTENDED TAIL-OFF** | **"An extended tail-off period could mean that there was DELAYED IGNITION of some propellant surface regions."** | **End-face primer coverage.** Inter-segment spacing if BATES. Grain remnants will show which surfaces burned last |
| 🔴 **LOWER OVERALL CHAMBER PRESSURE** | **"Lower overall chamber pressure is often related to some particular aspect of PROPELLANT PREPARATION, such as OXIDISER PARTICLE SIZE."** | Grind time record; sieve analysis; mix time; moisture/dessication record. **Also check `a` — this is the expected result of as-obtained materials** |
| 🔴 **"MOUNTAIN" / TRIANGULAR CURVE** | **KNSB-specific. Delayed ignition of the END FACES of grain segments.** Also the **flushing** mechanism (see `Propulsion_Roadmap.md` §4.1) | End-face primer; inter-segment spacing (**10–20% of grain diameter**); grain remnants |
| **Startup spike** | 🔴 **Oversized igniter charge.** **See `Ignition_System_Design.md` §5 — this is the failure that shears the safety bolts retaining the motor head** | Charge mass record. **Reduce the charge and re-test, do not fire again unchanged** |
| **Pressure correct, thrust low** | **Nozzle problem — `C_F`** | Expansion ratio, divergence angle, throat erosion, flow separation |

### 5.6 Data reduction — delivered Isp, `c*` and `C_F`

#### 5.6.1 Total impulse and specific impulse

$$I_{\text{tot}} \;=\; \int_0^{t_b} F\,dt \qquad\text{(the AREA UNDER THE THRUST–TIME CURVE)}$$

$$I_{sp,\text{delivered}} \;=\; \frac{I_{\text{tot}}}{m_p\,g_0}$$

| Symbol | Meaning | Unit |
|---|---|---|
| `I_tot` | **Total impulse** | N·s |
| `m_p` | **Propellant mass actually loaded** | kg |
| `g_0` | **Standard gravity, 9.80665 m/s²** | m/s² |
| `I_sp` | **Delivered specific impulse** | s |

> 🔴 **Use the mass of propellant that was actually in the motor** — the grain mass from the batch record,
> not the design mass. **A 10% mass error is a 10% Isp error.**

#### 5.6.2 Delivered `c*` — the propellant's combustion efficiency

$$c^* \;=\; \frac{P_c\,A_t}{\dot m}$$

**Reduced from discrete measured data** by summing the pressure values over the burn. 🔴 **Take care with
units:**

| System | Pressure | Throat area | Mass | Result |
|---|---|---|---|---|
| **Metric** | **N/mm² (= MPa)**, or **Pa** | **mm²** if pressure is N/mm²; **m²** if pressure is Pa | **kg** | **m/s** |
| **US** | **psi** | **inch²** | **lbₘ ÷ g (32.18 ft/s²)** | **ft/s** |

> **"To obtain propellant mass, the weight of propellant, in pounds, must be divided by g (32.18 ft/sec²)."**
> **Mixing these up is the classic `c*` error and it produces a plausible-looking wrong number.**

#### 5.6.3 🔴 Delivered `c*` for standard sugar propellants is typically 90–95% of ideal

> **"From experience, delivered c-star for the standard sugar propellants is typically in the range of
> 90-95% of ideal."**

**And the diagnostic value:**

> **"As c-star is a benchmark of propellant combustion efficiency, if the value is lower, it's likely a
> result of shortcomings of preparation, such as INADEQUATE MIXING, LARGE OXIDISER PARTICLE SIZE or
> EXCESSIVE RESIDUAL MOISTURE. Chamber pressure also plays a (lesser) role."**

| Delivered `c*` (% of ideal) | Verdict | Action |
|---|---|---|
| **> 95%** | ✅ Excellent | Record it |
| **90–95%** | ✅ **Normal for sugar propellants** | Record it |
| **85–90%** | 🟡 Below normal | Check mix time, grind record, dessication record |
| **< 85%** | 🔴 **Preparation problem** | **Do not scale up.** Fix the process. Check the strand-burner data for the same batch |

> **Compare against ProPEP or an equivalent propellant evaluation program for the ideal value.** ⏳ **The
> club's ideal `c*` for KNSB is currently a design assumption (~900–950 m/s) pending exact retrieval.**
> **Use a `c*` efficiency of 0.92–0.95 when computing expected performance, and always measure `c*` from a
> static test.**

#### 5.6.4 🔴 Thrust coefficient — a well-designed sugar nozzle delivers 1.6 or slightly better

$$C_F \;=\; \frac{F}{P_c\,A_t}$$

| Nozzle | Delivered `C_F` | Thrust vs a simple hole |
|---|---|---|
| **A simple hole, no divergent cone** | **≈ 1.0** | Baseline |
| **A well-designed and reasonably well-made steel nozzle** | ✅ **1.6 or slightly better** | 🔴 **A 60% thrust increase over a simple hole** |
| **Conservative design value for sugar propellant** | **1.5** | Use this for estimating thrust from pressure alone (§5.4) |

> **"A sugar-propellant nozzle with a well designed nozzle can have a delivered Cf value of 1.6 or
> slightly better, indicating a thrust increase of 60% over a simple hole."**

**Two rules for computing `C_F`:**

| Rule | Detail |
|---|---|
| 🔴 **Only meaningful during STEADY-STATE operation** | **Start-up and tail-off phases are neglected.** Averaging `C_F` over the whole burn including the transient gives you a number that describes nothing |
| 🔴 **If throat erosion occurs, use the AVERAGE of the initial and final throat diameters** | **"The simplest way is to use the average between the initial and final throat diameters."** Measure the throat **before and after every burn** |

#### 5.6.5 The performance split — what each number implicates

| `c*` | `C_F` | Meaning |
|---|---|---|
| ✅ Good | ✅ Good | **The motor works.** Record the delivered numbers and use them for flight simulation |
| ❌ Poor | ✅ Good | 🔴 **PROPELLANT problem.** Mixing, particle size, moisture. **Go back to `Propellant_Formulations.md` §4, §5** |
| ✅ Good | ❌ Poor | 🔴 **NOZZLE problem.** Expansion ratio, divergence angle, separation, erosion. **Go back to `Motor_Design_Guide.md` §6** |
| ❌ Poor | ❌ Poor | **Both.** Start with the propellant — it is upstream |

> **This split is what makes `c*` and `C_F` worth computing.** Peak thrust and total impulse tell you
> *that* something is wrong. **The split tells you WHICH HALF of the motor to fix.**

---

## 6. Hydrostatic proof testing

> **"It is a good practice to hydrostatic pressure test new motor designs."**
> **Club rule: it is mandatory for every new case, every new closure design, and every new nozzle
> retention scheme.**

### 6.1 The method

| Step | Action |
|---|---|
| **1** | **Fill a COMPLETED and SEALED motor with water** |
| **2** | 🔴 **Bleed all air** — this is the important part, **because trapped air stores energy that water does not** |
| **3** | **Pressurise with a grease gun or hydraulic jack fitted with a pressure gauge** |
| **4** | ✅ **Pressurise to 1.2 × MEOP** (maximum expected operating pressure) |
| **5** | 🔴 **Place a PLYWOOD SHIELD between the motor and the operator** |
| **6** | **Hold the pressure** and inspect for weeping, deformation or leakage **from a distance** |
| **7** | **Record the pressure, hold time, and observations** |

> ### 🔴 **WHY THE PLYWOOD SHIELD IS NOT OPTIONAL**
>
> **"Although compressed water stores little energy, a plywood shield should nevertheless be placed
> between the motor and the operator IN CASE TRAPPED AIR IS PRESENT."**
>
> **The physics:** compressed water stores very little energy, so a water-filled vessel that splits simply
> splits — it does not throw fragments. **Trapped air is a compressed-gas spring.** A vessel containing
> even a small air pocket, on failure, **releases that gas explosively** and turns the case into
> fragments.
>
> **You cannot verify that there is no trapped air.** You can only bleed carefully and then shield as
> though there is. **The shield costs a sheet of plywood.**

### 6.2 Design context — do not build a boilerplate motor

> 🔴 **"Avoid 'boilerplate' motor designs. These thick-walled heavy-duty contraptions have the capability
> of storing an incredible amount of energy before bursting, increasing the potential risk associated with
> catastrophic failure."**

| Rule | Value |
|---|---|
| **Target burst pressure** | ✅ **≤ 2.5 × MEOP** (safety margin of 2.5) |
| 🔴 **Absolute minimum margin** | ✅ **1.5 × MEOP** |
| **Rationale** | **A case that bursts at 5× MEOP holds far more energy than one that bursts at 2.5×.** When it eventually fails — and something eventually fails — **it fails harder** |

> **This is counterintuitive and it is the correct engineering.** The instinct is "thicker is safer."
> **Thicker is safer against bursting and MORE DANGEROUS when bursting happens.** The right answer is a
> case sized with a *known, modest* margin, proof-tested, and treated with respect.

### 6.3 Rejection criteria

| Observation | Verdict |
|---|---|
| **Holds 1.2 × MEOP with no weeping, no deformation, no leakage** | ✅ **Pass.** Record it and proceed |
| **Any permanent deformation** | 🔴 **REJECT.** No repair. No "it's probably fine" |
| **Any leak at a thread, seal, or weld** | 🔴 **REJECT.** Diagnose and rebuild, then re-proof |
| **Any failure** | 🔴 **REJECT.** The design is wrong. **Do not simply thicken the wall — find out why it failed** |
| **Case with a history of an off-nominal firing** | 🔴 **RETIRE, not reuse** |

> **"Any permanent deformation, leak, or failure = the case is rejected. No repair."**

---

## 7. Grain density QC — use these exact criteria

> ### 🔴 **THIS IS THE CLUB'S PRIMARY VOID-DETECTION TOOL. USE THE NUMBER, NOT YOUR EYES.**

### 7.1 The method

**The density check detects air bubbles and voids.** Air inclusion of a few percent is negligible.
🔴 **Sizeable bubbles, many bubbles, or trapped voids significantly increase burning surface area, which
leads to over-pressurisation or a CATO.**

| Step | Action |
|---|---|
| **1** | **Weigh the grain segment** — accurately, on a scale appropriate to the mass |
| **2** | **Measure its volume from measured dimensions** — **calipers are more accurate than a ruler** |
| **3** | 🔴 **Core diameter need not be measured explicitly — it EQUALS the coring rod diameter.** Measure the coring rod |
| **4** | **If the grain is integral with its casting tube, SUBTRACT the tube's mass and thickness** |
| **5** | **Compute:** `grain density = mass / V_g` | Units consistently: **grams & centimetres**, or **pounds & inches** |
| **6** | **Compute the density ratio:** `Density ratio (%) = (calculated grain density / ideal density) × 100` |

**Two tools that do the arithmetic for you:**

| Tool | What it does |
|---|---|
| **`Graindensity.xls`** | Performs the volume/density calculation and provides **ideal densities for a wide variety of sugar propellants**, including those **doped with oxides or other ballistic modifiers** (Table A1) |
| **Club ideal density** | **KNSB 65/35: 1.841 g/cm³ = 0.0665 lb/in³** |

### 7.2 🔴 The accept / reject criteria — the exact numbers

> ### ✅ **Nakka typically obtains grain densities of 95% ideal using the casting method described.**
>
> ### 🟡 **If the measured grain density is less than around 90%, this implies SIGNIFICANT AIR INCLUSION (POROSITY) or the presence of significant flaws or air bubbles.**

| Measured density ratio | Verdict | Action |
|---|---|---|
| **≥ 95% of ideal** | ✅ **Target.** This is what good casting technique produces | **Accept** |
| **90–95%** | 🟡 **Acceptable** | **Accept.** Record it. Watch for a trend across a batch |
| 🔴 **< 90%, WITH visible external flaws or bubbles** | 🟡 **Repairable** | ✅ **"External air bubbles or flaws can be repaired by OPENING A CAVITY THEN FILLING IT WITH MOLTEN PROPELLANT."** Re-run the density check after repair |
| 🔴 **< 90%, with NO visible external flaws** | 🔴 **DISCARD THE GRAIN** | 🔴 **"Then either hidden voids exist or porosity is present, and the grain SHOULD BE DISCARDED. The consequence of firing such a grain could result in a CATO due to unpredictable burning rate behaviour."** |

> ### 🔴 **READ THE ASYMMETRY IN THAT TABLE**
>
> **A grain below 90% with a visible bubble is repairable. A grain below 90% with NO visible bubble is
> scrap.**
>
> **The reason is that you can only repair what you can see.** A visible bubble can be opened and filled,
> and you can verify the repair. **A grain that is 88% dense with a clean exterior has voids you cannot
> find, cannot open, and cannot fill — and those voids are internal free surfaces that will multiply your
> burning area the instant the flame front reaches one.**
>
> **That is why the rule is discard, not investigate.** You have no tool that will tell you where the
> voids are. **The grain is a known unknown and it goes in the bin.**

### 7.3 The tap test — the second mandatory check

**Applies ONLY to a grain whose inhibitor is an integral casting tube.**

**Why:** the inhibitor must be **intimately bonded**. **Any disbonding lets hot gas seep between the
inhibitor and the propellant, increasing the burning area** — the same failure mode as an internal void,
delivered by a different route.

| Step | Action |
|---|---|
| **1** | 🔴 **Only perform AFTER FULL CURE** — or the indications may be false. **Residual moisture in the bondline also causes a false fail** |
| **2** | **Tap the inhibitor gently with a coin** — **a larger coin works better** — at points **all around** the segment |
| **3** | **Sound and feel should be a SOLID tap, not a dull one.** The difference **takes experience to recognise** |
| **4** | ✅ **Best technique: listen to the RELATIVE tap sounds.** **Every tap should sound identical** |
| **5** | **Analogy:** a dull tap is like **tapping hard rubber**; a good tap is like **tapping hard plastic** |

**Accept/reject rules:**

| Observation | Verdict |
|---|---|
| **All taps identical and solid** | ✅ **PASS** |
| **One isolated dull spot, rest solid** | ✅ **Acceptable** — single isolated spots are generally not a problem |
| **A different tap sound at the SEAM of a rolled casting tube** | ✅ **NORMAL** — not a defect |
| 🔴 **A different tap response BETWEEN SEGMENTS OF THE SAME BATCH** | ❌ **REJECT that segment.** **"If one segment sounds distinctly different and less solid, its inhibitor bond may be flawed. Reject that segment."** |
| **Multiple dull spots, or a dull region** | ❌ **REJECT** |

> ✅ **The batch-relative comparison is the powerful technique, and it is the one to teach.**
> You are not judging absolute tap sound. **You are judging one segment against its siblings, made from
> the same batch on the same day.** That controls for propellant, cure, humidity **and your own hearing**.
>
> **A segment that is the odd one out is the segment that will fail.**

> 🟢 **A useful reference point: on grains CURED UNDER PRESSURE, tap test failure is very rare — a few out
> of roughly 200 segments.** **Pressure curing is a real, available process improvement**, and it is
> something the club should trial once it has a repeatable baseline.

**False-fail recovery:** **a few days in a desiccator often converts a false fail to a pass.** That is a
moisture artefact in the bondline, not a real disbond.

### 7.4 The other documented grain-kill failure mode — over-drying

| Cause | Consequence | Control |
|---|---|---|
| 🔴 **Long-term storage in a desiccator** | **The grain can get OVERLY DRY, producing a burn rate GREATER than normal. This could result in a CATO** | 🔴 **A desiccator is for DRYING, not for STORAGE.** For long-term storage: **zip-lock bag, then freezer** |

**Full treatment in `Ignition_System_Design.md` §3.4.** The mechanism: **residual moisture suppresses burn
rate by reducing `a`.** Remove too much and `a` rises above design, and **`P_c ∝ a^(1/(1−n))`** — roughly
`a^1.43` at `n = 0.3`.

### 7.5 Where the QC sits in the workflow

```
   CAST ---------> CURE 1-2 days --------> DEMOULD
                                             |
                                             v
                              CLEAN (acetone, core + end faces)
                                             |
                                             v
                                    DRY (desiccator, short)
                                             |
                                             v
                                    TRIM / CUT TO LENGTH
                                             |
                                             v
                       +---------------------+---------------------+
                       |                     |                     |
                       v                     v                     v
              DENSITY CHECK            TAP TEST              MEASURE & RECORD
              (mass + dimensions)   (after FULL cure)      mass, OD, ID, length
                       |                     |                     |
                       +---------------------+---------------------+
                                             |
                              >= 90%?  AND  tap PASS?
                                             |
                            +----------------+----------------+
                            |                                 |
                           YES                                NO
                            |                                 |
                            v                                 v
                     PRIME (thin,               < 90% + visible flaw  -> REPAIR
                     200 micron)                < 90% + no flaw       -> DISCARD
                            |                   tap fail (batch-odd)  -> REJECT
                            v
                    DRY PRIMER -> STORE (bag, freezer) -> FIRE
```

---

## 8. Batch documentation — what to record for every grain

> **An undocumented grain is a grain you cannot learn from.** When a motor behaves unexpectedly six weeks
> from now, the batch record is the only thing that will tell you why.

### 8.1 The grain batch record

**A single sheet per batch. Filled in as you go, not from memory afterwards. Signed by the operator and a
witness.**

```
=============================================================================
 UVCE ROCKETRY CLUB -- KNSB 65/35 GRAIN BATCH RECORD
=============================================================================
 BATCH ID: ______________     DATE: __________     GRAIN SEGMENT IDs: ______
 OPERATOR: ________________   WITNESS: ________________
=============================================================================

 -- 1. RAW MATERIALS ---------------------------------------------------------
 KNO3  supplier: ______________  lot #: __________  date received: __________
       KN purity check: 33 g / 100 ml water -> pH = ______  PASS (6.5-7.0)/FAIL
 Sorbitol supplier: ____________  lot #: __________  date received: _________
 SLES  supplier: ______________  lot #: __________  concentration: ______ %
       Confirmed NOT Sodium Lauryl Sulfate (SLS):  Y / N

 -- 2. PREPARATION -----------------------------------------------------------
 KNO3 grind time per load:  ______ s     Number of loads: ______
   Gyration performed: Y / N     Grinder ID: ________
   Sieve analysis (74 um / 234 um), date: __________  Result: ______________
 Sorbitol sifted: Y / N     Sorbitol desiccated: Y / N    Days: ______
   Desiccator desiccant charge date: __________   Fresh: Y / N
 Slurry batch mass prepared:  ______ g
   KNO3 = ______ g   Sorbitol = ______ g   Sum = ______ g   Scale check: OK/NO
 SLES added after melting:  ______ g   (target 0.1% of molten mass = ______ g)
 Blend method: ____________   Blend time: ______ h   (target >= 3 h per 100 g)

 -- 3. CASTING ---------------------------------------------------------------
 Casting vessel: ____________________  Thermostatic, NO exposed elements: Y/N
 Vessel preheat temp: ______ C      Casting temperature reached: ______ C
   (target 120-130 C +/- 5 C)       Max temperature observed: ______ C
 Melt start: ________   Casting temp reached: ________   Pour complete: ______
   *** TOTAL TRANSFER TIME: ______ s ***
 Slurry appearance: pure white / light ivory / yellowish-amber
   (yellow-amber = alkaline KN impurity -> investigate the lot)
 Tap-out performed: Y / N     Coring rod preheated (150 C, 15 min): Y / N
 Coring rod lubricant: ______________   Fully seated: Y / N
 Solid plunger used: Y / N     Hollow plunger used: Y / N
 Plungers frozen >= 1 h beforehand: Y / N
 Temperature at end of cast: ______ C

 -- 4. CURE AND DEMOULD ------------------------------------------------------
 Cure start: ____________   Demoulded: ____________   Cure time: ______ h
   (target 24 h for KNSB)
 Demoulding notes: ______________________________________________________
 Coring rod removed by twist-then-pull: Y / N
 Casting tube slit and peeled cleanly: Y / N   Chipping observed: Y / N

 -- 5. FINISHING -------------------------------------------------------------
 Cleaned with: acetone / lacquer thinner    Passes until clean: ______
 Desiccator dried: Y / N    Time: ______    Grain not sticky: Y / N
 Trimmed / cut: Y / N    Cut method: ______________
 *** REMOVED FROM DESICCATOR -- NOT STORED THERE ***  Y / N

 -- 6. DIMENSIONS AND MASS ---------------------------------------------------
 Segment   Mass (g)   OD (mm)   ID (mm)   Length (mm)   Notes
 --------  ---------  --------  --------  ------------  --------------------
    1      _________  ________  ________  ____________  ____________________
    2      _________  ________  ________  ____________  ____________________
    3      _________  ________  ________  ____________  ____________________
   (Core ID = coring rod diameter = ______ mm, measured)

 -- 7. DENSITY CHECK ---------------------------------------------------------
 Segment   Volume (cm3)   Density (g/cm3)   Ratio (% of 1.841)   PASS/FAIL
 --------  -------------  ----------------  -------------------  ----------
    1      ___________    _______________   __________________   _________
    2      ___________    _______________   __________________   _________
    3      ___________    _______________   __________________   _________
   Ratio >= 95% = target.   90-95% = acceptable.   < 90% = see below.
   < 90% with a VISIBLE flaw:  repaired?  Y / N   Re-checked ratio: ______
   < 90% with NO visible flaw: *** GRAIN DISCARDED ***  Y / N

 -- 8. TAP TEST (AFTER FULL CURE ONLY) ---------------------------------------
   Full cure date: __________   Days cured: ______
 Segment   All taps identical/solid?   Batch-relative comparison   PASS/FAIL
 --------  -------------------------  -------------------------  ----------
    1      Y / N                      same as siblings / ODD      _________
    2      Y / N                      same as siblings / ODD      _________
    3      Y / N                      same as siblings / ODD      _________
   Tube seam tap difference noted: Y / N  (this is NORMAL)
   Any segment ODD vs its batch -> REJECTED: Y / N

 -- 9. PRIMER ----------------------------------------------------------------
 Primer batch: IP pulverised with mortar & pestle first: Y / N
 IP/IPA consistency: thick paint  Y / N
 Coat type: *** SINGLE THIN COAT ***  Y / N   (target 200 micron)
 Surfaces coated: CORE [ ]  FWD END FACE [ ]  AFT END FACE [ ]  OUTER [ ]
 Inspected for bare patches: Y / N
 Dried: 24 h open air [ ]   OR   30 min air + desiccator [ ]
 Primer durability check after handling: INTACT / TOUCHED UP

 -- 10. STORAGE --------------------------------------------------------------
 Stored: zip-lock bag -> freezer  Y / N     Date: __________
   *** NOT stored in the desiccator ***  Y / N
 Removed from freezer: __________  Opened at room temp: Y / N
 Condition on removal: __________________________________________________
 Re-primed: Y / N    Re-checked density/tap (if > 1 month): Y / N

 -- 11. DISPOSITION ----------------------------------------------------------
 ACCEPTED for motor ID: __________     REJECTED: [ ]  Reason: ____________
 Operator signature: ________________  Witness signature: ________________
=============================================================================
```

### 8.2 What else goes in the permanent record

| Record | Where | Retention |
|---|---|---|
| **Grain batch records** | Permanent test record | Indefinite |
| **Strand burner runs** — pressure, gauge length, `t₁`, `t₂`, computed `r`, regime fit | Permanent test record | Indefinite |
| **Static test reports** — per `Static_Test_Procedure.md` §8.3, **within 24 hours** | Permanent test record | Indefinite |
| **Raw data files** — never edited, never overwritten | Two copies, two devices | Indefinite |
| **Video** | Same naming convention as the data | Indefinite |
| **Proof test certificates** | With the case's history | Life of the case |
| **Throat diameter log** — before and after **every** burn | With the motor's history | Life of the nozzle |
| **Case history** — every firing, every inspection, every rejection | With the case | Life of the case |
| **Change-control records** | `Propellant_Formulations.md` §9.3 | Indefinite |

### 8.3 The three numbers to put on the wall

| Number | Value |
|---|---|
| **Ideal cast density** | **1.841 g/cm³** |
| **Typical achieved** | **95% of ideal** |
| 🔴 **Discard threshold** | **< 90% of ideal with no visible flaw** |

---

## 9. Recommended test order and first-year schedule

### 9.1 The order — do not reorder this

**The order is set by the principle of §1.4: cheapest and least destructive first.**

| # | Activity | Depends on | Gate to the next step |
|---|---|---|---|
| **1** | **Build the strand burner** | Nothing | Apparatus holds pressure; thermocouples read cleanly; two repeat runs at one pressure agree within your stated uncertainty |
| **2** | **Inert grain practice ×5** | Nothing (runs in parallel with 1) | **Five consecutive inert grains at ≥90% density**, with transfer time recorded and improving |
| **3** | **Strand burner campaign** | 1, 2 | 🔴 **`a` and `n` extracted per regime, over ≥5 pressures, 0.5–8 MPa, with repeats.** `n` checked against 0.3–0.6 in the operating band |
| **4** | **Motor design re-solve** | 3 | Throat diameter, grain geometry and burn time re-solved with the **measured** law. Port/throat ≥ 2 at ignition. Case margin documented |
| **5** | **Motor hardware build** | 4 | Case, closures, nozzle retention built and dimensioned |
| **6** | 🔴 **Hydrostatic proof test** | 5 | **Holds 1.2 × MEOP, no deformation, no leak.** Certificate filed |
| **7** | **First real grain cast** | 4 | Passes density check ≥ 90% and tap test |
| **8** | 🔴 **First static fire — PRESSURE ONLY** | 6, 7 | Pressure trace captured. `c*` computed. **Motor survived.** Reference §5.4 |
| **9** | **Second and third firings** | 8 | **Three motors with overlapping pressure traces** |
| **10** | **Add thrust measurement** | 9 | `C_F` and delivered Isp computed. Dispensable load cell acceptable |
| **11** | **Repeatability series at 38 mm** | 10 | **The 38 mm gate (§2.2 Stage 1)** |
| **12** | **Scale up** | 11 | Only now |

> 🔴 **The most common way a club gets this wrong is to skip to step 8.** The first firing is exciting,
> the strand burner is boring, and the inert grains are boring. **And then the first firing produces a
> pressure trace that nobody can interpret, because there is no measured `a` and `n` to compare it
> against.** The motor is consumed and the club learns nothing.
>
> **Steps 1–4 are what make step 8 an experiment instead of a stunt.**

### 9.2 Rough first-year schedule

**Twelve months. Assumes a club of 5–8 active members with roughly one full working session per week
(4 hours) plus one weekend day per month for casting and firing.**

| Month | Focus | Deliverable | Note |
|---|---|---|---|
| **1** | **Foundations and apparatus** | **Strand burner built and commissioned.** Inert casting supplies acquired. First two inert grains cast | Strand burner is the **highest-value first build**. ₹₹ |
| **2** | **Inert casting competence** | **Five inert grains at ≥90% density.** Casting procedure written and timed. Transfer time under target | **Density ≥90% on salt before you touch propellant** |
| **3** | **Strand burner campaign** | **8–10 strand runs at ≥5 pressures, with repeats.** Raw `log r` vs `log P` plot produced | 🔴 **This is the month that unblocks everything else.** Budget strand material as propellant |
| **4** | **Burn-rate law extraction** | 🔴 **`a` and `n` per pressure regime, published to `config/engineering_constants.md`.** Regime boundaries documented. `n` checked against 0.3–0.6 | **If `n` is outside the band, this month becomes two months. Plan for it** |
| **5** | **Motor design re-solve and hardware** | **Throat diameter, grain geometry and burn time re-solved with the measured law.** Case and nozzle drawn, then built | The existing design in `config/engineering_constants.md` §4 was computed on the **placeholder** law. **It will change** |
| **6** | **Proof test and first real grain** | 🔴 **Hydrostatic proof at 1.2 × MEOP passed.** First real KNSB grain passes density and tap test. Range arrangements and permissions in place | **Range permission is a long-lead item. Start it a month earlier than you think** |
| **7** | 🔴 **First static fire — pressure only** | **Pressure trace captured. `c*` computed. Test report within 24 h.** Reference §5.4 | **Expect the trace to differ from prediction.** That is the result |
| **8** | **Second and third firings** | **Three overlapping pressure traces.** Post-fire throat diameters measured and erosion recorded | **Change one variable at a time, or change nothing** |
| **9** | **Thrust measurement** | **Dispensable load cell built, calibrated, and flown on a firing.** `C_F` and delivered Isp computed | Build the load cell **before** you need it |
| **10** | **38 mm entry** | **38 mm case and nozzle designed and built. Proof-tested.** First 38 mm grain cast | **Check the 24 mm gate: three overlapping traces, all reports filed** |
| **11** | **38 mm firing series** | **Three 38 mm motors fired.** Curves compared against the 24 mm data and the strand-burner law | **This is where process control becomes visible**, because throat tolerance stops dominating |
| **12** | **Review and next-year plan** | **Written programme review.** All data in the permanent record. Next scale's hazard review drafted | **Quantify your scatter.** It is the honest headline number |

**What the schedule deliberately does NOT include:** no 54 mm motor, no 75 mm motor, no 94 mm motor, no
BATES stack, no star grain, no flight. **Those are year-two items, and some are year-three.**
**The year-one deliverable is a measured burn-rate law and three repeatable motors — and that is a
genuinely hard year's work.**

> ⏱️ **Where the schedule will actually slip:**
>
> | Risk | Effect | Mitigation |
> |---|---|---|
> | **`a`/`n` campaign takes longer than a month** | Pushes everything right | **Budget two months.** The schedule has slack built into month 4 |
> | **Inert grain density will not reach 90%** | Stops the programme | **This is the point of practising on salt.** If you cannot do it on salt, find out why before spending propellant |
> | **Range permission and site access** | Can slip months and is outside the club's control | **Start month 6's arrangements in month 4** |
> | **Monsoon (June–October) halts outdoor firing** | Seasonal hard stop | **Put the strand burner and casting work in the monsoon months. Put firings either side** |
> | **Bengaluru humidity raises batch-to-batch scatter** | `a` drifts, curves stop overlapping | **Dessicate on a fixed 2-day clock. Re-measure `a` if the data goes strange.** `Propellant_Formulations.md` §5.2 |
> | **Exams** | Two months of near-zero throughput | **Schedule the reading and review work there** |

---

## 10. Cross-references

| For | See |
|---|---|
| Igniter design, primer recipe, igniter sizing | `Ignition_System_Design.md` |
| Formulation, particle size, moisture, density QC rules | `Propellant_Formulations.md` §3.4, §4, §5, §9 |
| Motor design equations, `Kn`, throat sizing, nozzle design | `Motor_Design_Guide.md` §2, §6 |
| Full static-test procedure, distances, arming, misfire, NO-GO list | `40_SAFETY/Static_Test_Procedure.md` |
| Scale-up ladder, gate criteria, INR costs, risks, timeline | `Propulsion_Roadmap.md` |
| The flushing phenomenon and sorbitol grain-length guidance | `Propulsion_Roadmap.md` §4.1 |
| Design constants, `a` and `n` status | `config/engineering_constants.md` §3 |

---

*UVCE Rocketry Club — `10_PROPULSION/Motor_Test_Program.md`. Quantitative criteria traced to Richard
Nakka's Experimental Rocketry Site (`inert.html`, `casting1.html`, `igniter.html`, `static.html`,
`pressure-measurement.html`, `strainlc.html`, `safety.html`, `knsbchar.html`) as extracted in
`80_REFERENCE/nakka-technical-reference.md` §1–§3, §5–§9. The grain density accept/reject criteria
(95% typical, 90% discard threshold) and the delivered `c*` and `C_F` figures are the source's own and are
reproduced without adjustment. This document is subordinate to `40_SAFETY/Safety_Manual_Master.md`.*
