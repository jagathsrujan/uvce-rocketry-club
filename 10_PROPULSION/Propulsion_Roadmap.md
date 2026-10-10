# UVCE Rocketry Club — Propulsion Roadmap

**Document:** `10_PROPULSION/Propulsion_Roadmap.md`
**Applies to:** the club's propulsion capability programme, from zero experience to a reliable K-class motor
**Status:** 🟡 **Stage 0 in progress.** Two known-hard problems are documented in §4 and both are counterintuitive.
**Parent references:** `Technical_Reference_Nakka.md` Parts 1–5; `80_REFERENCE/nakka-technical-reference.md` §8, §9; `Propellant_Formulations.md`; `Motor_Design_Guide.md`; `Motor_Test_Program.md`; `Ignition_System_Design.md`

> ### 🔴 **READ §4 BEFORE YOU READ THE STAGES**
>
> **Two hard-won findings from the source material change the shape of this roadmap, and both of them
> point the same way:**
>
> 1. **The FLUSHING phenomenon.** Sorbitol propellant loses performance catastrophically in **short
>    grains.** Measured delivered Isp: **108 s for the G and H motors, but 129 s for the I motor whose
>    grain was twice as long.** The design guidance: **the minimum length of a sorbitol grain for optimum
>    performance is on the order of 13–15 inches.**
> 2. **Casting difficulty scales INVERSELY with size.** **"The larger the grain (or rather the mould), the
>    easier it is to cast."** The small motor is the hard one.
>
> **Together these mean: your first motor is the hardest motor you will ever build, and it is also the
> worst-performing per gram of propellant. Both facts must be designed around, not discovered.**

---

## 1. How to use this roadmap

### 1.1 What this document is

**A staged capability plan.** Each stage lists what you can do at the end of it, what you must have built
and learned to get there, what it costs, what can kill you, and **the specific evidence required before
you are allowed to move to the next stage.**

### 1.2 The three rules that govern the whole document

| # | Rule | Why |
|---|---|---|
| **1** | 🔴 **You may not scale up until you have three consistent motors at the current scale** | §3. **One motor proves nothing** |
| **2** | 🔴 **You may not finalise a throat until you have measured `a` and `n` for your own materials** | **KNSB is a mesa propellant — a single power law is invalid.** The club's `a` and `n` are currently 🔴 BLOCKING |
| **3** | 🔴 **The small motor is the hard one.** Do not treat Stage 0 as a formality | §4.2. **The single most counterintuitive fact in the programme** |

### 1.3 The scale ladder at a glance

| Stage | Motor | Impulse class | Propellant | Cumulative cost | Primary lesson |
|---|---|---|---|---|---|
| **0** | **24 mm** | D/E, ~24 N·s | ~23 g | **₹25,000–40,000** | **Learn to cast. Learn to fire. Make every cheap mistake** |
| **1** | **38 mm** | G/H, 300–600 N·s | 150–250 g | **₹60,000–1,00,000** | **Process control. Repeatability. Real measurement** |
| **2** | **54 mm** | I/J, 1000–2500 N·s | 500–900 g | **₹1,20,000–2,00,000** | **Structural design. Thermal design. Nozzle life** |
| **3** | **75 mm** | J/K, 3000–6000 N·s | 1.5–2.5 kg | **₹2,00,000–3,50,000** | **BATES stacks. Spacing. Multi-segment ignition** |
| **4** | **94 mm** | K, 6000–12000 N·s | 3–6 kg | **₹3,00,000–5,00,000** | **Full system integration at competition scale** |

> ⚠️ **Cost figures are rough planning estimates in INR, not quotations**, and they assume the club
> already owns basic workshop tooling. **They include the instruments, because the instruments are the
> point** — a motor without data is a firework. **Itemised per stage in §5–§9.**

### 1.4 What "capability" means

**Capability is not "we built a motor that worked." Capability is:**

1. **A measured burn-rate law for the club's own materials**, valid per pressure regime.
2. **A documented casting process** that produces grains at **≥ 90% of ideal density**, repeatably.
3. **A documented ignition system** that lights the grain reliably without over-pressurising it.
4. **A test programme** producing **three or more overlapping thrust curves** per design.
5. **A documented failure record.** **A club with no CATOs has not been testing hard enough — it has been
   testing too little, or hiding the results.**

---

## 2. Stage 0 — 24 mm (D/E, ~24 N·s)

### 2.1 What this stage is for

**Stage 0 is not about the motor. It is about making every mistake that is cheap to make.**

The 24 mm motor produces about **24 N·s** — enough to lift a 330 g rocket to 200 m. It is a real motor.
**But its purpose in the programme is to be the vehicle for the club's first fifty lessons.**

| What Stage 0 teaches | Why it is cheap here |
|---|---|
| **Casting technique** | **23 g of propellant per attempt.** A rejected grain costs a rupee or two of chemicals |
| **Grain QC** | Density check, tap test — learned on grains you can afford to bin |
| **Igniter construction** | A gram of Ignition Powder per igniter. Learn the nichrome soldering before it matters |
| **Primer application** | Thin coat, correct coverage — practised on a grain you will not fly |
| **The firing procedure** | Full countdown, arming, data capture — run for real, but with a small charge |
| **Data capture and reduction** | Learn `c*` computation on data you can survive losing |
| **Failure experience** | 🔴 **A CATO at 24 mm is a loud noise and a wrecked tube. A CATO at 94 mm is an incident** |

### 2.2 Skills to acquire

| # | Skill | Standard to reach |
|---|---|---|
| 1 | **Melting and casting KNSB** | Transfer from vessel to mould in a **timed, repeatable** operation. Temperature held **120–130 °C ±5 °C** |
| 2 | **Inert grain practice** | **Five consecutive inert grains at ≥90% density** before the first real grain |
| 3 | 🔴 **Strand burner operation** | **Two repeat runs at one pressure agreeing within your stated uncertainty** |
| 4 | **Burn-rate data reduction** | Extract `a` and `n` **per regime** from a `log r` vs `log P` plot. **Not one global fit** |
| 5 | **Grain QC** | Density check and tap test performed on **every** grain, correctly, and recorded |
| 6 | **Ignition Powder preparation** | 80/20 KN/charcoal, no sulphur, 3 h per 100 g blend, wet-paste-granulate |
| 7 | **Straw igniter construction** | 5 mm bridgewire span, acid-paste soldering, **magnified inspection**, alcohol rinse |
| 8 | **Grain priming** | **Thin** coat, ~200 micron, core + both end faces, correct drying |
| 9 | **Firing procedure** | Full remote sequence executed from memory, correctly, under observation |
| 10 | **Data reduction** | `c*`, delivered Isp, `C_F` computed from a real test |

### 2.3 Equipment and instrumentation

| Item | Spec | INR (approx.) | Priority |
|---|---|---|---|
| **Strand burner pressure vessel** | Steel tube rated > 15 MPa, with burst disc, N₂ fill, gauge | **₹6,000–12,000** | 🔴 **FIRST BUILD** |
| **Thermocouples (type K) ×4** | For the strand burner gauge length and spares | **₹1,500–3,000** | 🔴 |
| **DAQ / logger** | **≥2 channels, ≥100 Hz, 12-bit.** A DATAQ-class unit or a microcontroller + SD logger | **₹3,000–8,000** | 🔴 |
| **Casting vessel** | 🔴 **Thermostatically controlled electric deep fryer or skillet — NO exposed elements** | **₹2,000–4,000** | 🔴 **Non-negotiable** |
| **IR thermometer / probe thermometer** | For melt temperature | **₹800–2,000** | 🔴 |
| **Scale, 0.001 g resolution** | For SLES dosing and small batches | **₹2,500–6,000** | 🔴 |
| **Scale, 0.1 g resolution, 1 kg** | For batch weighing | **₹800–1,500** | 🔴 |
| **Coffee grinder (KN-dedicated)** | Blade type, **labelled and never used for food again** | **₹1,000–2,000** | 🔴 |
| **Desiccator + fresh CaCl₂** | Sealed container, perforated barrier | **₹500–1,000** | 🔴 |
| **Digital calipers (0.01 mm)** | For grain dimensions and throat measurement | **₹800–2,000** | 🔴 |
| **Pin gauge set** | For throat diameter measurement | **₹1,500–4,000** | 🔴 |
| **Mould hardware** | Casting tubes (tagboard), coring rods, solid + hollow plungers, mould base, closing pin | **₹1,500–3,000** | 🔴 |
| **Pressure gauge, 0–10 MPa, glycerine-filled** | For the first pressure-only firing | **₹1,500–3,000** | 🔴 |
| **Pressure transducer + copper tubing + flare tool** | For later firings | **₹6,000–15,000** | 🟡 Stage 0 late |
| **PPE** | Face shield, heat gloves, nitrile gloves, eye protection, ear defenders ×4 | **₹5,000–10,000** | 🔴 **Before anything else** |
| **Fire cover** | Extinguishers ×2, dunk bucket, bulk water drums | **₹3,000–6,000** | 🔴 |
| **Test stand** | Steel frame, ballasted **≥5× peak thrust** | **₹4,000–8,000** | 🔴 |
| **Motor hardware** | Steel case, closures, graphite nozzle, O-rings | **₹3,000–6,000** | 🔴 |
| **Fireproof storage** | For KNO₃ (separated) and Ignition Powder | **₹3,000–8,000** | 🔴 |
| **Stage 0 total** | | **₹25,000–40,000** | **excluding the load cell, which is Stage 1** |

> 🔴 **The three items that are not optional and not deferrable: the thermostatic casting vessel, the
> PPE, and the fire cover.** Everything else in the list can be improvised or borrowed. **Those three
> cannot**, and a programme that starts without them is not a programme — it is an accident waiting for
> a date.

### 2.4 Risks and mitigations

| Risk | Likelihood | Consequence | Mitigation |
|---|---|---|---|
| 🔴 **Melt ignition from an exposed heating element** | Low if disciplined | 🔥 **Severe burns, fire** | 🔴 **Only a thermostatic vessel with no exposed elements.** The intent: **no exposed heating surface significantly hotter than the propellant's melting point.** If surfaces get hot *before* the powder goes in, **ignition can occur immediately** |
| **Overheating the melt** | Moderate | Decomposition, fume, potential ignition | Hold **120–130 °C ±5 °C**. Watch for the indicators: **colour change ~175 °C, smoke and strong odour ~250 °C**. Auto-ignition **> 300 °C** |
| 🔴 **Void-driven CATO** | **High** — this is the #1 amateur CATO cause | Case rupture | **Density check on every grain. < 90% with no visible flaw = DISCARD.** `Motor_Test_Program.md` §7 |
| 🔴 **Over-dried grain → high burn rate → CATO** | Moderate | Case rupture | 🔴 **A desiccator is for DRYING, not STORAGE.** Bag + freezer for storage |
| 🔴 **Oversized igniter → startup pressure spike → sheared safety bolts** | Moderate | Case rupture | **Start at 0.5 g and step up in 0.25 g.** Buy ignition speed with **primer**, not charge mass |
| **Ignition failure / misfire** | **High** — KNSB is 4.15× harder to ignite than KNSU | Wasted test, approach hazard | **Grain primer. Every time.** `Ignition_System_Design.md` §2 |
| 🔴 **Throat tolerance pressure scatter** | **High** — intrinsic to small motors | Non-repeatable data | **Ream, don't drill.** Measure every throat with pin gauges. **Accept and quantify** the scatter |
| **Strand data unusable (scatter too large)** | Moderate | 🔴 **Blocks the whole programme** | **Inhibit the strands properly. Prime them. Measure the gauge length accurately.** Poor technique, not bad propellant |
| **Propellant dust / grinding incident** | Low | Fire, burns | **Grind KN alone. Never grind a blend. Grounded equipment. Dedicated grinder** |
| **Static discharge** | Low | Ignition of powder | Ground equipment. No synthetic clothing over the melt. No vacuum cleaning |
| **Castration of the programme by regulatory confusion** | Moderate | Loss of a year | **IN-SPACe authorisation is NOT required below 40,960 N·s combined impulse.** Our first motor is **~24 N·s — far below every threshold.** But **local administration approval and written landowner permission are still required for launches, always** |
| **Monsoon shutdown** | **Certain** (Jun–Oct) | Schedule slip | **Schedule strand burner, casting practice and data work into the monsoon.** Fire either side |

### 2.5 Gate criteria to advance to Stage 1

```
=============================================================================
 STAGE 0 -> STAGE 1 GATE
=============================================================================
 [ ] Burn-rate law: >= 5 strand-burner pressures, 0.5-8 MPa, with repeats
 [ ] `a` and `n` extracted PER PRESSURE REGIME (not one global fit)
 [ ] `n` lands in 0.3-0.6 in the motor's steady-state operating band
 [ ] Why the exponent was chosen is written down
 [ ] 5 consecutive inert grains at >= 90% density
 [ ] 3 real KNSB grains at >= 90% density, tap test PASS after full cure
 [ ] 3 motors fired, all 3 with captured pressure traces
 [ ] Motor throat diameter measured with pin gauges BEFORE and AFTER each burn
 [ ] Test report filed within 24 h for every firing
 [ ] Delivered c* computed for at least one firing, within 90-95% of ideal
 [ ] Igniter charge mass vs peak pressure relationship documented
 [ ] Case proof-tested hydrostatically to 1.2 x MEOP
 [ ] Every firing executed with the full remote sequence at >= 100 m
 [ ] Any CATOs fully documented, photographed, and root-caused in writing
 [ ] NO outstanding unexplained anomalies
 [ ] A written hazard review for the 38 mm scale, signed off
=============================================================================
```

---

## 3. Stage 1 — 38 mm (G/H, 300–600 N·s)

### 3.1 What changes fundamentally

| Dimension | Change from Stage 0 |
|---|---|
| **Propellant per motor** | **×10** (23 g → 150–250 g). **A CATO now has real energy in it** |
| **Throat diameter** | ~2.5 mm → **~8 mm**. 🔴 **Throat tolerance stops dominating** — ±0.05 mm on an 8 mm throat is **±1.3% pressure**, versus ±4% on a 2.5 mm throat |
| **Burn time** | Long enough and consistent enough that **thermal effects are measurable** |
| **Grain mass** | Large enough that **density QC actually predicts CATO risk** |
| **What scatter means** | 🔴 **Whatever scatter remains is YOUR PROCESS**, not your tooling. **This is the stage where you find out how good you actually are** |

> ### 🎯 **STAGE 1'S REAL DELIVERABLE IS A NUMBER, NOT A MOTOR**
>
> **Your unit-to-unit scatter in peak chamber pressure and total impulse.** Everything before this stage
> produced a motor. **This stage produces a measurement of your own repeatability** — and that number
> determines whether you can fly, and how much margin every future design needs.
>
> **Target: ≤10% peak pressure scatter across three motors.** If you are at 25%, **do not scale up.** Go
> back to `Propellant_Formulations.md` §9.5 and tighten the process.

### 3.2 Skills to acquire

| Skill | Why it appears at 38 mm and not before |
|---|---|
| **Thrust measurement** | You can now afford to build a **dispensable strain-gauge load cell** and risk it |
| **`C_F` computation** | Nozzle performance becomes separable from propellant performance |
| **Thermal analysis** | Burn is long enough that case temperature at burnout matters |
| **Nozzle erosion measurement** | Throat growth is now measurable and material-dependent |
| **Process control discipline** | 🔴 **The whole point of this stage.** Grind time, dessication time, mix time, transfer time — all timed and recorded |
| **Statistical thinking** | Three motors is a small sample. **Learn what you can and cannot conclude from it** |

### 3.3 Equipment additions

| Item | Spec | INR (approx.) |
|---|---|---|
| **Load cell** | Home-made bending-beam, **capacity chosen so peak thrust is 50–80% of full scale**. 4-gauge full bridge | **₹3,000–8,000** |
| **Strain gauges** | **KFG-5-120-C1-11L1M2R** (with leads) or **OMEGA SG-3/350-LY43** (no leads) | **₹3,500–5,000 per pack of 10** |
| **Instrumentation amplifier + regs + parts** | **INA122** and the support circuit of `Motor_Test_Program.md` §5.1.4 | **₹1,500–3,500** |
| **Pressure transducer** | Rated to **≥2× expected MEOP** | **₹6,000–15,000** |
| **Flare tool + copper tubing + flare fittings** | 🔴 **Flare fittings, not compression** | **₹2,500–6,000** |
| **Graphite nozzle stock** | Rod, for 2–3 nozzles | **₹400–1,200 each** |
| **Motor cases (2–3)** | Steel, or 6061 aluminium with a documented thermal analysis | **₹4,000–10,000** |
| **High-speed camera or phone at 240 fps** | For the ignition transient | **₹0–15,000** |
| **Thermal protection materials** | Kraft paper, polyester resin, phenolic tube | **₹1,000–3,000** |
| **Stage 1 subtotal** | | **₹25,000–60,000** |

### 3.4 Risks and mitigations

| Risk | Mitigation |
|---|---|
| 🔴 **CATO with 10× the propellant** | **Standoff ≥150 m for a new design.** Ballast the stand **≥5× peak thrust**. **Fire from behind hard cover, always** |
| **Case overheating softening the material** | **Aluminium 6061 has only ~80% of room-temperature strength at 150 °C.** Mild steel retains 80% of yield strength at **240 °C**. **Size the case at the temperature it will actually reach** |
| **Inhibitor disbond** | **Tap test after full cure. Batch-relative comparison.** A disbond increases burning area exactly like a void |
| **Over-reliance on three motors** | **Three is the minimum, not the goal.** Report the scatter. **Do not fit a distribution to n = 3** |
| **Scaling enthusiasm** | 🔴 **Resist it.** The gate is three **overlapping** motors, not three motors |
| **Cost escalation** | The load cell, transducer and camera are the expensive items. **Build the load cell; borrow the camera** |

### 3.5 Gate criteria to advance to Stage 2

```
=============================================================================
 STAGE 1 -> STAGE 2 GATE
=============================================================================
 [ ] 3 motors, overlapping thrust curves within a PRE-STATED tolerance band
 [ ] Peak pressure scatter quantified and reported (target <= 10%)
 [ ] Delivered c* and C_F computed for every burn
 [ ] c* within 90-95% of ideal      (else: propellant PREPARATION problem)
 [ ] C_F at or near 1.6             (else: NOZZLE problem)
 [ ] Throat erosion rate for the club's graphite, measured over >= 3 burns
 [ ] Insulation / thermal protection performance measured post-fire
 [ ] Load cell calibrated with known masses immediately before every test
 [ ] 3 motors, all from documented batches, all density-checked
 [ ] Any anomaly explained in writing or explicitly carried forward
 [ ] 54 mm case DESIGN with a written stress analysis
 [ ] 54 mm case PROOF-TESTED hydrostatically to 1.2 x MEOP
 [ ] Burst margin documented: target <= 2.5 x MEOP, absolute minimum 1.5 x
 [ ] Written hazard review for 54 mm, signed off
=============================================================================
```

---

## 4. 🔴 THE TWO HARD LESSONS

> **These two findings are the reason this roadmap does not simply say "build a bigger motor."**
> **Both are counterintuitive. Both are measured. Both determine the shape of the programme.**

### 4.1 LESSON ONE — The FLUSHING phenomenon

**Source: "Burn Characteristics of Sorbitol Based Propellants" by Chuck Knight.**

#### 4.1.1 The three anomalies it explains

Sorbitol propellant shows three odd behaviours that are **not fully understood** and that were observed by
Nakka with his KSB motors, by other experimenters, and in the PVC motor series:

| # | Anomaly |
|---|---|
| **1** | **A slower burn rate in motors than predictions based on strand burn rate tests** |
| **2** | 🔴 **An achieved specific impulse MUCH LESS than the theoretical specific impulse** |
| **3** | 🔴 **A PROGRESSIVE burn characteristic, even with motors whose grains were designed to provide a FLAT response** |

**Theories previously offered: crack formation, and delayed ignition. Knight proposes a third: FLUSHING.**

#### 4.1.2 The mechanism

> **1. Upon ignition, there is NO delayed ignition and all exposed surfaces ignite quickly.**
>
> Evidence: the **"knee" on the leading edge of almost every published thrust curve for sorbitol
> propellant.** Thrust typically reaches a plateau, flattens, then peaks. **Nakka's KSB-002
> ignition-initiator experiment, compared to KSB-001, showed little difference in thrust-curve shape** —
> further evidence that **ignition spreads quickly to all exposed surfaces.**
>
> **2. A process is ERODING the grain surface. This is NOT erosive burning — it is a "FLUSHING" action
> occurring FASTER than the burn rate of the propellant.**

**Two effects follow:**

**(a) PERFORMANCE LOSS.** Propellant is **expelled from the motor before it can burn and contribute to
impulse.**

> 🔴 **The measurement that proves it:**
> **The "G" and "H" motors had specific impulses of ONLY 108 SECONDS while the "I" motor had 129 SECONDS.**
>
> **The explanation: THE GRAIN OF THE "I" MOTOR WAS TWICE AS LONG**, which allowed for a more complete burn
> of propellant — which accounted for the increased performance.

**(b) PROGRESSIVE BURN.** **Flushing is the result of heat that melts the sorbitol PLUS rapidly moving
gases that push the molten propellant from the motor.**

> **Since gases are flowing SLOWEST at the top of the grain and FASTEST near the nozzle, the difference in
> flow rates SHAPES THE CORE INTO A CONE WITH THE BASE OF THE CONE AT THE NOZZLE.**
>
> **This coning action increases `Kn` faster than predicted by conventional uniform burn rate models, and
> contributes to the progressive burning nature of sorbitol.**

#### 4.1.3 🔴 The single most important sentence about flushing

> ### **"The flowing gases DO NOT affect the burn rate at the TOP OF THE CORE or on the END SURFACES. These areas are the ONLY surfaces of the grain that exhibit the TRUE BURN RATE of Sorbitol propellant."**

**Why this matters:** it tells you **which surfaces you can model with your strand-burner data and which
you cannot.** Your strand burner measures the true burn rate. **The nozzle end of your motor's core burns
at 1.37× that rate, or faster, for reasons your strand burner cannot see.**

#### 4.1.4 The quantitative flush rate — from the K1000

| Point | Definition | Measured value |
|---|---|---|
| **Point A** | **The knee of the thrust curve** — the initial `Kn`. **"The only point during the burn that the `Kn` is known with any certainty."** Flushing is ignored here because **it has not had time to take effect** | — |
| **Initial burn rate at ignition, `r_b`** | Calculated from the knee | **0.279 in/s** |
| **Strand-burn-test burn rate at Point A** | From the strand burner | **0.305 in/s** |
| ⚠️ Note | 🔴 **"The reason for the difference between the two burn rates is not clear."** | **A 9% discrepancy the source itself cannot explain** |
| **Point B** | **The instant the flame front reaches the grain OD** — i.e. the flame front has burned through a **web thickness of 0.485 in** | — |
| **Time A → B** | | **1.53 s** |
| 🔴 **Combined burn/flush rate over A→B** | `0.485 in / 1.53 s` | 🔴 **0.381 in/s = 1.37× the initial burn rate** |
| **Total burn time** | | **2.0 s** |
| **A → total burn** | | **1.74 s** |
| **Burn rate at the TOP of the grain** | `0.485 / 1.74` | **0.279 in/s — EXACTLY the rate calculated at Point A** |

> 🔴 **"This accelerated rate is the flush rate of the propellant."** — **1.37×.**

**And the model's prediction, which explains why the `Kn` curve plunges:**

> **With a flush rate of 1.37, the `Kn` takes a DRAMATIC PLUNGE near the end of the progression.** This is
> caused when **the bottom edge of the cone reaches the OD of the grain, leaving a WEDGE-SHAPED GRAIN in
> the upper portion of the motor that shortens at an ever-increasing rate as the cone attempts to get
> wider and wider.**
>
> **The model suggests that the web at the TOP of the core is NOT BREACHED UNTIL THE BURN PROCESS COMES TO
> A COMPLETE END.**

**And the wedge explains the low Isp:**

> **"The propellant in the wedge contributes little or nothing to the overall total impulse of the motor.
> However, specific impulse is the total impulse of the motor divided by the TOTAL WEIGHT OF THE
> PROPELLANT INCLUDING ANY NONCONTRIBUTING PORTIONS. This total weight computes a smaller specific
> impulse than what may have actually been achieved by the motor at any instantaneous point in time."**
>
> 🔴 **You are paying for propellant that does not push.**

**And the honest negative result from the model:**

> **"It was the intention of the model to show that the added area of the conical surface was a major
> factor that compensated for the regressive thrust curve calculated by the uniform burn rate model.
> However, THIS WAS NOT THE CASE."**
>
> **The K1000 exhibited a flat thrust curve because MOST OF THE PROPELLANT WAS BURNED ACROSS THE SHORT
> FLAT PORTION OF THE CURVE** — not because the coning compensated for the regressivity.

#### 4.1.5 The direct experimental proof — the long-chamber test

**The cleanest experiment in the whole body of work, and it is beautifully simple.**

> **A "G" motor was built with a 13 in chamber but a 7 in propellant grain** — matching the original G
> design. **The grain was placed at the TOP of the motor, with a 6 in SPACER between the grain and the
> nozzle.** Fired in the same test stand as the rest of the PVC series.

| Motor | Grain length | Chamber | Delivered Isp |
|---|---|---|---|
| **Original "G"** | **7 in** | 7 in | 🔴 **108 s** |
| **Long-chamber "G"** | **7 in (identical grain)** | **13 in (6 in empty spacer)** | ✅ **124 s** |

> ### **"Clearly, propellant is being FLUSHED from the grain and BURNED IN THE AFT SECTION OF THE LONG CHAMBER that boosts the performance of the motor."**

**Note what this experiment does and does not change:**

| Changed | Not changed |
|---|---|
| **Chamber length** | **Grain design, propellant, nozzle, test stand — all identical** |

> 🔴 **A 15% improvement in delivered specific impulse, from changing NOTHING but the length of empty tube
> downstream of the grain.** That is a bigger performance gain than most propellant "improvements" people
> spend months chasing — **and it is free.**

#### 4.1.6 🔴 THE DESIGN GUIDANCE

> ### **"To maximize the performance of Sorbitol based motors it is best to use LONG rather than SHORT FAT grains. These experiments show that THE MINIMUM LENGTH OF A SORBITOL GRAIN TO ACHIEVE OPTIMUM PERFORMANCE IS ON THE ORDER OF 13" – 15"."**

**13–15 inches = 330–381 mm.**

**And the corollary:**

> **Traditional uniform burn rate models are "good enough to compute approximations for motor designs that
> can be refined through experimentation."**
>
> **Understanding the consequences of flushing allows application of the uniform burn rate model to design
> a REGRESSIVE thrust curve that COMPENSATES for the coning of the core, and to produce a FLAT thrust
> curve.**

#### 4.1.7 🔴 What this means for a 24 mm grain — the implication, stated bluntly

**The club's Stage 0 grain:**

| Parameter | Value |
|---|---|
| **Grain outer diameter** | **24 mm** |
| **Grain length** | **~33 mm** |
| **L/D** | **≈ 1.4** |
| 🔴 **Recommended minimum length for optimum performance** | **330–381 mm (13–15 in)** |
| 🔴 **Shortfall** | 🔴 **The club's grain is roughly 1/10th the recommended length** |

> ### 🔴 **CONSEQUENCE ONE: EXPECT THE LOW ISP. DO NOT PANIC WHEN YOU SEE IT.**
>
> **A 108 s motor was a 7-inch grain. Yours is 1.3 inches.** Knight's own comparison — the "G" at 108 s
> versus the "I" at 129 s — is between grains **7 in and 14 in long.**
>
> **The club should expect its Stage 0 delivered Isp to fall at or below the bottom of the range in
> `Propellant_Formulations.md` (115–130 s). If it comes back at 95–110 s, that is not a mistake. It is
> flushing, and it is predicted.**
>
> **Record it as a data point. It is the club's first confirmation that flushing is real.**

> ### 🔴 **CONSEQUENCE TWO: THE 24 mm MOTOR IS A TRAINING MOTOR, NOT A PERFORMANCE MOTOR.**
>
> **There is no propellant change that fixes this.** The formulation is frozen
> (`Propellant_Formulations.md` §9). **The only fix is a longer grain — which means a bigger motor.**
>
> **So do not spend Stage 0 trying to improve Stage 0's Isp. Spend it learning to cast, prime, ignite and
> measure.** The Isp will come at Stage 1 and Stage 2, when the grain gets long.

> ### 🔴 **CONSEQUENCE THREE: DESIGN THE FLIGHT ON MEASURED IMPULSE, NOT ON THEORETICAL ISP.**
>
> **Every flight simulation and every mass budget must use the delivered impulse you measured on the test
> stand** — not a theoretical Isp and not a published range. **If your 24 mm grain delivers 100 s instead
> of 125 s, your 200 m apogee is not 200 m.** Re-run the trajectory with the real number.

> ### 🔴 **CONSEQUENCE FOUR: LONG AND SLENDER, NOT SHORT AND FAT — AND THIS IS A DESIGN RULE, NOT A PREFERENCE.**
>
> **This inverts the instinct.** A beginner's instinct is "small motor, so short fat grain." **For sorbitol
> propellant the correct instinct is the opposite.**
>
> | Worse | Better |
> |---|---|
> | **Short, fat grain** (L/D ≈ 1–2) | **Long, slender grain** (L/D much higher) |
> | Less residence time for the gas | **More residence time** |
> | Propellant flushed out unburned | **Flushed propellant burns inside the motor and contributes impulse** |
> | Modeled Isp achieved, delivered Isp not | **Delivered Isp approaches modeled** |

#### 4.1.8 What it means for the scaling strategy

**This is the part that reshapes the roadmap.**

| Stage | Motor dia | Realistic grain length | vs the 13–15 in target | Expected flushing loss |
|---|---|---|---|---|
| **0** | **24 mm** | **33 mm** | 🔴 **~10%** | 🔴 **Severe. Expect bottom-of-range Isp** |
| **1** | **38 mm** | **100–150 mm** | 🔴 **~30–45%** | 🔴 **Still significant** |
| **2** | **54 mm** | **200–300 mm** | 🟡 **60–90%** | 🟡 **Moderate. Approaching the target** |
| **3** | **75 mm** | **330–380 mm** — a **single segment** can hit the target | ✅ **100%+** | ✅ **Small** |
| **4** | **94 mm** | **Multiple BATES segments, total ≫ 380 mm** | ✅ **Exceeds** | ✅ **Minimal** |

> ### 🔴 **THE STRATEGIC CONCLUSION — AND IT IS THE OPPOSITE OF WHAT YOU WOULD GUESS**
>
> **1. Per gram of propellant, the small motors are the WORST performers, and the large motors are the
> BEST.** Flushing is a *relative* loss, and it shrinks as the grain gets longer. **So the scale-up is not
> just about flying higher — it is about getting the performance you are already paying for.**
>
> **2. A SINGLE-SEGMENT 75 mm MOTOR CAN ACHIEVE THE 13–15 INCH OPTIMUM LENGTH.** At 75 mm diameter, a
> **330–380 mm grain** is a perfectly reasonable single segment with **L/D ≈ 4.4–5.1**, which is inside the
> single-segment limit of ~6. **This is a significant finding: the club can reach optimum sorbitol grain
> length WITHOUT going to BATES.**
>
> **3. BUT THE ROADMAP STILL GOES THROUGH BATES AT 75 mm** — for a different reason. At 75 mm a single
> 380 mm grain is **~2 kg of propellant** and a **very long flame path**, and KNSB is **particularly
> susceptible to NEGATIVE EROSIVE BURNING** at high L/D. **The port-to-throat rule (≥2 at L/D = 6, larger
> for higher L/D) starts to bind.** So the club reaches the length target, **and then splits the grain to
> manage the flow** — which is exactly what BATES is for.
>
> **4. THE INTERMEDIATE SCALES ARE THE AWKWARD ONES.** 38 mm and 54 mm grains are **too long for their
> diameter to be short, and too short to reach the optimum.** They are **transitional scales**, and the
> club should treat their Isp numbers as **transitional numbers**, not as verdicts on the design.
>
> **5. DO NOT CHASE ISP AT 38 mm AND 54 mm.** Chase **repeatability, `c*` and `C_F`.** Those are the
> competencies that transfer. **The Isp arrives at 75 mm and 94 mm, because that is where the grain gets
> long enough to keep its own propellant in the motor.**

### 4.2 LESSON TWO — Casting difficulty scales INVERSELY with size

**Source: Nakka's A-100M casting page.**

> ### 🔴 **"The LARGER the grain (or rather the mould), the EASIER it is to cast."**

**The small motor is the hard one.** This is counterintuitive and it is important.

#### 4.2.1 Why small grains are hard — the three reasons

| # | Reason | Detail |
|---|---|---|
| **1** | **The slurry will not pour** | **"The sugar propellants are quite viscous and generally do not pour well. As such, the casting process is a COMBINATION OF PRECISE POURING, HURRIED SCOOPING AND CAREFUL PACKING."** |
| **2** | 🔴 **A small batch cools faster** | **"A smaller quantity of melted propellant slurry cools more quickly, AND AS IT COOLS IT BECOMES EVEN MORE VISCOUS AND DIFFICULT TO WORK WITH."** |
| **3** | **The stuff is sticky** | **"The sticky nature of these propellants doesn't help matters much."** |

**And the resulting challenge, in the source's own words:**

> **"The challenge, therefore, becomes one of getting all the slurry into the mould and done so QUICKLY and WITHOUT MAKING A MESS of the whole thing (WHICH I HAVE DONE ENOUGH TIMES)."**

#### 4.2.2 The honest warning about practice

> ### **"After a lot of experimentation that resulted in MANY REJECTED GRAINS, I've gradually developed a process that works reasonably well. Even so, A LOT OF PRACTICE MAY BE NEEDED IN ORDER TO FINALLY GET THE 'PERFECT' GRAIN."**

**Note who is saying this.** This is the man who went on to cast **89 mm, six-segment, 6 kg M-class
grains** for the *Muon* motor. **He needed many rejected grains and a lot of practice to learn this — on
a motor larger than ours.**

> ### 🔴 **PLAN FOR REJECTED GRAINS. THEY ARE NOT FAILURES. THEY ARE THE CURRICULUM.**

#### 4.2.3 Why the slurry behaves this way — the physics

| Factor | Small mould | Large mould |
|---|---|---|
| **Surface area to volume ratio** | 🔴 **HIGH** — the mould wall is a heat sink proportional to `D·L`, while the thermal mass is proportional to `D²·L` | **LOW** — much less wall per unit of hot propellant |
| **Cooling rate** | 🔴 **Fast.** The slurry thickens **while you are still trying to pour it** | **Slow.** The slurry stays workable for minutes |
| **Working time** | 🔴 **Seconds** | **Minutes** |
| **Margin for error in the pour-and-scoop** | 🔴 **Almost none** | **Comfortable** |
| **Viscosity at the moment of transfer** | 🔴 **Rising rapidly** — you are racing a clock you cannot see | **Stable** |

> **And the compounding effect that makes it brutal at 24 mm:** the slurry **thickens as it cools**, and the
> thickening is **accelerated by contact with the cold mould wall.** So the first slurry into the mould
> chills against the wall and **blocks the passage for the slurry behind it** — which is why the reference
> says **"If the mould gets blocked with propellant, take hold of the mould, lift it, then STRIKE AGAINST
> THE TABLE A FEW TIMES, this will get the slurry flowing down into the bottom of the mould."**
>
> **At 94 mm you never do this. At 24 mm you do it on every cast.**

#### 4.2.4 🔴 THE FIVE CONTROLS THAT MAKE SMALL GRAINS CASTABLE

**Everything here is a process control, not a formulation change — so all of it is allowed and encouraged
under `Propellant_Formulations.md` §9.5.**

| # | Control | Detail | Effect |
|---|---|---|---|
| **1** | 🔴 **USE THE SURFACTANT — SLES at 0.1% of molten mass** | Molten KNSB is **normally too viscous to pour.** A tiny amount of surfactant makes it **"readily pourable, having a viscosity similar to maple syrup"**, with an **immediate viscosity drop on stirring** | ✅ **This is the single largest lever available.** It converts a scoop-and-scrape operation into a pour. **Decouples "dry propellant" from "uncastable slurry"** |
| **2** | **PREHEAT EVERYTHING** | **Coring rod preheated in an oven at 300 °F (150 °C) for 15 minutes.** Consider warming the mould and casting tube similarly | Removes the cold-wall chilling that causes the mould to block |
| **3** | 🔴 **FREEZE THE PLUNGERS** | **Plungers placed in a freezer at least one hour beforehand** — **"the propellant does not stick to a frozen surface"** | Plungers that do not stick do not pull propellant back out of the mould |
| **4** | **USE THE SLES TO BUY POURABILITY, THEN THE PLUNGERS TO DE-AIR** | Solid plunger to bottom, coring rod all the way down, hollow plunger over the rod for final packing, **holding the rod end to stop it being forced out** | **"Do not press excessively hard"** — or propellant flows past the closing pin |
| **5** | 🔴 **PRACTISE ON INERT GRAINS** | **Common table salt substituted for potassium nitrate, same 65/35 ratio.** Melting rate and slurry viscosity are **"quite similar"** to genuine propellant | ✅ **Unlimited free repetitions of the hardest skill in the programme.** `Motor_Test_Program.md` §3 |

#### 4.2.5 🔴 THE COUNTERINTUITIVE CONSEQUENCE FOR THE ROADMAP

> ### **THE SCALE-UP WILL MAKE CASTING EASIER, NOT HARDER.**
>
> **The instinct is that moving from a 24 mm grain to a 94 mm grain is a leap in difficulty. On the
> casting side, it is the opposite.** The 94 mm grain is **easier to cast successfully** than the 24 mm
> grain you are struggling with now.
>
> **What actually gets harder as you scale up:**
>
> | Gets EASIER | Gets HARDER |
> |---|---|
> | ✅ **Casting** — the slurry stays workable | 🔴 **Consequence of failure** — 6 kg of propellant vs 23 g |
> | ✅ **Throat tolerance** — ±0.05 mm on 22 mm is 0.45% | 🔴 **Structural design** — real pressure-vessel engineering |
> | ✅ **Flushing losses** — long grain keeps its propellant | 🔴 **Thermal design** — long burn, hot case |
> | ✅ **Measurement signal-to-noise** | 🔴 **BATES ignition** — end faces in stagnant flow |
> | ✅ **Handling** — you can get your fingers in | 🔴 **Regulatory and institutional burden** |
>
> **So the ladder is not "small easy → large hard." It is a series of DIFFERENT problems**, and the
> casting problem — historically the club's biggest source of rejected work — **gets smaller as you climb.**
>
> ### 🔴 **DO NOT INTERPRET STAGE 0 CASTING DIFFICULTY AS A SIGN YOU ARE NOT READY TO SCALE.**
> **It is the expected difficulty, it is documented, and the fix is repetitions on inert grains.**

---

## 5. Stage 2 — 54 mm (I/J, 1000–2500 N·s)

### 5.1 What changes fundamentally

| Dimension | Change |
|---|---|
| **This is the first scale where the CASE is a real pressure vessel** | Not a tube you bought — a vessel you must analyse, with a documented burst margin and a proof test |
| **This is the first scale where THERMAL design is mandatory** | Burn times are long enough, and the case walls thin enough, that **material strength at temperature** determines the wall thickness |
| **Grain length reaches 60–90% of the flushing optimum** | 🟡 **Delivered Isp starts approaching the modeled value** |
| **Failure is now a serious event** | 900 g of KNSB holds **~2.4 MJ** — the energy of a **1000 W heater running for 40 minutes, released in about two seconds** |

### 5.2 Skills to acquire

| Skill | Why now |
|---|---|
| **Pressure-vessel stress analysis** | Hoop stress, wall thickness, closure design, thread engagement, burst margin |
| **Thermal analysis** | **Aluminium 6061 has only ~80% of room-temperature strength at 150 °C (300 °F).** **Mild steel retains 80% of yield at 240 °C and 80% of ultimate at 380 °C** |
| **Thermal protection design** | Insulation, ablatives, or heat-sink thickness — an explicit trade against **reduced casing diameter → reduced web thickness → reduced burn duration** |
| **Nozzle material selection** | Graphite erosion rate, throat growth, `C_F` loss through the burn |
| **Hydrostatic proof testing as routine** | 1.2 × MEOP, plywood shield, documented certificate |

### 5.3 Equipment additions

| Item | Spec | INR (approx.) |
|---|---|---|
| **54 mm case stock** | Steel tube or 6061 aluminium, machined threads | **₹8,000–20,000** |
| **Nozzle — graphite + steel shell** | Turned graphite, steel retainer | **₹2,000–6,000** |
| **Thermal protection materials** | **Brown postal paper measured ~0.15 mm per layer**; **utility-grade polyester resin** (automotive body-repair type) measured ~**0.11 mm** as a single rotated coating | **₹1,500–4,000** |
| **Hydrostatic test rig** | Grease gun or hydraulic jack with gauge, fittings, plywood shield | **₹4,000–10,000** |
| **Thermocouples for case-wall measurement** | Type K, soldered to the outer wall | **₹1,500–3,000** |
| **Machining access** | Lathe time, or a club machinist | **₹5,000–15,000** |
| **Stage 2 subtotal** | | **₹22,000–58,000** |

> 💡 **A cost-saving finding from the source's own insulation test programme.** Measured performance of
> cheap materials on a **63.5 mm OD, 1.65 mm wall 6061-T6511 tube**:
>
> | Material | Thickness tested | Result |
> |---|---|---|
> | **Brown "postal paper"** | **measured average 0.15 mm per layer.** Tested at **2 layers (0.29 mm)** and **7 layers (1.0 mm)** | **Some charring of the innermost layer(s), otherwise intact** |
> | **Utility-grade polyester resin** (automotive body-repair type), **applied to the casing inside and allowed to harden fully while the casing was slowly and continuously rotated** | **measured average 0.11 mm** | ✅ **No discernible degradation other than some discolouration** |
>
> **Measured densities: paper 0.646 g/cm³; cast polyester 1.26 g/cm³.** **The 7-layer paper had LOWER
> conductivity than 2-layer — because trapped air between layers provides additional insulation.**
>
> ✅ **Conclusion: "layered paper and polyester coatings would both seem to be viable insulating materials
> for rocket motor casings."** **You do not need exotic ablatives at this scale.**

### 5.4 Risks and mitigations

| Risk | Mitigation |
|---|---|
| 🔴 **Case burst from an over-pressure event** | **Burst margin target ≤2.5 × MEOP, absolute minimum 1.5 ×.** 🔴 **Avoid "boilerplate" thick-walled cases — they store an incredible amount of energy before bursting, INCREASING the risk associated with catastrophic failure** |
| 🔴 **Case strength loss from heating** | **Determine maximum average wall temperature at burnout, then size the case to MEOP at that temperature.** Or **design the thrust profile to be regressive so MEOP occurs early while the walls are still cool** |
| **Insulation too thick** | **The downside is not mass** — insulation density is low. 🔴 **It is REDUCED CASING DIAMETER, which reduces propellant volume and, more significantly, DECREASES WEB THICKNESS, thereby reducing burn duration** |
| **PVC temptation** | 🔴 **Do not use PVC casings at this scale.** PVC **begins to soften at about 100 °C**, requires a **"knock-down" factor on wall thickness** (`t_eff = (1 − 9/22) × 3.9 = 2.3 mm` for the reference example), and **shatters** on failure |
| **Nozzle erosion spoiling the test** | **Measure throat before and after every burn.** Use graphite. Budget 5–10% area margin |
| **Cost overrun on machining** | **Design around stock material.** Minimise the number of setups |

### 5.5 Gate criteria to advance to Stage 3

```
=============================================================================
 STAGE 2 -> STAGE 3 GATE
=============================================================================
 [ ] 3 motors, overlapping thrust curves
 [ ] Delivered Isp approaching the modeled value (flushing loss reducing)
 [ ] Written stress analysis: burst margin <= 2.5 x MEOP, >= 1.5 x
 [ ] Hydrostatic proof certificate at 1.2 x MEOP for every case
 [ ] Measured case-wall temperature at burnout, or post-fire wall condition assessed
 [ ] Thermal protection design validated by test
 [ ] Nozzle erosion rate for the club's graphite over >= 5 burns
 [ ] Port-to-throat area ratio >= 2 verified AT IGNITION for every motor
 [ ] L/D at or approaching 6 (the single-segment limit)
 [ ] A written assessment: is a SINGLE long grain viable at 75 mm, or is BATES required?
 [ ] Ignition system qualified for a longer core (pyrogen assessment documented)
 [ ] Written hazard review for 75 mm, signed off
 [ ] Institutional and regulatory position confirmed for the larger scale
=============================================================================
```

---

## 6. Stage 3 — 75 mm (J/K, 3000–6000 N·s)

### 6.1 What changes fundamentally

| Dimension | Change |
|---|---|
| ✅ **Grain length reaches and exceeds the 13–15 inch flushing optimum** | **This is the scale at which the club finally gets the performance it has been paying for since Stage 0.** A single 330–380 mm grain at 75 mm diameter is **L/D ≈ 4.4–5.1** |
| 🔴 **Multi-segment BATES becomes necessary anyway** | Not for performance — **for flow management.** At L/D ≈ 5 the **port-to-throat rule (≥2 at L/D = 6, larger above) starts to bind**, and KNSB is **particularly susceptible to NEGATIVE erosive burning** |
| 🔴 **End-face ignition becomes the dominant ignition problem** | **"A BATES grain consists of stacked segments. Timely ignition of the segment ends is imperative... However, THE SEGMENT ENDS ARE PRETTY MUCH IN A REGION OF STAGNANT FLOW, and thus reliable ignition may pose a problem, REGARDLESS OF IGNITER DESIGN."** |

### 6.2 The two KNSB-specific requirements at this scale

| Requirement | Value | Evidence |
|---|---|---|
| 🔴 **Inter-segment spacing** | **10–20% of the grain diameter** | **Confirmed by motor testing varying spacing from 1.5 mm to 18.5 mm.** **Rubber O-rings work well as spacers** |
| 🔴 **End-face priming** | **A thin coat of ignition primer on the segment end faces and the core near the ends** | **Only a THIN layer on the end faces. A heavy coat DEFEATS THE PURPOSE and causes delayed ignition** |

> 🔴 **THE MOUNTAIN CURVE LIVES HERE.**
> **KNSB motors show chamber pressure and thrust curves that are "triangular" or mountain-shaped, rather
> than the flat or gently curved profile predicted by design.** KNSU and KNDX do not do this.
> **The cause: delayed ignition of the end faces of BATES grain segments.**
> **The solution requires BOTH parts: adequate spacing AND a thin primer coat.**
>
> **At 75 mm you have enough segments for this to dominate the curve, and enough instrumentation heritage
> to see it clearly and fix it.** That is why this is a stage and not a jump.

### 6.3 Skills to acquire

| Skill | Why |
|---|---|
| **BATES stack design** | Segment count, spacing, total `A_b(t)`, `Kn` progression |
| **Inhibitor bonding on multiple segments** | More bonds, more places for a defect. **The tap test earns its keep here** |
| **Pyrogen assessment** | For larger motors (**K-class and larger**), **a pyrogen ignition system provides superior motor starts.** A pyrogen is **essentially a small rocket motor mounted at the bulkhead** |
| **Casting at scale** | 🔴 **Which, per §4.2, is now the EASY part** |
| **Field operation** | Transport, handling, and setup of a multi-kilogram motor |

### 6.4 Equipment additions

| Item | Spec | INR (approx.) |
|---|---|---|
| **75 mm case + closures** | Steel, machined, proof-tested | **₹15,000–35,000** |
| **Graphite nozzle + steel shell** | Larger throat, longer land | **₹4,000–10,000** |
| **BATES tooling** | Segment moulds, O-ring spacers, inhibitor bonding fixtures | **₹5,000–12,000** |
| **Pyrogen hardware** (if adopted) | Bulkhead-mounted canister, nozzle, burst diaphragm **for the pyrogen only** | **₹5,000–15,000** |
| **Cast propellant per motor** | 1.5–2.5 kg | **₹2,000–5,000** |
| **Stage 3 subtotal** | | **₹31,000–77,000** |

> ⚠️ **Note the burst-diaphragm exception — and its limits.**
> **A pyrogen is ignited by a black powder charge initially held in the canister by a burst diaphragm,
> which ALSO AIDS MOTOR PRESSURISATION.** This is a documented, working use of a burst diaphragm
> **inside the pyrogen canister** — a small, well-characterised, secondary device.
>
> 🔴 **This is NOT the same as the abandoned motor-throat burst diaphragm.** Nakka tried a **thin brass
> sheet blocking the MOTOR throat** to force pressure build-up. **It did not work satisfactorily and
> CAUSED A MOTOR FAILURE on Flight C-18 in July 1980**, because **sizing the diaphragm to burst reliably
> at exactly the right pressure was not simple to achieve, at least not with narrow-throated motors.**
>
> 🔴 **CLUB RULE: NO BURST DIAPHRAGM ANYWHERE IN THE MOTOR'S OWN PRESSURE PATH.** A pyrogen canister is a
> separate engineering problem requiring its own hazard review, and it is a **Stage 3+ item**.

### 6.5 Risks and mitigations

| Risk | Mitigation |
|---|---|
| 🔴 **Mountain curve from delayed end-face ignition** | **Inter-segment spacing 10–20% of grain diameter. Thin end-face primer. Both are required** |
| 🔴 **Progressive burn from flushing coning** | **Apply the uniform burn rate model to design a REGRESSIVE thrust curve that COMPENSATES for the coning of the core, and produce a flat thrust curve.** Knight's method |
| 🔴 **Negative erosive burning** | **Port-to-throat area ratio ≥2 at L/D = 6, larger for higher L/D.** Check at ignition, not average |
| **Inhibitor disbond on a long stack** | **Tap test every segment, batch-relative, after full cure.** Reject the odd one |
| 🔴 **Large propellant mass at risk in one firing** | **150 m+ standoff. Ballasted stand. Fire cover. Two-person minimum. Full procedure** |
| **Scale of consequence** | 🔴 **3 kg of KNSB holds ~8 MJ.** **Every step needs a written procedure and a second person** |

### 6.6 Gate criteria to advance to Stage 4

```
=============================================================================
 STAGE 3 -> STAGE 4 GATE
=============================================================================
 [ ] 3 motors, overlapping thrust curves, with BATES stacks
 [ ] Inter-segment spacing effect measured experimentally and documented
 [ ] Mountain-curve behaviour eliminated or quantified and explained
 [ ] Flat or regressive thrust profile achieved by design (not by luck)
 [ ] Ignition system qualified: charge mass vs peak pressure curve documented
 [ ] Pyrogen assessed and either qualified or explicitly ruled out with reasons
 [ ] Inhibitor bond quality: 100% tap test pass rate over the last 10 segments
 [ ] Case proof-tested at 1.2 x MEOP; burst margin documented
 [ ] Thermal protection validated at full burn duration
 [ ] Full written procedure for casting, handling, transport and firing at this scale
 [ ] Written hazard review for 94 mm, signed off
 [ ] Regulatory and institutional position confirmed
=============================================================================
```

---

## 7. Stage 4 — 94 mm (K, 6000–12000 N·s)

### 7.1 What this stage is

**The competition scale.** This is the scale at which the club operates **kilograms of propellant per
motor**, and where the programme stops being an experiment and becomes an operation.

| Parameter | Value |
|---|---|
| **Motor diameter** | **94 mm** (competition constraint) |
| **Casing length** | **383 mm (Al) / 313 mm (PVC)** per competition rules |
| **Motor mass** | **~3 kg** |
| **Propellant per motor** | **3–6 kg** |
| 🔴 **Stored energy per motor** | **~8–16 MJ** |
| **Reference point** | **Nakka's largest KNSB motor: 89 mm *Muon*, M-class, six grain segments, 6 kg total propellant** |

> ⚠️ **Note the competition constraint from `config/engineering_constants.md` §8: the competition motor
> must be COMMERCIALLY MADE, from IN-SPACe-identified vendors.** The club's own 94 mm K-class motor is a
> **capability and research objective**, and its flight use is subject to the competition rules. **Confirm
> the current rules before planning a flight campaign** (`00_ADMINISTRATION/Institutional_Approvals_and_Compliance.md`).

### 7.2 What is different

| Dimension | Change |
|---|---|
| 🔴 **Regulatory** | **Prior intimation and advisory are advised for 10,000–40,960 N·s, ≥30 days ahead. IN-SPACe authorisation is NOT required below 40,960 N·s. Local administration approval is required for launches, ALWAYS.** **PESO clearance may be sought where custom/high-mass propellant is used** |
| 🔴 **Storage** | **Kilograms of propellant require a licensed/approved store.** Never a hostel room, lab, workshop, or vehicle |
| 🔴 **Handling** | **Every step needs a written procedure and a minimum of two authorised persons** |
| 🔴 **Fire load** | **Bulk water at the pad, not just at the firing point** |
| ✅ **Performance** | **Grain length well beyond the 13–15 inch optimum. Flushing losses minimal. This is where the club finally sees its design Isp** |

### 7.3 Equipment additions

| Item | Spec | INR (approx.) |
|---|---|---|
| **94 mm case + closures** | Machined steel or aluminium, proof-tested | **₹25,000–55,000** |
| **Nozzle** | Graphite + steel shell | **₹6,000–15,000** |
| **Large mould sets** | Female mould, funnel, plungers, coring rods | **₹8,000–18,000** |
| **Casting vessel, larger** | Thermostatic, no exposed elements, sized for 8 kg batches | **₹6,000–15,000** |
| **Transport and storage** | Approved store, transport cases | **₹15,000–40,000** |
| **Propellant per motor** | 3–6 kg | **₹4,000–12,000** |
| **Stage 4 subtotal** | | **₹64,000–1,55,000** |

### 7.4 Risks and mitigations

| Risk | Mitigation |
|---|---|
| 🔴 **Consequence of failure is severe** | **Maximum standoff. Hard cover. Full written procedure. Two-person minimum. Fire cover at the pad** |
| 🔴 **Regulatory non-compliance** | **Confirm thresholds and approvals BEFORE building.** Local administration approval always. Keep the records that prove compliance |
| 🔴 **Storage and transport** | **Approved store only. Documented inventory. No exceptions for convenience** |
| **Casting at scale** | ✅ **This is the EASY part now** (§4.2). **But every step needs documenting because the batch is large** |
| **Batch-to-batch `a` drift** | 🔴 **Re-measure `a` on every new raw-material lot.** `Propellant_Formulations.md` §5.1 |
| **Schedule and cost overrun** | **Stage 4 is a multi-month programme, not a build** |

---

## 8. Timeline and programme summary

### 8.1 Realistic 3-year timeline

| Year | Quarter | Milestone | Hard dependency |
|---|---|---|---|
| **1** | **Q1** | **Strand burner built and commissioned.** Inert casting practice begins | — |
| | **Q2** | 🔴 **`a` and `n` measured for the club's materials, per regime** | Strand burner |
| | **Q3** | **Motor re-designed on the measured law. Hardware built. Proof-tested.** | `a`, `n` |
| | **Q4** | 🔴 **Stage 0 complete: 3 × 24 mm motors, overlapping traces, all reports filed** | Proof test, range access |
| **2** | **Q1** | **Stage 1: 38 mm design and hardware.** Load cell built | Stage 0 gate |
| | **Q2** | **Stage 1 firing series. Scatter quantified** | Load cell calibration |
| | **Q3** | **Stage 2: 54 mm design, stress analysis, proof test** | Stage 1 gate |
| | **Q4** | **Stage 2 firing series. Thermal protection validated** | Proof test |
| **3** | **Q1** | **Stage 3: 75 mm BATES design and tooling** | Stage 2 gate |
| | **Q2** | **Stage 3 firing series. Spacing and ignition qualified** | BATES tooling |
| | **Q3** | **Stage 4: 94 mm design, hardware, proof test, approvals** | Stage 3 gate |
| | **Q4** | 🔴 **Stage 4: K-class motor demonstrated** | Everything |

> ### ⏱️ **HONEST CAVEATS ON THIS TIMELINE**
>
> | Caveat | Effect |
> |---|---|
> | **The `a`/`n` campaign is the critical path** | If it takes four months instead of two, **everything moves right by two months.** Budget for it |
> | **Casting competence is a skill, not a task** | **"Many rejected grains" and "a lot of practice"** is the documented experience. If your first three real grains are rejected, **that is on schedule** |
> | **Monsoon (Jun–Oct) is a hard stop for outdoor firing** | **Fit casting and data work into those months.** Treat firing as a Nov–May activity |
> | **Range access and permissions are outside the club's control** | **Start approval processes a full quarter before you need them** |
> | **Exams** | Two months of near-zero throughput per year. **Plan around it, not through it** |
> | **Cost is the real gate, not time** | **₹3–5 lakh to reach a K-class motor.** If funding is slower than the technical programme, the technical programme waits |

### 8.2 The critical path

```
   STRAND BURNER
        |
        v
   a, n  MEASURED          <-- THE CRITICAL PATH. Everything waits on this.
        |
        v
   MOTOR DESIGN RE-SOLVED
        |
        v
   CASE BUILT + PROOF TESTED
        |
        v
   GRAIN CAST (>= 90% density, tap test pass)
        |
        v
   PRIMED (thin, core + end faces)  +  IGNITER BUILT (5 mm span)
        |
        v
   FIRED (pressure only, >= 100 m, full remote sequence)
        |
        v
   THREE OVERLAPPING MOTORS   <-- THE GATE
        |
        v
   SCALE UP
```

> 🔴 **Two things on this diagram are almost always done last and should be done first: the strand burner
> and the grain QC.** They are unglamorous, they produce no noise, and they determine whether the noisy
> part produces knowledge or just a hole in the ground.

### 8.3 The programme in one table

| Stage | Scale | The one thing it teaches | The one thing that can kill you | The gate |
|---|---|---|---|---|
| **0** | 24 mm | **Casting and firing at all** | **Voids and over-dried grain** | 3 overlapping traces |
| **1** | 38 mm | **Process control — your scatter number** | **10× the propellant** | Scatter quantified |
| **2** | 54 mm | **Structural and thermal design** | **Case burst; strength loss at temperature** | Proof test + stress analysis |
| **3** | 75 mm | **BATES, spacing, multi-surface ignition** | **Mountain curve → over-pressure** | Flat profile by design |
| **4** | 94 mm | **Full system integration** | **Kilograms of propellant** | K-class demonstrated |

---

## 9. The five things this roadmap will get wrong if you let it

> **A closing section, because roadmaps create false confidence. These are the ways this one fails.**

| # | Failure mode | Why it happens | Countermeasure |
|---|---|---|---|
| **1** | 🔴 **The club skips to firing and never builds the strand burner** | **Firing is exciting. A pressure vessel with thermocouples in it is not** | 🔴 **No throat is finalised until `a` and `n` exist.** Make it a signed gate, not a good intention |
| **2** | 🔴 **The club chases Isp at 38 mm and 54 mm** | 108 s looks like failure next to 129 s | 🔴 **§4.1.7. Those are TRANSITIONAL scales. Chase repeatability, `c*` and `C_F`. The Isp arrives at 75 mm because that is where the grain gets long** |
| **3** | 🔴 **The club treats small-motor casting difficulty as evidence it is not ready** | *"We can't even cast a 24 mm grain, how will we ever do 94 mm?"* | 🔴 **§4.2. THE OPPOSITE IS TRUE. "The larger the grain (or rather the mould), the easier it is to cast." Practise on salt and keep going** |
| **4** | 🔴 **The club hides a CATO** | Embarrassment. Schedule pressure | 🔴 **A CATO is the most informative thing that can happen.** Photograph it, map the debris, root-cause it in writing. **A club with no CATOs has either been lucky or has not been testing** |
| **5** | 🔴 **The club scales up on enthusiasm instead of on the gate** | The gate feels bureaucratic when you have three successful motors and a big case sitting there | 🔴 **The gate is not about whether the motor worked. It is about whether you know WHY it worked.** Three motors that worked for three different reasons is not a design |

> ### **THE HONEST SUMMARY OF THIS ROADMAP**
>
> **The technical content is not the hard part.** `Motor_Design_Guide.md` gives you the equations.
> `Motor_Test_Program.md` gives you the procedures. `Ignition_System_Design.md` gives you the ignition
> system. **All of it is documented and all of it works.**
>
> **The hard part is discipline:** building the boring instrument first, casting on salt before you cast
> on propellant, firing three motors instead of one, measuring the throat before and after every burn,
> and writing the report within 24 hours when you would rather go home.
>
> **A club that does those five things will have a K-class motor. A club that does not will have a
> collection of anecdotes and a stack of burnt tubes.**

---

## 10. Cross-references

| For | See |
|---|---|
| The flushing analysis in full | `80_REFERENCE/nakka-technical-reference.md` §9 |
| Casting procedure, supplies, demoulding, grain finishing | `80_REFERENCE/nakka-technical-reference.md` §8; `Propellant_Formulations.md` |
| Inert grain recipe and fidelity evidence | `Motor_Test_Program.md` §3 |
| Strand burner design and `a`/`n` extraction | `Motor_Test_Program.md` §4 |
| Grain density QC criteria (95% / 90%) | `Motor_Test_Program.md` §7 |
| Igniter construction, primer recipe, charge sizing | `Ignition_System_Design.md` |
| Motor design equations, `Kn`, nozzle design, throat tolerance | `Motor_Design_Guide.md` |
| Case bonding, thermal insulation, measured insulation data | `80_REFERENCE/nakka-technical-reference.md` §4, §5 |
| Static test stand design and load path | `80_REFERENCE/nakka-technical-reference.md` §6 |
| Full static-test safety procedure, distances, NO-GO list | `40_SAFETY/Static_Test_Procedure.md` |
| Regulatory thresholds and institutional approvals | `00_ADMINISTRATION/Institutional_Approvals_and_Compliance.md`; `config/engineering_constants.md` §7 |

---

*UVCE Rocketry Club — `10_PROPULSION/Propulsion_Roadmap.md`. The flushing analysis, the 13–15 inch grain
length guidance, the 108 s / 124 s / 129 s specific impulse measurements, the flush rate of 1.37×, and
the casting-difficulty finding are Chuck Knight's and Richard Nakka's own, extracted in
`80_REFERENCE/nakka-technical-reference.md` §8–§9 and reproduced without adjustment. INR costs are rough
planning estimates for Bengaluru and are not quotations. This document is subordinate to
`40_SAFETY/Safety_Manual_Master.md`.*
