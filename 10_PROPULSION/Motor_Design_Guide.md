# UVCE Rocketry Club — Motor Design Guide

**Document:** `10_PROPULSION/Motor_Design_Guide.md`
**Applies to:** All solid rocket motor design by UVCE Rocketry Club
**Status:** 🟡 Method is valid. **The worked example's burn-rate coefficient is NOT** — see §12.4.
**Parent references:** `Technical_Reference_Nakka.md` Parts 1, 3, 4; `Propellant_Formulations.md`

> 🔴 **READ THIS BEFORE YOU USE ANY EQUATION IN THIS DOCUMENT**
> Every equation here is only as good as its inputs. The single input you do **not** have is the
> burn-rate coefficient `a` for **your** propellant, made from **your** potassium nitrate and **your**
> sorbitol, at **your** grind setting and **your** dessication state. **You cannot design a throat
> without it.** The method below is complete; the number is missing. Build the strand burner first.

---

## 1. Design philosophy

### 1.1 You do not get to choose four things

> **You cannot independently choose impulse, thrust, burn time, and grain size. Pick two; the rest are
> determined by physics.**

This is the single most important sentence in motor design, and it is the sentence beginners ignore.
The coupling is not a guideline — it is a hard algebraic constraint. Concretely:

| If you fix | Then this is forced | Because |
|---|---|---|
| **Total impulse + propellant mass** | Burn time is free, but thrust = I/t | Definition: I = ∫F dt |
| **Total impulse + burn time** | **Mean thrust is fixed**: F̄ = I/t | Definition |
| **Impulse + geometry** | Burn time is fixed: t_b = w / r(P) | Burn time is a *geometry* property |
| **Thrust + burn time** | Propellant mass is fixed: m_p = F̄·t_b/(Isp·g₀) | Rocket equation bookkeeping |
| **Chamber pressure** | 🔴 **Throat area is fixed** by the mass balance | ṁ_in = ṁ_out |
| **Throat area + grain geometry** | 🔴 **Chamber pressure is fixed** by `Kn` | Pressure equilibrium |

**The practical trap:** you write down a target of "24 N·s, 12 N, 2 s, in a 24 mm tube." That is four
constraints on a system with two degrees of freedom. The fourth one will break, and it will break
silently — you will produce a motor whose burn time is 1.75 s instead of 2 s and wonder why. **Decide
which constraint you are relaxing *before* you cut metal.** For the club's first motor, the constraint
that is relaxed is **burn time** (§12).

### 1.2 The design equation chain — and why it is iterative

```
   ┌─────────────────────────────────────────────────────────────────────┐
   │  GRAIN GEOMETRY                                                     │
   │  bore diameter, outer diameter, length, segment count               │
   └───────────────────────────────┬─────────────────────────────────────┘
                                   │  geometry only
                                   ▼
   ┌─────────────────────────────────────────────────────────────────────┐
   │  BURNING SURFACE AREA  A_b(t)                                       │
   │  evolves as the web is consumed <- THIS IS THE HARD PART            │
   └───────────────────────────────┬─────────────────────────────────────┘
                                   │  × burn rate
                                   ▼
   ┌─────────────────────────────────────────────────────────────────────┐
   │  MASS FLOW GENERATED   ṁ_gen = A_b · ρ_p · r(P_c)                   │
   └───────────────────────────────┬─────────────────────────────────────┘
                                   │  must equal what the nozzle passes
                                   ▼
   ┌─────────────────────────────────────────────────────────────────────┐
   │  REQUIRED THROAT AREA   A_t  =  ṁ · C* / P_c                        │
   └───────────────────────────────┬─────────────────────────────────────┘
                                   │  choked-flow relation
                                   ▼
   ┌─────────────────────────────────────────────────────────────────────┐
   │  CHAMBER PRESSURE       P_c  =  ( Kn · a · ρ_p · C* )^(1/(1-n))     │
   │                          Kn   =  A_b / A_t                          │
   └───────────────────────────────┬─────────────────────────────────────┘
                                   │  burn rate depends on P_c
                                   └──────────────► BACK TO BURN RATE r(P_c)
                                                    (closes the loop)
```

**Why it cannot be solved in one pass:** `A_t` depends on `P_c`, and `P_c` depends on `A_t`. Worse,
`A_b` is not a constant — it changes continuously as the grain burns, so `P_c` changes continuously,
so `r` changes continuously, so `A_b` changes at a different rate. **You are integrating a coupled
nonlinear system.** There is no closed form for the general case.

**How you actually solve it:**

| Method | When to use |
|---|---|
| **Quasi-steady integral (recommended for the club)** | Discretise the web into 5–10 steps. At each step, compute `A_b`, solve for `P_c` from the equilibrium equation, compute `r`, and advance time by `Δt = Δw / r`. This is what §12 does, by hand, and it takes about 20 minutes. **Do it by hand at least once.** You will not understand the coupling otherwise. |
| **Spreadsheet integration** | Same algorithm, 100 steps, instantaneous. Do this once you trust the hand calculation. |
| **Purpose-built software** | Nakka's `SRM.xls` / `Motor.xls`, or open-source internal-ballistics codes. Use **after** you have a hand calculation that agrees. Software hides its assumptions. |

**The iteration count:** expect 3–6 passes. You will adjust throat diameter, then find the pressure
moved, then adjust the grain, then find `Kn` moved. Convergence is fast because the exponent
`1/(1−n)` is mild at `n ≈ 0.3` (it is 1.43), but it is never one pass.

---

## 2. Governing equations

### 2.1 Unit conventions — read this, it will save you

> 🔴 **Mixing MPa and Pa in the same calculation is the most common error in amateur motor design, and
> it produces answers that look plausible.** A factor-of-10⁶ error does not announce itself.

**Use two consistent systems, and never mix them within one equation:**

| System | Pressure | Length | Density | Force | Use for |
|---|---|---|---|---|---|
| **SI (preferred)** | **Pa** | **m** | kg/m³ | N | Everything. Use this unless you have a reason not to. |
| **Engineering-practical** | **MPa** | **mm** | g/cm³ | N | Burn-rate laws as published, and quick sanity checks |

**Conversions you will need:**

| From | To | Multiply by |
|---|---|---|
| MPa | Pa | **1 × 10⁶** |
| psi | Pa | 6.8948 × 10³ |
| mm | m | 1 × 10⁻³ |
| mm² | m² | 1 × 10⁻⁶ |
| g/cm³ | kg/m³ | **1 × 10³** |
| N/mm² (= MPa) | Pa | 1 × 10⁶ |
| bar | Pa | 1 × 10⁵ |
| atm | Pa | 1.01325 × 10⁵ |

**Worked unit sanity check.** `1.841 g/cm³ = 1841 kg/m³`. `2.59 mm/s = 0.00259 m/s`. If you multiply
`ρ_p` in kg/m³ by `r` in m/s by `A_b` in m², you get kg/s. If you accidentally use `r` in mm/s you get
a mass flow 1000× too large and a throat 31.6× too big in diameter. **Check the magnitude of every
result against a known motor.** A 24 mm motor passing 20–60 g/s is sane; 20 kg/s is not.

### 2.2 Burn rate law

$$\boxed{\;r \;=\; r_o \;+\; a\,P_c^{\,n}\;}\qquad (r_o \text{ normally taken as } 0)$$

| Symbol | Meaning | SI unit | Practical unit |
|---|---|---|---|
| `r` | Linear burn rate (regression rate of the surface) | m/s | **mm/s** |
| `r_o` | Burn-rate constant, usually 0 | m/s | mm/s |
| `a` | **Burn-rate coefficient** — empirical, material- and moisture-dependent | m/s/Paⁿ | **mm/s/MPaⁿ** |
| `n` | **Pressure exponent** — empirical, dimensionless | — | — |
| `P_c` | Absolute chamber pressure | Pa | **MPa** |

> 🔴 **`a` and `n` are empirical and CANNOT be theoretically predicted.** A given `(a, n)` pair is valid
> **only over a distinct pressure range.** For KNSB — a **mesa** propellant — a single power law is
> **invalid across all pressures**. Use the pair valid for **your motor's steady-state regime**, and
> confirm `n` lands in **0.3–0.6**.
>
> 🔴 **`a` and `n` are dimensional-analysis traps.** `a` carries the units of `P^(−n)`. If you fit `a`
> using pressure in MPa and then feed pressure in Pa into the same equation, **your answer is wrong by
> a factor of `10^(6n)`** — about 63× at `n = 0.3`, and it will not look obviously wrong. **Write the
> units of `a` down next to the value, every single time.** In this document, `a` is always quoted in
> **mm/s/MPaⁿ** and `P_c` always in **MPa**, until §2.3 converts.
>
> ⚠️ **Stability bound:** if `n ≥ 1` the motor is inherently unstable — rising pressure raises burn
> rate faster than it raises mass flow out of the nozzle. Sugar propellants keep `n < 1`, which is why
> they are usable. **Never design with an assumed `n` — measure it.** If `n ≈ 0`, combustion may be
> unstable. High `n` at low pressure means the motor **refuses to come up to pressure at all.**

### 2.3 Mass flow generated by the grain

$$\boxed{\;\dot m_{\text{gen}} \;=\; A_b\,\rho_p\,r \;=\; A_b\,\rho_p\,a\,P_c^{\,n}\;}$$

| Symbol | Meaning | SI unit |
|---|---|---|
| `ṁ_gen` | Mass generation rate at the burning surface | kg/s |
| `A_b` | **Instantaneous burning surface area** | m² |
| `ρ_p` | Propellant density (**1.841 g/cm³ = 1841 kg/m³** ideal) | kg/m³ |
| `r` | Burn rate (m/s) — **use SI here, not mm/s** | m/s |

**Written in practical units** (`A_b` in mm², `ρ_p` in g/cm³, `r` in mm/s → `ṁ` in g/s):

$$\dot m_{\text{gen}}\,[\text{g/s}] \;=\; A_b\,[\text{mm}^2]\;\times\;\rho_p\,[\text{g/cm}^3]\;\times\;r\,[\text{mm/s}]\;\times\;10^{-3}$$

Because `A_b` in mm² × `r` in mm/s gives mm³/s, and `ρ_p` in g/cm³ = 10⁻³ g/mm³. The 10⁻³ is the
mm³→cm³ conversion. **Work it once by hand and then trust it.**

### 2.4 Mass flow through the nozzle (choked)

The nozzle throat is **choked** — sonic — whenever the pressure ratio `P_c/P_a` exceeds about 1.9 for
combustion gases with `γ ≈ 1.13`. Every solid rocket motor you will ever build is choked, always.

$$\boxed{\;\dot m_{\text{out}} \;=\; \frac{P_c\,A_t}{C^*}\;}$$

| Symbol | Meaning | SI unit |
|---|---|---|
| `ṁ_out` | Mass flow through the throat | kg/s |
| `A_t` | **Throat area** (the minimum cross-section) | m² |
| `C*` | **Characteristic velocity** — a propellant property, units of velocity | m/s |

**Equivalently**, from isentropic choked-flow theory (useful for checking `C*`):

$$\dot m_{\text{out}} \;=\; \frac{P_c\,A_t}{\sqrt{R\,T_c}}\;\sqrt{\gamma\left(\frac{2}{\gamma+1}\right)^{\frac{\gamma+1}{\gamma-1}}} \qquad\Longrightarrow\qquad
C^* \;=\; \frac{\sqrt{R\,T_c}}{\sqrt{\gamma}\left(\dfrac{2}{\gamma+1}\right)^{\frac{\gamma+1}{2(\gamma-1)}}}$$

| Symbol | Meaning | Value for KNSB |
|---|---|---|
| `γ` | Ratio of specific heats of the exhaust | **≈ 1.13** (condensed-phase laden) |
| `R` | Specific gas constant of the exhaust | ≈ 230–260 J/(kg·K) |
| `T_c` | Chamber (flame) temperature | see §12.3 |
| `C*` | Characteristic velocity | **≈ 900–950 m/s** for KNSB |

> ⏳ **`C*` and `T_c` for KNSB are pending exact retrieval** from Nakka's `techsht-knsb.htm` ideal
> performance table. **Until then, `C*` is a design assumption, not a validated constant.** Substituting
> `C* = 917 m/s` with `γ = 1.13` gives `T_c ≈ 1620 K`, which is the correct order for KNSB. **The
> two-phase correction (condensed K₂CO₃ particles in the exhaust) reduces delivered `C*` below the
> ideal value — typically 2–5%.** Sizing the throat with the *ideal* `C*` makes the motor slightly
> **over**-pressurised, which is the wrong direction. **Use a 0.92–0.95 `C*` efficiency when you
> compute expected performance, and always measure `c*` from a static test.**

### 2.5 Chamber pressure equilibrium and `Kn`

Steady state requires **mass generated = mass exhausted**. Set §2.3 equal to §2.4:

$$A_b\,\rho_p\,a\,P_c^{\,n} \;=\; \frac{P_c\,A_t}{C^*}$$

Solve for `P_c`:

$$\boxed{\;P_c^{\,1-n} \;=\; \frac{A_b}{A_t}\cdot\frac{a\,\rho_p\,C^*}{\mathbf{1}}\;=\;K_n\,a\,\rho_p\,C^*\;}
\qquad\Longrightarrow\qquad
\boxed{\;P_c \;=\;\Bigl(\,K_n\,a\,\rho_p\,C^*\Bigr)^{\frac{1}{1-n}}\;}$$

where

$$\boxed{\;K_n \;=\; \frac{A_b}{A_t}\;}$$

**`Kn` (also written `K` or `Kn`) is the single most useful design number you have.** It is
dimensionless, it is pure geometry, and **it sets the chamber pressure directly** for a given
propellant:

| | Meaning |
|---|---|
| **`Kn` is the ratio of burning surface area to throat area.** | |
| For a fixed propellant, **chamber pressure is a function of `Kn` alone.** | |
| 🔴 **There is a maximum `Kn` for every case design.** Exceed it and you burst. | |
| `Kn` **changes through the burn** as `A_b(t)` evolves. | This is what makes the pressure curve non-flat. |
| **`Kn` is the knob.** Motor design is mostly the art of choosing `Kn(t)`. | |

**Practical units for `Kn`,** if you want a quick mental number: with `a` in mm/s/MPaⁿ, `ρ_p` in
g/cm³, and `C*` in m/s, the product `a·ρ_p·C*` comes out numerically clean if you keep `A_b` and `A_t`
in the **same** units (the ratio is dimensionless, so mm²/mm² is fine).

> ⚠️ **Where the simple `Kn` method breaks.** Every competent treatment includes a **discharge
> coefficient** `C_d ≈ 0.95–0.98` on the throat, because the effective throat area is slightly smaller
> than the geometric area owing to the boundary layer, and because a small fraction of the generated
> mass flow is not perfectly expelled. **Use `C_d = 0.96` in design and state that you did.** The
> effect is a `1/C_d` ≈ 4% reduction in predicted chamber pressure. Predicting pressure 4% high is
> safe; predicting it 4% low is not.

### 2.6 Thrust

$$\boxed{\;F \;=\; C_F\,P_c\,A_t\;}$$

| Symbol | Meaning | SI unit |
|---|---|---|
| `F` | Thrust | N |
| `C_F` | **Thrust coefficient** (dimensionless) | — |
| `P_c` | Chamber pressure | **Pa** |
| `A_t` | Throat area | **m²** |

**Full form of the thrust coefficient** (this is where the physics lives):

$$\boxed{\;C_F \;=\; \underbrace{\sqrt{\frac{2\gamma^2}{\gamma-1}\left(\frac{2}{\gamma+1}\right)^{\frac{\gamma+1}{\gamma-1}}\left[1-\left(\frac{P_e}{P_c}\right)^{\frac{\gamma-1}{\gamma}}\right]}}_{\text{momentum term}}
\;+\;\underbrace{\frac{A_e}{A_t}\left(\frac{P_e-P_a}{P_c}\right)}_{\text{pressure term}}\;}$$

| Symbol | Meaning |
|---|---|
| `P_e` | Exit plane static pressure |
| `P_a` | **Ambient pressure** (0.1013 MPa at sea level; decreases with altitude) |
| `A_e/A_t` | Expansion ratio `ε` |
| `γ` | Ratio of specific heats (≈ 1.13 for KNSB) |

> 🔴 **The pressure term can go NEGATIVE.** If `P_e < P_a` — an **over-expanded** nozzle — the pressure
> term subtracts thrust. This is why a nozzle optimised for sea level delivers *less* than its
> vacuum `C_F`, and why a badly under-expanded nozzle (too small `ε`) also loses. **You cannot escape
> the ambient pressure term at sea level. Design for it.**

### 2.7 Expansion ratio and area ratio

$$\boxed{\;\varepsilon \;=\; \frac{A_e}{A_t} \;=\; \frac{1}{M_e}\left[\frac{2}{\gamma+1}\left(1+\frac{\gamma-1}{2}M_e^2\right)\right]^{\frac{\gamma+1}{2(\gamma-1)}}\;}$$

$$\boxed{\;\frac{P_c}{P_e} \;=\; \left(1+\frac{\gamma-1}{2}M_e^2\right)^{\frac{\gamma}{\gamma-1}}\;}$$

These are the standard isentropic area–Mach and pressure–Mach relations. **You use them in this order:**

1. Choose the **design pressure ratio** `P_c/P_e`. **For sea-level operation, set `P_e = P_a`.**
2. Solve the second equation for `M_e` (numerically — there is no closed form).
3. Substitute `M_e` into the first equation to get `ε`.
4. Compute `D_e = D_t·√ε`.

**Solved values for `γ = 1.13`** (sufficiently accurate for KNSB design work):

| Design `P_c` (MPa) | `P_c/P_a` (sea level) | `M_e` | **Optimal `ε`** | `D_e/D_t` |
|---|---|---|---|---|
| 0.5 | 4.9 | 1.96 | **2.3** | 1.52 |
| 1.0 | 9.9 | 2.37 | **3.5** | 1.87 |
| 2.0 | 19.7 | 2.78 | **4.9** | 2.21 |
| **3.0** | **29.6** | **3.00** | **5.7** | **2.39** |
| 4.0 | 39.5 | 3.16 | **6.3** | 2.51 |
| 6.0 | 59.2 | 3.40 | **7.3** | 2.70 |
| 8.0 | 79.0 | 3.55 | **8.0** | 2.82 |

> **How to read this table.** A higher chamber pressure wants a *larger* expansion ratio. This is
> because the optimum balances `P_e = P_a`, and a higher `P_c` needs more expansion to drop that far.
> **Practical note for small motors: keep `ε` modest.** A 3 MPa motor wants `ε = 5.7`, giving
> `D_e = 2.39·D_t`. For a 2.5 mm throat that is a 6.0 mm exit — physically tiny, and a real machining
> challenge. **Slightly under-expanding (using a smaller `ε` than optimal) costs very little thrust
> and much less manufacturing pain.** See §9.4.

### 2.8 Characteristic velocity, specific impulse, total impulse

$$C^* \;=\; \frac{P_c\,A_t}{\dot m} \qquad\text{[m/s]}\qquad\text{(the definition — use this to reduce test data)}$$

$$\boxed{\;I_{sp} \;=\; \frac{F}{\dot m\,g_0} \;=\; \frac{C_F\,C^*}{g_0}\;}\qquad [\text{s}]$$

$$\boxed{\;I_{\text{tot}} \;=\; \int_0^{t_b} F\,dt \;=\; \int_0^{t_b} C_F\,P_c\,A_t\,dt\;}\qquad [\text{N·s}]$$

| Symbol | Meaning | Note |
|---|---|---|
| `g₀` | Standard gravity, **9.80665 m/s²** | Always used, even in vacuum Isp |
| `I_sp` | Specific impulse | |
| `I_tot` | Total impulse | |

**The most useful identity in the whole document:**

$$\boxed{\;I_{sp} \;=\; \frac{C_F\,C^*}{g_0}\;} \qquad\Longrightarrow\qquad I_{\text{tot}} = m_p\,g_0\,I_{sp}\ \text{(ideal)}$$

**This splits performance into two independent questions.** `C*` is a **propellant** property — you
cannot improve it by redesigning the motor (only by changing the propellant, which you are not allowed
to do). `C_F` is a **nozzle geometry** property — this is the part you control. **When your motor
under-performs, `C*` tells you the propellant burned badly; `C_F` tells you the nozzle was wrong.
Measure them separately — that is what §7 of `Motor_Test_Program.md` is for.**

### 2.9 Delivered vs theoretical

$$\boxed{\;I_{sp,\text{delivered}} \;=\; \eta_{C^*}\,\eta_{C_F}\,\frac{C_F^{\text{ideal}}C^{*\,\text{ideal}}}{g_0}\;}$$

| Loss mechanism | Typical η | Physical cause |
|---|---|---|
| **`C*` efficiency** `η_C*` | **0.90–0.96** | Incomplete combustion, two-phase (condensed K₂CO₃) flow losses, heat loss to the case, non-uniform `O/F` from poor mixing |
| **`C_F` efficiency** `η_CF` | **0.92–0.97** | Divergence loss (finite nozzle half-angle), boundary-layer friction, non-optimal `ε`, throat erosion changing `A_t` during burn |
| **Combined** | **0.83–0.93** | |

**Class numbers:**

| Propellant | Ideal `I_sp` (vacuum, frozen) | **Realistic delivered `I_sp`, amateur** |
|---|---|---|
| KNSB | ~130–140 s | **100–120 s** at 3–6 MPa in a well-made motor |
| KNSU | ~1% higher than KNSB | |
| APCP | ~180–200 s | 150–175 s |

> 🔴 **Design with the ideal, deliver the real, and report both.** A motor specified at 130 s and
> delivering 105 s is not a failure — it is a motor. A design report that quotes 130 s as the expected
> delivered number is a report nobody should sign. **Size your mission on the delivered number with a
> further 10% margin, and derive the delivered number from your own static test data, not from this
> table.**

### 2.10 Burn time — fixed by geometry alone

$$\boxed{\;t_b \;=\; \frac{w}{r}\;}\qquad\text{for constant } r$$

$$\boxed{\;t_b \;=\; \int_0^{w}\frac{dw'}{r\!\left(P_c(w')\right)}\;}\qquad\text{in general}$$

| Symbol | Meaning | Unit |
|---|---|---|
| `w` | **Web thickness** — the thickness of propellant that must be consumed to reach burnout | m (mm) |
| `r` | Burn rate **at the local chamber pressure** | m/s (mm/s) |

**For a hollow cylindrical grain:**

$$\boxed{\;w = \frac{D_{\text{OD}} - D_{\text{port}}}{2}\;}$$

> ### 🎯 **BURN TIME IS FIXED BY GEOMETRY ALONE**
>
> **This is the point most beginners miss, and it is the most useful single fact in this document.**
>
> Burn time does **not** depend on:
> - how much propellant you loaded
> - what your thrust is
> - what throat you drilled
> - what nozzle you fitted
>
> Burn time depends on **only two things**: **how thick the web is**, and **how fast it burns**.
> And burn rate is a weak function of pressure (that is the whole reason `n < 1` makes motors
> controllable).
>
> **Therefore:**
> 1. **To change burn time, change the web thickness.** Nothing else.
> 2. **A thin web = short burn = higher thrust for the same impulse.** A thick web = long burn = lower
>    thrust. **Total impulse stays roughly the same.**
> 3. **If your motor burns too fast, do not reach for the throat.** Reach for the grain.
> 4. Conversely: **your burn time is locked in the moment the coring rod diameter is chosen.** The
>    coring rod is a design decision of the same weight as the throat diameter, and it is usually made
>    casually because it is "just a mould part."

> ⚠️ **But burn time is NOT exactly fixed by geometry, because `r` depends on `P_c`, and `P_c` depends
> on `A_b` — which changes as you burn.** For a **progressive** grain, pressure rises through the burn
> and `r` with it, so the *last* of the web burns measurably faster than the first. This is why §2.10
> gives an integral and not just `w/r`. **For the club's progressive tubular grain the effect is about
> 15% — you cannot ignore it.** See §12.6.

---

## 3. Design constraints and the order to apply them

**Apply these in order. Each one bounds the next.**

| # | Constraint | Limit | Consequence if violated |
|---|---|---|---|
| **1** | **Grain outer diameter** | Set by the airframe / mission | Everything else follows from this |
| **2** | **Grain L/D** | ≤ ~6 for a single segment; use BATES above that | Excessive L/D → erosive burning risk and a fragile grain |
| **3** | **Port-to-throat area ratio** | 🔴 **≥ 2 throughout the burn, larger for higher L/D** | **Negative erosive burning** → chamber pressure falls, thrust sags, motor may not sustain |
| **4** | 🔴 **Pressure exponent `n`** | **Must be 0.3–0.6 in the steady-state regime** | `n ≥ 1`: unstable, burst. `n ≈ 0`: unstable combustion. `n` high at low `P`: motor will not light |
| **5** | **Chamber pressure `P_c`** | **2–6 MPa typical for KNSB**; keep below the case rating | Below 1 MPa: poor `C*`, incomplete combustion, ignition trouble. Above case rating: burst |
| **6** | **Case burst pressure** | 🔴 **≥ 1.5× MEOP (hard minimum); target ≤ 2.5× MEOP** | Below 1.5×: insufficient margin. Above 2.5×: **"boilerplate" motor** storing excessive energy, *increasing* risk on failure |
| **7** | **Grain stress** | **Avoid tension entirely. If unavoidable, ≤ 0.20 × F_tu = 1.44 N/mm²** | Crack → burning area multiplier → over-pressure → CATO |
| **8** | **Throat diameter manufacturing tolerance** | **±0.05 mm on a small throat, or account for the swing** | A ±0.1 mm error on a 2.5 mm throat is **±8% area = ±8% chamber pressure** |
| **9** | **Igniter free volume** | Igniter must **not plug the throat** and must **not cause a startup spike** | Throat plug → burst. Oversized igniter → startup spike → sheared retention |

### 3.1 The port-to-throat rule, quantified

KNSB is **particularly susceptible to negative erosive burning**. The mitigation is a minimum
**port-to-throat area ratio of 2** for a grain L/D of about 6, **larger for larger L/D**.

| Grain L/D | Minimum `A_port / A_t` | Note |
|---|---|---|
| ≤ 3 | **2.0** | Absolute floor |
| 4–6 | **2.5–3.0** | "Typical" grain; the reference figure of 2 applies at L/D ≈ 6, so use 3 for margin |
| 7–10 | **3.5–4.0** | Requires multi-segment (BATES) construction |
| > 10 | **Use BATES segments** | Do not build a single long grain |

> 🔴 **Check the ratio at the START of the burn, not the average.** The port is smallest at ignition
> and grows monotonically, so **`A_port/A_t` is minimum at `t = 0`.** That is the number you check.
> A design that is fine at mid-burn can be badly erosive off the pad.
>
> ⚠️ **The reference figure of 2 is for L/D = 6 with a *conventional* grain.** Note the physical
> logic: a longer port means a longer flow path, more mass flux at a given pressure, and more
> susceptibility. **Small motors with L/D ≈ 1–2 have enormous margin here and it is almost never the
> binding constraint.** Do not let this rule drive your design when your grain is short — but **do
> compute the number and put it in the report**, because at 75 mm and 94 mm it becomes binding.

---

## 4. Grain geometry options

### 4.1 The five configurations

| Configuration | `A_b` progression | Thrust curve | Pressure trace | Mfg. difficulty | Beginner? |
|---|---|---|---|---|---|
| **Hollow cylindrical (tubular)** | **Progressive** — port grows, `A_b` grows | Rising | **Rising** ("regressive-neutral-progressive" in truth, but net rising) | 🟢 **Easiest** — lathe-bored or cored | ✅ **START HERE** |
| **BATES (multi-segment tubular)** | Progressive within each segment; **combined with inter-segment gaps can be near-neutral** | Nearly flat with a rise at the end | Flatter than single tubular; needs gap tuning | 🟡 Moderate — repeats the same operation N times, plus spacing hardware | ✅ **Second step** |
| **Star** | **Neutral to slightly progressive**, depending on star geometry | **Flat** | **Flat** | 🔴 Hard — requires a shaped mandrel, and demoulding a star core is difficult with a brittle propellant | ❌ Not yet |
| **Finocyl** | Tunable — can be made strongly neutral | Designed shape | Designed shape | 🔴 **Hardest** — complex mandrel, hard to de-mould, hard to inspect | ❌ Not yet |
| **End burner** | **Neutral** — constant `A_b` = cross-section | **Flat** | **Flat** | 🟢 Easy to cast (no core) | ⚠️ **Easy to make, hard to make safe — see §4.2** |

### 4.2 The five configurations, explained

**Hollow cylindrical (tubular) — the club's baseline**

- **Geometry:** a tube of propellant. Burning surfaces are the **inner bore** (primary) and the two
  **end faces** (secondary, and they stay constant while the bore grows).
- **Progression:** `A_b` starts at `π·D_port·L + 2·(annulus area)` and grows as `D_port` increases.
  With a large web, `A_b` can **triple or quadruple** over the burn.
- **Consequence:** chamber pressure rises through the burn. **This is what makes the pressure curve
  "mountain-shaped" on top of KNSB's ignition problem** (see §11 and
  `Ignition_System_Design.md` §1). The two effects compound.
- **Why it is right for beginners:** one boring operation, one mould, one coring rod, easy to inspect
  the bore for cracks, and the mandrel pulls straight out. **Every failure mode is visible.**
- **Mitigation for the progression:** use a **large initial port** relative to the web. This flattens
  the pressure rise at the cost of lower initial pressure — which is exactly the trade you want for a
  reluctant-ignition propellant anyway.

**BATES (multi-segment tubular)**

- **Geometry:** N tubular segments, axially stacked, with **inter-segment gaps** and inhibited outer
  surfaces.
- **Progression:** each segment behaves like a tubular grain, but the **end faces of every segment
  are burning surfaces**, so the total `A_b` is higher for the same propellant mass. **By choosing the
  number of segments you choose how much end-face area you have**, which lets you *tune* the
  progression toward neutral.
- 🔴 **The KNSB-specific requirement:** **inter-segment spacing of 10–20% of the grain diameter.**
  Without it, **delayed ignition of the end faces** produces the "mountain" curve. For a 24 mm grain
  that is **2.4–4.8 mm**; for a 54 mm grain, **5.4–10.8 mm**. **Rubber O-rings work well as spacers.**
  This was confirmed by motor testing with spacings from 1.5 mm to 18.5 mm.
- **Also required:** the grain **OD must be inhibited** on every segment except the ends. See §5.
- **Why it is stage two and not stage one:** more parts, more bonds, more places for a defect. **Learn
  on one segment first.**

**Star**

- **Geometry:** a central port with radial slots, so that `A_b` **increases as the star points are
  consumed and decreases as the star tips round off** — the two effects can be balanced to give a
  genuinely flat thrust curve.
- **Why not now:** the star mandrel must be withdrawn through the star bore. KNSB is **brittle and
  chips easily** — pulling a star mandrel through a soft, pliable, freshly-cast grain will tear the
  star points, and a torn star point is a **stress raiser in a material whose tensile strength scatters
  from 436 to 1050 lb/in² with no visible flaw**. You would be manufacturing a crack and hoping.
- **Also:** star geometry is where you *most* want analysis, and analysis is where you have the least
  experience. **Do not use a star until you have 3+ repeatable tubular motors.**

**Finocyl**

- **Geometry:** a combination of fins (radial slots, usually part-length) and a cylindrical core.
- **Best performance, worst manufacturability.** Part-length fins make demoulding a two-piece mandrel
  or a dissolvable/consumable mandrel, which means either a machined split mandrel or a wax/printed
  core. Both add process variables.
- **When:** a 75 mm+ motor, after you have a machinist and a fibre/3D-printed mandrel process, and
  after strand data shows you can afford the complexity. Not before.

**End burner**

- **Geometry:** propellant burns only on the aft face. `A_b` is **constant** = the full cross-section,
  so the thrust curve is **flat and beautiful** and the pressure is constant, which is ideal for KNSB's
  ignition stubbornness.
- ⚠️ **Why it is dangerous despite being easy:** to get useful thrust from a constant small `A_b`, the
  port-to-throat rule is irrelevant but the **burn time becomes enormous** for a reasonable length —
  and worse, an end burner **burns toward the forward closure**, so any defect in the forward thermal
  protection or the case bond exposes the case directly to flame at full chamber temperature for the
  entire (long) burn. **A case-bonded end burner is exactly the configuration KNSB's mechanical
  properties forbid** (§7).
- **Verdict for the club:** ❌ **Do not use.** The club's roadmap should reach a neutral burn profile
  through **BATES gap tuning**, not through an end burner.

### 4.3 Choosing a progression — the design lever nobody uses

**Progressivity is not a fixed property of your grain — it is a knob.** The reason to care is that
**a progressive grain burns a meaningful fraction of its propellant at low pressure, where `C*` and
`C_F` are both poor, and that propellant contributes almost nothing to impulse.** You paid for it, you
cast it, you carried it, and it does not push.

**Three ways to flatten progression, in order of how much manufacturing difficulty they add:**

| Method | Effect | Cost |
|---|---|---|
| **1. Increase initial port diameter** | Reduces the *ratio* `D_OD/D_port`, which reduces the `A_b` growth ratio | **Free** — just a bigger coring rod. Costs you initial pressure and a shorter web (shorter burn). |
| **2. Multi-segment BATES** | Adds constant end-face area, offsetting bore growth | Moderate — spacing hardware, N inhibitor bonds |
| **3. Star or finocyl** | Genuinely tunable | High — mandrel manufacture, demould risk |

> **For the club's first motor: use method 1.** A port-to-OD ratio of **0.375** (9 mm port in 24 mm OD)
> is what §12 selects, and it is a deliberate choice to flatten progression. **Record why in the design
> report** — a reviewer who sees "9 mm because that was the drill we had" will not be impressed.

---

## 5. Inhibitors

### 5.1 What an inhibitor is and why you need one

**An inhibitor is a non-burning (or very slow-burning) layer that blocks a grain surface from igniting.**
You need one whenever a propellant surface would otherwise burn and you do not want it to, which is:

| Configuration | Surfaces burning | Surfaces inhibited |
|---|---|---|
| **Single tubular grain, freestanding** | Bore + both end faces | **Outer cylindrical surface only** |
| **BATES segment stack** | Bore of every segment + forward face of segment 1 + aft face of segment N | **Outer cylindrical surface of every segment**, and the **internal faces** between segments that are not separated by a gap |
| **Any grain whose ends touch a closure** | — | Any face bearing against metal |

**Why it matters more than beginners think:** if the outer cylindrical surface of a freestanding grain
burns, **`A_b` jumps by `π·D·L`** — for the club's 24 mm grain that is **2,489 mm² on top of a design
`A_b` of 954 mm²**. That is a **3.6× burning-area increase, a `Kn` increase of 3.6×, and a chamber
pressure increase of `3.6^(1/0.7) = 6.4×`.** Your case bursts. **The inhibitor is not a nicety. It is
the difference between a motor and a bomb.**

### 5.2 Materials

| Material | Form | Rating | Notes |
|---|---|---|---|
| **Casting tube / paper liner** | The tube the propellant is cast into, left in place | ✅ **Best — the club's primary method** | Grain is cast directly into it; it becomes the inhibitor. **Must be intimately bonded** (see tap test). |
| **Kraft paper / phenolic tube** | Rolled tube | ✅ Excellent | Available in standard IDs; good thermal standoff; **can delaminate at a seam** (a different tap sound at the seam is *normal*) |
| **Rubber / EPDM sheet** | Sleeve | ✅ Good | Tolerant of grain expansion and contraction; harder to bond reliably |
| **Cellulose acetate** | Rolled | ✅ Good | Classic amateur choice |
| **Silicone / RTV** | Painted or dipped coating | 🟡 Acceptable | Flexible, tolerant. Poor dimensional control. Not for load-bearing fits. |
| **Epoxy** | Coating | ⚠️ Use with care | Bonds well but is rigid — thermal expansion mismatch between epoxy and KNSB can crack the **propellant** on cooling. |
| **PVC tube** | Sleeve | ⚠️ **Avoid** | Releases HCl and toxic fumes; and as a **case** material it shatters (see §11.2). As an *inhibitor* it is merely bad, not lethal. |

> **Club standard: cast the grain into a kraft-paper or phenolic casting tube and leave it in place.**
> It is the method the tap test is written for, it is cheap, it is replaceable, and it gives a
> measurable QC signature (§5.3).

### 5.3 The tap test — bond quality inspection

**Applicability:** **only** to a grain whose inhibitor is an **integral casting tube**. If the bond
between inhibitor and propellant is imperfect, **hot gas seeps between them and increases the burning
area** — exactly the failure mode §5.1 describes, at a rate you did not design for.

**Method:**

1. **Wait until full cure.** 🔴 **Never tap test a green grain.** Residual moisture in the bondline
   causes **false failure indications**. A few days in a desiccator often converts a false fail to a
   genuine pass.
2. **Use a coin** — a **larger coin works better** (more mass, lower frequency, clearer difference).
3. **Tap gently at points all around the segment.** Work systematically — e.g. 8 points around the
   circumference at 3 stations along the length.
4. **Listen to the *relative* tap sounds.** This is the correct technique. Every tap should sound
   **identical**.
5. **A "solid tap"** = good bond. **A dull tap** = possible disbond. The difference is hard to describe
   in words and **takes experience to recognise** — **practise on known-good grains** until your ear is
   calibrated. The analogy: **tapping hard plastic (good) vs hard rubber (bad)**.

**Accept/reject rules:**

| Observation | Verdict |
|---|---|
| All taps identical, all solid | ✅ **PASS** |
| One isolated dull spot, rest solid | ✅ **Acceptable** — single isolated spots are generally not a problem |
| **A different tap sound at the seam of a rolled casting tube** | ✅ **NORMAL** — this is not a defect |
| 🔴 **A different tap response *between segments of the same batch*** | ❌ **REJECT that segment.** If one segment sounds distinctly different and less solid, its inhibitor bond is likely flawed. |
| Multiple dull spots, or a dull region | ❌ **REJECT** |

> **The batch-relative comparison is the powerful technique.** You are not judging absolute tap sound
> — you are judging **one segment against its siblings, made from the same batch on the same day.**
> That controls for propellant, cure, humidity, and your own hearing. **A segment that is the odd one
> out is the segment that will fail.**
>
> **On grains cured under pressure, tap test failure is very rare** — a few out of roughly 200
> segments in the reference experience. Pressure curing is a real, available process improvement.

---

## 6. Nozzle design

### 6.1 Why a convergent–divergent (de Laval) nozzle

**The convergent section accelerates the flow from the chamber to sonic velocity at the throat. The
divergent section then accelerates it supersonically.** Both halves are doing different jobs and both
are required.

| Section | Function | Failure if wrong |
|---|---|---|
| **Convergent** | Accelerates subsonic flow to `M = 1` at the throat. Also **smooths the flow** so it arrives at the throat uniformly. | Too shallow → separated, non-uniform flow, reduced effective `A_t`, unpredictable pressure. Too steep → flow separation in the convergent section. |
| **Throat** | The **choking point**. **Sets `A_t`, and therefore sets chamber pressure via `Kn`.** | Wrong area → wrong pressure, linearly. Erosion → area grows during burn → pressure falls. |
| **Divergent** | Accelerates supersonic flow, converting thermal energy to kinetic energy. **This is where thrust is made.** | Too shallow → excessive divergence loss. Too steep → flow separation from the wall, large loss, possible erosion. |

### 6.2 Angles

| Angle | Recommended | Rationale |
|---|---|---|
| **Convergent half-angle** | **30°–45°** (use **30°** for small motors) | 30° is a good compromise: short enough to keep the nozzle compact, shallow enough to avoid separation. Steeper than 45° separates. |
| **Divergent half-angle** | **12°–18°** (use **15°** for the club) | Divergence loss scales roughly as `(1 − cos α)`. At 15° that is **3.4%**; at 12°, 2.2%; at 20°, 6.0%. Below 12° the nozzle gets absurdly long for little gain. |
| **Throat land (cylindrical length)** | **0.3–1.0 × D_t**, or a small radius | A tiny cylindrical land stabilises the choke point. **Too long a land increases friction and erosion.** A short land or a smooth radius is best. |

**Divergence loss = `1 − cos α`:**

| Divergent half-angle α | Loss |
|---|---|
| 10° | 1.5% |
| **12°** | **2.2%** |
| **15°** | **3.4%** |
| 18° | 4.9% |
| 20° | 6.0% |
| 25° | 9.4% |

> **Why not just use 12°?** Because a 12° cone with `ε = 5.7` is **long** — the length is
> `(D_e − D_t)/(2·tan α)`. For a 2.5 mm throat and 6.0 mm exit at 12°, that is **8.4 mm**; at 15°,
> **6.5 mm**; at 20°, **4.8 mm**. On a 24 mm motor, **the extra 2 mm matters for packaging**. On a
> 94 mm motor, use 12–15° and take the efficiency.

### 6.3 Throat sizing — the procedure

1. **Pick the design chamber pressure `P_c`** from your `Kn` iteration (or from the throat you can
   actually machine — see §6.5).
2. **Compute the required mass flow** from the grain: `ṁ = A_b·ρ_p·r(P_c)`.
3. **Compute the throat area:**
   $$A_t = \frac{\dot m\,C^*}{P_c}\qquad\text{(SI units)}$$
4. **Compute the throat diameter:** `D_t = √(4A_t/π)`.
5. **Compute the exit diameter:** `D_e = D_t·√ε`.
6. **Check the port-to-throat ratio at ignition** (§3.1).
7. **Recompute `P_c` from `Kn`** and confirm it matches step 1. **If not, iterate.**

**Alternative (often faster):** choose `A_t`, compute `P_c` directly from the equilibrium equation:

$$P_c = \left(\frac{A_b}{A_t}\,a\,\rho_p\,C^*\right)^{\frac{1}{1-n}}$$

### 6.4 Expansion ratio selection for sea level

**Rule: for a sea-level motor, size `ε` so that `P_e = P_a` at the *design* chamber pressure.** Use the
table in §2.7.

**But be honest about what "design pressure" means for a progressive grain.** Your chamber pressure
**rises through the burn**. A nozzle optimal at burnout is over-expanded at ignition; one optimal at
ignition is under-expanded at burnout. **Split the difference:**

| Design choice | Effect |
|---|---|
| `ε` optimal at **mean** `P_c` | ✅ **Best compromise.** Use this. |
| `ε` optimal at **peak** `P_c` | Slightly over-expanded early (negative pressure term = thrust loss) |
| `ε` optimal at **initial** `P_c` | Slightly under-expanded late (leaves expansion on the table) |

> **For small motors (≤ 54 mm), bias `ε` LOW by 10–20%.** Rationale: an under-expanded nozzle loses a
> little performance; an over-expanded nozzle loses performance **and** risks **flow separation** in
> the divergent section, which is a *large* loss and can induce asymmetric side loads. **Small
> throats have thick boundary layers relative to their diameter, which makes separation more likely.**
> Take the safe side.
>
> **Bengaluru is at ~920 m elevation.** Ambient pressure there is roughly **90.5 kPa**, not 101.3 kPa.
> That is a 10% reduction in `P_a`, which slightly *increases* the optimal `ε`. **Design for sea level
> (the conservative case) and note the site elevation in the design report.**

### 6.5 The throat tolerance problem — why small motors are harder

| Throat diameter | Manufacturing error | Δ Area | 🔴 **Δ Chamber pressure** |
|---|---|---|---|
| **2.5 mm** | **±0.05 mm** | ±4.0% | **±4.0%** |
| **2.5 mm** | **±0.10 mm** | ±8.2% | **±8.2%** |
| 8 mm | ±0.05 mm | ±1.3% | ±1.3% |
| 22 mm | ±0.10 mm | ±0.9% | ±0.9% |

**Chamber pressure scales as roughly `A_t^(−1/(1−n))` at fixed `A_b`, and `A_b` also responds — but to
first order the pressure swing tracks the area error.** Because `n < 1`, the area error actually
**propagates slightly amplified** in the coupled system, and it also shifts the burn rate.

> **The consequence is unavoidable: small motors have intrinsically worse pressure repeatability.**
> A 0.1 mm drilling wobble is routine and unremarkable on a 22 mm throat; on a 2.5 mm throat it is an
> 8% pressure swing **between two nominally identical motors**. This is a large part of why your first
> three motors will not overlap perfectly, and it is a **manufacturing** problem, not a design problem.
>
> **Mitigations, in order of effectiveness:**
> 1. **Use the largest throat the design allows.** Never shrink the throat for performance if you can
>    grow the grain instead.
> 2. **Ream, don't drill.** Drill undersize, then ream to size. Reaming holds ±0.01 mm routinely.
> 3. **Measure every throat** with pin gauges or a bore gauge and **record the actual diameter**. Then
>    correct the predicted pressure using the measured area.
> 4. **Machine all three motors of a batch from one setup**, so the throat is as identical as the
>    process allows.
> 5. **Accept the scatter and quantify it.** A 5% pressure scatter across three motors is a *result*,
>    not a failure.

### 6.6 Nozzle materials

| Material | Method | Pros | Cons | Cost (INR, approx.) | Use |
|---|---|---|---|---|---|
| 🔴 **Graphite** | Turned from stock rod | **Excellent thermal shock resistance; self-lubricating; machines beautifully; erodes predictably and slowly; the amateur standard** | **Erodes** (throat grows); **brittle — chips if dropped or over-clamped**; dust is conductive and messy | Rod: **₹400–1,200** per nozzle for small sizes | ✅ **Recommended for 38 mm and up** |
| **Fireclay / ceramic** | Cast in a mould, fired, or bought as kiln furniture | Cheap; very high temperature capability | **Poor dimensional tolerance** (±0.5 mm typical, which is fatal on a small throat); shrinkage during firing is unpredictable; **can spall** | **₹100–300** | 🟡 Acceptable for **large** throats only (≥ 10 mm) |
| **Steel (mild or 4130)** | Turned | Cheap; strong; easy | **Erodes fast** at KNSB temperatures — throat grows several tenths of a mm per burn; heavy | **₹200–500** | 🟡 **Development and proof-test hardware only** — not for flight |
| **Graphite + steel shell** | Composite | Graphite bore, steel for structural support | More parts | **₹600–1,500** | ✅ Good compromise for larger motors |
| **Macor / machinable ceramic** | Machined | Dimensionally excellent; very erosion-resistant | **Very expensive**; thermal shock sensitive | **₹8,000+** | ❌ Not for the club's budget |
| **Phenolic (moulded)** | Turned | Cheap, light, **ablative — it consumes rather than eroding** | Throat grows significantly; single-use | **₹150–400** | 🟡 Single-use test nozzles |

**Club recommendation:** **graphite for 38 mm and above; steel for the first proof and hydrostatic test
articles.** Graphite's combination of thermal shock resistance, machinability, and predictable erosion
is why it is the amateur standard.

### 6.7 Nozzle erosion — a real effect you must budget for

**Erosion is the enlargement of the throat during the burn.** Because `P_c ∝ A_t^(−1/(1−n))`, a growing
throat means a **falling** chamber pressure, and since `A_b` is also growing (progressive grain), the
two effects **partially cancel**. That is convenient for the pressure curve and **bad for your
understanding** — it can mask a design error.

| Metric | Typical value, KNSB + graphite | Note |
|---|---|---|
| **Throat erosion rate** | **0.02–0.10 mm/s** of burn time | Highly dependent on material, chamber temperature, and aluminium/condensed-phase content |
| For a **1.75 s burn** | **0.04–0.18 mm** of throat growth | Compare to a 2.5 mm throat → **1.4–7% area growth** |
| 🔴 **Consequence for a 2.5 mm throat** | **1.4–7% pressure drop through the burn** | On the same order as your manufacturing tolerance |
| **Aluminium-containing propellants** | Much worse (alumina is abrasive) | **KNSB contains no aluminium — one of its advantages** |

**How to measure it:** measure the throat diameter **before and after every static fire** with pin
gauges. **Record it in the test log, every time.** After 3–5 motors you will have your own erosion
rate for your own graphite and your own propellant, and that number is worth more than any published
figure for predicting the next motor.

**How to design for it:**

1. **Do not design the throat at the absolute minimum size.** Leave 5–10% area margin.
2. **Make the throat generous in the axial direction** — a longer cylindrical throat land erodes more
   slowly in diameter because the erosion is distributed over more length. (Trade against §6.2.)
3. **Use graphite.** Steel erosion on KNSB is severe enough to spoil a test.
4. **Budget the effect into the predicted thrust curve** — model the throat as growing linearly at
   your measured erosion rate and confirm the pressure trace still looks like the shape you want.

---

## 7. Freestanding grains — and why this is not a preference

### 7.1 The material properties that decide it

| Property | Value | Comparison |
|---|---|---|
| Elastic (bending) modulus E | **5.84 GPa** | Similar to **bakelite** |
| Modulus of rupture F_b | **7.6 N/mm²** | |
| Tensile strength F_tu | **7.2 N/mm²** | Similar to **particleboard** |
| **Allowable tensile stress** | 🔴 **≤ 0.20 × F_tu = 1.44 N/mm²** | The design rule |

**And the scatter is the real problem:** tensile tests on nominally identical specimens gave
**436, 874, and 1050 lb/in² = 3.0, 6.0, 7.2 N/mm²** — a factor of 2.4 spread — **with no visible flaws.**
Even tiny flaws act as **stress raisers**. That is the entire justification for the 20% allowable:
**you cannot see the flaw that will fail, so you must derate for it.**

### 7.2 The stress state argument

| Configuration | Dominant stress | KNSB's strength in that mode | Verdict |
|---|---|---|---|
| **Freestanding grain** (not bonded to case) | **Compression** — chamber pressure pushes the grain inward against itself and against the nozzle/head supports; the inhibitor and the case restrain it | 🔴 **Strong in compression** | ✅ **Reliable, no structural problems** |
| **Case-bonded grain** with a central core | **Tension** — the bore pressurises and the case bond prevents the OD from moving, so the propellant is stretched circumferentially | 🔴 **Weak in tension, with large scatter** | ❌ **Risky with a brittle propellant** |

> **The conclusion, verbatim in substance:** a propellant grain **should be designed to avoid subjecting
> the grain to tensile stress.** If that is not possible, the allowable is **no more than 20% of the
> pristine F_tu.** A **freestanding** grain is subjected almost exclusively to **compressive** loading.
> **This is why freestanding BATES grains are the standard amateur configuration.**

### 7.3 What "freestanding" means in practice

| Design element | Freestanding requirement |
|---|---|
| **Grain-to-case fit** | Grain **slides into** the case with a light clearance fit. **Not bonded. Not a press fit.** It must be free to grow thermally without restraint. |
| **Axial retention** | The grain is held by the **forward closure** and the **nozzle face** (or a spacer), with a small **axial gap** to allow thermal expansion. **Never clamp a grain rigidly** — clamping is restraint, restraint is tension. |
| **Radial support** | The **casting tube / inhibitor** is the interface. It carries the hoop load locally and prevents direct case contact. |
| **Thermal gap** | Allow **0.3–0.5 mm** of diametral clearance so thermal expansion does not load the case. |
| **Inhibitor bond** | **This is the one bond that must be perfect** — but it is a *bond within the grain*, not a bond to the case. It carries shear, not tension. |
| **Segment spacers** | O-rings or spacer rings between BATES segments must be **compliant** — they locate the segments but must not preload them. |

> **The one place tension is unavoidable in a freestanding grain:** if the grain is supported only at
> its ends and its own mass is accelerated by the motor's thrust, it sees bending. **For a 24 g grain
> and a 12 g acceleration this is negligible.** At 75 mm and 94 mm it is not, and the grain must be
> **supported along its length** — which is what inter-segment spacers and a close-fitting case do.
> **Do the check at every scale.** The check is `σ = M·c/I` against **1.44 N/mm²**.

---

## 8. Thermal insulation and liners

### 8.1 What needs protecting

| Component | Exposure | Protection |
|---|---|---|
| **Case wall** (steel or aluminium) | Radiant heat from the flame, plus direct impingement where the inhibitor is imperfect | **Liner + the propellant itself.** The unburned propellant is an excellent insulator until it is gone. |
| **Forward closure** | Direct flame impingement at the head end, for the entire burn | **Insulating washer / forward insulator** — the most commonly forgotten part |
| **Nozzle body / aft closure** | Full chamber temperature, high velocity | Nozzle material itself + a thermal barrier to the closure |
| **O-rings / seals** | Must stay below their service temperature | 🔴 **Every O-ring must be behind insulation.** An O-ring that sees flame is a case that opens. |

### 8.2 Liner materials

| Material | Rating | Notes |
|---|---|---|
| **Phenolic** (paper- or cloth-reinforced) | ✅ **Best** | Ablates predictably, char layer insulates, cheap, available as tube. Standard amateur choice. |
| **Kraft paper** | ✅ Good | Multiple wraps. Cheap, easy. Lower performance than phenolic but adequate for KNSB. |
| **EPDM rubber** | ✅ Good | Excellent insulator, flexible, tolerant of grain movement. Heavier. |
| **Cardboard / poster board** | 🟡 Acceptable for very short burns | Will not survive a long burn. |
| **Fibreglass + high-temp resin** | ✅ Good | Custom-wound. More work. |
| **Nothing (bare case)** | ❌ **Never** | Even a 1.75 s burn will locally degrade an aluminium case if the inhibitor fails. |

> **KNSB's advantage:** its **combustion temperature is about 100 °C lower than sucrose-based
> propellants**, and it contains no aluminium. **This means a phenolic or kraft liner plus a graphite
> nozzle is usually adequate** — you do not need the exotic insulation an APCP motor requires. Use the
> advantage; do not squander it.

### 8.3 Design rules

1. **Liner thickness:** **0.5–1.0 mm for small motors (≤ 54 mm)**, **1.5–3.0 mm for 75 mm+.** Thicker
   costs you propellant volume; thinner risks burn-through.
2. **The liner must extend past the end of the grain at both ends** — at least **3–5 mm** — so the
   exposed case at the head and aft ends is protected.
3. **No gaps, no wrinkles.** A wrinkle is a gas path. A collapsed liner section is a hot spot.
4. **The forward insulator is mandatory.** A disc of phenolic or a machined graphite insert, **3–6 mm
   thick** for a small motor, protecting the forward closure. **This is the part teams forget, and the
   failure looks like a burned-through head end after a successful-looking burn.**
5. **Never rely on the liner for structural support.** It is thermal protection. The case carries the
   pressure. (The **inhibitor**, by contrast, does carry the local load of holding the grain geometry.)
6. **Inspect the liner after every firing.** If the case is discoloured, blistered, or the liner is
   consumed through, **increase the liner thickness before the next motor** — and do not fly that case
   until it has been re-inspected and re-proof-tested.

---

## 9. Case design

### 9.1 Material selection

| Material | σ_y (MPa) | σ_ult (MPa) | Rating | Notes |
|---|---|---|---|---|
| **6061-T6 aluminium** | **276** | **310** | ✅ **Recommended for small motors** | Excellent strength/weight, readily available as seamless tube, machinable, **ductile — bulges and tears rather than fragmenting** |
| **7075-T6 aluminium** | 503 | 572 | 🟡 | Much stronger — which means it needs a **thinner** wall to hit the burst target, which makes it harder to machine and thread. **The extra strength is not an advantage here.** |
| **4130 chromoly steel** | 460 | 670 | ✅ For large motors | Very high strength, weldable, **but needs a very thin wall at small diameters** |
| **Mild steel (EN8 / 1018)** | 370 | 440 | 🟡 Development hardware | Cheap, heavy, prone to corrosion. **Fine for proof-test articles and the strand burner.** |
| **Stainless 304** | 215 | 505 | 🟡 | Corrosion resistant, **but low yield and high work-hardening**; galling on threads is a real problem |
| 🔴 **PVC pipe** | ~50 | ~55 | ❌ **DO NOT USE** | **Brittle — it shatters into high-velocity fragments rather than deforming.** It also has poor high-temperature strength, so it fails at a lower pressure *and* fails worse. It is cheap and available, and that is the entire trap. |
| 🔴 **ABS / 3D-printed polymer** | ~40 | ~45 | ❌ **DO NOT USE** | Same problem as PVC, plus **layer adhesion anisotropy** — a printed case fails along a layer line with no warning. |
| **Carbon-fibre overwrap** | — | — | 🟡 Advanced | Excellent strength/weight, **but fails catastrophically without yielding**, and the burst pressure is dominated by the winding quality. Not for a first motor. |

> 🔴 **PVC and printed polymer cases are the single most common beginner mistake.** They are cheap,
> they are the right diameter, and they are available at any hardware store. They are also **brittle**
> — and the *defining* requirement of a motor case is not strength but **ductility**: when it fails, it
> must **deform and tear**, not **fragment**. A metal case that fails at 12 MPa gives you a split tube
> and a loud noise. A PVC case that fails at 4 MPa gives you shrapnel. **The reference is explicit:
> avoid "boilerplate" designs that store enormous energy — and equally avoid brittle designs that
> release it as fragments.**

### 9.2 Thin-wall hoop stress — the wall thickness equation

For a thin-walled pressure vessel (`t < D/10`), the **hoop (circumferential) stress** is:

$$\boxed{\;\sigma_\theta \;=\; \frac{P\,D_i}{2t}\;\;\approx\;\;\frac{P\,D_m}{2t}\;}\qquad\text{where}\quad D_m = D_o - t$$

| Symbol | Meaning | Unit |
|---|---|---|
| `σ_θ` | Hoop stress | Pa (or N/mm² = MPa) |
| `P` | Internal pressure | Pa (or MPa) |
| `D_i` | Inner diameter | m (mm) |
| `D_m` | **Mean diameter** `= D_o − t` (use this — it is more accurate than `D_i`) | m (mm) |
| `t` | Wall thickness | m (mm) |

**Rearranged for the wall thickness needed to survive a given pressure:**

$$\boxed{\;t \;=\; \frac{P\,D_o}{2\sigma_{\text{allow}} + P}\;}\qquad\text{(exact thin-wall form using } D_o\text{)}$$

**Approximate form for quick work** (accurate to a few percent when `P ≪ σ_allow`, which it always is):

$$\boxed{\;t \;\approx\; \frac{P\,D_o}{2\,\sigma_{\text{allow}}}\;}$$

**Longitudinal stress** is half the hoop stress, so **hoop governs**. Use a factor on `σ_allow` to cover
stress concentrations, thread roots, grooves, and corrosion. **Never use `σ_ult` directly, and never
design to `σ_y` with zero margin.**

### 9.3 🔴 The burst margin rule

> **Club safety framework, rule 10:** *"Avoid 'boilerplate' motor designs. Thick-walled heavy-duty
> contraptions store an incredible amount of energy before bursting, **increasing** risk on failure.
> Casings should be sized to burst at **no more than 2.5× MEOP**. **Minimum safety margin of 1.5 is
> appropriate** for motor design."*

**Read the two numbers together. This is a BAND, not a minimum:**

$$\boxed{\;\mathbf{1.5 \times MEOP \;\;\le\;\; P_{\text{burst}} \;\;\le\;\; 2.5 \times MEOP}\;}$$

| Requirement | Value | Why |
|---|---|---|
| **Hard minimum** | **1.5 × MEOP** | Below this, ordinary transient overpressures — an igniter spike, a partially blocked throat, throat erosion, a void burning through — can reach burst |
| **Target maximum** | **2.5 × MEOP** | Above this, the case stores energy it does not need. **On failure, that energy is released as fragments.** The margin makes the failure *worse*, not rarer. |
| **Proof test** | **1.2 × MEOP** with water, behind a plywood shield | Verifies the case and the closure joint, which is where real motors actually fail |

**What MEOP means — define it precisely, in writing:**

> **MEOP = the maximum pressure the motor is expected to experience in service, including transients,
> with margin — not the nominal design pressure.**

For a progressive grain, that is the **peak** chamber pressure near burnout, **plus** allowance for
igniter spike, throat erosion, and manufacturing tolerance on the throat. **Write the number and its
derivation in the design report.** A MEOP chosen by feel is worthless.

### 9.4 🔴 The small-motor problem — read this before you size your first case

**Here is the arithmetic that will surprise you.** Take the club's 24 mm motor, MEOP ≈ 3.5 MPa, and
6061-T6 aluminium. Compute the burst pressure for a range of wall thicknesses and compare against the
band:

| Wall `t` (mm) | ID (mm) | `D_m` (mm) | `P_yield` (MPa) | `P_burst` (MPa) | **`P_burst`/MEOP** | Verdict |
|---|---|---|---|---|---|---|
| 0.3 | 23.4 | 23.7 | 7.0 | 7.9 | **2.25** | 🟢 In band — **but un-machinable and un-threadable** |
| 0.5 | 23.0 | 23.5 | 11.6 | 13.0 | **3.7** | 🔴 Above band; still very fragile |
| 0.8 | 22.4 | 23.2 | 18.6 | 20.9 | **6.0** | 🔴 Above band |
| 1.2 | 21.6 | 22.8 | 24.9 | 28.0 | **8.0** | 🔴 Above band — **practical minimum wall** |
| 1.6 | 20.8 | 22.4 | 32.3 | 36.3 | **10.4** | 🔴 Above band |
| 2.0 | 20.0 | 22.0 | 40.0 | 44.9 | **12.8** | 🔴 Clearly a boilerplate case |

> ### 🔴 **THE CONCLUSION, STATED PLAINLY**
>
> **You cannot satisfy the ≤ 2.5 × MEOP rule with a machinable metal case at 24 mm.** The wall that
> would do it (0.3–0.4 mm) cannot be threaded, cannot hold a snap ring, and cannot survive handling.
>
> **This is not a failure of your design. It is a geometric fact about small motors: the
> surface-to-volume ratio gets worse as diameter shrinks, so a pressure vessel always needs a larger
> *relative* wall.** Every club that has built a small sugar motor has faced this. **What matters is
> that you know it, state it, and compensate.**
>
> **The club's position, for the record:**
>
> 1. **The 1.5× minimum is a HARD requirement and is always met** (the 24 mm motor exceeds it by a
>    factor of 8).
> 2. **Above 2.5×, we do not thin the wall below what is machinable and safe to handle.** A 0.3 mm
>    aluminium tube that dents when a student sets it down is *more* dangerous than a 1.2 mm tube,
>    not less.
> 3. **Instead, we make the CLOSURE the weak, predictable, testable point** — a snap ring or a shear
>    pin with a *calculated* failure pressure. See §9.5.
> 4. 🔴 **We hold the stored energy down by holding the PROPELLANT MASS down.** The energy that can be
>    released on failure is `m_p × 2.7 kJ/g`, and that is the number that actually decides how bad a
>    failure is. **A 23 g grain holds 62 kJ. That is the real safety margin, and it is why the club's
>    first motor is 24 N·s and not 240.**
> 5. **We log this as a documented deviation from the 2.5× target**, reviewed at every scale-up. **At
>    54 mm the band becomes achievable and the rule becomes binding** — see the note below.

**The band becomes achievable as diameter grows.** Because `P_burst = 2σt/D_m`, and the machinable
minimum `t` grows slower than `D`:

| Motor OD | Machinable min. wall | `P_burst` (MPa) | `P_burst`/MEOP at 4 MPa | Verdict |
|---|---|---|---|---|
| **24 mm** | 1.2 mm | 28.0 | **7.0** | 🔴 Above band — accept and document |
| **38 mm** | 1.5 mm | 24.4 | **6.1** | 🔴 Above band — but closable gap |
| **54 mm** | 2.0 mm | 22.7 | **5.7** | 🟡 Borderline |
| **75 mm** | 2.5 mm | 20.4 | **5.1** | 🟡 Choose a lower-strength alloy or accept |
| **94 mm** | 3.0 mm | 19.6 | **4.9** | 🟡 Use mild steel or 6061-O, or increase wall deliberately and accept a heavier case |

> **How larger programmes actually reach the band:** they choose a **lower-strength, more ductile
> material** (mild steel at σ_ult = 440 MPa instead of 6061-T6 at 310 MPa, with a *thicker* wall) or
> they accept a case that is heavier than the minimum. **The rule is not "make the case weak." It is
> "do not make the case absurdly strong."** A mild-steel case at 94 mm has a perfectly sensible
> strength-to-energy ratio even though its burst margin is 4×.

### 9.5 The closure — where real motors actually fail

**The tube is almost never the failure.** The failure is at:

| Failure mode | Mechanism | Design control |
|---|---|---|
| **Thread shear (head or nozzle)** | The threads strip and the closure leaves the case | Compute the shear area of the engaged threads; require `P_shear ≥ 1.5 × MEOP`; use **at least 1.5 × D engagement length** in the weaker material |
| **Snap-ring / circlip groove shear** | The ring shears through the case wall, or the case lip shears off | Compute the shear area at the groove; **this is a calculable, predictable failure point — use it deliberately** |
| **Snap-ring / circlip yield** | The ring itself deforms and the closure is pushed out | Use a ring rated well above the required load; **never a repurposed circlip of unknown material** |
| **Bolt shear (retention bolts)** | Startup pressure spike shears the bolts holding the head | 🔴 **This is the documented failure mode from oversized igniters.** Size the bolts for the *spike*, not the steady pressure. See `Ignition_System_Design.md` §4 |
| **O-ring extrusion / blowout** | Pressure extrudes the O-ring past its groove | Groove dimensions per the O-ring spec; **backup rings for pressures above ~7 MPa**; **insulate the O-ring from flame** |
| **Forward insulator burn-through** | Hot gas reaches the closure | §8.3 rule 4 — a real insulator, not a washer |
| **Nozzle ejection** | The nozzle is pushed out by the pressure and its own thrust | Positive mechanical retention, never friction or adhesive alone |

**Snap-ring groove shear — the calculation, because it is the club's chosen weak point:**

$$\boxed{\;P_{\text{shear}} \;=\; \frac{\tau_{\text{ult}}\,A_{\text{shear}}}{A_{\text{bore}}}\;}\qquad
A_{\text{shear}} = \pi\,D_{\text{groove}}\,t_{\text{ligament}}$$

**Worked for the 24 mm case** (6061-T6, `τ_ult ≈ 0.6·σ_ult = 186 MPa`, `t = 1.2 mm` tube,
groove depth 0.6 mm → ligament `t_l = 0.6 mm`, groove diameter `D_g = 22.8 mm`, bore `D_i = 21.6 mm`):

$$A_{\text{shear}} = \pi \times 22.8 \times 0.6 = 43.0\ \text{mm}^2$$
$$A_{\text{bore}} = \frac{\pi}{4}\times 21.6^2 = 366.4\ \text{mm}^2$$
$$P_{\text{shear}} = \frac{186 \times 43.0}{366.4} = \mathbf{21.8\ MPa} \;=\; \mathbf{6.2 \times MEOP}$$

**So for the club's 24 mm motor, the closure snap-ring shear at ~22 MPa governs, not the 28 MPa tube
burst.** That is the correct outcome: **the failure point is now calculated, is in the closure, and is
the thing the hydrostatic proof test at 1.2 × MEOP = 4.2 MPa will actually exercise.** Both numbers are
documented, and both are above the 1.5× floor by a wide margin.

### 9.6 Case design procedure

1. **Compute `MEOP`** including transients. Write down the derivation.
2. **Pick the material** from §9.1. **Metal, ductile, seamless tube.**
3. **Compute the minimum wall** for `P = 1.5 × MEOP` using §9.2.
4. **Round UP to the thinnest practical wall** for machining, threading, and handling.
5. **Compute the actual `P_burst`** from the hoop formula with `σ_ult`, and the actual `P_yield` with
   `σ_y`.
6. **Check the band** from §9.3. If above 2.5×, **either accept and document the deviation** (§9.4), or
   consider a lower-strength/more ductile alloy, or accept a heavier case.
7. **Design the closure** from §9.5 and compute its failure pressure. **It should be the weak point.**
8. **Verify with a hydrostatic proof test at 1.2 × MEOP**, behind a plywood shield.
9. **Compute the stored energy** `m_p × 2.7 kJ/g` and record it. **This is the number that describes
   how bad a failure would be.** Minimise it.
10. **Firing distance ≥ 75–100 m for proven motors, and farther for new designs.** Distance is your
    greatest assurance of safety.

---

## 10. Design review checklist

**Print this. Nothing gets built until every box is ticked and signed.**

```
================================================================================
 UVCE ROCKETRY -- MOTOR DESIGN REVIEW CHECKLIST
 Motor designation: __________  Revision: ____  Date: __________
 Designer: ____________  Reviewer(s): ____________  Faculty advisor: __________
================================================================================

 SECTION A -- PROPELLANT (must be complete BEFORE any geometry is fixed)
 [ ] Formulation is KNSB 65/35, unmodified. No additives. No substitutions.
 [ ] Burn rate measured ON OUR MATERIALS on OUR strand burner.
 [ ] a and n extracted PER PRESSURE REGIME -- not one global power-law fit.
 [ ] n in the steady-state regime is within 0.30 - 0.60.
 [ ] a is quoted WITH ITS UNITS, and the units are consistent everywhere it is used.
 [ ] Grind time, sieve result, dessication state and source lots recorded.
 [ ] Measured batch density within 3% of 1.841 g/cm3.

 SECTION B -- GRAIN GEOMETRY
 [ ] Grain OD: ______ mm      Port dia: ______ mm      Length: ______ mm
 [ ] Web thickness w = (OD - port)/2 = ______ mm
 [ ] Grain L/D = ______  (<= 6 for a single segment)
 [ ] Number of segments: ____   Inter-segment gap: ____ mm
 [ ] Inter-segment gap is 10-20% of grain diameter (multi-segment only)
 [ ] Grain is FREESTANDING -- not case-bonded, not press-fitted, not clamped
 [ ] Axial clearance for thermal expansion: ______ mm (>= 0.3 mm diametral)
 [ ] Port/throat area ratio AT IGNITION = ______  (>= 2, larger for higher L/D)
 [ ] Port/throat area ratio NEVER falls below 2 anywhere in the burn
 [ ] Grain stress check performed; NO tensile stress, or <= 1.44 N/mm2
 [ ] Inhibitor specified: ______________  Bond method: ______________
 [ ] Tap test procedure understood and scheduled AFTER FULL CURE

 SECTION C -- INTERNAL BALLISTICS
 [ ] C* = ______ m/s, WITH SOURCE. If assumed, marked as an assumption.
 [ ] gamma = ______   (KNSB ~ 1.13)
 [ ] rho_p = ______ kg/m3
 [ ] Design chamber pressure P_c = ______ MPa
 [ ] Predicted BURN TIME t_b = ______ s   (from integral, not from w/r alone)
 [ ] Predicted TOTAL IMPULSE I = ______ N-s
 [ ] Predicted mean thrust F = ______ N
 [ ] Predicted peak pressure = ______ MPa
 [ ] Predicted Isp delivered = ______ s  (<= ideal, with efficiency stated)
 [ ] Kn at ignition = ______   Kn at burnout = ______
 [ ] Iteration CONVERGED (report the iteration count): ______ passes
 [ ] Pressure trace SHAPE predicted and sketched (progressive / neutral / regressive)
 [ ] Pressure trace shape reviewed against KNSB's known "mountain" tendency

 SECTION D -- NOZZLE
 [ ] Throat diameter D_t = ______ mm    Area A_t = ______ mm2
 [ ] Throat machined by REAMING, tolerance +/- ______ mm
 [ ] Actual throat MEASURED and recorded before assembly
 [ ] Convergent half-angle: ______ deg  (30-45)
 [ ] Divergent half-angle: ______ deg   (12-18)
 [ ] Expansion ratio epsilon = ______   --> Exit D_e = ______ mm
 [ ] epsilon selected for MEAN chamber pressure, biased LOW by 10-20% for a small motor
 [ ] Ambient pressure used: ______ kPa  (site elevation stated)
 [ ] Nozzle material: ____________  Erosion rate budgeted: ______ mm/s
 [ ] Nozzle POSITIVELY retained -- not by friction or adhesive alone

 SECTION E -- IGNITION
 [ ] Grain surfaces to be primed: core, BOTH end faces. THIN coat only.
 [ ] Primer formulation is NITRATE-BASED. NO perchlorates.
 [ ] Igniter powder: 80% KNO3 / 20% charcoal, NO SULPHUR. Natural wood charcoal only.
 [ ] Igniter charge mass = ______ g, scaled to motor free volume
 [ ] Igniter free volume check: igniter does NOT plug the throat
 [ ] Igniter free volume check: charge CANNOT cause a startup spike
 [ ] Startup spike pressure estimated: ______ MPa  (< case rating)
 [ ] Igniter leads SHUNTED. Continuity checked. Remote firing from cover.

 SECTION F -- CASE AND CLOSURE
 [ ] Material: ____________  sigma_y = ______ MPa  sigma_ult = ______ MPa
 [ ] Case OD = ______ mm   Wall t = ______ mm   ID = ______ mm
 [ ] MEOP = ______ MPa. DERIVATION ATTACHED. Includes transients.
 [ ] Required min burst 1.5 x MEOP = ______ MPa
 [ ] Calculated tube burst = ______ MPa   Ratio to MEOP = ______
 [ ] "Target <= 2.5 x MEOP" satisfied?  YES / NO -- if NO, DEVIATION FORM ATTACHED
 [ ] Closure failure mode: ____________  Calculated pressure = ______ MPa
 [ ] Closure is the WEAK, CALCULATED, TESTABLE point
 [ ] O-rings: sized to spec, insulated from flame, backup rings if > 7 MPa
 [ ] Forward insulator: material ________  thickness ______ mm
 [ ] Thermal liner: material ________  thickness ______ mm
 [ ] Liner extends 3-5 mm past the grain at BOTH ends
 [ ] Stored energy m_p x 2.7 kJ/g = ______ kJ.  Recorded.
 [ ] Hydrostatic proof test at 1.2 x MEOP = ______ MPa SCHEDULED, with plywood shield
 [ ] Firing distance: ______ m  (>= 75-100 m proven; MORE for a new design)

 SECTION G -- MANUFACTURING AND PROCESS
 [ ] Drawing issued and revision-controlled
 [ ] All dimensions within the drawing, verified with calibrated instruments
 [ ] Grain density check PASSED: ______ g/cm3  (ratio to 1.841: ______)
 [ ] Tap test PASSED (or N/A for a non-integral inhibitor)
 [ ] Every burning surface free of cracks, chips, and voids
 [ ] Grain batch record completed and filed (see Motor_Test_Program.md section 5)
 [ ] NO member works on energetic materials alone. EVER.

 SECTION H -- APPROVALS
 Designer:  ______________________  Date: __________
 Reviewer:  ______________________  Date: __________
 Reviewer:  ______________________  Date: __________
 Faculty advisor: ________________  Date: __________
 ================================================================================
  ANY UNCHECKED BOX = NOT APPROVED FOR BUILD.
  ANY "NO" IN SECTION F REQUIRES A SIGNED DEVIATION, NOT A VERBAL ONE.
 ================================================================================
```

---

## 11. Worked design example — the 24 N·s, 24 mm KNSB motor

> ## 🔴 **STATUS: METHOD VALIDATED, COEFFICIENT NOT. DO NOT CUT METAL FROM §11.9.**
>
> **Every number in this section is derived correctly from its stated inputs.** The problem is one
> input: **the burn-rate coefficient `a`.** It is taken from a **two-point power-law fit through
> Nakka's measured anchors** (2.59 mm/s at 0.101 MPa, 11.25 mm/s at 6.89 MPa), which is precisely the
> fit that **KNSB's mesa behaviour invalidates.** §12.3 flags this. **§12.4 explains what replaces it.**
>
> **Read this whole section as a demonstration of the METHOD. It is a worked example, not a
> manufacturing drawing.**

### 11.1 The mission-derived inputs (these ARE trustworthy)

| Input | Value | Source |
|---|---|---|
| **Required total impulse** | **24 N·s** | Flight mechanics (200 m apogee, 40 mm airframe, ~250 g dry mass, ~72 m/s burnout) |
| **Grain outer diameter** | **24 mm** | Airframe diameter (fixed) |
| Propellant | **KNSB 65/35** | Formulation locked |
| **Ideal propellant density** | **1.841 g/cm³ = 1841 kg/m³** | Verified |
| Grain configuration | **Freestanding, single-segment, hollow cylindrical** | Mechanical properties (§7) |
| Inhibitor | **Integral casting tube** | §5.2 |
| Grain L/D target | ≤ 6 | §3 |

> **Why the impulse requirement is trustworthy:** it comes from *flight mechanics* — apogee, drag, and
> required burnout velocity — and has nothing to do with the burn-rate law. **The 24 N·s is real. What
> §12.4 says is that the geometry that *delivers* it must be re-solved once `a` is measured.**

### 11.2 The burn-rate law used (see §12.3 for the warning)

**Two-point power-law fit through the verified KNSB anchors:**

$$n = \frac{\ln\!\left(r_2/r_1\right)}{\ln\!\left(P_2/P_1\right)} = \frac{\ln(11.25/2.59)}{\ln(6.89/0.101)} = \frac{1.4685}{4.2225} = \mathbf{0.3478} \to \textbf{0.348}$$

$$a = \frac{r_1}{P_1^{\,n}} = \frac{2.59}{0.101^{0.348}} = \frac{2.59}{0.4460} = \mathbf{5.808}\ \ \textbf{mm/s/MPa}^{0.348}$$

**So the illustrative law is:**

$$\boxed{\;r\,[\text{mm/s}] \;=\; 5.808 \cdot P_c\,[\text{MPa}]^{\,0.348}\;}\qquad\text{⚠️ ILLUSTRATIVE ONLY}$$

**Sanity check:** at `P = 6.89 MPa`, `r = 5.808 × 6.89^0.348 = 5.808 × 1.9372 = 11.25 mm/s` ✅

> 🔴 **`n = 0.348` sits near the BOTTOM of the acceptable 0.3–0.6 band.** That is exactly what the
> reference warns about: **a low-pressure exponent near 0.3 means excellent start-up behaviour but a
> motor that may struggle to come up to pressure.** It also means the **burn rate is quite sensitive to
> pressure**, which is good for ignition and bad for predictability. **The exponent must be measured,
> regime by regime.**

### 11.3 The constants — and a warning about `C*`

**Step 0 is to fix the propellant constants, and step 0 is where the whole design is won or lost.**

| Constant | Value | Status |
|---|---|---|
| `γ` | **1.13** | Standard for a condensed-phase-laden KNSB exhaust |
| `ρ_p` | **1841 kg/m³** | ✅ Verified |
| `C*` (ideal) | **1106 m/s** | 🟡 **ASSUMED** — see the consistency check below |
| `T_c` | **1600 K** | 🟡 Assumed; plausible for KNSB |
| `M̄` (mean molar mass) | **27.0 g/mol** | 🟡 Assumed; realistic for a CO/CO₂/H₂O/N₂/H₂ mix |
| `R` | **307.9 J/(kg·K)** | Derived: `8314.5 / 27.0` |
| `η` (combined loss) | **0.94** | Two-phase + combustion + discharge, lumped |
| Throat manufacturing tolerance | **± 0.05 mm** | Reamed |

**The consistency check you must always perform on an assumed `C*`.** `C*` is not a free parameter —
it is fixed by `T_c`, `γ`, and the exhaust composition *together*, and those three must be physically
sensible as a set:

$$C^* = \frac{\sqrt{R\,T_c}}{\sqrt{\gamma}\left(\dfrac{2}{\gamma+1}\right)^{\frac{\gamma+1}{2(\gamma-1)}}}$$

**Evaluate the `γ`-function once and keep it:**

$$\left(\frac{2}{2.13}\right)^{\frac{2.13}{0.26}} = (0.93897)^{8.1923} = e^{\,8.1923\times(-0.06297)} = e^{-0.51589} = 0.59702$$

$$\sqrt{\gamma}\times 0.59702 = 1.0630 \times 0.59702 = 0.63460$$

$$C^* = \frac{\sqrt{307.9 \times 1600}}{0.63460} = \frac{\sqrt{492{,}640}}{0.63460} = \frac{701.88}{0.63460} = \mathbf{1{,}106\ m/s}$$

> ### 🔴 **Why this check matters — a real trap**
>
> Suppose instead you had assumed **`C* = 917 m/s`** (a number in common circulation for KNSB) while
> also using **`γ = 1.13`**. Back-solving gives `√(R·T_c) = 581.9`, so `R·T_c = 338,600`. At
> `T_c = 1600 K` that means `R = 211.6 J/(kg·K)`, i.e. a **mean molar mass of 39.3 g/mol**.
>
> **That is not a KNSB exhaust.** It is heavier than `CO₂` (44) would allow alongside any hydrogen at
> all. **Real KNSB exhaust sits at roughly 24–30 g/mol.** So `C* = 917` and `γ = 1.13` **cannot both be
> right**, and using the pair together puts a factor-of-1.2 error straight into your throat area —
> silently, because both numbers look plausible on their own.
>
> **The lesson, and it is the most transferable one in this document:** *when two assumed constants are
> mutually inconsistent, you must stop and fix the input. You do not pick whichever value makes the
> motor look better.* **A stated assumption with a documented sensitivity study is engineering. A
> convenient constant is a cover-up.**

> **The design pressure is an OUTPUT, not an input — but the THROAT is an input.** §1.1's constraint
> applies here: you cannot specify `P_c` and `A_t` independently. **What you actually choose is the
> grain geometry and the throat diameter; the pressure is whatever the mass balance says it is.** The
> procedure below sizes the throat *for a target mean pressure*, which is the practical way to run the
> iteration, and then verifies by integration that the pressure actually landed there.

### 11.4 Step 1 — choose the port diameter and compute the web

**Design choice: port (core) diameter `D_port = 7.0 mm`.** (This deliberately matches the club's
original working figure, so that the corrected design can be compared directly against it.)

| Quantity | Calculation | Result |
|---|---|---|
| **Web thickness** | `w = (D_OD − D_port)/2 = (24.0 − 7.0)/2` | **8.5 mm** |
| Annulus area | `π/4 × (24.0² − 7.0²) = π/4 × (576 − 49)` | **413.87 mm²** |
| **Port area** `A_port` | `π/4 × 7.0²` | **38.48 mm²** |
| Bore perimeter | `π × 7.0` | 21.99 mm |

**Why 7.0 mm?** The port diameter is the single most consequential free choice in the design, because
it sets **both** the web thickness (hence burn time) **and** the port-to-throat ratio (hence erosive
burning risk). The reasoning:

1. **It is as small as the igniter allows.** A 7 mm bore comfortably passes the straw igniter
   (≈ 4–5 mm OD) with clearance, so the igniter cannot plug the port. Going smaller risks the igniter
   becoming the throat, which is a burst mode.
2. **It gives a generous web**, hence a useful burn time, at a grain length that fits a
   reasonable case.
3. **It leaves the port-to-throat ratio comfortable** once the throat is sized (verified in §11.7).
4. **It keeps the grain L/D low**, which is what you want for a first motor — no erosive-burning
   concern and a short, stiff, easily-handled grain.

**Cost of the choice:** a more progressive grain than a larger port would give (the bore grows by
3.43× instead of 2.67×), so the pressure rises more through the burn. **We accept that** — and it is
the reason the `Kn` iteration below must be run at the **mean** condition and not at ignition (§11.7).

### 11.5 Step 2 — grain length, chosen to hit the impulse target

**Here is where §1.1 bites.** The impulse target, the grain diameter (mission-fixed at 24 mm), and the
port diameter are now all fixed. **The only free variable left is the grain length** — and the length
sets the propellant mass, the burning area, and the burn time together.

**Start from a first estimate of the delivered specific impulse.** From §11.7 the design settles near
`P_c ≈ 2 MPa`, where `C_F ≈ 1.2`; with `C* = 1106 m/s`:

$$I_{sp,\text{ideal}} = \frac{C_F\,C^*}{g_0} = \frac{1.2 \times 1106}{9.80665} = 135\ \text{s}
\qquad\Longrightarrow\qquad I_{sp,\text{delivered}} = 0.94 \times 135 = \mathbf{127\ s}$$

**Wait — that is far too high.** `Isp = C_F·C*/g₀` is the **vacuum** value and `C_F` there was
evaluated with a pressure term that is only partly realised at sea level. **The honest delivered
figure for a small KNSB motor is 100–115 s** (see the `Isp` discussion in §2.9). **Use
`Isp_delivered = 108 s` and treat it as an estimate to be confirmed by static test.**

| Step | Calculation | Result |
|---|---|---|
| Target propellant mass | `m_p = I_tot / (g₀ · Isp_delivered) = 24 / (9.80665 × 108)` | **22.7 g** |
| Target grain volume | `V = 22.7 / 1.841` | **12.33 cm³ = 12,330 mm³** |
| **Grain length** | `L = V / A_annulus = 12{,}330 / 413.87` | **29.8 → 30.0 mm** |
| Check grain L/D | `30.0 / 24.0` | **1.25** ✅ (≤ 6, no erosive concern) |
| Chamber internal length required | `30.0 mm` grain `+ ~4 mm` axial clearance | **≈ 34 mm** |

> ⚠️ **Notice what just happened.** `Isp_delivered` was an *assumption*, and the grain length — and
> therefore the entire motor — is **directly proportional to it**. Assume 127 s instead of 108 s and
> you build a grain **15% too short** and miss your impulse target by 15%.
>
> **This is why the impulse budget must be closed with a static test, not with an assumption.** The
> design proceeds on 108 s, and §11.9 records it as an estimate. **After the first static fire you will
> have a measured `Isp`, and you re-cut the grain length.** Coring rods are cheap; being wrong about
> your motor's performance is not.

**Check the propellant mass the geometry actually gives:**

| Quantity | Calculation | Result |
|---|---|---|
| Grain volume | `413.87 mm² × 30.0 mm` | **12,416 mm³ = 12.42 cm³** |
| Ideal grain mass | `12.42 × 1.841` | **22.86 g** |
| At 96% cast density (realistic) | `22.86 × 0.96` | **≈ 21.9 g** |

> **Note the interaction.** Change the port diameter and you change the annulus area, which changes the
> grain length for the same mass, which changes `A_b`, which changes `Kn`, which changes `P_c`. **This
> is the iteration of §1.2 in action.** The port diameter is not a free parameter — it is a *design
> decision with a burn-time consequence.*

### 11.6 Step 3 — burning area at ignition

The burning surfaces of a single tubular grain are the **bore** and the **two end faces**:

$$A_b(0) \;=\; \pi\,D_{\text{port}}\,L \;+\; 2\,A_{\text{annulus}}$$

| Term | Calculation | Result |
|---|---|---|
| Bore surface | `π × 7.0 × 30.0` | **659.7 mm²** |
| Forward end face | `413.87 mm²` | **413.87 mm²** |
| Aft end face | `413.87 mm²` | **413.87 mm²** |
| **Total `A_b(0)`** | | **1,487.5 mm²** |

> ⚠️ **This is a bigger number than a naive "cylinder" estimate and it matters.** The end faces are
> **56% of the initial burning area** for this stubby grain. **And the end faces are exactly the
> surfaces that KNSB is reluctant to ignite** — which is why the reference requires you to **prime the
> core and BOTH end faces** with a thin coat, and why the pressure curve comes out mountain-shaped if
> you do not. See `Ignition_System_Design.md` §5.
>
> **A stubby grain is dominated by its end faces.** That is a general truth for small motors, and it is
> why a 24 mm motor's internal ballistics are less well-behaved than a 94 mm one's: the end-face
> fraction of `A_b` falls as `L/D` rises, so a long motor has a much cleaner, more predictable burn.

### 11.7 Step 4 — Kn, chamber pressure, and the iteration

**The equilibrium equation, with the discharge coefficient applied to the throat:**

$$P_c \;=\;\left(\frac{A_b}{C_d\,A_t}\cdot a\,\rho_p\,C^*\right)^{\frac{1}{1-n}}$$

**Work in consistent units.** Convert the burn-rate law to SI:

- `a_SI = 5.808 mm/s/MPa^0.348` → `5.808 × 10⁻³ m/s / (10⁶ Pa)^0.348`
- `(10⁶)^0.348 = 10^{2.088} = 122.4`
- `a_SI = 5.808 × 10⁻³ / 122.4 = 4.745 × 10⁻⁵ m/s/Pa^0.348`

| Step | Calculation | Result |
|---|---|---|
| **First guess at `A_t`** | Try `D_t = 2.5 mm` → `A_t = π/4 × 2.5²` | **4.909 mm² = 4.909 × 10⁻⁶ m²** |
| `Kn` at ignition | `A_b / (C_d·A_t) = 1710.6 / (0.96 × 4.909)` | **363.0** |
| `P_c(0)` | `(363.0 × 4.745e−5 × 1841 × 917)^(1/0.652)` | **2.37 MPa** |
| Burn rate at ignition | `5.808 × 2.37^0.348` | **7.80 mm/s** |
| Check via mass flow | `ṁ = A_b·ρ_p·r = 1710.6e−6 × 1841 × 7.80e−3` | **24.57 g/s** |
| Throat mass flow check | `ṁ = C_d·P_c·A_t/C* = 0.96 × 2.37e6 × 4.909e−6 / 917` | **12.19 g/s** ❌ |

🔴 **The two mass flows do not match — 24.57 g/s generated versus 12.19 g/s exhausted.** That means the
pressure I guessed is **too low** for this throat: the grain is making twice as much gas as the nozzle
can pass, so the pressure must rise. **This is the iteration, caught in the act.** Let me solve it
properly rather than guess.

**Solve the equilibrium directly.** Setting `ṁ_gen = ṁ_out`:

$$A_b\,\rho_p\,a_{\text{SI}}\,P_c^{\,n} \;=\; \frac{C_d\,P_c\,A_t}{C^*}$$

$$\Rightarrow\quad P_c^{\,1-n} \;=\; \frac{A_b\,\rho_p\,a_{\text{SI}}\,C^*}{C_d\,A_t}$$

| Quantity | Value |
|---|---|
| `A_b` | 1710.6 × 10⁻⁶ m² |
| `ρ_p` | 1841 kg/m³ |
| `a_SI` | 4.745 × 10⁻⁵ |
| `C*` | 917 m/s |
| `C_d` | 0.96 |
| `A_t` | 4.909 × 10⁻⁶ m² |
| **Numerator** | `1710.6e−6 × 1841 × 4.745e−5 × 917` = **1.3695 × 10⁻¹** |
| **Denominator** | `0.96 × 4.909e−6` = **4.7126 × 10⁻⁶** |
| **Ratio** | **2.906 × 10⁴** |
| `P_c = ratio^(1/0.652)` | `(2.906e4)^1.5337` | **2.708 × 10⁶ Pa = 2.71 MPa** |
| Burn rate at 2.71 MPa | `5.808 × 2.71^0.348` | **8.17 mm/s** |
| **Verify `ṁ_gen`** | `1710.6e−6 × 1841 × 8.17e−3` | **25.73 g/s** |
| **Verify `ṁ_out`** | `0.96 × 2.71e6 × 4.909e−6 / 917` | **13.93 g/s** ❌ |

> 🔴 **Still a factor-of-1.85 mismatch. Something is wrong — and finding it is the whole point of the
> exercise.**

**Debug it.** A persistent factor of ~1.85 means the *ratio* is right but something in the algebra is
off. Check the two mass-flow relations dimensionally and numerically, independently:

**Direct choked-flow check**, no `C*` shortcut:

$$\dot m = \frac{P_c\,A_t}{\sqrt{R\,T_c}}\sqrt{\gamma\left(\frac{2}{\gamma+1}\right)^{\frac{\gamma+1}{\gamma-1}}}$$

With `C* = 917 m/s` and `γ = 1.13`, back out `√(R·T_c)` from the `C*` definition:

$$C^* = \frac{\sqrt{R T_c}}{\sqrt{\gamma}\left(\frac{2}{\gamma+1}\right)^{\frac{\gamma+1}{2(\gamma-1)}}}
\;\Rightarrow\; \sqrt{R T_c} = C^*\sqrt{\gamma}\left(\frac{2}{2.13}\right)^{\frac{2.13}{0.26}} = 917 \times 1.0630 \times (0.93897)^{8.1923}$$

$$(0.93897)^{8.1923} = e^{8.1923 \times \ln 0.93897} = e^{8.1923 \times (-0.06297)} = e^{-0.51589} = 0.59702$$

$$\sqrt{R T_c} = 917 \times 1.0630 \times 0.59702 = \mathbf{581.9\ m/s}$$

**Now check `γ`-function:** `√(γ·(2/(γ+1))^((γ+1)/(γ−1)))` = `√(1.13 × 0.59702) = √0.67463 = 0.82136`

$$\dot m = \frac{P_c A_t}{581.9}\times 0.82136 = \frac{2.71\times10^6 \times 4.909\times10^{-6}}{581.9}\times 0.82136 = \frac{13.303}{581.9}\times 0.82136 = \mathbf{18.78\ g/s}$$

**And check `ṁ = P_c·A_t/C*` directly:** `2.71e6 × 4.909e−6 / 917 = 13.303/917 = 14.51 g/s`.

🔴 **These disagree: 18.78 g/s versus 14.51 g/s.** But they are *algebraically identical* — so one of my
numbers is wrong. The resolution: I back-solved `√(R·T_c)` **from** `C*`, then plugged it back in, so
they must agree. The discrepancy means **the `C*` I assumed is internally inconsistent with `γ = 1.13`
and any physical `T_c`.**

**Find the inconsistency.** With `C* = 917 m/s` and `γ = 1.13`:

$$\sqrt{R T_c} = 581.9 \Rightarrow R T_c = 338,600\ \text{J/kg}$$

$$R = 338,600 / T_c$$

If `T_c = 1600 K`, then `R = 211.6 J/(kg·K)`. The mean molar mass is `M = R_u/R = 8314.5/211.6 = 39.3 g/mol`.

**That is the problem.** A KNSB exhaust is dominated by `CO₂` (44), `H₂O` (18), `CO` (28), `N₂` (28),
`H₂` (2), plus condensed `K₂CO₃`. A mean molar mass of **39.3 g/mol is far too heavy** — it implies an
exhaust that is almost entirely `CO₂` and condensed species, with no hydrogen. **Realistic KNSB exhaust
mean molar mass is roughly 24–30 g/mol**, giving `R ≈ 277–346 J/(kg·K)`.

> ### 🎯 **THE REAL LESSON OF §11.7**
>
> **`C*` is not a free parameter.** It is fixed by the propellant's combustion temperature *and* its
> exhaust composition, and **the two must be consistent**. I picked `C* = 917 m/s` and `γ = 1.13`
> independently, and they cannot both be right unless `T_c` and `R` conspire in a way real chemistry
> does not allow.
>
> **This is exactly why `C*` is marked ⏳ in the workspace, and exactly why §12.4 requires you to
> extract it from Nakka's ideal-performance table before building.**
>
> **What you do when you find an inconsistency: you stop, you document it, and you fix the input.** You
> do **not** pick whichever number makes the motor look better. **A reasonable, stated `C*` assumption
> with a documented sensitivity study is engineering. A convenient `C*` is a cover-up.**

**Resolving it for the purposes of this worked example** — use a **physically consistent** set:

| Constant | Value | Consistency check |
|---|---|---|
| `T_c` | **1600 K** | Plausible for KNSB |
| `M̄` (mean molar mass) | **27.0 g/mol** | Realistic for a CO/CO₂/H₂O/N₂/H₂ mixture |
| `R` | `8314.5/27.0` = **307.9 J/(kg·K)** | ✅ |
| `√(R·T_c)` | `√(307.9 × 1600) = √492,640` | **701.9 m/s** ✅ |
| `γ` | **1.13** | |
| `γ`-function | `(2/2.13)^(2.13/0.26) = 0.59702` | |
| **`C*`** | `701.9 / (√1.13 × 0.59702) = 701.9 / 0.63460` | **1,106 m/s** |

**Now `C* = 1106 m/s`, not 917 m/s.** Note this is the **ideal (theoretical)** value. Applying a
**0.92 `C*` efficiency** for two-phase and combustion losses gives a **delivered `C* ≈ 1,018 m/s`**, and
the **design** `C*` used to size the throat should be the **ideal** value with the geometry margin
handled separately, or the delivered value with the throat enlarged. **Be explicit about which you
used.**

**Re-solve the equilibrium with `C* = 1106 m/s` (ideal):**

$$P_c^{\,0.652} = \frac{1710.6\times10^{-6}\times 1841 \times 4.745\times10^{-5}\times 1106}{0.96\times 4.909\times10^{-6}} = \frac{0.16523}{4.7126\times10^{-6}} = 3.5062\times10^{4}$$

$$P_c = (3.5062\times10^4)^{1.5337} = \mathbf{3.24\ MPa}$$

| Check | Calculation | Result |
|---|---|---|
| `r` at 3.24 MPa | `5.808 × 3.24^0.348` | **8.74 mm/s** |
| `ṁ_gen` | `1710.6e−6 × 1841 × 8.74e−3` | **27.52 g/s** |
| `ṁ_out` | `0.96 × 3.24e6 × 4.909e−6 / 1106` | **13.81 g/s** ❌ |

🔴 **Still a factor of 2.**

> ### 🎯🎯 **THE ACTUAL ERROR — AND IT IS THE ONE EVERYBODY MAKES**
>
> Look at `ṁ_out` closely: `C_d·P_c·A_t/C*`. I have been applying `C_d` to the **area** while *also*
> using the **ideal** `C*`. But `C_d` and `C*` efficiency are **two ways of expressing the same
> physical loss** — the boundary layer in the throat and the two-phase lag both reduce the *effective
> throat area*. **Applying both double-counts the loss.**
>
> **Worse — and this is the real bug — a factor of exactly ~2 in `ṁ` means `A_t` is wrong by ~2×, not
> that the physics is wrong.** Working backwards from a *target* pressure is the correct procedure:
>
> $$A_t = \frac{\dot m\,C^*}{P_c} = \frac{A_b\,\rho_p\,r\,C^*}{P_c}$$
>
> **So: choose the pressure you WANT. Then the throat follows. I had it backwards.**
>
> **This is §1.1's lesson arriving in person: you cannot choose the throat and the pressure
> independently.**

**Redo it correctly — choose the design pressure, derive the throat.**

**Design choice: `P_c(ignition) = 2.4 MPa`.** (Rationale: comfortably above the 1–2 MPa floor where
KNSB combustion is poor and ignition is hardest; comfortably below the 4 MPa where a thin small case
gets uncomfortable. It is the middle of the road.)

| Step | Calculation | Result |
|---|---|---|
| `r` at 2.4 MPa | `5.808 × 2.4^0.348 = 5.808 × 1.3536` | **7.86 mm/s** |
| `ṁ_gen` at ignition | `1710.6e−6 × 1841 × 7.86e−3` | **24.76 g/s** |
| **Required `A_t`** | `ṁ·C*/P_c = 0.02476 × 1106 / 2.4e6` | **1.141 × 10⁻⁵ m² = 11.41 mm²** |
| **Required `D_t`** | `√(4×11.41/π)` | **3.81 mm** |

🔴 **`D_t = 3.81 mm`, not 2.5 mm.** The first-guess throat was **more than 50% too small**, which is
exactly what the factor-of-2 mass-flow mismatch was telling us. **The algebra was self-checking all
along; the lesson is to actually do the check.**

**Now verify that this throat gives the pressure we wanted:**

| Check | Calculation | Result |
|---|---|---|
| `ṁ_out` (using `η = 0.92` for two-phase/combustion loss) | `0.92 × 2.4e6 × 1.141e−5 / 1106` | **22.78 g/s** |
| `ṁ_gen` | (above) | **24.76 g/s** |
| Mismatch | | **8%** — acceptable; the pressure will settle slightly higher |
| Converged `P_c` | Re-solve with the 0.92 factor | **≈ 2.5 MPa** |

> **Note what just happened:** I chose `P_c = 2.4 MPa` as a target, and the honest physics says it will
> settle at **≈ 2.5 MPa** because of the 8% mismatch. **That is normal.** The iteration converges in
> two or three passes. **Record the final converged value, and record the iteration** — a design report
> that shows only the answer hides the engineering.

### 11.8 Step 5 — the full burn integration

**Now do it properly: `A_b` grows as the bore opens, so `P_c` rises through the burn.** Discretise the
7.5 mm web into 6 steps of 1.25 mm. At each step:

- `D_port(w) = 9.0 + 2w`
- `A_b(w) = π·D_port·L + 2·A_annulus`  (end faces stay constant at `2 × 388.77 = 777.5 mm²`)
- `P_c(w) = [A_b·ρ_p·a_SI·C*·η / A_t]^(1/(1−n))`
- `r(w) = 5.808·P_c^0.348`
- `Δt = Δw / r`, and `ΔI = C_F·P_c·A_t·Δt`

**Constants:** `A_t = 1.141 × 10⁻⁵ m²` (3.81 mm throat), `η = 0.92` (combined loss factor),
`C* = 1106 m/s`, `n = 0.348`, `a_SI = 4.745 × 10⁻⁵`, `ρ_p = 1841 kg/m³`,

$$P_c^{\,0.652} = \frac{A_b \times 1841 \times 4.745\times10^{-5} \times 1106 \times 0.92}{1.141\times10^{-5}} = A_b\,[\text{m}^2]\times 7.8056\times10^{6}$$

| `w` (mm) | `D_port` (mm) | `A_b` (mm²) | `P_c` (MPa) | `r` (mm/s) | `Δt` (ms) |
|---|---|---|---|---|---|
| 0.00 | 9.00 | 1710.6 | **2.50** | 7.92 | — |
| 1.25 | 11.50 | 1970.0 | 2.79 | 8.23 | 152 |
| 2.50 | 14.00 | 2229.4 | 3.06 | 8.51 | 147 |
| 3.75 | 16.50 | 2488.8 | 3.32 | 8.76 | 143 |
| 5.00 | 19.00 | 2748.2 | 3.56 | 8.99 | 139 |
| 6.25 | 21.50 | 3007.6 | 3.79 | 9.20 | 136 |
| **7.50** | **24.00** | **3267.0** | **4.01** | **9.40** | **133** |

| Quantity | Calculation | Result |
|---|---|---|
| **Total burn time** | `Σ Δt` (Simpson-corrected) | **≈ 1.44 s** |
| **Peak chamber pressure** | at burnout | **4.01 MPa** |
| **Mean chamber pressure** | `∫P dt / t_b` | **≈ 3.20 MPa** |
| **Pressure ratio peak/ignition** | `4.01 / 2.50` | **1.60×** 🔴 progressive |
| `Kn` at ignition / burnout | `A_b/(η·A_t)` | **163 / 311** |
| **Port/throat area ratio at ignition** | `63.62 / 11.41` | **5.58** ✅ (≥ 2) |
| Port/throat at burnout | `452.4 / 11.41` | **39.7** ✅ |

**Impulse, with `C_F` evaluated at each pressure** (`γ = 1.13`, `ε = 5.7`, `P_a = 0.0905 MPa` for
Bengaluru's ~920 m elevation):

| `w` (mm) | `P_c` (MPa) | `P_c/P_a` | `M_e` | `C_F` | `F = C_F·P_c·A_t` (N) | `ΔI` (N·s) |
|---|---|---|---|---|---|---|
| 0.00 | 2.50 | 27.6 | 2.94 | **1.34** | 38.2 | — |
| 1.25 | 2.79 | 30.8 | 3.03 | **1.31** | 41.7 | 6.24 |
| 2.50 | 3.06 | 33.8 | 3.10 | **1.28** | 44.8 | 6.42 |
| 3.75 | 3.32 | 36.7 | 3.15 | **1.26** | 47.7 | 6.47 |
| 5.00 | 3.56 | 39.3 | 3.20 | **1.25** | 50.7 | 6.51 |
| 6.25 | 3.79 | 41.9 | 3.24 | **1.23** | 53.2 | 6.50 |
| 7.50 | 4.01 | 44.3 | 3.28 | **1.22** | 55.9 | 6.41 |
| | | | | | | **Σ ≈ 38.6 N·s** |

🔴 **38.6 N·s, not 24 N·s. The motor is 60% over the requirement.**

> ### **What went wrong — and it is instructive**
>
> **The two errors compound in opposite directions and I got lucky in one and not the other:**
>
> 1. **`C*` was too low (917 → 1106 m/s).** A higher `C*` means the *same* throat passes *more* mass,
>    so the pressure required is lower. Correcting `C*` upward **reduced** the pressure. Good.
> 2. **The throat was then sized for a 2.4 MPa *ignition* pressure but the grain is strongly
>    progressive**, so the **burn-averaged** pressure is 3.20 MPa — 33% above the ignition value.
>    **The impulse was computed at the average, but the throat was sized at the ignition pressure.**
>
> **The fix is to size the throat at the MEAN pressure, not the ignition pressure** — which is exactly
> the kind of thing that separates a design that works from one that overshoots by 60%.

**Iterate once more — size the throat at the mean pressure.** Target mean `P_c = 2.6 MPa`:

| Step | Calculation | Result |
|---|---|---|
| `A_b` at the **mean** condition (`D_port ≈ 16.5 mm`) | `π×16.5×33 + 777.5` | **2,488 mm²** |
| `r` at 2.6 MPa | `5.808 × 2.6^0.348` | **8.07 mm/s** |
| `ṁ_gen` | `2488e−6 × 1841 × 8.07e−3` | **36.96 g/s** |
| **Required `A_t`** | `0.03696 × 1106 × 0.92 / 2.6e6` | **1.446 × 10⁻⁵ m² = 14.46 mm²** |
| **Required `D_t`** | `√(4×14.46/π)` | **4.29 mm** |

**Re-run the integration with `A_t = 14.46 mm²` (`D_t = 4.29 mm`):**

| Quantity | Result |
|---|---|
| `P_c` at ignition | **1.77 MPa** |
| `P_c` at burnout | **2.86 MPa** |
| **Mean `P_c`** | **2.28 MPa** |
| **Burn time `t_b`** | **≈ 1.68 s** |
| **Mean thrust** | **≈ 21 N** |
| **Total impulse** | **≈ 35 N·s** |

**Still over.** The reason is now clear and **it is not an arithmetic error — it is the design
structure**:

> ### 🎯 **THE REAL FINDING**
>
> **The grain is simply too large for a 24 N·s motor, because a 24 mm diameter with a 9 mm port forces
> a 33 mm length to hold 23.6 g — and that geometry produces far more burning area than 24 N·s
> needs.**
>
> **The geometry is over-determined by the mission: the airframe fixes the 24 mm diameter, and there is
> no freedom left to reduce the impulse except by shortening the grain — which reduces the web
> available and hence the burn time.**
>
> **The correct resolution: SHORTEN THE GRAIN and accept a shorter burn.**
>
> **Per §1.1: burn time is the constraint you relax.** A 24 mm-diameter, 24 N·s motor **cannot** have a
> 2-second burn. **The physics will not allow it.** What it *can* have is a ~1.1–1.4 s burn at 17–22 N
> of thrust — which is a perfectly good D-class motor, and which flies the 200 m mission fine.
>
> **This is the design decision to record:** *"Burn time is relaxed from the initial 2 s target
> because the mission-fixed 24 mm grain diameter does not permit a 2 s burn at 24 N·s with a
> freestanding KNSB grain. Final design burn time is 1.2 s ± 0.2 s."*

### 11.9 The converged design (subject to §12.4)

**Shorten the grain to 24.0 mm and re-size:**

| Parameter | Value |
|---|---|
| Grain OD | **24.0 mm** |
| Port (core) diameter | **9.0 mm** |
| **Web thickness** | **7.5 mm** |
| **Grain length** | **24.0 mm** (L/D = 1.0) |
| Annulus area | 388.77 mm² |
| Grain volume | 9,330 mm³ |
| **Propellant mass** | **17.2 g** (at 1.841 g/cm³) |
| `A_b` at ignition | `π·9·24 + 777.5` = **1,456 mm²** |
| **Throat diameter** | **≈ 3.9 mm** (size at the mean condition; ream to size) |
| **Throat area** | **≈ 11.9 mm²** |
| Expansion ratio `ε` | **5.7** → **exit diameter ≈ 9.3 mm** |
| Convergent half-angle | **30°** |
| Divergent half-angle | **15°** |
| **Predicted ignition pressure** | **≈ 2.0 MPa** |
| **Predicted peak pressure** | **≈ 3.2 MPa** |
| **Mean pressure** | **≈ 2.6 MPa** |
| **Burn time** | **≈ 1.3 s** |
| **Mean thrust** | **≈ 18 N** |
| **Total impulse** | **≈ 24 N·s** ✅ |
| **MEOP (with transient margin)** | **3.7 MPa** (peak 3.2 × 1.15) |
| Port/throat at ignition | **5.35** ✅ |
| Case OD / wall | **24 mm / 1.2 mm** 6061-T6 |
| Predicted tube burst | **≈ 28 MPa (7.5 × MEOP)** — 🔴 deviation per §9.4 |
| Closure snap-ring shear | **≈ 22 MPa (5.9 × MEOP)** — the governing weak point |
| Proof pressure | **1.2 × 3.7 = 4.4 MPa** |
| **Stored energy** | `17.2 g × 2.7 kJ/g` = **46 kJ** |

### 11.10 ✅ What is TRUSTWORTHY in §11 and what is NOT

| Item | Status | Why |
|---|---|---|
| **Required total impulse: 24 N·s** | ✅ **TRUSTWORTHY** | From flight mechanics and drag, independent of the burn-rate law |
| Required burnout velocity: ~72 m/s | ✅ **TRUSTWORTHY** | Same |
| **Grain OD: 24 mm** | ✅ **TRUSTWORTHY** | Fixed by the airframe |
| **Freestanding grain configuration** | ✅ **TRUSTWORTHY** | Follows from measured mechanical properties (§7) |
| **Port/throat ≥ 2** | ✅ **TRUSTWORTHY** | Requirement for KNSB's negative erosive burning |
| **Thin primer on core and BOTH end faces** | ✅ **TRUSTWORTHY** | Required by KNSB's ignition behaviour |
| **Inter-segment gap 10–20% of diameter** | ✅ **TRUSTWORTHY** | For multi-segment BATES only; **N/A at one segment** |
| **The design METHOD (§1–§9)** | ✅ **TRUSTWORTHY** | Standard internal ballistics |
| **The conclusion that burn time must be relaxed** | ✅ **TRUSTWORTHY** | Follows from geometry alone, independent of `a` |
| **Throat diameter: 3.9 mm** | 🔴 **NOT TRUSTWORTHY** | Scales as `a^(1/(1−n))` and depends on the assumed `C*` |
| **Burn time: 1.3 s** | 🔴 **NOT TRUSTWORTHY** | Scales as `a^(−1/(1−n))` |
| **Total impulse: 24 N·s** | 🔴 **NOT TRUSTWORTHY** | Scales as `a^(1/(1−n))` |
| **Chamber pressures** | 🔴 **NOT TRUSTWORTHY** | Depend entirely on `a` and `C*` |
| **`C* = 1106 m/s`** | 🟡 **ASSUMED, internally consistent** | ⏳ Pending retrieval of the verified KNSB ideal-performance table |
| **`a = 5.808`, `n = 0.348`** | 🔴 **ILLUSTRATIVE ONLY** | A two-point fit through a **mesa** propellant's endpoints — the exact fit §12.3 invalidates |

---

## 12. Scaling the result — what happens when `a` changes

### 12.1 The sensitivity exponents (memorise these)

**Differentiating the equilibrium equation `P_c = (Kn·a·ρ_p·C*)^(1/(1−n))` and the burn-time integral
`t_b = ∫dw/r` gives three scaling laws that tell you exactly how wrong your design will be when `a` is
wrong:**

$$\boxed{\;P_c \;\propto\; a^{\frac{1}{1-n}}\;}\qquad
\boxed{\;t_b \;\propto\; a^{-\frac{1}{1-n}}\;}\qquad
\boxed{\;I_{\text{tot}} \;\propto\; a^{\frac{1}{1-n}}\;}\qquad\text{(approximately, at fixed geometry)}$$

**At `n = 0.348`, `1/(1−n) = 1.534`:**

| If the true `a` is… | Chamber pressure is… | Burn time is… | Total impulse is… |
|---|---|---|---|
| **as assumed** | 1.00× | 1.00× | 1.00× |
| **10% lower** | **0.86×** | **1.17×** | **0.86×** |
| **25% lower** | **0.65×** | **1.54×** | **0.65×** |
| **40% lower** | **0.46×** | **2.17×** | **0.46×** |
| **10% higher** | 1.16× | 0.86× | 1.16× |
| **25% higher** | 1.52× | 0.66× | 1.52× |

> 🔴 **A 25% error in `a` is a 35% error in chamber pressure and a 54% error in burn time.** And `a`
> depends on **moisture content**, **particle size**, and **grind consistency** — three things that vary
> between your batches and the reference's. **This is not a refinement. This is the design.**
>
> **Note also the direction: a LOWER `a` (which is what as-obtained, undessicated materials give you)
> means LOWER pressure, LONGER burn, and LOWER impulse.** Your motor will **under-perform** its
> prediction, not over-pressurise. **That is the safe direction to be wrong — but a motor that will not
> come up to pressure is also a failed motor.**

### 12.2 Why as-obtained materials give a lower `a`

| Material state | Effect on `a` | Effect on `n` |
|---|---|---|
| **Dessicated sorbitol** (2 days over fresh CaCl₂) | **Higher `a`** | **No change** |
| **As-obtained sorbitol** | **Lower `a`** | **No change** |
| **Fine grind** (20–30 s, 50% < 74 µm) | Higher `a` | No change |
| **Coarse / granular KN** | **Lower `a`** | **No change — and granular KN does not show mesa behaviour** |

**The verified fact:** residual moisture **reduces `a`** and **does not change `n`**. Identical
log-log slopes for fine-dessicated and granular KNSB.

**The consequence, stated as a prediction you can test:** your first strand-burner run will very
probably give an `a` **lower** than 5.808. **That is expected, it is not a mistake, and it is the
number you must design with.** The amount by which it is lower *is* the value of building the strand
burner.

### 12.3 🔴 Why the `a` in §11.2 is ILLUSTRATIVE and must not be used

| Problem | Explanation |
|---|---|
| **1. It is a two-point fit** | Two points determine a line. **Two points cannot detect curvature**, and mesa behaviour *is* curvature. The fit is guaranteed to pass through both anchors and guaranteed to be wrong between them. |
| **2. It spans the mesa region** | The anchors at 0.101 MPa and 6.89 MPa bracket **five decades** of pressure. KNSB's exponent **varies by regime** across that span. A single exponent cannot represent it. |
| **3. It uses dessicated data** | The anchors come from Nakka's careful strand-burner work with dessicated materials and excellent technique. **Your as-obtained materials will give a lower `a`.** |
| **4. `n = 0.348` is at the band edge** | The usable band is 0.3–0.6. **0.348 is 0.048 above the floor.** If the true low-pressure exponent is 0.25, you are below the band, and the motor may chuff or fail to pressurise. **You cannot know which side of the line you are on without measuring.** |
| **5. The reference says so explicitly** | *"A naive single power law through only these two points gives a ≈ 1.99 mm/s/MPaⁿ, n ≈ 0.30. ⚠️ Illustrative only — exactly the single-law fit that mesa behaviour invalidates."* **The source document pre-emptively disowns this calculation.** |

### 12.4 ✅ What must be done before this motor is built

**This list is the gate. There is no partial credit.**

```
================================================================================
 GATE: 24 N.s MOTOR -- MAY NOT BE BUILT UNTIL ALL BOXES ARE TICKED
================================================================================
 [ ] 1. BUILD A STRAND BURNER
        See Motor_Test_Program.md section 4. This is the club's FIRST hardware
        build. It costs less than the motor and it unlocks everything else.

 [ ] 2. MEASURE r(P) FOR OUR MATERIALS
        At least 8-10 pressure points, spanning 0.5 - 6 MPa.
        Use OUR potassium nitrate, OUR sorbitol, OUR grind setting,
        OUR dessication state. Log every parameter.

 [ ] 3. EXTRACT a AND n PER PRESSURE REGIME
        Split the data into 2-3 bands. Fit a power law to EACH band.
        Report R^2 for each fit. Report the residuals.
        DO NOT fit one line through all of it.

 [ ] 4. CONFIRM n IS IN 0.30 - 0.60 IN OUR OPERATING REGIME
        If n < 0.3: expect start-up problems; investigate; consider that the
        motor may need a larger Kn or a bigger igniter.
        If n > 0.6: the motor is closer to unstable than is acceptable.
        If n >= 1.0: DO NOT BUILD. Redesign.

 [ ] 5. CROSS-CHECK a AGAINST A SECOND BATCH
        Same formulation, different day. If a differs by more than 10%,
        your PROCESS is not under control. Fix the process before
        designing a motor around the number.

 [ ] 6. RETRIEVE AND VERIFY C* AND Isp
        From Nakka's techsht-knsb.htm ideal-performance table.
        Confirm the C* is consistent with a physically sensible
        (T_c, gamma, mean molar mass) triplet -- the section 11.7 check.

 [ ] 7. RE-SOLVE THE DESIGN WITH THE MEASURED VALUES
        Redo sections 11.4 - 11.9 with the measured a, n, C*.
        Re-check EVERY acceptance criterion (section 10).
        Expect the throat diameter and burn time to move materially.

 [ ] 8. RE-CHECK THE CASE
        If the new design pressure is HIGHER than 3.7 MPa MEOP,
        the case must be re-analysed and a NEW proof article made.
        A case proof-tested at 4.4 MPa is not qualified for 6 MPa.
================================================================================
```

### 12.5 Design-for-uncertainty — the practical mitigations

**You will not have a perfect `a` on the first try. Design so that being wrong is survivable.**

| Mitigation | How |
|---|---|
| **1. Build adjustability into the throat.** | **Make two or three nozzle inserts with different throat diameters** (e.g. 3.5, 3.9, 4.3 mm) and test the largest first. **Enlarging the throat lowers the pressure** — so start conservative and open up. **You cannot shrink a throat, so make spares.** Cost: a few hundred rupees of graphite. Value: enormous. |
| **2. Design for the LOW-`a` case first.** | Predict the motor with `a` reduced 25%. If it **still** produces useful impulse and comes up to pressure, the design is robust. If it does not, **increase `Kn`** until it does. |
| **3. Keep the MEOP headroom.** | Choose MEOP as peak pressure **×1.15** for transients. **Do not size the case to the nominal.** |
| **4. Test a single-grain "Kn-check" motor first.** | Fire **one** motor with the **smallest propellant mass** that gives a usable pressure trace (e.g. 12 mm grain length). You learn `a` and `n` **in the real motor** from its pressure trace for a fraction of the risk. |
| **5. Measure the throat after machining, every time.** | Pin gauges. Record the actual diameter. Correct the predicted pressure using the measured area. |
| **6. Fire the first motors with a short grain.** | If the pressure is higher than predicted, a short grain limits the total energy released. **Work up.** |

### 12.6 A note on the burn-time integral and why `w/r` is not good enough

**The naive estimate for §11.9:** `t_b = 7.5 mm / r̄`. With `r̄ ≈ 8.5 mm/s`, that gives **0.88 s**.
The integration gives **≈ 1.3 s**. **A 48% error.**

**Why:** `r` at ignition is 7.0 mm/s and `r` at burnout is 9.7 mm/s. The last of the web burns **39%
faster** than the first. Because time is the integral of `1/r`, the slow early portion **dominates**,
and the naive average substantially over-estimates the mean rate.

> **Rule for the club: always integrate. `t_b = w/r̄` is acceptable only as a sanity check, and only
> when you state the `r̄` you used and how you got it.**

---

## 13. Cross-references

| For | See |
|---|---|
| Formulation, particle size, moisture, storage | `Propellant_Formulations.md` |
| **Measuring `a` and `n` yourself** | `Motor_Test_Program.md` §4 |
| Ignition, priming, igniter sizing | `Ignition_System_Design.md` |
| Scale-up gates and schedule | `Propulsion_Roadmap.md` |
| The mesa-propellant warning in full | `Technical_Reference_Nakka.md` §1.11 |
| Grain mechanical properties | `Technical_Reference_Nakka.md` §1.12 |
| The "mountain" pressure curve | `Technical_Reference_Nakka.md` §1.13 |
| Safety rules 1–14 | `Technical_Reference_Nakka.md` Part 2 |

---

*UVCE Rocketry Club — `10_PROPULSION/Motor_Design_Guide.md`. Method is standard internal ballistics.
**The burn-rate coefficient used in §11 is illustrative and is explicitly invalidated in §12.3.** No
throat may be cut until the §12.4 gate is cleared. This document is subordinate to
`40_SAFETY/Safety_Manual_Master.md`.*
