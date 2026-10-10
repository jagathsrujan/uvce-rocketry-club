# 02 — Simulation Path

**Trajectory, stability, and knowing whether your answer is believable.**

| | |
|---|---|
| **Time** | Foundation 2 weeks · Working 4–6 weeks · Advanced months |
| **Prerequisites** | [`01_Start_Here.md`](<01_Start_Here.md>) |
| **Cost** | ₹0 — everything here is free |
| **You will need** | A laptop. Any laptop. |
| **Workspace docs** | [`../50_SIMULATION/`](<../50_SIMULATION/OpenRocket_Workflow.md>) |

> **Why this path is a good default:** it touches every other subsystem, requires no hardware, costs
> nothing, and can be done at a desk at 11 pm. If you cannot choose a path, choose this one.

---

## FOUNDATION (2 weeks)

### Learn

1. **What simulation is for** — and what it is *not* for. Simulation predicts; it does not prove.
   A simulation is a hypothesis you test with a flight.
2. **OpenRocket basics** — the part tree, entering dimensions, running a simulation, reading the plot.
3. **The outputs that matter** — apogee, max velocity, stability margin over time, rail exit velocity,
   descent rate.
4. **The four numbers that decide a design:**
   - **Static margin** — 1–2 calibers
   - **Rail exit velocity** — fast enough to be stable before leaving the rail
   - **Thrust-to-weight** — at least 5:1 at launch
   - **Descent rate** — 2–5 m/s for competition

### Do

- Install OpenRocket. Open our reference rocket if one exists, or build one from scratch.
- Build the **40 mm reference rocket**: 900 mm body, ogive nose cone, 3 trapezoidal fins.
- Enter realistic component masses — **this is where beginners go wrong.** A simulation with guessed
  masses is fiction.
- Run it with a 24 N·s motor and see what happens.

### Checkpoint — you can:

- [ ] Build a complete rocket in OpenRocket from a dimensioned sketch
- [ ] Enter a motor from a thrust curve
- [ ] Explain what static margin means and read it off the plot
- [ ] Say whether a given design is stable, and why
- [ ] Explain why a simulation with guessed masses is worthless

---

## WORKING (4–6 weeks)

### Learn

1. **The Barrowman method** — how CP is actually calculated, by hand. You should do this **once**,
   manually, even though OpenRocket does it for you. Otherwise you are trusting a number you do not
   understand.
2. **Drag** — skin friction, form drag, base drag. Why Cd ≈ 0.45 is a starting guess and how to
   correct it from real flight data.
3. **Off-nominal analysis** — what happens with +5% mass, −10% thrust, wind from four directions,
   launch angle variation.
4. **Dispersion** — where the rocket might land, and why range safety depends on knowing this.

### Do

- **Hand-calculate the Barrowman CP** for the 40 mm rocket and compare against OpenRocket. If they
  disagree, find out why. This is the single most educational exercise in this path.
- **Batch simulation** — run 100+ off-nominal cases and plot the landing dispersion.
- **Validate against a real flight** — fly something with an altimeter, compare measured apogee
  against predicted, and adjust your drag coefficient until they agree.

> 🔴 **The validation step is what separates simulation from fiction.** Anyone can produce a plot.
> The person who checks it against reality is doing engineering.

### Checkpoint — you can:

- [ ] Hand-calculate CP with the Barrowman method and justify the result
- [ ] Run a batch simulation and produce a dispersion ellipse
- [ ] Explain the gap between predicted and measured apogee
- [ ] Tell a subsystem lead what the worst-case apogee and range are, with numbers
- [ ] Say which of your inputs you trust and which you are guessing

---

## ADVANCED (months)

- **6-DOF simulation** — full rigid-body dynamics, not just point-mass
- **CFD** — OpenFOAM or SimScale, for fin and nose cone drag
- **Monte Carlo analysis** — probabilistic dispersion rather than discrete cases
- **Custom tooling in Python** — your own trajectory integrator, so you understand every assumption
- **Motor internal ballistics codes** — coupling grain regression to chamber pressure (see
  [`03_Propulsion.md`](<03_Propulsion.md>))

### Checkpoint — you can:

- [ ] Explain the assumptions in OpenRocket's point-mass model and when they break
- [ ] Write your own trajectory integrator and match OpenRocket
- [ ] Produce the dispersion and risk analysis needed for an IN-SPACe advisory submission
- [ ] Teach the Barrowman method to a new member

---

## First build

**Model our reference rocket and validate the stability margin.**

| Step | Output |
|---|---|
| 1 | OpenRocket file for the 40 mm rocket |
| 2 | Hand Barrowman calculation on paper (photograph it) |
| 3 | Comparison table: hand calculation vs OpenRocket |
| 4 | Off-nominal batch run with dispersion plot |
| 5 | One-page write-up in `70_REPORTS/` |

**If the hand calculation and OpenRocket disagree by more than 5%, do not move on.** Find the
discrepancy. That investigation is the actual learning.

---

## Resources

| Resource | Cost | What it is good for |
|---|---|---|
| [OpenRocket](https://openrocket.info/) | Free | The tool. Runs on Java, works on Windows/Mac/Linux |
| [OpenRocket User Guide](https://openrocket.readthedocs.io/en/latest/) | Free | The manual. Read it properly, do not guess at menus |
| [OpenRocket Tutorials](https://openrocket.info/tutorials/) | Free | Newer, task-oriented walkthroughs |
| [OpenRocket Technical Documentation (PDF)](https://github.com/openrocket/openrocket/releases/download/OpenRocket_technical_documentation-v13.05/OpenRocket_technical_documentation-v13.05.pdf) | Free | The maths behind it. Dense but authoritative. |
| [OpenRocket Resources wiki](https://wiki.openrocket.info/Resources) | Free | **Includes Barrowman's original report** and experimental rocket data |
| [NASA Beginner's Guide to Aeronautics](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/) | Free | Aerodynamics fundamentals |
| [`../50_SIMULATION/OpenRocket_Workflow.md`](<../50_SIMULATION/OpenRocket_Workflow.md>) | Free | Our own task-specific guide |
| [`../50_SIMULATION/Motor_Files.md`](<../50_SIMULATION/Motor_Files.md>) | Free | How to get *our* motor into the simulator |
| [`../50_SIMULATION/Simulation_Plan_and_Validation.md`](<../50_SIMULATION/Simulation_Plan_and_Validation.md>) | Free | Error sources and validation methodology |
| [RASAero](https://www.rasaero.com/) | Free | Alternative to OpenRocket; better supersonic drag modelling |

### Books (later, if you go deep)

| Book | Why |
|---|---|
| *Handbook of Model Rocketry* — Stine | The classic; stability chapters are excellent |
| *Topics in Advanced Model Rocketry* — Mandell, Caporaso, Bengen | The next level up |
| *Rocket Propulsion Elements* — Sutton | For coupling flight sim to motor performance |

---

## What NOT to do

| ❌ | Why |
|---|---|
| Trust a simulation with guessed masses | Garbage in, garbage out. Weigh everything. |
| Assume Cd = 0.45 forever | It is a starting guess. Correct it from flight data. |
| Skip the hand calculation | You will not know when the software is wrong — and it sometimes is |
| Model the rocket perfectly but ignore wind | Wind dominates dispersion for small rockets |
| Present a simulation as evidence | It is a prediction. Only a flight is evidence. |
