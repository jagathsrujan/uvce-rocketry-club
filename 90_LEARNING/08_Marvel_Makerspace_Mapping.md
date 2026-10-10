# 08 — UVCE Marvel Makerspace: Reuse Mapping

**What to take from Marvel's curriculum, what to skip, and what we must build ourselves.**

| | |
|---|---|
| **Source** | [hub.uvcemarvel.in](https://hub.uvcemarvel.in) — UVCE's alumni-funded makerspace, K.R. Circle |
| **Status of this document** | 🟡 Based on Marvel's public site as read in **October 2026**. Courses, tracks, equipment and eligibility **change** — verify with Marvel directly before relying on anything here. |
| **Bottom line** | **Marvel covers roughly 40% of our training needs — and mostly the parts that are hardest to self-teach.** |

---

## 1. Why this matters

Marvel is at **our own college**, alumni-funded, with real equipment and a structured curriculum. That
changes our training plan in three ways:

1. **We do not need to build a CAD course, a soldering induction, or a PCB curriculum.** Marvel has
   them, taught by coordinators, with equipment we cannot afford.
2. **Their Competition Track offers financial assistance and mentorship** — potentially a funding
   route for our competition entry.
3. **Their Equipment Support Programme gives non-Marvel students access to the lab's tools** — 3D
   printers, an oscilloscope, a power supply, microcontrollers.

> **The strategic conclusion:** we should be a **specialist** club that consumes Marvel's generalist
> training, not a club that tries to teach everything itself.

---

## 2. Equipment you can potentially access

From Marvel's published Equipment Catalogue:

| Equipment | What we would use it for | Rocketry subsystem |
|---|---|---|
| **Creality CR-10 Smart Pro** (3D printer) | Nose cones, avionics sleds, fin alignment jigs, enclosures | Structures + Avionics |
| **Creality Ender V3** (3D printer) | Same | Structures + Avionics |
| **Keysight Oscilloscope** (2-ch DSO + signal generator) | Debugging sensor signals, verifying PWM, servo signals, noise analysis | Avionics |
| **RIGOL DP 712** (bench power supply) | Powering avionics on the bench, current-limited testing | Avionics |
| **BOSCH Tool Kit** (mechanical tools) | Airframe and test-stand fabrication | Structures |
| **ESP32 / ESP8266 / ESP32-CAM** | **Flight computer candidates** — the same chip our architecture doc recommends | Avionics |
| **Arduino Uno / Nano / Mega** | Test-stand instrumentation, prototyping | Avionics |
| **Raspberry Pi 4 (8 GB)** | Ground station, data processing | Avionics |
| **Nvidia Jetson Nano** | Overkill for us, but available | — |
| **Digilent Basys 3** (FPGA) | Not relevant to us | — |
| **Computers** | Simulation, CAD, analysis | All |

> ✅ **The ESP32 and Arduino availability is directly useful** — our
> [`Flight_Computer_Architecture.md`](<../30_AVIONICS/Flight_Computer_Architecture.md>) already
> recommends the ESP32, and the test-stand instrumentation needs an Arduino-class board.

**Access route:** Marvel's **Equipment Support Programme** is explicitly for students *not* in
Marvel. Apply via the form on their site. Terms and conditions apply.

---

## 3. The three tracks to apply to

### 🎯 Competition Track — highest value, act first

> *"MARVEL's Competition Track supports UVCE students who want to participate in technical
> competitions across domains… MARVEL provides resources such as **financial assistance, mentorship,
> and guidance** to ensure team success."*

**Why this is the single most valuable thing on this page:** the IN-SPACe competition costs money —
₹10,000 registration, ₹15,000 after the workshop, plus the motor, payload, materials and travel. We
have ₹2–3 lakh indicated but nothing committed.

**Action:** submit the competition details and budget estimate. Do this **before** you need the money,
not after.

### 🎯 Project Track — for the strand burner and test stand

> *"Project Track is for UVCE students with project ideas but limited resources. Marvel provides
> facilities and resources to support these projects… submit an abstract, timeline, team details, and
> budget estimate."*

**Our use case:** the **strand burner and static test stand** — roughly ₹23,000 of instrumentation and
fabrication, which is the club's critical path.

**Caveat:** be careful how you describe energetic work. Submit the **instrumentation, data acquisition,
and structural fabrication** aspects — the load cell, pressure transducer, DAQ, and test stand
structure. **Propellant handling is our responsibility and stays ours.** See §5.

### 🎯 Equipment Support Programme — for tools you cannot buy

> *"Students who are not part of Marvel can get access to the Lab's Equipments and Components."*

Use it for the oscilloscope and 3D printers. These are exactly the tools that are hard to justify
buying and easy to book by the hour.

---

## 4. What to REUSE from Marvel's courses

### 4.1 From AIR-001 (Aviation & Drone Science) — the most relevant course

| Marvel task | Maps to our | Verdict |
|---|---|---|
| **Level 0 — 3D printing** (STL, slicing, bed temp, infill, SOPs) | Nose cones, sleds, jigs | ✅ **Take it.** Teaches the SOP discipline too. |
| **Level 0 — GitHub workflows** | Our workspace version control | ✅ **Take it.** We need this and don't teach it. |
| **Level 0 — Ubuntu command line** | OpenRocket, Python, ground station | ✅ **Take it.** |
| **Level 0 — NumPy + Matplotlib** (matrix puzzle) | 🔴 **Thrust curve plotting and analysis** | ✅ **Take it — this is directly our data analysis skill** |
| **Level 0 — Markdown article writing** | 🔴 **Our entire workspace is Markdown** | ✅ **Take it.** Free documentation training. |
| **Level 0 — Tinkercad** (ultrasonic + servo) | Circuit intuition, servo control | ✅ Take it |
| **Level 0 — DC motor / L298N** | Actuators, deployment mechanisms | ✅ Take it |
| **Level 0 — ESP32 web server** | 🔴 **Telemetry fundamentals** | ✅ **Take it — same chip as our flight computer** |
| **Level 0 — Soldering prerequisites** (supervised) | 🔴 **Essential for avionics** | ✅ **Take it.** Supervised soldering with real equipment. |
| **Level 0 — 555 astable + DSO** | Timing circuits, using a scope | ✅ Take it |
| **Level 2 — Aerodynamics & aircraft structures** (Bernoulli, Newton's 3rd, lift/drag/thrust/weight, **stability**, control surfaces, pitot) | 🔴 **Our stability and aero foundation** | ✅ **Take it — directly relevant** |
| **Level 2 — Airfoil design + CFD** (NACA 4412, Fusion 360 + Autodesk CFD) | Fin aerodynamics, CFD method | ✅ **Take it.** The CFD toolchain transfers. |
| **Level 2 — UAV assembly** (🔴 **thrust-to-weight ratio, LiPo/Li-ion/NiMH chemistry and safety**, component compatibility, E-Calc) | 🔴 **Mass budget and power design** | ✅ **Take it — battery chemistry and T/W calc are directly ours** |
| **Level 2 — Propeller blade design + CFD** | Fin design methodology | 🟡 Partially — the method transfers, the application differs |
| **Level 2 — ESC control** | Actuator drive | 🟡 Partially |
| **Level 2 — RF communication** (2.4/5.8 GHz, 🔴 **LoRa**, ELRS, link budget, binding) | 🔴 **Our telemetry problem exactly** | ✅ **Take it — LoRa is in our comms plan** |
| **Level 2 — Basics of PID** | Control systems (for later TVC) | 🟡 Useful background |
| **Level 2 — DGCA regulations** | 🔴 **Regulatory framework awareness** — directly parallels our IN-SPACe/PESO work | ✅ **Take it** |
| **Level 3 — UAV assembly + flight controller config** (GPS, sensor calibration) | 🔴 **Our flight computer work** | ✅ **Take it — sensor calibration especially** |
| **Level 3 — Autonomous flight + SITL + geofencing** | 🔴 **Software-in-the-loop testing for our flight software** | ✅ **Take it — SITL is exactly the right method** |
| **Level 3 — MATLAB/Simulink Onramp** | Simulation | ✅ Take it (free certificates) |
| **Level 3 — Advanced PID** | Control | 🟡 Later |
| **Level 3 — "Rules in the Rule Book Written by Blood"** (🔴 **air crash investigation, Swiss Cheese Model**) | 🔴 **SAFETY CULTURE** | ✅✅ **TAKE THIS. HIGHEST VALUE ITEM ON THE LIST.** |
| **Level 3 — Flight data logging & analysis** (🔴 extract logs, altitude/velocity/time graphs, **convert to KML, view 3D path in Google Earth**) | 🔴 **Flight data analysis and recovery** | ✅✅ **TAKE THIS — it is exactly our post-flight workflow** |
| **Level 3 — ROS 2 nodes/publishers/subscribers** | Ground station architecture | 🟡 Useful pattern for ground station software |

#### 🔴 Two tasks deserve special emphasis

**"Rules in the Rule Book Written by Blood" — the Swiss Cheese Model.**
This is **accident investigation methodology**: taking a real crash, identifying the technical, human
and environmental contributing factors, and analysing how independent failures aligned to cause a
disaster. **This is precisely how we should think about CATO prevention** — our safety manual already
describes multiple independent barriers, and this task teaches the analytical framework formally.

**Recommendation: make this a required task for every club member**, not just those doing Marvel.

**"Flight Data Logging & Analysis" — the post-flight workflow.**
Extracting logs, plotting altitude/velocity/throttle against time, generating KML, and viewing the
flight path in 3D. **This is literally our Post Flight Analysis deliverable** and our recovery
technique. Adapt it directly: swap Pixhawk logs for our barometer and IMU data.

### 4.2 From D-P-001 (Design & Prototyping) — the fabrication goldmine

| Marvel task | Maps to our | Verdict |
|---|---|---|
| **Fundamentals of CAD** + Autodesk education licence | 🔴 **Everything we design** | ✅ **Take it — this is our CAD course** |
| **Engineering drawing: isometric & orthographic projections** | 🔴 **Our engineering drawings** | ✅ **Take it.** We need this for design reviews. |
| **2D drawings in CAD (Sketcher)** | Drawings | ✅ Take it |
| **3D drafting (Allen key, machine parts)** | Precision modelling | ✅ **Take it** |
| **Solid modelling — NACA airfoil in Fusion 360** | Fin profiles | ✅ Take it |
| **Surface modelling — toroidal propeller** | Advanced fin shapes (later) | 🟡 Optional |
| **Sheet metal design** | Test stand brackets, mounting plates | ✅ Take it |
| **Assembly and animation** (slider, Geneva wheel, ratchet & pawl) | 🔴 **Separation and retention mechanisms** | ✅ **Take it — mechanism design is our hardest mechanical problem** |
| **Spur gear design** | Mechanisms | 🟡 Later |
| **Parametric box with threads, snap joints, slide joints** | 🔴 **Avionics bay, enclosures, retention** | ✅ **Take it — snap joints are exactly retention mechanisms** |
| **GD&T (Geometric Dimensioning & Tolerancing)** | 🔴 **Our throat diameter is a precision feature** | ✅✅ **TAKE THIS. A ±0.1 mm throat error is ±11% chamber pressure.** |
| **Assembly & simulation — gripper design** | Mechanisms | ✅ Take it |
| **CFD (wind tunnel, lift force)** | Fin and nozzle analysis | ✅ Take it |
| **Piston & crankshaft + CAM/G-code** | 🔴 **Machining our nozzle and casing** | ✅ **Take it — G-code generation is directly useful** |
| **Generative design** | Not a priority | 🟡 Skip |
| **Laser engraving** | Marking components, team number on airframe | 🟡 Nice to have |
| **Datasheet report writing** | 🔴 **Reading sensor datasheets** | ✅ **Take it — essential avionics skill** |
| **PCB design in Altium** (student licence + coursework) | 🔴 **Flight computer PCB** | ✅✅ **TAKE THIS — we have no PCB capability otherwise** |
| **STM32 Blue Pill custom board** (schematic, footprints, decoupling caps, STM32CubeMX, 2-layer layout) | 🔴 **Exactly the flight computer PCB skill** | ✅✅ **Take this** |
| **AM transmitter/receiver, envelope detector, RC time constant** | RF fundamentals | ✅ Take it |
| **DSP, convolution, Fourier** | 🔴 **Sensor filtering and noise** | ✅ Take it |
| **Sad Servers Linux troubleshooting** | Debugging discipline | ✅ Take it |
| **Web app (Express)** | 🔴 **Ground station user interface** | ✅ Take it |
| **Karnaugh maps, logic circuits, LUTs, FPGA/Verilog** | Digital logic fundamentals | 🟡 Background only — not directly needed |
| **VLSI / CMOS / STA** | Not relevant to us | ❌ Skip |

---

## 5. What Marvel does NOT cover — our gaps remain ours

Marvel will not teach these, and should not:

| Gap | Why Marvel can't cover it | Where we cover it |
|---|---|---|
| 🔴 **Propellant chemistry and casting** | Energetic materials — outside a makerspace's remit entirely | [`03_Propulsion.md`](<03_Propulsion.md>) + our SOPs |
| 🔴 **Solid motor design** (grain geometry, Kn, nozzle theory, chamber pressure) | Highly specialised | [`03_Propulsion.md`](<03_Propulsion.md>), [`Motor_Design_Guide.md`](<../10_PROPULSION/Motor_Design_Guide.md>) |
| 🔴 **Rocket stability** (CG/CP, static margin, Barrowman) | Drone stability ≠ rocket stability | [`04_Structures_and_Aero.md`](<04_Structures_and_Aero.md>), [`Stability_and_Aerodynamics.md`](<../20_AEROSTRUCTURES/Stability_and_Aerodynamics.md>) |
| 🔴 **OpenRocket / trajectory simulation** | Drone simulation ≠ ballistic simulation | [`02_Simulation.md`](<02_Simulation.md>) |
| 🔴 **Parachute design and descent rate** | Not a drone topic | [`Recovery_Electronics_and_Control.md`](<../30_AVIONICS/Recovery_Electronics_and_Control.md>) |
| 🔴 **Rocket-specific safety** (CATO prevention, firing distances, propellant handling) | Our responsibility, non-delegable | [`../40_SAFETY/`](<../40_SAFETY/Safety_Manual_Master.md>) |
| 🔴 **IN-SPACe / PESO regulatory framework** | DGCA drone rules are a different regime | [`Institutional_Approvals_and_Compliance.md`](<../00_ADMINISTRATION/Institutional_Approvals_and_Compliance.md>) |
| **Motor test operations** | Not a makerspace activity | [`Static_Test_Procedure.md`](<../40_SAFETY/Static_Test_Procedure.md>) |
| **Composite airframe layup** | Not taught | [`Structures_Design_Guide.md`](<../20_AEROSTRUCTURES/Structures_Design_Guide.md>) |

> ⚠️ **Important boundary:** when applying to Marvel's Project or Competition Track, describe our work
> in terms of **structures, instrumentation, data acquisition, simulation, and electronics**. The
> energetic work is ours alone, at our site, under our SOPs. Do not ask a makerspace to host or
> resource propellant work — it is out of their scope and would put the relationship at risk.

---

## 6. Recommended integration into our induction

Marvel's Student Track is **cohort-based and opens twice a year** — so plan around it, don't depend on
it. Here is how to slot it into our
[4-week induction](<README.md>).

| Our phase | Marvel component | Why |
|---|---|---|
| **Week 1–2 (Foundation)** | Apply to Marvel Student Track (D-P-001 or AIR-001) as a club cohort | Gets our members trained in CAD/electronics with their equipment |
| **Week 1–2** | Do Marvel's **Markdown** and **GitHub** tasks | Directly enables our documentation culture |
| **Week 3 (sampling)** | Structure/aero people → **AIR-001 Level 2 aerodynamics**, **D-P-001 engineering drawing** | The transferable fundamentals |
| **Week 3** | Avionics people → **AIR-001 Level 0/2 electronics**, **D-P-001 PCB design** | Soldering, ESP32, RF, PCB |
| **Week 4 onward** | **Equipment Support Programme** for 3D printer and oscilloscope access | Tools we can't buy |
| **Standing** | 🔴 **"Rules in the Rule Book Written by Blood" for ALL members** | Safety culture — the Swiss Cheese Model |
| **Post-flight** | 🔴 **AIR-001 Level 3 "Flight Data Logging & Analysis"** | Our Post Flight Analysis workflow |
| **When competition-bound** | 🎯 **Competition Track application** | Financial assistance and mentorship |
| **For the strand burner** | 🎯 **Project Track application** | Facilities and resources for instrumentation |

### Division of labour

| Marvel teaches | We teach |
|---|---|
| CAD, engineering drawing, GD&T | Rocket stability and Barrowman |
| Soldering, PCB, Altium, STM32 | Solid motor design and grain geometry |
| 3D printing, workshop tools | Propellant handling and safety SOPs |
| Aerodynamics fundamentals, CFD | OpenRocket trajectory simulation |
| RF, LoRa, telemetry protocols | Parachute design and recovery |
| Flight data analysis, SITL | Motor static testing and CATO prevention |
| Swiss Cheese safety analysis | IN-SPACe / PESO regulatory compliance |

---

## 7. Action list

| # | Action | Owner | Priority |
|---|---|---|---|
| 1 | **Apply to the Competition Track** with competition details and budget | Team Lead | 🔴 **Now** |
| 2 | **Apply to the Project Track** for strand burner + test stand instrumentation | Avionics + Propulsion leads | 🔴 **Now** |
| 3 | **Apply to Equipment Support** for oscilloscope and 3D printer access | Operations Lead | 🟠 Soon |
| 4 | Enrol a club cohort in the **Student Track** (D-P-001 and/or AIR-001) | Team Lead + VP | 🟠 At the next intake |
| 5 | Adopt **"Rules in the Rule Book Written by Blood"** as a required club task | Safety Officer | 🔴 **Now** |
| 6 | Adapt **"Flight Data Logging & Analysis"** into our post-flight procedure | Avionics Lead | 🟠 Before first instrumented flight |
| 7 | Enrol in the **Open Learner Programme** for members who can't get Student Track seats | Any member | 🟢 Rolling |
| 8 | Verify all of the above is still current with Marvel directly | Team Lead | 🔴 On contact |

> ⚠️ **Verify before relying.** This mapping was read from Marvel's public site in **October 2026**.
> Course contents, track eligibility, equipment availability and terms **change**. Confirm with Marvel
> before you build a plan around any specific item.

---

## 8. The honest assessment

**What this changes:** we were planning to teach CAD, soldering, PCB design, 3D printing, basic
electronics and data analysis ourselves. **Marvel already does all of it, better, with equipment we
don't have.** That removes a large amount of work from our plate.

**What it does not change:** the propulsion, stability, simulation and regulatory content is ours
alone, and it is the harder half.

**The strategic risk to manage:** if all our members go through Marvel and none of them come back to
rocketry, we have trained people for someone else. **Keep the rocketry-specific work visible and
interesting** — the strand burner, the first flights, the motor data — so that Marvel is a feeder into
our club rather than a replacement for it.

**The upside:** a student who has completed Marvel's D-P-001 arrives knowing CAD, GD&T, mechanisms and
PCB design. They are immediately useful to us. **That is a far better starting point than the
4-week induction alone could produce.**
