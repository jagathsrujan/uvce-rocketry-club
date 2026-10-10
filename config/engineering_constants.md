# ENGINEERING CONSTANTS — SINGLE SOURCE OF TRUTH

> **Rule:** if a design number changes, it changes *here* and nowhere else. Design documents
> reference this file rather than hard-coding values.
>
> **Confidence key:** ✅ verified from source · 🟡 estimated, needs confirmation · ⏳ **unverified —
> do not design against this** · 🔴 blocking issue

Last updated: workspace initialisation.

---

## 1. MISSION TARGETS

| Parameter | Value | Confidence | Source / note |
|---|---|---|---|
| First flight apogee target | 200 m | — | deliberate stepping stone from 100 m |
| Second-stage apogee | 500–1000 m | — | after repeatable 200 m flights |
| Competition apogee target | 1000 m ± 100 m | ✅ | IN-SPACe rules |
| Competition payload | 1.0 kg ± 0.05 kg | ✅ | CAN-7USAT |
| Competition max total impulse | 2800 N·s | ✅ | competition rule 5.vii |
| Competition max overall length | < 1800 mm | ✅ | competition rule 5.i |
| Competition launch angle range | 80°–85°, lockable | ✅ | competition rule 5.iv |
| Competition descent rate | 2–5 m/s (±0.5) | ✅ | competition rule 7.2 |
| Competition structural loads | 15 g launch, 30 g shock | ✅ | competition rule 3.1 |
| Lift-off mass tolerance | ±5% of design value | ✅ | competition rule 5.i |

## 2. FIRST VEHICLE — PRELIMINARY CONFIGURATION

| Parameter | Value | Confidence | Note |
|---|---|---|---|
| Airframe diameter | 40 mm | 🟡 | preliminary |
| Dry mass target | 250 g | 🟡 | 40 mm / 200 m class |
| **Current mass budget total** | **306 g** | ✅ | **22.4% OVER — must cut 43.5 g** |
| Launch mass | 330 g | ✅ | dry + 24 g propellant |
| Overall length | 900 mm | 🟡 | preliminary |
| Drag coefficient (subsonic) | 0.45 | 🟡 | typical; correct from flight data |
| Required burnout velocity (200 m) | 72 m/s | ✅ | computed with quadratic drag |
| Vacuum ideal for 200 m | 62.6 m/s | ✅ | so drag costs ~15% at this scale |
| Static margin target | 1.0–2.0 calibers | ✅ | standard model rocket practice |
| Centre of pressure | **not yet computed** | ⏳ | get from OpenRocket |
| CG (from mass budget) | 457 mm from nose | ✅ | current component list |

## 3. PROPELLANT — KNSB 65/35

| Parameter | Value | Confidence | Source |
|---|---|---|---|
| Formulation | 65% KNO₃ / 35% sorbitol by mass | ✅ | Nakka |
| Ideal cast density | **1.841 g/cm³** | ✅ | Nakka (density check benchmark) |
| Elastic modulus | 5.84 GPa | ✅ | Nakka measured |
| Modulus of rupture | 7.6 N/mm² | ✅ | Nakka measured |
| Tensile strength (pristine) | 7.2 N/mm² | ✅ | Nakka measured |
| Allowable tensile stress | ≤ 20% of pristine | ✅ | Nakka design rule |
| Burn rate at 1 atm | 2.59 mm/s | ✅ | Nakka measured |
| Burn rate at 6.89 MPa | 11.25 mm/s | ✅ | Nakka measured |
| Casting temperature | 120–130 °C, ±5 °C | ✅ | Nakka |
| Decomposition onset | ~175 °C | ✅ | Nakka overheat test |
| Auto-ignition | > 300 °C | ✅ | Nakka overheat test |
| Surfactant (SLES) dose | 0.1% by mass | ✅ | Nakka |
| **Density ratio — typical good cast** | **95% of ideal** | ✅ | Nakka measured |
| **Density ratio — reject threshold** | **< 90% ⇒ DISCARD the grain** | ✅ | Nakka: risks CATO |
| Cure before demoulding | **24 hours for KNSB** | ✅ | Nakka (KNDX 30–45 min) |
| Casting temperature, KNSB | **130 °C** | ✅ | Nakka casting1 |
| Inter-segment spacing (multi-grain) | 10–20% of grain dia | ✅ | Nakka |
| Practical delivered Isp | 115–130 s | 🟡 | amateur range |
| Delivered c* | **90–95% of ideal** | ✅ | Nakka |
| Thrust coefficient Cf, good sugar nozzle | **1.6 or slightly better** | ✅ | Nakka (a plain hole ≈ 1.0) |
| Pressure sampling rate | **100 samples/s** | ✅ | Nakka (higher = noisy) |

### 🔴 Grain preparation — do not skip

| Step | Requirement | Confidence |
|---|---|---|
| **Clean off casting grease** | acetone or lacquer thinner — **mandatory** | ✅ |
| Consequence of not cleaning | delayed or failed ignition | ✅ |
| Storage, long term | zip-lock bag, then freezer — **NOT a desiccator** | ✅ |
| Why not desiccator long-term | over-drying raises burn rate above normal → **CATO risk** | ✅ |
| Desiccator use | short-term drying only; pellets must not touch grain | ✅ |

### 🔴 Burn rate law — BLOCKING

| Parameter | Value | Confidence |
|---|---|---|
| **`a` (burn-rate coefficient)** | **UNKNOWN for club materials** | 🔴 |
| **`n` (pressure exponent)** | **UNKNOWN per regime** | 🔴 |
| Interpolated 2-point placeholder | a ≈ 1.99 mm/s/MPaⁿ, n ≈ 0.30 | ⏳ **placeholder only** |
| Acceptable `n` band | 0.3–0.6 in operating regime | ✅ |
| KNSB behaviour class | **MESA propellant** | ✅ |

> 🔴 **KNSB is a mesa propellant. A single power law is INVALID across all pressures.** The `a`/`n`
> pair must be measured per pressure regime with a strand burner using the club's actual
> (as-obtained, undessicated) materials. **No throat may be finalised until this is done.**

## 4. MOTOR — FIRST DESIGN (D/E CLASS, ~24 N·s)

Computed by `10_PROPULSION/Motor_Design_Calculator.xlsx` using the **placeholder** burn-rate law.

| Parameter | Value | Confidence |
|---|---|---|
| Total impulse target | 24 N·s | ✅ from flight mechanics |
| Propellant mass | 26.7 g | ✅ |
| Grain OD | 24 mm | 🟡 |
| Core port | 7 mm | 🟡 |
| Grain length | 35.0 mm | ⏳ depends on burn law |
| Web thickness | 8.5 mm | ✅ geometry only |
| Burn rate at 3 MPa | 2.77 mm/s | 🔴 placeholder law |
| Burn time | 3.07 s | 🔴 placeholder law |
| Mass flow | 8.68 g/s | 🔴 placeholder law |
| **Throat diameter** | **1.87 mm** | 🔴 placeholder law |
| Port / throat at ignition | 14.0 | ✅ passes (≥ 2) |
| Erosive burning check | PASS | ✅ |

| Design rule | Value | Confidence |
|---|---|---|
| Casing burst pressure | ≤ 2.5 × MEOP | ✅ Nakka |
| Absolute minimum margin | 1.5 × | ✅ Nakka |
| Hydrostatic proof test | 1.2 × MEOP, with plywood shield | ✅ Nakka |
| Port / throat area ratio | ≥ 2 (more for higher L/D) | ✅ Nakka |
| Grain configuration | **freestanding**, not case-bonded | ✅ justified by material properties |

### 4.1 🔴 THE FLUSHING PHENOMENON — changes the grain design philosophy

Chuck Knight's analysis of sorbitol propellants (`knsbchar.html`) identifies a mechanism that
standard burn-rate models do not capture:

> **A "flushing" action erodes the grain surface FASTER than the burn rate.** Gas flow melts the
> sorbitol and pushes molten propellant out of the motor before it can burn.

**Consequences:**

| Symptom | Explanation |
|---|---|
| Isp far below theoretical | propellant expelled unburned — Isp is computed on *total* propellant mass |
| **Progressive** burn from a grain designed to be neutral | the core is shaped into a cone with its base at the nozzle, raising Kn faster than uniform-burn models predict |
| Motor burns slower than strand tests predict | the flush rate adds to, and is not explained by, the strand-test burn rate |

**Measured evidence:**

| Motor | Grain length | Delivered Isp |
|---|---|---|
| G | short | **108 s** |
| H | short | **108 s** |
| I | **twice as long** | **129 s** |
| "G" re-run with a 13 in chamber but a 7 in grain (6 in spacer to nozzle) | — | **124 s** (vs 108 s) |

**Key physics:** the gas does **not** affect burn rate at the top of the core or on the end faces —
those are the only surfaces showing the true sorbitol burn rate.

> 🔴 **DESIGN GUIDANCE: "the minimum length of a sorbitol grain to achieve optimum performance is on
> the order of 13"–15"."** Long slender grains beat short fat ones.

**Implication for our first motor:** the planned 35 mm (1.4 in) grain is **far below** the 13–15 in
optimum. We should therefore expect **significant flush losses and low Isp** on the small motor. That
is acceptable for a first learning motor — but it means:

1. **Do not use the small motor's measured Isp to predict the large motor's performance.** They will
   differ, and the large one will be better.
2. **Prefer longer, thinner grains** as we scale, within the constraint that a longer grain means a
   longer motor and a higher L/D requiring a larger port-to-throat ratio.
3. **A regressive burn curve is the correct design target** for a long sorbitol grain, because it
   compensates for the coning and yields an approximately flat thrust curve.

⚠️ Also note from the same analysis: **ignition spreads quickly — delayed ignition is NOT the cause**
of the anomalous curves (Nakka's KSB-002 initiator test showed little difference in curve shape).
The "knee" on the leading edge of published sorbitol curves is evidence of fast complete ignition.

## 5. IGNITION

### 5.1 The primer — gap now CLOSED ✅

| Parameter | Value | Confidence |
|---|---|---|
| **Primer formulation** | **Ignition Powder (80% KNO₃ / 20% charcoal) + 70% isopropyl alcohol**, to a thick-paint consistency | ✅ Nakka `ignexp` + `casting1` |
| Preparation | pulverise the IP granules with mortar and pestle first | ✅ |
| Application | **single THIN coat with a fine paintbrush** | ✅ |
| **Measured coat thickness** | **0.0075 in = 200 µm** | ✅ Nakka measured |
| Coverage | entire outer surface and core; **coating the core is not strictly necessary** | ✅ |
| Drying | ≥ 24 h, or ~30 min open air then desiccator | ✅ |
| Durability | will not rub off with normal handling or storage | ✅ |
| Why it works | black colour / high emissivity aids **radiant** heat transfer; KNO₃ melts 333 °C then decomposes 400 °C releasing O₂ that burns the charcoal | ✅ |
| ⚠️ No thick-coat variant exists in the source | the only thickness-linked failure is a perchlorate pyrolant > 3 mm, which **fractures on firing** | ✅ |

### 5.2 Measured igniteability ✅

| Propellant | Time to ignition (avg of 5) | Ratio vs KNSU |
|---|---|---|
| KN-Sucrose | 4.8 s | 1.00 |
| KN-Dextrose | 7.9 s | 1.64 |
| **KN-Sorbitol (KNSB), bare** | **19.9 s** | **4.15** |
| **KNSB, primed** | **5.8 s** (4.0 s excl. one outlier) | ~1.2 |

> 🔴 **Bare KNSB needs ~4× longer to ignite than KNSU.** The primer recovers nearly all of it.
> This is why the primer is **mandatory**, not optional.
>
> Mechanism: KNSU partly caramelises during casting and decomposes readily. **KNSB does not
> caramelise** and only carbonises after sustained heating.

**BATES grains are a specific ignition problem:** segment ends sit in a region of stagnant flow, so
ignition is doubtful regardless of igniter design — the primer is the fix.

### 5.3 Igniter hardware ✅

| Parameter | Value | Confidence |
|---|---|---|
| Ignition powder | 80% KNO₃ / 20% charcoal, **no sulphur** | ✅ Nakka |
| Charcoal | natural wood only, **not briquettes** | ✅ |
| Blending | rotating mixer, **3 hours per 100 g** | ✅ |
| Bridgewire span | ~5 mm | ✅ Nakka |
| Bridgewire material | nichrome (or 1–2 strands coarse steel wool / fine copper) | ✅ |
| Firing supply | 2 × 3.6 V NiMH in series (7.2 V), 300 mAh | ✅ Nakka |
| Cold performance | fired instantly after 6 h at −20 °C | ✅ |
| Igniter charge | scale to motor — ⚠ oversized = startup spike = motor failure | ✅ |
| Charge sizes tested (BEM) | 3 g / 7 g / 15 g | ✅ |
| ❌ Burst diaphragm | **caused a motor failure** (Flight C-18, Jul 1980) — do not use | ✅ |

## 6. SAFETY DISTANCES AND LIMITS

| Parameter | Value | Confidence |
|---|---|---|
| Firing distance, proven motor | 75–100 m | ✅ Nakka |
| Firing distance, new design | greater than 75–100 m | ✅ |
| Igniter leads | **shunted** until moment of connection | ✅ |
| Misfire wait before approach | several minutes | ✅ |
| Safe/Arm switch | only **partial** security — need interlocked ignition box | ✅ |
| Propellant work | never alone; dunk bucket + extinguisher + escape route present | ✅ |

## 7. REGULATORY THRESHOLDS (INDIA)

| Threshold | Value | Confidence |
|---|---|---|
| IN-SPACe authorisation NOT required below | 40,960 N·s combined impulse | ✅ IN-SPACe advisory |
| Prior intimation + advisory advised | 10,000–40,960 N·s, ≥30 days ahead | ✅ |
| Below 10,000 N·s | no authorisation; inform local administration | ✅ |
| Local administration approval | required for launches, always | ✅ |
| PESO clearance | may be sought where custom/high-mass propellant used | ✅ |
| Our first motor | ~24 N·s — far below all thresholds | ✅ |
| Competition motor | ≤ 2800 N·s — also below | ✅ |

## 8. COMPETITION CONSTRAINTS WORTH REMEMBERING

| Item | Value | Confidence |
|---|---|---|
| Motor | must be **commercially made**, from IN-SPACe-identified vendors | ✅ |
| Motor diameter | 94 mm | ✅ |
| Motor casing length | 383 mm (Al) / 313 mm (PVC) | ✅ |
| Motor mass | ~3 kg | ✅ |
| Stages | 1 only | ✅ |
| Payload bay | 15 cm dia × 40 cm height max | ✅ |
| Pyrotechnics | **PROHIBITED anywhere** in the rocket | ✅ |
| LiPo batteries | **PROHIBITED**; Li-ion must be metal-cased | ✅ |
| Backup altimeter | independent COTS, mandatory in redundant chain | ✅ |
| Telemetry rate | ≥ 1 Hz | ✅ |
| Telemetry format | ASCII comma-separated, exact field order | ✅ |
| File naming | `Flight_<TEAM_ID>.csv` | ✅ |
| Airframe colour | fluorescent pink, red or orange | ✅ |
| Team size | 5–8 members | ✅ |
| Team limit | 1 team per college | ✅ |
| Registration fee | ₹10,000, then ₹15,000 after workshop | ✅ |
| Funding from IN-SPACe | **none** | ✅ |

---

## CHANGE LOG

| Date | Change | Reason |
|---|---|---|
| init | Created | workspace setup |
| init+1 | **Density threshold corrected** from "≥0.97" to "95% typical, <90% discard" | earlier value was engineering judgement; Nakka measured 95% typical and states <90% risks CATO |
| init+1 | **Cure time corrected** to 24 h for KNSB | Nakka `casting1` is specific: KNSB must cure 24 hours, unlike KNDX at 30–45 min |
| init+1 | **Casting temperature corrected** to 130 °C for KNSB | Nakka `casting1` gives KNSB at 130 °C |
| init+1 | **Primer recipe added** — gap closed | recovered from `ignexp` + `casting1`: IP + 70% IPA, thin coat, 200 µm |
| init+1 | **Igniteability data added** — bare KNSB 4.15× harder to ignite than KNSU | measured, `ignexp` |
| init+1 | **Flushing phenomenon added** (§4.1) with 13–15 in grain guidance | `knsbchar` — affects grain design philosophy and Isp expectations |
| init+1 | **Grain cleaning requirement added** — acetone/lacquer thinner mandatory | `casting1` — grease film causes delayed/failed ignition |
| init+1 | **Storage rule added** — no long-term desiccator | over-drying raises burn rate → CATO risk |
| init+1 | Added c* (90–95% ideal), Cf (1.6), sampling rate (100 Hz) | `pressure-measurement` |

> ⚠️ **Note the pattern:** three values in the first draft of this file were engineering judgement
> that turned out to be wrong or imprecise once measured data arrived. **Prefer measured values over
> plausible-sounding ones, and mark the difference.**

> **When you change a value here, add a row to the change log and update any design document that
> referenced the old value.**
