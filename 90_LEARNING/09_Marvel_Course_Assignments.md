# 09 — Marvel Course Assignments by Subsystem

**Which Marvel track each recruit should take, and which tasks to do first.**

| | |
|---|---|
| **Companion to** | [`08_Marvel_Makerspace_Mapping.md`](<08_Marvel_Makerspace_Mapping.md>) (what exists) — this document is **who takes what** |
| **Status** | 🟡 Read from Marvel's public site, **October 2026**. Syllabi, eligibility and intake dates **change** — verify with Marvel. |
| **The one rule** | **Take ONE track. Cherry-pick tasks from others.** |

---

## 0. Read this before assigning anything

### Three constraints that shape every recommendation

**1. The tracks are long.** 6–11 months across 3–4 levels. A student cannot take two. Assigning
someone to "D-P-001 and AIR-001" is assigning them to fail both.

**2. The Student Track is a cohort programme that opens twice a year.** Admission is *"limited."*
So plan for a waiting period, and have the Open Learner Programme as the fallback.

**3. Everyone starts with the same generic tasks.** Every Marvel course shares a Level 0 / Level 1
block of generic tasks — Markdown, GitHub, Ubuntu, NumPy/Matplotlib, soldering, 3D printing. **That
common foundation is free to everyone and is exactly what we need.** Do it first, before
specialising.

### The assignment principle

| Layer | What | Who |
|---|---|---|
| **Common foundation** | Marvel's generic tasks (§1) | **Every member, no exceptions** |
| **Primary track** | One full course, chosen by subsystem (§2) | Assigned per person |
| **Cherry-picked tasks** | 2–4 specific tasks from other tracks | As needed |
| **Our own material** | Rocketry-specific training | Us, always |

---

## 1. The common foundation — everyone does these first

Do these **before** the cohort opens. They are self-paced, free, and prerequisite to everything.

| # | Task | Time | Why every rocketry member needs it |
|---|---|---|---|
| 1 | **Markdown article** | 1 h | Our entire workspace is Markdown. You cannot document without it. |
| 2 | **GitHub workflows** | 3 h | Version control stops the club losing knowledge at graduation |
| 3 | **Ubuntu command line** | 2 h | OpenRocket, Python, ground station all live there |
| 4 | **NumPy + Matplotlib** | 1 week | 🔴 **Thrust curve plotting and analysis.** You will do this constantly. |
| 5 | **Soldering prerequisites** | 2 h (supervised) | Every avionics member. Also useful for everyone. |
| 6 | **3D printing + SOPs** | 2 h (supervised) | Nose cones, sleds, jigs — and it teaches SOP discipline |
| 7 | **Datasheet report writing** | 3 h | 🔴 **Reading a sensor datasheet is a core engineering skill** |

**Where these live:** generic Level 0/1 block of *any* Marvel course (AIR-001, D-P-001 and IOT-001
all carry them). If you are not enrolled, they are available through the **Open Learner Programme**.

> ⚠️ **Task 4 is the highest-value item on this list for us.** A member who can load a CSV of thrust
> data and plot it has already become useful. Everything else can wait.

---

## 2. Primary track by subsystem

| Subsystem | **Primary track** | Why this one | Duration |
|---|---|---|---|
| **Propulsion** | **D-P-001** Design & Prototyping | Precision CAD, GD&T, mechanisms, CAM/G-code for machining the nozzle | 6 months |
| **Structures & Aero** | **D-P-001** Design & Prototyping | CAD, assemblies, mechanisms, snap joints, sheet metal, CFD | 6 months |
| **Avionics — hardware/software** | **IOT-001** Internet of Things | 🔴 **ESP32, sensors, I²C/SPI, real-time dashboards, data logging** | 6 months |
| **Avionics — comms/systems** | **AIR-001** Aviation & Drone Science | RF, LoRa, link budget, flight controller config, SITL, flight data | 8 months |
| **Simulation** | **AIR-001** Aviation & Drone Science | MATLAB/Simulink, PID, aerodynamics, flight data analysis | 8 months |
| **Operations** | **VFX-001** (2 months) + generic web/Markdown tasks | Media, documentation, club web presence — short and immediately useful | 2 months |
| **Safety Officer** | *No full track* — cherry-pick (§3) | Needs two specific tasks, not a 6-month course | — |
| **Documentation Lead** | *No full track* — cherry-pick (§3) | Markdown + web app tasks are the whole job | — |
| **Team Lead / Systems** | *No full track* — cherry-pick (§3) | Needs breadth, not depth in one toolchain | — |

### Why IOT-001 for avionics hardware

I initially expected AIR-001 to be the avionics course. Reading IOT-001's syllabus changed that. It
maps almost task-for-task onto our flight computer and ground station:

| IOT-001 task | What it is | Our equivalent |
|---|---|---|
| **1a — Digital I/O & interrupts** | GPIO, pull-up/down, interrupt-driven handling | Flight computer I/O, launch detect |
| **2 — Temperature-based fan control** | Sensor → serial → **threshold** → motor driver → actuator | 🔴 **Apogee detect → deployment. Same pattern.** |
| **3a — MQTT, HTTP, I2C, SPI** | Communication protocols | 🔴 **I²C and SPI are our sensor buses** |
| **3b — MQTT publish/subscribe** | Remote control of hardware | Telemetry uplink/downlink pattern |
| **4 — I2C between two ESP32s** | Wired MCU-to-MCU | Sensor bus, and two-chain redundancy |
| **5 — ThingSpeak + regression + Matplotlib** | Publish data, retrieve, plot vs time | 🔴 **Telemetry logging + thrust curve analysis** |
| **7 — Health vitals dashboard** | 🔴 **Real-time graph plotting on a webserver** | 🔴 **This IS the ground station** |
| **Level 3 / 1 — Solenoid valve + relay, threshold-triggered** | Automated actuation | 🔴 **Non-pyro deployment mechanism** |
| **Level 3 / 3 — Node-RED real-time dashboard** | Sensor fusion + live monitoring + alerts | 🔴 **Ground station architecture** |
| **Level 3 / 4 — Cloud data logging** | Logging with timestamps | Flight data logging and archiving |

> ✅ **Verdict: IOT-001 is the closest thing Marvel offers to a flight-computer-and-ground-station
> course.** It uses the ESP32 — the same chip our
> [`Flight_Computer_Architecture.md`](<../30_AVIONICS/Flight_Computer_Architecture.md>) recommends.

---

## 3. Cherry-picked tasks — do these regardless of track

These are too valuable to leave behind a 6-month commitment.

### 🔴 For EVERY member — non-negotiable

| Task | From | Why |
|---|---|---|
| **"Rules in the Rule Book Written by Blood"** | AIR-001 Level 3 | **Swiss Cheese Model accident analysis.** This is how you think about CATO prevention. Technical, human and environmental failures aligning. **Make it a club requirement.** |
| **DGCA regulations study** | AIR-001 Level 2 | Regulatory framework thinking — parallels our IN-SPACe / PESO compliance work |

### By subsystem

| Subsystem | Cherry-pick | From |
|---|---|---|
| **Propulsion** | GD&T · 3D drafting · **Piston/crankshaft + CAM/G-code** | D-P-001 L2 Mechanical |
| **Structures** | Aerodynamics & stability · **Airfoil design + CFD** | AIR-001 L2 |
| **Avionics** | **PCB design in Altium** · STM32 custom board · DSP/convolution (sensor filtering) | D-P-001 L2 Electronic |
| **Avionics** | RF communication · LoRa · flight controller config · **SITL simulation** | AIR-001 L2–L3 |
| **Simulation** | **MATLAB/Simulink Onramp** · PID · **flight data logging & analysis** | AIR-001 L3 |
| **Simulation** | CFD (wind tunnel, lift force) | D-P-001 L2 / AIR-001 L2 |
| **Operations** | Express web app · laser engraving | D-P-001 |
| **Safety Officer** | Swiss Cheese · DGCA | AIR-001 L2–L3 |
| **Documentation** | Markdown · Express web app · laser engraving | generic / D-P-001 |
| **Team Lead** | DGCA · Swiss Cheese · ROS 2 (architecture thinking) | AIR-001 |

### 🔴 The post-flight workflow — assign this before your first instrumented flight

| Task | From | Why |
|---|---|---|
| **"Flight Data Logging & Analysis"** | AIR-001 Level 3 | Extract logs → plot altitude/velocity/throttle vs time → convert to KML → view the 3D path in Google Earth. **This is our Post Flight Analysis deliverable and our recovery technique.** Swap Pixhawk logs for our barometer and IMU data and it drops straight in. |

---

## 4. Suggested club-wide intake plan

Because the Student Track is cohort-based and limited, stagger it.

### This month — no enrolment needed

| Who | Do |
|---|---|
| **Everyone** | Generic tasks §1 (items 1–7) via the **Open Learner Programme** |
| **Everyone** | 🔴 **"Rules in the Rule Book Written by Blood"** |
| **Avionics** | IOT-001 Level 2 **tasks 2, 3a, 4, 7** — sensor→threshold→actuator, I²C, dashboards |
| **Simulation** | NumPy/Matplotlib task, then plot a real thrust curve |
| **Team Lead** | 🎯 **Submit the Competition Track and Project Track applications** |

### Next intake — Student Track enrolment

| Subsystem | Enrol in | Notes |
|---|---|---|
| Propulsion | **D-P-001** | Needs it most — CAD and GD&T are prerequisites for motor design |
| Structures & Aero | **D-P-001** | |
| Avionics (×2 people) | **IOT-001** and **AIR-001** | Split deliberately — hardware vs comms |
| Simulation | **AIR-001** | |
| Operations | **VFX-001** | Only 2 months — finishes early, frees them for club work |
| Others | Open Learner Programme | If Student Track seats are unavailable |

### Rolling

| Need | Route |
|---|---|
| Oscilloscope, 3D printer, bench supply | **Equipment Support Programme** |
| Strand burner + test stand | 🎯 **Project Track** |
| Competition funding | 🎯 **Competition Track** |

---

## 5. Time reality check

Be honest with recruits about this before they commit.

| Track | Duration | Realistic weekly load |
|---|---|---|
| **VFX-001** | 2 months | 2–3 h |
| **D-P-001** | 6 months | 3–5 h |
| **IOT-001** | 6 months | 3–5 h |
| **AIR-001** | 8 months | 3–5 h |
| **AI-ML-001** | 11 months | 4–6 h |

**Plus our own rocketry work.** A member doing D-P-001 and club work is committing roughly
**6–8 hours a week**. That is a genuine commitment and it should be stated plainly at recruitment.

> ⚠️ **Expect attrition.** Many recruits will not finish a 6-month track. That is normal. **The
> cherry-picked tasks in §3 exist precisely so that a member who drops out of a track has still
> learned something useful.** Design for partial completion.

---

## 6. What we still teach — Marvel cannot cover this

| Gap | Our material |
|---|---|
| 🔴 **OpenRocket / rocket trajectory simulation** | [`02_Simulation.md`](<02_Simulation.md>) |
| 🔴 **Rocket stability (CG/CP, static margin, Barrowman)** | [`04_Structures_and_Aero.md`](<04_Structures_and_Aero.md>) |
| 🔴 **Solid motor design (grain geometry, Kn, nozzles)** | [`03_Propulsion.md`](<03_Propulsion.md>) |
| 🔴 **Propellant chemistry and casting** | [`03_Propulsion.md`](<03_Propulsion.md>) + [`../40_SAFETY/`](<../40_SAFETY/Safety_Manual_Master.md>) |
| 🔴 **Parachute sizing and recovery** | [`../30_AVIONICS/Recovery_Electronics_and_Control.md`](<../30_AVIONICS/Recovery_Electronics_and_Control.md>) |
| 🔴 **Static test operations and CATO prevention** | [`../40_SAFETY/Static_Test_Procedure.md`](<../40_SAFETY/Static_Test_Procedure.md>) |
| 🔴 **IN-SPACe / PESO compliance** | [`../00_ADMINISTRATION/Institutional_Approvals_and_Compliance.md`](<../00_ADMINISTRATION/Institutional_Approvals_and_Compliance.md>) |

**Marvel gives them tools. We give them the rocket.**

---

## 7. One-page assignment sheet

Print this and fill it in per member.

| Field | |
|---|---|
| **Member name** | ______________________ |
| **Subsystem** | Propulsion / Structures / Avionics / Simulation / Operations |
| **Common foundation complete?** | ☐ Markdown ☐ GitHub ☐ Ubuntu ☐ NumPy/Matplotlib ☐ Soldering ☐ 3D printing ☐ Datasheets |
| **Primary track** | ______________________ |
| **Enrolment intake** | ______________________ |
| **Cherry-picked tasks** | 1. ______________ 2. ______________ 3. ______________ |
| **Swiss Cheese task done?** | ☐ (required for all members) |
| **Our own training assigned** | ______________________ |
| **Mentor / buddy** | ______________________ |

---

> ⚠️ **Verify before relying.** All course names, contents, durations, eligibility and intake dates
> were read from Marvel's public site in **October 2026** and are subject to change. Confirm with
> Marvel directly before committing members to a specific plan.
