# UVCE Rocketry Club — Design Review Document

```
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║  UVCE ROCKETRY CLUB — DESIGN REVIEW                                                       ║
║  Template: Design_Review_Template.md  |  Rev 1.0  |  Issued: ____________                 ║
║                                                                                          ║
║  Use this template for BOTH a Preliminary Design Review (PDR) and a Critical Design       ║
║  Review (CDR). Tick the review type in Section 1 and complete the sections required for    ║
║  that type — see 70_REPORTS/README.md §4 for what each review must contain.                ║
║                                                                                          ║
║  ⚠  NOTHING GETS BUILT WITHOUT A PASSED DESIGN REVIEW.                                     ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝
```

---

## 1. Review identification

| Field | Entry |
|---|---|
| **Review type** | ☐ **Preliminary Design Review (PDR)** ☐ **Critical Design Review (CDR)** ☐ Other: ______________ |
| **Document ID** | ______________________ e.g. `PDR-2027-001` / `CDR-2027-001` |
| **Revision** | ______________ |
| **Date of review** | ______________________ |
| **Time** | __________ hrs to __________ hrs |
| **Place** | ______________________ |
| **Subject system** | ______________________ |
| **Project / programme** | ______________________ |
| **Applies to** | ______________________ (exact system, motor, airframe, or subsystem this review covers) |
| **Supersedes** | ______________________ or "—" for a first issue |
| **Review pack circulated on** | ______________________ (**minimum 3 days before the review**) |
| **Pack revision reviewed** | ______________ |
| **Author(s) of the design** | ______________________ |
| **Document prepared by** | ______________________ |
| **Related documents** | PDR: ______________ · CDR: ______________ · Test reports: ______________ · Data: ______________ |

> **A CDR is not a repeat of the PDR.** The PDR asks *"is this the right approach?"* The CDR asks *"is
> this specific design — with these drawings, these numbers, these materials, and this budget — ready to
> build?"*

---

## 2. Attendees

| # | Name | Role | Reviewer? | Independent of the design? | Present for the full review? |
|---|---|---|---|---|---|
| 1 | | Design lead (presenter) | ☐ | — | ☐ |
| 2 | | Independent reviewer 1 (technical) | ☐ | ☐ Yes ☐ No | ☐ |
| 3 | | Independent reviewer 2 (technical) | ☐ | ☐ Yes ☐ No | ☐ |
| 4 | | Safety Officer | ☐ | ☐ Yes ☐ No | ☐ |
| 5 | | Faculty advisor / mentor | ☐ | ☐ Yes ☐ No | ☐ |
| 6 | | Project lead / club office bearer | ☐ | ☐ Yes ☐ No | ☐ |
| 7 | | | ☐ | ☐ Yes ☐ No | ☐ |
| 8 | | | ☐ | ☐ Yes ☐ No | ☐ |

**Apologies / absent (and who represents them):** ______________________________________________

**Minimum for a valid review:** **two independent reviewers who did not author the design, plus the
Safety Officer.** A designer cannot review their own design as the sole reviewer.

**Was the minimum met?** ☐ **Yes** ☐ **No — the review is not valid; record why and reconvene:**
______________________________________________________________________________

**Declared conflicts of interest:** ______________________________________________

**Minutes taken by:** ______________________ **Minutes filed at:** ______________________

---

## 3. System description

### 3.1 Purpose and function

**What is this system for, in two or three sentences a new member would understand?**

______________________________________________________________________________
______________________________________________________________________________
______________________________________________________________________________

### 3.2 System overview

| Item | Description |
|---|---|
| **System name / designation** | ______________________ |
| **Function** | ______________________ |
| **Overall configuration** | ______________________ |
| **Principal dimensions** | ______________________ |
| **Total mass (dry / loaded)** | ______ kg / ______ kg |
| **Propellant mass** | ______ g |
| **Expected total impulse** | ______ N·s |
| **Expected peak thrust** | ______ N |
| **Expected MEOP** | ______ bar |
| **Expected apogee (if flight)** | ______ m |
| **Principal materials** | ______________________ |
| **Key bought-in components** | ______________________ |

### 3.3 Subsystems and their boundaries

| Subsystem | Function | Interfaces with | Owner |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

### 3.4 Operations concept *(PDR: required · CDR: required, now frozen)*

**How the system is used end to end** — transport, assembly, integration, arming, firing or launch,
recovery, and disposal. **Who does what, where, and in what order.**

| Phase | What happens | Who does it | Where | Duration |
|---|---|---|---|---|
| Transport | | | | |
| Assembly | | | | |
| Integration | | | | |
| Pre-launch / pre-fire checks | | | | |
| Arming | | | | |
| Firing / launch | | | | |
| Recovery / post-fire | | | | |
| Disposal / storage | | | | |

### 3.5 Operating environment and constraints

| Factor | Value / range | Source |
|---|---|---|
| Site | | |
| Ambient temperature | | |
| Humidity | | |
| Wind | | |
| Altitude above sea level | | |
| Regulatory constraints (IN-SPACe thresholds, PESO, landowner) | | |
| Competition constraints | | |

---

## 4. Requirements traceability table

**Every requirement, traced from its source to the evidence that satisfies it.** Reviewers should be
able to walk this table **in both directions** for any requirement picked at random.

**Trace chain:** mission requirement → system requirement → allocated subsystem requirement → design
feature → analysis / calculation → margin → verification test → test report → raw data.

### 4.1 Mission requirements — the source of everything

| Req ID | Mission requirement | Source (competition rule / club objective / regulatory / landowner) | Priority | Traced to |
|---|---|---|---|---|
| MR-01 | | | ☐ Shall ☐ Should | SR-____ |
| MR-02 | | | ☐ Shall ☐ Should | SR-____ |
| MR-03 | | | ☐ Shall ☐ Should | SR-____ |
| MR-04 | | | ☐ Shall ☐ Should | SR-____ |
| MR-05 | | | ☐ Shall ☐ Should | SR-____ |

> **A requirement with no source is a wish; a requirement with no trace is a gap.**

### 4.2 Allocated system and subsystem requirements

**Each requirement needs a number, a value, a tolerance, and a verification method.** "The motor shall
produce 180 ± 18 N·s of total impulse, verified by static fire" is a requirement. "The motor should be
powerful" is not.

| Req ID | Requirement (value ± tolerance) | Allocated to | Parent (MR / SR) | Verification method | Verification status | Evidence / reference |
|---|---|---|---|---|---|---|
| SR-01 | | | MR-____ | ☐ Analysis ☐ Test ☐ Inspection ☐ Demonstration | ☐ Verified ☐ Partially ☐ Not yet | |
| SR-02 | | | MR-____ | ☐ Analysis ☐ Test ☐ Inspection ☐ Demonstration | ☐ Verified ☐ Partially ☐ Not yet | |
| SR-03 | | | MR-____ | ☐ Analysis ☐ Test ☐ Inspection ☐ Demonstration | ☐ Verified ☐ Partially ☐ Not yet | |
| SR-04 | | | MR-____ | ☐ Analysis ☐ Test ☐ Inspection ☐ Demonstration | ☐ Verified ☐ Partially ☐ Not yet | |
| SR-05 | | | MR-____ | ☐ Analysis ☐ Test ☐ Inspection ☐ Demonstration | ☐ Verified ☐ Partially ☐ Not yet | |
| SR-06 | | | MR-____ | ☐ Analysis ☐ Test ☐ Inspection ☐ Demonstration | ☐ Verified ☐ Partially ☐ Not yet | |
| SR-07 | | | MR-____ | ☐ Analysis ☐ Test ☐ Inspection ☐ Demonstration | ☐ Verified ☐ Partially ☐ Not yet | |
| SR-08 | | | MR-____ | ☐ Analysis ☐ Test ☐ Inspection ☐ Demonstration | ☐ Verified ☐ Partially ☐ Not yet | |

### 4.3 Requirements with no trace — the gaps

> **List every requirement that could not be traced, and say why.** A gap that is written down is a
> known risk. A gap that is not written down is the thing that fails.

| Req ID | Why it is untraced | Consequence | Action | Owner |
|---|---|---|---|---|
| | | | | |

### 4.4 Safety requirements

| Req ID | Safety requirement | Source | Verified by | Status |
|---|---|---|---|---|
| SAF-01 | Case bursts at no more than **2.5 × MEOP** | `Safety_Manual_Master.md` §3.4 | Analysis + hydrostatic proof test | |
| SAF-02 | **Minimum safety margin of 1.5** on motor design | `Safety_Manual_Master.md` §3.4 | Analysis | |
| SAF-03 | Port-to-throat area ratio **≥ 2** throughout the burn | `Static_Test_Procedure.md` §3.2 | Analysis + test | |
| SAF-04 | Minimum safe distance met — **75–100 m proven; 150 m or more for a new design** | `Static_Test_Procedure.md` §2.2 | Site check | |
| SAF-05 | Igniter sized so it cannot plug the throat | `Static_Test_Procedure.md` §3.5 | Inspection + test | |
| SAF-06 | Load cell sized so peak expected thrust is **50–80% of full scale** | `Static_Test_Procedure.md` §3.3 | Analysis | |
| SAF-07 | Pressure transducer rated to at least **2× expected MEOP**, thermally protected | `Static_Test_Procedure.md` §3.4 | Inspection | |
| SAF-08 | Relevant NO-GO criteria addressed by the design and the procedures | `Static_Test_Procedure.md` §7.5 | Review | |

---

## 5. Design description

### 5.1 Configuration and drawings

| Drawing / model reference | Revision | Description |
|---|---|---|
| | | |
| | | |
| | | |

**Are the drawings at the revision reviewed here?** ☐ Yes ☐ No — **a review against a superseded
drawing is void**

### 5.2 Design description narrative

**Describe the design as built on paper: geometry, materials, joining methods, tolerances, and the
reason for each major choice.** Write it so a reviewer who has never seen the project can follow it.

______________________________________________________________________________
______________________________________________________________________________
______________________________________________________________________________
______________________________________________________________________________
______________________________________________________________________________

### 5.3 Materials and their justification

| Component | Material | Specification / grade | Why this material | Alternative rejected, and why |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |

**Any material with a prohibited or restricted status?** ☐ No ☐ Yes: ______________________
*(perchlorates and chlorates are prohibited — `Safety_Manual_Master.md` §3.4)*

### 5.4 Component selection

| Component | Selected item | Specification | Why selected | Lead time | If unavailable |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

### 5.5 Mass budget

| Item | Mass (g) | Uncertainty (g) | Source |
|---|---|---|---|
| Motor hardware | | | |
| Propellant | | | |
| Airframe and fins | | | |
| Recovery system | | | |
| Avionics | | | |
| Payload | | | |
| **Total** | | | |

**Mass margin:** ______ % (**state the required minimum and whether it is met**)

### 5.6 Trade studies — the alternatives that were rejected

**A design review that shows only one option has not shown that the option is right.**

| Option | Configuration | Pros | Cons | Verdict | Why rejected / selected |
|---|---|---|---|---|---|
| A | | | | ☐ Selected ☐ Rejected | |
| B | | | | ☐ Selected ☐ Rejected | |
| C | | | | ☐ Selected ☐ Rejected | |

---

## 6. Analysis and calculations *(PDR: required · CDR: required, updated)*

> **An FEA result without its assumptions is a picture, not an analysis.** Every calculation must state
> its inputs, its assumptions, its method, its result, and its uncertainty.

### 6.1 Analysis index

| # | Analysis | Method | Performed by | Reference / file | Reviewed by |
|---|---|---|---|---|---|
| 1 | Chamber pressure and thrust prediction | Analytical | | | |
| 2 | Burn rate / strand burner correlation | Empirical | | | |
| 3 | Total impulse and delivered Isp | Analytical | | | |
| 4 | Nozzle expansion and throat sizing | Analytical | | | |
| 5 | Case hoop stress and burst margin | Analytical | | | |
| 6 | Case and closure stress | **FEA** | | | |
| 7 | Nozzle thermal analysis | Analytical / FEA | | | |
| 8 | Fin flutter and stability | Analytical | | | |
| 9 | Recovery system descent rate and drift | Analytical | | | |
| 10 | Structural loads on the thrust stand | Analytical / FEA | | | |
| 11 | | | | | |

### 6.2 Theoretical calculations — summary

| Quantity | Symbol | Predicted value | Method / formula | Inputs and assumptions | Uncertainty |
|---|---|---|---|---|---|
| Chamber pressure | Pc | ______ bar | | | ± ______ |
| Thrust | F | ______ N | | | ± ______ |
| Burn time | t_b | ______ s | | | ± ______ |
| Total impulse | I | ______ N·s | | | ± ______ |
| Delivered Isp | Isp | ______ s | | | ± ______ |
| Propellant mass | m_p | ______ g | | | ± ______ |
| Burn rate at MEOP | r | ______ mm/s | | | ± ______ |
| Port-to-throat ratio | J | ______ | | | |
| Nozzle expansion ratio | ε | ______ | | | |
| Apogee (if flight) | h | ______ m | | | ± ______ |

**Total impulse basis:** total impulse is the **area under the thrust-time curve** — state how the
prediction was integrated and over what time base.

### 6.3 FEA — required inputs for every model

| Field | Entry |
|---|---|
| **Analysis name** | ______________________ |
| **Software and version** | ______________________ |
| **Model type** | ☐ 2D axisymmetric ☐ 3D solid ☐ Shell ☐ Other: ______________ |
| **Element type and order** | ______________________ |
| **Mesh:** element count | ______ |
| **Mesh:** characteristic size | ______ mm |
| **Mesh convergence study performed?** | ☐ Yes — result changed by ______ % ☐ **No — this is a finding** |
| **Material model** | ☐ Linear elastic ☐ Elastic-plastic ☐ Other: ______________ |
| **Material properties used (E, ν, σ_y, σ_ult, ρ)** | ______________________ |
| **Source of material properties** | ☐ Datasheet ☐ Supplier certificate ☐ Measured ☐ Handbook |
| **Boundary conditions** | ______________________ |
| **Loads applied (magnitude and direction)** | ______________________ |
| **Load cases run** | ______________________ |
| **Factor applied to loads** | ______ |
| **Results: maximum stress** | ______ MPa |
| **Results: location of maximum stress** | ______________________ |
| **Results: maximum deflection** | ______ mm |
| **Safety factor from the model** | ______ |
| **Assumptions and simplifications** | ______________________ |
| **Limitations of the model** | ______________________ |
| **Verified against a hand calculation or a textbook case?** | ☐ Yes — reference: ______________ ☐ **No — this is a finding** |

### 6.4 Assumptions register

**Every engineering assumption, stated so it can be challenged.**

| # | Assumption | Basis | If it is wrong, what happens? | Owner |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

---

## 7. Margins *(PDR: required · CDR: required, updated)*

> **Margins on joints and fasteners are the specific thing reviewers must not let slide.** A design that
> "looks strong enough" has no margin — it has an opinion.

### 7.1 Motor case margins

| Quantity | Value |
|---|---|
| **MEOP (maximum expected operating pressure)** | ______ bar |
| **Case burst pressure (analysis)** | ______ bar |
| **Burst / MEOP ratio** | ______ |
| **Requirement: burst at no more than 2.5 × MEOP** | ☐ Met ☐ Not met |
| **Requirement: minimum safety margin of 1.5** | ☐ Met ☐ Not met |
| **Material yield strength used** | ______ MPa at ______ °C |
| **Material ultimate strength used** | ______ MPa at ______ °C |
| **Wall thickness** | ______ mm |
| **Corrosion / wear allowance** | ______ mm |
| **Hoop stress at MEOP** | ______ MPa |
| **Safety factor against yield** | ______ |
| **Safety factor against ultimate** | ______ |
| **Hydrostatic proof test performed to 1.2 × MEOP?** | ☐ Yes — pressure ______ bar, hold ______ s ☐ Not yet (new design: required) |
| **Proof test result** | ☐ No deformation or leak ☐ Rejected |

**Avoid "boilerplate" thick-walled cases** — they store an incredible amount of energy before bursting,
which **increases** the severity of a failure.

### 7.2 Joints and fasteners — margin of safety on every one

> **Margin of safety (MS) = (Allowable / Applied) − 1.** **MS ≥ 0** is the minimum; the club requires the
> stated design margin to be met on every joint, and **the minimum acceptable safety margin on the motor
> design is 1.5.**

| # | Joint / fastener | Location | Load case | Applied load (N) | Allowable (N) | MS = (A/P) − 1 | Required MS | Met? | Basis of allowable |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | ______ | ______ | ______ | ______ | ☐ ☐ No | |
| 2 | | | | ______ | ______ | ______ | ______ | ☐ Yes ☐ No | |
| 3 | | | | ______ | ______ | ______ | ______ | ☐ Yes ☐ No | |
| 4 | | | | ______ | ______ | ______ | ______ | ☐ Yes ☐ No | |
| 5 | | | | ______ | ______ | ______ | ______ | ☐ Yes ☐ No | |
| 6 | | | | ______ | ______ | ______ | ______ | ☐ Yes ☐ No | |
| 7 | | | | ______ | ______ | ______ | ______ | ☐ Yes ☐ No | |
| 8 | | | | ______ | ______ | ______ | ______ | ☐ Yes ☐ No | |
| 9 | | | | ______ | ______ | ______ | ______ | ☐ Yes ☐ No | |
| 10 | | | | ______ | ______ | ______ | ______ | ☐ Yes ☐ No | |

**Fastener details:**

| Field | Entry |
|---|---|
| **Fastener standard and grade** | ______________________ |
| **Thread engagement** | ______ × nominal diameter (**state the minimum required**) |
| **Preload / torque specification** | ______ N·m |
| **Torque method** | ☐ Torque wrench ☐ Torque-angle ☐ Other: ______________ |
| **Shear-pin sizing (where specified)** | ______________________ |
| **Thread stripping checked?** | ☐ Yes ☐ No |
| **Bearing stress checked?** | ☐ Yes ☐ No |
| **Pull-out / tear-out checked?** | ☐ Yes ☐ No |
| **Fatigue considered?** | ☐ Yes ☐ No ☐ N/A |
| **Thermal effects on preload considered?** | ☐ Yes ☐ No |
| **Retaining ring / snap ring margin** | ______________________ |
| **Any joint with MS < 0** | ☐ None ☐ **Present — the design does not pass** |

### 7.3 Other margins

| Margin | Value | Requirement | Met? |
|---|---|---|---|
| **Thrust stand anchoring / ballast** | ______ × expected peak thrust | **≥ 5×** | ☐ Yes ☐ No |
| **Load cell range margin** | Peak expected thrust = ______ % of full scale | **50–80%** | ☐ Yes ☐ No |
| **Pressure transducer rating margin** | Rating = ______ × expected MEOP | **≥ 2×** | ☐ Yes ☐ No |
| **Port-to-throat area ratio** | ______ | **≥ 2 throughout the burn** | ☐ Yes ☐ No |
| **Recovery descent rate margin** | ______ m/s | ≤ ______ m/s | ☐ Yes ☐ No |
| **Stability margin (calibres)** | ______ | ≥ ______ | ☐ Yes ☐ No |
| **Mass margin** | ______ % | ≥ ______ % | ☐ Yes ☐ No |
| **Schedule margin** | ______ days | ≥ ______ days | ☐ Yes ☐ No |
| **Budget margin** | ______ % | ≥ ______ % | ☐ Yes ☐ No |

---

## 8. Interfaces

**Interfaces are where integration fails.** Every interface needs a definition on both sides, a
tolerance, and an owner.

### 8.1 Interface register

| # | Interface | Between (A ↔ B) | Type | Definition (dimensions, loads, signals, fluids) | Tolerance | Owner | Verified? |
|---|---|---|---|---|---|---|---|
| 1 | | ↔ | ☐ Mechanical ☐ Electrical ☐ Thermal ☐ Fluid ☐ Data ☐ Human | | | | ☐ |
| 2 | | ↔ | ☐ Mechanical ☐ Electrical ☐ Thermal ☐ Fluid ☐ Data ☐ Human | | | | ☐ |
| 3 | | ↔ | ☐ Mechanical ☐ Electrical ☐ Thermal ☐ Fluid ☐ Data ☐ Human | | | | ☐ |
| 4 | | ↔ | ☐ Mechanical ☐ Electrical ☐ Thermal ☐ Fluid ☐ Data ☐ Human | | | | ☐ |
| 5 | | ↔ | ☐ Mechanical ☐ Electrical ☐ Thermal ☐ Fluid ☐ Data ☐ Human | | | | ☐ |

### 8.2 Critical interfaces — the ones that would hurt

| Interface | Failure mode | Consequence | Detection method | Mitigation |
|---|---|---|---|---|
| Case ↔ grain (inhibitor bond) | Disbonding | Increased burning area, over-pressurisation | **Coin tap test after full cure** | Reject any segment sounding different from its batch-mates |
| Grain ↔ nozzle (throat blockage) | Igniter or debris plugs the throat | Case burst | Igniter sized so it cannot plug the throat | Igniter sizing review |
| Nozzle ↔ case (retaining system) | Nozzle ejection | Loss of pressure, lateral hazard | Visual + torque verification | Specified retaining system, verified torque |
| Motor ↔ thrust stand | Stand movement | **Thrust data invalidated** | Post-test stand inspection | 5× ballast, rigid mounting, side-on camera |
| Load cell ↔ motor axis | Misalignment | Thrust measurement error | Dimensional check before the test | Documented mounting, lever ratio recorded |
| Recovery ↔ airframe | Premature or no deployment | Ballistic impact | Ground test / flight test | Redundant deployment, verified packing |
| Igniter ↔ firing circuit | Uncommanded ignition | Injury | Shunts, key, safe/arm in series, continuity < 50 mA | Eight-layer defence (`Static_Test_Procedure.md` §4.3) |

---

## 9. Risks and mitigations

**Risk = likelihood × consequence.** Be honest about both. **A risk register that lists only small risks
is a risk register that has not been written honestly.**

| # | Risk | Category | Likelihood (L/M/H) | Consequence (L/M/H) | Severity | Mitigation | Residual risk | Owner |
|---|---|---|---|---|---|---|---|---|
| 1 | | ☐ Technical ☐ Safety ☐ Schedule ☐ Budget ☐ Supply ☐ Regulatory ☐ Environmental | | | | | | |
| 2 | | ☐ Technical ☐ Safety ☐ Schedule ☐ Budget ☐ Supply ☐ Regulatory ☐ Environmental | | | | | | |
| 3 | | ☐ Technical ☐ Safety ☐ Schedule ☐ Budget ☐ Supply ☐ Regulatory ☐ Environmental | | | | | | |
| 4 | | ☐ Technical ☐ Safety ☐ Schedule ☐ Budget ☐ Supply ☐ Regulatory ☐ Environmental | | | | | | |
| 5 | | ☐ Technical ☐ Safety ☐ Schedule ☐ Budget ☐ Supply ☐ Regulatory ☐ Environmental | | | | | | |
| 6 | | ☐ Technical ☐ Safety ☐ Schedule ☐ Budget ☐ Supply ☐ Regulatory ☐ Environmental | | | | | | |
| 7 | | ☐ Technical ☐ Safety ☐ Schedule ☐ Budget ☐ Supply ☐ Regulatory ☐ Environmental | | | | | | |
| 8 | | ☐ Technical ☐ Safety ☐ Schedule ☐ Budget ☐ Supply ☐ Regulatory ☐ Environmental | | | | | | |

### 9.1 The risk that keeps people up at night

**State the single worst credible outcome for this design, and what the design does about it:**

______________________________________________________________________________
______________________________________________________________________________

### 9.2 Safety hazards identified

| # | Hazard | Cause | Consequence | Existing control | Adequate? |
|---|---|---|---|---|---|
| 1 | | | | | ☐ Yes ☐ No |
| 2 | | | | | ☐ Yes ☐ No |
| 3 | | | | | ☐ Yes ☐ No |
| 4 | | | | | ☐ Yes ☐ No |

*Cross-reference the safety review carried out under `40_SAFETY/Safety_Manual_Master.md`.*

### 9.3 Schedule pressure — declared honestly

> **Schedule pressure is a hazard, and it is a hazard we can see coming** (`Safety_Manual_Master.md`
> §5.2). **"Never let schedule pressure, competition deadlines, or a senior member's impatience justify
> skipping any step."**

| Field | Entry |
|---|---|
| **Is this project under schedule pressure?** | ☐ No ☐ Yes |
| **Hard deadline (if any)** | ______________________ |
| **Days available vs days required** | ______ vs ______ |
| **What will be cut if the deadline cannot be met?** | ☐ Scope ☐ Test campaign ☐ Nothing — **"safety steps" and "checks" are not options** |
| **Is any safety step proposed to be compressed?** | ☐ **No** ☐ Yes — **this is a NO-GO and a finding** |

---

## 10. Open items with owners

**Every open item is a numbered action with a named owner and a due date. There are no verbal-only
findings.**

| # | Open item / finding | Raised by | Category | Blocking? | Owner | Due date | Status |
|---|---|---|---|---|---|---|---|
| 1 | | | ☐ Design ☐ Analysis ☐ Safety ☐ Documentation ☐ Test ☐ Budget ☐ Interface | ☐ Blocking ☐ Advisory | | | ☐ Open ☐ Closed |
| 2 | | | ☐ Design ☐ Analysis ☐ Safety ☐ Documentation ☐ Test ☐ Budget ☐ Interface | ☐ Blocking ☐ Advisory | | | ☐ Open ☐ Closed |
| 3 | | | ☐ Design ☐ Analysis ☐ Safety ☐ Documentation ☐ Test ☐ Budget ☐ Interface | ☐ Blocking ☐ Advisory | | | ☐ Open ☐ Closed |
| 4 | | | ☐ Design ☐ Analysis ☐ Safety ☐ Documentation ☐ Test ☐ Budget ☐ Interface | ☐ Blocking ☐ Advisory | | | ☐ Open ☐ Closed |
| 5 | | | ☐ Design ☐ Analysis ☐ Safety ☐ Documentation ☐ Test ☐ Budget ☐ Interface | ☐ Blocking ☐ Advisory | | | ☐ Open ☐ Closed |
| 6 | | | ☐ Design ☐ Analysis ☐ Safety ☐ Documentation ☐ Test ☐ Budget ☐ Interface | ☐ Blocking ☐ Advisory | | | ☐ Open ☐ Closed |
| 7 | | | ☐ Design ☐ Analysis ☐ Safety ☐ Documentation ☐ Test ☐ Budget ☐ Interface | ☐ Blocking ☐ Advisory | | | ☐ Open ☐ Closed |
| 8 | | | ☐ Design ☐ Analysis ☐ Safety ☐ Documentation ☐ Test ☐ Budget ☐ Interface | ☐ Blocking ☐ Advisory | | | ☐ Open ☐ Closed |
| 9 | | | ☐ Design ☐ Analysis ☐ Safety ☐ Documentation ☐ Test ☐ Budget ☐ Interface | ☐ Blocking ☐ Advisory | | | ☐ Open ☐ Closed |
| 10 | | | ☐ Design ☐ Analysis ☐ Safety ☐ Documentation ☐ Test ☐ Budget ☐ Interface | ☐ Blocking ☐ Advisory | | | ☐ Open ☐ Closed |

**Action closure verification:** the gate opens only when all **blocking** actions are closed and
verified. **Verification of closure is by the original raiser of the finding, not by the owner.**

| Action # | Declared closed on | Evidence provided | Verified closed by | Date verified |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

---

## 11. Bill of materials reference

| Field | Entry |
|---|---|
| **Bill of materials document reference** | ______________________ |
| **BOM revision** | ______________ |
| **BOM complete (every part, quantity, supplier, part number, unit cost)?** | ☐ Yes ☐ No |
| **Consumables included?** | ☐ Yes ☐ No |
| **Test campaign costs included?** | ☐ Yes ☐ No |
| **Estimated total cost** | ₹______________________ |
| **Actual / quoted total cost** *(CDR)* | ₹______________________ |
| **Variance** *(CDR)* | ₹______________________ = ______ % |
| **Explanation of variance** *(CDR)* | ______________________ |
| **Budget approved by** | ______________________ |
| **Sponsorship details** *(CDR)* | ______________________ |
| **Funding confirmed vs pending** | ₹______________ confirmed / ₹______________ pending |
| **If a sponsor does not deliver, what happens?** | ______________________ |
| **Procurement lead time (longest item)** | ______ days |
| **Long-lead items on the critical path** | ______________________ |

---

## 12. Test plan reference

| Field | Entry |
|---|---|
| **Test plan document reference** | ______________________ |
| **Test plan revision** | ______________ |
| **Test criteria written BEFORE the test?** | ☐ Yes ☐ No — **a pass/fail rule written after the test is not a criterion** |

### 12.1 Verification matrix — requirement to test

| Req ID | Requirement | Verification method | Test ID / analysis ref | Acceptance threshold | Pass/fail rule | Status |
|---|---|---|---|---|---|---|
| | | ☐ Analysis ☐ Test ☐ Inspection ☐ Demonstration | | | | ☐ Not run ☐ Pass ☐ Fail |
| | | ☐ Analysis ☐ Test ☐ Inspection ☐ Demonstration | | | | ☐ Not run ☐ Pass ☐ Fail |
| | | ☐ Analysis ☐ Test ☐ Inspection ☐ Demonstration | | | | ☐ Not run ☐ Pass ☐ Fail |
| | | ☐ Analysis ☐ Test ☐ Inspection ☐ Demonstration | | | | ☐ Not run ☐ Pass ☐ Fail |
| | | ☐ Analysis ☐ Test ☐ Inspection ☐ Demonstration | | | | ☐ Not run ☐ Pass ☐ Fail |
| | | ☐ Analysis ☐ Test ☐ Inspection ☐ Demonstration | | | | ☐ Not run ☐ Pass ☐ Fail |
| | | ☐ Analysis ☐ Test ☐ Inspection ☐ Demonstration | | | | ☐ Not run ☐ Pass ☐ Fail |
| | | ☐ Analysis ☐ Test ☐ Inspection ☐ Demonstration | | | | ☐ Not run ☐ Pass ☐ Fail |

### 12.2 Test readiness — what must exist before a test is run

- [ ] Instrumentation specified, with the required sample rates (**≥ 100 Hz; 1000 Hz preferred**)
- [ ] Instrument calibration current, and the calibration record IDs identified
- [ ] Before-and-after calibration procedure defined
- [ ] Data capture and backup method defined (**two copies, two devices, before anyone leaves the site**)
- [ ] Side-on camera position defined (**240 fps minimum; 1000 fps preferred**)
- [ ] Sync marker method defined
- [ ] Environment limits defined (wind, rain, lightning, daylight)
- [ ] **NO-GO criteria defined before the test**
- [ ] Safety procedure identified and the field forms named (`FORM-01`, `FORM-04` or `FORM-05`)
- [ ] Safety Officer and Test Director named
- [ ] Site, distance, and cover identified
- [ ] Debrief and reporting route defined (**test report within 24 hours for a static fire**)

### 12.3 Success criteria — what "this worked" means

**State it numerically, before the test.**

| Criterion | Threshold | Measurement method |
|---|---|---|
| | | |
| | | |
| | | |

---

## 13. Reviewer verification checklist

**Every reviewer completes this section individually.** Tick only what you **personally verified** — not
what was presented to you. **A reviewer who ticks without checking has made the review worthless.**

### 13.1 Requirements and traceability

- [ ] **Every mission requirement has a source.** I checked, and none is an unsourced wish
- [ ] **Every system requirement is numeric** — a value, a tolerance, and a unit
- [ ] **Every requirement traces in both directions** — down to a design feature, and back up to a mission requirement
- [ ] **Every requirement has a verification method** — analysis, test, inspection, or demonstration
- [ ] **Every requirement has a status** — verified, partially verified, or not yet. **No blanks**
- [ ] **Untraced requirements are listed as gaps**, with the consequence stated
- [ ] **The safety requirements are included** and verified
- [ ] I picked **three requirements at random** and walked the chain myself. Reference: ______________

### 13.2 Design description

- [ ] The design is described well enough for someone who has never seen the project to follow it
- [ ] **The drawings referenced are at the revision reviewed here**
- [ ] Every material has a specification and a stated reason for selection
- [ ] **No prohibited material** (perchlorates, chlorates) is present
- [ ] Component selections state the lead time and the fallback
- [ ] The mass budget is complete and carries a stated margin
- [ ] **Rejected alternatives are documented** — this is not a single-option review
- [ ] The operations concept covers transport, assembly, arming, firing/launch, recovery, and disposal

### 13.3 Analysis and calculations

- [ ] **Every calculation states its inputs, assumptions, method, result, and uncertainty**
- [ ] I can reproduce at least one calculation from the inputs given. Which one: ______________
- [ ] **Every FEA model states its:**
  - [ ] software and version
  - [ ] element type and mesh size
  - [ ] **mesh convergence study** (or the absence of one is flagged as a finding)
  - [ ] material model and the **source of the material properties**
  - [ ] boundary conditions and applied loads
  - [ ] **assumptions and limitations**
  - [ ] **verification against a hand calculation or a textbook case**
- [ ] **No result is presented without its assumptions**
- [ ] The assumptions register is complete, and I have challenged at least two assumptions
- [ ] Where analysis and test disagree, the discrepancy is explained

### 13.4 Margins — the part that must not slide

- [ ] **Every joint and fastener has an explicit margin of safety**, calculated as (Allowable / Applied) − 1
- [ ] **No joint has MS < 0**
- [ ] **The required minimum margin is stated and met on every joint**
- [ ] The motor design carries a **minimum safety margin of 1.5**
- [ ] The case **bursts at no more than 2.5 × MEOP**
- [ ] The **hydrostatic proof test at 1.2 × MEOP** is planned or performed for a new design
- [ ] **No "boilerplate" thick-walled case** — I checked that mass was not added as a substitute for analysis
- [ ] Thread engagement, bearing stress, tear-out, and shear-pin sizing are all checked
- [ ] Thrust stand anchoring is **≥ 5× expected peak thrust**
- [ ] Load cell range is **50–80% of full scale** at peak expected thrust
- [ ] Pressure transducer is rated to **≥ 2× expected MEOP**
- [ ] **Port-to-throat area ratio is ≥ 2 throughout the burn**
- [ ] Mass, schedule, and budget margins are stated and met

### 13.5 Interfaces

- [ ] **Every interface is defined on both sides** — a definition that exists on one side only is a gap
- [ ] Every interface has a tolerance and an owner
- [ ] **Critical interfaces have failure modes and detection methods**
- [ ] The case ↔ grain inhibitor bond is verified by a coin tap test **after full cure**
- [ ] Motor ↔ stand interface accounts for stand movement invalidating thrust data
- [ ] Load cell alignment with the thrust axis is defined and verifiable
- [ ] Recovery ↔ airframe interface is verified

### 13.6 Risks

- [ ] The risk register is **honest** — it includes at least one risk that could actually stop the project
- [ ] Every risk has a mitigation and an owner
- [ ] Residual risk is stated after mitigation
- [ ] **The worst credible outcome is stated** and the design addresses it
- [ ] **Schedule pressure is declared honestly** if it exists
- [ ] **No safety step is proposed to be compressed to meet a deadline**

### 13.7 Cost, schedule, and readiness

- [ ] The **bill of materials is complete** — every part, quantity, supplier, and cost
- [ ] Consumables and test campaign costs are included
- [ ] *(CDR)* The **estimate versus actual** comparison is present, and every variance is explained
- [ ] *(CDR)* **Sponsorship details** are complete, with confirmed vs pending funding identified
- [ ] The development schedule has milestones, dependencies, and a critical path
- [ ] Long-lead items are identified and ordered in time
- [ ] The schedule does not require compressing any safety step

### 13.8 Test plan

- [ ] **Test criteria were written before the test**, with numeric acceptance thresholds
- [ ] The verification matrix covers **every** requirement
- [ ] Instrumentation, sample rates, and calibration validity are specified
- [ ] The data capture and backup method is defined
- [ ] **NO-GO criteria are defined in advance**
- [ ] The safety procedure and the field forms are named
- [ ] The safety roles are named
- [ ] Site, distance, and cover are identified
- [ ] *(CDR)* **Test results are presented** where they exist, each referenced to its test report and raw data

### 13.9 Documentation and control

- [ ] The document is **dated and versioned**, and states what it supersedes
- [ ] The document states **exactly what it applies to**
- [ ] **Every open item is numbered, with an owner and a due date** — no verbal-only findings
- [ ] **Blocking vs advisory** actions are distinguished
- [ ] All referenced documents exist and are at the revision cited
- [ ] **I have not identified anything I was asked to overlook**

### 13.10 Reviewer's independence statement

**I confirm that I did not author this design, and that I have reviewed it against the evidence
presented rather than against the presentation itself.**

**Reviewer 1:** ______________________ **Signature:** ______________________ **Date:** __________

**Reviewer 2:** ______________________ **Signature:** ______________________ **Date:** __________

**Safety Officer:** ______________________ **Signature:** ______________________ **Date:** __________

---

## 14. Review outcome and action items

### 14.1 Outcome

| Outcome | Tick ONE | Meaning |
|---|---|---|
| ✅ **PASS** | ☐ | The design is approved. **The gate opens** |
| ⚠️ **PASS WITH ACTIONS** | ☐ | Approved **conditionally**. The gate opens **only when all BLOCKING actions are closed and verified**. Advisory actions may remain open with a due date |
| ❌ **FAIL** | ☐ | **The gate is closed.** The design returns to the design lead. A re-review is required |

**Outcome declared by:** ______________________ **Time:** __________

### 14.2 If PASS WITH ACTIONS — what unblocks the gate

| Blocking action # | Description | Owner | Due date | Closed on | Verified by |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

**Gate opens on:** ______________________ (when all blocking actions above are verified closed)

### 14.3 If FAIL — what must happen before a re-review

**Findings that caused the failure:**

______________________________________________________________________________
______________________________________________________________________________

**Re-review scheduled for:** ______________________ **Review panel for re-review:** ______________________

**Re-review document ID:** ______________________

### 14.4 Action items — complete list

| # | Action | Raised by | Owner | Due date | Blocking? | Status |
|---|---|---|---|---|---|---|
| 1 | | | | | ☐ ☐ | ☐ Open ☐ Closed |
| 2 | | | | | ☐ ☐ | ☐ Open ☐ Closed |
| 3 | | | | | ☐ ☐ | ☐ Open ☐ Closed |
| 4 | | | | | ☐ ☐ | ☐ Open ☐ Closed |
| 5 | | | | | ☐ ☐ | ☐ Open ☐ Closed |
| 6 | | | | | ☐ ☐ | ☐ Open ☐ Closed |
| 7 | | | | | ☐ ☐ | ☐ Open ☐ Closed |
| 8 | | | | | ☐ ☐ | ☐ Open ☐ Closed |
| 9 | | | | | ☐ ☐ | ☐ Open ☐ Closed |
| 10 | | | | | ☐ ☐ | ☐ Open ☐ Closed |
| 11 | | | | | ☐ ☐ | ☐ Open ☐ Closed |
| 12 | | | | | ☐ ☐ | ☐ Open ☐ Closed |

**Action tracking reviewed at:** ______________________ (the actions are tracked to closure and
verified, not merely recorded)

---

## 15. Approval signatures

**A review is only valid when it is signed.** Signatures signify that the signatory attended the review,
read the document, and agrees with the outcome recorded.

| Role | Name (print) | Signature | Date |
|---|---|---|---|
| **Design lead** — owns the design and the actions | ______________________ | ______________________ | __________ |
| **Independent reviewer 1** (technical) | ______________________ | ______________________ | __________ |
| **Independent reviewer 2** (technical) | ______________________ | ______________________ | __________ |
| **Safety Officer** — owns the safety review | ______________________ | ______________________ | __________ |
| **Faculty advisor / mentor** | ______________________ | ______________________ | __________ |
| **Project lead / club office bearer** | ______________________ | ______________________ | __________ |
| **Approving authority** (faculty advisor, per `Safety_Manual_Master.md` §10) | ______________________ | ______________________ | __________ |

**Minutes filed at:** ______________________

---

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│  THE GATE                                                                                 │
│                                                                                          │
│  AFTER A PDR  →  detailed design may proceed.                                             │
│  AFTER A CDR  →  manufacture and procurement may proceed.                                 │
│                                                                                          │
│  WITHOUT A PASSED REVIEW  →  NOTHING GETS BUILT.                                          │
│  Not a "quick prototype". Not a "just to check the fit". Not a part ordered "because the  │
│  lead time is long". NOTHING GETS BUILT WITHOUT A PASSED DESIGN REVIEW.                    │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

```
Design_Review_Template  |  Rev 1.0  |  UVCE Rocketry Club  |  Retain PERMANENTLY
Use for PDR and CDR  |  Parent: 70_REPORTS/README.md §3, §4
```

*A design error is cheap on paper and expensive in metal. The reviewer's job is to find the mistake
before the metal does.*
