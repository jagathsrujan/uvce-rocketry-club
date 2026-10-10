# Fabrication and Manufacturing

**UVCE Rocketry Club — Aerostructures Guide 4**

| | |
|---|---|
| **Document** | `20_AEROSTRUCTURES/Fabrication_and_Manufacturing.md` |
| **Purpose** | How we actually build things, safely, repeatably, and to documented quality |
| **Companion documents** | `Structures_Design_Guide.md`, `Materials_Database.md`, `Stability_and_Aerodynamics.md` |
| **Safety** | Read `40_SAFETY/Safety_Manual_Master.md` first. This document is not a substitute. |

> **The rule that governs everything below: anything undocumented did not happen.**
> Record dimensions, masses, and deviations as you build. A rocket that flew well but was not
> documented teaches the club nothing after you graduate.

---

## 1. Workshop safety

| Rule | Why |
|---|---|
| **Eye protection at all times** — including hand tools, not just power tools | The most common workshop injury is a small fragment in the eye |
| **No loose clothing, no dangling sleeves, tie back long hair** | Entanglement in a drill press or lathe is how people die in workshops |
| **No synthetic clothing when working with propellant** | Synthetics melt into skin; cotton or FR clothing only |
| **Never work alone on anything energetic** | Two-person rule. If something happens, someone must be able to respond |
| **Dust extraction or a mask when sanding composites, graphite, or balsa** | Composite and graphite dust is a respiratory hazard; graphite dust is also conductive |
| **Clamp your work** | A part that moves during drilling or cutting injures hands |
| **Sharp tools, correctly used** | A dull blade needs more force and slips further |
| **Clean as you go** | Offcuts and swarf cause trips and hide damage |
| **Know where the first aid kit and fire extinguisher are** | Before you start, not after |

---

## 2. Airframe fabrication

### 2.1 Cutting and squaring body tubes

A tube cut at an angle produces a crooked rocket that flies crooked.

| Step | Method |
|---|---|
| 1 | **Wrap a paper strip** around the tube, aligning its edges. The paper edge gives a true perpendicular line. |
| 2 | **Mark** around the paper edge with a fine marker. |
| 3 | **Cut** slightly proud of the line with a fine-tooth saw or hobby knife, rotating the tube as you cut. |
| 4 | **Square** by sanding on a flat surface with the tube held vertical against a square. |
| 5 | **Verify** by standing the tube on a flat surface and checking for rocking; measure the length at four points around the circumference — **they must agree within 0.5 mm.** |
| 6 | **Seal the cut edge** with thin CA to prevent the tube unravelling. |

### 2.2 Fin slotting (through-the-wall)

Through-the-wall fins are **substantially stronger** than surface-mounted fins because the fin root
is bonded to the motor mount tube, not just the airframe wall.

| Step | Method |
|---|---|
| 1 | **Mark fin positions** using a wrap-around guide — a paper strip divided into three equal parts (or four, for four fins) |
| 2 | **Extend the marks** along the full tube length with a flexible straightedge |
| 3 | **Cut the slots** with a fine saw or hobby knife, **slightly narrower than the fin thickness** |
| 4 | **Test-fit** the fin dry. It should require light pressure. If it drops in loose, the slot is too wide |
| 5 | **Do not glue yet** — dry-assemble the whole stack first to verify alignment |

> ⚠️ **Cut slots undersize, then file to fit.** You cannot add material back to an oversized slot.

### 2.3 Fin fabrication and alignment

**Building a fin alignment jig** (this is a half-hour job that pays for itself immediately):

```
                    ┌──────────────────────────┐
                    │   BASE BOARD (plywood)   │
                    └──────────────────────────┘
                       │        │        │
                       │        │        │      ← three (or four) vertical
                       │        │        │        alignment fins, set at exactly
                       ▼        ▼        ▼        120° (or 90°) apart
                    ┌──────────────────────────┐
                    │   Body tube clamped here │
                    └──────────────────────────┘
```

1. Cut a plywood base.
2. Cut three (or four) vertical support fins with a slot to hold the fin at the correct angle.
3. Set them at exactly 120° apart using a protractor, and **glue them in place permanently**.
4. The body tube clamps between them, and each fin slides into its slot perpendicular to the tube.

**Fin airfoiling:** sand a symmetric taper on the leading and trailing edges. A sharp trailing edge
is not desirable — a slight blunt edge (0.5 mm) resists damage better and has negligible drag penalty.

| Edge | Treatment |
|---|---|
| Leading edge | Rounded or tapered, ~30° included angle |
| Trailing edge | Tapered to ~0.5 mm blunt |
| Tip | Rounded slightly to resist chipping |
| Root | **Left square** — this is the bonding surface |

### 2.4 Bonding — surface preparation

**This is where most amateur structures fail.** A perfect epoxy joint on a dirty surface is a bad joint.

| Step | Detail |
|---|---|
| 1. **Sand** | 600 grit or finer. You are creating a mechanical key, not removing material. |
| 2. **Clean** | Acetone or lacquer thinner on a clean lint-free cloth. |
| 3. **Let it evaporate fully** | Acetone must be completely gone — it will weaken the bond if trapped. |
| 4. **Bond within 15 minutes** | A cleaned surface re-contaminates quickly. |
| 5. **Measure epoxy by weight** | Volume mixing is inaccurate. Use a scale. |
| 6. **Mix thoroughly** for a full minute | Incompletely mixed epoxy never fully cures. |
| 7. **Clamp and do not disturb** | Full cure is 24 hours even for "5-minute" epoxy's structural strength. |

### 2.5 Fin fillets

Fillets spread the load at the fin root and dramatically improve joint strength.

- Use **epoxy thickened with microballoons or colloidal silica** to a peanut-butter consistency.
- Apply with a **smooth round tool** (a dowel or the back of a spoon) drawn along the joint.
- **Do one side at a time**, letting each set, to avoid pulling the fin out of alignment.
- A fillet radius of **5–8 mm** is appropriate for a 40 mm airframe.

---

## 3. Nose cone fabrication

| Method | Steps | Best for |
|---|---|---|
| **Turned balsa** | Glue balsa blocks, turn or sand to profile using a template, seal with thin CA, sand smooth | First rockets — cheap and fast |
| **3D printed PETG** | Print with 3+ perimeters, 40%+ infill, orient so layers are not perpendicular to the axis | Repeatability, complex shapes |
| **Fibreglass over foam** | Shape foam plug, lay up glass, dissolve the foam with acetone | Larger cones |

**Nose cone fit:** the shoulder should be a **sliding fit** in the body tube — snug enough not to
rattle, loose enough to release. Test it **before** you commit to the separation design.

> ⚠️ **The competition requires the nose cone or payload bay to separate at apogee.** Design the
> retention and release mechanism **before** finalising the cone geometry — retrofitting a release
> into a finished cone is painful.

---

## 4. Motor mount, thrust plate, and centring rings

### 4.1 The load path

Motor thrust must travel into the airframe **without** relying on glue alone:

```
Motor → thrust plate → airframe (via screws) → fins / body → flight
```

| Component | Function | Notes |
|---|---|---|
| **Motor mount tube** | Holds the motor concentric | Matches motor case OD |
| **Centring rings** | Centre the mount tube in the airframe; transfer radial loads | Plywood, 2 or more |
| **Thrust plate** | Takes the axial thrust from the motor and passes it to the airframe | **The critical part** |
| **Motor retention** | Prevents the motor being ejected | **Positive mechanical retention — not friction fit** |

> 🔴 **The competition explicitly requires positive mechanical retention** (clips, hooks, screw-on
> cap) and states that friction fit is **not acceptable**. Design for this from the start.

### 4.2 Fabrication sequence

1. **Cut centring rings** to the airframe ID, with a hole for the motor mount OD. Sand to a
   sliding fit — not tight.
2. **Dry-assemble** the motor mount, rings, and thrust plate inside the airframe. Verify
   concentricity by measuring the gap at four points.
3. **Bond the forward centring ring** first, let it cure, then the aft ring. This avoids the stack
   shifting while you work.
4. **Drill the thrust plate screw holes** with the assembly clamped, so the holes are match-drilled
   to the airframe. **Do not pre-drill separately** — the holes will not line up.
5. **Fit blind nuts or nyloc nuts** on the inside where you cannot reach later.
6. **Install the thrust plate** and verify the motor sits square: measure the gap between the motor
   case and the airframe at four points around the circumference.

> ⚠️ **A motor mounted at an angle produces thrust misalignment**, which steers the rocket. This is
> a common and easily-avoided cause of a curved flight.

---

## 5. Propellant grain fabrication

> 🔴 **Read `40_SAFETY/Propellant_Handling_SOP.md` before this section.** Casting is the highest-risk
> activity the club performs.

### 5.1 Making the casting tube

The casting tube serves **two** purposes: it is the **non-stick liner**, and it **slightly reduces
the cast grain diameter** so the grain is a loose fit in the motor. It is peeled away after curing.

| Step | Detail |
|---|---|
| 1 | **Tagboard / file-folder paper**, cut to **18 × 18 cm** |
| 2 | Draw a line **8 cm from one edge** |
| 3 | Apply a **thin layer of glue** on one side of that line |
| 4 | **Roll tightly around a mandrel** starting from the glue-free edge, so the finished **inner diameter equals the mandrel diameter** |
| 5 | **Tape the free edge** |
| 6 | **Press the whole surface flat with a pen** to consolidate the layers |
| 7 | **Cure ~30 minutes** before removing from the mandrel |
| 8 | **Grease the inside** — this is what lets you extract the grain later |

> ⚠️ **The finished ID must equal the mandrel diameter.** If the roll is loose, the grain comes out
> oversized and will not fit the motor.

### 5.2 Mould preparation

- **Light grease on the nozzle convergent area** — do not over-grease.
- **Insert the casting tube fully.**
- **A dab of 5-minute epoxy through the bulkhead attachment holes** creates a temporary joint that
  prevents the tube being **hydraulically forced out** during compression. This is a real failure
  mode — do not skip it.
- **Mould base:** the closing pin must protrude **exactly half way up the throat**, so that trapped
  air can escape past it. Drill small vent holes in the base around the pin.
- **Hot glue around the nozzle periphery** to secure the motor to the base.

### 5.3 Plungers and coring rod

| Tool | Specification | Purpose |
|---|---|---|
| **Coring rod** | Diameter = the desired core diameter | The "male mould" for the central core. **Preheat to 150 °C for 15 minutes** before casting — this is what prevents premature freeze-up |
| **Solid plunger** | Plain circular rod, ~¾ of the mould diameter | Presses the slurry down after loading |
| **Hollow plunger** | Just under mould diameter, **with a central hole** | Compresses the slurry and squeezes out air bubbles. **The hole lets it slide over the coring rod — which is why plunging happens AFTER the rod is inserted** |
| **Plungers, chilled** | In a freezer for **≥ 1 hour** | **Propellant does not stick to a frozen surface** |

### 5.4 Casting sequence

1. Prepare the powdered mix with **20–25% excess** for waste.
2. **Preheat** the pot to casting temperature: **KNSB at 130 °C**, held ±5 °C.
3. **Chill the plungers** (≥1 h) and **preheat the coring rod** (150 °C, 15 min).
4. Add powder a few tablespoons at a time, **stirring nearly continuously** until the binder melts.
5. Add the surfactant (**0.1% SLES by mass**) once fully molten. Viscosity drops immediately.
6. Transfer **about half** the slurry to the funnel; coax it in with a craft stick. **If the mould
   blocks, lift it and strike it against the table a few times.** Repeat with the rest.
7. **Press gently with the solid plunger until it bottoms.** ⚠️ **Do not press hard** or propellant
   will flow past the closing pin.
8. **Insert the coring rod all the way down.**
9. **Slide the hollow plunger over the rod** and press for final packing. **Hold the coring rod end
   so it is not forced out.**
10. **Withdraw the plunger most of the way but leave it partly inserted** to keep the rod centred.
11. **Tap the mould firmly against a hard surface repeatedly** — this forces trapped air to the
    surface. This is an important step, and skipping it is how you get voids.

### 5.5 Curing before demoulding

| Propellant | Minimum cool/cure before demoulding |
|---|---|
| KNDX | 30–45 minutes |
| **KNSB** | **24 HOURS** |

> 🔴 **KNSB must cure for 24 hours before demoulding.** Demoulding early distorts the grain when the
> coring rod is extracted.

### 5.6 Demoulding

1. **Hairdryer to soften the hot glue** at the nozzle and base.
2. **Grip the protruding coring rod** in a vise or with locking pliers.
3. **Slide the female mould off.**
4. **Give the grain a quick rotational twist** to break the weak bond to the rod, then pull the rod
   out.
5. **Slit the casting tube lengthwise and peel it off.**

### 5.7 🔴 Grain finishing — the step that gets forgotten

> **After demoulding, the grain has a thin residual grease film on the outer AND core surfaces.**
> This **must be cleaned off completely** with **acetone or lacquer thinner**, or ignition will be
> **delayed or fail**.

Then:

1. **Dry in a desiccator** (sealed container with calcium chloride or silica gel — **pellets must not
   touch the grains**, or they dissolve and stick).
2. **Trim** and **record mass and dimensions** → fill in **FORM-03**.
3. **Apply the thin primer coat** — see `10_PROPULSION/Ignition_System_Design.md` §2.

> ⚠️ **Do not store grains in a desiccator long-term.** Over-drying raises the burn rate above
> normal, which can cause a **CATO**. For long-term storage, use a **zip-lock bag, then a freezer.**

---

## 6. Recovery system fabrication

| Component | Fabrication |
|---|---|
| **Parachute** | Ripstop nylon, 6–8 gores, 6–8 shroud lines of equal length. **Hem the edges** or they will fray. Attach lines with a folded-and-stitched or knotted-and-CA'd method. |
| **Shroud lines** | All **exactly equal length** — unequal lines make the canopy tilt and descend faster |
| **Shock cord** | Kevlar near the heat, with a **loop at each end** for attachment. **Over-specify the strength.** |
| **Attachment points** | Plywood bulkhead bonded and **screwed** to the airframe. **Never rely on glue alone.** |
| **Heat protection** | Nomex blanket or wadding between the deployment charge and the parachute |
| **Nose cone retention** | Positive mechanical retention (friction alone is not acceptable for competition) |

**Descent rate check:** after fabrication, **measure the canopy diameter** and compute the expected
descent rate at the actual recovery mass. It must land in the **2–5 m/s** band. Then **verify by
drop test.**

---

## 7. Finishing and marking

### 7.1 Painting

| Step | Detail |
|---|---|
| 1 | **Sand** the airframe lightly (400 grit) for adhesion |
| 2 | **Prime** — a light coat, not a heavy one |
| 3 | **Sand** the primer smooth |
| 4 | **Topcoat** in the required colour |
| 5 | **Do not paint** inside the motor mount or any mating surface |

> 🔴 **The competition requires fluorescent pink, red, or orange** (rule 5.xiii) for visibility
> during recovery.

### 7.2 Mandatory markings

The competition requires **team number, email address and phone number in English, Hindi, and the
regional language of the launch state** (rule 3.2). For Karnataka, that means **Kannada**.

Apply the markings:
- On the **outside of the airframe** where they will survive the flight
- **Durably** — printed label under clear tape, or painted
- On **every separable part**, including the payload, so a part found in a field can be returned

> ⚠️ **Verify the phone number is reachable** and that whoever answers knows what the object is. A
> farmer finding a rocket with an unanswered number will call the police.

---

## 8. Quality control at each stage

| Stage | Check | Pass criterion | Record |
|---|---|---|---|
| **Materials on receipt** | Dimensions, grade, visual | Per `Materials_Database.md` §11 | BOM workbook |
| **Tube cutting** | Squareness | Length agrees within 0.5 mm at 4 points | Build log |
| **Fin slots** | Fit | Light pressure to insert, no play | Build log |
| **Fin alignment** | Angular position | Within **±1°** of nominal | Photo + build log |
| **Bonding** | Fillet quality | No voids, no gaps, full cure | Photo |
| **Motor mount** | Concentricity and squareness | Gap varies < 0.5 mm at 4 points | Build log |
| **Thrust plate** | Fastener engagement | All screws engage fully; nyloc nuts fitted | Build log |
| **Grain density** | Density ratio | **≥ 0.95 accept; < 0.90 discard** | **FORM-03** |
| **Grain tap test** | Sound consistency | Identical to batch-mates | **FORM-03** |
| **Grease removal** | Visual + feel | No slickness; dry to the touch | **FORM-03** |
| **Primer** | Coverage and thickness | Thin, even, complete | **FORM-03** |
| **Recovery** | Deployment test | 10+ bench actuations, no jams | Test log |
| **Parachute** | Descent rate | **2–5 m/s** measured | Test log |
| **Final mass** | Mass and CG | Within **±5%** of design | Mass budget workbook |
| **Static margin** | CG vs CP | **1–2 calibers** | Mass budget workbook |
| **Markings** | Required text present | Team no., email, phone in EN/HI/KN | Photo |

> 🔴 **The final mass and CG check is a go/no-go.** The competition requires lift-off mass within
> **±5%** of the design value. If it fails, add or remove mass deliberately and **re-verify
> stability** — do not fly a rocket whose CG has moved aft without rechecking the static margin.

---

## 9. Fabrication sequence for the first rocket

Realistically **2–3 weeks of part-time work** for a small team.

| Week | Task | Deliverable | Gate |
|---|---|---|---|
| **1** | Cut tubes, make fin alignment jig, cut and shape fins | Tube squared, fins profiled | Squareness within 0.5 mm |
| **1–2** | Dry-assemble; cut slots; fit everything | Full dry stack | Fins fit, motor mount concentric |
| **2** | Bond fins and fillets (one side at a time) | Fins bonded and filleted | Alignment within ±1° |
| **2** | Bond centring rings and thrust plate | Motor mount installed | Squareness verified |
| **2–3** | Nose cone fabrication and fit | Cone fits and releases | Sliding fit, release tested |
| **3** | Recovery system: parachute, shock cord, attachments | Complete recovery assembly | **10 bench deployment tests pass** |
| **3** | Paint and mark | Finished airframe | Fluorescent colour, all markings present |
| **3** | **Final mass, CG, and static margin check** | Completed mass budget | **±5% mass, 1–2 calibers stability** |
| **3** | Parachute drop test | Measured descent rate | **2–5 m/s** |

**Do not proceed past any gate with a failed check.** Fix it and re-verify. A rocket that fails a
gate on the bench will fail harder in the air.

---

## 10. Common fabrication mistakes

| Mistake | Consequence | Prevention |
|---|---|---|
| Tube cut out of square | Curved flight | Paper-wrap method, verify at 4 points |
| Fins not aligned | Spiral flight, loss of altitude | Use an alignment jig — always |
| Dirty bonding surface | Joint fails under load | Sand, clean with acetone, bond within 15 min |
| Epoxy mixed by volume | Inconsistent, weak joints | Measure by weight |
| Not enough epoxy mixing | Never fully cures | Mix a full minute |
| Motor mounted at an angle | Thrust misalignment, curved flight | Measure the gap at 4 points |
| Friction-fit motor retention | **Motor ejected in flight** | **Positive mechanical retention** |
| Grain grease not removed | Delayed or failed ignition | Acetone / lacquer thinner — mandatory |
| Heavy primer coat | **Delayed ignition** | Thin coat only |
| Grain demoulded too early | Distorted core, cracks | **24 hours for KNSB** |
| Parachute too small | Descent rate above 5 m/s, damage | Size for 3.5 m/s, then drop-test |
| Shock cord not heat-protected | Melts, parachute separates | Kevlar + Nomex |
| No markings | Lost rocket, unreturned | Mark every part |
| Flying without final mass/CG check | **Instability** | Always complete the mass budget |

---

## 11. Tools you actually need

**Minimum viable set for the first rocket (≈ ₹6,000):**

| Tool | Use | Approx ₹ |
|---|---|---|
| Hobby knife + spare blades | Cutting tubes, paper | 200 |
| Fine-tooth saw / razor saw | Cutting tube and fins | 400 |
| Steel rule + square | Measuring, squaring | 300 |
| Digital calipers (150 mm) | **Essential** — dimensions and QC | 900 |
| Digital scale (0.01 g) | Epoxy mixing, grain mass, propellant | 1,500 |
| Sanding block + assorted grits | Fillets, surface prep | 300 |
| Clamps (4–6, various sizes) | Bonding | 700 |
| Drill + bits (1.5–6 mm) | Thrust plate, holes | 1,200 |
| Soldering iron | Electronics, igniters | 900 |
| Safety glasses + mask | **Non-negotiable** | 500 |

**Later additions:** bench drill press, rotary tool, 3D printer, vacuum pump, lathe access.

---

## 12. Sources

- `80_REFERENCE/nakka_source_text/casting1.txt` — casting tube fabrication, mould preparation,
  plunger and coring rod practice, the exact casting sequence, cure times, demoulding, and the
  mandatory grease removal
- `80_REFERENCE/nakka_source_text/inert.txt` — inert grain practice
- `Technical_Reference_Nakka.md` §1.5–1.8 (casting, curing, quality control) and §1.13 (priming)
- IN-SPACe Model Rocketry India Student Competition 2026 — Mission Requirements and Competition
  Guidelines (Doc No. IN-SPACe.MR.Model.CG.01, Issue No.1, dtd 24.03.2026). Rules 3.1, 3.2, 5.i,
  5.iv, 5.viii, 5.xiii.
- `40_SAFETY/Propellant_Handling_SOP.md` and `40_SAFETY/forms/FORM-03_Grain_QC_Record.md`
