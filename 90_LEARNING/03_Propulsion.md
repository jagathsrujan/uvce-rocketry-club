# 03 — Propulsion Path

**Propellant, grain design, and static testing.**

| | |
|---|---|
| **Time** | Foundation 3 weeks · Working 6–10 weeks · Advanced months |
| **Prerequisites** | [`01_Start_Here.md`](<01_Start_Here.md>) **plus the safety induction** |
| **Cost** | ₹0 to learn. ~₹12,000 to build the first test capability. |
| **Workspace docs** | [`../10_PROPULSION/`](<../10_PROPULSION/Motor_Design_Guide.md>) · [`../40_SAFETY/`](<../40_SAFETY/Safety_Manual_Master.md>) |

> ## 🔴 HARD GATE — READ THIS BEFORE ANYTHING ELSE
>
> **You may not touch propellant until you have:**
> 1. Completed the safety induction and signed it
> 2. Read [`../40_SAFETY/Propellant_Handling_SOP.md`](<../40_SAFETY/Propellant_Handling_SOP.md>) **in full**
> 3. Been signed off by the Safety Officer
> 4. Worked at the sanctioned test site, never anywhere else
>
> **The Foundation tier below is entirely theory. That is deliberate.** You learn how motors work
> before you are allowed near one. Nobody finds this unreasonable after they have seen a CATO video.
>
> **Also note:** a nitrate-based propellant like KNSB is what this club works with. **Perchlorates are
> explicitly out of scope** — see [`../10_PROPULSION/Propellant_Formulations.md`](<../10_PROPULSION/Propellant_Formulations.md>) §8.4.

---

## FOUNDATION (3 weeks — theory only, no hands-on)

### Learn

1. **What a solid propellant is** — an oxidiser and a fuel, mixed and cast into a solid. Burning is
   the oxidiser giving up oxygen to the fuel, very fast.
2. **KNSB specifically** — 65% potassium nitrate / 35% sorbitol by mass. Why sorbitol rather than
   sucrose or dextrose. Full detail in
   [`../Technical_Reference_Nakka.md`](<../Technical_Reference_Nakka.md>) §1.2.
3. **Burn rate** — how fast the surface recedes, and that it depends strongly on pressure.
4. **The four things you cannot choose independently:** impulse, thrust, burn time, grain size. Pick
   two; the rest follow.
5. **Kn** — burning area ÷ throat area. This ratio sets the chamber pressure.
6. **Why grain geometry matters** — a hole down the middle (core) means the burning area *grows* as
   it burns (progressive), stays flat (neutral), or shrinks (regressive). This shapes the thrust curve.
7. **The safety physics** — that 1 kg of sugar propellant holds ~2.7 MJ, equivalent to a 1 kW heater
   running 45 minutes, released in 2–3 seconds. See
   [`../40_SAFETY/Safety_Manual_Master.md`](<../40_SAFETY/Safety_Manual_Master.md>) §1.

### Do

- **Read [`../Technical_Reference_Nakka.md`](<../Technical_Reference_Nakka.md>) Parts 1 and 4.** This
  is our consolidated reference and it is dense with the real measured data.
- **Watch a CATO video.** Several exist on YouTube. Understand what failure actually looks like.
- **Calculate, on paper, the burn time** for a given web thickness and burn rate. Trivial arithmetic,
  but do it by hand so the relationship is real to you.
- **Run the motor design calculator** at
  [`../10_PROPULSION/Motor_Design_Calculator.xlsx`](<../10_PROPULSION/Motor_Design_Calculator.xlsx>).
  Change the target impulse and watch the throat diameter move.

### Checkpoint — you can:

- [ ] State the KNSB formulation and why it was chosen over sucrose
- [ ] Explain what Kn is and what it controls
- [ ] Explain why you cannot independently choose impulse, thrust, burn time and grain size
- [ ] Say what "progressive", "neutral" and "regressive" burns mean
- [ ] Explain why the club uses freestanding grains rather than case-bonded ones
- [ ] Recite the safe firing distance rule and why distance is the primary protection

---

## WORKING (6–10 weeks)

### Learn

1. **Grain geometry in practice** — cylindrical core, BATES, star, finocyl. Trade-offs in
   manufacturing difficulty versus burn profile.
2. **Nozzle theory** — convergent/divergent (de Laval), why supersonic flow needs a diverging
   section, expansion ratio, and why the throat is the controlling feature.
3. **Chamber pressure prediction** — the equilibrium between mass generated (burning area × burn
   rate) and mass leaving (throat area).
4. **Strand burners** — how `a` and `n` are measured, and why **KNSB's mesa behaviour means a single
   power law is invalid.**
5. **Case design** — hoop stress, why casings should burst at no more than 2.5× MEOP, and why
   "boilerplate" thick casings are *more* dangerous.
6. **Ignition** — why KNSB is 4.15× harder to ignite than KNSU, and the thin primer coat that fixes it.

### Do

This is where hands-on begins, **at the sanctioned site, under supervision.**

1. **Make inert grains first.** Table salt replaces potassium nitrate, same 65/35 ratio. Melting and
   viscosity behaviour is similar, so you practise casting with no energetic risk.
   → [`../10_PROPULSION/Motor_Test_Program.md`](<../10_PROPULSION/Motor_Test_Program.md>)
2. **Build the strand burner.** This is the club's critical path — the burn-rate coefficients are the
   one blocking unknown.
3. **Measure `a` and `n`** for our actual materials across a pressure range.
4. **Cast a real grain** and run the two QC checks: density ratio and coin tap test.
5. **Static fire** an instrumented motor with pressure measurement.

### Checkpoint — you can:

- [ ] Cast an inert grain to correct dimensions with no voids
- [ ] Explain the density check and state the accept/reject thresholds
- [ ] Perform a coin tap test and interpret the result
- [ ] Explain why the strand burner exists and what it measures
- [ ] Say why a single power law is invalid for KNSB
- [ ] Run a static fire following the SOP, and fill in FORM-04 correctly

---

## ADVANCED (months)

- **Internal ballistics modelling** — code the coupled grain regression and chamber pressure in Python
- **Nozzle design** — from first principles, including two-phase flow losses
- **Scale-up** — 54 mm, 75 mm, 94 mm, with the gate criteria in
  [`../10_PROPULSION/Propulsion_Roadmap.md`](<../10_PROPULSION/Propulsion_Roadmap.md>)
- **The flushing phenomenon** — understand why short grains underperform and why the optimum sorbitol
  grain is 13–15 inches
- **Composite propellants** — only after years of experience, and only with proper facilities. Not a
  student club activity.

### Checkpoint — you can:

- [ ] Predict a motor's pressure trace and explain any discrepancy with measurement
- [ ] Design a grain for a target thrust curve
- [ ] Explain the flushing mechanism and its effect on Isp
- [ ] Teach the Foundation tier to a new member

---

## First build

**The strand burner.** It is the single highest-value piece of equipment the club can own.

| Step | Output |
|---|---|
| 1 | Design the burner (pressure vessel, strand holder, timing) |
| 2 | Fabricate it — this is mechanical work, good for a structures collaboration |
| 3 | Cast and test inert strands to prove the mechanism |
| 4 | Cast KNSB strands and measure burn rate at 3+ pressures |
| 5 | Fit `a` and `n` **per pressure regime** — not one global fit |
| 6 | Record everything in `60_TEST_DATA/` |

**Rough cost: ₹12,000 including instrumentation.** See
[`../30_AVIONICS/Electronics_BOM_and_Sourcing.md`](<../30_AVIONICS/Electronics_BOM_and_Sourcing.md>)
Tier (c).

---

## Resources

| Resource | Cost | What it is good for |
|---|---|---|
| **[Richard Nakka's Experimental Rocketry Site](https://www.nakka-rocketry.net/)** | Free | **The single best amateur solid-propulsion resource that exists.** We have 13 pages cached in [`../80_REFERENCE/nakka_source_text/`](<../80_REFERENCE/nakka_source_text/>) |
| [`../Technical_Reference_Nakka.md`](<../Technical_Reference_Nakka.md>) | Free | Our consolidated extraction — **start here rather than the raw site** |
| [James Yawn's Rocketry Site](http://www.jamesyawn.net/) | Free | Extremely practical, photo-heavy, recrystallised sugar propellant. Different method to ours but superb technique documentation |
| [Sugar Shot to Space](https://www.sugarshot.org/) | Free | Advanced sugar motors, large scale. Aspirational and educational |
| *Rocket Propulsion Elements* — Sutton & Biblarz | ~₹800 (Indian edition) | **The** propulsion textbook. Dense. Worth buying. |
| NASA SP-8039 — *Solid Rocket Motor Performance Analysis and Prediction* | Free (search the title) | The reference for internal ballistics and erosive burning |
| *Experimental Composite Propellant* — Terry McCreary | ~₹3,000 (import) | The APCP standard. **Not needed for years** — do not buy yet. |
| [`../10_PROPULSION/Motor_Design_Guide.md`](<../10_PROPULSION/Motor_Design_Guide.md>) | Free | Our own step-by-step design method |

### Safety reading (mandatory, not optional)

| Resource | Cost |
|---|---|
| [`../40_SAFETY/Safety_Manual_Master.md`](<../40_SAFETY/Safety_Manual_Master.md>) | Free |
| [`../40_SAFETY/Propellant_Handling_SOP.md`](<../40_SAFETY/Propellant_Handling_SOP.md>) | Free |
| [`../40_SAFETY/Static_Test_Procedure.md`](<../40_SAFETY/Static_Test_Procedure.md>) | Free |

### India-specific notes

| Item | Note |
|---|---|
| **Potassium nitrate** | Sold as **14-0-45 fertiliser** at farm supply stores, 98–99% pure. Sale is restricted in some jurisdictions — check locally. |
| **Sorbitol** | Readily available online (confectionery / diabetic sweetener suppliers). |
| **Regulatory** | Below 40,960 N·s combined impulse, IN-SPACe authorisation is **not** required. Below 10,000 N·s, inform local administration. See [`../00_ADMINISTRATION/Institutional_Approvals_and_Compliance.md`](<../00_ADMINISTRATION/Institutional_Approvals_and_Compliance.md>). |
| **PESO** | The district administration may seek PESO clearance or a no-objection where custom propellants are used. Be prepared for this paperwork. |
| **Storage** | Oxidisers and fuels stored **separately**, locked, labelled. See the SOP. |

---

## What NOT to do

| ❌ | Why |
|---|---|
| Touch propellant before the safety induction | Non-negotiable. This is how people get hurt. |
| Invent or "improve" a formulation | Nakka's explicit warning: even small additive changes can turn a proven design into a CATO |
| Use perchlorates | Out of scope for this club, full stop |
| Work alone | Two-person rule, always |
| Work anywhere except the sanctioned site | Never a hostel, lab, or workshop |
| Skip the density check | Below 90% of ideal density means **discard**, because voids cause unpredictable burning |
| Copy the burst diaphragm idea | It caused a documented motor failure in 1980 |
| Be the only person who knows how to do this | Teach someone else. That is club policy. |
