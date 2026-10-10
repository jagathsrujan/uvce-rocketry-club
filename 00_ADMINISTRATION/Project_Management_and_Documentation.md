# PROJECT MANAGEMENT AND DOCUMENTATION

## UVCE Rocketry Club (URC)

| Field | Detail |
|---|---|
| Document ID | URC-ADMIN-PM-001 |
| Version | 1.0 |
| Owner | Documentation Lead (custodian), Team Lead (accountable), every Lead (compliance in their subsystem) |
| Companion to | `Club_Charter.md` Articles 8 and 12; `Roles_and_Responsibilities.md` |
| Review cycle | Annually in March, at the Continuity Review |

---

## 1. WHY DOCUMENTATION IS THE CLUB'S MOST VALUABLE ASSET

### 1.1 The graduation cliff

Every year, in May or June, the Club loses its most experienced members. This is not a risk that might materialise; it is a certainty with a known date. What happens next depends entirely on one thing: **what those members left behind.**

- If they left **their knowledge in their heads**, the Club restarts from zero. The new team re-derives stability margins, re-discovers that the fin attachment fails at a certain load, re-orders the wrong motor casing, re-learns that the launch site floods in October.
- If they left **a written record**, the new team starts from where the last team finished. They read the last design record, see the open problems, look up the measured mass of every part, find the vendor who actually delivers on time, and get to spend their year on new problems instead of old ones.

**The difference between those two clubs is not talent, or money, or luck. It is documentation.**

### 1.2 What documentation actually is

Documentation is not a report written at the end to satisfy someone. It is the **engineering record kept as the work happens**, and it serves five concrete purposes:

| Purpose | What it does |
|---|---|
| **Continuity** | Lets next year's team start from this year's endpoint rather than from scratch |
| **Correctness** | Forces the author to notice the step they skipped, the assumption they never checked, the unit they got wrong |
| **Safety** | A written procedure is what makes a hazardous operation repeatable, reviewable and stoppable |
| **Credibility** | Competition submissions, sponsors, the College and any authority all judge the Club by what it can show |
| **Fairness** | Written credit ensures the people who did the work are known to have done it |

### 1.3 The rules this document exists to enforce

1. **A decision that is not recorded did not happen.** It will be re-litigated by next year's team at full cost.
2. **Nothing lives on one person's laptop.** Ever. For any reason. (Section 10)
3. **Documentation is engineering work, not overhead.** It counts towards a member's contribution exactly as much as fabrication does, and it is assessed in probation, in role appointments and in handovers.
4. **A handover without a written note is not a handover.** (Section 9)
5. **The record is blameless in intent, and honest in content.** Failures are recorded in full. Data is never adjusted. (Constitution Clause 9.2(d))

### 1.4 The cost of not documenting — a worked example

> **Year 1.** The team designs a fin can. The fins flutter at a certain speed and one sheds during a test flight. They fix it by adding a layer of fibreglass and thickening the root chord. It works. Nobody writes down why. The fix is a WhatsApp message and a memory.
>
> **Year 2.** A new team designs a new fin can, from first principles, with the same fin profile that failed. They discover the flutter problem in a test flight. They lose a vehicle and a motor reload — perhaps ₹8,000 and three weeks — and they spend two meetings working out a fix that the previous team already knew.
>
> **Year 3.** Same again, unless someone wrote it down.
>
> **The cost of that one unrecorded lesson, over three years: roughly ₹16,000–₹24,000, six weeks of schedule, and two avoidable failures — plus the loss of the confidence that comes from a team knowing what it is doing.**

---

## 2. THE DOCUMENTATION STANDARD

### 2.1 The core requirement — decision records

**Every design decision shall be recorded, at the time it is made, in the Design Record.** A design decision is any choice that constrains later work: a configuration, a dimension, a material, a component, a motor class, a recovery method, a vendor, a test approach, or the deliberate decision to do nothing about a known problem.

Each entry shall contain all of the following. **An entry missing any of these fields is incomplete and will be returned by the Documentation Lead.**

| Field | Content | Example |
|---|---|---|
| **DR-ID** | Sequential decision record identifier | `DR-2026-014` |
| **Date** | The date the decision was made (not the date it was written up) | 2026-11-14 |
| **Title** | One line naming the decision | Fin attachment method for Vehicle-1 |
| **Context** | Why a decision was needed at all | Fin attachment through the body tube wall was suspected of being the failure point in the September test flight |
| **Options considered** | At least two, honestly described, including "do nothing" | (a) Through-the-wall (TTW) tabs, (b) surface-mounted with epoxy fillets, (c) surface-mounted with fibreglass tip-to-tip reinforcement |
| **Decision** | The option chosen, stated unambiguously | Option (a): TTW tabs into the motor mount, plus internal fillets |
| **Rationale** | *Why* — the actual reasoning, with numbers where available | TTW transfers load into the motor mount rather than relying on the tube-to-fin bond; measured pull-off strength of the surface-mounted joint (from the Sept test) was below the calculated flight load with margin |
| **Evidence / data** | Test data, calculations, references, simulation files | `TEST-2026-007_fin-pull-test.pdf`; `ANALYSIS_fin-loads_v3.xlsx` |
| **Alternatives rejected and why** | This is the most valuable field for the next team | (b) rejected for insufficient strength; (c) rejected because the team had no experience with tip-to-tip layup and the schedule did not allow for learning it |
| **Decided by** | Named person, with the role | S. Kumar, Structures Lead |
| **Consulted** | Named people whose input was sought | Propulsion Lead (motor mount interface), Safety Officer (fabrication hazards) |
| **Status** | Proposed / Approved / Superseded / Reversed | Approved |
| **Reversibility** | Easy / Costly / Irreversible, and what reversing would take | Costly — changing attachment after the tube is slotted requires a new body tube |
| **Supersedes / superseded by** | Links to related decisions | Supersedes DR-2026-009 |
| **Open questions** | What is still unknown about this decision | Whether the internal fillet can be reached through the forward end on the flight article |

### 2.2 Why "options considered" and "alternatives rejected" matter most

A record that says only "we chose TTW fins" tells next year's team what to do but not whether it is still the right answer. A record that says "we chose TTW over surface mounting because the measured pull-off strength was below the calculated load, and we rejected tip-to-tip because we lacked layup experience" gives the next team the information to decide whether **their** situation is different — and it tells them exactly what would have to change for a different choice to become correct.

**The reasoning is the asset. The decision is just its output.**

### 2.3 Documentation types and where they live

| # | Record | Content | Owner | Update frequency | Retention |
|---|---|---|---|---|---|
| 1 | **Design Record** | Decision records (Section 2.1) | Documentation Lead | As decisions are made | Permanent |
| 2 | **Drawings & CAD** | Models, fabrication drawings, assembly drawings, revision history | Structures Lead | On change | Permanent |
| 3 | **Analysis** | Calculations, simulations, spreadsheets, scripts, with assumptions stated | Relevant Lead | On change | Permanent |
| 4 | **Test Log** | Every test: setup, conditions, data, outcome, conclusions (Section 5.1) | Testing Lead | Within 48 hrs of the test | Permanent |
| 5 | **Incident Register** | Incidents and near-misses, blameless, with corrective actions | Safety Officer | Within 24 hrs | Permanent |
| 6 | **Safety Log** | Hazard assessments, procedures, go/no-go checklists, halts and clearances | Safety Officer | Per activity | Permanent |
| 7 | **Financial Ledger & BOM** | Every transaction; estimate vs actual per vehicle | Treasurer | Within 48 hrs | Permanent |
| 8 | **Meeting Minutes** | All meetings (Section 8) | Documentation Lead | Within 72 hrs | Permanent |
| 9 | **Approvals File** | Every permission, letter, intimation, acknowledgement | Documentation Lead | On receipt | Permanent |
| 10 | **Succession & Critical Knowledge Registers** | Named successors; competencies and RED items | Documentation Lead | Start of each semester | Permanent |
| 11 | **Member Register & Skills Matrix** | Members, attendance, demonstrated competencies | VP + Doc Lead | Each semester | Permanent |
| 12 | **Handover Packs** | One per role per year | Outgoing office-bearer | Annually | Permanent |
| 13 | **Exit Interviews & lessons notes** | What departing members wish they had known | Doc Lead | Annually | Permanent |
| 14 | **Procurement & vendor records** | Quotations, purchase orders, invoices, delivery notes, warranty | Treasurer + Leads | Per purchase | Permanent |
| 15 | **Photographs & video** | Build, test, launch, damage, repair — with dates and captions | Designated media member | Continuous | Permanent |
| 16 | **Competition submissions** | Every submitted document, plus the acknowledgement | Doc Lead | Per submission | Permanent |

### 2.4 Writing standard

- **Write for the person who replaces you**, not for yourself. Assume they are intelligent, motivated, and know nothing about what you did.
- **Be specific.** "The fin bond failed" is useless. "The fin root bond failed at approximately 45 N of applied load, at the leading-edge end of the root, with the epoxy showing no adhesion to the tube surface — the tube was not abraded before bonding" is a lesson.
- **State units always.** `N`, `N·s`, `mm`, `g`, `MPa`, `m/s`. A number without a unit is a defect.
- **State assumptions explicitly** and mark them as assumptions.
- **Record uncertainty honestly**: "estimated", "calculated", "measured", "assumed", "taken from the vendor's datasheet". These are four different levels of confidence and must not be conflated.
- **Record failures in full.** What broke, when, how, and what you concluded. **A failure documented is worth more than a success documented**, because it is the thing that cannot be re-derived.
- **Date everything.** An undated document is nearly worthless.
- **Name the author.** Credit and accountability both require it.
- **Write in English** (Constitution Clause 17.5), in plain sentences, with short paragraphs.

---

## 3. NAMING CONVENTIONS

Consistency matters more than elegance. **A file whose name explains itself saves the next person a painful search.** The Documentation Lead shall enforce these conventions, and non-conforming files may be renamed.

### 3.1 General file naming

```
YYYY-MM-DD_<DOC-TYPE>_<SUBSYSTEM>_<SHORT-DESCRIPTION>_v<MAJOR>.<MINOR>.<EXT>
```

**Examples:**
```
2026-11-14_DR_STRUCT_fin-attachment-method_v1.0.md
2026-11-20_TEST_PROP_static-test-03_v2.1.pdf
2026-12-01_DWG_STRUCT_vehicle1-assembly_v3.0.pdf
2026-12-03_MINUTES_general-body_v1.0.md
2026-12-10_APPR_DISTRICT_launch-permission_v1.0.pdf
2027-01-15_BOM_ALL_vehicle1-final_v2.0.xlsx
2027-02-02_PHOTO_LAUNCH_flight-04-apogee_v1.0.jpg
```

**Rules:**
- **Date first** in `YYYY-MM-DD`. This sorts chronologically by default, which is the single most useful property a filename can have.
- **Lowercase, hyphens not spaces, no special characters** (`&`, `#`, `/`, `%`, `(`, `)`), no non-ASCII characters. Hyphens, underscores and alphanumerics only. This prevents broken links, encoding problems and script failures.
- **No "final", "latest", "new", "final2", "final_FINAL", "copy of", or a person's initials.** Version numbers replace all of these, and a person's name belongs inside the document, not in the filename.
- **Description of 3–6 words.** Enough to identify the file without opening it.
- **Version suffix for documents and drawings** (see 3.2). Images, receipts and scans may carry a date and description only.

### 3.2 Versioning

**Format:** `v<MAJOR>.<MINOR>`

| Change | Version | Meaning |
|---|---|---|
| **Major** (`v1.0` → `v2.0`) | A change that invalidates previous work: a dimension change that affects mating parts, a material change, a configuration change, a released drawing reissued | Anyone using the old version must be told |
| **Minor** (`v2.0` → `v2.1`) | Editorial, clarification, additional data, a note added, a typo fixed, no change to the engineering content | Old version still describes the same design |

**Rules:**
- **`v0.x` is draft, `v1.0` onwards is released.** A released document is one that others may build to or rely on.
- **Never overwrite a released version.** Issue the next number. The old version is retained permanently (Constitution Article 12.8).
- **Every released document carries a version block** at the top:

```markdown
| Version | Date | Author | Change | Approved by |
|---|---|---|---|---|
| 1.0 | 2026-11-14 | S. Kumar | Initial release | Team Lead |
| 1.1 | 2026-11-21 | S. Kumar | Root chord increased 15 mm after pull test | Structures Lead |
| 2.0 | 2026-12-02 | A. Rao | Attachment changed to through-the-wall | Team Lead |
```

- **A change to a released drawing requires a new revision, not an edit.** On engineering drawings, carry a **revision table** in the title block with revision letter, date, description and approver.
- **The flown/used configuration must be identifiable.** For every flight, record the exact revision of every flight-critical part, and the exact software revision that flew.

### 3.3 Drawing and CAD conventions

**CAD file naming:** `YYYY-MM-DD_CAD_<SUBSYSTEM>_<part-name>_v<M>.<m>.<native-ext>`
```
2026-11-18_CAD_STRUCT_fin-can-assembly_v2.0.FCStd
2026-11-18_CAD_PROP_nozzle-v3_v1.2.step
```

**Rules:**
- **One part, one file.** No multi-part files with names like "misc" or "parts".
- **Export a neutral format** (STEP or PDF) alongside the native file, so that a future team with different software can still open it. **This is not optional** — a native file from software the College no longer licenses is a dead file.
- **Always export a PDF of every released drawing.** PDFs open everywhere and cannot be accidentally edited.
- **Assembly naming:** `<vehicle>_<assembly>` — e.g. `Vehicle1_fin-can-assembly`.
- **Every released drawing must show:** part name, part number, revision, scale, units, material, finish, tolerances where critical, dimensions with units, author, date, approver, and the revision table.
- **Units on the drawing, always — and state them in text** ("ALL DIMENSIONS IN mm"). Unit errors are a classic and expensive student failure: a part modelled in inches and exported as millimetres is scrap.
- **Mark critical dimensions** explicitly, and note which are inspection dimensions that must be measured and recorded.

**Suggested part numbering:**
```
<VEHICLE>-<SUBSYSTEM>-<SEQUENCE>
V1-STR-001   Vehicle 1, Structures, part 001
V1-PROP-004  Vehicle 1, Propulsion, part 004
V1-AV-002    Vehicle 1, Avionics, part 002
```
Subsystem codes: `STR` structures · `PROP` propulsion · `AV` avionics · `REC` recovery · `GSE` ground support equipment · `TEST` test hardware.

### 3.4 Test log and data file naming

```
YYYY-MM-DD_TEST_<SUBSYSTEM>_<test-name>_<test-number>
```

**Rules for data files:**
- **Never overwrite raw data.** Raw files from the data logger, the camera, the altimeter or the GPS are write-once. Copy, do not edit in place.
- **Raw data and processed data are separate files**, in separate folders. The chain from raw to processed must be reproducible by a script that is in the repository.
- **Every processed file states what was done to the raw data**: filtering, calibration applied, samples dropped and why.
- **Calibration records sit with the data**, with the date of calibration and the reference used.

### 3.5 Folder structure — the archive

```
UVCE-Rocketry-Club/
├── 00_ADMINISTRATION/
│   ├── Club_Charter.md
│   ├── Roles_and_Responsibilities.md
│   ├── Recruitment_and_Onboarding.md
│   ├── Institutional_Approvals_and_Compliance.md
│   ├── Funding_and_Sponsorship.md
│   ├── Project_Management_and_Documentation.md
│   ├── approvals/            ← every permission and letter, by year
│   ├── compliance/           ← hazard assessments, procedures, incident register
│   ├── finance/              ← ledger, BOMs, receipts, audit reports
│   ├── meetings/             ← minutes, by year
│   ├── registers/            ← member, succession, critical knowledge, skills matrix
│   ├── handovers/            ← one pack per role per year
│   └── submissions/          ← competition and college submissions
├── 01_DESIGN/
│   ├── design-record/        ← the decision records
│   ├── requirements/         ← mission requirements and constraints
│   ├── analysis/             ← calculations, simulations, scripts
│   ├── cad/                  ← native + STEP exports
│   ├── drawings/             ← released PDF drawings
│   └── reviews/              ← PDR/CDR packages, review minutes, action closure
├── 02_VEHICLES/
│   └── V1/                   ← one folder per vehicle
│       ├── PROP/  STR/  AV/  REC/  GSE/
│       ├── BOM/
│       ├── as-built/         ← measured masses, inspection records, deviations
│       └── flight-data/
├── 03_TESTS/
│   ├── 2026/
│   │   ├── TEST-2026-001_fin-pull/
│   │   │   ├── procedure/
│   │   │   ├── raw-data/
│   │   │   ├── processed/
│   │   │   ├── photos/
│   │   │   └── TEST-2026-001_report.md
│   │   └── …
│   └── test-index.md         ← one row per test, linking to its folder
├── 04_SOFTWARE/
│   ├── flight-software/      ← git submodule or its own repository
│   ├── ground-station/
│   └── analysis-scripts/
├── 05_TRAINING/
│   ├── safety-induction/
│   ├── openrocket/
│   ├── electronics-basics/
│   └── hand-tools/
├── 06_OUTREACH/
│   ├── workshops/
│   ├── demonstration-flights/
│   └── media/                ← photographs, videos, posters, logos
├── 07_ALUMNI/
│   ├── register.md
│   ├── annual-reports/
│   └── exit-interviews/
└── 99_ARCHIVE/
    └── superseded/           ← nothing is deleted; superseded files move here
```

**Rules for the structure:**
- **The structure is published at the start of every semester** by the Documentation Lead, and every member is expected to file into it.
- **Do not create new top-level folders** without the Documentation Lead's agreement. A structure with fifteen top-level folders is a structure nobody can navigate.
- **Nothing is deleted.** Superseded material moves to `99_ARCHIVE/superseded/`, with the superseding document referenced.
- **Every folder has a `README.md`** explaining what belongs in it and who owns it. This takes ten minutes and saves hours.

---

## 4. DESIGN REVIEW PROCESS

### 4.1 Purpose and principle

A design review is a **structured, scheduled examination of the design by people who did not create it**, held at a defined point, against defined entry criteria, producing a written record of findings and actions.

Its purpose is **not** to approve a design, and not to demonstrate how clever the team is. It is to **find the problems while they are still cheap to fix**. A problem found at PDR costs an afternoon. The same problem found after the airframe is built costs a rebuild and a month.

**The review culture the Club must build:**
- **Criticism is directed at the design, never at the person.**
- **The presenter is expected to say what they are unsure about.** A presentation with no acknowledged uncertainties is a presentation that has not been thought about.
- **A finding is not an insult; it is the review doing its job.** A review that produces no findings has either examined nothing or been too polite to be useful.
- **No design is approved by default** because time is short.

### 4.2 Preliminary Design Review (PDR)

**When:** when the concept is fixed and the design direction is chosen, but before detailed design, before significant procurement, and before any hardware is cut.

**Purpose:** to confirm that the requirements are understood, the concept will meet them, the plan is achievable, and the risks — including the *people* risks — are identified.

**Mandatory entry criteria (the review does not proceed without these):**
- Mission requirements documented: target altitude, payload, recovery method, impulse class, site constraints, competition class.
- At least one complete concept, with **at least two alternatives documented and the reason for rejecting them recorded** in the Design Record.
- Preliminary mass and CG estimate, and a preliminary stability margin.
- Preliminary performance prediction from a simulation, with the assumptions stated.
- Preliminary structural load estimate.
- A preliminary BOM with rough costs, compared against the available budget.
- A preliminary schedule with milestones, and a named owner for every subsystem.
- A safety and permissions assessment: what approvals will be needed, what the hazardous operations are, and who the Safety Officer is.
- A **staffing and continuity assessment**: who owns each subsystem, who their named successor is, and which competencies are single-point-of-failure (from the Critical Knowledge Register).

**What the PDR package must contain (the review pack, circulated at least 3 days in advance):**

| # | Item | Owner |
|---|---|---|
| 1 | Requirements and constraints statement | Team Lead |
| 2 | Concept of operations: how the flight actually happens, step by step | Operations Lead |
| 3 | Configuration description and trade study, with alternatives and rationale | Relevant Leads |
| 4 | Preliminary mass, CG and stability budget | Structures Lead |
| 5 | Preliminary performance prediction (simulation files and assumptions) | Structures/Propulsion |
| 6 | Propulsion concept, impulse class, commercial or planned motor | Propulsion Lead |
| 7 | Recovery concept and deployment method | Structures/Recovery |
| 8 | Avionics architecture, power and mass estimate, data plan | Avionics Lead |
| 9 | Structural concept and preliminary loads | Structures Lead |
| 10 | Preliminary BOM and budget, with funding status | Treasurer |
| 11 | Schedule with milestones, critical path, and owners | Team Lead |
| 12 | Risk register: technical, safety, financial, **and people/continuity** | Team Lead |
| 13 | Safety and permissions plan | Safety Officer |
| 14 | Continuity plan: successors, competencies, RED items | Documentation Lead |

**PDR outcomes:** the design is confirmed, modified, or returned for rework. **Every finding gets a number, an owner and a due date; nothing closes without evidence.** Findings are tracked to closure in the review's action register, and **the PDR is not closed until every action is closed or explicitly waived in writing by the Team Lead with a stated reason.**

### 4.3 Critical Design Review (CDR)

**When:** when detailed design is complete and **before any irreversible fabrication, before major procurement, and before any flight of the vehicle.**

**Purpose:** to confirm that the design is buildable, safe, and will meet the requirements, and that every drawing, dimension, material and interface is final.

**Mandatory entry criteria:**
- PDR findings all closed or formally waived.
- Complete CAD models and released drawings, with revision numbers.
- Complete structural analysis with margins stated for every load case.
- Mass and CG budget from **calculated and, where available, measured** part masses, with the flight configuration's CG and stability margin stated.
- Full performance prediction with sensitivity to the main uncertainties (mass, drag, thrust, wind).
- Propulsion design final, with the static test data if a test has been run, or the commercial motor's data and a verification plan.
- Recovery design final, with deployment loads, sizing calculations and a test plan.
- Avionics design final: architecture, wiring diagram, power budget, software revision plan, bench and range test plan.
- Fabrication plan: processes, jigs, tolerances, inspection points, and who does what.
- Complete BOM with quotations and confirmed funding, and the funding gap stated honestly if one exists.
- Complete test plan: what will be tested, how, where, with what instrumentation and what acceptance criteria.
- Safety case: hazard assessment for every operation, written procedures, go/no-go checklists, exclusion zones, emergency plan.
- Permissions status: what is obtained, what is applied for, what is outstanding — **in writing, with dates**.
- Continuity check: is any subsystem still dependent on one person? (RED items from the Critical Knowledge Register.)

**What the CDR package must contain:** everything in the PDR package, updated and final, plus:

| # | Additional item | Owner |
|---|---|---|
| 15 | Complete released drawing set (PDF + native + STEP) | Structures Lead |
| 16 | Structural analysis report with margins and assumptions | Structures Lead |
| 17 | As-designed mass and CG table, part by part | Structures Lead |
| 18 | Final performance prediction with uncertainty and sensitivity | Analysis owner |
| 19 | Static test report (if applicable) and motor data | Propulsion Lead |
| 20 | Recovery deployment analysis and test results | Recovery owner |
| 21 | Avionics test results: bench, hardware-in-the-loop, range | Avionics Lead |
| 22 | Fabrication and assembly plan with inspection points | Structures Lead |
| 23 | Test and acceptance plan for the vehicle | Team Lead |
| 24 | Reference mission timeline: every event from arming to recovery | Operations Lead |
| 25 | Failure modes and effects: what happens if each critical item fails, and the mitigation | All Leads |
| 26 | Competition compliance check against the current rulebook | Documentation Lead |
| 27 | **Handover readiness statement**: what would a successor need, and is it in the archive? | Documentation Lead |

**CDR outcomes:** the design is **released for fabrication and flight**, or returned. **No irreversible fabrication and no flight may proceed without a closed or formally waived CDR.** This is a hard rule. A club that fabricates before its CDR is a club that has decided that review is optional, and the review is the only thing standing between a student and an injury.

### 4.4 Review participants and roles

| Role | Who | Responsibilities |
|---|---|---|
| **Chair** | Team Lead, or a senior member not on the presenting subsystem | Runs the review to the agenda, keeps time, ensures findings are recorded, closes the review |
| **Presenters** | The subsystem's owner | Presents the design, states uncertainties honestly, answers questions |
| **Reviewers** | Faculty Advisor, Alumni Mentors, other Leads, senior members, **and at least one junior member** | Ask hard questions; challenge assumptions; verify evidence |
| **Safety reviewer** | Safety Officer | Reviews hazards, procedures and compliance; **may veto the design on safety grounds** |
| **Scribe** | Documentation Lead | Records every question, finding, decision and action with an owner and a due date |
| **Junior observer** | At least one 1st/2nd-year member | Learns how reviews work, and is invited to ask at least one question — **this is a training mechanism, not a courtesy** |

**Faculty Advisor and Alumni Mentor boundary at reviews** (see `Roles_and_Responsibilities.md`): both may ask questions, request evidence and flag risks. **Neither may make design decisions or give design recommendations.** If either offers a technical opinion, the scribe records it in the minutes as advice, attributed, and the decision remains the team's.

### 4.5 How to run an effective design review

**Before:**
1. **Fix the date two weeks ahead** and put it in the calendar. Reviews that are scheduled "when we're ready" never happen.
2. **Circulate the pack at least 3 days in advance.** Reviewers who read the pack beforehand give useful comments; reviewers who see it for the first time in the room give opinions.
3. **Give reviewers a one-page summary** at the front: what is being decided, what has changed since the last review, and **what the team is unsure about**.
4. **Explicitly invite the awkward questions.** Ask reviewers in advance to look for specific things: mass growth, unit errors, interface mismatches, single points of failure, unverified assumptions, missing permissions.
5. **Prepare the room:** projector, a printed copy of the drawings for each reviewer, and the previous review's action register.

**During:**
6. **Start on time. Keep to the agenda.** Time-box each section; a review that runs four hours produces fatigue, not findings.
7. **The presenter states uncertainties first**, before the questions. This sets the tone: the review is about finding problems, not about defending a design.
8. **Every finding is captured in the room, with an owner and a date.** A finding not written down is a finding lost.
9. **Separate questions from findings.** A question seeks information; a finding is an issue requiring action. The scribe records both, distinctly.
10. **No design decision is made in the corridor after the review.** If a decision is needed, it goes into the Design Record.
11. **End with a clear disposition:** approved / approved with actions / returned for rework, and a stated date for the next review.

**After:**
12. **Circulate minutes and the action register within 72 hours.**
13. **Track every action to closure** in the project tracker, with evidence.
14. **The review is not closed until every action is closed or formally waived in writing**, with the reason recorded.
15. **Hold a five-minute retrospective:** what worked about this review, what did not, and what the Club will change next time. Record it — this is how the Club's review practice improves.

**Common failure modes to avoid:**
- Reviewing after the part is made. (The most common and most expensive.)
- Inviting only friends who will be positive.
- Presenting only the finished-looking parts and hiding the uncertain ones.
- No written actions, so the same findings reappear next review.
- Reviewing the slides rather than the design: **demand the drawings, the calculations and the test data, not the presentation.**
- The most senior person present talking the most.

---

## 5. TEST LOG AND INCIDENT REPORT TEMPLATES

### 5.1 TEST LOG TEMPLATE

> **File as:** `YYYY-MM-DD_TEST_<SUBSYSTEM>_<test-name>_<number>.md`
> **Complete within 48 hours of the test, while memory is fresh.** A test log written a week later is a reconstruction, not a record.

```markdown
# TEST LOG — TEST-YYYY-NNN

## 1. Identification
| Field | Value |
|---|---|
| Test ID | TEST-2026-007 |
| Test name | Fin attachment pull-off test, through-the-wall vs surface-mounted |
| Date and time | 2026-11-14, 10:15–13:40 IST |
| Location | Workshop, UVCE Mechanical Department (approved access ref: URC-APR-2026-008) |
| Subsystem | Structures |
| Vehicle / article | Test article TA-FIN-02 (not flight hardware) |
| Test conductor | S. Kumar, Structures Lead |
| Persons present | S. Kumar, A. Rao, P. Nair (Safety Officer), 2 observers |
| Related decision records | DR-2026-014 |
| Related drawing revisions | V1-STR-007 v1.0 |

## 2. Objective
To measure the pull-off strength of the two candidate fin attachment methods and compare
against the calculated flight load of 180 N with a target margin of 2.0.

## 3. Success criteria (stated BEFORE the test)
| Criterion | Threshold |
|---|---|
| TTW configuration ultimate load | ≥ 360 N (2.0 × flight load) |
| Surface-mounted configuration ultimate load | Report only (comparison) |
| Both specimens fabricated to the released drawing | Visual + dimensional check |

## 4. Setup
| Item | Detail |
|---|---|
| Test rig | Universal testing machine, Mech Dept lab, 5 kN load cell |
| Instrumentation | Load cell (calibration cert: LC-2026-03, calibrated 2026-08-02), 10 Hz sampling |
| Fixture | Custom fin root clamp, drawing `TEST-FIX-001 v1.0` |
| Specimens | 2 × body tube sections, 2 × fin sets, epoxy per drawing V1-STR-007 v1.0 |
| Environmental conditions | 24 °C, 58% RH |
| Deviations from procedure | None / [describe] |

## 5. Procedure (as executed — note any deviation)
1. Specimen dimensions verified with vernier; recorded in Section 6.
2. Specimen mounted in the fixture, alignment checked.
3. Load applied at 2 mm/min until failure or 1000 N.
4. Failure mode photographed and described.
5. Repeat for specimen 2.

## 6. Raw data
| Specimen | Configuration | Peak load (N) | Failure mode | Notes |
|---|---|---|---|---|
| TA-FIN-02-A | Surface-mounted, epoxy fillet | 214 | Adhesive failure at tube interface | Tube surface not abraded |
| TA-FIN-02-B | Through-the-wall + internal fillet | 512 | Tube wall tear-out | Exceeded rig expectation |

Raw data file: `03_TESTS/2026/TEST-2026-007_fin-pull/raw-data/loadcell_2026-11-14.csv`
Photographs: `03_TESTS/2026/TEST-2026-007_fin-pull/photos/`

## 7. Analysis
- TTW margin achieved: 512 / 180 = 2.84 (target 2.0) → PASS
- Surface-mounted margin: 214 / 180 = 1.19 → FAIL (insufficient)
- The surface-mounted failure was adhesive (not cohesive), suggesting surface preparation
  was inadequate; even with better preparation, the margin would remain insufficient.

## 8. Result against success criteria
| Criterion | Result | Pass / Fail |
|---|---|---|
| TTW ≥ 360 N | 512 N | **PASS** |
| Surface-mounted reported | 214 N | Reported |
| Specimens to drawing | Verified | PASS |

## 9. Conclusions
Through-the-wall attachment with internal fillets meets the required margin and is adopted.
Surface mounting is rejected. Surface preparation must nonetheless be specified for all
bonded joints (abrade + solvent wipe) because the adhesive failure mode observed here is a
process risk that would affect any bonded interface.

## 10. Actions arising
| # | Action | Owner | Due | Status |
|---|---|---|---|---|
| 1 | Update drawing V1-STR-007 to TTW (revision 2.0) | S. Kumar | 2026-11-21 | Closed |
| 2 | Record decision in Design Record | S. Kumar | 2026-11-18 | Closed |
| 3 | Add surface-preparation note to all bonding procedures | Structures Lead | 2026-11-30 | Open |

## 11. Anomalies and lessons
- The rig's fixture slipped on the first attempt at 90 N, which is not recorded as a data
  point. Fixture redesigned. **Lesson: check the fixture's own capacity before testing
  the article, or the first data point measures the fixture.**
- Neither specimen was instrumented for strain; we could not determine where the load path
  actually ran. Add strain gauges next time.

## 12. Sign-off
| Role | Name | Date |
|---|---|---|
| Test conductor | S. Kumar | 2026-11-14 |
| Safety Officer | P. Nair | 2026-11-14 |
| Documentation Lead (filed) | R. Iyer | 2026-11-15 |
```

### 5.2 INCIDENT REPORT TEMPLATE

> **File as:** `YYYY-MM-DD_INCIDENT_<short-description>.md`
> **Complete within 24 hours. Report to the Faculty Advisor and Team Lead in writing the same day** (Constitution Clause 4.7). **Blameless in intent: the purpose is to find the cause, not the culprit. Concealment is a disciplinary matter; reporting is not.**

```markdown
# INCIDENT REPORT — INC-YYYY-NNN

## 1. Classification
| Field | Value |
|---|---|
| Incident ID | INC-2026-002 |
| Classification | Incident / **Near-miss** / Property damage / Injury / Regulatory |
| Severity | Minor / Moderate / Serious / Critical |
| Date, time, location | 2026-12-05, 09:42 IST, [site name, survey no., village] |
| Reported by | [Name, role] |
| Reported to (Safety Officer) at | 09:45 |
| Reported to Faculty Advisor at | 11:20 (same day) |
| Persons involved | [Names and roles] |
| Injuries | None / [describe: nature, body part, treatment, hospital, outcome] |
| Property damage | [describe, with estimated cost] |
| Emergency services | Not required / [which, when, response] |
| Activity in progress | Launch of Vehicle-1, flight 03 |

## 2. What happened (factual narrative, no blame, no speculation)
At 09:42, during the countdown for flight 03, the igniter was armed at the range box.
The continuity check indicated continuity. At T-10, a participant entered the pad area
to adjust the launch rail angle, contrary to the briefing which stated nobody approaches
the pad after arming. The RSO called a halt. The participant withdrew. The igniter was
disarmed and removed before any further action.

## 3. Sequence of events (timeline)
| Time | Event |
|---|---|
| 09:30 | Range brief conducted; arming procedure stated |
| 09:38 | Pad crew withdrew; range declared clear |
| 09:41 | Igniter armed; continuity confirmed |
| 09:42 | Participant entered the pad area |
| 09:42 | RSO called halt; arming circuit opened |
| 09:44 | Pad area cleared; igniter removed and made safe |
| 09:50 | Operations suspended; team briefed |
| 10:30 | Activity resumed after a revised briefing |

## 4. Immediate actions taken
- Ignition circuit opened and igniter removed.
- All personnel withdrawn; area made safe.
- Team briefed on the arming rule.
- Activity paused for 48 minutes and resumed only after a re-brief.

## 5. Root cause analysis
**Immediate cause:** a participant entered the pad area after arming.
**Contributing factors:**
- The briefing stated the rule but did not assign a specific person to physically control
  access to the pad after arming.
- The participant was a first-time attendee who had not attended the range briefing because
  they arrived late; there was no check that everyone present had been briefed.
- There was no physical barrier or marker at the arming line.
**Root cause:** access control to the pad after arming was a stated rule with no assigned
owner, no physical barrier, and no verification that all present had been briefed.

## 6. Corrective actions
| # | Action | Type (eliminate/guard/warn/procedure/training) | Owner | Due | Status |
|---|---|---|---|---|---|
| 1 | Assign a named Pad Access Controller for every launch; this person's only duty is to prevent entry after arming | Procedural + physical | Ops Lead | Immediate, all future launches | Closed |
| 2 | Physical barrier and painted arming line at every range setup | Engineering control | Ops Lead | 2026-12-20 | Open |
| 3 | Attendance check at the range brief: nobody participates without being marked present | Procedural | Safety Officer | Immediate | Closed |
| 4 | Late arrivals must be briefed separately before any role is assigned | Procedural | Safety Officer | Immediate | Closed |
| 5 | Add this incident as a case study in the safety induction | Training | Safety Officer | 2027-01-10 | Open |

## 7. Lessons for the Club
- A safety rule without a named owner, a physical control, and a verification step is a
  rule that will eventually be broken by someone who never heard it.
- "Everyone was briefed" is an assumption. A signed or ticked attendance record is a fact.
- The halt worked exactly as intended. The RSO's immediate stop prevented any injury.
  **The halt is the system working, not the system failing.**

## 8. Follow-up verification
| Action # | Verified by | Date verified | Evidence |
|---|---|---|---|
| 1 | Safety Officer | 2026-12-06 | Named in the flight-04 range plan |
| 3 | Safety Officer | 2026-12-06 | Attendance sheet filed |
| 2, 4, 5 | Safety Officer | [pending] | — |

## 9. Sign-off
| Role | Name | Date |
|---|---|---|
| Reported by | [Name] | 2026-12-05 |
| Safety Officer | P. Nair | 2026-12-05 |
| Team Lead | [Name] | 2026-12-05 |
| Faculty Advisor (acknowledged) | [Name] | 2026-12-06 |
| Documentation Lead (filed) | [Name] | 2026-12-06 |
```

**Rules for incident reporting:**
- **Report within 24 hours, always, including near-misses.** A near-miss is a free lesson; an incident is an expensive one. **Near-misses are the most valuable reports the Club produces**, because they identify the hazard before it produces an injury.
- **Blameless in intent.** The report finds causes, not culprits. Disciplinary matters are handled separately under Constitution Article 10, on the basis of the report — never instead of it.
- **Concealment is a disciplinary matter** (Constitution Clause 4.3(g) and Article 10.1). Reporting is not.
- **Corrective actions are verified in writing with evidence.** An action marked "closed" without verification is not closed.
- **Every incident and near-miss is presented at the next general meeting**, so the whole Club learns.

---

## 6. VERSION CONTROL

### 6.1 The rule

**All documents and all code shall be version-controlled, and the Club's required tool is Git.**

A shared folder is not version control. "Final_v3_latest" is not version control. Version control means: every change is recorded, attributed and reversible; two people can work on the same file without overwriting each other; and any past state can be recovered exactly.

### 6.2 Why Git, specifically

- **It is free and standard**, and it is what a member will be expected to know in industry. **Teaching Git is a legitimate engineering skill transfer and should be in the onboarding pathway** (see `Recruitment_and_Onboarding.md` §7.1, module S5).
- **It records who changed what, when, and why** — which is exactly the design-decision record the Club needs, in the place the work actually happens.
- **It makes the archive indestructible by accident.** Every member has a full copy; a lost laptop loses nothing.
- **It allows branches**, so a risky rewrite of the flight software happens without breaking the working version.
- **It handles text well** (Markdown, code, CSV, small drawings) and reasonably well for binary files (CAD, images) with Git LFS where needed.

### 6.3 Repository structure

**Recommended: one repository per major area, under a single Club organisation account (GitHub or GitLab).**

```
uvce-rocketry-club (organisation)
├── admin-and-docs        ← this documentation set, minutes, registers, approvals index
├── flight-software       ← embedded code, with tagged releases per flown configuration
├── ground-station        ← ground software, telemetry decoding, GUI
├── analysis              ← Python/MATLAB scripts, simulation models, data reduction
├── design-files          ← CAD (native + STEP), drawings (PDF), with Git LFS for binaries
└── website               ← if the Club maintains one
```

**Access rules:**
- **All members get read access to everything.** Universal read access is non-negotiable (Constitution Article 12.6) — a member who cannot see the archive cannot learn from it.
- **Write access to `main` is limited** to the Leads of the relevant area and the Documentation Lead.
- **Everyone else contributes via branches and pull requests**, with at least one review before merge. This is not bureaucracy: a second pair of eyes on a flight-critical calculation is exactly the safety culture the Club is trying to build.
- **A minimum of three people hold organisation-owner rights** — the Team Lead, the Documentation Lead and the Vice President — **so that one graduation cannot lock the Club out of its own repositories.** (Constitution Clause 12.7.)
- **Use the Club's account, never a personal account**, and never a member's personal email as the account owner's recovery address. **Account recovery is a continuity risk: document the recovery method in the credentials store, and hand it over at every leadership handover.**

### 6.4 Branching, commits and tags

**Branching (keep it simple):**
```
main            ← always correct, always releasable
dev             ← integration branch for larger changes
<name>/<topic>  ← short-lived working branches, e.g. ravi/fin-drawing-rev2
```

**Commit messages** — the standard format:
```
<area>: <what changed>

<why it changed>
```

Examples:
```
prop: increase nozzle throat diameter 2 mm to 9 mm

Chamber pressure was 12% above prediction in static test 03.
Throat enlarged to bring Kn into the design range. See TEST-2026-011.
```
```
docs: add DR-2026-014 fin attachment decision

Records the TTW decision and the pull-test evidence.
```

**Rules:**
- Commit **small and often**, with a message explaining *why*, not just *what*. "Update file" is a useless commit message.
- **Never commit secrets**: passwords, API keys, bank details, member personal data, or files containing them. If committed by accident, treat the credential as compromised and change it immediately.
- **Never commit large binaries without Git LFS** — a 500 MB CAD file in a repository makes it unusable for everyone.
- **Tag every flown or tested configuration:**
```
v1.0-flight-03     ← the exact software + configuration that flew flight 03
v1.1-bench         ← bench-tested revision
```
**The flown revision must be recorded in the flight data and the test log.** Without it, the flight data cannot be interpreted and the bug cannot be found.

**Version-controlled code discipline:**
- **A `README.md` in every repository** explaining what it is, how to build it, how to upload it to the hardware, and who owns it. A repository without a build instruction is a repository nobody can use next year.
- **A pinned dependency list** (requirements.txt, platformio.ini, package.json) so a build is reproducible.
- **Pin the toolchain version** in the README (which compiler, which IDE version, which board definition). Toolchain drift silently breaks builds.
- **Tests where practical** — at minimum, a documented bench procedure that anyone can follow.
- **Never edit code on the hardware and leave the repository behind.** If it flew, it is committed.

### 6.5 Documents in Git

- Markdown for text (this documentation set, design records, minutes, procedures, reports) — Git diffs it beautifully, which means every change to a procedure is visible and reviewable.
- Spreadsheets and Office documents: keep them, but consider maintaining the **authoritative** version of critical tables (BOM, ledger, skills matrix) in a format that diffs (CSV) and using the spreadsheet as a view.
- **PDFs for released drawings** — final outputs, committed alongside the native files.
- **A `CHANGELOG.md`** in the docs repository: one line per significant change, so the Club's documentation history is browsable.

### 6.6 The minimum viable alternative

If, in the founding months, a full Git setup is not yet in place, the Club shall at minimum maintain **dated, versioned files in a shared cloud folder with at least two owners**, and shall migrate to Git within the first semester. **A single shared folder with no version history is a temporary measure, not a solution** — and the migration must be on the Documentation Lead's deliverable list, with a date.

---

## 7. PROJECT TRACKER AND WORK BREAKDOWN STRUCTURE

### 7.1 Principle

The Club's work is decomposed into a **work breakdown structure (WBS)**, with a named owner for every element and a stated deliverable. **Anything without an owner and a date does not exist.**

**And critically: every technical work package has a documentation work package attached to it.** Not as a separate phase at the end, but as part of the same task. You do not "finish the fin design and then document it"; finishing the fin design *includes* filing the drawing, the analysis and the decision record.

### 7.2 Work breakdown structure — a template

```
1.0  VEHICLE V1 PROGRAMME                            [Owner: Team Lead]
│
├── 1.1  Requirements and mission definition         [Owner: Team Lead]
│   ├── 1.1.1 Mission requirements document          → REQ-V1-v1.0.md
│   ├── 1.1.2 Site and permission constraints        → input to 1.8
│   └── 1.1.3 Competition class and rulebook check   → compliance matrix
│
├── 1.2  Systems engineering and design record       [Owner: Documentation Lead]
│   ├── 1.2.1 Design Record maintenance              → DR entries, current
│   ├── 1.2.2 Interface control (mass, CG, power)    → ICD-1.0.md
│   └── 1.2.3 Configuration control and revisions    → released baseline
│
├── 1.3  Propulsion subsystem                        [Owner: Propulsion Lead]
│   ├── 1.3.1 Motor selection and verification       → DR + datasheet + calc
│   ├── 1.3.2 Grain/motor hardware design (if any)   → drawings + analysis
│   ├── 1.3.3 Static test plan and procedure         → procedure signed by Safety Officer
│   ├── 1.3.4 Static test execution                  → TEST logs + raw data
│   └── 1.3.5 Documentation package                  → propulsion section of PDR/CDR
│
├── 1.4  Structures and airframe                     [Owner: Structures Lead]
│   ├── 1.4.1 Configuration and trade study          → DR with alternatives
│   ├── 1.4.2 CAD and released drawings              → V1-STR-### v1.0 (PDF + STEP)
│   ├── 1.4.3 Structural analysis                    → analysis report with margins
│   ├── 1.4.4 Mass and CG budget                     → live spreadsheet
│   ├── 1.4.5 Fabrication and jigs                   → fabrication plan + jig drawings
│   ├── 1.4.6 Structural tests                       → TEST logs
│   ├── 1.4.7 Inspection record and as-built         → as-built deviations list
│   └── 1.4.8 Documentation package                  → structures section
│
├── 1.5  Recovery system                             [Owner: Structures/Recovery Lead]
│   ├── 1.5.1 Sizing calculations and design         → analysis + DR
│   ├── 1.5.2 Deployment method and energetics       → procedure signed by Safety Officer
│   ├── 1.5.3 Ground deployment tests                → TEST logs
│   └── 1.5.4 Documentation package
│
├── 1.6  Avionics and software                       [Owner: Avionics Lead]
│   ├── 1.6.1 Architecture and interface design      → avionics architecture doc
│   ├── 1.6.2 Flight software development            → repository, tagged releases
│   ├── 1.6.3 Bench and HIL testing                  → TEST logs
│   ├── 1.6.4 Ground station and telemetry           → ground station README + range test
│   ├── 1.6.5 Pre-flight checklist                   → signed checklist
│   ├── 1.6.6 Flight data analysis                   → flight data report
│   └── 1.6.7 Documentation package
│
├── 1.7  Ground support and range equipment          [Owner: Operations Lead]
│   ├── 1.7.1 Launch rail, pad, ignition system      → drawings + equipment register
│   ├── 1.7.2 Range box, tools, spares               → packing list
│   └── 1.7.3 Equipment maintenance and inventory    → semiannual inventory record
│
├── 1.8  Safety, compliance and permissions          [Owner: Safety Officer]
│   ├── 1.8.1 Hazard assessments and procedures      → one per hazardous activity
│   ├── 1.8.2 Go/no-go checklists                    → per test and launch
│   ├── 1.8.3 Emergency response plan                → per site
│   ├── 1.8.4 Site permission and district approvals → Approvals Register
│   ├── 1.8.5 Impulse calculation and band check     → written calculation per activity
│   ├── 1.8.6 Incident and near-miss register        → INC entries
│   └── 1.8.7 Safety induction and training records  → attendance records
│
├── 1.9  Finance and procurement                     [Owner: Treasurer]
│   ├── 1.9.1 Budget and funding pipeline            → budget tracker
│   ├── 1.9.2 Procurement and vendor management      → quotations, POs, invoices
│   ├── 1.9.3 Ledger and receipts                    → financial ledger
│   ├── 1.9.4 Bill of materials (estimate vs actual) → BOM sheet
│   └── 1.9.5 Sponsorship register and reporting     → register + utilisation reports
│
├── 1.10 Reviews and gates                           [Owner: Team Lead]
│   ├── 1.10.1 PDR package and review                → pack + minutes + action register
│   ├── 1.10.2 CDR package and review                → pack + minutes + action register
│   ├── 1.10.3 Action closure                        → closure evidence for every action
│   └── 1.10.4 Flight readiness review               → signed readiness checklist
│
├── 1.11 Test and launch campaign                    [Owner: Operations Lead]
│   ├── 1.11.1 Campaign plan                         → written plan
│   ├── 1.11.2 Permissions verified                  → Approvals Register entries
│   ├── 1.11.3 Execution and range logs              → range log per day
│   ├── 1.11.4 Post-campaign debrief                 → debrief record within 72 hours
│   └── 1.11.5 Flight data reports                   → one per flight
│
├── 1.12 Competition                                 [Owner: Team Lead + Doc Lead]
│   ├── 1.12.1 Rulebook compliance matrix            → compliance check
│   ├── 1.12.2 Technical report                      → submission package
│   ├── 1.12.3 Safety documentation                  → submission package
│   ├── 1.12.4 Bill of materials                     → competition format
│   ├── 1.12.5 Institutional approval letter         → letter with full roster
│   ├── 1.12.6 Submission and acknowledgement        → proof of submission, filed
│   └── 1.12.7 Post-competition lessons report       → written, circulated to the whole Club
│
├── 1.13 People, recruitment and continuity          [Owner: Team Lead + VP]
│   ├── 1.13.1 Recruitment drive                     → plan, posters, applications
│   ├── 1.13.2 Onboarding and 30/60/90 check-ins     → records per member
│   ├── 1.13.3 Training modules                      → syllabi, attendance, assessments
│   ├── 1.13.4 Mentorship pairing                    → recorded pairings
│   ├── 1.13.5 Skills matrix                         → current matrix
│   ├── 1.13.6 Succession Register                   → one successor per role
│   ├── 1.13.7 Critical Knowledge Register           → two-deep check, RED items
│   └── 1.13.8 March Continuity Review               → review report
│
└── 1.14 Outreach and communication                  [Owner: Operations Lead + VP]
    ├── 1.14.1 Demonstration flights                 → plans, permissions, reports
    ├── 1.14.2 Workshops for schools/PU colleges     → materials, attendance, feedback
    ├── 1.14.3 Social media and website              → content calendar, posts
    └── 1.14.4 Alumni engagement                     → register, annual report, appeal
```

**Note that 1.13 (People) is a first-class work package with the same status as propulsion or structures.** That is deliberate. **A club that treats recruitment and continuity as an afterthought will not exist in three years, however good the rocket was.**

### 7.3 Project tracker structure

Maintained in a shared spreadsheet or a project board (GitHub Projects, Trello, or a simple sheet). **Whatever tool is used, it must be accessible to all members and it must be updated weekly**, or it becomes a work of fiction.

| Column | Field | Notes |
|---|---|---|
| A | Task ID | WBS reference, e.g. `1.4.2` |
| B | Task | Specific, actionable, starting with a verb |
| C | WBS area | 1.0–1.14 |
| D | Owner | **One named person. Never two, never "the team".** |
| E | Deputy / understudy | The two-deep rule applied at task level |
| F | Start date | |
| G | Due date | |
| H | Status | Not started / In progress / Blocked / In review / **Closed** |
| I | Deliverable | The artefact that proves it is done (a file, a test log, a drawing, a signature) |
| J | Dependencies | Task IDs that must complete first |
| K | Blockers | What is stopping it, and who can unblock it |
| L | Last updated | Date |
| M | Evidence link | Path or URL to the deliverable in the archive |
| N | Reviewer / approver | Who signs it off |

**Tracker rules:**
1. **One owner per task.** A task with two owners has none.
2. **A task is only "Closed" when its deliverable exists in the archive and is linked in column M.** "Done" without an artefact is not done.
3. **Blocked tasks are escalated at the next Core Team meeting**, with the blocker named and the unblocking action assigned.
4. **The tracker is reviewed at every weekly Core Team meeting**, area by area, with each Lead reporting their own.
5. **The Team Lead's contribution to the tracker is the critical path** — the sequence of tasks that determines whether the campaign happens. Everything else can slip; the critical path cannot.
6. **Documentation tasks are on the critical path, not appended to it.** A test that has no filed test log is not complete, and the next task does not start.

### 7.4 Schedule and milestone discipline

**Milestones (gates) for a typical campaign:**

| Milestone | Gate criteria | Approver |
|---|---|---|
| **M1 — Requirements frozen** | Requirements document released | Team Lead |
| **M2 — PDR passed** | PDR pack reviewed; all actions closed or waived | Team Lead + Faculty Advisor informed |
| **M3 — Permissions secured** | Site, district and institutional approvals in hand | Safety Officer |
| **M4 — CDR passed** | CDR pack reviewed; design released for fabrication | Team Lead + Safety Officer |
| **M5 — Fabrication complete** | As-built record, inspection record, mass and CG updated | Structures Lead |
| **M6 — Bench and structural tests passed** | Test logs filed; success criteria met | Relevant Lead |
| **M7 — Flight readiness review passed** | Readiness checklist signed: hardware, software, procedures, permissions, personnel, weather limits, recovery plan | Team Lead + Safety Officer |
| **M8 — Flight campaign executed** | Range logs, flight data, incidents (if any) filed | Operations Lead |
| **M9 — Reported and archived** | Flight data report, BOM finalised, lessons recorded, all files archived | Documentation Lead |

**M9 is not optional and is not the last thing squeezed in.** A campaign that flies and does not report and archive has produced a memory, not an asset.

**Scheduling rules:**
- **Work backwards from the launch or competition date**, not forwards from today.
- **Add explicit contingency** — at least 30% on fabrication, 50% on approvals, and 100% on a first-of-its-kind task.
- **Approvals are the longest-lead item.** Start them before the design is finished (see `Institutional_Approvals_and_Compliance.md`).
- **Schedule around examination periods explicitly.** Publish the exam windows on the plan and do not put critical tasks in them. **A plan that pretends exams do not exist is a plan that will fail in the exam weeks, every year.**
- **Cut scope, never safety and never documentation.** If the schedule slips, the response is to fly a smaller vehicle, not to skip the CDR, the hazard assessment, or the test log.

---

## 8. MEETING MINUTES TEMPLATE

> **File as:** `YYYY-MM-DD_MINUTES_<meeting-type>_v1.0.md`
> **Circulate within 72 hours. File in the archive the same day.** (Constitution Clause 11.7.)

```markdown
# MINUTES — [Core Team / General Body / Steering Committee / Design Review]

| Field | Detail |
|---|---|
| Date and time | 2026-11-20, 17:05–18:35 IST |
| Venue | Room M-204, Mechanical Block / Google Meet |
| Chair | [Name], Team Lead |
| Minutes by | [Name], Documentation Lead |
| Present | [Name (role)], [Name (role)], … |
| Absent with apologies | [Name], [Name] |
| Absent without apology | [Name] |
| Quorum | Yes — 6 of 9 Core Team positions filled |
| Distribution | All members (WhatsApp group + repository) |
| Next meeting | 2026-11-27, 17:00, Room M-204 |

## 1. Safety review  ← ALWAYS THE FIRST ITEM
- No incidents or near-misses since the last meeting.
- Open corrective action from INC-2026-002: physical barrier at the arming line — **still open, due 2026-12-20**.
- Hazard assessment for the December static test is drafted; Safety Officer to circulate for comment before sign-off.

## 2. Review of previous action items
| # | Action (from 2026-11-13) | Owner | Due | Status | Note |
|---|---|---|---|---|---|
| 1 | Order motor reloads | Treasurer | 2026-11-18 | **Closed** | Ordered; invoice in the ledger |
| 2 | Update fin drawing to revision 2.0 | S. Kumar | 2026-11-21 | **In progress** | 80% complete; due date holds |
| 3 | Confirm district permission application | Ops Lead | 2026-11-15 | **Overdue** | Application submitted late; new date 2026-11-25 |

## 3. Progress against plan (by WBS area)
| Area | Owner | Status | Notes |
|---|---|---|---|
| 1.4 Structures | S. Kumar | On track | Fin attachment resolved; drawing revision in progress |
| 1.5 Recovery | A. Rao | **At risk** | Parachute supplier delayed; evaluating an alternative |
| 1.6 Avionics | R. Iyer | On track | Bench test passed; range test scheduled |
| 1.8 Safety/approvals | P. Nair | **At risk** | District permission delayed; may affect the December window |
| 1.9 Finance | [Name] | On track | Balance ₹41,200; two funding applications pending |

## 4. Decisions taken
| # | Decision | Rationale | Decided by | DR reference |
|---|---|---|---|---|
| 1 | Move the December test to the January window rather than fly without the district permission | The permission is a hard requirement; a delayed test is recoverable, an unpermitted test is not | Core Team, unanimous | DR-2026-021 |
| 2 | Adopt TTW fin attachment | Pull test showed a margin of 2.84 vs the required 2.0 | Structures Lead | DR-2026-014 |

## 5. Discussion (brief summary of substantive points, not a transcript)
- The recovery supplier has quoted a four-week lead time, which does not fit the January window. Two alternatives were discussed: an in-house parachute (the team has a member with sewing experience) and a higher-priced local supplier. The Recovery owner will price both and report at the next meeting.
- The Treasurer reported that the alumni appeal has raised ₹15,000 from four donors, and that a utilisation report is due to them within 30 days of the launch.

## 6. Action items
| # | Action | Owner | Due | Evidence required |
|---|---|---|---|---|
| 1 | Complete fin drawing revision 2.0 and file it | S. Kumar | 2026-11-21 | PDF + native file in the repository |
| 2 | Follow up the district permission application in person | Ops Lead | 2026-11-25 | Written acknowledgement or a note of what was said, filed |
| 3 | Price both recovery options and report | A. Rao | 2026-11-24 | Comparison table, filed |
| 4 | Circulate the hazard assessment for comment | P. Nair | 2026-11-23 | Circulation email filed |
| 5 | Send sponsor utilisation report | Treasurer | 2026-12-15 | Report filed + acknowledgement received |

## 7. People and pipeline  ← STANDING ITEM
- New members: 4 applications received this week; interview panel on 2026-11-24.
- Skills matrix updated: telemetry decoding still a RED item with only one competent member. **Action: pair R. Iyer with a 1st-year member for the next range test.**
- Succession Register: Structures Lead successor nominated (K. Menon). Avionics Lead successor still vacant — **flagged to the Steering Committee**.

## 8. Finance
| Item | Amount (₹) |
|---|---|
| Opening balance | 38,500 |
| Income this period | 15,000 (alumni) |
| Expenditure this period | 12,300 (motors and epoxy) |
| Closing balance | 41,200 |
| Outstanding commitments | 8,000 (recovery system) |

## 9. Any other business
- Department has offered workshop access on Saturday mornings from December. Accepted; Structures Lead to publish the schedule.

## 10. Next meeting
2026-11-27, 17:00, Room M-204. Standing agenda: safety review; previous actions; progress by area; decisions; actions; people and pipeline; finance; AOB.

---
**Minutes approved by:** ____________________ (Chair)  **Date:** ____________
```

**Minutes rules:**
- **Minutes are a record of decisions and actions, not a transcript.** Summarise discussion in a few lines; record decisions and actions precisely.
- **Every action has one owner and one due date.** An action without both is not an action.
- **Decisions record the rationale**, not just the outcome — that is what makes the minutes useful next year.
- **The safety review is always item 1.** Always. Without exception.
- **The people-and-pipeline item is always present** (recruitment, onboarding, skills, succession). Without it, the Club's most important work is the only work that never gets discussed.

---

## 9. HANDOVER PROCESS AND CHECKLIST

### 9.1 The rule

**No one leaves a role without a completed handover** (Constitution Article 8.4). The consequence of non-compliance is stated at appointment: **no Club service certificate, no letter of recommendation, no competition-credit letter.**

### 9.2 The five-step handover

**Step 1 — Write the handover note (3–10 pages).** Using the template below. Due **at least 14 days before** the handover meeting.

**Step 2 — Audit the files.** Every artefact in the archive, correctly named, versioned and complete. Nothing on a personal device. Nothing missing. Cryptographic hashes are unnecessary; a folder listing checked against the tracker is enough.

**Step 3 — Live walkthrough (2 hours).** The outgoing holder briefs the successor and demonstrates access to every system: the repository, the bank or finance records, the approvals file, the equipment, the accounts, the vendor contacts, the software.

**Step 4 — Joint handover meeting.** With the Team Lead and the Documentation Lead, minuted. The outgoing holder presents the note; the successor asks questions; open risks are listed.

**Step 5 — Sign-off.** **The successor confirms in writing that they can find the files, operate the systems, and name the open problems.** If they cannot, **the handover is not complete**, and the Documentation Lead shall refuse to record it as complete.

### 9.3 Handover note template

```markdown
# HANDOVER NOTE — [Role] — [Academic Year]

| Field | Detail |
|---|---|
| Role | Structures Lead |
| Outgoing holder | [Name], [branch], graduating [year] |
| Incoming holder | [Name], [branch], [semester] |
| Date of handover meeting | 2027-04-18 |
| Successor designated on | 2026-09-01 (Constitution Clause 8.1) |

## 1. State of the work
Where the subsystem actually is, in plain terms. What is finished, what is half-finished,
what is designed but not built, what is built but not tested. Be specific about the
flight vehicle's current condition and what it would take to fly it again.

## 2. What is decided, and what is still open
A list of the key decisions made this year (with DR references) and the questions that
remain unresolved. For each open question: what it blocks and what information would
resolve it.

## 3. Known problems
Every known defect, weakness, non-conformance, workaround and accepted risk.
Include the ones that were never written up officially, and the ones that were
"temporarily" fixed. Include the non-conformances that were accepted and why.
**This section is the most valuable part of the note. Do not soften it.**

## 4. File and archive index
Where everything is: the folder paths, the key documents, the drawing revisions,
the test logs, the raw data, the analysis scripts. A reader should be able to find
any artefact from this section alone.

## 5. Vendor and contact list
| Vendor / contact | What for | Contact | Rates / terms | Reliability note |
|---|---|---|---|---|
Include suppliers, machinists, the workshop supervisor, the landowner, the district
office contact, and the Faculty Advisor.

## 6. Access and credentials
What access the role requires, and confirmation that it has been transferred
(transferred through the credentials store, never written in this document).
- Repository write access: transferred / pending
- Club email: transferred / pending
- Bank signatory or finance access: transferred / pending
- Lab and workshop access: transferred / pending
- Vendor accounts: n/a

## 7. Equipment and assets
| Item | Location | Condition | Notes |
|---|---|---|---|
Include tools, test stands, jigs, spares, PPE, and anything the Club owns. Note what is
broken, worn, missing, or on loan to someone.

## 8. Calendar and recurring obligations
Every recurring date the role must meet: review dates, permission renewals, safety
inductions, competition deadlines, department meetings, the March Continuity Review.

## 9. Successor training record
What the incoming holder was actually taught this year, what real work they did,
what they have demonstrated, and what they have not yet done at all. **Be honest:
a successor who has never done the task alone is not yet a successor.**

## 10. Advice to my successor
Three to ten things you wish you had known at the start. The most useful sentences in
this document. Include what you would do differently, what you would not attempt again,
and what you would protect at all costs.

## 11. What I never got around to
The honest list. Every outgoing holder has one. Writing it down is what stops the next
person assuming it was already done.

## 12. Sign-off
| Role | Name | Signature | Date |
|---|---|---|---|
| Outgoing holder | | | |
| Incoming holder (confirms access to all files and systems) | | | |
| Team Lead | | | |
| Documentation Lead (handover complete / not complete) | | | |
```

### 9.4 Handover checklist — every role

- [ ] Handover note written and circulated at least 14 days before the meeting
- [ ] All files in the archive, correctly named and versioned; **nothing on a personal device**
- [ ] Repository access transferred and verified by the successor logging in
- [ ] Credentials transferred through the credentials store, **not written in the handover note**
- [ ] Equipment physically handed over and the equipment register updated
- [ ] Financial records reconciled and signed (Treasurer, and any role holding an imprest)
- [ ] Approvals file checked: all current permissions present, with expiry dates and renewal reminders set
- [ ] Vendor and contact list complete
- [ ] Succession Register updated with the new successor designation for the role
- [ ] Critical Knowledge Register updated; **any RED item reported to the Steering Committee**
- [ ] Live walkthrough conducted (2 hours)
- [ ] Joint handover meeting held, with the Team Lead and Documentation Lead, and minuted
- [ ] **Successor has demonstrated they can find every file and operate every system unaided**
- [ ] Successor has named the open problems back to the outgoing holder
- [ ] Exit interview offered and, where given, filed
- [ ] "What I wish I had known" note written for the archive
- [ ] Sign-off completed by all four parties

**A handover with an unticked box is incomplete, and the Documentation Lead shall not record it as complete.** An incomplete handover is reported to the Team Lead and, for roles in the process of graduating, to the Faculty Advisor.

---

## 10. ARCHIVING, BACKUP AND THE ONE-PERSON RULE

### 10.1 The rule

> **Nothing lives on one person's laptop. Ever. For any reason.**
>
> Not the CAD files. Not the flight software. Not the ledger. Not the only photograph of the launch. Not the test data that took six hours to collect. Not this document.

This rule is not about tidiness. It is about the specific, predictable, and entirely avoidable catastrophe of a member's laptop failing, being stolen, or leaving the country with the Club's entire technical history on it.

### 10.2 Where files live

| Tier | What it is | What goes there | Access |
|---|---|---|---|
| **1. Primary archive** | The Club's Git organisation and shared drive | Everything: the master copies of all documents, code, data, drawings, records | All members read; Leads and Doc Lead write |
| **2. Cloud backup** | A second cloud location, on a different provider or account | A mirror of the primary archive, updated automatically where possible, **at least monthly otherwise** | Three named holders |
| **3. Physical backup** | An external drive or two, held by two different people | A full copy, refreshed **once per semester**, and after every campaign | Doc Lead + one other Core Team member |
| **4. Distributed copies** | Every member's own working copy via Git | The natural by-product of Git — every clone is a full backup | All members |
| **5. Field copies** | A USB drive or offline device taken to test and launch days | The current procedures, checklists, permissions, BOM, contact list — **because rural sites often have no signal** | Operations Lead |

### 10.3 What is backed up, and how often

| Content | Frequency | Where |
|---|---|---|
| Documents, minutes, registers (text) | Continuous, via Git | Primary + cloud + distributed |
| Design record, drawings, CAD | On every change, via Git | Primary + cloud + physical |
| Test and flight data (raw) | Immediately after every test — **same day** | Primary + cloud + physical |
| Photographs and video | Within 48 hours of capture | Primary + cloud + physical |
| Financial records and receipts | Within 7 days (scans), plus the physical originals | Primary + cloud + physical (originals in the financial file) |
| Approvals and permissions | Same day as receipt | Primary + cloud + a printed copy carried to the site |
| Full archive snapshot | Once per semester, and after every campaign | Physical drive, verified |

### 10.4 Verification — a backup nobody has tested is not a backup

- **Once per semester, the Documentation Lead shall perform a documented restore test:** pick three files at random from the backup, restore them to a clean location, open them, and confirm they are complete and current.
- **Record the test in writing**, with the date, the files tested and the result.
- **Report the result at the next Core Team meeting.** A failed restore test is escalated to the Team Lead immediately.
- **Check the backup's currency**, not just its existence: an automatic backup job that silently stopped in September is worse than no backup, because it creates false confidence.

### 10.5 Retention — what is kept forever

**Permanent (never deleted):** the Design Record · Test Logs and raw data · Incident Register and Safety Log · Financial Ledger, receipts and audit reports · Approvals File · meeting minutes · Handover Packs · Succession and Critical Knowledge Registers · exit interviews and lessons notes · competition submissions · the Constitution and its amendment history.

**Retained for the life of the vehicle plus three years:** CAD files, drawings, analysis, BOMs.

**May be archived:** routine correspondence, working notes, superseded drafts, exploratory work that led nowhere — **archived, not deleted**, in `99_ARCHIVE/`.

**Never deleted without the Documentation Lead's and Team Lead's joint written approval**, recorded in the minutes. **Superseded is not the same as useless**: knowing which design was rejected, and why, is often more valuable than knowing which was chosen.

### 10.6 The archive's role at the graduation cliff

The archive is where the Club's memory lives when its people leave. Accordingly:

- **The March Continuity Review shall include an archive health check**: is the year's work actually in the archive? Can the incoming team find it? Are any subsystems documented only in one person's head?
- **A subsystem with no documentation in the archive is treated as a RED item**, exactly as a subsystem with only one competent member is.
- **The Faculty Advisor holds a copy of the archive index**, and the Department holds a copy of the archive under Constitution Article 8.7 — so that even a complete collapse of the Club's membership does not destroy its records.
- **The alumni register, the annual reports and the exit interviews are the Club's longest-lived documents.** They are the only things that will still be read in ten years. **Write them accordingly.**

### 10.7 The one-sentence version

**If the Club lost every laptop, every phone and every member tomorrow, could a new team read the archive and understand what was built, what was learned, and what to do next?** That is the test. Everything in this document exists to make the answer yes.

---

## 11. QUICK REFERENCE — THE TEN RULES

1. **A decision that is not recorded did not happen.**
2. **Every decision record states the alternatives considered and why they were rejected.**
3. **Date everything; units always; assumptions explicit; failures in full.**
4. **`YYYY-MM-DD_TYPE_SUBSYSTEM_description_vM.m.ext` — and never "final".**
5. **No irreversible fabrication and no flight without a closed CDR.**
6. **Test logs within 48 hours; incident reports within 24. Blameless in intent.**
7. **Git for everything. Tag every flown configuration.**
8. **One owner per task; a task is closed only when its deliverable is in the archive.**
9. **No one leaves a role without a signed handover.**
10. **Nothing lives on one person's laptop.**

---

*End of Project Management and Documentation, Version 1.0.*

*This document set — `Club_Charter.md`, `Roles_and_Responsibilities.md`, `Recruitment_and_Onboarding.md`, `Institutional_Approvals_and_Compliance.md`, `Funding_and_Sponsorship.md`, `Project_Management_and_Documentation.md` — is the founding administration of the UVCE Rocketry Club. It is written to be amended, and the first amendment should probably come from the first person who reads it and finds something that does not work. That is the process functioning correctly.*
