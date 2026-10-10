# 04 — Structures & Aerodynamics Path

**Airframes, fins, materials, recovery, and fabrication.**

| | |
|---|---|
| **Time** | Foundation 2–3 weeks · Working 4–8 weeks · Advanced months |
| **Prerequisites** | [`01_Start_Here.md`](<01_Start_Here.md>) |
| **Cost** | ~₹3,250 for three airframes |
| **You will need** | Hand tools, and access to a workshop for the later tiers |
| **Workspace docs** | [`../20_AEROSTRUCTURES/`](<../20_AEROSTRUCTURES/Structures_Design_Guide.md>) |

> **Why this path is satisfying:** you finish each session holding something. That matters more than
> it sounds — it is the difference between a member who stays and one who drifts.

---

## FOUNDATION (2–3 weeks)

### Learn

1. **The loads a rocket sees** — thrust, drag, bending from wind and angle of attack, landing shock,
   and the deployment shock from the recovery system. All of them act on the same tube.
2. **Stress and strain, simply** — force ÷ area = stress. Materials have a limit.
3. **The two structural requirements that get designed to:**
   - The competition requires surviving **15 g launch acceleration** and **30 g shock**
   - Our own casing rule: burst at no more than **2.5 × MEOP**, never below **1.5 ×**
4. **Why PVC is dangerous** — it *shatters* into fragments; paper and phenolic *split*. Same load,
   very different failure. Full comparison in
   [`../20_AEROSTRUCTURES/Materials_Database.md`](<../20_AEROSTRUCTURES/Materials_Database.md>) §2.
5. **Fins and stability** — fins move the CP backwards. That is their entire purpose. Slightly
   thicker fins resist flutter dramatically better (flutter scales with thickness³).
6. **Nose cone shapes** — ogive, conical, parabolic, Von Kármán. Drag differences are small at our
   speeds; manufacturing simplicity matters more.

### Do

- **Cut and square a body tube.** Verify the length agrees within 0.5 mm at four points. This sounds
  trivial and is not.
- **Build a fin alignment jig.** Half an hour of work that prevents the most common amateur failure.
- **Cut and shape a set of fins** in 3 mm aircraft plywood.
- **Dry-assemble** a complete rocket. No glue. Find out what does not fit *before* it is permanent.

### Checkpoint — you can:

- [ ] Cut a tube square to within 0.5 mm and prove it
- [ ] Explain why through-the-wall fins are stronger than surface-mounted
- [ ] Say what static margin is and how fin size affects it
- [ ] Explain why we use paper or phenolic rather than PVC
- [ ] State the 2.5× / 1.5× casing rule and why an over-strong casing is *more* dangerous
- [ ] Dry-assemble a rocket that fits

---

## WORKING (4–8 weeks)

### Learn

1. **Buckling** — thin tubes fail by buckling, not by exceeding material strength. Euler column
   buckling and local shell buckling, with the equations.
2. **Bonding properly** — surface preparation, epoxy mixing by weight, fillet radii, and why a dirty
   surface defeats the best adhesive.
3. **Fin flutter** — the aeroelastic failure that shreds fins. How to avoid it.
4. **Recovery design** — parachute sizing from the descent-rate equation, shock cord loads, and why
   the parachute must survive the deployment.
5. **Composite basics** — fibre types, wet layup versus vacuum bagging, and the dust hazard.

### Do

1. **Build airframe #1** — simple, surface-mounted fins, launch lug. Fly it.
2. **Build airframe #2** — through-the-wall fins, rail buttons, better finish. Fly it.
3. **Build airframe #3** — recovery system sized and drop-tested, all measurements logged.
4. **Run a structural test** — load a tube to failure and compare against your prediction. Then you
   know whether your calculations are any good.
5. **Parachute drop test** — measure the actual descent rate and confirm it is in the 2–5 m/s band.

> ⚠️ **Measure everything.** Mass, CG, dimensions, descent rate. A rocket whose CG you do not know is
> a rocket whose stability you cannot claim.

### Checkpoint — you can:

- [ ] Bond a structural joint that survives a load test
- [ ] Calculate the buckling load of a thin tube and explain the failure mode
- [ ] Size a parachute for a target descent rate, then verify by drop test
- [ ] Explain fin flutter and how thickness and span affect it
- [ ] Complete a mass budget to within ±5%
- [ ] Measure CG and compute the static margin

---

## ADVANCED (months)

- **FEA** — model a fin or a pressure vessel, apply the right loads and boundary conditions, and
  interpret the result critically
- **Composite fabrication** — vacuum bagging, and understanding fibre orientation
- **Thermal analysis** — casing heating during burn, insulation sizing
- **Mechanism design** — the separation and deployment mechanisms, which are the hardest mechanical
  problem on the vehicle
- **Design for the competition payload** — the CAN-7USAT bay, with the 15 cm × 40 cm envelope

### Checkpoint — you can:

- [ ] Produce an FEA result and justify your boundary conditions
- [ ] Design and test a non-pyrotechnic separation mechanism
- [ ] Size thermal insulation with a heat-transfer calculation
- [ ] Teach the Foundation tier to a new member

---

## First build

**Three airframes, increasing in difficulty.** Not one. Three.

| # | Complexity | New skills | Gate |
|---|---|---|---|
| 1 | Simple | Tube cutting, fin alignment, surface mount, launch lug | Flies straight, recovers intact |
| 2 | Intermediate | Through-the-wall fins, fillets, rail buttons, better finish | Flies straight **twice** |
| 3 | Full | Sized recovery, drop-tested, full mass budget, primer and paint | Mass within ±5%, descent 2–5 m/s |

**Total material cost ≈ ₹3,250** — see
[`../20_AEROSTRUCTURES/Materials_Database.md`](<../20_AEROSTRUCTURES/Materials_Database.md>) §12.

> **Why three:** the first teaches you what you do not know. The second teaches you to do it properly.
> The third teaches you to do it repeatably. Repeatability is the actual engineering skill.

---

## Resources

| Resource | Cost | What it is good for |
|---|---|---|
| [`../20_AEROSTRUCTURES/Structures_Design_Guide.md`](<../20_AEROSTRUCTURES/Structures_Design_Guide.md>) | Free | Our own loads, materials and design method |
| [`../20_AEROSTRUCTURES/Stability_and_Aerodynamics.md`](<../20_AEROSTRUCTURES/Stability_and_Aerodynamics.md>) | Free | Barrowman method and stability |
| [`../20_AEROSTRUCTURES/Materials_Database.md`](<../20_AEROSTRUCTURES/Materials_Database.md>) | Free | Properties and Indian sourcing |
| [`../20_AEROSTRUCTURES/Fabrication_and_Manufacturing.md`](<../20_AEROSTRUCTURES/Fabrication_and_Manufacturing.md>) | Free | Workshop practice, step by step |
| [NASA Beginner's Guide to Aeronautics](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/) | Free | Aerodynamics fundamentals, well explained |
| [MIT OpenCourseWare](https://ocw.mit.edu/) | Free | Search for *Unified Engineering* (structures + materials) and *Solid Mechanics*. Real lecture courses, free. |
| [OpenRocket Resources wiki](https://wiki.openrocket.info/Resources) | Free | Barrowman's original report and experimental data |
| *Understanding Aircraft Composite Construction* — Zeke Smith | ~₹2,500 | If you go down the composites route |
| *Machinery's Handbook* | ~₹3,000 | Workshop reference. The club should own one copy. |

### YouTube — practical fabrication

Search for these topics rather than specific channels; the good channels change:
- "through the wall fins model rocket"
- "fin alignment jig build"
- "rocket parachute folding"
- "composite vacuum bagging"

### India-specific notes

| Item | Note |
|---|---|
| **Aircraft plywood** | Model/hobby shops, or timber merchants. Ask for **birch aircraft ply**, not construction ply. |
| **Kraft paper tube** | Stationery/paper merchants — ask for heavy-wall postal tube |
| **Aluminium** | Local metal merchants. **Always ask for the alloy and temper** — "aluminium" is not a specification |
| **Composites** | Online composites suppliers. Cut with extraction or wet — the dust is a genuine hazard. |
| **3D printing** | Use **PETG, not PLA** — PLA softens at ~60 °C and can deform sitting on the pad in the sun |

---

## What NOT to do

| ❌ | Why |
|---|---|
| Skip the dry assembly | You will discover the misfit after the epoxy cures |
| Glue before checking fin alignment | A misaligned fin spirals the rocket and costs most of your altitude |
| Use PVC | It shatters. Paper splits. |
| Guess the mass | You cannot claim stability without knowing CG |
| Fly without measuring descent rate | A rocket coming down at 15 m/s is a hazard, not a recovery |
| Over-build "for safety" | Excess strength is excess mass, and mass costs altitude |
| Make fins too thick everywhere | Thickness helps flutter but costs drag and mass — a tapered section is better |
