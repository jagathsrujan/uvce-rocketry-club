# Materials Database

**UVCE Rocketry Club — Aerostructures Guide 3**

| | |
|---|---|
| **Document** | `20_AEROSTRUCTURES/Materials_Database.md` |
| **Purpose** | One place to look up material properties, workability, and Indian sourcing |
| **Companion documents** | `Structures_Design_Guide.md`, `Fabrication_and_Manufacturing.md` |
| **Status** | 🟡 Properties are typical handbook values. **Verify your actual stock** — especially for anything pressure-bearing. |

> ⚠️ **Costs are indicative 2026 Bengaluru planning figures, not quotations.**

---

## 1. How to use this database

1. **Find the material** in the relevant section.
2. **Check the beginner-suitability rating.** Anything rated ❌ should not be used until the club has
   flight heritage.
3. **For pressure-bearing parts, do not trust a handbook number alone.** Measure, or buy certified
   stock with a mill certificate.
4. **Record what you actually bought** in `00_ADMINISTRATION/BOM_and_Budget.xlsx`.

**Rating key:** ✅ good for beginners · 🟡 usable with care · ❌ avoid until experienced

---

## 2. AIRFRAME / BODY TUBE MATERIALS

| Material | Density (g/cm³) | Tensile strength (MPa) | Elastic modulus (GPa) | Cost | Workability | Failure mode | Rating |
|---|---|---|---|---|---|---|---|
| **Kraft paper tube** | ~0.7 | 20–40 (axial) | 2–4 | ₹80–200/tube | Trivial — cut with a hobby knife | **Splits** | ✅ |
| **Phenolic tube** | 1.3–1.4 | 60–100 | 6–10 | ₹400–900/tube | Easy to cut and sand | **Splits / delaminates** | ✅ |
| **Fibreglass (G10/GRP) tube** | 1.8–2.0 | 200–300 | 15–25 | ₹800–2,000/tube | Needs carbide tools, dusty | Splinters | 🟡 |
| **Carbon fibre tube** | 1.5–1.6 | 600–1,200 | 70–150 | ₹1,500–5,000/tube | Hard on tools, conductive, dusty | **Catastrophic shatter** | ❌ |
| **Aluminium 6061-T6** | 2.70 | 310 | 69 | ₹500–1,200/m | Machinable, weldable | Dents then tears | 🟡 |
| **Aluminium 6082-T6** | 2.70 | 310 | 70 | ₹500–1,200/m | Similar to 6061 | Dents then tears | 🟡 |
| **Mild steel** | 7.85 | 400–550 | 200 | ₹150–400/m | Easy to weld and machine | Yields then tears | 🟡 |
| **PVC pipe** | 1.4 | 40–55 | 2.4–3.0 | ₹60–250/m | Trivial | 🔴 **SHATTERS INTO SHRAPNEL** | ❌ |

### 🔴 The PVC question — read this

PVC is the amateur default because it is cheap and available. **It is also the most dangerous common
choice for a motor casing.** PVC does not yield or split — it **fragments**, producing high-velocity
shards.

| | Paper / phenolic | PVC |
|---|---|---|
| Failure mode | **Splits along the length** | **Shatters into fragments** |
| Fragment energy | Low (light material, contained split) | High (dense, sharp shards) |
| Repairable | Sometimes | No |

> **For our first motors, use kraft paper or phenolic.** At 24 mm and ~3 MPa, paper is genuinely
> adequate as a casing, and it fails in the safest possible way. PVC's only advantage is
> availability, and it is not worth the difference in failure mode.

---

## 3. FIN MATERIALS

| Material | Density (g/cm³) | Strength (MPa) | Cost | Notes | Rating |
|---|---|---|---|---|---|
| **Balsa** | 0.10–0.20 | 10–20 | ₹150/sheet | Very light, needs hardening (CA or epoxy) for anything fast | ✅ small rockets |
| **Aircraft plywood (3 mm)** | 0.6–0.8 | 40–60 | ₹200/sheet | **The workhorse fin material.** Through-the-wall mountable | ✅ |
| **G10 fibreglass sheet (2–3 mm)** | 1.8–2.0 | 200–300 | ₹700/sheet | Excellent stiffness and strength, dust hazard | 🟡 |
| **Aluminium (1.5–2 mm)** | 2.70 | 310 | ₹300/sheet | Strong, but heavy and bends permanently | 🟡 |
| **Polycarbonate** | 1.20 | 60–70 | ₹400/sheet | Tough, but softens at ~130 °C, flexes | 🟡 |
| **3D printed PLA** | 1.24 | 50 | ₹1,200/kg | ⚠️ **Softens at ~60 °C** — can deform in the sun on the pad | 🟡 |
| **3D printed PETG** | 1.27 | 50 | ₹1,200/kg | ⚠️ Softens at ~80 °C — **preferred over PLA** | ✅ |

> **Fin flutter** is the failure mode that matters. It scales with span³ and inversely with
> thickness³ — **a slightly thicker fin is dramatically more flutter-resistant.** See
> `Stability_and_Aerodynamics.md`.

---

## 4. NOSE CONE MATERIALS

| Material | Cost | Method | Rating |
|---|---|---|---|
| **Balsa** | ₹200/block | Turn on a lathe or sand to shape | ✅ |
| **Polystyrene foam** | ₹300/block | Hot-wire cut, then glass or coat | 🟡 |
| **3D printed PETG** | ₹50–150 | Print | ✅ **preferred for repeatability** |
| **Fibreglass over foam** | ₹600 | Layup over a foam plug, dissolve the foam | 🟡 |

> ⚠️ The competition requires the payload bay to be ≤ **15 cm diameter × 40 cm height** and the
> payload to separate at apogee — so the nose cone is the most likely separation point. Design the
> joint before you design the cone.

---

## 5. NOZZLE MATERIALS

| Material | Max service temp | Erosion resistance | Cost | Machinability | Rating |
|---|---|---|---|---|---|
| **Graphite** | ~3,000 °C (sublimes) | **Excellent** | ₹800/rod | Machines easily but **chips**; dust is conductive | ✅ **best** |
| **Clay / kitty litter** | ~1,200 °C | Poor — erodes | ₹100 | Cast in place | ✅ for first motors |
| **Mild steel** | ~1,400 °C | Moderate — erodes | ₹200 | Machinable | 🟡 |
| **Phenolic** | ~200 °C (ablates) | Ablates away | ₹150 | Easy | 🟡 short burns only |

> 🔴 **Throat diameter is a precision feature.** A ±0.1 mm error on a 1.87 mm throat is a **±11%
> change in throat area and chamber pressure.** Graphite drills cleanly if you go slowly; **drill as
> a series of progressively larger holes** rather than straight to size.

---

## 6. MOTOR CASE MATERIALS

### 6.1 Strength at temperature — the data that governs casing design

| Material | Room-temp strength retained | At temperature |
|---|---|---|
| **Aluminium 6061** | **80%** | 150 °C |
| **Mild steel** | 80% of **yield** | 240 °C |
| **Mild steel** | 80% of **ultimate** | 380 °C |

**Melting points:**

| Material | Melting point |
|---|---|
| Aluminium 2024-T3 | 500 °C |
| Aluminium 6061-T6 | 580 °C |
| Stainless steel AISI 301 | 1,400 °C |
| Inconel | 1,400 °C |
| Low-alloy steel | 1,480 °C |
| Mild steel SAE1020 | 1,530 °C |

> ⚠️ These are **half-hour exposure** figures. Rapid heating is less severe, so using half-hour data
> for design is **conservative** — which is what we want.

### 6.2 Casing design rules

> 🔴 **Size casings to burst at no more than 2.5 × MEOP. Absolute minimum design margin: 1.5 ×.**

**Why an upper limit on burst margin?** A thick "boilerplate" casing **stores more energy before it
fails**, so when it does fail, it fails worse. A casing that is just strong enough is *safer* than
one that is enormously over-strength, because it fails earlier and with less energy.

Hoop stress for a thin-walled tube:

$$\sigma_{\theta} = \frac{P D}{2 t} \quad \Rightarrow \quad t = \frac{P D}{2 \sigma_{allow}}$$

- `P` = MEOP · `D` = internal diameter · `t` = wall thickness · `σ_allow` = allowable stress

### 6.3 Thermal protection

| Material | Measured density | Thermal conductivity | Notes |
|---|---|---|---|
| **Kraft / postal paper** | **0.646 g/cm³** | ~0.18 W/m·K (published) | Measured **0.15 mm per layer**. **7 layers had LOWER conductivity than 2 layers** — trapped air between layers adds insulation |
| **Cast polyester resin** | **1.26 g/cm³** | 0.19–0.50 W/m·K | A single **0.11 mm** coating survived torch testing with only discolouration |
| **Silicone** | ~1.1 g/cm³ | ~0.2 W/m·K | Flexible, expensive |

> ⚠️ **The insulation tradeoff nobody expects:** thicker insulation reduces the casing internal
> diameter, which reduces propellant volume and — more importantly — **reduces web thickness, which
> shortens burn duration.** Insulation mass is negligible; the volume penalty is what costs you.

**When no insulation is needed** (all three must hold): burn time < 1 s, low combustion temperature
(nitrate propellants), and a casing material with enough wall thickness at reduced strength.

**Aluminium 6061 diffusivity: 690 × 10⁻⁷ m²/s** — it spreads heat well, giving a lower uniform
temperature. **PVC diffusivity: 3.4 × 10⁻⁷ m²/s** — steep gradient, so the bulk stays cool but the
inner surface gets very hot, which self-limits heat transfer. **PVC begins to decompose
(carbonise) at ~225 °C**, which gives it accidental ablative protection.

---

## 7. ADHESIVES

| Adhesive | Gap fill | Working time | Strength | Notes | Rating |
|---|---|---|---|---|---|
| **Two-part epoxy (30 min)** | Good | 30 min | High | **The default for structural joints.** Measure by weight, not volume | ✅ |
| **Two-part epoxy (5 min)** | Good | 5 min | Medium | Convenient, weaker. Use for tacking, not primary structure | ✅ |
| **Cyanoacrylate (CA)** | None | Seconds | High (brittle) | Great for balsa and tacking. Brittle under shock | ✅ |
| **Hot melt** | Good | ~30 s | Low | Use for mould sealing and temporary joints only | ✅ |
| **Polyurethane (Gorilla-type)** | Good | 20 min | Medium | Foams, needs moisture, messy | 🟡 |
| **PVA / wood glue** | Poor | 30 min | Low | Wood only, not structural | 🟡 |

> ⚠️ **Do not use "adhesive grade" epoxy for pyrolant or high-temperature work.** Where a
> high-grade epoxy is specified (e.g. West System), a general adhesive-grade product is **not a
> substitute.**

**Surface preparation for any structural bond:**
1. **Sand** with 600 grit or finer
2. **Clean** with acetone or lacquer thinner — let it fully evaporate
3. **Bond** within 15 minutes of cleaning
4. **Clamp** and do not disturb until fully cured

---

## 8. RECOVERY MATERIALS

| Material | Density | Temp limit | Cost | Use | Rating |
|---|---|---|---|---|---|
| **Ripstop nylon** | ~0.07 g/cm³ | ~120 °C | ₹300/m | **Main parachute** — the standard choice | ✅ |
| **Kevlar (aramid) cord** | — | **~400 °C** | ₹80/m | **Shock cord near the ejection** — survives the heat | ✅ |
| **Nylon cord** | — | ~120 °C | ₹20/m | Cheaper shock cord, **but melts** — protect it | 🟡 |
| **Elastic (bungee)** | — | ~80 °C | ₹30/m | Absorbs shock, but degrades and loses strength | 🟡 |
| **Mylar / ripstop streamer** | — | ~150 °C | ₹100 | Drogue or small rockets | ✅ |
| **Nomex / fire blanket** | — | ~400 °C | ₹400 | **Protects the parachute from ejection gas** | ✅ |

> 🔴 **The parachute must survive the ejection charge or deployment gas.** Use a Nomex protector or
> wadding, and put Kevlar where the heat is. A melted parachute is a ballistic return.

**Descent rate sizing:**

$$v = \sqrt{\frac{2 m g}{\rho \, C_d \, A}}$$

Use `C_d ≈ 0.75` for a flat circular canopy (conservative), `ρ ≈ 1.2 kg/m³`, and solve for the
canopy diameter that gives **≈ 3.5 m/s** — the middle of the required 2–5 m/s band.

---

## 9. FASTENERS AND HARDWARE

| Item | Spec | Use | Cost | Notes |
|---|---|---|---|---|
| **M3, M4, M5 socket screws** | Stainless or zinc-plated | General assembly | ₹5–15 each | Use nyloc nuts or threadlocker anywhere subject to vibration |
| **Nyloc nuts** | Matching thread | Vibration-critical joints | ₹8 each | **Mandatory** on motor retention and recovery attachment |
| **Threadlocker (Loctite 243)** | Medium strength | Metal-to-metal threads | ₹400/bottle | Do not use on plastic |
| **Blind nuts / rivnuts** | M4–M5 | Threads in thin tube walls | ₹25 each | Much better than a nut you cannot reach |
| **Rail buttons** | 1010 or 1515 rail | Launch guide | ₹150/pair | Preferred over launch lugs for anything above ~500 g |
| **Launch lug** | 6 mm ID | Small rockets | ₹40 | Adequate for the first rockets |
| **Shock cord anchors** | Plywood bulkhead + Kevlar | Recovery attachment | — | **Over-specify.** This is a single-point failure |
| **Ball bearing** | Hardened steel | Load-cell load application point | ₹20 | Epoxied into the DIY load cell |

---

## 10. INDIAN SOURCING

| Material | Where | Notes |
|---|---|---|
| Kraft paper tube | Local stationery/paper merchants; online hobby suppliers | Ask for heavy-wall postal tube |
| Phenolic tube | Online composites suppliers | Import or domestic composite shops |
| Plywood (aircraft) | Model/hobby shops; timber merchants | Ask for **birch aircraft ply**, not construction ply |
| G10 / fibreglass sheet | Online composites suppliers | Dust hazard — cut wet or with extraction |
| Carbon fibre | Online composites suppliers | Not recommended yet |
| Aluminium tube/rod | Local metal merchants (SP Road area, Peenya) | **Ask for the alloy and temper** — 6061-T6, not generic "aluminium" |
| Mild steel tube | Local metal merchants | EMT conduit is cheap and adequate for the test stand |
| Copper tubing + flare fittings | **Refrigeration / AC spares shops** | Far cheaper than industrial suppliers for identical parts |
| Graphite rod | Online industrial suppliers; die-sinking suppliers | Ask for fine-grain, high-density graphite |
| PVC pipe | Any hardware shop | ⚠️ Avoid for motor casings |
| Epoxy | Local hardware; marine suppliers | West System and similar are high grade |
| Ripstop nylon | Fabric shops; online | Ask for ripstop, not plain nylon |
| Kevlar cord | Online (kite/parachute suppliers) | Sold as shock cord or kite line |
| Nyloc nuts, screws | Local hardware (SP Road) | Buy in boxes, not singly |
| 3D printing filament | Online | **PETG, not PLA** |

### 10.1 Sourcing rules

1. **Buy spares of anything cheap.** A ₹25 part that fails costs you a test day.
2. **Ask for the alloy and temper** on any metal. "Aluminium" is not a specification.
3. **Keep every invoice** — the competition requires a BOM with estimate vs actual.
4. **Photograph the label** of any certified or precision material.
5. **Do not buy pressure-bearing material without knowing its grade.** This is the one place where
   guessing is genuinely dangerous.

---

## 11. QUALITY CHECKS ON RECEIPT

Before anything enters the workshop:

- [ ] **Dimensions verified** with calipers against the order (tube ID/OD/wall, sheet thickness)
- [ ] **Material grade confirmed** — alloy and temper for metals; do not accept "aluminium"
- [ ] **Visual inspection** — no dents, kinks, cracks, delamination, or corrosion
- [ ] **Tube straightness checked** by rolling on a flat surface
- [ ] **Quantity counted** against the invoice
- [ ] **Recorded** in the BOM workbook with supplier and date
- [ ] **Stored properly** — metals off the floor, composites flat and dry, propellant chemicals
      separated and locked

---

## 12. WHAT WE ACTUALLY NEED FOR THE FIRST ROCKET

Keeping it minimal and cheap:

| Item | Qty | Approx cost |
|---|---|---|
| Kraft paper tube, 40 mm OD | 3 | ₹500 |
| Aircraft plywood 3 mm (fins + centring rings + bulkheads) | 1 sheet | ₹250 |
| Balsa block (nose cone) or PETG filament | 1 | ₹200 |
| Epoxy (30 min, two-part) | 1 | ₹450 |
| CA glue | 1 | ₹150 |
| Kevlar shock cord, 3 m | 1 | ₹250 |
| Ripstop nylon (parachute) | 1 m | ₹300 |
| Nomex / fire blanket piece | 1 | ₹200 |
| Nyloc nuts + M3/M4 screws assortment | 1 set | ₹400 |
| Rail buttons or launch lug | 1 set | ₹200 |
| Fluorescent paint (mandatory colour) | 1 | ₹350 |
| **TOTAL** | | **≈ ₹3,250** |

**Three airframes for ≈ ₹3,250.** This is why the first flights are affordable — and why the club
should fly three progressively harder rockets before spending on anything else.

---

## 13. SOURCES

- `Technical_Reference_Nakka.md` §1.12 (grain mechanical properties) and §2.3 (casing rules)
- `80_REFERENCE/nakka-technical-reference.md` and `80_REFERENCE/nakka_source_text/` — particularly
  `therm.txt` (thermal properties, strength at temperature, melting points, insulation measurements)
  and `casebond.txt` (elastic moduli, casing mass comparison)
- Standard handbook values for steel, aluminium, and polymer properties
- Indian pricing is indicative for 2026 and must be verified before purchase
