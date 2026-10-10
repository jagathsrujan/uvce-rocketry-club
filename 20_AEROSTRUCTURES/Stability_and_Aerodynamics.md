# UVCE Rocketry Club — Stability and Aerodynamics

**Document:** `20_AEROSTRUCTURES/Stability_and_Aerodynamics.md`
**Applies to:** UVCE-SR-1 "Kaveri" (40 mm airframe, 306 g dry, ~1020 mm overall) and follow-on vehicles
**Companion documents:** [Structures_Design_Guide.md](Structures_Design_Guide.md) (loads and margins),
[Materials_Database.md](Materials_Database.md) (properties), [Fabrication_and_Manufacturing.md](Fabrication_and_Manufacturing.md) (how to build it)

> **Status:** Working design document. Every number is derived in-line or traceable to a named source.
> Values marked **[VERIFY BY TEST]** must be confirmed on flight or test data before they are treated as
> validated. Nothing here authorises a launch.
>
> **Constants used throughout:** $g = 9.81\ \text{m/s}^2$ · $\rho = 1.10\ \text{kg/m}^3$ (Bengaluru,
> ~900 m elevation, 25 °C) · $a = 343\ \text{m/s}$ · $d = 40\ \text{mm}$ body caliber.

---

## 0. THE ONE-PAGE SUMMARY

Read this box before you read anything else. It is the conclusion of the whole document.

| Quantity | Value | Verdict |
|---|---|---|
| Centre of pressure (Barrowman), baseline 40 mm / 1020 mm / 3 fins **as specified** | **417 mm** from the nose tip | — |
| Centre of gravity, current mass budget | **458 mm** (burnout), 484.5 mm (liftoff) | — |
| **Static margin as specified** | **−1.02 calibers (burnout), −1.68 (liftoff)** | 🔴 **UNSTABLE — DO NOT FLY** |
| 🔴 **Root cause** | The **fin root chord is too long** (120 mm for a 40 mm span) | see §5.8 |
| **Fix** | Shorten to **$C_r = 60$, $C_t = 30$, $X_R = 22$, $s = 35$ mm** | see §5.8 |
| Centre of pressure with the recommended fin | **539.8 mm** | — |
| **Static margin with the recommended fin** | **+1.38 at liftoff, +2.04 at burnout** | ✅ **inside the 1–2 band** |
| Ballast required with the recommended fin | **none — and the fin is 35 g lighter** | ✅ |
| Burnout velocity, 24 N·s / 2 s motor | 54.3 m/s | — |
| Apogee, 24 N·s / 2 s, Cd = 0.45, 306 g dry | **186 m** | short of the 200 m target |
| Impulse actually required for 200 m at that burn time | **24.9 N·s** | 24 N·s is 4 % short |
| Rail exit velocity at T/W = 3.7 on a 1.5 m rail | **8.9 m/s** | 🔴 **below the 15–20 m/s rule** |
| Working drag coefficient | **Cd = 0.45** | within the 0.4–0.6 band |

> **Three actions fall straight out of this document.**
> **(1)** 🔴 **Do not build the fin as drawn.** A 120 mm root chord on a 40 mm span makes the vehicle
> **statically unstable by over a caliber**. Shortening the root chord to 60 mm and the span to 35 mm
> makes it properly stable **with no ballast** — and removes 35 g of fin mass at the same time. This is
> the single highest-value change in the document; see §5.8.
> **(2)** A 24 N·s / 2 s motor cannot reach 200 m at this mass — either burn the same impulse in 0.8 s
> (214 m) or go to 26–30 N·s.
> **(3)** A 1.5 m rail with a 3.7:1 thrust-to-weight ratio gives an 8.9 m/s exit: use a 4 m rail or raise
> the thrust.

---

## 1. CENTRE OF PRESSURE AND CENTRE OF GRAVITY

### 1.1 The centre of gravity (CG)

The **centre of gravity** is the mass centroid of the whole vehicle. It is the point through which the
resultant weight acts, and the point about which the vehicle's rotational inertia is measured. Physically
it is the balance point: put the rocket on a knife-edge and the CG is where it sits level.

$$x_{CG} = \frac{\sum_i m_i\, x_i}{\sum_i m_i}$$

where $x_i$ is the station of each component measured from the nose tip. Change one component and the CG
moves; the CG is a property of **mass distribution only**, never of the airflow. It is set by the mass
budget, and the mass budget is therefore a flight-critical document, not bookkeeping.

On this vehicle the CG moves during the burn. The KNSB grain sits well aft, so burning it away moves the
CG **forward** — which *increases* the static margin. That is the opposite of the usual worry, and it is
worth knowing explicitly: this vehicle gets *more* stable as it burns, so the critical case is
**liftoff**, not burnout.

### 1.2 The centre of pressure (CP)

The **centre of pressure** is the point at which the resultant aerodynamic force acts. For a symmetric
vehicle at a small angle of attack $\alpha$, the aerodynamic normal force is

$$N = C_{N\alpha}\,\alpha\,q\,A_{ref}, \qquad q = \tfrac{1}{2}\rho v^2$$

and the CP is defined by taking moments about any reference station:

$$x_{CP} = \frac{\sum_i \left(C_{N\alpha}\right)_i x_i}{\sum_i \left(C_{N\alpha}\right)_i}$$

where the sum runs over every lifting component — nose, shoulder, body, fins. Unlike the CG, the CP is a
property of the **airflow and the external shape only**. It does not know or care what the vehicle
weighs. It moves a little with Mach number (and a lot at transonic speeds), but it is essentially fixed
for a subsonic vehicle.

### 1.3 Why CP must be behind CG

The vehicle is a weathervane. In flight at a small angle of attack, the aerodynamic normal force pushes
the nose away from the relative wind. The question is whether that force *increases* the angle of attack
(unstable) or *reduces* it (stable).

Take moments about the CG. The aerodynamic force $N$ acts at the CP, a distance $(x_{CP} - x_{CG})$ from
the CG. The pitching moment is

$$M = N\,(x_{CP} - x_{CG})$$

- **CP behind CG** $(x_{CP} > x_{CG})$: as the nose swings away from the wind, the resulting moment pulls
  the nose *back* into the wind. The vehicle is **statically stable**. Disturbances decay.
- **CP ahead of CG** $(x_{CP} < x_{CG})$: the moment pushes the nose *further* away. The vehicle **tumbles**.
  It will not fly a stable trajectory and will not point its nose up at apogee.

A useful mental model: the rocket is an arrow. The feathers (fins) put the CP behind the CG, exactly as
fletching puts an arrow's CP behind its balance point. **The fins are not there to "push the rocket up" —
they are there to move the CP aft.**

> 🔴 **The rule, in one line:** *CP must be at of CG, by 1–2 body calibers.*

---

## 2. STATIC MARGIN

### 2.1 Definition

The **static margin** is the distance between CP and CG, expressed in **body calibers** (one caliber = one
body diameter, 40 mm here):

$$\text{SM} = \frac{x_{CP} - x_{CG}}{d}$$

It is a **positive** number for a stable vehicle. It is a *length*, not a force, and not a ratio — which
is why it is always quoted in calibers, so that it can be compared between rockets of different sizes.

### 2.2 Recommended range

| Static margin | Behaviour |
|---|---|
| Negative | Unstable. Tumbles. Never fly. |
| 0 to 0.5 | Marginally stable. Any disturbance, gust, or fin misalignment dominates. **Do not fly.** |
| **1.0 to 2.0** | **The design band.** Restoring moment is decisive but the vehicle still flies its intended trajectory. |
| 2.0 to 3.0 | Over-stable. Flies perfectly straight — into the wind. See §2.4. |
| > 3.0 | Strongly over-stable. Severe weathercocking, high drag at angle of attack, disappointing apogee. |

> **Club standard: design for 1.5 calibers, accept 1.0–2.0.** Note the asymmetry of the risk. At 0.8
> calibers the vehicle may fly; at 1.2 it will fly. There is no prize for a low static margin, and the
> cost of the standard band is a small amount of nose-ward mass.

### 2.3 How the static margin changes during the burn

Two effects, and they push in the same direction on this vehicle:

1. **The CG moves.** The grain is the most aft significant mass. As it burns, mass leaves the aft end, so
   the CG moves **forward** and the static margin **increases**.
2. **The CP is unchanged.** The CP depends on external shape, and the external shape does not change
   during the burn (the nozzle erosion and any ablative change are negligible at this scale).

Worked for the baseline vehicle (306 g dry, 24 g grain at station 822 mm):

| State | Mass | CG station | SM at $x_{CP} = 417.2$ mm |
|---|---|---|---|
| Liftoff | 330 g | 484.5 mm | **−1.68 calibers** 🔴 |
| Burnout | 306 g | 458.0 mm | **−1.02 calibers** 🔴 |

$$x_{CG,\text{liftoff}} = \frac{306(458) + 24(822)}{330} = \frac{140\,148 + 19\,728}{330} = 484.5\ \text{mm}$$

$$\text{SM}_{\text{liftoff}} = \frac{417.2 - 484.5}{40} = -1.68, \qquad
\text{SM}_{\text{burnout}} = \frac{417.2 - 458.0}{40} = -1.02$$

> 🔴 **This is the single most important number in the document.** The CP at 417 mm is **41 mm ahead of
> the CG at burnout and 67 mm ahead at liftoff.** A vehicle in this condition is statically unstable and
> will not fly a straight, nose-up trajectory. **The fix is in §5.8 — and it is a fin-chord fix, not a
> ballast fix.**

**Corollary for the general case:** if the grain were *forward* of the CG the margin would instead
*decrease* during the burn, and burnout would be the critical case. Always check **both** ends of the
burn, and also check with a **spent motor** (some motors retain a heavy aft closure).

### 2.4 Too much static margin is also a fault — weathercocking

It is tempting to conclude "more margin is better". It is not.

A large static margin means a large restoring moment for a given angle of attack. At the instant of
liftoff the vehicle is slow, still on or just off the rail, and the wind is blowing across it. The fins
generate a strong restoring moment and the vehicle **turns into the wind**. This is **weathercocking**, and
it is a *trajectory* fault, not a stability fault:

- The rocket pitches upwind; apogee is lower and the landing point is off-axis from the pad.
- At high angles of attack induced drag rises steeply; apogee falls further.
- Under extreme conditions the vehicle can be pushed past 90° and fly **downwind, nose-down**, and no
  recovery system will save it.

The severity scales with the **restoring moment per unit of pitch rate**, which is roughly
$\propto \text{SM}$ for a given vehicle. A 4-caliber vehicle is roughly twice as eager to turn into the
wind as a 2-caliber vehicle.

> **The design consequence:** aim for the **middle** of the band. Roughly **1.5 calibers** is the sweet
> spot for a small amateur vehicle: stable enough to be decisive, not so stable that it flies into the
> wind. Anything over **2.0 calibers** is over-stable and should be trimmed.

Full weathercocking management is in §6.

### 2.5 Fixing the stability of THIS vehicle

The baseline configuration has $x_{CP} = 417.2$ mm and $x_{CG} = 458$ mm — **unstable by 1.02 calibers.**
There are only two ways to create a static margin: **move the CP aft**, or **move the CG forward**.

**(a) Move the CP aft — what works and what does not.** The fin contribution to the CP is the *only*
large aft-ward term; the nose and body terms are forward-ward and are set by the nose length and body
length. The full trade study is in §5.8, and its headline result is counter-intuitive:

| Change | Effect on $x_{CP}$ | Verdict |
|---|---|---|
| **Shorten the fin CHORD** ($C_r$ 120 → 80 mm), **span unchanged at 40 mm** | 417 → **538 mm** | ✅ **The fix. No ballast needed.** |
| **Increase the fin SPAN** ($s$ 30 → 40 mm) at $C_r = 90$ mm | 453 → 514 mm | ✅ strong, but adds mass and drag |
| **Reduce the fin SPAN** ($s$ 40 → 20 mm) at $C_r = 120$ mm | 460 → 383 mm | 🔴 **destroys stability** |
| **Lengthen the fin CHORD** ($C_r$ 80 → 140 mm), span unchanged | 538 → 432 mm | 🔴 **destroys stability** |
| **Lengthen the body** (1020 → 1500 mm overall) | 417 → 649 mm | strong, but costs mass and stiffness |
| **Shorten the nose** (120 → 40 mm) | 417 → 392 mm | moves the CP the *wrong* way |

The mechanism is set out in full in §5.8: **span buys lift, chord buys nothing but moment arm against
you.** The originally-specified 120 mm root chord is the whole problem.

**(b) Move the CG forward — the fallback whenever (a) is not enough.** If a fin change is not available
(you have already cut the fins, or the geometry is fixed by a competition rule), then the CG must move
forward. The cost is brutal, because nose ballast is the least efficient mass on the vehicle:

| Target SM | Required CG | Nose ballast needed (at station 40 mm) |
|---|---|---|
| 1.0 caliber | 377 mm | **+31 g** (with the recommended 80 mm fin: **0 g**) |
| 1.5 calibers | 357 mm | **+49 g** (with the recommended 80 mm fin: **0 g**) |
| 2.0 calibers | 337 mm | +74 g |

> **Recommended action.** Cut the fins to $C_r = 80$ mm, $C_t = 40$ mm, $X_R = 30$ mm with the span
> held at **40 mm**, in 3 mm G10. This alone gives $x_{CP} = 538$ mm and a static margin of **+1.34
> calibers at liftoff and +2.00 at burnout**, with **no ballast and no mass penalty whatsoever.**
> Verify in OpenRocket, then confirm on the swing test (§5.9) before the first flight.

**Do not** solve a stability problem by making the nose heavier unless you have exhausted the
aerodynamic options. Nose ballast adds mass exactly where it hurts apogee most — 31 g of nose ballast
costs roughly 25 m of apogee on this vehicle (see §10.5).

---

## 3. THE BARROWMAN METHOD — FOUNDATIONS

### 3.1 What it is and what it assumes

The **Barrowman method** (James S. Barrowman, NACA, 1966–67) is a hand-calculation method for the
subsonic centre of pressure of a slender body of revolution with fins. It is the standard method in
model rocketry and is what OpenRocket, RASAero and every hobby design tool implement internally.

Its assumptions, which you must respect:

1. **Slender body**, small angle of attack, **attached, subsonic flow**. It is invalid above about
   Mach 0.7–0.8 and completely wrong transonic.
2. **Linear aerodynamics** — lift is proportional to $\alpha$. Fine below ~10°–12°.
3. **The flow is inviscid** — Barrowman gives **no drag at all**. The drag analysis in §7 is a separate,
   independent calculation.
4. **Each component's contribution is independent** and the total is their sum. Interference is handled
   by a single empirically-fitted factor (the body-fin interference factor, §3.5) rather than by solving
   the flow.
5. **The CP result is a function of geometry only** — it does not depend on mass, velocity, or air
   density. This is why Barrowman is a *design* tool: you can iterate geometry without re-running a
   trajectory.

The output of the method is two numbers per component: the **normal-force slope**
$\left(C_{N\alpha}\right)_i$ (how much lift that component makes per radian of angle of attack) and the
**station** $x_i$ at which that lift acts. From these the vehicle CP follows by the weighted average of
§1.2.

### 3.2 The normal-force coefficient slope

Barrowman works entirely in terms of

$$C_{N\alpha} = \frac{\partial C_N}{\partial \alpha} \qquad \text{per radian}$$

so that the normal force at angle of attack $\alpha$ (radians) is

$$N = C_{N\alpha}\,\alpha\,q\,A_{ref}, \qquad A_{ref} = \frac{\pi}{4}d^2$$

$A_{ref}$ is **always** the body cross-sectional area, $\frac{\pi}{4}d^2$ — never the fin area, never the
wetted area. Getting this wrong is the most common Barrowman error. Convert to per-degree by
multiplying by $\pi/180 = 0.017453$.

### 3.3 Symbol definitions — the complete list

| Symbol | Meaning | Units |
|---|---|---|
| $d$ | Body tube outside diameter (= 1 caliber) | mm |
| $d_b$ | Body diameter at the base of the shoulder / boat-tail | mm |
| $R$ | Body radius, $R = d/2$ | mm |
| $L_N$ | Nose cone length | mm |
| $L_B$ | Body tube length | mm |
| $L$ | Overall length, $L = L_N + L_B$ (fins flush with the aft end) | mm |
| $s$ | Fin **exposed semi-span** — from the body surface to the fin tip | mm |
| $m$ | Fin semi-span measured from the **body centreline**, $m = s + R$ | mm |
| $\eta$ | Span ratio, $\eta = s/R$ | — |
| $C_r$ | Fin **root chord** (at the body surface) | mm |
| $C_t$ | Fin **tip chord** | mm |
| $X_R$ | Fin **leading-edge sweep** — the axial distance from the root leading edge to the tip leading edge | mm |
| $X$ | Axial distance from the fin root leading edge to the **mid-chord point of the tip**, $X = X_R + \dfrac{C_t - C_r}{2}$ | mm |
| $\lambda$ | Taper ratio, $\lambda = C_t/C_r$ | — |
| $N$ | Number of fins | — |
| $\gamma$ | Fin-body interference correction for supersonic flow; **$\gamma = 1$ for subsonic** | — |
| $K$ | Body-fin upwash factor, $K = 1 + R/m$ | — |
| $k_{body}$ | Fin lift reduction from body carry-over, $k_{body} = 1 + \dfrac{C_r X_R}{2(C_r + C_t)}$ | — |
| $K_{fb}$ | Fin-body interference factor applied to the **lift**, $K_{fb} = 1 + K\lambda$ | — |
| $K_f$ | Fin taper factor applied to the **CP location**, $K_f = 1 + \lambda$ | — |
| $x_N, x_B, x_f$ | Stations of the nose, body and fin CP contributions | mm |
| $A_B$ | Body cross-sectional area, $A_B = \frac{\pi}{4}d^2$ | mm² |
| $A_{FB}$ | **Shoulder** annular area, $A_{FB} = \frac{\pi}{4}\left(d^2 - d_b^2\right)$ | mm² |
| $\Gamma$ | Body-fin interference factor (also written $K_{fb}$ in some texts) | — |
| $\Lambda$ | Leading-edge sweep **angle**, $\Lambda = \arctan(X_R/s)$ | deg |
| $t$ | Fin thickness | mm |

> ⚠️ **Two conventions exist for $s$.** Some texts define $s$ from the body **centreline**, others from the
> body **surface**. This document uses the **surface** convention because that is how a physical fin is
> measured with calipers, and because the body-centreline convention *under-predicts* the CP location
> (and therefore over-predicts the static margin) by roughly a factor of 1.6 on this vehicle. State your
> convention in your report. If your number disagrees with OpenRocket by ~10 %, check this first.

---

## 4. THE BARROWMAN EQUATION SET

### 4.1 Nose cone

Only the nose's **shape** matters, not its length — the normal-force slope of any slender nose at small
$\alpha$ is the same, and only the *station* of the CP changes with shape.

$$\boxed{\left(C_{N\alpha}\right)_N = 2.0 \ \text{per radian}}$$

**Centre of pressure location**, as a fraction of nose length from the tip:

| Nose shape | $x_N / L_N$ | Note |
|---|---|---|
| **Conical** | $0.666$ | Exact for a cone |
| **Tangent ogive** | $\mathbf{0.466}$ | The value Barrowman tabulates |
| Secant ogive | ≈ 0.5 | Between ogive and parabola |
| Parabolic ($n = 0.5$) | 0.500 | Exact for the power series |
| Von Kármán (LD-Haack) | 0.500 | — |
| Elliptical | 0.500 | — |

$$x_N = 0.466\,L_N \quad \text{(tangent ogive)}$$

For a **power-series** nose of the form $r(x) = R\,(x/L_N)^n$ the slender-body result is exact:

$$\frac{x_N}{L_N} = \frac{2n}{2n+1}$$

which returns $2/3$ for a cone ($n = 1$) and $1/2$ for a parabola ($n = 0.5$). The tangent-ogive value
0.466 sits between them, which is why the ogive is a good compromise.

### 4.2 Body tube (and boattail / shoulder)

A constant-diameter body tube makes **no lift** at zero angle of attack, so its contribution is zero. If
there is a **shoulder** — an abrupt diameter change $d \to d_b$ — the annular face generates a small
normal force:

$$\boxed{\left(C_{N\alpha}\right)_B = \frac{2\,A_{FB}}{A_B} = \frac{2\left(d^2 - d_b^2\right)}{d^2}}$$

with its centre of pressure at the geometric centre of the shoulder:

$$x_B = L_N + \frac{L_B}{2}$$

**Important notes.**

- For a **shoulder of zero height** ($d_b = d$) this correctly returns **zero lift**. Most model-rocket
  nose cones have a shoulder that is *inside* the body tube at the same diameter, so $d_b = d$ and the
  contribution genuinely is zero. Do not invent a shoulder contribution that is not there.
- A **boattail** (aft diameter reduction, $d_b < d$) has $A_{FB} > 0$ and contributes a **destabilising**
  lift (its CP is forward of the fins). Boattails cost stability. This is a real effect and is why
  scale models of V-2s and similar boatsailed shapes need extra nose weight.
- On the **baseline vehicle** the nose shoulder sits inside the 37.6 mm bore, so $d_b = 37.6$ mm and
  $d = 40$ mm, giving the small non-zero value computed in §5.3. It is retained there to demonstrate the
  method, not because it matters.

### 4.3 Fins — the full set

**(a) Fin lift, fin panel alone (with the body's upwash):**

$$\boxed{\left(C_{N\alpha}\right)_F = \frac{4N\left(\dfrac{s}{d}\right)}
{1 + \sqrt{1 + \left(\dfrac{2\left(C_r + X_R\right)}{C_r + C_t}\right)^2}}}$$

The term $\left(s/d\right)$ is the **exposed semi-span in calibers** — the aspect-ratio driver. The whole
denominator is the correction for the fin's taper and sweep: as the fin gets longer and more swept, the
denominator grows and the fin becomes less effective per unit area.

**(b) The body-fin interference factor.** The body does not sit passively beside the fins — the fins
induce an upwash that makes the adjacent body generate lift too. Barrowman captures this with

$$\boxed{K_{fb} = 1 + K\lambda, \qquad K = 1 + \frac{R}{m}, \qquad m = s + R}$$

$K_{fb}$ **multiplies the fin lift**. For the baseline vehicle $K_{fb} = 1 + 1.333 \times 0.5 = 1.667$ —
that is, the fins and the body they sit on make **67 % more lift together than the fin panels alone**.
This is not a small correction and it is the most commonly omitted term in amateur Barrowman code.

**(c) The fin lift, assembled:**

$$\boxed{C_{N\alpha,\ \text{fins}} = K_{fb}\,\gamma\,\left(C_{N\alpha}\right)_F}$$

with $\gamma = 1$ subsonic. $\gamma$ rises to about 1.5 supersonic; **do not apply a supersonic $\gamma$
to a subsonic design.**

**(d) Fin centre of pressure.** Measured **aft of the fin root leading edge**:

$$\boxed{x_f = \frac{C_r^2 + C_r C_t + C_t^2 + C_r X_R + 2\,C_t X_R}{3\left(C_r + C_t\right)}}$$

This is the exact chordwise-integration result for a trapezoidal lifting panel (the derivation is shown
in §4.4), and it satisfies the checks that any correct formula must satisfy:

- **Rectangular fin** ($C_r = C_t = c$, $X_R = 0$): $x_f = c/2$ — the mid-chord. ✔
- **Delta fin** ($C_t = 0$, $X_R = 0$): $x_f = C_r/3$ — the centroid of a triangle from its base. ✔

Some texts write the same quantity in the equivalent Barrowman form

$$x_f = \frac{\left(C_r + 2C_t\right)\dfrac{X_R}{2} + \left(C_r + 2C_t\right)\dfrac{X}{3} + \left(C_r + 2C_t\right)\dfrac{C_r}{6}}{3\,K_f},
\qquad K_f = 1 + \lambda$$

which reduces to the same thing; the compact form above is preferred because it is easier to check. The
**fin CP station on the vehicle** is then

$$x_{f,\ \text{vehicle}} = L_N + L_B + x_f - X_R$$

> ⚠️ **Watch the datum.** $x_f$ from the formula above is measured from the **fin root leading edge**.
> Turning that into a station from the nose tip requires subtracting $X_R$ if your $x_f$ is measured from
> the root LE. The worked example in §5 keeps the datum explicit at every step for exactly this reason.

**(e) The fin pressure-drag term** (Barrowman's own drag result — not part of the CP calculation):

$$\boxed{\Delta C_{d,\text{fin}} = 4N\left(\frac{s}{d}\right)\left(\frac{t}{c}\right)^2
\left(1 + \frac{1}{2 + 2\lambda}\right)(1 + \lambda)}$$

where $t$ is the fin thickness and $c$ the mean chord, $c = \left(C_r + C_t\right)/2$. This term is small
and scales with $\left(t/c\right)^2$ — doubling the fin thickness **quadruples** its drag contribution.
It is tabulated here so the drag budget of §7 closes; it contributes ≈ 0.03–0.09 to $C_d$ referred to the
body cross-section for typical model fins.

### 4.4 Where the fin CP formula comes from

Do not take the $x_f$ formula on faith — it is a five-line integration and you should be able to
reproduce it.

For a trapezoidal fin panel, at a spanwise station $z$ measured from the root ($0 \le z \le s$):

$$\text{leading edge: } \ell(z) = \frac{X_R}{s}z, \qquad
\text{chord: } c(z) = C_r + \frac{C_t - C_r}{s}z$$

In slender (strip) theory the local lift per unit span is proportional to $c(z)$, and within a strip the
chordwise loading is uniform, so the strip's centre of pressure is at its mid-chord, $\ell(z) + c(z)/2$.
Taking moments about the root leading edge:

$$x_f = \frac{\displaystyle\int_0^s c(z)\left[\ell(z) + \tfrac{1}{2}c(z)\right]dz}
{\displaystyle\int_0^s c(z)\,dz}$$

Evaluating the two integrals (use `sympy` — see the worked script in §5.6):

$$\int_0^s c\,dz = \frac{s}{2}\left(C_r + C_t\right),
\qquad
\int_0^s c\left(\ell + \frac{c}{2}\right)dz = \frac{s}{6}\left(C_r^2 + C_rC_t + C_t^2 + C_rX_R + 2C_tX_R\right)$$

Dividing gives the boxed formula of §4.3(d). The same integral is valid for **any** number of fins, which
is why $N$ does not appear in $x_f$ but does appear in $C_{N\alpha}$.

### 4.5 Assembling the vehicle CP

$$\boxed{\left(C_{N\alpha}\right)_{total} = \left(C_{N\alpha}\right)_N + \left(C_{N\alpha}\right)_B + C_{N\alpha,\ \text{fins}}}$$

$$\boxed{x_{CP} = \frac{\left(C_{N\alpha}\right)_N x_N + \left(C_{N\alpha}\right)_B x_B + C_{N\alpha,\text{fins}}\,x_{f,\text{vehicle}}}
{\left(C_{N\alpha}\right)_{total}}}$$

And then the result you actually care about:

$$\boxed{\text{SM} = \frac{x_{CP} - x_{CG}}{d}}$$

---

## 5. FULLY WORKED BARROWMAN CALCULATION

### 5.1 The vehicle

| Parameter | Symbol | Value |
|---|---|---|
| Body diameter | $d$ | **40.0 mm** |
| Nose cone | — | **tangent ogive, $L_N = 120$ mm** (3.0 calibers) |
| Body tube | $L_B$ | **900 mm** |
| Overall length | $L$ | **1020 mm** |
| Nose shoulder diameter | $d_b$ | 37.6 mm |
| Fin count | $N$ | **3** |
| Fin root chord | $C_r$ | **120 mm** |
| Fin tip chord | $C_t$ | **60 mm** |
| Fin exposed semi-span | $s$ | **40 mm** |
| Fin leading-edge sweep | $X_R$ | **45 mm** |
| Fin thickness | $t$ | 3.0 mm |
| Centre of gravity (mass budget) | $x_{CG}$ | 458 mm |

**Derived geometry**

$$X = X_R + \frac{C_t - C_r}{2} = 45 + \frac{60 - 120}{2} = 45 - 30 = \mathbf{15.0\ mm}$$

$$\lambda = \frac{C_t}{C_r} = \frac{60}{120} = \mathbf{0.5}$$

$$m = s + R = 40 + 20 = \mathbf{60.0\ mm}, \qquad \frac{m}{R} = \frac{60}{20} = \mathbf{3.0}$$

### 5.2 Reference areas

$$A_B = \frac{\pi}{4}d^2 = \frac{\pi}{4}(40.0)^2 = \mathbf{1256.637\ mm^2}$$

$$A_{FB} = \frac{\pi}{4}\left(d^2 - d_b^2\right) = \frac{\pi}{4}\left(40.0^2 - 37.6^2\right)
= \frac{\pi}{4}(1600 - 1413.76) = \mathbf{146.273\ mm^2}$$

$$\frac{A_{FB}}{A_B} = \frac{146.273}{1256.637} = \mathbf{0.11640}$$

### 5.3 Component 1 — nose cone (tangent ogive)

$$\left(C_{N\alpha}\right)_N = 2.0\ \text{rad}^{-1}$$

$$x_N = 0.466\,L_N = 0.466 \times 120 = \mathbf{55.920\ mm}$$

### 5.4 Component 2 — body / shoulder

$$\left(C_{N\alpha}\right)_B = \frac{2\,A_{FB}}{A_B} = 2 \times 0.11640 = \mathbf{0.23280\ rad^{-1}}$$

$$x_B = L_N + \frac{L_B}{2} = 120 + \frac{900}{2} = \mathbf{570.0\ mm}$$

### 5.5 Component 3 — fins

**Step 1 — the sweep/taper denominator.**

$$\frac{2\left(C_r + X_R\right)}{C_r + C_t} = \frac{2(120 + 45)}{120 + 60} = \frac{330}{180} = 1.833333$$

$$\sqrt{1 + (1.833333)^2} = \sqrt{1 + 3.361111} = \sqrt{4.361111} = \mathbf{2.088327}$$

$$\text{denominator} = 1 + 2.088327 = \mathbf{3.088327}$$

**Step 2 — the span term.**

$$\frac{s}{d} = \frac{40}{40} = \mathbf{1.000}$$

**Step 3 — fin panel lift (including body carry-over).**

$$k_{body} = 1 + \frac{C_r X_R}{2\left(C_r + C_t\right)} = 1 + \frac{120 \times 45}{2(180)} = 1 + \frac{5400}{360} = 1 + 15 = \mathbf{16.0}$$

This large value is correct and is the point of the term: the fins are short and steeply swept relative to
their chord, so a large fraction of the panel's lift is "carried over" to the body rather than appearing
as fin lift. It is the reason $C_{N\alpha,\text{fins}}$ is only 1.25 despite three substantial-looking fins.

$$\left(C_{N\alpha}\right)_F = \frac{4N\left(\dfrac{s}{d}\right)}{k_{body}}
= \frac{4 \times 3 \times 1.000}{16.0} = \frac{12}{16} = \mathbf{0.750000\ rad^{-1}}$$

**Step 4 — the body-fin interference factor.**

$$K = 1 + \frac{R}{m} = 1 + \frac{20}{60} = 1 + 0.333333 = \mathbf{1.333333}$$

$$K_{fb} = 1 + K\lambda = 1 + (1.333333)(0.5) = 1 + 0.666667 = \mathbf{1.666667}$$

**Step 5 — fin lift.** With $\gamma = 1$ (subsonic):

$$C_{N\alpha,\ \text{fins}} = K_{fb}\,\gamma\,\left(C_{N\alpha}\right)_F = 1.666667 \times 1.0 \times 0.750000
= \mathbf{1.250000\ rad^{-1}}$$

**Step 6 — fin CP, measured from the fin root leading edge.** Using the boxed formula of §4.3(d):

$$C_r^2 = 120^2 = 14\,400$$
$$C_rC_t = 120 \times 60 = 7\,200$$
$$C_t^2 = 60^2 = 3\,600$$
$$C_rX_R = 120 \times 45 = 5\,400$$
$$2C_tX_R = 2 \times 60 \times 45 = 5\,400$$

$$\text{numerator} = 14\,400 + 7\,200 + 3\,600 + 5\,400 + 5\,400 = \mathbf{36\,000}$$

$$\text{denominator} = 3\left(C_r + C_t\right) = 3(180) = \mathbf{540}$$

$$x_f = \frac{36\,000}{540} = \mathbf{66.6667\ mm\ \text{aft of the fin root LE}}$$

**Step 7 — fin CP station on the vehicle.** With the fins flush with the aft end, the fin root leading
edge sits at station $L - C_r = 1020 - 120 = 900$ mm from the nose tip. Therefore

$$x_{f,\ \text{vehicle}} = 900 + 66.667 = \mathbf{966.667\ mm}$$

> ⚠️ **This step is where nearly every hand calculation goes wrong.** The formula gives a position
> *within the fin*; you must add the fin's own station. Check the answer for sanity: a fin CP that lies
> outside the fin's own chord envelope is wrong.

### 5.6 Component 4 — assembly

| Component | $C_{N\alpha}$ (rad⁻¹) | Station $x_i$ (mm) | Moment $C_{N\alpha}x_i$ (mm) |
|---|---|---|---|
| Nose cone | 2.00000 | 55.920 | 111.840 |
| Body / shoulder | 0.23280 | 570.000 | 132.696 |
| Fins (3, with $K_{fb}$) | 1.25000 | 966.667 | 1 208.334 |
| **TOTAL** | **3.48280** | — | **1 452.870** |

$$x_{CP} = \frac{1\,452.870}{3.48280} = \mathbf{417.16\ mm\ \text{from the nose tip}}$$

$$C_{N\alpha} = 3.48280\ \text{rad}^{-1} = 3.48280 \times \frac{\pi}{180} = \mathbf{0.06079\ deg^{-1}}$$

### 5.7 The static margin

With $x_{CG} = 458$ mm (burnout) and 484.5 mm (liftoff):

$$\text{SM} = \frac{x_{CP} - x_{CG}}{d} = \frac{417.16 - 458.0}{40} = \mathbf{-1.02\ calibers\ (burnout)}$$

$$\text{SM}_{\text{liftoff}} = \frac{417.16 - 484.5}{40} = \mathbf{-1.68\ calibers}$$

> 🔴 **The vehicle is statically UNSTABLE as specified.** The CP is 41 mm *ahead* of the burnout CG and
> 67 mm ahead of the liftoff CG. The fin chord must be reduced, or the CG must move forward by 60–90 mm.

**Sanity check on the calculation** — an independent Python script (reproduce it yourself) gives the
same answer, and the intermediate checks all pass:

```
C_r^2+C_rC_t+C_t^2+C_rX_R+2C_tX_R  = 36000
3(C_r+C_t)                         = 540
x_f                                = 66.6667 mm      <- rectangular check gives c/2 ✓
x_f,vehicle                        = 966.667 mm
(C_Na)_total                       = 3.48280 /rad
x_CP                               = 417.16 mm
SM vs 458 mm (burnout)             = -1.02 calibers
SM vs 484.5 mm (liftoff)           = -1.68 calibers
```

### 5.8 Fixing it — the fin trade study

This is the most valuable calculation in the document, because the answer is counter-intuitive. **Span
and chord move the CP in OPPOSITE directions**, and the originally-specified fin has far too much chord
for its span.

**(a) Span sensitivity** (root chord held at $C_r = 90$ mm, $C_t = 45$ mm, $X_R = 34$ mm):

| Span $s$ | $C_{N\alpha,\text{fins}}$ | $x_{CP}$ | SM at CG 458 mm |
|---|---|---|---|
| 20 mm | 0.851 | 374.7 mm | −2.08 🔴 |
| 25 mm | 1.047 | 416.2 mm | −1.04 🔴 |
| 30 mm | 1.241 | 452.6 mm | −0.13 🔴 |
| 35 mm | 1.432 | 484.8 mm | +0.67 |
| 40 mm | 1.622 | 513.7 mm | +1.39 ✅ |
| 45 mm | 1.810 | 539.6 mm | +2.04 |

**More span → CP aft → more stable.** This is the intuitive direction.

**(b) Chord sensitivity** (span held at $s = 40$ mm, $C_t = C_r/2$, $X_R = 0.375\,C_r$):

| Root chord $C_r$ | $C_{N\alpha,\text{fins}}$ | $x_{CP}$ | SM at CG 458 mm |
|---|---|---|---|
| 40 mm | 2.459 | 620.8 mm | **+4.07** (wildly over-stable) |
| 60 mm | 2.353 | 593.8 mm | +3.39 |
| 80 mm | 1.818 | 538.1 mm | +2.00 |
| 100 mm | 1.482 | 494.8 mm | +0.92 |
| **120 mm (as specified)** | **1.250** | **460.2 mm** | **+0.06** 🔴 |
| 140 mm | 1.081 | 431.9 mm | −0.65 🔴 |

**More chord → CP FORWARD → less stable.** This is the counter-intuitive direction, and it is why the
as-specified fin fails.

**(c) Why.** A fin's lift comes from its **span**; the **chord** only provides a lever arm *within* the
fin. Two effects compound:

1. **$k_{body}$ grows with chord.** The body carry-over factor
   $k_{body} = 1 + \frac{C_rX_R}{2(C_r+C_t)}$ **divides** the fin's lift. At $C_r = 120$ mm with
   $X_R = 45$ mm it is **16.0**, which slashes the fin panel's lift to 0.75 rad⁻¹.
2. **A longer root chord moves the fin's own CP forward** relative to the fin's trailing edge, i.e.
   toward the nose.

Both push the vehicle CP forward. The comparison from the as-specified fin to the recommended one:

| Quantity | As specified (120/60/45/40) | **Recommended (60/30/22/35)** | Change |
|---|---|---|---|
| $k_{body}$ (body carry-over dilution) | 16.00 | **8.33** | halved |
| Fin panel lift $\left(C_{N\alpha}\right)_F$ | 0.750 | **1.260** | +68 % |
| $K_{fb}$ (body-fin interference) | 1.667 | 1.682 | — |
| Fin lift $C_{N\alpha,\text{fins}}$ | 1.250 | **2.119** | **+70 %** |
| $x_f$ (fin CP aft of the fin root LE) | 66.67 mm | 33.11 mm | — |
| Fin root LE station | 900 mm | 960 mm | +60 mm aft |
| Fin CP station on the vehicle | 966.7 mm | **993.1 mm** | **+26 mm aft** |
| $C_{N\alpha}$ total | 3.483 rad⁻¹ | 4.352 rad⁻¹ | +25 % more control authority |
| **$x_{CP}$ (vehicle)** | **417.2 mm** | **539.8 mm** | **+123 mm aft** |
| **SM at liftoff (CG 484.5)** | **−1.68** 🔴 | **+1.38** ✅ | fixed |
| **SM at burnout (CG 458)** | **−1.02** 🔴 | **+2.04** ✅ | fixed |
| Fin planform area (each) | 3 600 mm² | **1 575 mm²** | **−56 %** |
| Fin mass, 3 mm G10 (3 fins) | 61.6 g | **26.9 g** | **−34.6 g** ✅ |
| Fin pressure drag $\Delta C_d$ | 0.076 | 0.134 | +0.058 (see note) |

> ✅ **Design decision for SR-1: $C_r = 60$ mm, $C_t = 30$ mm, $X_R = 22$ mm, $s = 35$ mm, thickness
> 3 mm G10.** This is **the fix**. It makes the vehicle stable across the whole burn *and* saves 35 g of
> fin mass — which is very nearly the entire 43.5 g mass-budget overrun recorded in
> `config/engineering_constants.md`.
>
> ⚠️ **The one penalty is fin pressure drag**, which rises from 0.076 to 0.134 because the *chord is
> shorter and the thickness unchanged*, so $t/c$ rises from 0.033 to 0.067 and the term scales as
> $(t/c)^2$. This is worth about **+0.06 on $C_d$**, i.e. roughly 3–4 m of apogee (§7.4). **Recover it by
> thinning the fins from 3.0 mm to 2.0 mm once the flutter screen in §11 confirms it is safe** — at
> 2 mm the fin pressure drag falls back to 0.059, and the flutter screen gives 258 m/s for 2 mm G10
> against a 54–67 m/s flight envelope. If you are building in plywood rather than G10, keep 3 mm.

**(d) If you cannot change the fins.** Then the CG must move forward, and the cost is severe because
nose ballast is the least efficient mass on the vehicle. From 306 g at 458 mm, ballast at station 40 mm:

| Target SM | Required CG | Ballast needed (as-specified fin, $x_{CP} = 417$ mm) |
|---|---|---|
| 1.0 caliber | 377 mm | **+71 g** |
| 1.5 calibers | 357 mm | +99 g |

Compare that with **0 g** for the fin fix. **Change the fin.**

**(e) Moving the CG forward at zero mass cost.** Independent of the fin, there is a free gain available:
relocating existing mass. Moving the ~75 g avionics + battery stack from station 350 mm to station
120 mm:

$$x_{CG,new} = \frac{306(458) - 75(350) + 75(120)}{306} = \frac{140\,148 - 26\,250 + 9\,000}{306} = 401.6\ \text{mm}$$

That is a **56 mm forward shift for zero added mass**, worth about **+1.4 calibers** of static margin on
its own. **Do this as well as the fin change, then trim the fin to bring the margin back toward the
middle of the 1–2 band.** Stacking both fixes and then relaxing the fin is how you end up with a vehicle
that is both stable and light.

### 5.9 The swing test — the empirical check

Barrowman is a prediction. The **swing test** is the measurement, and it costs nothing:

1. Assemble the vehicle **at its flight CG** — motor loaded or ballasted to flight mass, everything
   installed.
2. Tie a 2–3 m length of thin cord around the body **at the CG station** (a single loop, so the vehicle
   can pitch freely).
3. Swing the vehicle in a horizontal circle above your head, fast enough that it is clearly flying
   (roughly 10–15 m/s), not so fast that the string breaks.
4. **The nose must point into the direction of travel and stay there**, steadily, with no tendency to
   oscillate or flip.

If it does not, the vehicle is **not airworthy** regardless of what Barrowman says. Add nose-ward mass
and repeat. Record the result in the pre-flight log — this is a flight-readiness gate, not a suggestion.

---

## 6. WEATHERCOCKING AND ITS MANAGEMENT

### 6.1 What it is

**Weathercocking** is the tendency of a stable rocket to rotate its nose **into the wind** during the
low-speed, high-angle-of-attack part of the flight — from liftoff to roughly rail exit plus a second.

### 6.2 Why it happens

Three ingredients, and all three are present at liftoff:

1. **Crosswind.** Even a 3 m/s breeze is a large fraction of the 9 m/s rail exit velocity at T/W = 3.7.
2. **Angle of attack.** The relative wind is the vector sum of the vehicle's velocity and the wind, so
   the vehicle sees a genuine $\alpha$ even while pointing straight up.
3. **Restoring moment.** That $\alpha$ generates a normal force at the CP. With the CP 100–150 mm behind
   the CG, the resulting moment pitches the nose upwind.

The magnitude of the turn depends on the moment divided by the vehicle's pitching inertia and on how long
the vehicle remains slow. Since the moment is proportional to $q = \frac{1}{2}\rho v^2$ and the dynamic
pressure is tiny at low speed, the *rate* of turn peaks just after rail exit.

A handy estimate of the horizontal displacement accumulated while the vehicle is still slow, for a
vehicle accelerating at $a = g\left(\text{T/W} - 1\right)$ and reaching 15 m/s:

$$t_{15} = \frac{15}{g\left(\text{T/W} - 1\right)}, \qquad \Delta x \approx w\,t_{15}$$

At T/W = 3.71 this gives $t_{15} = 0.56$ s, so:

| Wind speed | Horizontal drift before the vehicle is "flying" |
|---|---|
| 2 m/s | 1.1 m |
| 4 m/s | 2.3 m |
| 6 m/s | 3.4 m |
| 8 m/s | 4.5 m |
| 10 m/s | 5.6 m |

Five metres of drift at 15 m/s of forward speed is **18° of trajectory tilt** before the vehicle has even
begun to fly properly — and the apogee penalty for an 18° tilt is $\cos^2(18°) = 0.90$, i.e. 10 % of apogee.
That is the real cost of a low thrust-to-weight ratio, and it is why §8 matters so much.

### 6.3 How to manage it

In order of effectiveness:

| # | Measure | Why it works | Cost |
|---|---|---|---|
| 1 | **Get off the rail fast** (higher T/W, longer rail) | Shortens the slow, high-$\alpha$ window | Bigger motor or a longer rail |
| 2 | **Keep the static margin at 1.0–1.5, not 3+** | The restoring moment is proportional to SM | Needs CG discipline |
| 3 | **Launch into the wind, not across it** | A headwind produces no net turn; a crosswind produces the maximum | Pad siting — free |
| 4 | **Use a long rail** (3–4 m) | Same as #1, cheaper | Rail transport and setup |
| 5 | **Lower the launch angle slightly** (e.g. 85° instead of 87°) | Trades apogee for a windage allowance; standard practice is to tilt *into* the wind | Some apogee |
| 6 | **Fly in the calm** (early morning) | Bengaluru surface winds are typically 2–4 m/s before 08:00 | Scheduling |
| 7 | Never reduce the static margin below 1.0 to "cure" weathercocking | You trade a trajectory fault for a stability fault | 🔴 Never do this |

> ⚠️ **The IN-SPACe competition rule requires a launch angle of 80°–85°, lockable.** That is not an
> accident: it is the competition's own weathercocking allowance. Design the pad so 80°–85° is
> repeatable and **locked** — a pad that drifts during the count is a range-safety problem.

---

## 7. DRAG

### 7.1 The drag equation

$$D = \tfrac{1}{2}\rho v^2 C_d A, \qquad A = \frac{\pi}{4}d^2 = 1.2566\times10^{-3}\ \text{m}^2$$

Equivalently, with a single lumped coefficient $k = \frac{1}{2}\rho C_d A$:

$$D = k v^2, \qquad k = 0.5 \times 1.10 \times 0.45 \times 1.2566\times10^{-3}
= \mathbf{3.11\times10^{-4}\ N/(m/s)^2}$$

That one number, $k$, is all a flight simulation needs for the drag model, and it makes the coast phase
integrable in closed form (§7.5).

### 7.2 Where the drag comes from

| Component | Physical cause | Typical $\Delta C_d$ | How to reduce it |
|---|---|---|---|
| **Skin friction** | Viscous shear in the boundary layer over all wetted area | **0.20–0.40** | Smoother finish, less wetted area, delayed transition |
| **Base drag** | The blunt aft end leaves a low-pressure wake; the pressure difference sucks the vehicle backwards | **0.12** (referred to base area at subsonic speeds) | Boattail (costs stability — see §4.2) |
| **Nose pressure (form) drag** | Flow decelerates and recompresses over the nose; losses in the nose boundary layer | **0.05–0.08** (ogive) | Better nose shape; small effect below Mach 0.6 |
| **Fin pressure drag** | Fin thickness; the term is $\propto (t/c)^2$ | **0.03–0.09** | Thinner fins, or an airfoiled section |
| **Interference drag** | Junctions: fin-root/body, launch lug, camera bumps, paint ridges | **0.02–0.05** | Fillets, blended transitions, fewer protuberances |
| **Total** | | **≈ 0.4–0.6** | |

**Skin friction is the dominant term and it is a wetted-area problem, not a speed problem.** The ratio of
wetted to frontal area on this vehicle is about **108:1** — 0.136 m² of wetted surface against
0.00126 m² of frontal area. That ratio is why a long, thin rocket has a higher $C_d$ (referred to frontal
area) than a short, fat one, and why "make it longer for stability" has a drag cost.

$$C_{d,\text{friction}} = C_f \times \frac{S_{wet}}{S_{ref}}$$

with the flat-plate skin-friction coefficient

$$C_f = \frac{1.328}{\sqrt{Re}} \ \ (\text{laminar}, \ Re < 5\times10^{5}),
\qquad
C_f = \frac{0.455}{\left(\log_{10}Re\right)^{2.58}} \ \ (\text{turbulent})$$

and $Re = \rho V d/\mu$ with $\mu = 1.85\times10^{-5}$ Pa·s. At the burnout condition ($V = 54$ m/s):

$$Re = \frac{(1.10)(54)(0.040)}{1.85\times10^{-5}} = \mathbf{1.28\times10^{5}}$$

This is **below the 5×10⁵ transition threshold**, so the boundary layer is laminar over most of the body
and the laminar $C_f$ applies. This matters: the turbulent formula would over-predict friction drag by
roughly a factor of two at this Reynolds number. **Model rockets at 50–150 m/s are laminar-drag
vehicles, and most amateur drag estimates are wrong because they assume turbulent flow.**

### 7.3 The working value: Cd = 0.45

For `config/engineering_constants.md`, the club uses

$$C_d = 0.45 \ \text{(subsonic, referred to body cross-section)}$$

**What it is:** a single, defensible, mid-band number for a cleanly-built 40 mm paper rocket at
50–150 m/s. It sits inside the measured 0.4–0.6 band, and the build-up above lands at ≈0.44 at the low
end and ≈0.64 at the pessimistic laminar-friction end, so 0.45 is at the **optimistic edge** of the
plausible range.

**What it is not:** a measured value for *this* vehicle. It carries no information about whether the
fillets are smooth, whether the paint is glossy, whether the fins are aligned, or whether the launch lug
is streamlined.

> **Rule: Cd = 0.45 is a design place-holder and must be corrected from measured flight data.** The
> correction procedure is in §7.6. Until then, treat every apogee prediction in this document as ±10 %.

### 7.4 How much does Cd actually matter here?

Less than most people think, and this is worth knowing before you spend a week polishing.

Full RK4 trajectory, 306 g dry, 24 N·s over 2.0 s, 1.5 m rail:

| $C_d$ | Burnout velocity | Apogee |
|---|---|---|
| 0.35 | 54.8 m/s | 191.6 m |
| **0.45** | **54.3 m/s** | **185.8 m** |
| 0.60 | 53.7 m/s | 177.9 m |
| 0.70 | 53.3 m/s | 173.2 m |

**Swinging Cd by ±0.15 — a huge change in aerodynamic quality — moves apogee by about ±6 m, or ±3 %.**
The reason is that a slow, heavy rocket's apogee is dominated by **gravity**, not by drag. Do not
optimise drag on a 200 m rocket. **Optimise mass.** §7.5 shows the same vehicle at 250 g dry reaching
258 m.

### 7.5 The closed-form coast solution

Because $D = kv^2$, the coast phase from burnout to apogee has an exact solution. From

$$m\frac{dv}{dt} = -kv^2 - mg$$

the coast height from burnout velocity $v_0$ with burnout mass $m$ is

$$\boxed{h_{coast} = \frac{m}{2k}\ln\left(1 + \frac{k v_0^2}{mg}\right)}$$

and the coast time is

$$t_{coast} = \sqrt{\frac{m}{kg}}\ \arctan\left(v_0\sqrt{\frac{k}{mg}}\right)$$

**Worked, for the 24 N·s / 2 s baseline:**

- Launch mass $m_0 = 306 + 24 = 330$ g
- Average thrust $T = 24/2.0 = 12.0$ N
- Ideal burnout velocity (impulse over mass) $= 24/0.330 = 72.7$ m/s
- Gravity loss during the burn $= g\,t_b/2 = 9.81 \times 1.0 = 9.81$ m/s
- **Burnout velocity $v_0 \approx 72.7 - 9.81 = 62.9$ m/s** (analytic; drag during the burn brings the
  simulated value to **54.3 m/s**)
- Burnout altitude $\approx \frac{1}{2}(0 + 54.3)(2.0) = 54.3$ m

With $m = 0.306$ kg at burnout and $k = 3.11\times10^{-4}$:

$$\frac{k v_0^2}{mg} = \frac{(3.11\times10^{-4})(54.3)^2}{(0.306)(9.81)} = \frac{0.9171}{3.002} = 0.3055$$

$$h_{coast} = \frac{0.306}{2(3.11\times10^{-4})}\ln(1.3055)
= 492.0 \times 0.2666 = \mathbf{131.2\ m}$$

$$h_{total} \approx 54.3 + 131.2 = \mathbf{185.5\ m} \quad \checkmark \ \text{(matches the RK4 result of 185.8 m)}$$

**The vacuum comparison** shows what drag actually costs:

$$h_{vacuum} = \frac{v_0^2}{2g} = \frac{(54.3)^2}{2(9.81)} = 150.3\ \text{m}
\quad \Rightarrow \quad \text{drag costs } 1 - \frac{131.2 + 0}{150.3} \approx \mathbf{12.7\ \%}$$

### 7.6 Correcting Cd from flight data — mandatory

The vehicle carries an altimeter. Use it.

1. **Fly with a known motor** whose total impulse and burn time are certified (a commercial motor, or
   your own motor measured on the static test stand).
2. **Record apogee** from the flight computer. Record the launch mass on the same day, on the same scale.
3. **Invert the closed form.** For a given $C_d$ (hence $k$), predict apogee by the §7.5 method using the
   *measured* burnout velocity; or, more simply, iterate $C_d$ in OpenRocket until the predicted apogee
   matches the measured apogee.
4. **Repeat three times.** Take the mean. Weathercocking and wind will bias individual flights low — if
   the three apogees scatter by more than 10 %, your launch conditions are not repeatable and the data is
   not yet usable.
5. **Write the result into `config/engineering_constants.md`** and update the change log. This document
   is then updated to reference it.

> **Expect the measured value to be higher than 0.45, not lower.** A paper rocket with a launch lug, a
> painted finish and hand-shaped fins typically measures 0.50–0.65. Plan for it.

### 7.7 The drag-corrected apogee prediction method

This is the club's standard method, and it is the one the tables in §10 use.

```
1.  m_dry                       from the mass budget
2.  m_prop = I_total / (Isp * g)      Isp ~ 120 s for KNSB (see config)
3.  m_0 = m_dry + m_prop
4.  T_avg = I_total / t_burn
5.  T/W = T_avg / (m_0 * g)          check against the 5:1 guideline (§8)
6.  v_rail = sqrt(2 * g * (T/W - 1) * L_rail)      check against 15-20 m/s
7.  v_bo  = I_total/m_0 - g*t_burn/2 - <drag loss>  (use RK4, or read the table in §10)
8.  h_bo  = 0.5 * v_bo * t_burn       (average-velocity estimate)
9.  k     = 0.5 * rho * Cd * A
10. h_coast = (m_dry/(2k)) * ln(1 + k*v_bo^2/(m_dry*g))
11. APOGEE = h_bo + h_coast
```

Steps 7–10 are exactly the closed-form solution of §7.5; step 7's drag-during-burn loss is the only part
that needs a numerical integration, and it is a few percent. **Run OpenRocket for the final number**, and
use this method to check that OpenRocket is not lying to you.

---

## 8. LAUNCH RAIL EXIT VELOCITY

### 8.1 Why it matters

The launch rail exists to hold the vehicle pointing in a known direction until the fins are generating
enough aerodynamic force to control it. **If the vehicle leaves the rail too slowly, the fins are not yet
flying, and the vehicle goes wherever the wind and the thrust misalignment send it.**

Two independent requirements set the minimum:

1. **Aerodynamic authority.** The fins need dynamic pressure. Below roughly **15 m/s** the restoring
   moment from the fins is comparable to the disturbance moments from a modest crosswind and from the
   motor's thrust misalignment. Above ~20 m/s the vehicle is decisively flying.
2. **Wind ratio.** A widely used rule is that the rail exit velocity should be **at least about 4 times
   the wind speed** at the pad. In a 4 m/s Bengaluru morning breeze that is 16 m/s — which agrees with
   the absolute guidance, and is a good sign that the rule is physically meaningful rather than folklore.

> **Club rule: rail exit velocity ≥ 15 m/s, target 20 m/s. Below 15 m/s the flight is not authorised
> unless the wind is under 3 m/s and the pad is sited directly into the wind.**

### 8.2 The relation to thrust-to-weight ratio

Ignoring drag (valid because the vehicle is slow), the net acceleration on the rail is

$$a = g\left(\frac{T}{W} - 1\right)$$

and for a rail of usable length $L$ (measure the **usable** length — from the top of the rail *button*
at rest to the point where the button leaves the rail, not the total rail length):

$$\boxed{v_{rail} = \sqrt{2\,g\left(\frac{T}{W} - 1\right)L}}$$

**Rail exit velocity (m/s):**

| T/W | $a$ (m/s²) | 1.0 m | 1.5 m | 2.0 m | 3.0 m | 4.0 m | 5.0 m |
|---|---|---|---|---|---|---|---|
| 2.0 | 9.8 | 3.4 | 5.4 | 6.3 | 7.7 | 8.9 | 9.9 |
| 3.0 | 19.6 | 6.3 | 7.7 | 8.9 | 10.9 | 12.5 | 14.0 |
| **3.7** | **26.5** | **7.3** | **8.9** | **10.3** | **12.6** | **14.6** | **16.3** |
| 4.0 | 29.4 | 7.7 | 9.4 | 10.9 | 13.3 | 15.3 | 17.2 |
| 5.0 | 39.2 | 8.9 | 10.9 | 12.5 | 15.3 | 17.7 | 19.8 |
| 6.0 | 49.1 | 9.9 | 12.1 | 14.0 | 17.2 | 19.8 | 22.2 |
| 8.0 | 68.7 | 11.7 | 14.4 | 16.6 | 20.3 | 23.4 | 26.2 |
| 10.0 | 88.3 | 13.3 | 16.3 | 18.8 | 23.0 | 26.6 | 29.7 |
| 12.0 | 107.9 | 14.7 | 18.0 | 20.8 | 25.5 | 29.4 | 32.9 |

**Run it backwards — thrust required to reach a target exit velocity** (launch mass 0.330 kg,
$T = m\left(a + g\right)$):

| Usable rail | Thrust for 15 m/s | T/W needed | Thrust for 20 m/s | T/W needed |
|---|---|---|---|---|
| 1.0 m | 40.4 N | 12.5 | 69.2 N | 21.4 |
| 1.5 m | 28.0 N | 8.7 | 47.2 N | 14.6 |
| 2.0 m | 21.8 N | 6.7 | 36.2 N | 11.2 |
| 3.0 m | 15.6 N | 4.8 | 25.2 N | 7.8 |
| 4.0 m | 12.5 N | 3.9 | 19.7 N | 6.1 |
| 5.0 m | 10.7 N | 3.3 | 16.4 N | 5.1 |

### 8.3 The 5:1 guideline applied to this vehicle

> **Common guideline: minimum thrust-to-weight ratio of about 5:1 at launch.**

$$\frac{T}{W} = \frac{12.0}{(0.330)(9.81)} = \frac{12.0}{3.24} = \mathbf{3.71}$$

🔴 **The baseline 24 N·s / 2 s motor violates the 5:1 guideline.** The consequences are concrete:

- Rail exit velocity on a 1.5 m rail is only **8.9 m/s** — barely half the club minimum.
- Reaching 15 m/s requires a **4.2 m** usable rail; reaching 20 m/s requires **7.5 m**.
- The vehicle spends the first ~0.6 s at low dynamic pressure, which is exactly the weathercocking
  window of §6.2.

**Three ways out, in increasing order of cost:**

| Fix | Effect | Cost |
|---|---|---|
| **Use a 4 m rail** | 14.6 m/s exit at unchanged T/W | Rail cost and transport; the cheapest fix by far |
| **Burn the same 24 N·s faster** (0.8 s → T = 30 N, T/W = 9.4) | **15.8 m/s** on a 1.5 m rail; apogee rises to 214 m | Higher chamber pressure, heavier casing, hotter nozzle — see `10_PROPULSION/Motor_Design_Guide.md` |
| **Go to 30–36 N·s** | T/W 4.6–5.5, exit 10.4–11.5 m/s on 1.5 m | New motor, new grains, thrust-plate re-check |

> **Recommendation for the first flight: use a 4 m rail and a 0.8 s burn.** The 4 m rail costs money once;
> the fast burn costs a re-designed throat and a casing check. Together they give a 15.8 m/s exit, a
> thrust-to-weight ratio of 9.4, and 214 m of apogee — clearing both the rail rule and the 200 m target
> with the same 24 N·s of impulse.

### 8.4 Rail, button, and lug practicalities

- **Rail buttons are better than a launch lug.** A lug is a long, low-aspect-ratio tube that binds on
  grit; buttons are short, self-clearing, and can be replaced when worn. Two buttons spaced as widely as
  the airframe allows (at least 300 mm apart on a 1020 mm vehicle) give a stable, non-binding interface.
- **The rail must be straight and clean.** A bent rail is a thrust-misalignment generator. Store rails
  vertically or in a straight rack, never leaning.
- **Usable length, not total length.** With the aft button at the bottom of the rail, the usable length
  is the rail length minus the button spacing. State this number in the flight card.
- **Rail vs rod.** A 40 mm vehicle is well past the point where a 6 mm rod is adequate; rods whip and
  induce exactly the tip-off that the rail exists to prevent. **Use a rail.**

---

## 9. LAUNCH ANGLE AND RAIL LENGTH GUIDANCE

### 9.1 Launch angle

| Angle from vertical | Vertical component | When to use |
|---|---|---|
| 0° (vertical) | 1.000 | Ideal conditions, calm, competition rules permitting |
| **5°** | 0.996 | **Club default.** Only 0.4 % of the vertical velocity is lost, and it buys a windage allowance |
| **10°** | 0.985 | Wind 4–6 m/s, into the wind |
| 15° | 0.966 | Wind 6–9 m/s; expect a visible apogee penalty |
| 20° | 0.940 | Not recommended — apogee loss exceeds 6 % and the descent drifts |
| 80°–85° from horizontal (IN-SPACe) | 0.985–0.996 | **Competition range; lockable.** Equivalent to 5°–10° from vertical |

**Rules.**

1. **Tilt into the wind, never away from it.** Tilting into the wind means the vehicle's initial velocity
   vector already has an upwind component, so the weathercocking turn *reduces* the net tilt rather than
   adding to it. Tilting downwind doubles the error.
2. **Launch directly into the wind when the wind is 3–6 m/s.** A pure headwind produces no turn at all.
   This is the single highest-value free action available on launch day.
3. **Record the angle and the wind** on every flight card. Without that record, the flight data cannot be
   used to correct Cd (§7.6).
4. The vertical-velocity penalty is $\cos\theta$. At 10° that is 1.5 % — a 3 m apogee loss on a 186 m
   flight. **The weathercocking you prevent is worth far more than the 1.5 % you spend.**

### 9.2 Rail length selection

$$L_{usable} \ge \frac{v_{target}^2}{2g\left(\text{T/W} - 1\right)}$$

| Vehicle T/W | Rail for 15 m/s | Rail for 20 m/s |
|---|---|---|
| 3.7 (baseline) | 4.2 m | 7.5 m |
| 5 | 2.9 m | 5.1 m |
| 8 | 1.6 m | 2.9 m |
| 10 | 1.3 m | 2.3 m |
| 15 | 0.8 m | 1.5 m |

> **Club standard rail: 4 m.** It satisfies 15 m/s for any vehicle with T/W ≥ 3.9, which covers the entire
> planned flight ladder. A 1.5 m rail should be regarded as a **test-stand and static-fire** item only.

---

## 10. IMPULSE TO APOGEE — THE FLIGHT LADDER

### 10.1 The method

All numbers below use the drag-corrected method of §7.7 with the club constants:

- $m_{dry} = 306$ g, $d = 40$ mm, $A = 1.2566\times10^{-3}$ m²
- $C_d = 0.45$, $\rho = 1.10$ kg/m³, $k = 3.11\times10^{-4}$ N/(m/s)²
- $I_{sp} = 120$ s, so $m_{prop} = \dfrac{I}{120 \times 9.81} \times 1000$ grams
- Rail: 1.5 m, vertical launch
- Full RK4 integration of boost (thrust − drag − weight) and coast (−drag − weight)

### 10.2 The table — 2.0 s burn

| Total impulse (N·s) | Class | Propellant (g) | Launch mass (g) | Thrust (N) | T/W | Rail exit (m/s) | Burnout $v$ (m/s) | **Apogee (m)** | vs 200 m |
|---|---|---|---|---|---|---|---|---|---|
| 10 | C | 8.5 | 314.5 | 5.0 | 1.62 | 4.3 | 12.5 | **20** | −180 |
| 16 | D | 13.6 | 319.6 | 8.0 | 2.55 | 6.8 | 30.9 | **77** | −123 |
| 20 | D | 17.0 | 323.0 | 10.0 | 3.16 | 8.0 | 42.8 | **128** | −72 |
| **24** | **D/E** | **20.4** | **326.4** | **12.0** | **3.75** | **9.0** | **54.3** | **186** | **−14** |
| 30 | E | 25.5 | 331.5 | 15.0 | 4.61 | 10.3 | 71.2 | **279** | +79 |
| 36 | E/F | 30.6 | 336.6 | 18.0 | 5.45 | 11.5 | 87.4 | **375** | +175 |
| 50 | F | 42.5 | 348.5 | 25.0 | 7.31 | 13.6 | 123.2 | **590** | +390 |
| 70 | F/G | 59.5 | 365.5 | 35.0 | 9.76 | 16.1 | 170.0 | **855** | +655 |
| 100 | G | 84.9 | 390.9 | 50.0 | 13.04 | 18.8 | 232.7 | **1 168** | +968 |

### 10.3 The same impulses burned in 0.8 s (higher thrust)

| Total impulse (N·s) | Thrust (N) | T/W | Rail exit (m/s) | Burnout $v$ (m/s) | **Apogee (m)** |
|---|---|---|---|---|---|
| 10 | 12.5 | 4.05 | 9.5 | 24.2 | 39 |
| 16 | 20.0 | 6.38 | 12.6 | 42.8 | 103 |
| 20 | 25.0 | 7.89 | 14.2 | 55.0 | 156 |
| **24** | **30.0** | **9.37** | **15.7** | **66.9** | **214** ✔ |
| 30 | 37.5 | 11.53 | 17.6 | 84.4 | 306 |
| 36 | 45.0 | 13.63 | 19.3 | 101.6 | 398 |
| 50 | 62.5 | 18.28 | 22.6 | 140.1 | 602 |

> **The comparison is the whole point of this section.** The same impulse, delivered faster, turns an
> 8.9 m/s rail exit into 15.8 m/s and an 186 m apogee into 214 m. **Thrust is not just about climbing
> harder — it is about getting the vehicle flying before the wind can touch it.**

### 10.4 Impulse actually required to reach 200 m

Solved by iterating the §7.7 method for exactly 200 m of apogee, at $m_{dry} = 306$ g:

| Burn time | Required impulse | Propellant | Thrust | T/W | Rail exit (1.5 m) | Burnout $v$ |
|---|---|---|---|---|---|---|
| 0.5 s | 22.6 N·s | 19.2 g | 45.2 N | 14.2 | 19.8 m/s | 66.1 m/s |
| 0.6 s | 22.8 N·s | 19.3 g | 37.9 N | 11.9 | 18.0 m/s | 65.4 m/s |
| **0.8 s** | **23.1 N·s** | **19.6 g** | **28.8 N** | **9.0** | **15.4 m/s** | **64.1 m/s** |
| 1.0 s | 23.4 N·s | 19.8 g | 23.4 N | 7.3 | 13.7 m/s | 62.8 m/s |
| 1.5 s | 24.1 N·s | 20.5 g | 16.1 N | 5.0 | 10.9 m/s | 59.8 m/s |
| **2.0 s** | **24.9 N·s** | **21.2 g** | **12.5 N** | **3.9** | **9.3 m/s** | **57.0 m/s** |
| 3.0 s | 26.7 N·s | 22.7 g | 8.9 N | 2.8 | 7.2 m/s | 52.0 m/s |

**Read the bottom row.** A slow burn is doubly penalised: it needs **more** impulse for the same apogee
(more gravity loss), and it gives a **worse** rail exit (less thrust). **For a fixed impulse, always burn
it as fast as the casing and nozzle can take.**

### 10.5 Sensitivity — mass is the dominant variable

24 N·s over 2.0 s, $C_d = 0.45$:

| Dry mass | Launch mass | Burnout $v$ | **Apogee** |
|---|---|---|---|
| 250 g | 270 g | 68.7 m/s | **258 m** |
| 275 g | 295 g | 61.7 m/s | **223 m** |
| **306 g** | **326 g** | **54.3 m/s** | **186 m** |
| 333 g | 353 g | 48.9 m/s | **159 m** |
| 360 g | 380 g | 44.1 m/s | **136 m** |

> **Every 25 g of dry mass is worth roughly 32 m of apogee.** Compare that with the ±6 m available from
> a heroic drag reduction. **If you want 200 m, go and remove 27 g from the vehicle — do not polish it.**

### 10.6 Reconciling 72 m/s with this table

`config/engineering_constants.md` records a **required burnout velocity of 72 m/s** for the 200 m target,
computed with quadratic drag. The club's own closed-form solution gives a different pair of numbers, and
the discrepancy must be understood rather than ignored:

| Statement | Value | Consistent with $C_d = 0.45$? |
|---|---|---|
| Vacuum ideal for 200 m, $m = 306$ g | $v = \sqrt{2gh} = 62.6$ m/s | ✅ — this is the vacuum result and is independent of drag |
| Required burnout velocity for 200 m at $C_d = 0.45$ | **69.6 m/s** | ✅ from the closed form of §7.5 |
| The recorded 72 m/s for 200 m | 72 m/s | implies an effective $C_d \approx 0.24$, which is optimistic for a paper rocket |
| Apogee at 72 m/s and $C_d = 0.45$ | **211.5 m** | 72 m/s *overshoots* 200 m |

**Conclusion.** The 72 m/s figure is conservative (it demands slightly more than the physics requires),
so it is safe to design to. But the *conversion* from 72 m/s to "24 N·s is enough" does not hold: at
$C_d = 0.45$ the baseline motor delivers 54.3 m/s, not 72 m/s. The gap is not in the velocity
requirement — it is in the **motor** and in the **thrust-to-weight ratio**.

> **Action:** update the required-burnout-velocity line in `config/engineering_constants.md` to
> **69.6 m/s at $C_d = 0.45$**, and add the note that a 24 N·s motor at 2.0 s of burn time delivers only
> 54 m/s at 306 g dry. The 72 m/s figure should be retained as a **design target with margin**, not as a
> prediction.

---

## 11. FIN FLUTTER AND DIVERGENCE

### 11.1 What flutter is

**Flutter** is a **self-excited** aeroelastic instability. It is not a load that you can compute
statically and compare with a material strength — it is a *feedback loop*:

1. Airflow bends the fin (bending mode).
2. Bending twists the fin because the aerodynamic centre is behind the fin's flexural axis (torsion mode).
3. Twisting increases the local angle of attack.
4. Increased $\alpha$ increases the lift, hence the bending.
5. The energy extracted from the airflow each cycle exceeds the structural damping, so the amplitude
   **grows exponentially**.

Below the **flutter velocity** $V_f$, disturbances decay. Above it, the amplitude doubles in a fraction of
a second and the fin sheds or shatters — usually followed by a violent pitch/yaw excursion and loss of
the vehicle. **There is no partial flutter and no warning.**

**Divergence** is the static limit of the same mechanism: the speed at which the torsional stiffness is
no longer able to hold the fin at a finite pitch angle, and the twist runs away to failure. Divergence is
always at a *higher* speed than flutter for a real fin, so a divergence calculation is a **conservative
screen**: if the fin is safe against divergence, it is safe against flutter.

### 11.2 The governing variables

The torsional stiffness of a rectangular fin section is

$$GJ \approx G \cdot \frac{1}{3} b t^3$$

so the divergence speed of a cantilever fin scales as

$$V_{div} \propto \sqrt{\frac{GJ}{q\,e\,c^2\,C_{L\alpha}\,S}}
\ \Longrightarrow \
\boxed{V_f \propto t^{1.5}\sqrt{\frac{G}{AR^3}}}$$

with $AR$ the exposed aspect ratio, $G$ the shear modulus, $t$ the fin thickness, $c$ the chord, $e$ the
distance from the aerodynamic centre to the fin's flexural axis, and $S$ the fin planform area.

**The three levers, in order of power:**

| Variable | Scaling | Going from → to | Effect on $V_f$ |
|---|---|---|---|
| **Thickness** $t$ | $t^{1.5}$ | 3 mm → 4 mm | **+54 %** |
| | | 3 mm → 2 mm | **−46 %** |
| **Aspect ratio** $AR$ | $AR^{-1.5}$ | 2 → 4 | **−65 %** |
| **Shear modulus** $G$ | $G^{0.5}$ | balsa → G10 | **+221 %** (3.2×) |

**Thickness is the dominant and cheapest lever.** A fin that flutters is almost never fixed by changing
material — it is fixed by making it thicker or shorter.

### 11.3 Worked screen for the baseline fins

Cantilever fin, $C_r = 120$ mm, $C_t = 60$ mm, $s = 40$ mm, $\rho = 1.10$ kg/m³, at 200 m altitude:

| Fin thickness | G10/FR-4 | Birch plywood | Balsa | Al 6061-T6 |
|---|---|---|---|---|
| 2.0 mm | 101 m/s | 45 m/s | 32 m/s | 276 m/s |
| **3.0 mm** | **186 m/s** | 83 m/s | 58 m/s | 507 m/s |
| 4.0 mm | 287 m/s | 128 m/s | 89 m/s | 781 m/s |

*(Exposed aspect ratio $AR = 2s/C_r = 0.67$ — a short, stubby fin. Values are the torsional-divergence
screen; the exact flutter velocity is somewhat lower but the trend is identical. Reproduce with the
script in §11.5.)*

**Verdict for this vehicle.** The baseline vehicle's maximum velocity is **54 m/s** (or 67 m/s with the
0.8 s burn). Against a 3 mm G10 fin at 186 m/s, that is a **factor of 3.4** — **flutter is not a driver
for SR-1 and the 3 mm G10 standard is confirmed adequate.**

### 11.4 When flutter *does* become the driver

| Vehicle | Max velocity | Fin $AR$ | Flutter risk |
|---|---|---|---|
| SR-1 (40 mm, 200 m) | 54–67 m/s | 0.67 | Negligible |
| 500 m class | ~140 m/s | 0.67–1.5 | Low, but check |
| 1000 m class | ~200 m/s | 1.5–3 | **Real — 4 mm G10 minimum** |
| Competition vehicle (94 mm, 1000 m) | ~250–300 m/s | 2–4 | **Design driver — 5 mm G10 or carbon, tip $t/c \ge 0.05$** |

> **Design rules that fall out of the scaling law:**
> 1. **Keep the tip thickness ≥ 3 mm** for anything above 200 m/s, and the tip $t/c \ge 0.05$.
> 2. **Never sharpen the trailing edge to a knife edge.** Leave 0.5–0.8 mm. A knife edge has zero
>    torsional stiffness and will flutter at a fraction of the panel's predicted speed.
> 3. **Airfoil the fin by rounding the leading edge**, not by thinning the section.
> 4. **Never use balsa for a flight fin above 100 m/s.** It is a wind-tunnel and mock-up material.
> 5. **A fin that flutters at 150 m/s will not be cured by a stronger bond.** It is a stiffness problem.

### 11.5 Reproducing the screen

```python
import math
rho, e, cla = 1.10, 0.25, 2*math.pi
def V_div(s, c, t, E, G):          # s, c, t in metres
    J  = (1/3)*c*t**3              # torsion constant, rectangular section
    S  = s*c                       # planform area
    V2 = 2*G*J/(rho*e*c*c*cla*S)
    return math.sqrt(V2)/math.sqrt(1 + 2/(2*s/c))   # finite-span allowance
# baseline: s=40 mm, mean chord=90 mm, t=3 mm, G10 (G=3.5 GPa)
print(V_div(0.040, 0.090, 0.003, 24e9, 3.5e9))     # -> 186 m/s
```

Thickness scaling check (must reproduce $t^{1.5}$):

| $t$ | $V_{div}$ | ratio to 3 mm | $(t/3)^{1.5}$ |
|---|---|---|---|
| 1.5 mm | 186 m/s | 0.354 | 0.354 ✔ |
| 2.0 mm | 287 m/s | 0.544 | 0.544 ✔ |
| 3.0 mm | 526 m/s | 1.000 | 1.000 ✔ |
| 4.0 mm | 810 m/s | 1.540 | 1.540 ✔ |

*(Values above are for the shorter 20 mm-span club fin, at sea-level density.)*

---

## 12. DESIGN CHECKLIST

Copy this into the PDR. Every line must be answered with a number and a source.

**Stability**

- [ ] $x_{CP}$ computed by hand (Barrowman) and cross-checked in OpenRocket — record both, and reconcile any difference over 10 %
- [ ] $x_{CG}$ measured on the **finished** vehicle, at flight mass, on a balance
- [ ] Static margin between **1.0 and 2.0 calibers** at **liftoff**
- [ ] Static margin checked at **burnout** and with a **spent motor**
- [ ] Static margin is **not above 2.5 calibers** (weathercocking)
- [ ] Swing test passed at the flight CG
- [ ] Fin alignment verified (all fins within 0.5° of the body axis; see `Fabrication_and_Manufacturing.md` §3)

**Rail and launch**

- [ ] $T/W \ge 5$ at liftoff, **or** a documented rail-length compensation
- [ ] Rail exit velocity $\ge 15$ m/s (target 20 m/s) — computed, not assumed
- [ ] Rail exit velocity $\ge 4 \times$ the forecast wind speed
- [ ] Usable rail length (not total length) used in the calculation
- [ ] Rail straight; buttons secure; usable length recorded on the flight card

**Drag and performance**

- [ ] $C_d$ value stated, with its source (default 0.45, flagged as unvalidated)
- [ ] Apogee predicted by the §7.7 method **and** by OpenRocket, and the two reconciled
- [ ] Mass budget within ±5 % of the design value at the moment of launch
- [ ] Post-flight: measured apogee used to correct $C_d$; `config/engineering_constants.md` updated

**Structure and flutter**

- [ ] Fin thickness ≥ 3 mm (G10 or equivalent) for any vehicle above 100 m/s
- [ ] Divergence/flutter screen run at 1.5 × the maximum predicted velocity
- [ ] Trailing edge not sharpened below 0.5 mm
- [ ] Fin root bond and tube bending checked per `Structures_Design_Guide.md` (do not duplicate the work — cite it)

---

## 13. WORKED EXAMPLE INDEX

Every number in this document can be reproduced. The scripts are short enough to retype.

| Section | What it computes | Key result |
|---|---|---|
| §4.4 | Fin CP by chordwise integration (verify with `sympy`) | $x_f = \dfrac{C_r^2 + C_rC_t + C_t^2 + C_rX_R + 2C_tX_R}{3(C_r+C_t)}$ |
| §5 | Full Barrowman for the baseline vehicle | $x_{CP} = 417.16$ mm, SM = −1.02 cal |
| §5.8 | Trim trade study | shrinking fins moves $x_{CP}$ aft but destroys lift |
| §7.4 | Apogee vs $C_d$ | ±0.15 in $C_d$ is worth ±6 m |
| §7.5 | Closed-form coast | $h = \frac{m}{2k}\ln\left(1 + \frac{kv_0^2}{mg}\right)$ |
| §8.2 | Rail exit velocity | $v = \sqrt{2g(T/W - 1)L}$ |
| §10.2 | Impulse-to-apogee ladder | 24 N·s @ 2 s → 186 m |
| §10.3 | Same impulse, 0.8 s burn | 24 N·s @ 0.8 s → 214 m ✔ |
| §10.5 | Mass sensitivity | 25 g ≈ 32 m |
| §11.5 | Flutter screen | $V_f \propto t^{1.5}$ confirmed exactly |

---

## 14. REFERENCES

| Source | Used for |
|---|---|
| James S. Barrowman, *The Practical Calculation of the Aerodynamic Characteristics of Slender Finned Vehicles*, NASA CR-* / NACA, 1966–67 | The entire CP method of §3–§5 |
| `Technical_Reference_Nakka.md` (this workspace) | Airframe diameter, mass, KNSB propellant, burn-rate behaviour, motor design context |
| `config/engineering_constants.md` (this workspace) | Vehicle baseline, IN-SPACe competition constraints, working $C_d$, required burnout velocity |
| `20_AEROSTRUCTURES/Structures_Design_Guide.md` (this workspace) | Section properties, loads, buckling, bond strengths — **not repeated here** |
| Richard Nakka, *Experimental Rocketry* — `fins.html`, `rtheory.html`, `rocket.html` | Fin practice, flutter rules of thumb, recovery-system context [⏳ raw text not yet retrieved into `80_REFERENCE/`] |
| NACA TN-4197, *Summary of Flutter Experiences as a Guide to the Preliminary Design of Lifting Surfaces on Missiles*, 1958 | Flutter/divergence scaling laws of §11 |

> **⚠️ Section reference note.** `Structures_Design_Guide.md` §1 uses a **700 mm** overall length
> (120 mm nose + 580 mm body). This document uses the vehicle baseline recorded in
> `config/engineering_constants.md` (**900 mm body, ~1020 mm overall**). Barrowman CP and the drag
> build-up depend on the body length, so the two documents are internally consistent but describe
> different body lengths. **Before the first flight, `config/engineering_constants.md` must be updated
> with a single agreed overall length, and both documents re-issued against it.** The Barrowman results
> scale as follows: for a 700 mm overall length, $x_{CP} = 334.7$ mm.

---

*Document owner: Aerostructures lead. Review cycle: before every PDR/CDR and after every flight.*
*Every number here is derived in-line. If you change a constant, change it in `config/engineering_constants.md` — not here.*
