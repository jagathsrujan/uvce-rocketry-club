# UVCE Rocketry Club — Structures Design Guide

**Document:** 20_AEROSTRUCTURES/Structures_Design_Guide.md
**Applies to:** UVCE-SR-1 "Kaveri" (40 mm airframe, 250–300 g dry) and follow-on vehicles
**Companion documents:** `Stability_and_Aerodynamics.md` (loads origin), `Materials_Database.md` (properties), `Fabrication_and_Manufacturing.md` (how to build it)

> **Status:** Working design document. Every number here is either derived in-line or traceable to a
> named source. Numbers marked **[VERIFY BY TEST]** must be confirmed on a physical sample before
> flight hardware is released. Nothing in this document authorises a flight — see the club's launch
> checklist and the IN-SPACe advisory.

---

## 0. HOW TO USE THIS DOCUMENT

Structure design has exactly four steps, in this order. Skipping step 1 is where student teams lose vehicles.

1. **Define the load cases** (§2) — what forces, in what combination, with what safety factor.
2. **Size for strength** (§4–§9) — can the part carry the load without yielding/rupturing?
3. **Size for stability** (§5) — can the part carry the load *without buckling or deflecting* into a
   shape that changes the aerodynamics? Thin tubes fail here, not in strength.
4. **Size the joints** (§9–§11) — 80 % of amateur structural failures are bond or fastener failures,
   not material failures. The material is usually fine; the glue line is not.

---

## 1. REFERENCE VEHICLE — UVCE-SR-1 "Kaveri"

All worked examples in this document use this vehicle. It is deliberately the smallest useful
airframe: big enough to teach every real effect, small enough to build in a college workshop and fly
from a college ground.

### 1.1 Geometry

| Parameter | Symbol | Value | Note |
|---|---|---|---|
| Body tube outside diameter | $D_o$ | 40.0 mm | 1 body caliber |
| Body tube inside diameter | $D_i$ | 37.6 mm | |
| Wall thickness | $t$ | 1.2 mm | convolute kraft paper |
| Body tube length | $L_{bt}$ | 580 mm | station 120 → 700 mm |
| Nose cone | — | tangent ogive, 120 mm | 3.0 calibers, station 0 → 120 mm |
| Overall length | $L$ | 700 mm | 17.5 calibers |
| Fin count | $N$ | 3 | |
| Fin root chord | $C_r$ | 120 mm | station 580 → 700 mm |
| Fin tip chord | $C_t$ | 60 mm | |
| Fin exposed semi-span | $s$ | 40 mm | = 1.0 caliber |
| Fin leading-edge sweep | $X_R$ | 45 mm | root LE → tip LE, axial |
| Fin thickness | $t_f$ | 3.0 mm | G10/FR-4 fibreglass |
| Motor mount tube | MMT | 24.5 mm ID × 95 mm | 24 mm commercial motors |
| Centring rings | — | 2 × 3 mm plywood | stations 612 and 688 mm |
| Recovery compartment | — | ~300 mm | chute + Nomex + shock cord |

### 1.2 Mass budget

Tracked to the gram. Competition rules require the lift-off mass to be within **±5 %** of the design
value, so this table is a flight-critical document, not bookkeeping.

| Item | Mass (g) | Station of item CG (mm from nose tip) |
|---|---|---|
| Nose cone (PLA printed, 2 perimeters / 20 % infill) | 30.0 | 50 |
| Body tube (580 mm, 1.2 mm kraft) | 81.0 | 410 |
| Fins (3 × G10, 6.7 g each) | 20.0 | 647 |
| Fin fillets (epoxy + silica) | 6.0 | 640 |
| Motor mount tube | 6.0 | 652 |
| Centring rings (2 × 3 mm ply) | 6.0 | 655 (average) |
| Thrust ring | 4.0 | 698 |
| Coupler (150 mm, station 330–480) | 8.0 | 405 |
| Bulkhead (3 mm ply) | 4.0 | 300 |
| Launch lug (6 × 60 mm) | 3.0 | 230 |
| Parachute (450 mm ripstop nylon) | 18.0 | 200 |
| Shock cord (2 m Kevlar + 2 m elastic) | 14.0 | 250 |
| Nomex/silica heat shield | 12.0 | 220 |
| Avionics (altimeter + Li-ion cell + bay) | 25.0 | 300 |
| Paint and sealer | 15.0 | 400 |
| Hardware (eye bolt, shear pin, screws) | 8.0 | 300 |
| **Weighed subtotal** | **260.0** | — |
| **Design dry mass (with 15 g growth margin)** | **275.0** | **CG = 353 mm** |

Motor masses (commercial, representative — **verify against the vendor's certified data sheet**):

| Motor | Class | Total impulse (N·s) | Burn time (s) | Propellant (g) | Loaded mass (g) | Launch mass (g) | Launch CG (mm) |
|---|---|---|---|---|---|---|---|
| Estes D12-5 | D | 16.8 | 1.6 | 21 | 43 | 318 | 397 |
| Estes E12-6 | E | 27.7 | 2.4 | 36 | 66 | 341 | 414 |
| 24 mm composite F | F | 50 | 1.5 | 30 | 88 | 363 | 428 |

### 1.3 Derived section properties (40 mm × 1.2 mm tube)

$$A = \frac{\pi}{4}\left(D_o^2 - D_i^2\right) = 1.463\times10^{-4}\ \text{m}^2 = 146.3\ \text{mm}^2$$

$$I = \frac{\pi}{64}\left(D_o^4 - D_i^4\right) = 2.755\times10^{-8}\ \text{m}^4$$

$$Z = \frac{I}{c} = \frac{I}{D_o/2} = 1.378\times10^{-6}\ \text{m}^3 = 1378\ \text{mm}^3 \quad \text{(bending section modulus)}$$

$$r_g = \sqrt{I/A} = 13.72\ \text{mm} \quad \text{(radius of gyration)}$$

$$J = \frac{\pi}{32}\left(D_o^4 - D_i^4\right) = 5.510\times10^{-8}\ \text{m}^4 \quad \text{(polar moment, for torsion)}$$

---

## 2. AIRFRAME LOADS

### 2.1 Thrust

Thrust is applied at the motor's forward closure and reacted by the **thrust plate / thrust ring**,
which pushes the motor mount tube (MMT) forward; the MMT drags the centring rings, which drag the
body tube, which accelerates everything forward of them.

**Never design to average thrust.** Use the peak thrust from the manufacturer's thrust curve. Peak/average
ratios of 1.6–2.2 are normal for black-powder motors (the initial spike) and 1.3–1.8 for composite
motors.

| Motor | Average thrust (N) | Peak thrust (N) | Peak/average |
|---|---|---|---|
| D12 | 10.5 | ~25 | 2.4 |
| E12 | 11.5 | ~33 | 2.9 |
| 24 mm F composite | 33 | ~60 | 1.8 |
| 29 mm G composite (next step) | 60 | ~110 | 1.8 |

**Design thrust (this vehicle):** $T_d = 90\ \text{N}$ — covers any 24 mm motor with margin.

The thrust load creates an internal **axial compression** in everything forward of the thrust plate:

$$N(x) = a_{\text{axial}} \sum_{i:\, x_i < x} m_i$$

where the sum is over all masses forward of station $x$. Note the load is **highest at the thrust
plate** and falls to zero at the nose tip.

### 2.2 Drag

$$D = \tfrac{1}{2}\rho v^2 C_d A$$

With $\rho = 1.10\ \text{kg/m}^3$ (Bengaluru, ~900 m elevation, 25 °C), $C_d = 0.50$,
$A = 1.2566\times10^{-3}\ \text{m}^2$:

| Motor | $v_{max}$ (m/s) | $q_{max} = \frac{1}{2}\rho v^2$ (Pa) | Drag at $v_{max}$ (N) | Drag/weight |
|---|---|---|---|---|
| D12 | 38 | 794 | 0.50 | 0.16 |
| E12 | 60 | 1 967 | 1.24 | 0.37 |
| 24 mm F | 123 | 8 321 | 5.23 | 1.47 |

Drag is a **compressive** load on the nose and a **tensile** load in the tube between the nose and the
fins. At F-class speeds the drag force exceeds the vehicle's weight — this is why composite-motor
airframes must be stiffer, not just stronger.

*Note:* the motor thrust also reacts against the nose/drag; the *net* axial load during coast is
tension (nose pulled one way, fins the other). For a 363 g vehicle at 5.2 N of drag this is a
negligible 0.04 MPa, but it becomes significant above ~100 mm diameter.

### 2.3 Bending from wind and angle of attack

This is the load case that actually breaks model-rocket airframes. When the vehicle flies at angle of
attack $\alpha$ to the relative wind, the fins generate a normal force at the centre of pressure while
the vehicle's inertia reacts at the centre of gravity. The offset between CP and CG is the moment arm.

$$N_{\text{aero}} = C_{N\alpha}\,\alpha\,q\,A_{ref}$$

$$M_{\text{bend}} \approx N_{\text{aero}}\left(x_{CP} - x_{CG}\right)$$

with $C_{N\alpha} = 9.59\ \text{rad}^{-1}$ for this vehicle (derived in `Stability_and_Aerodynamics.md` §4),
and moment taken about the CG station.

| Case | $\alpha$ | $q$ (Pa) | $N$ (N) | $x_{CP}-x_{CG}$ (mm) | $M$ (N·m) | $\sigma = M/Z$ (MPa) |
|---|---|---|---|---|---|---|
| D12 launch, 5° gust | 5° | 794 | 0.84 | 126 | 0.106 | 0.08 |
| E12 at max-q, 10° | 10° | 1 967 | 4.14 | 110 | 0.455 | 0.33 |
| F at max-q, 10° | 10° | 8 321 | 17.5 | 95 | 1.67 | **1.21** |
| F at max-q, 20° (extreme) | 20° | 8 321 | 35.0 | 95 | 3.34 | 2.42 |

**Guidance:** design to **10° at max-q** for a first vehicle. 20° is a survival case, not a design
case — if the vehicle reaches 20° AoA at F-class speed the fins will flutter anyway.

Add the axial component from §2.1 to get the total:

$$\sigma_{\text{total}} = \frac{N_{\text{axial}}}{A} + \frac{M}{Z}$$

For LC-5 (F motor, 10°): $\sigma = 0.13 + 1.21 = 1.34\ \text{MPa}$.

### 2.4 Landing shock

Descent at $v_d$ (competition window 2–5 m/s), stopping distance $s$ determined by the soil and by
how much structure you are willing to sacrifice:

$$a_{\text{impact}} = \frac{v_d^2}{2s}, \qquad n_g = \frac{a_{\text{impact}}}{g}$$

| $v_d$ (m/s) | $s$ = 5 mm (hard ground, rigid nose) | $s$ = 25 mm (soil, crushable nose) | $s$ = 50 mm (soft soil) |
|---|---|---|---|
| 2 | 40 g | 8 g | 4 g |
| 3 | 92 g | **18 g** | 9 g |
| 5 | 255 g | 51 g | 25 g |

**Read this table carefully.** A 5 m/s landing onto something rigid gives 255 g. No 30 g requirement
can cover that. The 30 g IN-SPACe figure is a **deployment/handling shock** requirement; the landing
case must be managed by design:

- Target the **low end** of the descent window (2.5–3.5 m/s), not the top.
- Design the nose tip as a **sacrificial crush zone** (a hollow printed tip, or a cardboard crush
  tube inside the nose). 25 mm of crush stroke is achievable and turns 92 g into 18 g.
- Land on soil, never on rock or concrete, and never on the launch rail base.

### 2.5 Motor retention loads

Three separate loads, in increasing order of severity:

**(a) Thrust reaction.** The motor pushes aft on its retainer with the full thrust:

$$F_{\text{ret}} = T_{peak} = 60\ \text{N (24 mm F)}$$

**(b) Ejection charge — the real driver.** When the ejection charge fires, the recovery compartment
pressurises and the pressure acts on the motor's forward closure, pushing the motor *aft out of the
vehicle*. Free volume for a 40 mm airframe with 300 mm of recovery compartment, packed to ~50 %:

$$V_{\text{free}} \approx 0.5 \times \frac{\pi}{4}(0.0376)^2 \times 0.30 = 1.66\times10^{-4}\ \text{m}^3$$

For 0.6 g of black powder (≈ 0.0067 mol of gas at ~2000 K):

$$P = \frac{nRT}{V} = \frac{0.0067 \times 8.314 \times 2000}{1.66\times10^{-4}} \approx 6.7\times10^{5}\ \text{Pa} \approx 0.67\ \text{MPa}$$

$$F_{\text{eject}} = P \cdot \frac{\pi}{4}D_{motor}^2 = 0.67\times10^{6} \times 4.52\times10^{-4} = 303\ \text{N}$$

> ⚠️ **The ejection charge is the largest force your airframe will ever see** — 5× the motor thrust,
> and 5.7× the 15 g inertial load. It is also the load case most often ignored. A real, packed
> recovery compartment typically reaches **0.3–0.7 MPa**; the free volume matters enormously, so a
> loosely packed chute is a structural decision, not a convenience.

**(c) Ejection charge hoop stress on the tube.** The same pressure inflates the body tube:

$$\sigma_{hoop} = \frac{P r}{t} = \frac{P \times 18.8}{1.2} = 15.7\,P \ \text{(MPa, } P \text{ in MPa)}$$

| Ejection pressure | Hoop stress (MPa) | Kraft paper tube verdict |
|---|---|---|
| 0.20 MPa (loose pack, small charge) | 3.1 | OK |
| 0.40 MPa (typical) | 6.3 | **MARGINAL** |
| 0.67 MPa (tight pack, big charge) | 10.5 | FAIL — tube splits |

Kraft paper tubes typically burst at 4–10 MPa hoop stress **[VERIFY BY TEST]**. **This is why model
rockets blow up on ejection.** Mitigations, in order of effectiveness:
1. Pack the recovery loosely — target ≥ 60 % free volume.
2. Use the smallest ejection charge that reliably deploys (reloadable motors let you choose).
3. Fit a **coupler** across the recovery compartment (doubles the wall in the highest-stress region).
4. Drill a **static port** (2 × 2 mm) in the recovery section if you also use electronic deployment —
   it equalises slowly during flight but relieves the ground-level pressure differential.
5. Never fly a *sealed* airframe.

### 2.6 Deployment shock (the 30 g case)

When the parachute inflates, the vehicle decelerates. At the moment of line stretch the canopy is
still closed; the peak force occurs as it snaps open:

$$F_{\text{snatch}} \approx C_d \cdot \tfrac{1}{2}\rho v_{\text{deploy}}^2 \cdot S_{\text{chute}} \cdot C_x$$

where $C_x \approx 1.5\text{–}2.5$ is the opening-shock factor. For a 450 mm chute ($S = 0.159\ \text{m}^2$,
$C_d = 0.80$) deploying at 15 m/s:

$$F_{\text{snatch}} = 0.80 \times \tfrac{1}{2}(1.10)(15^2)(0.159) \times 2.0 = 31.5\ \text{N}$$

The **IN-SPACe compliance case** is the equivalent static load:

$$F_{30g} = 30\,g \cdot m = 30 \times 9.81 \times m$$

| Mass being decelerated | $F_{30g}$ |
|---|---|
| Whole vehicle, 363 g | 107 N |
| Body + motor, 300 g | 88 N |
| Nose + chute, 60 g | 18 N |

Design every element of the recovery load path — eye bolt, bulkhead, bulkhead bond, coupler, shock
cord, cord attachment, nose shoulder, shear pins — for **107 N** with a factor of safety of 2.0
(§3.4).

### 2.7 Ground handling and transport

The most common *actual* cause of damage. Design to:

| Case | Load |
|---|---|
| Tip-over onto the pad (0.7 m fall, nose-first) | ~50 g on the nose shoulder |
| Crushed in a backpack | 200 N lateral on the tube |
| Fin knocked against a table edge | 50 N at the fin tip |
| Hot car interior (India, April) | 65–75 °C — see §13, adhesives and PLA |

**A fin knocked against a table edge is a 20–50 N tip load**, which is 3–10× any aerodynamic fin load.
This is why §6.3 checks the fin bond against impact, not against aerodynamics.

---

## 3. LOAD CASES AND SAFETY FACTORS

### 3.1 The IN-SPACe requirements, restated exactly

The governing competition document requires the vehicle to survive:

| Requirement | Value | Applies to |
|---|---|---|
| Launch acceleration | **15 g** (147 m/s²) | Airframe, motor mount, thrust structure, payload attachment |
| Shock | **30 g** (294 m/s²) | Recovery system, avionics mounting, all joints |
| Descent rate | 2–5 m/s ± 0.5 | Recovery system sizing |
| Launch angle | 80°–85°, lockable | Pad (not airframe) |
| Airframe colour | fluorescent pink / red / orange | Finish |

**Note the physics:** the 15 g figure is an *envelope*, not a measurement. Actual peak acceleration
in this vehicle is 2.5 g (D12) to 8.5 g (24 mm F). Designing to 15 g therefore covers a motor upgrade
without redesign — which is exactly why the rule is written that way. Do not "optimise" the structure
down to the measured flight acceleration; you will fail the review and you will break the vehicle on
an off-nominal flight.

### 3.2 Deriving an equivalent static load case from a g requirement

A g requirement is a **body-inertial** load, not a point load. Convert it like this:

1. **Identify the mass being accelerated**, $m$.
2. **Multiply by the g factor**: $F = n\,g\,m$ where $n$ = 15 or 30.
3. **Apply the resultant at the CG of that mass**, pointing *opposite* to the acceleration (i.e. aft
   during launch, forward during a chute opening).
4. **React it at the physical attachment.** For launch: all inertial loads sum to $15\,g\,m_{total}$,
   reacted by the thrust plate. For recovery: the load is reacted where the shock cord attaches.
5. **Take internal loads by cutting the structure** at the station of interest:
   $N(x) = n\,g\,\sum_{x_i < x} m_i$.
6. **Apply the factor of safety** (§3.4).

This is called d'Alembert's principle — the inertial load is treated as a static body force. It is
exact for a quasi-static case (the load's duration is much longer than the structure's natural
period). For the 30 g *shock* case it is an approximation, valid because the vehicle's first axial
mode (~800–1500 Hz for a 700 mm paper tube) is well above the 20–100 Hz content of a canopy opening
transient. For short, sharp shocks (a hard landing) the static equivalent is *unconservative* and a
crush zone is the correct answer (§2.4).

### 3.3 Design load cases

| ID | Case | Load | Factor | Governs |
|---|---|---|---|---|
| LC-1 | Ground handling | 200 N lateral, 50 g nose-first tip-over | 1.5 | tube wall, nose shoulder, fin bonds |
| LC-2 | Thrust | $T_{peak}$ = 60 N (24 mm F) | 1.5 | thrust plate, MMT, MMT bonds, centring rings |
| LC-3 | Launch inertia | 15 g axial, 363 g → **53.4 N** | 1.5 | body tube (compression), avionics mount, nose shoulder |
| LC-4 | Rail exit / low-speed gust | 5° AoA at $q$ = 800 Pa | 1.5 | fins, fin bonds |
| LC-5 | Max-q bending | **10° AoA at $q$ = 8 321 Pa → $M$ = 1.67 N·m** | 1.5 | body tube (bending), coupler, fin root |
| LC-6 | Deployment shock | **30 g → 107 N** | 2.0 | shock cord, eye bolt, bulkhead, coupler, nose shoulder, shear pins |
| LC-7 | Landing | 3 m/s onto soil with a 25 mm crush stroke → 18 g | 2.0 | nose tip, fin tips, tube |
| LC-8 | Ejection charge | **0.4 MPa → 181 N aft on the motor, 6.3 MPa hoop** | 1.5 | motor retention, MMT bond, tube hoop |
| LC-9 | Thermal | 70 °C soak (pad + car) | — | adhesives, PLA parts, PVC (never) |

**Combination rule.** Combine LC-3 + LC-5 (launch inertia with max-q bending happens in the same
instant). Do not combine LC-6 with LC-5 — recovery deployment occurs after burnout, in a different
flight phase. Combining everything is a common student error that leads to absurd over-design.

### 3.4 Factors of safety

| Structure | FoS | Basis |
|---|---|---|
| Aluminium/steel, yield | 1.25–1.5 | well-characterised material, ductile |
| Aluminium/steel, ultimate | 1.5 | |
| Composite (fibreglass, carbon) | 1.5–2.0 | hand layup scatter, void content |
| Bonded joint (epoxy) | **3.0** | surface-prep variability dominates |
| Paper / phenolic structure | **3.0–4.0** | moisture, ply overlap, big scatter |
| Recovery system | 2.0 on the 30 g case | |
| Fasteners, shear/bearing | 1.5 | |
| 3D-printed parts | 3.0 in-plane, **4.0 in Z** | interlayer strength is 50–70 % of bulk |
| Pressure vessel (Track B only) | burst ≥ 2.5 × MEOP, min 1.5 × | see `Materials_Database.md` §6 |

### 3.5 Margin of safety

$$\text{MS} = \frac{\sigma_{\text{allow}}}{\text{FoS} \times \sigma_{\text{applied}}} - 1$$

**MS ≥ 0 is required. MS ≥ 0.5 is the club standard for flight hardware.** A structure with
MS = +0.05 is a structure that fails on the third flight, in slightly hotter weather, with slightly
more glue. Report every margin in the PDR/CDR — reviewers look for exactly this table.

### 3.6 Structural margins summary — UVCE-SR-1

| # | Item | Load case | Applied | Allowable | FoS | MS | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | Body tube, axial compression | LC-3 | 0.36 MPa | 2.0 MPa | 3.0 | +0.85 | OK |
| 2 | Body tube, bending (1.2 mm wall) | LC-5 | 1.21 MPa | 3.0 MPa | 3.0 | **−0.17** | **ACTION** |
| 3 | Body tube, bending *with coupler* | LC-5 | 0.61 MPa | 3.0 MPa | 3.0 | +0.64 | OK |
| 4 | Body tube, Euler column | LC-3 | 53 N | 2 021 N | 1.5 | +24.4 | Not critical |
| 5 | Body tube, hoop (ejection) | LC-8 | 6.3 MPa | 8.0 MPa | 1.5 | **−0.15** | **ACTION** |
| 6 | Body tube, hoop *with coupler* | LC-8 | 3.1 MPa | 8.0 MPa | 1.5 | +0.72 | OK |
| 7 | Fin root bond, landing impact | LC-7 | 7.9 N·m | 65 N·m | 3.0 | +1.74 | OK |
| 8 | Fin root bond, aerodynamics | LC-5 | 0.10 N·m | 65 N·m | 3.0 | +216 | Not critical |
| 9 | Thrust plate bearing on ring | LC-2 | 0.22 MPa | 8 MPa | 1.5 | +23 | Not critical |
| 10 | MMT-to-centring-ring bond shear | LC-8 | 0.38 MPa | 8 MPa | 3.0 | +6.0 | OK |
| 11 | Screw bearing in paper tube (M3) | LC-2 | 4.2 MPa | 10 MPa | 1.5 | +0.59 | OK, use a washer |
| 12 | Shock cord anchor / bulkhead | LC-6 | 0.07 MPa | 8 MPa | 3.0 | +37 | Not critical |
| 13 | Shear pin (1 × 2 mm nylon) | LC-8 | 126 N | 181 N | 1.0 | +0.44 | OK — 1 pin only |
| 14 | Nose shoulder friction retention | LC-8 | 181 N | 250 N | 1.0 | +0.38 | OK, verify by pull test |

**Two actions fall out of this table**, and both are classic: (2) the paper tube is marginal in
bending at F-class dynamic pressure — fix with the coupler already in the mass budget, or stay at
D/E; (5) the tube hoop stress during ejection is marginal — fix by packing loosely and using a
minimal charge. Neither is a strength *material* problem; both are stiffness/pressure problems.
That is the normal outcome of amateur structural analysis.

---

## 4. BODY TUBE DESIGN

### 4.1 Material comparison

Full property data and Indian sourcing: `Materials_Database.md` §1. This table is the design-time
summary. Costs are indicative Bengaluru retail, 2025–26 — get quotes.

| Material | Density (g/cm³) | Tensile strength (MPa) | Modulus $E$ (GPa) | Cost (₹/m, 40 mm OD) | Workability | Failure mode | Beginner rating |
|---|---|---|---|---|---|---|---|
| **Kraft paper tube** (convolute) | 0.90–1.20 | 15–30 axial, 8–15 hoop | 1.5–3.0 | 60–120 | Trivial: cut, sand, glue | **Splits along a ply seam; delaminates; crushes** | ★★★★★ |
| **Phenolic tube** (paper-reinforced) | 1.35–1.45 | 60–100 axial | 6–10 | 350–700 | Cuts with a fine saw; dusty | Splits, then delaminates | ★★★★ |
| **Fibreglass tube** (filament-wound epoxy) | 1.80–2.00 | 250–350 | 18–25 | 900–1 800 | Needs an abrasive wheel; dust hazard | Shatters into stiff shards | ★★★ |
| **Carbon fibre tube** (roll-wrapped) | 1.50–1.60 | 600–1 200 (fibre dir.) | 60–120 | 1 500–3 500 | Abrasive wheel only; conductive dust | Shatters; splinters are conductive | ★★ |
| **Aluminium 6061-T6** | 2.70 | 276 yield / 310 UTS | 68.9 | 400–600 | Excellent: turn, drill, tap | Yields, then folds — ductile, visible warning | ★★ |
| **Aluminium 6082-T6** | 2.70 | 250–260 yield | 70 | 350–550 | Excellent (the standard Indian extrusion alloy, "HE30") | Yields, ductile | ★★ |
| **Mild steel** (EN3B / IS 2062) | 7.85 | 370 yield / 440 UTS | 200 | 250–450 | Easy but heavy | Yields, ductile | ★ |
| **PVC pipe** (uPVC plumbing) | 1.38–1.45 | 45–55 | 2.7–3.3 | 50–110 | Trivial to cut | **BRITTLE — SHATTERS INTO SHRAPNEL** | ✗ **PROHIBITED** |

### 4.2 Why PVC is banned and paper is preferred — the failure-mode argument

This is the single most important materials decision in the document, and it is **not** about
strength. PVC is stronger than kraft paper by every number in the table above. It is banned because
of *how it fails*.

**PVC (uPVC) — brittle fracture.**
- Fracture toughness $K_{Ic} \approx 2\text{–}3\ \text{MPa}\sqrt{\text{m}}$, versus 20–30 for
  aluminium and ~0.7 for glass. Low toughness means **no plastic deformation before fracture**.
- uPVC has no yield plateau. It goes from elastic to broken with no visible warning: no bulge, no
  necking, no audible creak. You cannot inspect a PVC case and know it is about to fail.
- Internal pressure or impact releases stored elastic energy in ~10⁻⁵ s, and the wall fragments into
  **sharp, high-velocity shards**. A 40 mm PVC tube at 0.5 MPa contains ≈ 3 J of stored energy — enough
  to drive fragments several metres. Fragment velocity scales with $\sqrt{2E/m_{frag}}$; small, light
  fragments go fast.
- It embrittles further with UV exposure (a season in the sun) and at low temperature.
- It softens at 60–80 °C (Tg ≈ 80 °C), i.e. a black PVC case on a launch pad in an Indian summer
  reaches its glass transition. Geometry changes; grain support changes; the motor's internal ballistics
  change.
- Nothing bonds reliably to PVC without a primer or a flame treatment. Your fin fillets and bulkheads
  will pop off.

**Kraft paper / phenolic — benign failure.**
- Paper and phenolic fail by **splitting along a ply seam or delaminating**. The pressure is relieved
  through a crack that propagates slowly relative to a brittle fracture, and the material stays in
  large, low-velocity pieces.
- The failure is **visible in advance**: a bulge, a soft spot, a discoloured seam, a hiss.
- It is the material used by every commercial black-powder motor casing sold in the world (Estes
  casings are kraft-paper/phenolic). That is not nostalgia — it is a deliberate failure-mode choice.
- Consequence for you: **your first motors burn paper. Your first airframes are paper.** When you have
  a hundred flights and a test stand with pressure traces, move to composites.

> **The rule:** *"Which material is stronger?"* is the wrong first question.
> *"How does it fail, and can I see it coming?"* is the right one.
> PVC answers badly on both counts. Paper answers well.

Fibreglass and carbon are acceptable **airframe** materials (they are not pressure vessels — the load
is bending, and the failure mode is a stiff shard rather than a pressure-driven fragmentation), but
they are not beginner materials: they need abrasive cutting with dust extraction, they cannot be
sanded to fit like paper, and their failure at a bond line is sudden.

### 4.3 Wall thickness selection

For a thin-walled tube, bending stiffness scales as $t$ and bending strength as $t$ (both roughly
linear in $t$ at constant diameter), while mass also scales as $t$. So thickness buys strength and
stiffness at proportional mass cost — the trade is with **diameter**, not thickness.

| Wall $t$ (mm) | Mass (g/m) | $Z$ (mm³) | $I$ (mm⁴) | Verdict for a 40 mm airframe |
|---|---|---|---|---|
| 0.5 | 34 | 580 | 11 600 | Estes-class, too flimsy for hand assembly at 700 mm |
| 0.8 | 54 | 915 | 18 300 | Minimum for a D/E vehicle with a mid-body coupler |
| **1.2** | **81** | **1 378** | **27 600** | **Recommended for SR-1** |
| 1.5 | 101 | 1 684 | 33 700 | Use if flying F or above |
| 2.0 | 134 | 2 188 | 43 800 | Only for a very stiff, heavy vehicle |
| 3.0 | 199 | 3 160 | 63 200 | Over-built; adds mass aft of the CG and hurts stability |

**Design rule:** choose $t$ so that the bending MS at max-q is ≥ +0.5 *without* relying on a coupler;
then add the coupler anyway for the ejection-hoop case.

---

## 5. BUCKLING

Two completely different failure modes share the name "buckling". Students check the first and lose
vehicles to the second.

| Mode | What happens | Governs when | Relevant here? |
|---|---|---|---|
| **Euler (global) column** | The whole tube bows sideways as a column | Long, slender, low axial load | **No** — margin is 40× |
| **Local shell buckling** | A short wave pattern dimples the wall | Thin wall, short length, compression | **YES** — this is the real limit |
| **Brazier (ovalisation)** | The section ovalises under bending, then collapses | Thin wall, high bending moment | Not at these loads, yes on a 94 mm vehicle |
| **Crippling between rings** | The unsupported span between centring rings buckles | Wide ring spacing | Check span < 30 D |

### 5.1 Euler column buckling

$$P_{cr} = \frac{\pi^2 E I}{(K L)^2}$$

| Symbol | Meaning | Value here |
|---|---|---|
| $E$ | effective axial Young's modulus | 2.5 GPa (kraft tube) |
| $I$ | second moment of area | 2.755×10⁻⁸ m⁴ |
| $L$ | unsupported length | 0.58 m |
| $K$ | effective-length factor | 1.0 pinned-pinned; 0.7 fixed-pinned; 0.5 fixed-fixed |

$$P_{cr} = \frac{\pi^2 (2.5\times10^9)(2.755\times10^{-8})}{(1.0 \times 0.58)^2} = \frac{679.9}{0.3364} = 2\,021\ \text{N}$$

Compare with LC-3 (15 g axial, 53.4 N): **MS = 2 021/(1.5 × 53.4) − 1 = +24.2.**

> **Conclusion: Euler buckling is irrelevant to this vehicle.** If your analysis stops here you will
> conclude the tube is bulletproof. It is not. Go to §5.2.

Euler only begins to matter for $L/D > 60$ or for a long unpressurised motor case in Track B.

### 5.2 Local shell buckling (the real limit)

The classical small-deflection result for an axially compressed thin cylinder is:

$$\sigma_{cr,classical} = \frac{E\,t}{r\sqrt{3(1-\nu^2)}}$$

where $r$ is the **mid-surface radius**, $r = (D_o - t)/2 = 19.4\ \text{mm}$, $t = 1.2\ \text{mm}$,
$\nu = 0.3$:

$$\sigma_{cr} = \frac{(2500)(1.2)}{19.4 \times 1.6523} = \frac{3000}{32.05} = 93.6\ \text{MPa}$$

**This number is a trap.** Real shells buckle far below the classical prediction because of geometric
imperfections, and the knockdown gets worse as the shell gets thinner. NASA SP-8007 gives a
knockdown factor for near-perfect isotropic shells:

$$\gamma = 1 - 0.901\left(1 - e^{-\phi}\right), \qquad \phi = \frac{1}{16}\sqrt{\frac{r}{t}}$$

For $r/t = 16.2$: $\phi = 0.2513$, $\gamma = 0.80$, giving $\sigma_{cr} = 74.9\ \text{MPa}$.

**For a hand-made paper tube, 74.9 MPa is still wrong by a factor of ~30.** The reasons are specific
and worth understanding:

| Effect | Consequence |
|---|---|
| Orthotropic, not isotropic (paper fibres + glue lines) | $E$ and strength differ by 3–5× between directions |
| Weak interlaminar shear (glue lines, ply overlaps) | The wall delaminates before it buckles |
| Ovality from winding and handling | Out-of-round by 1–3 % kills capacity |
| Moisture absorption | $E$ drops 20–40 % in humid Bengaluru air |
| End conditions are never uniform | Load concentrates on the high spots |
| Thickness varies ±15 % around the circumference | The thin spot buckles first |

The honest engineering answer for a first build:

> **Use an empirical allowable, obtained by crushing three sample tubes, and take 0.5× the lowest
> measured failure load as your design allowable.**

A cheap test rig: stand the tube vertically on a bathroom scale under a drill press quill (or a bottle
jack under a rigid frame), press a flat plate onto the top, and read the scale at failure. A 40 mm ×
1.2 mm kraft tube typically fails at **250–500 N**, i.e.

$$\sigma_{cr,empirical} = \frac{350\ \text{N}}{146\ \text{mm}^2} \approx 2.4\ \text{MPa}$$

**Recommended design allowables (axial compression), no test data:**

| Tube material | Classical $\sigma_{cr}$ (MPa) | Effective knockdown | **Design allowable (MPa)** |
|---|---|---|---|
| Kraft paper tube | 93.6 | 0.02–0.04 | **2.0** |
| Phenolic tube | ~200 | 0.05–0.10 | **10** |
| Fibreglass (wound epoxy) | ~450 | 0.10–0.20 | **40** |
| Carbon fibre | ~1 200 | 0.10–0.20 | **80** |
| Al 6061-T6 | ~1 400 | 0.10–0.15 (or yield, whichever is less) | **120** |
| Mild steel | ~3 500 | 0.10–0.15 (or yield) | **200** |

These are the numbers used throughout this document. Note that for metals the *yield* limit usually
governs before local buckling: 0.15 × 1400 = 210 MPa > 276 MPa yield? No — 210 < 276, so buckling
governs for a very thin aluminium tube. Always take the lower of the two.

### 5.3 Worked buckling example — UVCE-SR-1

**Given:** 40 × 37.6 mm kraft tube, $L$ = 580 mm, $E$ = 2.5 GPa, allowable
$\sigma_{allow}$ = 2.0 MPa (compression), 3.0 MPa (extreme fibre in bending).

**(a) Launch compression (LC-3).** Mass forward of the thrust plate = 0.363 kg (whole vehicle).
$N = 15 \times 9.81 \times 0.363 = 53.4\ \text{N}$.

$$\sigma = \frac{53.4}{146.3} = 0.365\ \text{MPa}, \quad \text{MS} = \frac{2.0}{3.0 \times 0.365} - 1 = +0.83 \ \checkmark$$

**(b) Combined compression + bending (LC-5, F motor, 10° AoA).** $M$ = 1.67 N·m.

$$\sigma_{bend} = \frac{M}{Z} = \frac{1.67}{1.378\times10^{-6}} = 1.21\ \text{MPa}$$

Axial at the station of maximum moment (station 428 mm; mass forward ≈ 0.13 kg):

$$N = 15 \times 9.81 \times 0.13 = 19.1\ \text{N} \Rightarrow \sigma_{axial} = 0.131\ \text{MPa}$$

$$\sigma_{total} = 1.21 + 0.131 = 1.34\ \text{MPa}, \quad \text{MS} = \frac{3.0}{3.0 \times 1.34} - 1 = -0.25\ \text{(bending allowable)}$$

Hmm — note the allowable used. In bending, the *tension* extreme fibre can carry 15 MPa but the
*compression* extreme fibre is buckling-limited to ~3 MPa. Take 3.0 MPa (conservative, and correct for
a thin tube):

$$\text{MS} = \frac{3.0}{3.0 \times 1.34} - 1 = -0.25 \ \text{✗ FAIL}$$

**This is the governing case for the vehicle.** Three fixes, in order of preference:

| Fix | Effect on $\sigma$ | Resulting MS | Mass penalty |
|---|---|---|---|
| **Add a 150 mm coupler at the mid-body** (doubles $t$ locally) | $\sigma \to 0.67$ MPa | **+0.49** | +8 g |
| Increase the wall to 1.5 mm | $\sigma \to 1.07$ MPa | +0.21 | +20 g |
| Move to a phenolic tube (allowable 10 MPa) | $\sigma \to 1.34$ MPa | +1.49 | +25 g, +₹300 |
| Restrict the vehicle to D/E motors | $\sigma \to 0.33$ MPa | +2.03 | 0 g |

**Decision for SR-1: build with the coupler and fly D/E for the first flights; the coupler makes the
F-class case marginal-but-positive.** This is exactly the sort of traceable decision the PDR wants.

**(c) Brazier ovalisation check (bending).** A thin tube in bending ovalises and collapses at:

$$M_{Brazier} = \frac{2\sqrt{2}}{3}\,\frac{\pi E r t^2}{\sqrt{1-\nu^2}} = \frac{2\sqrt{2}}{3}\cdot\frac{\pi (2.5\times10^9)(0.0194)(0.0012)^2}{0.9539} = 217\ \text{N·m}$$

Compare with 1.67 N·m: **130× margin.** Brazier matters on a 94 mm fibreglass airframe, not here.
Include the check anyway — it is one line, and it is the mode that folds thin motor cases.

**(d) Crippling between supports.** The longest unsupported span is from the nose shoulder (station
120) to the forward centring ring (station 612) = 492 mm = 12.3 D. Rule of thumb: keep the unsupported
span below **30 D** for paper, **20 D** if the span carries compression. **12.3 D ✓.** For a longer
vehicle, add a coupler or a mid-body ring to break the span.

### 5.4 Buckling cheat-sheet

| Check | Formula | When it governs |
|---|---|---|
| Euler column | $P_{cr} = \pi^2 EI/(KL)^2$ | $L/D > 40$ under axial load |
| Local axial buckling | $\sigma_{cr} = \dfrac{E t}{r\sqrt{3(1-\nu^2)}}$, then × knockdown | Any thin wall in compression |
| Brazier | $M_{Br} = \frac{2\sqrt2}{3}\pi E r t^2/\sqrt{1-\nu^2}$ | Thin wall in bending, $r/t > 30$ |
| Crippling span | keep $L_{span}/D < 30$ | Ring spacing |
| Crippling between fins | keep the fin tab depth ≥ 0.5 × the fin span | TTW tabs |

---

## 6. FIN DESIGN AND ATTACHMENT

### 6.1 Aerodynamic fin loads (small) versus everything else (large)

| Load | Magnitude at the fin root | Notes |
|---|---|---|
| Aerodynamic (LC-5, F, 10°) | 17.5 N ÷ 3 fins = 5.8 N → **0.10 N·m** | Trivial |
| Landing — one fin takes the vehicle | 397 N → **7.9 N·m** | The real case |
| Handling — knocked on a table | 50 N at the tip → 2.0 N·m | Very common |
| Fin flutter | Dynamic; see `Stability_and_Aerodynamics.md` §5 | Velocity-dependent |

**Design the fin joint for 8 N·m at the root, not for 0.1 N·m.** Every fin that has ever broken on an
amateur rocket broke on the ground or on landing, not in flight.

### 6.2 Through-the-wall (TTW) versus surface mount

| Attribute | Surface mount | **Through-the-wall (TTW)** |
|---|---|---|
| Load path | fin → fillet → outer ply of tube → hoop | fin tab → MMT + centring rings + tube wall in bearing |
| Relative joint strength | 1× | **3–10×** |
| Failure initiation | The tube's outer ply delaminates (the paper peels) | The tube wall tears at the slot ends |
| Difficulty | Easy | Moderate — needs slotting (§4 of the fabrication doc) |
| Leak path | None | Slots breach the tube; must be sealed inside with epoxy |
| Aft-end access | Full | Restricted until the thrust ring is fitted |
| Internal fillet access | N/A | Only through the aft end, before the thrust ring is bonded |
| Repairability | Easy (re-fillet) | Harder (the tab is inside) |
| Mass | Fillet mass only | Slightly lighter fillet possible |
| **Recommendation** | Acceptable for D/E with a 6 mm fillet + glass tape | **Standard for F and above; use it on SR-1** |

**TTW on a 40 mm airframe:** the fin tab depth into the tube is limited by the annular gap between
$D_i$ (37.6) and the MMT OD (25.0) = 6.3 mm. A 5 mm tab depth is realistic (leaving 1.3 mm clearance
to the MMT, filled with epoxy). Do **not** cut the tab so deep that it contacts the MMT dry — it will
jack the fin out of position. Leave 1 mm and let the epoxy fill it (a "bonded gap" is stronger than a
pre-loaded contact).

### 6.3 Fin root bond check (worked)

**Geometry.** Root chord 120 mm, fillet radius $r_f$ = 6 mm, both sides. The shear plane through a
triangular fillet runs at 45° from the tube surface, with a length of $r_f\sqrt{2}$ = 8.49 mm:

$$A_{shear} = 2 \times 120 \times 8.49 = 2\,037\ \text{mm}^2 = 2.037\times10^{-3}\ \text{m}^2$$

The centroid of that shear plane sits ≈ 4 mm above the tube surface, so the resisting moment is

$$M_{allow} = \tau_{allow} \cdot A_{shear} \cdot \bar{y} = (8\times10^6)(2.037\times10^{-3})(0.004) = 65\ \text{N·m}$$

using a conservative $\tau_{allow}$ = 8 MPa for a hand-made fillet (bulk epoxy is 15–25 MPa; the
knockdown covers poor wet-out, voids and surface contamination).

**Landing case:** 397 N applied at the fin's mid-span (20 mm from the root) → 7.9 N·m.

$$\text{MS} = \frac{65}{3.0 \times 7.9} - 1 = +1.74 \ \checkmark$$

**Aerodynamic case:** 0.10 N·m → MS = +216. Not a design driver.

Also check the fin's own bending strength (G10, 3 mm thick at the root):

$$Z_{fin} = \frac{b h^2}{6} = \frac{(0.120)(0.003)^2}{6} = 1.80\times10^{-7}\ \text{m}^3$$
$$M_{allow,fin} = 350\times10^6 \times 1.80\times10^{-7} = 63\ \text{N·m}$$

**The bond (65 N·m) and the fin (63 N·m) are matched.** That is the design target: a joint no weaker
than the material it joins, so the failure mode is predictable. If your fillet gives 20 N·m, you have
built a hinge.

### 6.4 Fillet design rules

| Parameter | Rule | Why |
|---|---|---|
| Fillet radius | ≥ 3 × fin thickness; target **5–10 % of root chord** (6–12 mm here) | Bond area and stress concentration |
| Shape | Concave "cove", tangent to both surfaces | Stress concentration at the toe |
| Thickener | Colloidal silica (Cab-O-Sil) or milled glass | Microballoons *lower* strength — use only for cosmetic fillets |
| Mix consistency | Peanut butter — it must hold a peak and not sag | A sagging fillet is a thin fillet |
| Application | Two-tape method: mask both sides, apply, drag a radius tool, remove tape while wet | Clean edges, no sanding of the bond |
| Reinforcement | Add a strip of 25 g/m² glass cloth over the fillet while wet (a "glassed fillet") | 2× the peel strength for +0.5 g |
| Cure | 24 h at 25 °C minimum, or 1 h at 60 °C | Full strength is not reached in 2 h |
| Inspection | A fillet is good if a 0.5 mm feeler gauge cannot be inserted at the toe | Catches the classic "dry" fillet |

### 6.5 Why fin flutter matters

Flutter is a **self-excited** aeroelastic oscillation: bending and torsion couple so that the fin
extracts energy from the airflow. Below the flutter velocity, disturbances decay; above it, amplitude
grows exponentially within a fraction of a second and the fin sheds or shatters, usually followed by
a violent pitch/yaw excursion.

It matters because it is **not predicted by static analysis** — a fin with a huge static margin can
still flutter — and because the failure is instantaneous and catastrophic. Full treatment, the
governing equation, and a worked number are in `Stability_and_Aerodynamics.md` §5. Design rules that
fall out of it:

- Flutter velocity scales as $t^{1.5}$ — **thickness is the dominant variable.** Going from 3 mm to
  4 mm raises $V_f$ by 54 %; going from 3 mm to 2 mm *cuts it by 46 %.*
- Scales as $\sqrt G$ — G10 (3.5 GPa) is 3.2× better than balsa (0.34 GPa).
- Decreases as $\sqrt{AR^3}$ — long, narrow, unswept fins flutter first.
- Keep the tip thickness ≥ 3 mm for anything above ~200 m/s, and the tip $t/C \ge 0.05$.
- Never sharpen the trailing edge to a knife edge. Leave 0.5–0.8 mm.

---

## 7. NOSE CONE SHAPES

### 7.1 Shape comparison

| Shape | Pressure drag $\Delta C_d$ (subsonic) | CP from tip | Relative volume | Manufacture | Use when |
|---|---|---|---|---|---|
| **Conical** | 0.10–0.15 | $0.666\,L_N$ | 0.33 | Easiest — straight taper | Never, unless nothing else is available |
| **Tangent ogive** | 0.05–0.08 | $0.466\,L_N$ | 0.50 | Easy — sand to a template | **Default for a first rocket** |
| Secant ogive | 0.05–0.07 | ≈0.5 $L_N$ | 0.50 | Moderate | Slightly lower drag, harder to make true |
| **Parabolic** ($n$ = 0.5) | 0.06–0.09 | $0.500\,L_N$ | 0.50 | Easy | Good all-round |
| **Von Kármán (LD-Haack)** | 0.04–0.06 | $0.500\,L_N$ | 0.53 | Hard by hand, easy to print | Transonic/supersonic vehicles |
| Power series ($n$ = 0.75) | 0.05–0.07 | $0.600\,L_N$ | 0.45 | Moderate | Between ogive and cone |
| Elliptical | 0.03–0.05 | $0.500\,L_N$ | 0.55 | Hard | Minimum subsonic drag, fragile tip |
| Blunt / hemispherical | 0.20–0.30 | — | 0.67 | Trivial | Only for transonic flow stability or a crush zone |

For a power-series nose $r(x) = R(x/L_N)^n$, the slender-body CP is exactly:

$$\bar{x}_{CP} = L_N \cdot \frac{2n}{2n+1}$$

which gives 0.667 for a cone ($n = 1$) and 0.500 for a parabola ($n = 0.5$). The tangent ogive value
0.466 is the equivalent slender-body result and is what Barrowman tabulates.

### 7.2 How much does the nose shape actually matter?

For UVCE-SR-1, nose pressure drag is ≈ 0.05 out of a total $C_d$ of 0.50 — **10 % of the drag**.
Choosing a tangent ogive over a cone saves ≈ 0.06 $C_d$, i.e. 12 % of the total drag. For the D12
trajectory (drag loss ≈ 6 % of apogee), that is worth ≈ **0.7 % of apogee — under a metre.**

> **Therefore:** do not agonise over the nose profile on a 100 m rocket. Choose a tangent ogive
> because it is easy to sand true and has a robust tip, and spend the saved effort on fillet quality
> and mass control. The nose *shape* becomes worth optimising above Mach 0.6, where wave drag appears.

### 7.3 Nose cone design rules

- **Length:** 3–5 calibers. Shorter than 3 calibers increases pressure drag noticeably; longer than
  5 adds wetted area (skin friction) and mass for negligible gain. SR-1 uses exactly 3.0.
- **Shoulder:** 1.0–1.5 × diameter long (40–60 mm here), a slip fit of 0.1–0.2 mm. Too loose and the
  nose wobbles (a stability and drag problem); too tight and the ejection charge cannot separate it.
- **Tip strength:** a printed or balsa tip must survive the LC-1 tip-over case. Bond a 6 mm hardwood
  dowel 30 mm into the tip, or print with 4 perimeters at the tip.
- **Crush zone:** for LC-7, leave the forward 20–25 mm of the nose hollow and unreinforced. It will
  crush on a hard landing and absorb the energy instead of transmitting it to the shoulder.
- **Base squareness:** the nose base must be perpendicular to the axis within 0.3 mm. A cocked nose
  cone is a permanent trim misalignment and a leak path for the ejection gas.
- **Mass:** keep the nose light (< 35 g). Every gram here moves the CG forward, raises the static
  margin and *increases weathercocking* — a heavier nose is not automatically "more stable is better".

---

## 8. MOTOR MOUNT, THRUST PLATE AND CENTRING RINGS

### 8.1 Two thrust-transfer architectures

**Architecture A — aft thrust ring (compression).** The motor's aft closure bears on a ring bonded
inside the aft end of the MMT; thrust travels as compression down the MMT into the aft centring ring
and thence into the body tube. Simple. The MMT is in compression; the bonds see only the *difference*
between the load paths, which is small.

**Architecture B — forward thrust block (tension in the MMT).** The motor's forward closure bears on
a block bonded into the forward end of the MMT; thrust travels as tension down the MMT to the aft
centring ring. Used when the motor must not move aft (reloadable cases with a forward closure).

**For SR-1: architecture A**, with the aft thrust ring bearing on the aft centring ring. Vertical
(axial) thrust then reaches the body tube through a **bearing face**, which is far more reliable than
a bonded joint in shear. Design the load path so the primary thrust is carried in **bearing**, and the
bonds only have to hold the parts in place.

### 8.2 Thrust plate / thrust ring — worked check

| Check | Calculation | Result |
|---|---|---|
| Design thrust (LC-2) | 60 N × 1.5 | **90 N** |
| Bearing area on the aft centring ring | $\frac{\pi}{4}(37.6^2 - 25.0^2)$ | 619 mm² |
| Bearing stress | 90 / 619 | **0.145 MPa** |
| Plywood allowable compression ⊥ to grain | — | 8 MPa |
| MS | 8/(1.5 × 0.145) − 1 | **+36** ✓ |
| Screw shear (if 6 × M3) | 90 / 6 | 15 N per screw |
| M3 grade 8.8 single shear capacity | — | ≈1 500 N |
| **Screw bearing in the 1.2 mm paper wall** | 15 / (3 × 1.2) | **4.2 MPa** |
| Paper bearing allowable | — | 10 MPa |
| MS | 10/(1.5 × 4.2) − 1 | **+0.59** ✓ |

**Lesson:** screws are never the weak link — the *paper they bear against* is. Always use a washer or,
better, a plywood doubler under any screw that passes through a paper tube. A screw without a washer
in a 1.2 mm wall will elongate its hole within a few flights.

### 8.3 Motor mount tube (MMT)

| Parameter | Value | Reason |
|---|---|---|
| MMT ID | Motor OD + 0.2 to 0.4 mm | A slip fit, not a press fit; paper swells with humidity |
| MMT wall | 0.8–1.5 mm kraft or phenolic | Phenolic resists ejection heat and erosion |
| MMT length | ≥ 1.5 × motor length + the thrust ring | Supports the case against bending |
| MMT material | Phenolic preferred for F and above (hot ejection gas) | Kraft chars and can smoulder |
| Bond to rings | Epoxy, 360° fillet both sides of both rings | See §8.4 |

### 8.4 MMT bond check under the ejection load (LC-8)

The ejection charge pushes the motor aft with ≈181 N (0.4 MPa case, §2.5). This load must travel
through the thrust ring → MMT → centring rings → body tube.

| Joint | Area | Stress | Allowable | MS |
|---|---|---|---|---|
| MMT OD to ring (×2 rings, 3 mm each) | $\pi(25)(3)\times2$ = 471 mm² | 0.38 MPa | 8 MPa | +6.0 |
| Ring OD to tube (×2 rings) | $\pi(37.6)(3)\times2$ = 709 mm² | 0.26 MPa | 8 MPa | +9.4 |
| Thrust ring bearing on MMT end face | $\frac{\pi}{4}(25^2 - 24.5^2)$ = 19.6 mm² | **9.2 MPa** | 8 MPa | **−0.24 ✗** |

**Action:** the thrust ring's bearing area on the MMT end face is marginal *if it is a thin annular
lip*. Fix by making the thrust ring a **plug** that is 10 mm deep and bonded *inside* the MMT (bond
area = π × 24.5 × 10 = 770 mm², shear stress 0.24 MPa → MS = +10). This also centres the ring and
gives a second load path. This is a good example of a joint that looks strong and is not, because the
bearing area was never computed.

### 8.5 Centring rings

- **Count:** 2 minimum (fore and aft). 3 for a motor longer than 150 mm or a heavy case.
- **Thickness:** 2.5–3 mm aircraft ply or 3 mm FR-4. Not balsa, not 3D-printed (they creep under
  launch vibration and heat).
- **Fit:** the OD is a *slip* fit in the tube (0.1–0.2 mm) so the mount can be inserted — but the gap
  must be filled with epoxy. A loose ring bonded with a thin glue line and no fillet will fail.
- **Fillet:** 360°, both sides of every ring. Fillets on the ring's **forward** face where you can
  reach them before installation, and on the aft face through the aft end.
- **Alignment:** the rings must be perpendicular to the MMT axis within 0.5° or the motor will bind.
  Drill/cut them as a matched pair on the same setup (stack them and drill together).
- **Ventilation:** the forward centring ring should have 2 × 4 mm holes so the ejection gas can reach
  the recovery compartment and the pressure cannot trap between the rings.

---

## 9. COUPLERS, BULKHEADS AND SEPARATION JOINTS

### 9.1 Couplers

A coupler is a short tube that fits *inside* the airframe, doubling the wall thickness locally. Two jobs:

1. **Structural:** it doubles the local bending stiffness and hoop strength (§5.3, §2.5). On SR-1 a
   150 mm coupler at the mid-body takes the bending MS from −0.25 to +0.49 and the ejection hoop
   MS from −0.15 to +0.72.
2. **Joint:** it is the sliding interface at the separation joint, where the nose (or the upper stage)
   joins the body.

| Parameter | Rule |
|---|---|
| Length | ≥ 2 × diameter (80 mm); 3–4 × diameter for a separation joint (120–160 mm) |
| Material | The same as the airframe (matched thermal expansion, matched stiffness) |
| Fit in the tube | 0.1–0.25 mm slip; it must fall out under its own weight |
| Bond | Epoxy, fully wetted, with a 6 mm internal fillet at one end only (leave the other end free to slide) |
| Vent | Drill a 2 mm hole through the coupler's free end so the joint cannot air-lock |
| Alignment | Test-fit with the recovery packed — a coupler that fits empty may bind when loaded |

### 9.2 Bulkheads

A bulkhead is a solid disc bonded inside a coupler or tube. It carries three jobs: it reacts the
ejection pressure, it anchors the shock cord, and it separates the recovery compartment from the
avionics.

| Load | Value | Check |
|---|---|---|
| Ejection pressure (LC-8) | 0.4 MPa over a 37.6 mm bore → **444 N** | Bond shear + plywood bending |
| Bond area (10 mm depth) | π(37.6)(10) = 1 181 mm² | shear = 444/1181 = 0.38 MPa ✓ MS = +6.0 |
| Plywood 3 mm disc bending | $M = \frac{Pr^3}{...}$ — treat as a flat plate | Use 3 mm minimum; 4 mm if unsupported |
| Peel | The dominant real-world failure | Add a mechanical backup: a through-bolt, or a second ring on the far side |

**Rules:**
- Plywood (3–4 mm, aircraft or marine grade). Not balsa. Not foam-core.
- Bond with a 6 mm fillet on the *loaded* side, plus a ring or a bolt as a mechanical backup.
- Every bulkhead gets a **pressure-relief hole** (2 mm) unless it is meant to seal. A trapped volume
  between two bulkheads will blow a joint apart when the vehicle goes from 900 m to ground level.
- The bulkhead that anchors the shock cord should be at least 60 mm from the tube's open end so the
  load spreads before it reaches the lip.

### 9.3 Separation joints

| Type | Retention | Release | Use |
|---|---|---|---|
| Friction fit (nose shoulder) | Friction + a shear pin | Ejection charge | **SR-1, first flights** |
| Shear pin (nylon 2 mm) | 1–2 nylon pins through the tube into the shoulder | Ejection charge | **Recommended** |
| Tape wrap | 1–2 wraps of masking tape | Ejection charge | Practice only; inconsistent |
| Screw + O-ring | Mechanical | Servo / solenoid | Payload separation, competition vehicle |
| CO2 / compressed gas | Mechanical | Altimeter | Large vehicles, no-pyro requirement |

**Shear pin sizing (worked).** Nylon 6.6, 2 mm diameter, single shear:

$$F_{shear} = \tau \cdot A = (0.5 \times 80\ \text{MPa}) \times \frac{\pi}{4}(2)^2 = 40 \times 3.14 = 126\ \text{N per pin}$$

Requirement: the pin must survive the *drag and inertia* separation load (small, < 20 N) but release
below the ejection force (181 N at 0.4 MPa). **One pin (126 N) is correct; two pins (252 N) will not
release at 0.4 MPa.** This is why shear-pin count is a *tuned* parameter, and why you test it on the
ground before every flight. Always carry spare pins.

---

## 10. RECOVERY SYSTEM ATTACHMENT — THE AIRFRAME MUST SURVIVE DEPLOYMENT

The deployment event is the highest-load event of the flight (§2.6). Every element below must be
designed, not assumed.

### 10.1 The load path, in order

```
parachute → shroud lines → swivel → shock cord (elastic section FIRST, then Kevlar)
   → eye bolt / hardpoint → bulkhead → bulkhead bond → coupler → body tube
   → (the other end) nose shoulder → shear pin → nose cone
```

**Every arrow is a joint that can fail.** Write them down; check each one.

### 10.2 Shock cord — the elasticity calculation (this is the important one)

A shock cord absorbs energy by stretching. The peak force when a mass $m$ falls a distance $h$ onto a
cord that then stretches by $x$ is found from energy balance:

$$mg(h + x) = \tfrac{1}{2}kx^2 \quad\Rightarrow\quad F_{peak} = kx = 2mg\frac{h+x}{x}$$

The **peak g level** is therefore

$$n_g = \frac{F_{peak}}{mg} = \frac{2(h+x)}{x}$$

| Shock-cord material | Stretch at 30 % load | $x$ for a 0.7 m fall | Peak g | Verdict |
|---|---|---|---|---|
| 2 mm Kevlar 29 (essentially inextensible, $x$ ≈ 5 mm) | < 3 % | 5 mm | **300 g** | ✗ Will rip the bulkhead out |
| 3 mm Kevlar + 2 m braided elastic | 60–100 % | ~500 mm | **4.8 g** | ✓ But elastic degrades with heat |
| 6 mm braided elastic only | 100–150 % | ~700 mm | **4.0 g** | ✗ Melts at the ejection charge |
| Tubular nylon webbing (1"), 20 % stretch | 20 % | 140 mm | 12 g | ✓ Good compromise |

**Design conclusion:** never use a Kevlar-only shock cord on a vehicle that must survive 30 g. Kevlar
does not stretch, so all the energy goes into the peak force. Use a **hybrid cord**: an elastic
section nearest the nose (energy absorber) and a Kevlar section nearest the ejection charge (heat
resistance). SR-1: 1.5 m elastic + 2 m Kevlar, giving 4–15 g under the 30 g requirement — a margin of
2–7×.

**Shock cord length:** ≥ 3 × the vehicle length (≥ 2.1 m for SR-1), and 5 × if you fly without a
Nomex shield. SR-1 carries 3.5 m total. The cord must be long enough that the nose cone cannot snap
back into the body tube — that collision is the classic "zipper" that splits a tube from lip to fin.

### 10.3 Anchor hardware

| Item | Sizing rule | Check |
|---|---|---|
| Eye bolt | M4 × 40 mm, stainless A2, screwed through the bulkhead with a nyloc on the far side | 107 N on an M4 = 0.09 × yield ✓ |
| Bonded hardpoint (no through-bolt) | ≥ 800 mm² of bond area | 107 N / 800 mm² = 0.13 MPa ✓ but peel is the risk — always add a mechanical key |
| Kevlar cord knot | A bowline loses 40–50 % of the cord strength; use a sewn or spliced loop, or a figure-8 with a 100 mm tail | 3 mm Kevlar ≈ 2 900 N; a knot gives ~1 500 N ✓ |
| Swivel | Rated ≥ 300 N | Prevents line twist on descent |
| Zipper guard | A 30 mm length of heat-shrink or a Kevlar sleeve over the cord where it exits the tube | Prevents the cord cutting the tube lip |

### 10.4 Heat protection

| Material | Continuous service | Short-term (ejection flame) | Indian sourcing |
|---|---|---|---|
| Nomex fabric | 200–250 °C | 370 °C | ₹1 200–2 500/m² (imported) |
| Silica cloth (welding blanket) | 1 000 °C | 1 200 °C | **₹400–900/m² — the best value in India** |
| Fibreglass cloth | 500 °C | 550 °C | ₹120–250/m² |
| Kraft paper wadding | 200 °C (chars) | — | ₹5 per flight — use it *as well* |
| Aluminium foil | Reflects radiant heat only | Melts at 660 °C | Not sufficient alone |

**Recommendation:** a silica welding blanket cut into a 150 × 150 mm square, wrapped around the chute,
plus a kraft-paper wadding plug between the motor and the recovery. Cost per flight: ~₹30. This one
item prevents most recovery failures.

---

## 11. COMPOSITE LAYUP BASICS (for when you advance)

### 11.1 Fibres

| Fibre | Density (g/cm³) | Tensile strength (MPa) | Modulus (GPa) | Strain to fail | Cost in India | Notes |
|---|---|---|---|---|---|---|
| E-glass | 2.54 | 3 400 | 72 | 4.8 % | ₹120–300/m² (200 gsm woven) | Cheap, tough, heavy, low stiffness |
| S-glass | 2.49 | 4 700 | 86 | 5.6 % | ₹800–1 500/m² | 30 % stronger than E, 3× the price |
| Aramid (Kevlar 49) | 1.44 | 3 600 | 131 | 2.8 % | ₹2 500–4 500/kg | Excellent impact, poor compression, hard to cut, absorbs moisture |
| Carbon (standard modulus, T300-class) | 1.76 | 3 530 | 230 | 1.5 % | ₹1 800–3 500/m² (200 gsm twill) | Stiff, brittle, conductive dust, galvanic with aluminium |
| Carbon (intermediate modulus) | 1.80 | 5 500 | 290 | 1.9 % | 2–4× standard | Not for a first build |

### 11.2 Resin systems

| Resin | Pot life | Tensile strength (MPa) | Elongation | Cure | Cost | Verdict |
|---|---|---|---|---|---|---|
| **Laminating epoxy** (e.g. Araldite AW106/HV953U, West 105) | 25–40 min | 50–80 | 4–6 % | 24 h @ 25 °C, + post-cure 60–80 °C | ₹700–1 500/kg | **Use this** |
| Polyester | 10–20 min | 40–60 | 2–3 % | 2–4 h with MEKP | ₹250–450/kg | ✗ Brittle, 5–8 % shrinkage, poor adhesion, styrene fumes |
| Vinyl ester | 20–30 min | 60–85 | 4–6 % | 4–8 h | ₹600–1 000/kg | ✓ Better toughness and moisture resistance than polyester |
| Phenolic | 30–60 min | 40–60 | 1–2 % | Heat-cured | ₹500–900/kg | High temperature and low smoke; brittle — for liners and ablatives |
| 5-minute epoxy | 5 min | 20–35 | 1–2 % | 20 min | ₹1 200–2 000/kg | ✗ Never structural (§13) |

### 11.3 Process comparison

| Process | Fibre volume fraction | Void content | UD tensile strength (glass / carbon) | Skill | Equipment |
|---|---|---|---|---|---|
| Hand wet layup | 30–45 % | 5–10 % | 250–400 / 500–800 MPa | Low | Brush, roller, release film |
| Vacuum bagging | 50–60 % | 1–3 % | 400–600 / 800–1 200 MPa | Medium | Vacuum pump (−0.8 bar), bagging film, breather, sealant tape |
| Resin infusion | 55–65 % | 1–2 % | 500–700 / 1 000–1 400 MPa | High | Pump, vacuum, flow media |
| Prepreg + autoclave | 60–65 % | < 1 % | 1 200–1 800 MPa (carbon) | Very high | Autoclave — not available to us |

**Rule of mixtures** for a first estimate of a unidirectional laminate:

$$\sigma_{laminate} \approx V_f \sigma_{fibre} + (1 - V_f)\sigma_{resin}$$

For E-glass/epoxy at $V_f$ = 0.40: $0.40(3400) + 0.60(60) = 1\,396\ \text{MPa}$ ideal — but a woven
fabric loses ~30 % to crimp, and a hand layup loses another 20–30 % to voids and misalignment. **Expect
500–700 MPa from a good hand-laid glass laminate, not 1 400.**

### 11.4 Making a body tube (roll-wrapping)

1. Mandrel: 37.6 mm OD aluminium tube, 800 mm long, polished, with a 1° taper at one end.
2. Release agent: 4–6 coats of PVA release film or a carnauba wax, buffed between coats.
3. Cut the fabric on the **bias** (45°) if you want torsional stiffness, or at 0°/90° for hoop and
   axial. A ±45°/90° stack is a good general airframe.
4. Wet out on a flat table with a squeegee, not on the mandrel — you get better wet-out and fewer voids.
5. Roll onto the mandrel under tension, working out bubbles as you go.
6. Wrap with **shrink tape** (2–3 wraps, 20 mm overlap) or a Mylar peel ply + breather, and vacuum bag.
7. Cure 24 h at room temperature, then post-cure 4 h at 60 °C (raises Tg from ~50 to ~80 °C).
8. Remove the mandrel, then machine the ends square on a lathe with a diamond or carbide wheel.

**Do not** attempt a roll-wrapped tube as your first composite part. Make flat fin stock first.

### 11.5 Composite dust and resin safety — non-negotiable

| Hazard | Mechanism | Control |
|---|---|---|
| **Epoxy sensitisation** | Repeated skin contact causes allergic dermatitis in 5–10 % of exposed people, then asthma. **Once sensitised, it is permanent.** | Nitrile gloves (not latex), long sleeves, no bare-hand wiping, wash with soap and cold water (never a solvent) |
| Cured composite dust | Respirable glass/carbon fibres; a mechanical irritant and a suspected carcinogen | **Wet-sand only.** If dry sanding is unavoidable: P100 half-mask, eye seal, HEPA vacuum at the tool, no compressed air |
| Carbon fibre dust | **Electrically conductive** — destroys motors, shorts electronics, irritates skin | Dedicated area, HEPA extraction, never near an open tool or a laptop |
| Styrene (polyester) | Narcotic, irritant, flammable | Only outdoors or with local extraction; organic vapour cartridge |
| Exotherm | A 200 g cup of mixed epoxy can reach 150–200 °C and smoke or ignite | Mix ≤ 80 g at a time, in a shallow container, never in a sealed pot |
| Acetone / IPA | Flammable, defats skin | Metal container, bonded storage, no ignition sources, ≤ 1 L in the shop |

**Shop rule: no epoxy work without gloves and ventilation. No dry sanding of composites. Ever.**

---

## 12. FASTENERS AND ADHESIVES

### 12.1 Adhesive selection chart

| Adhesive | Shear strength (MPa) | Service temp | Gap fill | Cure | Use for | **Never use for** |
|---|---|---|---|---|---|---|
| **Structural epoxy** (Araldite AW106/HV953U, West 105/206, 30-min) | 15–25 | 60–90 °C (post-cured) | 0.1–3 mm | 24 h @ 25 °C | Fins, bulkheads, MMT, couplers, fillets | — |
| Epoxy + colloidal silica | 12–20 | 60–90 °C | 0–10 mm | 24 h | Fillets, gap filling | Thin bond lines (too stiff) |
| Epoxy + microballoons | 6–12 | 50–70 °C | 0–20 mm | 24 h | Cosmetic fillets, fairings | **Structural fillets** |
| 5-minute epoxy | 8–12 | **40–55 °C** | 0–2 mm | 5–20 min | Tack-tacking, temporary fixing | Any structural joint |
| **Cyanoacrylate (CA)** | 15–25 | 70–80 °C | < 0.1 mm | Seconds | Balsa, tacking, hardening paper edges | Fin fillets, gap filling, hot areas, peel loads |
| Polyurethane (Sikaflex 221, Gorilla) | 5–10 | 60–80 °C | 0–5 mm | 12–24 h (moisture) | Wood/paper, gap filling, semi-flexible joints | High-stress joints, vacuum (it foams) |
| PVA (Fevicol SH, ₹120/kg) | 5–8 | **softens at 60 °C, re-dissolves in water** | < 0.2 mm | 4–12 h | Paper-tube couplers in a *practice* model | Fins, bulkheads, anything flown |
| Hot melt (EVA) | 2–5 | **softens at 60–80 °C** | 0–2 mm | 30 s | Temporary fixturing, packaging | Anything on a launch pad in the sun |
| Polyester resin | 5–15 | 50–70 °C | 0–5 mm | 1 h | Nothing on a flight vehicle | Structural joints |
| Epoxy putty (Araldite Steel) | 8–15 | 60–80 °C | 0–20 mm | 1 h | Fillet repair, thread repair | Primary structure (heavy) |

> ### The three adhesives that ruin student rockets
> 1. **5-minute epoxy on fin fillets.** Tg is 40–55 °C. A black rocket on a Bengaluru launch pad in
>    April reaches 65–75 °C surface temperature. The fillet goes rubbery and the fin moves. Use
>    30-minute or laminating epoxy.
> 2. **CA on anything that sees peel or heat.** CA is brilliant in shear and terrible everywhere else.
>    It also embrittles paper — a CA-soaked tube lip cracks instead of deforming.
> 3. **Hot melt anywhere in the flight vehicle.** It melts at 60–80 °C. Your recovery harness will
>    un-glue itself in a hot car.
>
> **The single best investment the club can make: one 1.2 kg kit of Araldite AW106/HV953U
> (≈ ₹1 800).** It is slower, messier and more annoying than 5-minute epoxy, and it is the reason
> your fins will still be attached after the tenth flight.

### 12.2 Epoxy working practice

| Parameter | Value | Note |
|---|---|---|
| Mix ratio AW106:HV953U | **100 : 80 by weight** (not by volume) | Weigh it. A ₹500 0.01 g scale pays for itself |
| Mix ratio West 105:205/206 | 5 : 1 by volume | |
| Pot life @ 25 °C | 30–40 min (AW106) | **Halves for every +10 °C** — a 35 °C workshop gives 15 min |
| Handling strength | 8–12 h | Do not move the part before this |
| Full cure | 24–48 h @ 25 °C | |
| Post-cure | 4 h @ 60 °C (optional) | Raises Tg from ~50 to ~80 °C — worth doing for fin cans |
| Max batch | 80 g in a shallow cup | Exotherm > 150 °C in a deep cup will smoke |
| Mixing | 2–3 minutes, scraping the sides and bottom | Unmixed resin is the #1 cause of a weak joint |
| Bond line | 0.1–0.3 mm | Starved (< 0.05) and thick (> 0.5) are both weak |
| Working temperature | > 18 °C | Below 15 °C, epoxy barely cures — use a heat lamp |

### 12.3 Surface preparation (this is 80 % of bond strength)

| Substrate | Method |
|---|---|
| Kraft paper / phenolic tube | Sand with **120 grit** until the gloss is gone — do **not** cut through the outer ply. Wipe with IPA. Let it dry 10 min (IPA soaks into paper and slows the cure) |
| G10 / FR-4 fin | Sand 80–120 grit, wipe with IPA or acetone. Never touch the bond area with bare hands afterwards |
| Aluminium | Sand 120 grit, then **bond within 30 minutes** — aluminium oxide forms instantly. Best practice: a chromic-acid etch or an epoxy primer (e.g. 3M 3960). Silane coupling agents (Dow Z-6040) give another 2–3× on aluminium and glass |
| Plywood | Sand 120 grit, dust off, size with thinned epoxy first if the wood is porous |
| 3D-printed parts | Sand the layer lines, wipe with IPA. PLA bonds moderately; PETG and ABS need a light flame treatment or a primer |
| PVC / polycarbonate / polyethylene | **Do not bond.** Use a mechanical fastener. If you must, use a cyanoacrylate primer (Loctite 770) and accept 30 % of the strength |
| **Any surface** | **No silicone anywhere near a bond area.** Silicone contamination (mould release, hand cream, some lubricants) destroys epoxy adhesion and is almost impossible to remove |

### 12.4 Fasteners

**Torque values (dry, into a matching-strength material):**

| Size | Grade 8.8 steel (N·m) | A2/A4 stainless (N·m) | Into 6061-T6 (N·m) | Nylon (N·m) |
|---|---|---|---|---|
| M3 | 1.3 | 1.0 | 0.6 | 0.15 |
| M4 | 3.0 | 2.3 | 1.4 | 0.3 |
| M5 | 5.9 | 4.4 | 2.7 | 0.5 |
| M6 | 10.1 | 7.6 | 4.6 | 0.8 |
| M8 | 24.6 | 18.5 | 11.0 | — |
| M12 | 86 | 65 | 40 | — |

**Rules:**
- **Never rely on friction alone** in a vibration environment. Use a nyloc nut, a castellated nut with
  a cotter pin, or threadlocker.
- **Loctite 243 (blue)** for anything you may need to remove; **Loctite 271 (red)** only where you
  never want it apart. Red requires 250 °C to release — do not use it on aluminium.
- **Never put threadlocker on plastic** (ABS, polycarbonate, acrylic). Anaerobic threadlockers
  stress-crack plastics. Use a nylon-insert nut instead.
- **Never use a star or split lock washer as the primary locking method.** They are close to useless
  under vibration. They are acceptable only as a secondary.
- **Always use a washer** under any fastener bearing on paper, phenolic or composite — see the bearing
  check in §8.2, which is the check that fails.
- **Rivets** (blind aluminium) are acceptable only for brackets that see no structural load; they
  loosen in a paper/composite wall.
- **Thread engagement:** at least 1.5 × the diameter in aluminium, 1.0 × in steel, 2.5 × in plastic.

---

## 13. DESIGN REVIEW CHECKLIST

Take this to every design review. Every "no" is an open action.

### Loads
- [ ] Thrust design value uses the **peak** thrust from a certified curve, not the average
- [ ] 15 g launch case applied as a body-inertial load, reacted at the thrust plate
- [ ] 30 g shock case applied to every element of the recovery load path
- [ ] **Ejection charge pressure (0.3–0.7 MPa) included** in the motor retention, MMT bond and tube hoop
- [ ] Max-q bending with a stated angle of attack (≥ 10°) and a stated $C_{N\alpha}$
- [ ] Landing case with a stated descent rate, stopping distance and crush stroke
- [ ] Handling case (tip-over, table knock) included for the fins and nose
- [ ] Thermal case: 70 °C soak, adhesives and printed parts derated

### Analysis
- [ ] Euler buckling check (and a statement that it is not critical, or why it is)
- [ ] **Local shell buckling with a knockdown factor, based on measured or tabulated allowable**
- [ ] Brazier ovalisation for any thin-walled tube in bending
- [ ] Unsupported span / diameter ratio reported
- [ ] Combined axial + bending stress with a stated interaction rule
- [ ] Every margin computed with the correct FoS for that class of structure
- [ ] At least one sample tested to failure for every non-metallic structural material

### Joints
- [ ] Every bond has a computed area and a computed shear stress
- [ ] Bonded joints use FoS = 3.0
- [ ] No joint relies on peel strength alone
- [ ] Every screw has a washer and a computed bearing stress
- [ ] Every threaded fastener has a positive locking method
- [ ] Thrust is carried in **bearing** somewhere in the load path, not only in shear

### Verification
- [ ] CG measured with the motor installed, marked on the airframe, and compared with the design
- [ ] Total launch mass within ±5 % of the design value
- [ ] Pull test on the shock cord anchor: 2 × the 30 g load, no movement
- [ ] Pull test on the motor retention: 200 N aft, no movement
- [ ] Shear pin release verified with the actual ejection charge on the ground
- [ ] Swing test performed (see `Stability_and_Aerodynamics.md` §7.4)
- [ ] 15 g axial static test performed on the assembled vehicle (sandbag / weight test)
- [ ] Fin alignment re-checked **after** painting (paint adds mass asymmetrically)

---

## 14. QUICK-REFERENCE SUMMARY

| Quantity | Value | Unit |
|---|---|---|
| Reference vehicle | UVCE-SR-1, 40 mm, 700 mm, 275 g dry | — |
| Design thrust (LC-2) | 90 | N |
| Launch inertial load, 15 g (LC-3) | 53.4 | N |
| Max-q bending, 10° AoA, F (LC-5) | 1.67 | N·m |
| Deployment shock, 30 g (LC-6) | 107 | N |
| Ejection charge force, 0.4 MPa (LC-8) | 181 | N |
| Ejection hoop stress, 0.4 MPa | 6.3 | MPa |
| Tube area / $I$ / $Z$ (1.2 mm wall) | 146.3 / 27 550 / 1 378 | mm² / mm⁴ / mm³ |
| Euler critical load | 2 021 | N |
| Local buckling, classical (paper) | 93.6 | MPa |
| **Local buckling, design allowable (paper)** | **2.0** | MPa |
| Governing structural case | Bending at max-q (LC-5) **and** ejection hoop (LC-8) | — |
| Fix | 150 mm mid-body coupler (+8 g) | — |
| Required FoS: bonded joint | 3.0 | — |
| Required FoS: paper structure | 3.0–4.0 | — |

---

*End of Structures Design Guide. See `Stability_and_Aerodynamics.md` for where the aero loads come
from, `Materials_Database.md` for the properties used above, and `Fabrication_and_Manufacturing.md`
for how to actually build it so that the joints meet the analysis.*
