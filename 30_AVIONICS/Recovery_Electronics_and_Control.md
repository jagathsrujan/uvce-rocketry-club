# Recovery Electronics and Control Systems

**UVCE Rocketry Club — Avionics Guide 4**

| | |
|---|---|
| **Document** | `30_AVIONICS/Recovery_Electronics_and_Control.md` |
| **Applies to** | Recovery system design, deployment electronics, and any active control system |
| **Companion documents** | `Flight_Computer_Architecture.md`, `Sensors_and_Instrumentation.md`, `Communications_and_Ground_Station.md` |
| **Status** | 🟡 Design guidance. All deployment mechanisms require ground testing before flight. |

> 🔴 **THE COMPETITION BANS PYROTECHNICS ANYWHERE IN THE ROCKET.**
> Rule 5.xi: *"The teams shall not use any Pyro technique devices at any part of the Rocket,
> including but not limited to CAN-7USAT Separation Systems, Parachute Activation Systems etc."*
> Teams using pyro devices are **not permitted to carry out preparatory activities at the site**.
> This is not a preference — it is a disqualification risk. **Design for non-pyrotechnic deployment
> from the start.**

---

## 1. The core design principle

> **The recovery system must deploy even if the primary flight computer dies completely.**

Recovery is the one subsystem where failure means losing the vehicle, and often means a ballistic
return to ground. Every other subsystem can fail gracefully. This one cannot. Design accordingly:

1. **Two independent computers**, not two sensors on one processor
2. **Two independent power sources**
3. **Two independent deployment chains** (separate channels, separate charges/actuators)
4. **At least one chain that requires no software at all** (a COTS altimeter)

The IN-SPACe rules make part of this mandatory: the launcher *"shall mandatorily have a back-up
Commercial-Off-The-Shelf (COTS) Altimeter, which shall be integrated in to the Redundant Chain for
initiating Separation of the launcher. Teams failing to adhere to this will not be permitted to
launch."* (rule 5.xv)

---

## 2. Non-pyrotechnic deployment mechanisms

An honest comparison. **There is no perfect option here** — each has real drawbacks.

| Mechanism | How it works | Reliability | Mass | Current | Failure modes | Verdict |
|---|---|---|---|---|---|---|
| **Servo-actuated release** | Servo rotates a pin/latch, releasing a spring-loaded door or the nose cone | High if mechanically over-centre | 10–25 g | 200 mA–1 A peak (stall) | Servo stall, gear stripping, brown-out of the bus, jamming under load | ✅ **Recommended primary** |
| **Solenoid release** | Solenoid retracts a pin | High | 20–40 g | 0.5–2 A continuous | High continuous current, heat, sticking | 🟡 Viable but power-hungry |
| **Nichrome burn-wire** | Current heats a wire that severs a tie or burns through a retaining line | Medium | 5 g | 1–2 A for ~1 s | Wire fails to cut, cuts too slowly, severs the wrong thing | ⚠️ **See §2.1** |
| **Spring-loaded + latch** | Passive spring held by a latch; any release mechanism trips it | High | 15 g | 0 (passive) | Latch vibration release (premature), spring force insufficient | ✅ Good as the *stored energy* half of a servo system |
| **Pressure/altitude mechanical** | A bellows or diaphragm trips a latch at a set pressure | Low | 20 g | 0 | Calibration drift, temperature sensitivity | ❌ Not reliable enough |
| **Burn-through of a rubber band / O-ring** | Same as nichrome but with a combustible link | Medium | 5 g | 1–2 A | Inconsistent burn, humidity effects | ❌ Avoid |

### 2.1 ⚠️ The nichrome burn-wire question

Nichrome burn-wire is technically a **thermal initiator**, not an explosive or a pyrotechnic
composition. It contains no energetic material — it is a resistive heating element. On a strict
reading it is **not** a "pyro technique device."

**But this is genuinely ambiguous**, and the consequence of being wrong is disqualification or being
barred from site preparation. Therefore:

> ⚠️ **If you intend to use nichrome burn-wire in a competition vehicle, obtain explicit written
> clarification from the jury before you design around it.** Ask the question through your faculty
> advisor — that is the only channel the organisers accept queries on. Do not assume.

**For club-internal flights** (not competition), nichrome burn-wire is a reasonable and widely used
amateur technique. It is still worth using a servo where mass allows, because a servo is
unambiguously not pyrotechnic.

### 2.2 Recommended architecture

```
                    ┌─────────────────────┐
   PRIMARY CHAIN    │  Flight computer    │──► Servo 1 ──► main parachute release
   (software)       │  + baro + IMU       │
                    │  battery A          │
                    └─────────────────────┘
                              ╳  no shared power, no shared signal path
                    ┌─────────────────────┐
   BACKUP CHAIN     │  COTS altimeter     │──► Servo 2  ──► redundant release on the
   (independent)    │  battery B          │                 SAME mechanism (or a
                    └─────────────────────┘                 separate one)
```

**Design rules:**

- The two chains must share **nothing** — not a battery, not a ground, not a connector.
- Ideally they act on **the same release mechanism in parallel**, so either one alone succeeds.
  Two independent mechanisms that both must fire is a worse design than one mechanism that either
  computer can trigger.
- The backup chain should be the **simpler** one. A COTS altimeter with a fixed deployment altitude
  and no configurability is a feature, not a limitation.
- **Test the backup chain by disabling the primary.** If you have never flown with the primary
  deliberately off, you do not know that the backup works.

---

## 3. Apogee detection — and why it is harder than it looks

### 3.1 The naive approach, and why it fails

> "Detect apogee when pressure stops falling and starts rising."

This fails on real data. Specific problems:

| Problem | What happens | Mitigation |
|---|---|---|
| **Motor burn-out acceleration spike** | The accelerometer sees a large transient; if you are integrating acceleration for velocity, that transient integrates into a large velocity error | Use the **barometer as primary** for apogee; use the accelerometer only for launch detection |
| **Mach transition pressure glitch** | Near Mach 1 the static pressure measured at the port drops sharply and can read as a false apogee (or a false launch) | Not a concern below ~250 m/s; apply a velocity gate — ignore pressure-derived apogee logic above a set speed |
| **Pressure noise** | Raw barometric data is noisy at 0.1 m resolution; a single noisy sample can look like a turnaround | Require **N consecutive samples** of falling-then-rising pressure, or apply a moving average / complementary filter |
| **Pad pressure drift** | Weather changes while you wait on the pad; the zero reference drifts | Re-zero immediately before launch, and use a **relative** rather than absolute threshold |
| **Ejection charge / deployment pressure transient** | The pressure spike from deployment (if any) can confuse the state machine | Latch the state — once you have committed to deployment, never go back |

### 3.2 A robust detection strategy

Use a **state machine with gating**, not a single comparison:

```
STATE: LAUNCH_PAD
  wait for: acceleration > 3 g sustained for 0.2 s   (launch detect)
     ↓
STATE: ASCENT
  start integrating; record max altitude so far
  wait for EITHER:
     (a) barometric altitude has decreased for 5 consecutive samples
         AND velocity (from baro rate) is negative
         AND altitude > 30 m          (prevents pad-level false triggers)
     OR  (b) backup timer expired      (T_backup, see §3.3)
     ↓
STATE: DEPLOY
  fire deployment; LATCH this state permanently
     ↓
STATE: DESCENT
  no further deployment actions
```

**Critical rules:**

- **Gate on altitude.** Never allow an apogee trigger below some minimum altitude (30–50 m is
  sensible for a 200 m flight). This prevents a pad-side pressure wobble from ejecting the parachute
  while the rocket is still on the rail.
- **Latch deployment.** Once deployed, never re-deploy and never revert state. A second deployment
  at 50 m is harmless; a spurious "return to ASCENT" could be catastrophic.
- **Require consecutive samples.** One noisy sample is not a trend.
- **For a 200 m flight the whole ascent is only a few seconds** — at 100 Hz you have plenty of
  samples, but at 1 Hz you have almost none. **Sample the barometer fast (≥ 50 Hz) even if you
  telemeter at 1 Hz.**

### 3.3 The backup timer

A timer is crude, but it is the only mechanism that works when **every sensor has failed**. Set it
generously:

$$T_{backup} \approx t_{burn} + t_{coast} + \text{margin}$$

For a 200 m flight with a 2–3 s burn, apogee occurs perhaps 6–9 s after ignition. A backup timer at
**12–15 seconds** would deploy well past apogee — the rocket would be descending, which is not ideal
but is far better than a ballistic return.

| Flight profile | Burn time | Coast to apogee | Suggested backup timer |
|---|---|---|---|
| 200 m, 24 N·s | ~2–3 s | ~4–6 s | **12 s** |
| 1 km, larger motor | ~3–5 s | ~10–15 s | **25–30 s** |

> ⚠️ A backup timer that fires **too early** is dangerous — it deploys the parachute during ascent
> at high speed, which will destroy the recovery system. **Err on the long side.**

---

## 4. Control surfaces and active stabilisation

### 4.1 ❌ Not recommended for this club yet

**Active stabilisation solves a problem we do not have.**

| System | What it is | Why we are not doing it yet |
|---|---|---|
| **Canards** | Small forward fins on actuators, to steer | Adds two failure modes (actuator, control law) to fix a problem that passive fins already solve |
| **Grid fins** | Lattice fins, often for guided descent | High drag, complex, only worth it for guided recovery |
| **Gimbal mount** | Motor pivots to vector thrust | Requires a flexible joint in the hottest, highest-pressure part of the vehicle |
| **TVC (thrust vector control)** | Actuators steer the motor nozzle or the whole motor | The hardest control problem in amateur rocketry. High consequence of failure |

### 4.2 Why passive fin stability is correct here

| Passive fins | Active control |
|---|---|
| Cannot fail — no power, no software | Fails if power, sensor, or software fails |
| Zero mass penalty beyond the fins themselves | Actuators, drivers, control law, extra power |
| Well understood, analytically predictable (Barrowman) | Requires tuning, and can be actively unstable if mistuned |
| Sufficient for a 200 m–1 km flight | Only needed for guided flight or recovery |

> **A passively stable rocket that flies straight is the goal. Active control adds risk without adding
> capability for our mission.** Revisit only if a future mission requires precision landing or
> guided recovery (an optional IN-SPACe objective).

---

## 5. Servo selection and the brown-out problem

### 5.1 Torque requirement

Estimate the force needed to release the mechanism, then apply a safety factor:

$$\tau_{required} = F_{release} \times r_{horn} \times SF$$

- `F_release` = force to pull the pin / trip the latch (measure it with a spring scale)
- `r_horn` = servo horn radius
- `SF` = safety factor, **at least 2**, preferably 3

Then add margin for the fact that the servo is holding against spring preload and vibration.

### 5.2 The stall current problem — this is the one that kills flights

> 🔴 **A stalled servo draws its full stall current continuously.** A small hobby servo can draw
> **1–2 A** stalled, versus ~200 mA moving. If that current comes from the same regulator as the
> flight computer, the rail voltage collapses and **the computer resets** — at exactly the moment it
> is trying to deploy the parachute.

**Mitigations, in order of preference:**

1. **Separate power rail for servos** — its own battery or its own regulator, with only a signal
   ground shared.
2. **Large reservoir capacitor** (1000 µF or more) on the servo supply, close to the servo.
3. **Mechanically avoid stall** — design the linkage so the servo reaches its end position and the
   load drops, rather than fighting a spring indefinitely.
4. **Current-limited driver** and a servo that is simply oversized for the job.

**Also:** the flight software should **command the servo, wait, then re-check** the deployment
sensor (if fitted), and should **cut servo power after deployment** to free the bus.

### 5.3 Servo specification checklist

- [ ] Torque ≥ 2× (preferably 3×) the measured release force × horn radius
- [ ] Operating voltage compatible with the chosen rail
- [ ] **Stall current measured** (not from the datasheet) and budgeted
- [ ] Metal gears if there is any shock load
- [ ] **Held at end position with no load** in the deployed state
- [ ] Bench-tested at the expected temperature
- [ ] Tested under vibration if possible

---

## 6. Failure modes and design for them

| Failure | Consequence | Design response |
|---|---|---|
| **Primary computer dies** | No deployment | Independent COTS backup chain |
| **Watchdog reset mid-flight** | State machine restarts, may re-detect launch or miss apogee | **Persist state to EEPROM/flash**; on boot, restore state and mission clock |
| **Brown-out from servo stall** | Computer resets at deployment | Separate servo rail + reservoir capacitor |
| **Servo jams** | No deployment on that chain | Second independent chain acting on the same mechanism |
| **Battery disconnects under shock** | Total loss | **No spring contacts** (the rules prohibit them for exactly this reason); soldered or screwed terminals; strain-relieve all wires |
| **Barometer port blocked** | No apogee detection | Route the port to undisturbed air, protect from ejection gas, and **test the port** |
| **False apogee on the pad** | Parachute deploys on the rail | Altitude gate + consecutive-sample requirement |
| **Deployment at high speed** | Recovery system torn apart | Backup timer set long, not short; structural margin on shock cord |
| **Parachute tangles** | High-speed landing | Pack carefully, ground-test deployment repeatedly |

### 6.1 Single point failure audit

For every subsystem, ask: **"if this one thing fails, does the rocket still come down safely?"**
Write the answer down. If the answer is no, either add redundancy or accept the risk explicitly and
record why.

| Subsystem | Single point? | Mitigation |
|---|---|---|
| Primary flight computer | Yes | COTS backup chain |
| Backup altimeter | Yes | Backup timer in the primary |
| Deployment mechanism (servo) | Yes | Two chains acting on one mechanism |
| Main parachute | Yes | Structural margin, careful packing, repeated ground tests |
| Shock cord | Yes | Over-specify the strength; inspect before every flight |
| Nose cone retention | Yes | Positive mechanical retention, verify by hand before flight |

---

## 7. Pre-flight arming and safe/arm architecture

The rules require remote ignition with an external power switch and indicator (rule 4.3) and that
the rocket **not transmit telemetry until commanded** (rule 5.2).

**Arming sequence (in order, no exceptions):**

1. Rocket fully assembled, **recovery system SAFE** (deployment inhibited in software *and*
   mechanically if possible)
2. Insert igniter **last**, leads **shunted**
3. Power on flight computer — verify boot state = `TEST_MODE`
4. Verify all sensors read plausibly (pressure, temperature, voltage, IMU)
5. Command telemetry ON via RF — verify ground station receives valid packets
6. Zero the barometer and accelerometer at the pad
7. Transition to `LAUNCH_PAD` state
8. Verify continuity on the igniter circuit
9. **ARM the recovery system** — this is the last step before the pad is cleared
10. Clear the pad, retire to the firing line, announce the countdown

> ⚠️ **Note the ordering principle:** the recovery system is armed *after* the rocket is otherwise
> ready, and the igniter is connected *last*. Never have an armed recovery system and an installed
> igniter while people are working on the vehicle.

---

## 8. Recovery system test plan

**Do not fly a recovery system you have not tested on the ground, repeatedly.**

### 8.1 Bench deployment tests (do these first, many times)

| Test | Method | Pass criterion |
|---|---|---|
| **Deployment actuation** | Command deployment on the bench, 20+ times | 100% actuation, no jams, no resets |
| **Servo current** | Measure peak and stall current with a shunt or clamp meter | Within budget; no rail collapse |
| **State machine** | Feed recorded/simulated pressure data | Deploys at the right point, never on the pad |
| **Backup chain isolation** | Disable primary, verify backup deploys | Backup works alone |
| **Brown-out** | Force a servo stall, watch the computer rail | No reset; if it resets, fix the power design |
| **Reset recovery** | Reset the processor mid-simulation | State and mission clock restored correctly |

### 8.2 Parachute deployment / drop tests

| Test | Method | Pass criterion |
|---|---|---|
| **Ejection test** | Deploy the parachute on the ground with the real mechanism and packing | Parachute extracts fully, no tangles, no damage |
| **Drop test** | Drop the rocket (or a mass-representative dummy) from height with the parachute deployed | Descent rate in the **2–5 m/s ±0.5** band |
| **Descent rate measurement** | Time the descent over a known height, or log barometric altitude during the drop | Measured rate inside the band, recorded |
| **Shock load** | Inspect all attachment points after the drop test | No deformation, no cracked fillets, no stretched knots |

**Descent rate calculation (for sizing the parachute):**

$$v_{descent} = \sqrt{\frac{2 m g}{\rho \, C_d \, A}}$$

- `m` = mass of the descending section (kg) — **remember the rocket and payload may descend
  separately, each needing its own parachute**
- `g` = 9.81 m/s²
- `ρ` = air density ≈ 1.2 kg/m³ at Bengaluru conditions (adjust for altitude/temperature)
- `C_d` = parachute drag coefficient (≈ 0.75–0.85 for a flat circular canopy; use 0.75 to be
  conservative)
- `A` = canopy area = π D²/4

Solve for the diameter `D` that gives a descent rate in the middle of the band (≈ 3.5 m/s) rather
than at the edge — you want margin on both sides.

> ⚠️ **The descent rate must be *measurable* during the competition** (rule 7.2). That means your
> telemetry must capture barometric altitude fast enough during descent to compute a rate. Plan for
> this in the telemetry design — it is a scored requirement, not just a safety one.

### 8.3 Repeat until boring

A recovery system that works once has not been tested. A recovery system that works **ten times in a
row** on the bench and **three times** in drop tests is approaching trustworthy. Log every test in
`60_TEST_DATA/`.

---

## 9. Checklist before any flight

- [ ] Primary and backup chains independently verified in the last 7 days
- [ ] Backup chain verified **with the primary disabled**
- [ ] Deployment tested on the bench at least 10 times since the last change
- [ ] Parachute descent rate measured and inside 2–5 m/s
- [ ] All shock cord attachment points inspected
- [ ] Battery terminals not spring-loaded; wires strain-relieved
- [ ] Servo stall current measured and budgeted
- [ ] Barometer port clear and protected from ejection gas
- [ ] State machine tested against recorded flight-like data
- [ ] Backup timer set (and set long, not short)
- [ ] Altitude gate active (no deployment below 30 m)
- [ ] Deployment state latches
- [ ] Arming sequence rehearsed with the whole team
- [ ] Recovery area identified and walkable
- [ ] Everything above recorded in the flight log

---

## 10. Sources

- IN-SPACe Model Rocketry India Student Competition 2026 — Mission Requirements and Competition
  Guidelines (Doc No. IN-SPACe.MR.Model.CG.01, Issue No.1, dtd 24.03.2026). Rules 4.3, 5.xi, 5.xv,
  5.2, 7.1–7.5.
- IN-SPACe advisory guidelines on Sub-Orbital Launches including Model Rocketry, April 2026 —
  remote ignition, safe distances, recovery and impact zone planning.
- Richard Nakka's Experimental Rocketry Site — recovery system and apogee detection practice.
- `Technical_Reference_Nakka.md` and `80_REFERENCE/nakka-technical-reference.md` in this workspace.
