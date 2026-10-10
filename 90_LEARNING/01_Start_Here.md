# 01 — Start Here: Rocketry Fundamentals

**Everyone does this path. No exceptions, no specialisation yet.**

| | |
|---|---|
| **Time** | ~2 weeks at 3–4 hours/week |
| **Prerequisites** | None. Genuinely none. |
| **Cost** | Under ₹1,000 for the first build |
| **Ends with** | A rocket you built and flew, and the vocabulary to talk to any subsystem lead |

---

## 1. What a rocket actually is

A rocket is not one machine. It is **four systems that must all work, in the same flight, at the
same time.** Nearly every amateur failure is one system working fine while another fails.

| System | Job | Fails by | Our workspace folder |
|---|---|---|---|
| **Structure** | Hold everything together and fly straight | Breaking, flexing, going unstable | [`20_AEROSTRUCTURES/`](<../20_AEROSTRUCTURES/Structures_Design_Guide.md>) |
| **Propulsion** | Produce thrust for a controlled time | Not igniting, over-pressurising, burning unevenly | [`10_PROPULSION/`](<../10_PROPULSION/Motor_Design_Guide.md>) |
| **Recovery** | Bring it down without destroying it | Not deploying, deploying too early, tearing apart | [`30_AVIONICS/`](<../30_AVIONICS/Recovery_Electronics_and_Control.md>) |
| **Avionics** | Know where it is and what it did | Losing telemetry, resetting, false triggers | [`30_AVIONICS/`](<../30_AVIONICS/Flight_Computer_Architecture.md>) |

**The systems are not independent.** A heavier recovery system means less altitude. A more powerful
motor means more structural load. This is why we have a
[systems engineer](<../config/engineering_constants.md>) — somebody has to keep the interfaces
consistent.

---

## 2. The physics that actually matters

You do not need calculus to start. You need these six ideas.

### 2.1 Thrust — Newton's third law

The motor throws mass backwards; the rocket is pushed forwards.

$$F = \dot{m} \cdot v_e$$

- `F` = thrust (newtons)
- `ṁ` = mass flow rate (kg/s) — how much stuff leaves per second
- `v_e` = exhaust velocity (m/s) — how fast it leaves

**Read this again:** thrust is mass flow **times** exhaust velocity. You can get thrust by throwing a
lot of mass slowly, or a little mass very fast. Real motors trade these off.

### 2.2 Total impulse — the single most useful number

$$I_t = \int F \, dt \approx F_{avg} \times t_{burn}$$

Total impulse (newton-seconds) is the **area under the thrust curve**. It is what determines how high
you go. Peak thrust does not.

**Our first motor targets ~24 N·s.** For comparison, a commercial "D" motor is about 20 N·s.

### 2.3 Motor classes — the letters

Motors are classified by total impulse. Each letter is **double** the previous.

| Class | Total impulse (N·s) | Typical use |
|---|---|---|
| A | 1.26 – 2.5 | Tiny |
| B | 2.5 – 5 | Small |
| C | 5 – 10 | Small |
| D | 10 – 20 | **Our first target** |
| E | 20 – 40 | Our 24 N·s motor sits here |
| F | 40 – 80 | |
| G | 80 – 160 | |
| H | 160 – 320 | "High power" begins |
| I | 320 – 640 | |
| **K** | **1,280 – 2,560** | Competition-class |
| O | 20,480 – 40,960 | **IN-SPACe authorisation threshold** |

> The IN-SPACe threshold is **40,960 N·s** — roughly an O motor. Everything the club does for years
> will be far below it. Full details in
> [`../00_ADMINISTRATION/Institutional_Approvals_and_Compliance.md`](<../00_ADMINISTRATION/Institutional_Approvals_and_Compliance.md>).

### 2.4 Specific impulse — how *good* the propellant is

$$I_{sp} = \frac{I_t}{m_p \cdot g}$$

- `m_p` = propellant mass (kg) · `g` = 9.81 m/s²

`I_sp` is measured in **seconds** and tells you how much impulse you get per unit of propellant. It is
the efficiency number.

| Propellant | Realistic I_sp |
|---|---|
| **KNSB (ours)** | **115–130 s** |
| APCP (commercial high power) | 180–200 s |
| Liquid hydrogen / oxygen | 450 s |

**Why this matters to us:** KNSB's lower `I_sp` means our motor will be **bigger and heavier** than a
commercial motor producing the same impulse. That is a mass-budget problem we design around, not a
surprise we discover at integration.

### 2.5 Mass ratio — the tyranny of the rocket equation

$$\Delta v = v_e \ln\left(\frac{m_0}{m_f}\right)$$

- `m_0` = mass at launch · `m_f` = mass at burnout

The rocket equation says: **most of your rocket has to be propellant, and the structure has to be
light.** This is why rockets are ~90% propellant by mass and why every gram of structure costs you
altitude.

Our first rocket is ~306 g dry + 24 g propellant. That is a **propellant fraction of 7%** — very low,
because it is a trainer, not a performance vehicle.

### 2.6 Stability — CG, CP, and the static margin

This is the concept beginners get wrong most often, and it is the one that makes rockets fly sideways.

| Term | Meaning |
|---|---|
| **CG** — Centre of Gravity | Where the mass balances. Think of it as where gravity pulls. |
| **CP** — Centre of Pressure | Where the aerodynamic forces balance. Think of it as where the wind pushes. |

**The rule:**

> 🔴 **The CP must be BEHIND the CG** (further from the nose). Then, if the rocket tips, the wind
> pushes the tail back and it self-corrects.

| Situation | What happens |
|---|---|
| CP behind CG | ✅ **Stable** — corrects itself |
| CP ahead of CG | ❌ **Unstable** — tumbles |
| CP too far behind CG | ⚠️ Over-stable — turns *into* the wind and flies sideways (weathercocking) |

The distance is measured in **calibers** (body diameters):

$$\text{Static margin} = \frac{x_{CP} - x_{CG}}{d}$$

**Target 1–2 calibers.** Below 1 is marginal. Above 2 causes weathercocking.

**Why fins work:** fins move the CP backwards. That is their entire job. Bigger fins = CP further
back = more stable.

**Why it changes during flight:** as propellant burns, the CG moves. If it moves *forward*, stability
increases. If *backward*, you can go unstable mid-flight. **Always check the CG at burnout, not just
at launch.**

---

## 3. The vocabulary

Learn these and you can follow any conversation in the club.

| Term | Meaning |
|---|---|
| **Grain** | The solid propellant casting — the "fuel tank" of a solid motor |
| **Core / port** | The hole down the middle of the grain. Burning starts here. |
| **BATES grain** | Multiple grain segments stacked, with gaps between them |
| **Inhibitor** | A coating that stops a surface burning, so you control *where* it burns |
| **Web thickness** | How much propellant the flame must eat through. **Web ÷ burn rate = burn time.** |
| **Kn** | Burning area ÷ throat area. Governs chamber pressure. |
| **Throat** | The narrowest part of the nozzle. Sets the chamber pressure. |
| **MEOP** | Maximum Expected Operating Pressure |
| **CATO** | Catastrophic failure — the motor bursts |
| **Apogee** | Highest point of the flight |
| **Static margin** | CP − CG, in calibers. Target 1–2. |
| **Weathercocking** | Turning into the wind because of over-stability |
| **Erosive burning** | Gas flow across the surface increasing burn rate — can burst a motor |
| **Delay** | The pause between burnout and ejection |
| **Drogue / main** | Small parachute first, then the big one |
| **Shock cord** | The tether between rocket sections — takes the deployment load |
| **CO₂ / pyro** | Ejection methods. **We do not use pyro — prohibited by competition rules.** |

---

## 4. First build — pick one

### Option A — Water rocket (₹300, safest, fastest)

**Do this if the club has no budget this week.** It teaches stability, fin alignment, recovery and
range discipline with no propellant at all.

- **Materials:** a 2 L PET bottle, a cork or rubber bung, a bicycle pump, cardboard or plastic fins,
  duct tape, a launch rail (a broom handle works)
- **Build:** tape three or four fins around the neck, add a nose cone made from a rolled cone of
  paper, and add a small parachute under the nose cone
- **Fly:** fill ⅓ water, pump to ~4 bar, release
- **What you will learn:** why fin alignment matters (your first one *will* spin), why the CG must be
  forward, how a parachute deploys, how far a "small" flight actually drifts

> ⚠️ **Never pump a PET bottle above its rated pressure, and never stand over it.** A burst bottle
> is genuinely dangerous. Point it away from people, and pressurise from the side.

**Deliverable:** photo, measured mass, altitude estimate (trigonometry from a known distance is fine),
and one thing that went wrong.

### Option B — Low-power kit rocket (₹800–2,500)

**Do this if you can source a commercial A–C motor.** These are available from Indian hobby
suppliers, though stock varies — ask the Operations Lead before ordering.

- Build it exactly per the instructions. Do not improvise on your first rocket.
- Fly it, recover it, fly it again.

**Deliverable:** the same as Option A, plus the measured altitude from the motor's published data
compared against what you observed.

### What to record either way

| Record | Why |
|---|---|
| Measured mass (g) | You will need this skill constantly |
| CG location (mm from nose) | Half of the stability calculation |
| Photo before flight and after recovery | Evidence, and it is how you spot damage |
| What went wrong | **The most valuable entry.** Everything teaches you something. |

---

## 5. Checkpoints

### After Foundation — you should be able to:

- [ ] Name the four systems and say what each does
- [ ] Explain why CP must be behind CG, in your own words
- [ ] Calculate total impulse from a thrust curve
- [ ] Convert between motor classes and N·s
- [ ] Explain why KNSB gives a bigger motor than APCP for the same impulse
- [ ] Say what static margin is and what value we target
- [ ] Build and fly a water rocket or kit rocket that goes roughly straight
- [ ] State the safe distance rule and why distance is the primary safety measure

### Then move to Week 3

Pick **two** paths from the [master index](<README.md>) and do their Foundation tier. You are
sampling, not committing.

---

## 6. What NOT to do at this stage

| ❌ Don't | Why |
|---|---|
| Start with propellant | Highest risk, lowest learning-per-hour, and you have not earned the safety induction yet |
| Try to build the competition rocket | You would be solving ten problems you cannot yet name |
| Buy expensive equipment | A ₹900 scale and ₹900 calipers will carry you for months |
| Skip the water rocket because it "isn't real rocketry" | It teaches the same stability and recovery physics as a real rocket, at 1% of the cost and risk |
| Read for three weeks without building | Reading without building does not stick. Build in week 2, always. |

---

## 7. Where to go next

| If you found yourself most interested in… | Go to |
|---|---|
| The maths — trajectory, stability, prediction | [`02_Simulation.md`](<02_Simulation.md>) |
| How the motor works | [`03_Propulsion.md`](<03_Propulsion.md>) |
| Building and flying the airframe | [`04_Structures_and_Aero.md`](<04_Structures_and_Aero.md>) |
| Electronics and code | [`05_Avionics.md`](<05_Avionics.md>) |
| All of it, and you cannot choose | [`02_Simulation.md`](<02_Simulation.md>) — it touches every other subsystem |

---

## 8. Resources for this path

| Resource | Cost | What it is good for |
|---|---|---|
| [NASA Beginner's Guide to Rockets](https://www.grc.nasa.gov/www/k-12/rocket/) | Free | **Start here.** Plain-language, correct, no maths barrier |
| [NASA Beginner's Guide to Aeronautics](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/) | Free | Aerodynamics and stability, explained properly |
| [OpenRocket](https://openrocket.info/) | Free | Simulation — install it in week 1 |
| [`../Technical_Reference_Nakka.md`](<../Technical_Reference_Nakka.md>) | Free | Our own propellant and safety reference |
| [`../UVCE_Rocketry_Roadmap.md`](<../UVCE_Rocketry_Roadmap.md>) | Free | Where the club is going and why |
| [r/rocketry wiki](https://www.reddit.com/r/rocketry/) | Free | Beginner FAQ, and a place to ask questions |
| *Handbook of Model Rocketry* — G. Harry Stine | ~₹1,500 | The classic text. Buy when the club has funds. |
