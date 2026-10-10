# UVCE ROCKETRY CLUB — PROJECT WORKSPACE

**Institution:** University Visvesvaraya College of Engineering (UVCE), K.R. Circle, Bengaluru 560001
**Founded:** 2026
**Objective:** Build genuine rocketry capability from zero, safely, and compete in the IN-SPACe
Model Rocketry India Student Competition.

---

## ⚠️ READ THIS FIRST

1. **No member works on energetic materials alone. Ever.**
2. **Nothing gets built from a design that has not passed a design review.**
3. **Read [`40_SAFETY/Safety_Manual_Master.md`](<40_SAFETY/Safety_Manual_Master.md>) before touching propellant.**
4. **Every number is a starting point, not a validated fact.** Confidence is marked inline:
   ✅ verified from source · 🟡 estimated · ⏳ **unverified — do not design against** · 🔴 blocking.

> **Safety documents take precedence over every other document in this workspace.**

---

## START HERE

| If you are… | Read, in this order |
|---|---|
| **Brand new to the club** | [Safety Manual](<40_SAFETY/Safety_Manual_Master.md>) → [Recruitment & Onboarding](<00_ADMINISTRATION/Recruitment_and_Onboarding.md>) → [README](<README.md>) |
| **Building the first hardware** | [Motor Test Program](<10_PROPULSION/Motor_Test_Program.md>) (strand burner) → [Electronics BOM](<30_AVIONICS/Electronics_BOM_and_Sourcing.md>) Tier (c) |
| **Designing a motor** | [Motor Design Guide](<10_PROPULSION/Motor_Design_Guide.md>) → [Propellant Formulations](<10_PROPULSION/Propellant_Formulations.md>) → [Ignition System](<10_PROPULSION/Ignition_System_Design.md>) |
| **Designing the rocket** | [Stability & Aerodynamics](<20_AEROSTRUCTURES/Stability_and_Aerodynamics.md>) → [Structures](<20_AEROSTRUCTURES/Structures_Design_Guide.md>) → [Mass Budget](<20_AEROSTRUCTURES/Mass_Budget_and_CG.xlsx>) |
| **Simulating** | [OpenRocket Workflow](<50_SIMULATION/OpenRocket_Workflow.md>) → [Motor Files](<50_SIMULATION/Motor_Files.md>) → [Validation](<50_SIMULATION/Simulation_Plan_and_Validation.md>) |
| **About to test** | [Static Test Procedure](<40_SAFETY/Static_Test_Procedure.md>) → [FORM-04](<40_SAFETY/forms/FORM-04_Static_Test_Checklist.md>) |
| **Running the club** | [Club Charter](<00_ADMINISTRATION/Club_Charter.md>) → [Roles](<00_ADMINISTRATION/Roles_and_Responsibilities.md>) → [Project Management](<00_ADMINISTRATION/Project_Management_and_Documentation.md>) |

---

## WORKSPACE MAP

### `00_ADMINISTRATION/` — Governance, people, money
| File | Contents |
|---|---|
| [Club_Charter.md](<00_ADMINISTRATION/Club_Charter.md>) | Constitution, roles, succession clause, safety-first clause |
| [Roles_and_Responsibilities.md](<00_ADMINISTRATION/Roles_and_Responsibilities.md>) | Every position, duties, handover requirements |
| [Recruitment_and_Onboarding.md](<00_ADMINISTRATION/Recruitment_and_Onboarding.md>) | The club's #1 risk, treated strategically |
| [Institutional_Approvals_and_Compliance.md](<00_ADMINISTRATION/Institutional_Approvals_and_Compliance.md>) | College, landowner, district, IN-SPACe, PESO |
| [Funding_and_Sponsorship.md](<00_ADMINISTRATION/Funding_and_Sponsorship.md>) | Budget tiers, sponsorship proposals, financial controls |
| [Project_Management_and_Documentation.md](<00_ADMINISTRATION/Project_Management_and_Documentation.md>) | Documentation standards, review process, handover |
| [BOM_and_Budget.xlsx](<00_ADMINISTRATION/BOM_and_Budget.xlsx>) | **Live workbook** — BOM with estimate vs actual, budget tiers |

### `10_PROPULSION/` — Motors and propellant
| File | Contents |
|---|---|
| [Propellant_Formulations.md](<10_PROPULSION/Propellant_Formulations.md>) | KNSB 65/35, why not sucrose/dextrose, no perchlorates |
| [Motor_Design_Guide.md](<10_PROPULSION/Motor_Design_Guide.md>) | Full equation chain, grain geometry, nozzle, case, worked example |
| [Motor_Test_Program.md](<10_PROPULSION/Motor_Test_Program.md>) | Strat burner, inert grains, static fire, density QC |
| [Ignition_System_Design.md](<10_PROPULSION/Ignition_System_Design.md>) | **The primer recipe**, straw igniters, sizing safety |
| [Propulsion_Roadmap.md](<10_PROPULSION/Propulsion_Roadmap.md>) | 24→38→54→75→94 mm with gate criteria, costs, timeline |
| [Motor_Design_Calculator.xlsx](<10_PROPULSION/Motor_Design_Calculator.xlsx>) | **Live calculator** — inputs drive geometry & throat |

### `20_AEROSTRUCTURES/` — Airframe, fins, recovery structure
| File | Contents |
|---|---|
| [Structures_Design_Guide.md](<20_AEROSTRUCTURES/Structures_Design_Guide.md>) | Loads, safety factors, buckling, composites |
| [Stability_and_Aerodynamics.md](<20_AEROSTRUCTURES/Stability_and_Aerodynamics.md>) | Barrowman method, static margin, drag, flutter |
| [Materials_Database.md](<20_AEROSTRUCTURES/Materials_Database.md>) | Properties, costs, Indian sourcing |
| [Fabrication_and_Manufacturing.md](<20_AEROSTRUCTURES/Fabrication_and_Manufacturing.md>) | Workshop practice, casting tubes, QC |
| [Mass_Budget_and_CG.xlsx](<20_AEROSTRUCTURES/Mass_Budget_and_CG.xlsx>) | **Live workbook** — mass, CG, static margin, ±5% check |

### `30_AVIONICS/` — Electronics, software, comms
| File | Contents |
|---|---|
| [Flight_Computer_Architecture.md](<30_AVIONICS/Flight_Computer_Architecture.md>) | MCU choice, sensors, power, state machine |
| [Sensors_and_Instrumentation.md](<30_AVIONICS/Sensors_and_Instrumentation.md>) | Every sensor, calibration, load cell theory |
| [Communications_and_Ground_Station.md](<30_AVIONICS/Communications_and_Ground_Station.md>) | Radios, link budget, telemetry format |
| [Recovery_Electronics_and_Control.md](<30_AVIONICS/Recovery_Electronics_and_Control.md>) | **No-pyro deployment**, apogee detection, servos |
| [Electronics_BOM_and_Sourcing.md](<30_AVIONICS/Electronics_BOM_and_Sourcing.md>) | **4 costed tiers**, Indian sourcing, counterfeits |

### `40_SAFETY/` — **READ BEFORE ANY ENERGETIC WORK**
| File | Contents |
|---|---|
| [Safety_Manual_Master.md](<40_SAFETY/Safety_Manual_Master.md>) | **Parent document.** Roles, STOP WORK authority, emergencies |
| [PPE_and_Equipment_Register.md](<40_SAFETY/PPE_and_Equipment_Register.md>) | Every item, qty, cost, priority |
| [Propellant_Handling_SOP.md](<40_SAFETY/Propellant_Handling_SOP.md>) | Grinding, mixing, casting, storage, transport |
| [Static_Test_Procedure.md](<40_SAFETY/Static_Test_Procedure.md>) | 60-item checklist, Phases A–F, misfire |
| [Flight_Operations_Safety.md](<40_SAFETY/Flight_Operations_Safety.md>) | Site, wind, man-limits, range discipline |
| [forms/](<40_SAFETY/forms/README.md>) | **6 printable field forms** — carry these to the field |

### `50_SIMULATION/` — Flight simulation
| File | Contents |
|---|---|
| [OpenRocket_Workflow.md](<50_SIMULATION/OpenRocket_Workflow.md>) | Zero to trustworthy simulation |
| [Motor_Files.md](<50_SIMULATION/Motor_Files.md>) | `.eng` format, static fire → thrust curve |
| [Simulation_Plan_and_Validation.md](<50_SIMULATION/Simulation_Plan_and_Validation.md>) | Error sources, dispersion, validation |

### `60_TEST_DATA/` — Raw data lives here, never edited
[README](<60_TEST_DATA/README.md>) · [Static_Test_Log.xlsx](<60_TEST_DATA/Static_Test_Log.xlsx>) · [Calibration_Record.md](<60_TEST_DATA/Calibration_Record.md>)

### `70_REPORTS/` — Design reviews and test reports
[README](<70_REPORTS/README.md>) · [Design_Review_Template.md](<70_REPORTS/Design_Review_Template.md>) · [Test_Report_Template.md](<70_REPORTS/Test_Report_Template.md>)

### `80_REFERENCE/` — Source material
- [nakka-technical-reference.md](<80_REFERENCE/nakka-technical-reference.md>) — 1100 lines of extracted Nakka data
- `nakka_source_text/` — raw text of 13 source pages

### `90_LEARNING/` — **On-ramp for new members with zero knowledge**
| File | Contents |
|---|---|
| [README.md](<90_LEARNING/README.md>) | **The 4-week induction** and how to match people to subsystems |
| [01_Start_Here.md](<90_LEARNING/01_Start_Here.md>) | Rocketry fundamentals — **everyone does this** |
| [02_Simulation.md](<90_LEARNING/02_Simulation.md>) | OpenRocket, Barrowman, validation |
| [03_Propulsion.md](<90_LEARNING/03_Propulsion.md>) | Propellant, grains, nozzles, static testing |
| [04_Structures_and_Aero.md](<90_LEARNING/04_Structures_and_Aero.md>) | Airframes, fins, materials, fabrication |
| [05_Avionics.md](<90_LEARNING/05_Avionics.md>) | Flight computer, sensors, telemetry, ground station |
| [06_Tools_and_Software.md](<90_LEARNING/06_Tools_and_Software.md>) | CAD, Python, Git, KiCad — all free |
| [07_Communities_and_Inspiration.md](<90_LEARNING/07_Communities_and_Inspiration.md>) | Where to ask, who to learn from |
| [08_Marvel_Makerspace_Mapping.md](<90_LEARNING/08_Marvel_Makerspace_Mapping.md>) | 🔴 **What to reuse from UVCE Marvel's courses, equipment and competition track** |
| [09_Marvel_Course_Assignments.md](<90_LEARNING/09_Marvel_Course_Assignments.md>) | 🔴 **Which Marvel track each subsystem's recruit should take** |

### `95_RECRUITMENT/` — **The recruitment and induction funnel**
| File | Contents |
|---|---|
| [README.md](<95_RECRUITMENT/README.md>) | **The 6-stage funnel** and what each stage filters for |
| [00_Founding_Team.md](<95_RECRUITMENT/00_Founding_Team.md>) | 🔴 **Build the founding team first** — who, what they learn, checkpoints |
| [01_Announcement_and_Outreach.md](<95_RECRUITMENT/01_Announcement_and_Outreach.md>) | The message, the channels, the sign-up form |
| [02_Video_Compilation.md](<95_RECRUITMENT/02_Video_Compilation.md>) | The curated 2-hour watch list |
| [03_Foundation_Reader.md](<95_RECRUITMENT/03_Foundation_Reader.md>) | 🔴 **The 10-page reader** — the core training material |
| [04_Open_Book_Test.md](<95_RECRUITMENT/04_Open_Book_Test.md>) | The test, with a full answer key and marking guide |
| [05_Essay_and_Assessment.md](<95_RECRUITMENT/05_Essay_and_Assessment.md>) | Essay prompts and how to mark them |
| [06_Interview_Framework.md](<95_RECRUITMENT/06_Interview_Framework.md>) | Questions, scoring, red and green flags |
| [07_Doubt_Session_Plan.md](<95_RECRUITMENT/07_Doubt_Session_Plan.md>) | How to run the highest-value stage |
| [08_Timeline_and_Logistics.md](<95_RECRUITMENT/08_Timeline_and_Logistics.md>) | Week-by-week run sheet and checklists |

### Root documents
- **[Technical_Reference_Nakka.md](<Technical_Reference_Nakka.md>)** — consolidated KNSB propellant & safety reference
- **[UVCE_Rocketry_Roadmap.md](<UVCE_Rocketry_Roadmap.md>)** — strategic plan and phased schedule
- **[config/engineering_constants.md](<config/engineering_constants.md>)** — **single source of truth for design numbers**

---

## 🔴 THE ONE BLOCKING ISSUE

**The burn-rate law for our propellant is unknown.**

KNSB is a **mesa propellant** — a single power law `r = a·Pⁿ` is **invalid** across all pressures.
The `a`/`n` pair must be measured **per pressure regime** using **our** potassium nitrate and
**our** sorbitol, at **our** grind setting and dessication state.

**Consequences:**
- Grain geometry and throat diameter **cannot be finalised**
- The interpolated placeholder (`a ≈ 1.99`, `n ≈ 0.30`) is **illustrative only**
- Our as-obtained materials will give a **lower `a`** than published dessicated test data

**→ The strand burner is the club's first hardware build.** See
[Motor_Test_Program.md](<10_PROPULSION/Motor_Test_Program.md>).
Estimated cost: **≈ ₹12,000** including instrumentation.

---

## WHAT WE HAVE LEARNED THAT CHANGES THE PLAN

Four findings from the source research that overturned initial assumptions:

| # | Finding | Consequence |
|---|---|---|
| 1 | **KNSB is a mesa propellant** | Single power law invalid; must measure per regime |
| 2 | **Bare KNSB is 4.15× harder to ignite than KNSU** (19.9 s vs 4.8 s) | The **thin primer coat is mandatory**, not optional. Recipe now documented. |
| 3 | **The flushing phenomenon** — gas erodes the grain faster than it burns | Delivered Isp 108 s for short grains vs 129 s for long. **Optimum sorbitol grain is 13–15 inches.** Our 35 mm grain will underperform. |
| 4 | **Small motors are HARDER to cast, not easier** | "The larger the grain, the easier it is to cast." Small batches cool faster and thicken. The 24 mm motor is the hard one. |

Additionally: casting difficulty, ignition difficulty, and throat tolerance sensitivity **all scale
inversely with motor size**. The club's instinct to start small is right for *safety*, but the small
motor is genuinely the more difficult build.

---

## CURRENT PROJECT STATE

### Phase 0 — Foundation

| Item | Status |
|---|---|
| Faculty advisor engaged | 🟡 interest expressed, not formalised |
| Club registered with college | ❌ not started |
| Committed members | ❌ none yet |
| Test land within 100 km | 🟡 access believed available, no written permission |
| Funding | 🟡 ₹2–3 lakh indicated as possible, nothing committed |
| Prior rocketry experience | ❌ none |

### Technical baseline

| Parameter | Value | Confidence |
|---|---|---|
| First target apogee | 200 m | mission choice |
| Airframe diameter | 40 mm | preliminary |
| Dry mass (current budget) | **306 g vs 250 g target** | ✅ **22.4% OVER — cut 43.5 g** |
| Launch mass | 330 g | ✅ |
| Required burnout velocity | 72 m/s | ✅ computed with drag |
| First motor impulse | ~24 N·s (D/E class) | ✅ from flight mechanics |
| Propellant | KNSB 65/35, ρ_ideal 1.841 g/cm³ | ✅ verified |
| Grain OD / port / length | 24 / 7 / 35 mm | 🔴 **requires re-solve** |
| Throat diameter | 1.87 mm | 🔴 **requires re-solve** |
| Port/throat ratio | 14.0 | ✅ passes (≥ 2) |

---

## THE HONEST ASSESSMENT

**Strengths:** a willing faculty advisor, land available for testing, a realistic funding prospect,
and now a complete technical reference base and operational documentation set.

**The critical risk is people, not hardware.** The club currently consists of one person and one
interested professor. The mitigation is not enthusiasm — it is **sequencing small, visible wins**:

1. **Build the strand burner** — ≈₹12,000, workbench-scale, produces real measured data in weeks
2. **Fly three progressively harder low-power rockets** — a few thousand rupees
3. **Build the flight computer and ground station** — desk work, heavily graded in competition

Any one of these is achievable within weeks and gives the club something to *show*. **Choose
visibility over ambition.**

---

## HOW TO USE THIS WORKSPACE

1. **New member?** Safety manual first. Always.
2. **Designing something?** Read the discipline folder → check
   [engineering_constants.md](<config/engineering_constants.md>) → record work in `70_REPORTS/`.
3. **Testing something?** Read the SOP **before** the test, not during. Fill the matching form.
   Record results in `60_TEST_DATA/` **the same day**.
4. **Changing a design number?** Change it in
   [engineering_constants.md](<config/engineering_constants.md>) and **nowhere else**, then add a
   change-log row.
5. **Anything undocumented did not happen.** If it is not written down, the club loses it at
   graduation.

---

## BI-WEEKLY PROGRESS LOG

| Date | Activity | Outcome | Next step |
|---|---|---|---|
| — | Workspace initialised | Complete technical + operational documentation set | Build the strand burner |

*Add a row after every working session. This log is the club's memory and the single most important
defence against losing knowledge when members graduate.*

---

*Documentation set: ~50 documents, ~250,000 words, 4 live engineering workbooks, 6 printable field
forms. Built from Richard Nakka's Experimental Rocketry Site and the IN-SPACe competition
documentation.*
