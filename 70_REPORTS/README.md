# UVCE Rocketry Club — Reports

**Folder:** `70_REPORTS/`
**Status:** Controlled. Reports are dated and versioned. They are the club's permanent technical record.
**Related:** `60_TEST_DATA/` (the data), `40_SAFETY/forms/` (the field records), `UVCE_Rocketry_Roadmap.md` (the programme)

> **A report is what the next team inherits.** A motor is consumed in two seconds and a graduating member
> takes their memory with them. The report is the only artefact that makes one team's failure into the
> next team's knowledge instead of the next team's accident.
>
> ## NOTHING GETS BUILT WITHOUT A PASSED DESIGN REVIEW.

---

## 1. What this folder is for

`70_REPORTS/` holds the **written, reviewed, signed** technical record of the club's work. It is not a
notes folder, not a working directory, and not a place for drafts that were never reviewed. It is what
an external examiner, a competition jury, a faculty advisor, or a future club member reads to understand
what was built, why it was built that way, what was measured, and what was learned.

**A report is filed here when it has been reviewed and signed.** Drafts live in the project's working
folder until then.

### 1.1 Folder structure

```
70_REPORTS/
├── README.md                          ← this file
├── Design_Review_Template.md          ← the reusable PDR/CDR document template
├── Test_Report_Template.md            ← the reusable test report template
├── design_reviews/
│   ├── PDR/
│   │   ├── PDR-2027-001_M-002_motor.md
│   │   └── PDR-2027-002_airframe.md
│   └── CDR/
│       ├── CDR-2027-001_M-002_motor.md
│       └── CDR-2027-002_airframe.md
├── test_reports/
│   ├── TR-2027-001_ST-003_motor_M-002.md
│   └── TR-2027-002_FL-007_flight.md
├── competition/
│   ├── INSPACe_submission_2027/
│   └── review_presentations/
├── reviews/
│   └── review_minutes/
│       └── 2027-02-14_PDR-2027-001_minutes.md
└── archive/
    └── superseded revisions, kept but not active
```

**Rules for the structure:**

- **One file per review, per test.** Do not append a new review onto an old document — a new review is a
  new document with a new number.
- **Superseded revisions move to `archive/`.** They are never deleted — the history of how a design
  changed, and why, is itself a record.
- **Signatures:** a report is signed physically on the printed copy and **scanned into the same file's
  companion PDF**. The markdown file carries the sign-off table; the PDF carries the ink.

---

## 2. What belongs in this folder

| Belongs here | Notes |
|---|---|
| **Preliminary Design Reviews (PDR)** | Per system, per project, before detailed design is committed |
| **Critical Design Reviews (CDR)** | Per system, per project, before anything is built |
| **Test reports** | Within **24 hours** of a static fire (`Static_Test_Procedure.md` §8.3); within a week of a flight day |
| **Review minutes** | Who attended, what was asked, what was decided, what actions were assigned |
| **Competition submissions** | IN-SPACe Model Rocketry Competition documents and the design report |
| **Design reports for external review** | Faculty advisor reviews, institutional reviews, mentor reviews |
| **Post-incident technical investigations** | The technical analysis that accompanies `FORM-06` — the safety report is a `40_SAFETY` record; the technical analysis lives here |
| **Trade studies and down-selection records** | Why this motor, this material, this recovery system, and not the alternatives |
| **Verification and validation matrices** | Which requirement was verified by which test or analysis |

**Does NOT belong here:**

- **Raw data and processed data** → `60_TEST_DATA/`
- **The completed field checklists** → `40_SAFETY/forms/completed/` (reference them from the report)
- **CAD, drawings, and simulation files** → the project design folder
- **Working notes, meeting scraps, and half-finished drafts** — a report is filed when it is reviewed and
  signed
- **Incident and near-miss reports** → `40_SAFETY/` records. The technical analysis may live here, but
  the safety report itself does not

---

## 3. The review process

> ### NOTHING GETS BUILT WITHOUT A PASSED DESIGN REVIEW.
>
> This is not a formality. It is the gate between a design on paper and hardware that stores megajoules
> next to people's hands and faces. **A design that has not survived a review has not been checked. A
> design that has not been checked is a design nobody has found the mistakes in — and every design has
> mistakes.**

### 3.1 Why reviews exist

- **Design errors are cheap on paper and expensive in metal.** A wrong wall thickness costs an hour and
  a red pen at a review. The same error costs a case, a test campaign, and possibly a hand.
- **The person who designed it cannot see it.** The designer knows what they meant; a reviewer only
  knows what is written down. **That gap is where the mistakes live.**
- **It creates the record.** A review produces a document that says what the design is, what it was
  checked against, what margins it carries, and what was left open. That document is what the next
  member starts from.
- **It is required externally.** The IN-SPACe competition process expects a documented design review
  trail, and so does any serious institutional or faculty review.

### 3.2 The two gates

| Gate | When | Purpose | Outcome |
|---|---|---|---|
| **PDR — Preliminary Design Review** | After concept selection, **before** detailed design is committed | Is this the right approach? Are the requirements traced? Is the preliminary sizing sound? Is the plan credible? | Pass / Pass with actions / Fail |
| **CDR — Critical Design Review** | After detailed design is complete, **before anything is built or bought** | Is this specific design compliant, analysed, margined, costed, and testable? Is every deviation justified? | Pass / Pass with actions / Fail |

**A CDR is not a repeat of the PDR.** The PDR asks *"is this the right approach?"*; the CDR asks *"is
this specific design, with these drawings and these numbers, ready to cut metal?"*

### 3.3 The process, step by step

1. **The design lead calls the review** and names a **review panel** — at least **two reviewers who did
   not author the design**, plus the Safety Officer, plus the faculty advisor or a mentor where
   available. **A designer cannot review their own design as the sole reviewer.**
2. **The review pack is circulated at least 3 days in advance.** A review where the reviewers read the
   document for the first time in the room is a presentation, not a review.
3. **The review is held.** The design lead presents against the checklist in
   `Design_Review_Template.md` §18. Reviewers **verify**; they do not merely listen.
4. **Every finding is recorded** as a numbered action with a **named owner** and a **due date**. There
   are no verbal-only findings.
5. **The outcome is declared:** **Pass**, **Pass with actions**, or **Fail**. A Fail means the gate is
   closed.
6. **Actions are tracked to closure.** A "Pass with actions" does not open the gate until the actions
   marked *blocking* are closed.
7. **The signed report and the review minutes are filed here.**
8. **Only then does the project proceed** — to detailed design after a PDR, to manufacture after a CDR.

### 3.4 Who reviews

| Reviewer | Verifies |
|---|---|
| **Design lead** (presenter, not sole reviewer) | Presents the design; owns the actions |
| **Independent reviewer 1** (technical) | Calculations, margins, materials, failure modes |
| **Independent reviewer 2** (technical) | Interfaces, integration, testability, manufacturability |
| **Safety Officer** | Hazard analysis, safety margins, procedure coverage, the safety review checklist |
| **Faculty advisor / mentor** | Academic rigour, budget realism, schedule feasibility, compliance |
| **Project lead / club office bearer** | Resource availability, schedule, dependency on other systems |

**Minimum for a valid review: two independent reviewers plus the Safety Officer.** Where the club is too
small to fill this, the faculty advisor nominates external reviewers — **the review still happens and it
is still independent.**

### 3.5 Traceability — the thread that must not break

Every review and every test report must be traceable **both ways**:

```
MISSION REQUIREMENT
   ↓ (traced to)
SYSTEM REQUIREMENT (with a number)
   ↓ (allocated to)
SUBSYSTEM / COMPONENT REQUIREMENT
   ↓ (satisfied by)
DESIGN FEATURE  →  ANALYSIS / CALCULATION  →  MARGIN
   ↓ (verified by)
TEST  →  TEST REPORT  →  RAW DATA FILE  →  CALIBRATION RECORD
```

**If any arrow is missing, the requirement is not verified** — and a requirement that is not verified is
an assumption, not an engineering claim. Reviewers should be able to walk this chain in both directions
for any requirement they pick at random.

---

## 4. PDR vs CDR — what each must contain

Both reviews follow the IN-SPACe competition requirements as recorded in the club's programme
documentation. The table below is the **minimum** content for each.

| PDR must contain | CDR must contain |
|---|---|
| **Mission requirements trace** | **Design compliance statement** |
| **Allocated system requirements** | **All deviations, with justification** |
| **Operations concept** | **Complete bill of materials, with estimate versus actual costs** |
| **Preliminary design** | **Sponsorship details** |
| **Component selection** | **Test results** |
| **Theoretical and FEA calculations, with margins on joints and fasteners** | *(carried forward and updated from the PDR)* |
| **The realisation and integration process** | *(carried forward — now frozen)* |
| **Test criteria** | *(carried forward — now with results against them)* |
| **Budget, with bill of materials** | *(now with estimate versus actual)* |
| **Development schedule** | *(now with actual progress against the plan)* |

### 4.1 PDR — Preliminary Design Review

**Question it answers:** *Is this the right approach, and is the plan to realise it credible?*

**Timing:** after concept selection and trade studies, before detailed design is committed.

**Required content:**

1. **Mission requirements trace** — every mission-level requirement, its source (competition rule,
   club objective, customer/landowner constraint, regulatory requirement), and how it flows down. **A
   requirement with no source is a wish; a requirement with no trace is a gap.**
2. **Allocated system requirements** — the mission requirements broken down and allocated to
   subsystems, **each with a number, a value, a tolerance, and a verification method**. "The motor shall
   produce 180 ± 18 N·s of total impulse, verified by static fire" is a requirement. "The motor should be
   powerful" is not.
3. **Operations concept** — how the system is used end to end: transport, assembly, integration, arming,
   launch or firing, recovery, and disposal. **Who does what, where, and in what order.**
4. **Preliminary design** — the chosen configuration, with preliminary sizing, geometry, materials, mass
   budget, and the reason each major choice was made. **Include the alternatives that were rejected and
   why** — that is the trade study.
5. **Component selection** — every bought-in item, why it was selected, its specification, its
   availability, its lead time, and what happens if it cannot be obtained.
6. **Theoretical and FEA calculations, with margins on joints and fasteners** —
   - the analytical basis: chamber pressure, thrust, burn rate, total impulse, mass flow, nozzle
     expansion;
   - structural analysis, including **FEA where appropriate**, with the boundary conditions, loads, and
     mesh stated — **an FEA result without its assumptions is a picture, not an analysis**;
   - **explicit margins on every joint and fastener**: the load, the allowable, and the resulting
     margin of safety;
   - the case sizing rule: the case should burst at **no more than 2.5 × MEOP**, with a **minimum
     acceptable safety margin of 1.5**;
   - **avoid "boilerplate" thick-walled cases** — they store an enormous amount of energy before
     bursting and *increase* the severity of a failure.
7. **The realisation and integration process** — how the design becomes hardware: manufacturing methods,
   tooling, tolerances, assembly sequence, integration checks, and the inspection points. **Identify
   what the club can actually make in-house and what must be bought or outsourced.**
8. **Test criteria** — for each requirement, the test that will verify it, the acceptance threshold, the
   instrumentation required, and the pass/fail rule. **Written before the test, not after.**
9. **Budget, with bill of materials** — every line item, quantity, unit cost, and total, with the source
   of the cost estimate. Include consumables and the cost of the test campaign.
10. **Development schedule** — the milestones, the dependencies, the critical path, and the risk that
    the schedule slips. **Schedule pressure is a hazard** (`Safety_Manual_Master.md` §5.2) — a schedule
    that only works if nothing goes wrong is a schedule that will cause a shortcut.

**PDR outcome:** ☐ Pass ☐ Pass with actions ☐ Fail

### 4.2 CDR — Critical Design Review

**Question it answers:** *Is this specific design — with these drawings, these numbers, these materials,
and this budget — ready to build?*

**Timing:** after detailed design is complete, **before anything is built or bought.**

**Required content:**

1. **Design compliance statement** — for **every** requirement from the PDR trace: the requirement, the
   achieved value, the evidence (analysis, test, or inspection), and a **compliant / partially compliant
   / non-compliant** verdict. **No requirement is left blank.** A blank cell means the design is not
   ready.
2. **All deviations, with justification** — every place the design departs from the requirement or from
   the preliminary design: what changed, why, what the consequence is, what mitigation is in place, and
   **who approved it**. **Undocumented changes are prohibited** (`Static_Test_Procedure.md` §1) — a
   deviation that is not written here is a deviation nobody has agreed to.
3. **Complete bill of materials, with estimate versus actual costs** — every part, quantity, supplier,
   part number, unit cost, and total; and **the estimate from the PDR next to the actual or quoted
   cost**, with an explanation of every variance. **A cost overrun that is not explained is a budget
   that is not under control.**
4. **Sponsorship details** — who is funding what, what has been committed, what is pending, what
   in-kind support exists, and what happens if a sponsor does not deliver. Include the deliverables and
   recognition obligations attached to each sponsorship.
5. **Test results** — the results that exist at the time of the CDR: strand burner data, material tests,
   coupon tests, component tests, hydrostatic proof tests, and any prior static fires. **Each result
   referenced to its test report and its raw data.** Where a test has not yet been run, say so
   explicitly and state which CDR action depends on it.
6. **Carried forward and updated** — the requirements trace, the operations concept, the design
   description, the analysis and margins, the interfaces, the realisation and integration process, the
   test criteria, and the schedule, **all updated to their final state**.

**CDR outcome:** ☐ Pass ☐ Pass with actions ☐ Fail

### 4.3 The gate

> **After a PDR:** detailed design may proceed.
> **After a CDR:** manufacture and procurement may proceed.
> **Without a passed review:** **nothing gets built.** Not a "quick prototype", not a "just to check the
> fit", not a part ordered "because the lead time is long". **Nothing gets built without a passed design
> review.**

---

## 5. Test reports

**Every test gets a test report.** A static fire report is due **within 24 hours** — written while the
detail is fresh, before the debrief fades (`Static_Test_Procedure.md` §8.3). A flight report is due
within a week of the flight day.

**Use `Test_Report_Template.md`.** The report contains, at minimum:

1. **Test identification** — test ID, date, location, motor/rocket ID, batch number
2. **Objective** — what this test was meant to determine
3. **Article under test** — configuration, grain geometry and mass, nozzle throat diameter, igniter type
   and charge, propellant batch and density ratio, tap test result
4. **Instrumentation and calibration validity** — instrument IDs, calibration record IDs, validity dates
5. **Procedure reference** — the procedure and revision followed, and the completed field checklist
6. **Environmental conditions** — distance, wind, temperature, humidity, sky
7. **Results** — thrust curve, pressure curve, total impulse, burn time, delivered Isp, peak thrust,
   peak pressure, each referenced to its data file
8. **Anomalies observed**
9. **Comparison against prediction** — **the measured performance against the design prediction, with
   any discrepancy explained**
10. **Conclusions** — and explicitly, **what single variable will change next**
11. **Lessons learned**
12. **Sign-off** by the Test Director and the Safety Officer

**One test proves nothing.** A repeatable design needs **3–5 identical motors with overlapping thrust
curves**, changing **one variable at a time** between tests. The test report must state which variable
changed.

**Sign-off:** the Test Director and the Safety Officer sign. Where the report makes a design claim that
affects the CDR, the faculty advisor reviews it.

---

## 6. Review minutes

Every review produces **minutes** filed in `reviews/review_minutes/`. They record:

- Date, time, place, and attendees (with roles), and who was absent
- The review pack reference and the revision reviewed
- **Every question asked**, and the answer given
- **Every finding**, as a numbered action with an owner and a due date
- The declared outcome
- Which actions are **blocking** (the gate stays closed until they close) and which are advisory
- The date and agenda of the follow-up review, where one is required

**Minutes are the evidence that the review actually happened.** A review with no minutes is a
conversation.

---

## 7. Document control, numbering, and retention

### 7.1 Numbering

| Document | Number format | Example |
|---|---|---|
| Preliminary Design Review | `PDR-<YYYY>-<###>` | `PDR-2027-001` |
| Critical Design Review | `CDR-<YYYY>-<###>` | `CDR-2027-001` |
| Test Report | `TR-<YYYY>-<###>` | `TR-2027-003` |
| Review minutes | `<YYYY-MM-DD>_<review-id>_minutes` | `2027-02-14_PDR-2027-001_minutes` |

**Filenames:** `<doc-id>_<subject>_<system>.md`, e.g.
`CDR-2027-001_M-002_motor.md`, `TR-2027-003_ST-003_motor_M-002.md`.

### 7.2 Every report carries, on its first page

- Document ID and revision (`Rev 1.0`, `Rev 1.1`, …)
- Date of issue
- Author(s) and reviewer(s), by name
- **Applies to** — the exact system, motor, airframe, or test it covers
- **Supersedes** — the revision it replaces, or "—" for a first issue
- Approval signatures

**A revision change is a new file.** The superseded revision goes to `archive/`. **Do not edit a signed
report** — issue a revision.

### 7.3 Retention

- **Design reviews, test reports, and review minutes: retained permanently**
  (`Safety_Manual_Master.md` §8.4).
- **They survive member graduation — that is the point.** A report filed by a final-year member in one
  year is read by a first-year member three years later.
- **The report goes to the club's permanent record and to the faculty advisor** and is **dated and
  versioned** (`Static_Test_Procedure.md` §8.3).
- **Records are handed over** at every office-bearer transition, with a written inventory of what was
  handed over and to whom.

---

## 8. Related documents

| Document | What it gives you |
|---|---|
| `70_REPORTS/Design_Review_Template.md` | The reusable PDR/CDR document template, with the reviewer's verification checklist |
| `70_REPORTS/Test_Report_Template.md` | The reusable test report template |
| `60_TEST_DATA/README.md` | The data these reports are built on — raw data, naming, the test log workbook |
| `60_TEST_DATA/Calibration_Record.md` | Instrument calibration validity, which every test report must state |
| `40_SAFETY/forms/FORM-04_Static_Test_Checklist.md` | The field sheet that produces the static fire data |
| `40_SAFETY/forms/FORM-05_Flight_Day_Checklist.md` | The field sheet that produces the flight data |
| `40_SAFETY/Static_Test_Procedure.md` §8.3 | Test report contents and the 24-hour deadline |
| `40_SAFETY/Safety_Manual_Master.md` §8.4 | Records retention |

---

*Nothing gets built without a passed design review. A report without a signature is a draft; a design
without a review is a gamble.*
