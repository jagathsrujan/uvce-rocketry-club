# Simulation Plan and Validation

**UVCE Rocketry Club, Bengaluru — Simulation Guide 3 of 3**

Companion documents:
[OpenRocket_Workflow.md](OpenRocket_Workflow.md) (how to use the simulator) ·
[Motor_Files.md](Motor_Files.md) (motor definitions and static-fire reduction)

**What this document is for:** turning OpenRocket output into a number you are willing to
defend in a design review and stake a launch on. It covers where the error comes from, how
to fly-test and correct the model, how to plan the off-nominal cases, how to produce the
dispersion data that range safety and the IN-SPACe technical assessment ask for, and how to
record all of it so the work is reproducible.

> **Numbers in this document are illustrative.** Where a table shows a specific apogee,
> landing distance or velocity, it is a worked *example* of the format and the reasoning —
> not a simulation result for your rocket. Every number you quote in a review must come out
> of a simulation *you* ran on the revision *you* built. Never copy an example number into
> a flight-readiness document.

---

## 1. Why simulation is not reality

A simulation is a hypothesis with units. It becomes useful when you know which inputs are
solid, which are guesses, and how much each guess moves the answer.

### 1.1 The error sources, ranked by how much they usually hurt

| # | Source | Typical size for a student rocket | Effect on apogee | Effect on landing point | How to shrink it |
|---|---|---|---|---|---|
| 1 | **Mass estimation** (unweighed paint, glue, fillets, hardware, avionics, cord, wadding) | **+10 % to +30 % under-estimate** | **Large — see §1.2** | Large (drives chute descent rate and drift) | **Weigh every part.** Override every mass. Re-weigh the finished rocket |
| 2 | **Drag coefficient (Cd)** uncertainty | ±20 % to ±30 % | Moderate — typically 5–15 % | Moderate | Correct against a measured apogee (§2); improve surface finish; model protuberances |
| 3 | **Motor thrust curve variability** (grain density, core diameter, Kn, temperature, nozzle erosion) | ±5 % to ±10 % on thrust; ±3–8 % on total impulse | Moderate (5–10 %) | Small | Use measured curves; re-fire; make ±10 % variants |
| 4 | **Wind** (speed, direction, gusts, wind aloft) | Unknown until you measure: 0–8 m/s surface, 1.3–2× that at 150 m | −5 % to −25 % in wind | **Dominant** — controls drift during descent | Anemometer at the field; wind sweeps; fly at dawn |
| 5 | **Launch angle and rail tip-off** | 1–3° typical; up to 5° | Small in calm; large in wind | Moderate to large (a 2° tilt is metres of offset, amplified by weathercocking) | Careful setup, a plumb line or digital level, a long rail |
| 6 | **Rail friction and rail exit state** | Not modelled at all | Small | Small in calm, large in wind | Long rail, clean rail, adequate rail exit velocity |
| 7 | **Atmosphere** (site altitude, temperature, pressure) | 900 m ASL in Bengaluru, 10–15 % density reduction vs sea level | 8–15 % if ignored | Small | Enter the real launch altitude, temperature and pressure |
| 8 | **Recovery device Cd, inflation and oscillation** | Chute Cd quoted as 0.75–0.9, real effective values 0.7–1.0 | None (descent only) | Moderate to large | Measure the descent rate from your own altimeter (§2.4) |
| 9 | **Altimeter / measurement error** | Barometric ±1–3 % of apogee; clipping at low sample rates | — | — | Same reference pressure for pad and log; record the pad pressure; use a fast logger |
| 10 | **Unmodelled physics**: ignition transient, thrust misalignment, fin misalignment, spin, rain, surface degradation, internal pressure | Small individually, occasionally large | ±5 % | Moderate | Build straight, align the fins, check the nozzle concentricity |

### 1.2 The mass-squared rule (why source #1 dominates)

In the drag-free limit:

```
h ≈ I_total² / (2 · g · m²)          so          h ∝ 1 / m²

+10 % mass  →  h × (1/1.10)² = 0.83  →  apogee 17 % LOW
-10 % mass  →  h × (1/0.90)² = 1.23  →  apogee 23 % HIGH
```

Drag softens the exponent (the real dependence is closer to `1/m^1.2`–`1/m^1.6` in the
speed range of our Stage 1 rockets), but the direction and the order of magnitude are
right: **mass errors are amplified, not damped.** That is why the club spends money on
scales before it spends money on altimeters, and why "override mass with the weighed value"
is the single most important habit in this guide set.

### 1.3 A simple error budget you can fill in

Do this once per design, on paper. It converts "the simulation says 168 m" into
"168 m, and I believe 140–200 m."

| Input | Nominal | Uncertainty | Apogee sensitivity | Apogee uncertainty |
|---|---|---|---|---|
| Liftoff mass | 299 g | ±5 % (weighed) | ∝ m^−1.4 approx. | ±7 % |
| Cd (corrected) | 0.55 | ±15 % | 10 % Cd ≈ 4 % apogee | ±6 % |
| Total impulse | 24.6 N·s | ±5 % | ∝ I^1.5 approx. | ±7 % |
| Site density altitude | 900 m, 28 °C | ±2 % | ±1 % | ±1 % |
| Wind (design case) | 3 m/s | ±1.5 m/s | ±3 % | ±3 % |
| **Combined (root-sum-square)** | | | | **±12 %** |
| **Nominal apogee 168 m → report** | | | | **148–188 m** |

Combine uncertainties in **root-sum-square** (`√(a²+b²+c²…)`) for the "expected" band and
in **worst case** (plain sum) for the "do not exceed" band. Then state which one you are
using. A reviewer will accept "168 m nominal, 148–188 m expected, 140 m worst case"; a
reviewer will not accept "168 m" with no band.

### 1.4 What the simulator cannot see at all

List these explicitly in your design review, because pretending they do not exist is how
reviews fail:

- A glue joint that was starved, or a fin that is 1.5° off vertical.
- The motor's actual thrust misalignment (the nozzle throat not concentric with the case).
- A recovery system that deploys but tangles.
- A parachute packed last week versus packed in March.
- Whether the nose cone actually pops off at the charge you chose.
- A rail that is bent, dirty, or not vertical.
- The wind at 120 m when the surface is calm.
- Whether the person who pressed the button followed the checklist.

The mitigation for all of these is process (checklists, ground tests, inspections), not
software.

---

## 2. Validation methodology: simulate → fly → compare → correct

The goal is a **calibrated model**: an OpenRocket file whose apogee prediction you trust to
±10 % for your build technique. You get there in five or six flights, not one.

```
     ┌──────────────────────────────────────────────────────────────┐
     │  1. MODEL      weigh everything, override masses, measure CG │
     │  2. SIMULATE   nominal + off-nominal cases (§3, §4)          │
     │  3. FLY        altimeter + (later) GPS; log the weather      │
     │  4. COMPARE    apogee, descent rate, drift, flight time      │
     │  5. CORRECT    mass first, then drag, then the chute         │
     └───────────────────────────────┬──────────────────────────────┘
                                     └──> back to 1, with better numbers
```

### 2.1 Before the flight: model honestly

1. Weigh every component as it is built and every sub-assembly after gluing.
2. Weigh the **finished, ready-to-fly rocket with the motor installed**. This single number
   is the most valuable measurement in the whole programme.
3. Measure the **CG** by balancing the rocket (with and without the motor) and record it as
   a distance from the nose tip.
4. Override masses in OpenRocket to match the weighed values; add a nose-weight or ballast
   mass component until the simulated CG matches the measured CG to within ~5 mm.
5. Record the masses and the CG in the design log, with the date. If you change anything
   afterwards (a repaint, an added tracker), update the numbers and the revision letter.

### 2.2 During the flight: measure the things you will need

| Measurement | Instrument | Why it matters |
|---|---|---|
| Apogee (AGL) | Barometric altimeter (logging) | The primary calibration number |
| Full altitude time history | The same logger | Lets you derive the descent rate, ejection altitude and flight time |
| Descent rate under the main chute | From the log, in the stable segment | Gives the **real chute Cd** (§2.4) |
| Landing position (distance and bearing from the pad) | GPS, or a phone at the landing point, or pacing plus a compass bearing | Validates the wind model and the dispersion prediction |
| Wind speed and direction at the pad, at the time of launch | Handheld anemometer | Without this, you cannot interpret an apogee difference |
| Temperature, pressure and site altitude | Phone/weather station/altimeter | The density part of the model |
| Flight timeline (ignition, apogee beep, landing) | Stopwatch or the logger | Cross-check the simulated flight time |
| Motor: propellant mass and grain dimensions actually used | Scale and callipers | Confirms which motor revision flew |

Put the altimeter in the rocket from the **first** flight, even while you are still using
motor ejection. Try to place it near the CG so that adding it does not change the stability
much, and then use the *same position* on every flight so the correction you derive stays
valid.

### 2.3 The comparison table

Keep one row per flight. This table is the evidence for every claim in your reviews.

| Flight | Date | Rev | Motor file | Liftoff mass (g) | CG (mm from tip) | Wind (m/s / dir) | Temp (°C) | Sim apogee (m) | Measured apogee (m) | Ratio | Sim descent (m/s) | Measured descent (m/s) | Drift (m) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F-01 | 2025-02-16 | rev-A | E19KNSB 2025-03-a | 299 | 412 | 2 / 090 | 24 | 168 | 148 | 0.88 | 6.4 | 6.2 | 95 |
| F-02 | 2025-03-09 | rev-B | E19KNSB 2025-03-a | 318 | 405 | 3 / 110 | 29 | 152 | 149 | 0.98 | 6.4 | 6.2 | 120 |

A ratio column close to 1.0 in calm conditions means the model is calibrated. A ratio of
0.85 for two flights in a row means something systematic is wrong — and §2.5 is how you
find out what.

### 2.4 Correcting the parachute Cd from the descent rate

This is free, reliable data that most teams throw away. The descent rate under a parachute
is:

```
v_desc  =  √( 2 · m · g / (ρ · Cd · A) )

so, inverting it to find the effective Cd of the real chute:

Cd_eff  =  2 · m · g / ( ρ · A · v_desc² )
```

where `m` is the mass at landing (burnout mass — the propellant is gone), `ρ` the air
density at the site, and `A = π·(D/2)²` the chute's nominal area.

**Worked example.** Landing mass 298 g (318 g liftoff minus 20 g of propellant), chute
diameter 450 mm, site density 1.05 kg/m³ (900 m ASL, 28 °C), measured stable descent rate
6.2 m/s:

```
A       = π × 0.225²            = 0.159 m²
Cd_eff  = 2 × 0.298 × 9.81 / (1.05 × 0.159 × 6.2²)
        = 5.85 / (1.05 × 0.159 × 38.44)
        = 5.85 / 6.42            = 0.91
```

So the real chute behaves like Cd ≈ 0.91, not the 0.8 the model assumed. Enter **0.9** in
the parachute's configuration. Note what this does to your safety case: the *measured*
chute is better than the model assumed, so the descent is slightly slower than predicted —
a benign correction. If your measurement had come out at Cd 0.65, the model would have been
optimistic and the landing velocity would be genuinely higher: that correction matters.

Practical notes: use the mean over a stable 5–10 s segment, not the swinging peaks; a
rocket descending horizontally adds a little of its own drag, which inflates the apparent
Cd slightly; and a chute that is oscillating or partially collapsed gives a higher descent
rate than its nominal Cd implies.

### 2.5 Correcting the drag coefficient from a measured apogee

Do this **only after the masses are verified.** If you tune Cd to compensate for a mass
error, you end up with two wrong numbers that agree.

**Worked example — attributing an apogee gap correctly.**

| Step | Action | Result |
|---|---|---|
| 1 | Simulate rev-A as modelled: 299 g, Cd from the geometry model, calm | **Predicted 168 m** |
| 2 | Fly it. Altimeter reads **148 m** | Ratio 148/168 = 0.88 — a 12 % over-prediction |
| 3 | Before touching Cd, weigh the actual rocket | It is **318 g**, not 299 g. 19 g of primer, paint, fillets and cord were never entered |
| 4 | Correct the model mass to 318 g and re-run | **152 m** (mass alone explains 16 m of the 20 m gap) |
| 5 | Compare again | 148/152 = 0.97 — the drag model is already within 3 % |
| 6 | **Conclusion** | The error was mass, not drag. Apply no Cd correction (or a small one). Fix the mass budget process for the next build |

If, after the mass correction, the model still over-predicts by more than ~8 %, correct the
drag. Three ways, in order of how defensible they are in a review:

1. **Fix the surface finish** in each body component's configuration (a rougher finish
   raises friction drag). This is physically motivated: it is what the real, painted,
   slightly wavy tube actually is. It also shows a reviewer that you know where the drag
   comes from.
2. **Model the protuberances** that are missing (launch lug size, rail buttons, camera
   shroud, fin fillets).
3. **Override the drag coefficient** with a constant value found by iteration. This works
   but it is a blunt instrument: it applies the same correction at Mach 0.1 and Mach 0.8.
   If you use it, record the value as a calibration constant, state the flight(s) it was
   fitted to, and note that it is only valid for this build technique and this speed range.

Typical sensitivity in our speed range: **a 10 % increase in Cd reduces apogee by about
3–6 %.** So adjust in 5–10 % steps and re-run; two or three iterations converge.

### 2.6 How many flights before you trust the model

| Flights | What you can claim |
|---|---|
| 0 | "This is a prediction." Nothing more |
| 1 | "The model is in the right region" — one data point can hide a compensating error |
| 2–3, calm conditions, same build | "Apogee predictions are within ±10 % for this build technique" |
| 3–5 including wind | "Dispersion predictions are usable for range planning" |
| 5+ with motor re-fires | "We can size a recovery area and pick delays with confidence" |

If two consecutive flights disagree with the model in the *same* direction, stop flying that
configuration until you have found the cause. Usually it is mass, sometimes it is a motor
file with a wrong propellant mass, occasionally it is a chute Cd, and very occasionally it
is a real aerodynamic surprise that deserves a CFD or RASAero cross-check.

### 2.7 Correcting the motor file from flight data

Flight data is a weaker motor measurement than a static fire (you cannot separate thrust
from drag from an altitude log), but there is one strong signal: if the same motor design
**consistently** under- or over-performs across several rockets, re-fire it and compare the
curves. Also check:

- The propellant mass actually loaded versus the file's field 5.
- The grain dimensions versus the drawing (core diameter drift changes thrust a lot).
- The ambient/propellant temperature at the fire and at the launch.

Do **not** "tune" a motor file to make the apogee match. Fix the mass, fix the Cd, and only
then revisit the motor — with a new static fire, not with a fudge factor.

---

## 3. Simulating off-nominal cases

A single nominal simulation tells you what happens if everything is exactly as modelled. Off-
nominal cases tell you what happens when it is not — which is always.

### 3.1 The standard case set for Stage 1

| Case ID | What varies | Values | Why it is in the set | What to report |
|---|---|---|---|---|
| `NOM` | Nothing | Nominal mass, nominal motor, calm, vertical, 2 m rail | The reference | Apogee, all key velocities |
| `M-M05` | Liftoff mass −5 % | Build tolerance, forgotten paint in reverse (an over-weight model) | Lightest plausible rocket → highest apogee, highest landing energy | Max apogee case |
| `M+P05` | Liftoff mass +5 % | Extra epoxy, a heavier chute, a wet day | Heaviest plausible rocket → lowest apogee and **lowest rail exit velocity** | Rail exit check |
| `T-M10` | Motor thrust −10 % | Slow-burning propellant batch, cold grain | Lowest thrust → worst rail exit | Rail exit and T/W check |
| `T+P10` | Motor thrust +10 % | Fast batch, warm grain | Highest thrust → highest acceleration and dynamic pressure | Structural and fin-flutter check |
| `W-03` | Wind 3 m/s, 8 directions | 0/45/…/315° | The design wind; establishes the drift pattern | Landing distance vs direction |
| `W-05` | Wind 5 m/s, 8 directions | As above | Elevated but flyable at some sites | Wind limit evidence |
| `W-08` | Wind 8 m/s, 8 directions | Worst case considered | Proves the case for standing down | "Do not fly above X m/s" |
| `A-02` | Launch tilt ±2°, several azimuths | Rod/rail setup error | Realistic setup error | Flight-path and landing offset |
| `A-05` | Launch tilt ±5° | Bad setup, or deliberate upwind tilt | The range-safety case | Maximum lateral excursion |
| `CG-M10` | CG 10 mm aft | Avionics moved, heavier motor, missing nose weight | **Minimum static margin** | Stability margin never below 1.0 cal |
| `CG+P10` | CG 10 mm forward | Extra nose weight, lighter motor | Maximum static margin | Weathercocking check (keep < 2.5 cal) |
| `RAIL-10` | Rail 1.0 m instead of 2.0 m | The launcher you actually have | Worst rail exit | Go/no-go on the rail |
| `CHUTE-LO` | Chute Cd 0.7 | A tangled or partially inflated chute | Highest landing velocity | Airframe survival |
| `D+P2` | Delay 2 s longer than optimum | Grain burn-rate scatter | Deployment velocity | "Never fly this delay" evidence |

Fifteen to twenty cases is a **complete** Stage 1 set. Batch simulation makes most of them
one button press; the rest are separate simulations on separate configurations.

### 3.2 How to set each one up in OpenRocket

- **Mass ±5 %.** Batch simulation often exposes "rocket mass" (or "mass") as a swept
  parameter — use it, sweeping from 0.95× to 1.05× of your weighed liftoff mass. If your
  version does not expose it, create configurations `M-M05` and `M+P05` with an extra mass
  component of ±5 % placed at the CG, and simulate each.
- **Thrust ±10 %.** Create two motor file variants by multiplying every thrust value by
  0.9 and 1.1 while **keeping the propellant mass the same**. That is the physically correct
  model of a burn-rate change: total impulse scales by 1.1 and burn time shortens by 1/1.1.
  (If instead you scale the thrust and stretch the time to keep the impulse, you are modelling
  a *different grain geometry*, which is a legitimate study but a different one — label it
  as such.) Save them as `E19KNSB-t90.eng` and `E19KNSB-t110.eng` with their own register
  rows, and never mix them up with the measured file.
- **Wind.** Batch simulation with wind speed and wind direction as the swept parameters is
  the fastest route. Sweep direction in 15° or 45° steps at each speed.
- **Launch angle.** Batch sweep "launch rod angle" if available (0 to 5°), and run separate
  batches with different launch directions (azimuth) to cover tilt directions relative to
  the wind.
- **CG shift.** Physically, CG shifts come from moving mass. Either move the avionics mass
  component's axial offset, or add a small ballast mass component at the nose or the aft end
  and re-run. Then read the static margin from the design view and the stability plot.
- **Rail length.** Batch parameter "launch rod length". Report the rail exit velocity for
  each option.
- **Chute Cd.** Change the parachute's Cd and re-run; this only affects the descent and the
  landing point, so it is cheap.
- **Delay.** In the simulation's motor/stage settings, override the ejection delay (checkbox
  plus a value in most versions) and create one simulation per delay case.

### 3.3 Reading the off-nominal results

Report a **worst-case table**, not a wall of numbers:

| Quantity | Nominal | Min over all cases | Max over all cases | Case that produced the extreme | Limit | Verdict |
|---|---|---|---|---|---|---|
| Apogee (m) | 168 | 140 | 190 | `M-M05` light + `T+P10` | 200 for this field | Pass |
| Static margin at launch (cal) | 1.60 | 1.25 | 2.20 | `CG-M10` / `CG+P10` | 1.0–2.5 | Pass |
| Rail exit velocity (m/s) | 14.7 | 13.2 | 16.1 | `T-M10`, `M+P05` | ≥ 12 (wind limit 3 m/s) | Pass, wind-limited |
| Max acceleration (g) | 6.9 | 6.2 | 7.6 | `T+P10` | 15 (airframe) | Pass |
| Max Mach | 0.23 | — | 0.25 | `M-M05` | 0.5 | Pass |
| Deployment velocity (m/s) | 0.4 | 0.4 | 24 at `D+P2` | Delay +2 s | < 20 | **Fail — do not fly a long delay** |
| Landing velocity (m/s) | 6.3 | 6.0 | 7.1 | `CHUTE-LO` | < 8 | Pass |
| Landing distance (m) | 0 (calm) | — | 135 | `W-05` worst azimuth | Field radius 250 m | Pass with margin |

(These figures are illustrative — see the note at the top of the document.)

The right-hand columns are what make the table useful: a number without a limit and a
verdict is decoration.

---

## 4. Dispersion analysis

**Dispersion** is the spread of probable landing points (and apogees) across a family of
nearly identical flights. It is not a failure analysis — a parachute that never opens is a
hazard, not a dispersion — and it is not a substitute for a big field. It is how you decide
how big the field needs to be, where to stand, and what to tell a reviewer.

**Who needs it:**

- **Range safety.** You must know where the rocket can come down, including the tails of the
  distribution, before you light it. The recovery team and any spectators must be outside
  that area, and the area must be inside the site boundary.
- **The IN-SPACe technical assessment.** The proforma for launch authorisation asks for the
  expected flight envelope — maximum altitude, the landing/impact area and the safety
  margins for the proposed site. Dispersion analysis is the quantitative basis for those
  answers. (Requirements are updated from time to time; check the current proforma and the
  launch range's own documentation rather than relying on a second-hand summary.)
- **Site choice.** A 200 m apogee with a 5 m/s wind at altitude can land 150 m downwind.
  Whether that is acceptable depends entirely on the site.

### 4.1 Method A — batch wind sweep (works in every version)

The fastest useful dispersion estimate, and the one to do first:

1. Create one batch simulation with **wind direction swept 0–360° in 15° steps** (24 runs)
   at your design wind speed, everything else nominal.
2. Add a second batch at the maximum considered wind speed.
3. Record, for each run: **landing distance** from the pad and **landing direction**
   (azimuth), plus apogee.
4. Plot the landing points in a spreadsheet: `x = distance × sin(azimuth)`,
   `y = distance × cos(azimuth)` with an appropriate compass convention (write yours down,
   and stay consistent).
5. The result is a closed curve, roughly a circle whose centre is offset **downwind** of the
   pad. Its largest radius from the pad is your **maximum expected landing distance** for
   that wind speed.

To fold in mass and thrust scatter, repeat the sweep for the extreme mass and thrust cases
and keep the largest radius of all of them.

### 4.2 Method B — Monte Carlo (OpenRocket 22.02 and later)

OpenRocket's Monte Carlo simulation draws each parameter from a distribution you specify
(batch/multi-run dialog: mean and standard deviation per parameter) and runs many flights.

Suggested distributions for Stage 1, justified from the sections above:

| Parameter | Distribution | Standard deviation | Justification |
|---|---|---|---|
| Liftoff mass | Normal | ±2 % | We weigh the rocket; the residual is finishing mass |
| Motor total impulse | Normal | ±5 % | Batch-to-batch propellant variation |
| Thrust (burn rate) | Normal | ±8 % | Grain and temperature sensitivity |
| Cd | Normal | ±15 % | Corrected against flights, but still uncertain |
| Wind speed | Normal | ±30 % of the mean (min 1 m/s) | Gusts plus measurement error |
| Wind direction | Normal | ±20° | Shifts during the flight |
| Launch angle | Normal | ±1.5° | Setup error |
| Launch direction | Uniform | 0–360° | You will not control which way the wind blows |
| Chute Cd | Normal | ±10 % | Packing and inflation variability |

Run **500–1000 flights** if your machine tolerates it; 200 is the practical minimum for a
stable ellipse. Then:

- Plot landing points as a scatter plot (export the data and use a spreadsheet or Python).
- Compute the mean position and the covariance, then draw the **2σ ellipse** (about 95 % of
  landings) and the **3σ ellipse** (about 99.7 %) — see §4.4 for the arithmetic.
- Report the **maximum distance from the pad** in the 3σ set as the planning radius, and
  state clearly that gross failures (no deployment) are excluded and handled separately
  (§4.5).

Keep the random seed or the run count with the results: a Monte Carlo result you cannot
reproduce is an anecdote with error bars.

### 4.3 Method C — a spreadsheet-only approximation

If you have nothing but batch simulation and a spreadsheet:

1. Assume the landing distance `R` is approximately `drift_during_descent`, i.e.
   `R ≈ w · t_desc`, where `w` is the wind speed and `t_desc` the descent time from apogee:
   `t_desc ≈ h_apogee / v_desc`.
2. Take the worst credible `w_max` and the *lowest* credible `v_desc` (a tangled chute), and
   compute `R_max = w_max · h_apogee / v_desc,min`.
3. Add the boost-phase and apogee-lateral offset (from your tilt cases) and a 30–50 % margin.
4. Use `R_max × 1.5` as the planning radius if you cannot do better.

This is crude but it is conservative, it is trivially explainable, and it uses the same
physics the simulation does. It is far better than quoting a single nominal landing point.

### 4.4 The ellipse arithmetic (for the record)

With landing coordinates `(xᵢ, yᵢ)`, `n` points:

```
mean:        x̄ = Σxᵢ/n ,   ȳ = Σyᵢ/n
covariance:  Sxx = Σ(xᵢ-x̄)²/(n-1)
             Syy = Σ(yᵢ-ȳ)²/(n-1)
             Sxy = Σ(xᵢ-x̄)(yᵢ-ȳ)/(n-1)

semi-axis lengths at k standard deviations:
    a = k·√λ₁ ,  b = k·√λ₂      where λ₁,₂ are the eigenvalues of [[Sxx,Sxy],[Sxy,Syy]]
    λ₁,₂ = ((Sxx+Syy) ± √((Sxx-Syy)² + 4Sxy²)) / 2

orientation of the major axis:
    θ = ½ · atan2( 2·Sxy , Sxx - Syy )
```

Use `k = 2` for the "expected" area and `k = 3` for planning. In a spreadsheet you can skip
the eigen-decomposition entirely and simply report the **maximum distance from the pad**, the
95th percentile distance, and the mean downwind offset — reviewers care about the radius, not
the elegance.

### 4.5 What dispersion does *not* cover

- **Recovery failure.** If the chute never opens, the rocket comes in ballistic or
  tumbling. Its footprint can be larger and its impact energy is far higher. Estimate a
  separate "ballistic case" radius: the horizontal distance reached by apogee plus the drift
  while falling. As a planning number, take the **worst-case dispersion radius** and add the
  simulated horizontal distance from apogee to impact for a no-deployment case (you can
  roughly model this in OpenRocket by disabling the chute, or estimate
  `v_terminal ≈ √(2mg/(ρ·Cd·A))` with the airframe's own Cd and area, then
  `t_fall ≈ h/v_terminal`, `drift ≈ w·t_fall`).
- **Motor CATO / case burst.** Debris lands unpredictably; that is why nobody stands near the
  pad.
- **Wind shear and thermals** that the model does not represent.
- **The launch site's own obstructions** — trees, buildings, ponds, roads — which convert a
  landing point into an incident.

**Practical safety radius.** For Stage 1:
`R_safe = max( maximum expected landing distance from the dispersion study × 1.5 , 250 m )`.
Place the pad so that the entire `R_safe` circle stays inside the site, put the launch
control and any spectators at or beyond `R_safe` and upwind of the pad, and run a recovery
team that reports the landing before anyone walks out. Confirm the numbers against the site's
own rules and the current IN-SPACe requirements.

---

## 5. Wind modelling and Bengaluru conditions

### 5.1 What OpenRocket actually models

In the simulation's **Wind** settings (the exact tab name varies; it is in the same options
dialog as the launch conditions):

| Setting | What it does | How to use it |
|---|---|---|
| **Average wind speed** | A steady horizontal wind at all altitudes (newer versions can vary it with altitude) | Set the design wind; sweep it in batch runs |
| **Wind direction** | The compass direction; check your version's tooltip for "from" versus "towards" | For dispersion, sweep all 360° so the convention cannot mislead you |
| **Turbulence / standard deviation** | Adds a random gust component, so repeated runs differ | Leave at **0** for design comparisons; use 3–8 % in Monte Carlo runs where you want gust scatter |

Wind enters the physics three ways: it changes the **relative airflow** (adding drag and
causing the rocket to weathercock into the wind), it **tilts the flight path** (losing
vertical velocity and therefore apogee), and it **carries the rocket downwind** during the
long descent under parachute. For our rockets the third effect dominates the landing point
by a wide margin — see §5.4.

Things the wind model does *not* capture: wind shear layers, thermals, the reduction in wind
near the ground, and the fact that your anemometer is 2 m up while the rocket is at 150 m.

### 5.2 What to use for Bengaluru

Bengaluru is inland, ~900 m ASL, ~12.9 °N, and its wind climate is dominated by the two
monsoons and by a strong day/night cycle. Approximate planning values (surface, 10 m
reference) — **replace these with your own measurements at the field**:

| Period | Typical surface wind | Prevailing direction | Flying suitability |
|---|---|---|---|
| Dec–Feb | 1.5–3 m/s | E to NE | **Best window.** Dry, stable, calm mornings |
| Mar–May | 2–4 m/s, gusty afternoons | W to SW | Good before ~0900; afternoon convection and pre-monsoon storms |
| Jun–Sep (SW monsoon) | 4–7 m/s, stronger aloft | W to SW | Poor for our size of rocket; expect low cloud and rain breaks |
| Oct–Nov (NE monsoon) | 2–4 m/s | NE to E | Fair, but rain spells; watch the radar |

Diurnal rule of thumb: **dawn (0600–0900) is the calmest part of the day**; by early
afternoon thermals routinely double the surface wind and add gusts. If the club has one
habit to build, it is launching early.

Recommended design values for Stage 1:

| Case | Value | Use |
|---|---|---|
| Calm | 0 m/s | Reference and validation flights |
| **Design wind** | **3 m/s** | The wind the rocket must fly in while remaining inside the field |
| Elevated | 5 m/s | Still flyable if the rail exit rule is met and the field is big |
| Hard limit | 8 m/s | Not flown at our scale, at any site we currently use |

The **wind limit is set by the rail exit velocity**, not by opinion: `v_rail ≥ 4 × w`, so a
rocket leaving a 2 m rail at 14.7 m/s is limited to about 3.5 m/s. Above that, the fins are
not yet effective when the rocket meets the crosswind and the flight path is unpredictable.

**Wind aloft matters more than the surface wind.** At 100–200 m, expect roughly **1.3–2×**
the surface wind speed, and a direction that can differ by 20–40°. Rules of thumb:

- Surface 2 m/s → expect 3–4 m/s at 150 m.
- Surface 4 m/s → expect 6–8 m/s at 150 m.
- If the surface wind is above your limit, do not launch — the aloft wind is worse.
- If there is any cumulus development or a sea-breeze-like shift, expect gusts; the model
  has no way to know.

**Air density.** At 900 m ASL with a 28 °C afternoon, density is about **1.05 kg/m³**, versus
1.225 kg/m³ at sea level — about 14 % thinner. That reduces drag, so a simulation left at the
default sea-level conditions will **under-predict** apogee by roughly 8–15 %. Always enter the
site altitude (and, if you want to be careful, the temperature and pressure) in the launch
conditions. Bengaluru's typical surface pressure at ~900 m is around **905–915 hPa**; do not
guess, read it off a phone barometer or the altimeter's pad reading on the day.

### 5.3 The effect of wind on apogee

Wind always *reduces* apogee, because the rocket tilts into the wind and flies a longer,
lower path with more induced drag. Typical magnitudes for Stage 1:

| Wind (surface) | Approx. apogee loss | Notes |
|---|---|---|
| 0 m/s | 0 % | Reference |
| 2 m/s | 2–5 % | Barely noticeable |
| 3 m/s | 5–10 % | The design case |
| 5 m/s | 10–18 % | Meaningful; report it |
| 8 m/s | 15–30 % | Not flown at our scale |

An over-stable rocket loses more, because it weathercocks harder. This is the mechanism
behind the "keep the static margin under ~2 cal" rule: the extra stability buys nothing and
costs altitude, predictability and drift.

### 5.4 The effect of wind on landing point (the number that surprises people)

The rocket spends far longer descending than ascending. For a 450 mm chute on a 300 g rocket
the descent rate is about 6 m/s, so from a 160 m apogee the descent takes ~27 s. Drift is
simply:

```
drift  ≈  wind speed  ×  descent time
```

| Apogee | Descent rate | Descent time | Drift at 2 m/s | at 3 m/s | at 5 m/s | at 8 m/s |
|---|---|---|---|---|---|---|
| 160 m | 6 m/s | ~27 s | 54 m | **81 m** | 135 m | 216 m |
| 160 m | 8 m/s (small chute) | ~20 s | 40 m | 60 m | 100 m | 160 m |
| 160 m | 6 m/s, main at 100 m (dual deploy) | ~17 s | 34 m | 51 m | 85 m | 136 m |

**The landing distance is usually larger than the apogee.** A 160 m flight can land 135 m
downwind in a 5 m/s wind, and the recovery walk is longer than the rocket's height. This is
why the dispersion study, not the apogee, drives the safe area.

Levers if the drift is unacceptable:

1. **Fly earlier in the day** (the single most effective and cheapest lever).
2. **Dual deployment** (Stage 2): a drogue at apogee and the main at 100–150 m cuts the drift
   substantially, at the cost of a flight computer and more failure modes.
3. **A smaller or faster-descending main** (higher landing velocity, so check the airframe).
4. **A bigger field**, or a different site.

Do **not** "solve" drift by removing the parachute. A streamer or a tiny chute gives a
higher descent rate but the landing energy then breaks fins and electronics, and the rocket
becomes a hazard.

---

## 6. The numbers a design review needs

Every review should contain this table, filled from your own simulation output, with the
source of each number noted. OpenRocket gives you all of them; the right-hand column is
where you find them.

| # | Quantity | Where it comes from | Why the reviewer wants it |
|---|---|---|---|
| 1 | Liftoff mass (weighed) | Scale | The single most sensitive input |
| 2 | CG position (measured, mm from tip) | Balance test | Stability is CG vs CP; both must be known |
| 3 | Static margin at launch (cal) | Design view stability line / stability plot | 1.0–2.0 is the design band |
| 4 | Minimum static margin through the burn (cal) | Stability-margin plot, minimum after launch | The launch value alone can hide a mid-burn dip |
| 5 | Static margin at rail exit (cal) | Stability plot at the rail-exit time | The margin when the fins first have to work |
| 6 | Rail exit velocity (m/s) | Overview: "Launch rod velocity" | Sets the wind limit (`≥ 4 × wind`, and ≥ 15 m/s) |
| 7 | Thrust-to-weight at liftoff | `F_avg / (m·g)` — compute it | Want ≥ 5:1 |
| 8 | Nominal apogee (m AGL) | Overview | The headline number |
| 9 | Worst-case high and low apogee (m) | `M-M05`, `M+P05`, `T±10` cases | The honest apogee claim |
| 10 | Max velocity (m/s) and max Mach | Overview | Drag regime, fin flutter, chute loads |
| 11 | Max acceleration (m/s² and g) | Overview | Structural and avionics loads |
| 12 | Max dynamic pressure (Pa) | Plot/data, or `½ρv²` from max velocity | Fin flutter and structural check |
| 13 | Time to apogee (s) and flight time (s) | Overview | Recovery planning, range timing |
| 14 | Optimum delay (s) | Overview | Delay-grain selection |
| 15 | Deployment velocity (m/s) | Overview | Chute opening load; must be < 20 m/s |
| 16 | Descent rate under the main chute (m/s) | Altitude plot's slope after deployment | Landing energy |
| 17 | Landing (ground hit) velocity (m/s) | Overview | Airframe survival |
| 18 | Nominal landing distance and bearing (m) | Landing distance/direction in the results or batch output | Recovery plan |
| 19 | Worst-case landing distance (m) and direction | Dispersion study (§4) | **Range safety and the IN-SPACe assessment** |
| 20 | Planning/exclusion radius (m) | §4.5 | Site boundary and spectator placement |
| 21 | Wind limit (m/s) | From #6 and the `W-*` cases | The go/no-go rule for the day |
| 22 | Motor file revision and static-fire reference | [Motor_Files.md](Motor_Files.md) register | Reproducibility |
| 23 | OpenRocket version and design revision hash | Design log | Reproducibility |
| 24 | Assumption list and known unknowns | Your own honesty | The difference between a review and a sales pitch |

### 6.1 The one-page review summary (template)

```
DESIGN REVIEW — UVCE-S1, revision B                    Date: ____________
Prepared by: ____________     OpenRocket version: ______     Motor file: E19KNSB rev ____

VEHICLE        Length ____ mm | Max dia ____ mm | Liftoff mass (weighed) ____ g
               CG (measured) ____ mm from tip | Dry mass ____ g | Motor loaded ____ g

MOTOR          E19KNSB | Itot 24.6 N.s | Favg 19.0 N | burn 1.30 s | delay: plugged
               Static fire ref: SF-2025-03-02 | Class E

NOMINAL        Apogee ______ m | Max velocity ______ m/s | Max Mach ______
               Max acceleration ______ g | Rail exit ______ m/s | T/W ______
               Static margin launch ____ cal, min ____ cal | Optimum delay ____ s
               Deployment velocity ____ m/s | Descent rate ____ m/s
               Landing velocity ____ m/s | Flight time ____ s

OFF-NOMINAL    Apogee range ______ to ______ m
               Min rail exit (worst case) ______ m/s  -> wind limit ______ m/s
               Min static margin over all cases ______ cal
               Worst-case deployment velocity ______ m/s

DISPERSION     Design wind ____ m/s | Max landing distance ____ m | Bearing ____
               Planning radius ____ m | Site boundary distance ____ m  -> PASS/FAIL

LIMITS & GO/NO-GO   Do not fly if: surface wind > ____ m/s; mass > ____ g;
                    static margin < 1.0 cal; rail exit < ____ m/s

ASSUMPTIONS    Cd source: ______ | Mass source: weighed/estimated | Chute Cd: ______
RISKS          ______
APPROVED BY    ______
```

Fill this in for **every** revision, and keep the previous ones. The comparison between
revisions is how the club learns.

---

## 7. Simulation checklist before every design review

Print it. Tick it. A design review that skips items 4, 9 or 17 is not a design review.

**Model integrity**

- [ ] 1. The design file has a revision letter in its filename, and it is saved (not just edited).
- [ ] 2. Every component with a known measured mass has an **override mass** entered.
- [ ] 3. Mass components exist for avionics, recovery hardware, paint/glue and any ballast, each with a real or explicitly-labelled estimated mass.
- [ ] 4. **The total liftoff mass in the model equals the weighed, ready-to-fly mass** to within 2 %.
- [ ] 5. The measured CG and the simulated CG agree to within about 5 mm.
- [ ] 6. The motor file revision used is recorded, and the imported motor's mass and impulse were verified against the register.
- [ ] 7. The motor is actually selected on the motor mount, in the configuration being simulated, with the intended delay setting.
- [ ] 8. The launch altitude (site ASL), temperature and pressure match the intended launch site and time of day.

**Aerodynamics and stability**

- [ ] 9. Static margin at launch is between 1.0 and 2.0 cal; the minimum through the burn is not below 1.0 cal.
- [ ] 10. The maximum static margin is below about 2.5 cal (weathercocking).
- [ ] 11. The angle-of-attack plot shows a small, decaying angle — no growing oscillation.
- [ ] 12. Max Mach is below 0.5, or the review states that the drag model is outside its validated range.
- [ ] 13. Cd and the chute Cd are either measured/corrected, or explicitly labelled as estimates with their uncertainty.

**Performance and loads**

- [ ] 14. Rail exit velocity ≥ 4 × the design wind, and ≥ 15 m/s, in every case including the worst mass and thrust.
- [ ] 15. Liftoff thrust-to-weight ≥ 5:1.
- [ ] 16. Max acceleration and max dynamic pressure are within the airframe's and avionics' limits.
- [ ] 17. Deployment velocity is below 20 m/s in every case, including the delay and mass extremes.
- [ ] 18. Landing (ground hit) velocity is below the airframe's survival limit (target < 8 m/s).
- [ ] 19. The vertical-velocity plot crosses zero at apogee (an internal consistency check on mass and motor data).

**Off-nominal and dispersion**

- [ ] 20. Mass, thrust, wind, launch-angle, CG, rail-length, chute-Cd and delay cases have all been run (§3.1).
- [ ] 21. A worst-case table exists with limits and verdicts, not just numbers.
- [ ] 22. A dispersion study exists (batch wind sweep, Monte Carlo, or the conservative method), covering at least the design wind and the elevated-wind case.
- [ ] 23. The planning radius is stated, and the entire circle fits inside the site.
- [ ] 24. The no-deployment / ballistic case has been considered and a separate planning distance noted.
- [ ] 25. The go/no-go wind limit is stated as a single number that a pad crew can check with an anemometer.

**Documentation**

- [ ] 26. Simulation CSVs exported (per-flight data and the multi-simulation summary).
- [ ] 27. Flight-profile plots exported or captured, with readable axes, titles and case names.
- [ ] 28. The one-page review summary is filled in, with the assumption list.
- [ ] 29. Everything is in the flight/revision folder, with the motor files included.
- [ ] 30. The previous revision's numbers are available for comparison.

---

## 8. OpenRocket versus other tools, and when to move on

| Tool | Cost / platform | Strengths | Weaknesses | Use it when |
|---|---|---|---|---|
| **OpenRocket** | Free, open source, Java, Windows/macOS/Linux | Full design + 6-DOF-ish flight simulation, mass/CG bookkeeping, batch and Monte Carlo, recovery modelling, an approachable UI, a large community, easy motor import | Semi-empirical drag build-up; accuracy degrades above ~Mach 0.8; occasional rough edges in the UI; amateur-motor support is entirely up to you | **Always, at our stage.** It is the right tool from Stage 0 to Stage 2 |
| **RASAero II** | Free (Windows) | Aerodynamics validated against flight data at transonic and supersonic speeds; the reference tool for high-power/supersonic drag; good for Mach 0.8–3+ | Weaker at design ergonomics, mass bookkeeping and recovery modelling; Windows-oriented; fewer people in the club will know it | Stage 3, or any flight above ~Mach 0.8 / ~3 km where drag dominates the answer |
| **RockSim** (Apogee) | Commercial | Large certified motor database, polished UI, good high-power support, integrated motor editor | Costs money; no capability advantage over OpenRocket in our speed range | If the club has a licence and wants the motor database or the UI |
| **RocketPy** | Free, open source, Python | A proper 6-DOF model, a real wind model (profiles, ensembles), built-in Monte Carlo dispersion, reads RASP `.eng` files; used by many university teams | You must write Python; more setup; less "design a rocket" and more "analyse a flight" | Stage 2+ dispersion studies, and as an independent cross-check on OpenRocket |
| **CFD (OpenFOAM, SU2)** | Free, steep learning curve | Detailed drag and pressure distributions; fin-flutter inputs | Weeks of effort for a few percent on a subsonic rocket | Only when a specific aerodynamic question cannot be answered any other way |
| **FEA (Fusion 360, CalculiX, Ansys)** | Free to expensive | Structural margins: fin flutter, tube buckling, thrust-plate loads | Needs real material properties and real loads | Stage 3, or when a flight has failed structurally |

**When to move on, concretely:**

- Stay in OpenRocket while max Mach < 0.5 and apogee < 1 km. That covers Stages 1 and 2.
- Add **RocketPy** (or RASAero) as a cross-check when you need dispersion statistics that
  must convince an external reviewer, or when the wind profile with altitude starts to
  matter more than the surface wind.
- Move the aerodynamic answer to **RASAero II** when the flight goes transonic: OpenRocket's
  drag build-up has no reliable transonic wave-drag model, and the error there is tens of
  percent.
- Add **FEA** the first time a fin or a tube fails, not before.

**Cross-checking is cheap and it catches real errors.** Run the same design in two tools with
the same mass and motor and compare the apogee. If they disagree by more than ~15 % in the
subsonic regime, one of your models has a bad input, and finding it is worth more than either
simulation alone.

---

## 9. Recording and archiving simulation runs

Reproducibility is a habit, not a document. The rule: **any number quoted in a review must be
traceable to a file, a revision and a version number.**

### 9.1 Folder structure

```
50_SIMULATION/
├── designs/
│   ├── UVCE-S1_rev-A.ork                      # superseded, kept
│   ├── UVCE-S1_rev-B.ork                      # reviewed revision (frozen)
│   └── UVCE-S1_rev-C_work.ork                 # in progress
├── motors/                                    # motor library (see Motor_Files.md)
│   ├── E19KNSB.eng
│   ├── E19KNSB-t90.eng                        # off-nominal variants, clearly named
│   └── E19KNSB-t110.eng
├── static_fire/
│   └── SF-2025-03-02/…
├── runs/
│   └── 2025-03-09_UVCE-S1_rev-B/
│       ├── README.md                          # what was run and why
│       ├── nominal_E19_calm_summary.csv
│       ├── nominal_E19_calm_data.csv
│       ├── batch_wind_0to360_3ms_summary.csv
│       ├── montecarlo_500runs_landing.csv
│       ├── plots/
│       │   ├── nominal_altitude_vs_time.png
│       │   ├── nominal_velocity_vs_time.png
│       │   ├── nominal_accel_vs_time.png
│       │   └── nominal_stability_vs_time.png
│       └── review_summary.md                  # the one-page summary
└── flights/
    └── F-02_2025-03-09/
        ├── altimeter_log.csv
        ├── weather_notes.md
        └── comparison.md                      # sim vs measured, and the correction applied
```

### 9.2 The run log

Keep one CSV for the whole programme. It is what you hand over when a reviewer asks "how do
you know?"

| Column | Example |
|---|---|
| run_id | R-2025-03-09-004 |
| date | 2025-03-09 |
| operator | AS |
| openrocket_version | 23.09 |
| design_file | UVCE-S1_rev-B.ork |
| motor_files | E19KNSB.eng rev 2025-03-a |
| case_id | W-03-135 |
| varied_parameter | wind 3 m/s from 135° |
| mass_g | 318 |
| apogee_m | 151 |
| max_velocity_ms | 76 |
| rail_exit_ms | 14.4 |
| static_margin_launch_cal | 1.55 |
| deployment_velocity_ms | 0.6 |
| ground_hit_ms | 6.2 |
| landing_distance_m | 118 |
| landing_bearing_deg | 315 |
| purpose | design-wind dispersion sweep |
| result_files | runs/2025-03-09_…/batch_wind_0to360_3ms_summary.csv |

### 9.3 Revision discipline

- **Letter every design revision.** Save as a new file; never edit a reviewed revision.
- **Freeze the reviewed revision.** Once a review is signed off, that file and its motor
  files are read-only. Further changes create a new letter.
- **Hash or timestamp the frozen set.** A checksum of the `.ork` and the motor files (or at
  minimum the file size and modification date) makes "is this the file we reviewed?"
  answerable.
- **One README per run folder**: what was asked, what was run, what the answer was, what
  changed as a result. Five lines is enough.
- **Ship the motor files with the design.** A `.ork` does not embed custom motors, so an
  archived design without its motor file cannot be re-run.
- **Back up off one laptop.** A shared drive or a repository, plus one physical copy. A lost
  simulation history means re-deriving a year of decisions.
- **Keep the failed runs.** The run that showed the design was unstable is the most valuable
  document in the folder.

### 9.4 Per-flight archive

For every flight, keep together:

1. The flight's comparison row from §2.3.
2. The altimeter log and the reported apogee.
3. The weather at launch (wind, temperature, pressure, cloud) and the wind limit you were
   flying under.
4. The motor file revision and the propellant mass actually loaded.
5. The weighed liftoff mass and the measured CG for that flight.
6. The measured descent rate and the chute Cd you derived from it.
7. Any correction applied to the model as a result, and the new design revision it produced.

Close the loop in writing. A club that flies, measures, corrects and writes it down will beat
a club with better software every time.

---

## Appendix A — Case ID scheme

```
NOM              nominal, calm, vertical, 2 m rail
M-M05 / M+P05    liftoff mass -5 % / +5 %
T-M10 / T+P10    motor thrust -10 % / +10 % (motor file variants)
W-<speed>-<dir>  wind, e.g. W-05-135 = 5 m/s from/to 135 degrees
A-<tilt>-<dir>   launch tilt, e.g. A-05-090
CG-M10 / CG+P10  CG moved 10 mm aft / forward
RAIL-10          rail length 1.0 m
CHUTE-LO         chute Cd reduced (partial inflation case)
D+P<n>           ejection delay n seconds longer than optimum
MC-<n>           Monte Carlo run set with n flights
```
Prefix every stored result file with the case ID so a plot can never be orphaned from the
case that produced it.

## Appendix B — Formulas worth having on one page

```
Model / performance
  I_total      = Σ (t(i+1)-t(i))·(F(i+1)+F(i))/2               [N·s]
  F_avg        = I_total / t_burn                              [N]
  Isp          = I_total / (m_prop[kg] · 9.80665)               [s]
  T/W          = F_avg / (m_liftoff · g)                        [-]
  v_rail       ≈ √(2 · a · L) ,  a = (F_avg − m·g)/m            [m/s]
  Δv (upper)   ≈ I_total / m_liftoff − g·t_burn/2               [m/s]
  h (no drag)  ≈ v²/(2g) + h_burnout ,  h ∝ I²/m²               [m]
  q            = ½ · ρ · v²                                     [Pa]
  Mach         = v / a ,  a ≈ 331.3 + 0.606·T(°C)               [m/s]

Atmosphere and recovery
  ρ            ≈ P / (287.05 · T[K])                            [kg/m³]
  v_desc       = √(2·m·g / (ρ·Cd·A))                            [m/s]
  Cd_eff       = 2·m·g / (ρ·A·v_desc²)                          [-]
  drift        ≈ wind · (apogee / v_desc)                       [m]
  landing KE   = ½ · m · v_landing²                             [J]
  v_terminal   = √(2·m·g / (ρ·Cd·A))   (ballistic case)          [m/s]

Error combination
  expected     = √(a² + b² + c² + …)      (root-sum-square)
  worst case   = a + b + c + …            (plain sum)
```

## Appendix C — Unit conversions and handy values

| Imperial | SI |
|---|---|
| 1 ft = 0.3048 m | 1 m = 3.281 ft |
| 1 in = 25.4 mm | 1 mm = 0.03937 in |
| 1 oz = 28.35 g | 1 g = 0.03527 oz |
| 1 lb = 0.4536 kg | 1 kg = 2.205 lb |
| 1 lbf = 4.448 N | 1 N = 0.2248 lbf |
| 1 ft/s = 0.3048 m/s | 1 m/s = 3.281 ft/s |
| 1 psi = 6.895 kPa | 1 hPa = 1 mbar = 100 Pa |
| 1 cal (caliber) = 1 body diameter | — |

Useful references: standard gravity `g = 9.80665 m/s²`; speed of sound at 28 °C ≈ 346 m/s;
air density at 900 m ASL and 28 °C ≈ 1.05 kg/m³; Bengaluru site altitude ≈ 850–950 m ASL.
