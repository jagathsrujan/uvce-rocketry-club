# UVCE Rocketry Club — Roadmap to IN-SPACe Model Rocketry India Student Competition 2027

**Prepared for:** Jagath Srujan, Mechanical Engineering, UVCE (3rd sem)
**Location:** UVCE, K.R. Circle, Bengaluru 560001
**Target:** IN-SPACe Model Rocketry India Student Competition (3rd Edition, 2027)
**Budget envelope:** ₹2–3 lakh (college + alumni funding)

---

## 1. THE SINGLE MOST IMPORTANT CORRECTION

Previous planning assumed the team must **design and build its own KNSB motors**.

**This is not permitted in this competition.**

> **Rule 5.vi (2026 guidelines):** *"The rockets must have only one stage that shall be powered only by **commercially-made model rocket motors, procured from Vendors identified by IN-SPACe**."*
>
> **Rule 5.vii:** *"The rocket motor capacity designed by teams cannot exceed **2800 Newton-seconds** of total impulse."*
>
> **Chapter 12:** *"The participating teams shall **mandatorily procure the motor from such identified vendors only**, at a pre-fixed price."*

The motor is a **given input**, not a design output. Custom propellant work belongs in a **separate experimental track** (§7), never on the competition vehicle.

### The motor you are designing around

| Parameter | Aluminium body | PVC body |
|---|---|---|
| Motor diameter | 94 mm | 94 mm |
| Casing length | 383 mm | 313 mm |
| Motor mass | ~3 kg | ~3 kg |
| Max total impulse | 2800 N·s | 2800 N·s |
| Body mass incl. motor | ≤ 15 kg | ≤ 11.5 kg |

**Motor interfaces (fixed):**
- Alignment via centering rings (motor OD → body ID)
- Thrust transfer via a **thrust plate**, attached to body with **6 × M5 screws** (match-drilled), attached to motor with **M12 bolt**

**Open question to resolve via faculty advisor:** the guidelines say motors are "made available by IN-SPACe through the vendor on cost basis" in one place, but "mandatorily procure... at a pre-fixed price" in another. Confirm supplied-vs-purchased, and the price. Queries are only accepted **through the faculty advisor by email, within 15 days of document release**.

---

## 2. THE ACTUAL ENGINEERING PROBLEM

With thrust fixed, the problem becomes: **hit exactly 1000 m ±100 m carrying 1.0 kg ±0.05 kg.**

### First-order trajectory check

| Item | Value |
|---|---|
| Total impulse available | ~2800 N·s |
| Assumed Isp (commercial K-class, ~3 kg motor) | ~100–115 s |
| Launch mass, if 3 kg of 2800 N·s is propellant | ~6 kg (near-optimal) |
| Burnout velocity (burnout mass ≈ 3.5 kg) | ≈ 335 m/s |
| Coast height from energy (mgh = ½mv²) | ≈ 5.7 km |
| Minus gravity loss (~100 m) and drag loss | substantial |

**Conclusion: the motor is almost certainly OVERSIZED for a 1000 m target on a light airframe.** The likely real answer is that a ~4–6 kg vehicle overshoots, and the design job is to *add mass or drag deliberately* to land inside the window.

> ⚠️ **This number is a sanity check only.** Do NOT trust it. The team must build a real mass budget and run proper 6-DOF trajectory simulation in OpenRocket (or equivalent) with a nominal AND worst-case case, which the PDR explicitly requires.

### What actually decides success (in priority order)

1. **Mass budget discipline.** Rule 5.i: lift-off mass must be within **±5%** of the design value. Every gram must be tracked. This is where teams lose.
2. **Descent rate 2–5 m/s (±0.5).** For a ~10 kg vehicle this is a main parachute of roughly **1.6–1.8 m diameter**, and it must survive **30 g opening shock** (rule 7.4). Parachute sizing, packing volume and deployment sequence are *primary* design drivers, not afterthoughts.
3. **Payload separation at exactly 1000 m ±100 m, with NO pyrotechnics** (rule 5.xi — pyro anywhere disqualifies you from even doing prep at the site). Requires servo/mechanical release plus the **mandatory independent COTS backup altimeter** in the redundant chain (rule 5.xv).
4. **Your own launch pad**, adjustable and lockable between **80°–85°** (rule 5.iv), verified by the Jury before launch.
5. **Avionics + ground station.** Detailed but fully achievable, and the highest-leverage place for a small team to win points.

### Vehicle constraints (hard limits)

| Constraint | Limit |
|---|---|
| Overall length (incl. fins, launch config) | < 180 cm |
| Stages | 1 (single stage only) |
| Payload | CAN-7USAT, 1.0 kg ±0.05 kg, enclosed in straight-line config |
| Structural loads | survive **15 g** launch acceleration, **30 g** shock |
| Descent rate | **2–5 m/s** ±0.5 |
| Airframe colour | fluorescent pink, red or orange (mandatory) |
| Markings | team no., email, phone in **English, Hindi, and regional language of launch state** |
| Launch angle | 80°–85°, lockable |
| Battery | LiPo **PROHIBITED**; Li-ion must be metal-cased (18650-type) |
| Recovery | all parts descend tethered together, parachute mandatory |
| Pad comms distance | launch pad ~1 km from viewing gallery — antenna range must cover max altitude |

---

## 3. AVIONICS & GROUND STATION SPEC (highest-leverage subsystem)

### Mandatory telemetry (≥1 Hz, ASCII comma-separated + carriage return)

Exact order per Annexure-2:

```
<TEAM ID>, <TIME STAMPING>, <PACKET COUNT>, <ALTITUDE>, <PRESSURE>, <TEMP>,
<VOLTAGE>, <GNSS TIME>, <GNSS LATITUDE>, <GNSS LONGITUDE>, <GNSS ALTITUDE>,
<GNSS SATS>, <ACCELEROMETER DATA>, <GYRO SPIN RATE>, <FLIGHT SOFTWARE STATE>,
<ANY OPTIONAL DATA>
```

| Field | Resolution |
|---|---|
| Altitude (relative to ground) | 0.1 m |
| Pressure | 1 Pa |
| Temperature | 0.1 °C |
| Voltage (CAN-7USAT bus) | 0.01 V |
| GNSS lat / long | 0.0001° |
| GNSS altitude | 0.1 m |
| GNSS sats | integer |
| Accelerometer | m/s² |
| Gyro spin rate | deg/s |

**File naming:** `Flight_<TEAM_ID>.csv` — handed to Jury on USB **immediately after launch operations**.

### Flight software states (must be telemetered)

`0 BOOT → 1 TEST_MODE → 2 LAUNCH_PAD → 3 ASCENT → 4 PAYLOAD_SEP → 5 DESCENT → 6 AEROBREAK_RELEASE → 7 IMPACT`

Must **recover correct state after processor reset**, and preserve mission clock across reset.

### Radio & ground station

- **XBee/Zigbee Series 1/2/Pro or LoRaWAN** (industrial grade)
- NETID/PANID set to team number, declared at CDR
- **Separate channels** for rocket and CAN-7USAT; interference test demonstrated to Jury
- RF command to switch telemetry ON/OFF; rocket must NOT transmit until commanded
- Onboard **micro-SD logging** as redundant recorder (.csv) for RF link loss
- Near-real-time plotting of every telemetry field, SI units
- Portable ground station: laptop (≥2 h battery), XBee, elevated hand-held antenna
- Ground station must command zero-setting of barometric altitude and accelerometer at pad
- **Independent COTS altimeter** wired to a redundant deployment chain (rule 5.xv) — teams without this are **not permitted to launch**

---

## 4. COMPETITION CYCLE (2026 dates → plan the 2027 equivalent)

| # | Activity | 2026 Window |
|---|---|---|
| 1 | Registration (₹10,000 non-refundable, SSDF) | 24 Mar – 15 Apr 2026 |
| 2 | PDR document submission | 1 May – 15 Jun 2026 |
| 3 | Preliminary Design Review (10 min presentation) | 16 Jun – 15 Jul 2026 |
| 4 | Skill development workshop (only 2 members/team) | 1 Aug – 16 Aug 2026 |
| 5 | CDR submission | 17 Aug – 20 Sep 2026 |
| 6 | Critical Design Review | 21 Sep – 10 Oct 2026 |
| 7 | Post-workshop fee ₹15,000 + FRR & Launch | Oct – Nov 2026 |
| 8 | Post Flight Analysis & results | After competition |

**⏰ Registration deadline was 30 April 2026. Assume ~30 April 2027.** Registration is the gate — miss it and the year is gone.

### Eligibility rules

- Undergraduate students, Engineering/Science, Indian colleges
- **Team size: minimum 5, maximum 8**
- **Only 1 team per college** (affiliated colleges may each send one)
- **1 faculty coordinator/advisor + up to 2 mentors** (mentors may be grad students, faculty, **or alumni**)
- Faculty advisor must **not** make design decisions — oversight only
- **Institutional approval letter required**, on letterhead, signed by **head of institution**, listing every member's name, institute ID, course, branch, year of graduation and role
- Faculty advisor is the **only** channel for official queries
- One launch opportunity only in finals
- Code of ethics: no copying designs or code, no outsourcing development, no restricted/hazardous chemicals

---

## 5. WHAT IS GRADED (design your effort around this)

| Criterion | Weight-bearing content |
|---|---|
| Rocket frame design & innovation | structure, materials, margins |
| Launchpad design & innovation | own pad, 80–85° lockable |
| Flight stability & performance | sims + actual flight vs 1000 m ±100 m |
| Avionics & continuous data collection | telemetry completeness, CSV quality |
| Ignition / Recovery | remote ignition, no-pyro deployment, 2–5 m/s |
| PDR / CDR quality | clarity, rigour, traceability |
| Optional (bonus) | innovative materials, separation mechanisms, **MIL/Indian/ECSS standards adherence**, extra sensors, in-flight video, innovative recovery, onboard experiment, precision landing |

**PDR must contain:** mission requirements trace, allocated system requirements, ops concept, preliminary design, component selection, **theoretical + FEA calculations with margins on joints and fasteners**, realisation/integration process, test criteria, **budget with BOM**, development schedule.

**CDR must contain:** design compliance statement, all deviations justified, **complete BOM with estimate-vs-actual costs**, sponsorship details, test results.

**Make in India components get due weightage.** Plan sourcing accordingly and document it.

---

## 6. RESOURCING REALITY

### Money
| Item | Note |
|---|---|
| Registration | ₹10,000 (non-refundable, SSDF) |
| Post-workshop fee | ₹15,000 |
| Motor | price unknown — confirm via faculty advisor |
| CAN-7USAT payload | **team must procure it themselves** |
| Ground station + avionics | laptop, XBee(s), sensors, GNSS, batteries |
| Fabrication | airframe, fins, nose cone, thrust plate, centring rings, pad |
| Testing | drop tests, ejection tests, structural tests |
| Travel & logistics | launch site, team lodging, hardware transport |
| **Sponsorship** | **actively encouraged and graded** — document every rupee |

**₹2–3L is workable but tight.** Start alumni/CSR sponsorship in Phase 0, not later.

### People — THE PRIMARY RISK
Nobody committing is the project-killer, not money or the range. Mitigations:

1. **Convert the professor's interest into a signed commitment now.** The institutional approval letter needs the head of institution's signature — that is the real gate.
2. **Recruit alumni/grad-student mentors** (explicitly allowed, up to 2). A mentor who outlasts you is worth more than three enthusiastic second-years.
3. **Build a pipeline, not a team.** Recruit 1st/2nd years deliberately. Never let a critical subsystem depend on one person.
4. **Sequence small wins.** Never let the team go months with nothing to show. Motivation follows visible progress.
5. **Document everything.** Institutional memory is the only defence against the June graduation cliff.

### Land within 100 km — what it can and cannot do

| ✅ CAN host | ❌ CANNOT host |
|---|---|
| Low-power (A–D) flights | The official competition launch (IN-SPACe range, IN-SPACe handles clearances) |
| Parachute drop tests | Anything needing IN-SPACe authorisation without going through them |
| Avionics range tests | |
| KNSB static fires (separate track, §7) | |

**Get written landowner permission on paper with a validity date.** The IN-SPACe advisory checklist explicitly requires it, and it is your credibility when approaching any official. For larger motors, expect to inform local district administration.

---

## 7. TWO-TRACK STRATEGY

### TRACK A — Competition vehicle (the priority)

Build around the **fixed 94 mm / 2800 N·s motor**. Deliverables:
- Mass budget accurate to ±5%
- OpenRocket 6-DOF sim, nominal + worst case
- FEA with margins on airframe, fins, thrust plate, joints, fasteners
- No-pyro payload separation at 1000 m + COTS backup altimeter
- Parachute sized for 2–5 m/s with 30 g opening shock margin
- Own launch pad, 80–85° lockable
- Full avionics + ground station to Annexure-2 spec
- BOM, test plan, FMEA, budget, schedule

### TRACK B — Experimental KNSB programme (separate, parallel, disciplined)

**Why it's still worth doing:** a 94 mm K-class KNSB motor is the *same physics* as a 38 mm one — same burn-rate law, same Kn ≈ 150–200 design point, same failure modes (grain cracks, erosive burning). Scaling up teaches you nothing new if you can't first make a small one repeatable.

**Scaling ladder — do not skip steps:**

| Stage | Impulse | Purpose |
|---|---|---|
| 38 mm | 100–200 N·s | Learn casting, grain quality, ignition, test stand |
| 54 mm | 300–600 N·s | Repeatability, nozzle erosion, pressure trace quality |
| 75 mm | 800–1500 N·s | Thermal liner, case design, batch consistency |
| 94 mm | ~2800 N·s | Full K-class capability |

**KNSB formulation:** 65% KNO₃ / 35% sorbitol by mass, melt-cast.
- Realistic delivered Isp for amateur builds: **115–130 s** (well below APCP's 180–200 s)
- Burn rate roughly **4–7 mm/s** at 2–4 MPa; pressure exponent sensitive to formulation and KNO₃ particle size
- **Cracks are the #1 CATO cause** — slow insulated cooling, no voids
- **Moisture is the enemy** — grind fine, dry hard, cast the same day
- Keep **port-to-throat ratio above ~2** throughout the burn or you get erosive burning → pressure spike → CATO
- KNSB's lower flame temperature means phenolic/kraft liner + graphite nozzle is usually adequate
- **One motor proves nothing — you need 3–5 identical motors with overlapping thrust curves**

**Non-negotiable safety discipline:**
- Propellant work **only** at the sanctioned range, never in hostel/lab/workshop
- Remote ignition, always, from behind hard cover
- Non-sparking tools, grounding, ESD control, PPE
- Sub-1 kg batches until you have real test heritage
- **One change at a time** between tests

**Note:** IN-SPACe's advisory only requires their authorisation above **40,960 N·s** (≈ O-class). A 2800 N·s motor is ~15× below that threshold. Between 10,000–40,960 N·s, 30 days' prior intimation + advisory is advised; below 10,000 N·s, inform local administration. Custom propellant may still trigger a **PESO** question from the district administration — plan for the paperwork, don't be surprised by it.

---

## 8. PHASED SCHEDULE

### Phase 0 — Now → Dec 2026: legitimacy + first flights
- [ ] Officially register the club with UVCE
- [ ] Convert professor's interest → **signed faculty advisor commitment**
- [ ] Draft club constitution, roles, handover process
- [ ] Recruit 3–4 committed core members (target 1st/2nd years)
- [ ] Identify 1–2 alumni/grad mentors
- [ ] **Build and fly 3 progressively harder low-power rockets** (a few thousand ₹ total)
- [ ] Obtain **written landowner permission** for the test land
- [ ] Start sponsorship conversations (alumni, CSR)

### Phase 1 — Jan → Mar 2027: capability
- [ ] OpenRocket proficiency; design a 38–54 mm rocket end-to-end
- [ ] Build flight computer + ground station to Annexure-2 spec
- [ ] Parachute sizing + drop tests
- [ ] Structural test rig (15 g / 30 g qualification approach)
- [ ] Build a portfolio — needed for recruiting and sponsors

### Phase 2 — Apr → Aug 2027: design cycle ⏰ REGISTER BY ~30 APRIL
- [ ] Submit registration (₹10,000, IDP portal) + institutional approval letter
- [ ] PDR submission (~1 May – 15 Jun)
- [ ] PDR review presentation (10 min, timed)
- [ ] Attend one-week IN-SPACe workshop (2 members only) + pass mandatory quiz
- [ ] CDR submission (~17 Aug – 20 Sep) — full BOM with estimate-vs-actual

### Phase 3 — Sep → Nov 2027: realisation + launch
- [ ] Fabrication with documented QC
- [ ] Qualification & acceptance testing
- [ ] Flight Readiness Review
- [ ] Launch, recovery, Post Flight Analysis

---

## 9. IMMEDIATE NEXT ACTIONS (this week)

1. **Email the professor** — ask specifically for (a) faculty advisor role, (b) a meeting with the head of institution about the approval letter, (c) a lab/workshop access request. Bring this roadmap.
2. **Priced BOM for 3 low-power rockets + launch kit.** Under ₹10,000. This is your first real deliverable and your recruiting tool.
3. **Draft the club charter** — 1 page: purpose, roles, election/handover, safety policy, meeting cadence.
4. **List 10 UVCE alumni** in aerospace/defence/space/mech to approach as mentors.
5. **Get the land permission letter drafted** for the landowner's signature.
6. **Set up a shared documentation repository** (Git + cloud storage). Every drawing, sim, test log, and decision — dated and versioned. This is what survives you.

---

## 10. KEY REFERENCE DOCUMENTS

- **Competition guidelines:** `model_rocketry_competition_guidelines.pdf` — Doc No. IN-SPACe.MR.Model.CG.01, Issue No.1, dtd 24.03.2026
- **IN-SPACe advisory on sub-orbital launches & model rocketry** (April 2026) — classification thresholds, safety best practices, launch checklist, advisory proforma
- **CAN-7USAT mission requirements:** IN-SPACe.CAN.MR.CG.01, Issue No.01, dtd 24-03-2026
- **IN-SPACe Digital Platform (IDP):** www.inspace.gov.in
- **Queries:** only via faculty advisor → `director-pd@inspace.gov.in` (team change requests use subject: *"Team Change Request IN-SPACe Model Rocketry Competition"*)

---

*Disclaimer: This roadmap interprets the 2026 competition documents as a guide to the 2027 edition. Timelines, motor supply arrangements and fees are subject to change — confirm everything through the faculty advisor once the 2027 documents are released. Trajectory figures quoted are first-order sanity checks only and must be replaced with proper simulation before any design decision.*
