# UVCE Rocketry Club — Foundation Reader

**The 10-page material. Read this before the open-book test.**

| | |
|---|---|
| **Version** | 1.0 |
| **Reading time** | ~45 minutes |
| **Test** | Open book. You may keep this in front of you. |

> **How to read this.** You are not expected to memorise anything. You *are* expected to understand
> the ideas well enough to look things up quickly during the test and apply them. Read it once
> properly, then use it as a reference.

---

# PAGE 1 — Why we exist

## What we are building

A rocket. Specifically, a **40 mm diameter, ~900 mm long, single-stage solid rocket** carrying a small
payload to **200 metres**, using a motor **we design and build ourselves**.

Then, later, a bigger one: the IN-SPACe Model Rocketry competition requires carrying **1 kg to
1,000 m ± 100 m** — and in that competition the motor is supplied, not built.

## Why this is hard

Four things must work **simultaneously, once, with no second attempt**:

1. The **motor** must ignite reliably, burn at the pressure we designed for, and not burst.
2. The **structure** must survive the thrust, the airloads, and the landing.
3. The **recovery system** must deploy at the right moment and slow the descent to a survivable speed.
4. The **avionics** must record what happened so we learn something.

Any one of these failing means the flight fails. This is why rocketry is a **systems engineering**
discipline: the difficulty is not any single part, it is making all the parts agree.

## What we are not

We are not a club that watches rocket videos. We build, test, fail, measure, and rebuild. If you want
to talk about rockets, there are easier places. If you want to hold a motor you cast yourself and
watch it burn on a test stand with your own data on the screen — this is the place.

## The honest expectation

**You will not know anything on day one. Neither did anyone else here.** The people who become good
at this are not the most talented. They are the ones who find the frustration interesting instead of
discouraging.

---

# PAGE 2 — What a rocket is: the four systems

A rocket is four systems that must cooperate. Every amateur failure is one system working fine while
another fails.

| System | Job | Typical failure |
|---|---|---|
| **Structure** | Hold everything together, fly straight | Breaks, flexes, goes unstable |
| **Propulsion** | Produce thrust for a controlled time | Won't ignite, over-pressurises, bursts |
| **Recovery** | Bring it down intact | Doesn't deploy, deploys too early, tears apart |
| **Avionics** | Know where it went and what it did | Loses telemetry, resets, false triggers |

## They are not independent

This is the part beginners miss:

- A **heavier recovery system** means less altitude.
- A **more powerful motor** means more structural load.
- A **longer burn** means more thermal load on the casing.
- A **bigger parachute** means more volume, which means less space for propellant.

Every decision trades against another. This is why we keep a **single source of truth** for design
numbers — so that when one changes, everyone knows.

## The vocabulary you need

| Term | Meaning |
|---|---|
| **Grain** | The solid propellant casting — the "fuel tank" of a solid motor |
| **Core / port** | The hole down the middle. Burning starts here. |
| **Web thickness** | How much propellant the flame must eat through |
| **Throat** | The narrowest part of the nozzle. Sets chamber pressure. |
| **Apogee** | Highest point of flight |
| **CATO** | Catastrophic failure — the motor bursts |
| **MEOP** | Maximum Expected Operating Pressure |
| **Static margin** | Stability measure, in body diameters |

---

# PAGE 3 — The physics that matters (1): thrust and impulse

## Thrust — Newton's third law

The motor throws mass backwards; the rocket goes forwards.

$$F = \dot{m} \times v_e$$

- `F` = thrust (newtons)
- `ṁ` (m-dot) = mass flow rate (kg/s) — how much stuff leaves per second
- `v_e` = exhaust velocity (m/s) — how fast it leaves

**Thrust is mass flow times exhaust velocity.** You can get thrust by throwing a lot of mass slowly,
or a little mass very fast. Real motors trade these off.

## Total impulse — the single most useful number

$$I_t = F_{avg} \times t_{burn}$$

Total impulse (newton-seconds, N·s) is the **area under the thrust curve**. It determines how high you
go. **Peak thrust does not.**

**Our first motor targets ~24 N·s.**

## Motor classes — the letters

Motors are classified by total impulse. **Each letter is double the previous.**

| Class | Total impulse (N·s) |
|---|---|
| A | 1.26 – 2.5 |
| B | 2.5 – 5 |
| C | 5 – 10 |
| **D** | **10 – 20** |
| **E** | **20 – 40** |
| F | 40 – 80 |
| G | 80 – 160 |
| H | 160 – 320 |
| K | 1,280 – 2,560 |
| O | 20,480 – 40,960 |

**Our 24 N·s motor is an E-class.** The IN-SPACe authorisation threshold (40,960 N·s) is roughly an
**O motor** — we are many orders of magnitude below it.

## Specific impulse — how good the propellant is

$$I_{sp} = \frac{I_t}{m_p \times g}$$

- `m_p` = propellant mass (kg) · `g` = 9.81 m/s²

`I_sp` is measured in **seconds** and tells you how much impulse you get per unit of propellant.

| Propellant | Realistic I_sp |
|---|---|
| **KNSB (ours)** | **115–130 s** |
| APCP (commercial high power) | 180–200 s |
| Liquid hydrogen/oxygen | 450 s |

**Why this matters enormously to us:** KNSB's lower `I_sp` means our motor must be **bigger and
heavier** than a commercial motor producing the same impulse. That is a mass-budget problem we design
around — not a surprise we discover at integration.

---

# PAGE 4 — The physics that matters (2): mass ratio and stability

## Mass ratio — the tyranny of the rocket equation

$$\Delta v = v_e \ln\left(\frac{m_0}{m_f}\right)$$

- `m_0` = mass at launch · `m_f` = mass at burnout · `Δv` = change in velocity

This says: **most of your rocket has to be propellant, and the structure has to be light.** Real
orbital rockets are ~90% propellant by mass.

Our first rocket: **306 g dry + 24 g propellant = 7% propellant fraction.** Very low — because it is a
trainer, not a performance vehicle.

## Stability — the concept beginners get wrong most

Two centres:

| Term | Meaning |
|---|---|
| **CG** — Centre of Gravity | Where the mass balances. Where gravity pulls. |
| **CP** — Centre of Pressure | Where aerodynamic forces balance. Where the wind pushes. |

### The rule

> 🔴 **The CP must be BEHIND the CG** (further from the nose). Then if the rocket tips, the wind pushes
> the tail back and it self-corrects.

| Situation | Result |
|---|---|
| CP behind CG | ✅ **Stable** — corrects itself |
| CP ahead of CG | ❌ **Unstable** — tumbles |
| CP too far behind CG | ⚠️ Over-stable — turns *into* the wind (weathercocking) |

### Static margin — how we measure it

$$\text{Static margin} = \frac{x_{CP} - x_{CG}}{d}$$

- `x_CP` and `x_CG` measured from the nose tip (mm)
- `d` = body diameter (mm)

**Measured in "calibers" (body diameters). Target 1–2.**

- **Below 1** → marginal, risky
- **1 to 2** → correct
- **Above 2** → too stable, weathercocks into the wind

### Why fins exist

**Fins move the CP backwards. That is their entire job.** Bigger fins = CP further back = more stable.

### The trap: CG moves during flight

As propellant burns, the CG moves. If it moves **forward**, stability increases. If it moves
**backward**, you can go unstable mid-flight.

> **Always check the CG at burnout, not just at launch.**

---

# PAGE 5 — Propulsion

## What a solid propellant is

An **oxidiser** and a **fuel**, mixed and cast into a solid. Burning is the oxidiser giving up oxygen
to the fuel, very fast.

## KNSB — ours

**65% potassium nitrate (KNO₃) / 35% sorbitol, by mass.** Melt-cast.

| Property | Value |
|---|---|
| Ideal cast density | **1.841 g/cm³** |
| Casting temperature | **120–130 °C** |
| Auto-ignition | **> 300 °C** |
| Practical I_sp | 115–130 s |

**Why sorbitol and not sugar?** Sorbitol does not caramelise when heated, so the pot life is
effectively unlimited and it casts with fewer voids. It is also less hygroscopic.

## Burn rate — how fast the surface recedes

$$r = a \cdot P^n$$

- `r` = burn rate (mm/s) · `P` = chamber pressure
- `a` = burn-rate coefficient · `n` = pressure exponent

**Burn rate increases with pressure.** Higher pressure → faster burn → more gas → higher pressure.
This feedback is why motor design is stable *only if* `n < 1`.

### 🔴 KNSB is a "mesa" propellant

This matters. Most propellants follow one power law across all pressures. **KNSB does not.** Its
pressure exponent changes with pressure regime, and over some ranges it becomes very small or even
negative.

**Consequence:** you cannot use a single `a`, `n` pair. You must measure them **for your materials, in
your operating pressure range.** We do this with a **strand burner**.

**Measured anchor points for KNSB:** 2.59 mm/s at 1 atmosphere; 11.25 mm/s at 6.89 MPa.

## Kn — what sets the chamber pressure

$$K_n = \frac{A_b}{A_t}$$

- `A_b` = burning surface area · `A_t` = throat area

Chamber pressure settles where **gas generated** (burning area × burn rate) equals **gas leaving**
(throat area). Bigger throat → lower pressure. This is why the throat is the controlling feature.

## Grain geometry — shaping the thrust curve

A hole down the middle means the burning area **grows** as it burns.

| Type | Burning area | Thrust curve |
|---|---|---|
| **Progressive** | Grows | Rising |
| **Neutral** | Constant | Flat — most efficient |
| **Regressive** | Shrinks | Falling |

**You cannot independently choose impulse, thrust, burn time and grain size. Pick two; the rest
follow.** Burn time is fixed by geometry alone: **web thickness ÷ burn rate.**

## Why our grains are "freestanding"

KNSB's measured properties:
- Elastic modulus **5.84 GPa** (like bakelite)
- Tensile strength **7.2 N/mm²** (like particleboard)

**Strong in compression, weak in tension.** A freestanding grain loads almost purely in compression →
reliable. A case-bonded grain loads in tension → cracks → bursts.

## Erosive burning

Gas flowing along the burning surface can increase burn rate. KNSB is unusually prone to the
**opposite** — *negative* erosive burning. Mitigation: keep **port-to-throat area ratio ≥ 2**.

---

# PAGE 6 — Structures and aerodynamics

## The loads

Thrust, drag, bending from wind, landing shock, and the **deployment shock** from the recovery
system — all acting on one tube.

**Design requirements we must meet:**
- Survive **15 g launch acceleration**
- Survive **30 g shock**
- Casing must burst at **no more than 2.5 × MEOP**
- Absolute minimum design margin **1.5 ×**

### 🔴 Why an *upper* limit on strength?

A thick "boilerplate" casing **stores more energy before it fails**. When it does fail, it fails
worse. A casing that is *just* strong enough is safer than one that is enormously over-strength,
because it fails earlier and with less energy.

## Materials — and why not PVC

| Material | Failure mode |
|---|---|
| **Kraft paper / phenolic** | **Splits** — safe |
| Aluminium | Dents, then tears |
| **PVC** | 🔴 **Shatters into shrapnel** |

PVC is the amateur default because it is cheap and available. It is also the most dangerous common
choice. **We use paper or phenolic for first motors.**

## Buckling

Thin tubes do not usually fail by exceeding material strength. They fail by **buckling** — collapsing
under compression. This is why a thin wall can fail far below its material's rated stress.

## Fin flutter

An aeroelastic failure where fins vibrate and tear off. It scales with **span³** and inversely with
**thickness³** — so a slightly thicker fin is *dramatically* more flutter-resistant. This is why "make
the fins a bit thicker" is usually good advice and "make them much bigger" usually is not.

---

# PAGE 7 — Recovery

## Why recovery is not optional

Kinetic energy must be dissipated before the rocket arrives. The only safe way is a **parachute**.

## Descent rate — the number that matters

$$v = \sqrt{\frac{2mg}{\rho \, C_d \, A}}$$

- `m` = mass of the descending section (kg) · `g` = 9.81 m/s²
- `ρ` = air density (≈ 1.2 kg/m³) · `C_d` ≈ 0.75 for a flat circular canopy
- `A` = canopy area = πD²/4

**Target 2–5 m/s.** We size for **~3.5 m/s** — the middle of the band — so we have margin on both
sides.

**Below 2 m/s** → canopy too large, drifts far, more material.
**Above 5 m/s** → landing damage, and it fails the competition requirement.

## 🔴 No pyrotechnics

The competition **prohibits pyro devices anywhere in the rocket**, including parachute activation.

So deployment must be **servo-actuated**, solenoid, or similar. This is a real engineering constraint,
not a preference.

## Redundant chains

> **The recovery system must deploy even if the primary flight computer dies completely.**

Therefore: **two independent computers, two power sources, two deployment chains.** The competition
requires an independent **COTS backup altimeter** wired into a redundant chain. Teams without it are
**not permitted to launch**.

## Apogee detection — harder than it looks

"Pressure stops falling and starts rising" is not sufficient. Real problems:

| Problem | Mitigation |
|---|---|
| Accelerometer spike at burnout | Use the **barometer** as primary for apogee |
| Pressure noise | Require **N consecutive samples** |
| Pad-side drift | Re-zero immediately before launch |
| False trigger on the pad | **Altitude gate** — never deploy below ~30 m |

**And always latch the deployment state.** Once deployed, never un-deploy.

---

# PAGE 8 — Avionics

## What the flight computer does

1. **Detect launch**
2. **Log data** — pressure, altitude, acceleration, orientation, voltage
3. **Detect apogee**
4. **Trigger deployment**
5. **Telemeter** it all to the ground

## The sensors

| Sensor | Measures | Note |
|---|---|---|
| **Barometer** | Pressure → altitude | Primary for apogee. Must be zeroed at the pad. |
| **IMU** (accel + gyro) | Acceleration, orientation | Needs **±16 g or more** for rocketry |
| **GNSS** | Position, time | Slow to get a fix; needs sky view |
| **Thermocouple** | Temperature | For motor casing during static tests |

## Power

⚠️ **LiPo batteries are prohibited by the competition.** Li-ion cells must be **metal-cased** (like
18650s). Alkaline, NiCad and NiMH are allowed.

⚠️ **Spring contacts are prohibited** for battery connections — shock causes momentary disconnects.
**Solder or screw terminals.**

**Budget for 30 minutes of pad wait** plus flight operations.

## Telemetry and the ground station

The competition requires **≥ 1 Hz**, ASCII comma-separated, in an exact field order, with the file
named `Flight_<TEAM_ID>.csv`. The ground station must plot every field **in real time** in SI units.

**Radio options:** XBee/Zigbee or LoRaWAN (both specified by the rules). Rocket and payload need
**separate channels** to avoid interference.

## The state machine

```
0 BOOT → 1 TEST_MODE → 2 LAUNCH_PAD → 3 ASCENT
      → 4 PAYLOAD_SEP → 5 DESCENT → 6 AEROBREAK_RELEASE → 7 IMPACT
```

**Must recover correctly after a processor reset**, keeping the mission clock.

## Why a stalled servo can ruin your flight

A small servo can draw **1–2 A** when stalled — versus ~200 mA moving. If that comes from the same
regulator as the flight computer, the rail collapses and **the computer resets at exactly the moment
it is trying to deploy the parachute.**

**Fix:** separate power rail for servos, plus a large reservoir capacitor.

---

# PAGE 9 — Safety: the Swiss Cheese Model

## The model

Imagine several slices of Swiss cheese in a row. Each slice is a **barrier** against an accident. Each
has **holes** — weaknesses. An accident happens when the **holes in every slice line up**.

**No single barrier is perfect. Safety comes from having many independent barriers.**

## Applying it to motor testing

| Slice (barrier) | Holes in it |
|---|---|
| **Design margin** | Wrong assumption, arithmetic error |
| **Quality control** | Undetected void in the grain |
| **Casing strength** | Material defect, wrong grade |
| **Remote ignition** | Someone forgot to shunt the leads |
| **Firing distance** | Not far enough for this motor size |
| **Hard cover** | Standing behind something too thin |
| **Two-person rule** | Working alone, tired, rushed |
| **Procedure** | Skipping a step because it seems unnecessary |

**A CATO is almost never one failure.** It is a void (slice 2) plus a thin casing (slice 3) plus
someone standing too close (slice 5) plus a skipped check (slice 8) — all on the same day.

## The energy argument

Sugar propellants release about **2.7 kJ per gram**.

- **1 kg holds 2.7 megajoules**
- That is a **1,000 W heater running 45 minutes**
- Released in **2–3 seconds**

**Respect is not optional.**

## The non-negotiables

1. **Never work alone** with energetic materials
2. **Remote ignition, always**, from behind hard cover
3. **Shunt the igniter leads** until the moment of connection
4. **Dunk bucket, fire extinguisher, and escape route** present whenever propellant is
5. **Firing distance: 75–100 m for proven motors, more for new designs**
6. **One change at a time** between tests
7. **Small batches only**
8. **A Safe/Arm switch is only partial security** — you need an interlocked ignition box
9. **If it fails to fire, wait several minutes, then disconnect the igniter leads FIRST**
10. **Propellant work only at the sanctioned site** — never a hostel, lab, or workshop

## The membership filter

If you are a risk taker, careless, unwilling to follow safety practices without exception, or lack
respect for the safety of others — **amateur rocketry is not for you.** We would rather tell you now
than at a hospital.

---

# PAGE 10 — Regulation, and how this club works

## The Indian framework

| Threshold | Requirement |
|---|---|
| **Below 10,000 N·s** | No IN-SPACe authorisation. Inform local administration. |
| **10,000 – 40,960 N·s** | 30 days' prior intimation and advisory advised |
| **Above 40,960 N·s** | **IN-SPACe authorisation required** |

**Our first motor is ~24 N·s. The competition motor is ≤2,800 N·s.** Both are far below every
threshold.

**But launches always need local administration approval** (district collector, sub-divisional
magistrate, or designated authority), and custom propellants may prompt a **PESO** question.
Planning for that paperwork is part of the job, not an obstacle to complain about.

## What the club is

A group of students building real hardware, on a real test site, with real documentation. Nobody here
knew anything when they started.

## What we expect from you

| Expectation | Why |
|---|---|
| **Read the safety documents** | Non-negotiable before any energetic work |
| **Show up when you say you will** | Reliability is the scarcest quality in a student club |
| **Document what you do** | If it is not written down, the club loses it when you graduate |
| **Teach what you learn** | If you cannot show someone else, you have not learned it |
| **Ask when you do not know** | Guessing in rocketry is how people get hurt |
| **Respect the safety rules without exception** | Including when nobody is watching |

## What you get

- Training in a real engineering discipline
- Access to tools, tests, and hardware most students never touch
- A portfolio that means something, because you built it
- The experience of doing something genuinely difficult, successfully

## The one thing to remember

**This club will survive you.** Every senior graduates. The thing that makes a club last is not
brilliance — it is **documentation, teaching, and successors.** When you learn something, write it
down and teach it. That is the whole job.

---

*End of reader. You may keep this open during the test.*
