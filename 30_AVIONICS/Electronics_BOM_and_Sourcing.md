# Electronics BOM and Sourcing (India)

**UVCE Rocketry Club — Avionics Guide 5**

| | |
|---|---|
| **Document** | `30_AVIONICS/Electronics_BOM_and_Sourcing.md` |
| **Currency** | Indian Rupees (₹). USD converted at ≈ ₹88/USD where the source price is in USD. |
| **Status** | 🟡 Indicative 2026 planning figures, not quotations. Verify before ordering. |
| **Companion documents** | `Flight_Computer_Architecture.md`, `Sensors_and_Instrumentation.md`, `Communications_and_Ground_Station.md`, `Recovery_Electronics_and_Control.md` |

> **Priority key:** 🔴 **MUST** have for first static fire · 🟠 **SHOULD** have · 🟢 **NICE** to have

---

## TIER (c) — STATIC TEST STAND INSTRUMENTATION ⭐ START HERE

**This is the tier to buy first.** The static test stand is the club's highest-value build: it is
cheap, it is workbench-scale, it produces real measured data within weeks, and it directly unblocks
the motor design (the burn-rate coefficient).

> 💡 **Strategy note from Nakka:** for **new motor designs**, measuring **chamber pressure only** is a
> good strategy, because it avoids destroying an expensive load cell if the motor over-pressurises
> and blows out the nozzle or bulkhead. Start with pressure; add thrust measurement once the motor
> is no longer a CATO risk.

### c.1 Chamber pressure measurement

| # | Item | Spec | Qty | Unit ₹ | Total ₹ | Source | Pri |
|---|---|---|---|---|---|---|---|
| c1 | Pressure transducer | 0–10 MPa (0–1450 psi), strain-gauge type, 0–5 V or 4–20 mA output | 1 | 3,500 | 3,500 | Industrial instrumentation suppliers; IndiaMART; automation dealers | 🔴 |
| c2 | Analogue pressure gauge | 0–10 MPa (or 0–1500 psi), glycerine-filled, 63 mm dial | 1 | 900 | 900 | Local industrial/hardware market | 🔴 |
| c3 | Copper tubing | 1/4 in OD refrigeration-grade copper, 1 m | 1 | 250 | 250 | Refrigeration/AC spares shop | 🔴 |
| c4 | **Flare fittings** | 1/4 in NPT male adapter, flare nuts, female flare adapter, Tee | set | 800 | 800 | Refrigeration/AC spares shop | 🔴 |
| c5 | Flaring tool | 1/4 in flaring tool kit | 1 | 900 | 900 | Tool suppliers | 🔴 |
| c6 | Steel wool | Medium grade — used as an inline filter | 1 | 80 | 80 | Local hardware | 🔴 |
| c7 | PTFE tape + pipe sealant | For NPT threads only | 1 | 150 | 150 | Local hardware | 🔴 |
| c8 | Grease | Silicone or high-temp grease, to pack the sensor inlet port | 1 | 250 | 250 | Local hardware | 🔴 |

**Subtotal (pressure only): ≈ ₹6,830**

#### Why the plumbing matters (do not skip this)

| Design element | Reason |
|---|---|
| **A length of copper tubing between motor and sensor** | The **cool trapped air in the tube compresses on firing and isolates the sensor from the hot gas**, and the copper absorbs heat. Without this the sensor is destroyed. |
| **Pack the sensor inlet port with grease** | Protects the element from hot corrosive gas and keeps it cool. **A heated pressure sensor may give erroneous readings.** |
| **Flare fittings, NOT compression fittings** | The source is emphatic: *"In the aerospace field, flare fittings are used exclusively."* Compression fittings are simpler but flare is far more reliable and leak-free, and is reusable. |
| **A small ball of steel wool in the bulkhead hole** | Acts as a filter. Without it, liquid residue cools, solidifies and **blocks the line**, destroying the measurement. |
| **A full loop bent into the copper tube** | Gives compactness and flexibility, and accommodates thermal expansion. |
| **Teflon tape only on NPT threads** | Never on the flare faces — it will prevent the flare sealing. |

### c.2 Thrust measurement

| # | Item | Spec | Qty | Unit ₹ | Total ₹ | Source | Pri |
|---|---|---|---|---|---|---|---|
| c9 | **Option A:** Commercial load cell | 500 kg S-beam (or 50 kg for small motors), with mounting | 1 | 2,500 | 2,500 | IndiaMART; weighing-scale suppliers | 🟠 |
| c10 | **Option B:** DIY bending-beam load cell | Aluminium 6061 block; see §c.3 | 1 | 300 | 300 | Local metal supplier | 🟠 |
| c11 | Strain gauges (no leads) | **OMEGA SG-3/350-LY43** — 350 Ω, Constantan foil, phenol backing, 3 mm grid, self-temp-compensated for aluminium, −10 to 70 °C, GF 2.06, 2% strain limit. ≈$45/pack of 10 | 1 pack | 4,000 | 4,000 | OMEGA or authorised distributor | 🟠 |
| c12 | Strain gauges (with leads) | **KFG-5-120-C1-11L1M2R** — same family, pre-attached leads. ≈$59/pack of 10 | 1 pack | 5,200 | 5,200 | Distributor | 🟢 |
| c13 | Instrumentation amplifier | **INA122** — Digi-Key **INA122PA-ND** | 2 | 450 | 900 | Mouser/Digi-Key India; Robu.in; Element14 | 🔴 |
| c14 | +5 V regulator | **LM78L05ACZFS-ND** | 2 | 25 | 50 | Local electronics (SP Road, Bengaluru) | 🔴 |
| c15 | −5 V regulator | **LM320LZ-5.0-ND** | 2 | 40 | 80 | Local electronics | 🔴 |
| c16 | Capacitor 1.0 µF | **P2105-ND** | 4 | 15 | 60 | Local electronics | 🔴 |
| c17 | Switch | **SW102-ND** or equivalent DPST | 2 | 60 | 120 | Local electronics | 🔴 |
| c18 | 9 V battery straps | **2243K-ND** | 4 | 30 | 120 | Local electronics | 🔴 |
| c19 | 9 V batteries | Alkaline | 4 | 60 | 240 | Anywhere | 🔴 |
| c20 | Resistor kit | For R_G (gain) and bridge balancing — 1% metal film assortment | 1 | 300 | 300 | Local electronics | 🔴 |
| c21 | Perfboard / stripboard | | 3 | 60 | 180 | Local electronics | 🔴 |
| c22 | 30 AWG wire-wrap wire | For soldering to gauges without leads | 1 | 250 | 250 | Local electronics | 🔴 |
| c23 | Soldering iron + fine tip | Temperature controlled | 1 | 900 | 900 | Local electronics | 🔴 |
| c24 | Digital multimeter | With resistance and mV ranges | 1 | 800 | 800 | Local electronics | 🔴 |

**Subtotal (thrust, Option A): ≈ ₹10,700** · **(Option B, DIY cell + gauges): ≈ ₹8,500**

### c.3 The DIY bending-beam load cell — why it is worth building

A metal block with **one hole drilled through and a slit cut on one side**, creating a bending
"bridge" on the opposite side where the strain gauges are bonded.

**Key advantage (from the source):** the **total displacement under load is very small**, which
*"nearly eliminate[s] unwanted dynamic effects associated with mass and large displacement (e.g.
spring) systems."* This is a direct lesson — Nakka's earlier spring-restrained rig suffered **severe
underdamped oscillation** and needed a **hydraulic damper** to fix it. A stiff bending beam avoids
the problem entirely.

#### Mandatory geometric limits

$$B/3 \le D \le 2B/3 \qquad B \le H \le 1.75B \qquad B/8 \le t \le B/2 \qquad b \ge B/2$$

- `B` = body width · `t` = thickness · `D` = hole diameter
- `b` = load location · `e` = hole location

#### Stress and strain limits

| Rule | Value |
|---|---|
| Design maximum body stress | **≈ half the yield stress** (avoids permanent strain ruining calibration, preserves linearity) |
| Maximum gauge strain | **< 2000 microstrain** |
| Target gauge strain | **1500 microstrain** |
| **The body is always the limit, never the gauge** | A foil gauge tolerates 1% strain or more — at least double what a steel or aluminium body can take |

#### Construction notes

- Design around material you can actually get.
- **Drill the body hole as a series of progressively larger holes** — drilling straight to size lets
  the location drift.
- The slot is simply **cut with a hacksaw**.
- A **hardened steel ball bearing is epoxied in** to precisely define the load application point; it
  can be removed later by moderate heating to soften the epoxy.
- **Bonding:** sand with 600 grit or finer, clean with acetone or lacquer thinner, bond with
  cyanoacrylate or epoxy (epoxy is easier and perhaps more reliable).
- **Active gauges: grid lines parallel to the long edge.** Passive gauges: grid lines
  **perpendicular** to the active gauges.
- **Cover the bonded gauge with a protective epoxy layer**, immersing part of the leads.
- A prototype 250 lb (1100 N) cell in 6061 aluminium had a measured **maximum deflection of just
  0.0035 in (0.09 mm)** at full load.

#### Gauge arrangements

| Arrangement | Sensitivity | Notes |
|---|---|---|
| Single gauge | 1× | Simplest, most temperature-sensitive |
| **Two side-by-side** | 2× | Double the output — good compromise |
| **Full bridge (4 gauges, 2 active + 2 passive)** | Best | Excellent sensitivity, and **minimises adverse temperature effects** if all four are mounted in close proximity |

### c.4 The amplifier circuit — exact design

Four gauges in a **Wheatstone bridge**, feeding an **INA122 instrumentation amplifier**, output to an
A/D converter. Powered from **two 9 V batteries** with **+5 V and −5 V regulators** and a single DPST
switch.

#### Gain calculation procedure

1. Compute the maximum gauge strain.
2. Bridge output: $e = \dfrac{E}{4} \cdot GF \cdot (\varepsilon_1 - \varepsilon_2 + \varepsilon_3 - \varepsilon_4)$
   where `E` = excitation voltage and `GF` = gauge factor.
3. Required gain: $G = V_o / e$
4. Read `R_G` from the INA122 datasheet for that gain.

#### Worked example (200 lb cell — use as your template)

| Step | Value |
|---|---|
| Maximum gauge strain | 1778 microstrain |
| Gauge factor | 2.06 |
| Excitation `E` | 5.0 V |
| Passive gauges (SG2, SG4) strain | always zero |
| Bridge maximum output `e` | **0.009157 V** |
| Chosen output range | 0 to +5 V |
| **Required gain `G`** | **5.0 / 0.009157 = 546** |
| `R_G` | from the INA122 datasheet at G = 546 |

**Bridge balance:** ideally the bridge reads zero at zero strain. In reality a small output of
either polarity appears due to gauge resistance differences. **Simply zero it in the analysis
software**, or fit balancing resistors in the bridge.

### c.5 Data acquisition

| # | Item | Spec | Qty | Unit ₹ | Total ₹ | Source | Pri |
|---|---|---|---|---|---|---|---|
| c25 | **DATAQ DI-154RS** | 4-channel, 12-bit, up to **250 samples/second**, with WINDAQ software | 1 | 9,000 | 9,000 | DATAQ direct (import) | 🟠 |
| c26 | **DATAQ DI-194RS** (alt) | Lower cost, 4-channel, 10-bit | 1 | 4,500 | 4,500 | DATAQ direct (import) | 🟢 |
| c27 | **Alternative:** Arduino + SD logger | 16-bit external ADC (ADS1115) + micro-SD, custom firmware | 1 | 1,200 | 1,200 | Local electronics | 🟠 |
| c28 | Laptop | Any working laptop with USB | 1 | — | — | already available | 🔴 |

> 💡 **Sampling rate guidance from the source: 100 samples per second is right for chamber
> pressure.** Higher rates produce "noisy" data that then needs software filtering. Video at 30 fps
> is also "perfectly fine."

> 💡 **The Arduino + ADS1115 route (c27) is the best value for this club.** It costs a fraction of a
> DATAQ, it is a legitimate learning project, and it doubles as the basis of the flight computer.
> Weigh the time cost against the money saved.

### c.6 Test stand structure and safety

| # | Item | Spec | Qty | Unit ₹ | Total ₹ | Source | Pri |
|---|---|---|---|---|---|---|---|
| c29 | Steel tube (EMT or conduit) | For the tripod legs, thrust struts, cross beams, leg braces | ~6 m | 150/m | 900 | Local metal/hardware | 🔴 |
| c30 | Base plate | 6 mm steel or aluminium, 120 mm triangular | 1 | 400 | 400 | Local metal | 🔴 |
| c31 | Bolts and nuts | 1/4 in structural bolts + #10 machine screws | set | 500 | 500 | Local hardware | 🔴 |
| c32 | Tension rods / turnbuckles | 1/8 in steel rod, or eyebolts + turnbuckles | 3 | 120 | 360 | Local hardware | 🟠 |
| c33 | Hardwood motor guides ("mushroom plugs") | Drilled to take the motor mount fasteners | 2 | 100 | 200 | Local hardware | 🔴 |
| c34 | **Plywood blast shield** | 12 mm plywood, for the hydrostatic proof test | 1 | 500 | 500 | Local hardware | 🔴 |
| c35 | Heavy backstop | Steel plate or concrete block — the motor must not be able to tip toward the crew | 1 | 1,500 | 1,500 | Local metal/scrap | 🔴 |
| c36 | Ignition cable | 2-core, 100 m | 1 | 2,500 | 2,500 | Local electrical | 🔴 |
| c37 | Relay / MOSFET + ignition box | With interlock, continuity check, and audible click | 1 | 1,500 | 1,500 | Local electronics | 🔴 |

**Subtotal (structure + safety): ≈ ₹8,860**

### TIER (c) TOTAL

| Configuration | Total ₹ |
|---|---|
| **Minimum viable: pressure only** | **≈ 6,830** |
| Pressure + DIY thrust cell + Arduino DAQ + structure | **≈ 27,000** |
| Full: pressure + commercial load cell + DATAQ + structure | **≈ 38,000** |

---

## TIER (a) — MINIMUM VIABLE FLIGHT COMPUTER

| # | Item | Spec | Qty | Unit ₹ | Total ₹ | Source | Pri |
|---|---|---|---|---|---|---|---|
| a1 | Microcontroller | ESP32 dev board (WiFi/BT, dual core, 12-bit ADC) | 2 | 450 | 900 | Robu.in, SP Road | 🔴 |
| a2 | Barometer | **BMP390** or **MS5611** (BMP280 is adequate; MS5611 has better resolution) | 2 | 600 | 1,200 | Robu.in, Element14 | 🔴 |
| a3 | IMU | **ICM-20948** or **BMI088**. ⚠️ Avoid MPU6050 — obsolete and its clones are notoriously unreliable | 2 | 700 | 1,400 | Robu.in, Mouser | 🔴 |
| a4 | GNSS module | With **NavIC/IRNSS** support if available; u-blox NEO-M9N or similar | 1 | 2,200 | 2,200 | Robu.in, Element14 | 🟠 |
| a5 | Micro-SD module + card | SPI interface, 8 GB card (FAT32) | 2 | 350 | 700 | Local electronics | 🔴 |
| a6 | Battery | **Li-ion 18650** (metal-cased) + holder. ⚠️ **LiPo is PROHIBITED by the rules** | 4 | 250 | 1,000 | Local electronics | 🔴 |
| a7 | Battery holder | 18650 holder, **screwed terminals — not spring contacts** (rules prohibit spring contacts) | 2 | 80 | 160 | Local electronics | 🔴 |
| a8 | Regulator | Buck converter 5 V/3 A + LDO for clean analog rail | 3 | 120 | 360 | Local electronics | 🔴 |
| a9 | COTS backup altimeter | **Independent** altimeter with its own battery and deployment output (e.g. a commercial rocket altimeter) | 1 | 3,500 | 3,500 | Hobby suppliers / import | 🔴 |
| a10 | Servo | Metal-gear, torque per §5 of the recovery guide | 3 | 600 | 1,800 | Robu.in | 🔴 |
| a11 | Passive components | Resistors, capacitors (incl. 1000 µF reservoir), diodes, transistors | kit | 600 | 600 | SP Road | 🔴 |
| a12 | Perfboard / custom PCB | Perfboard first, PCB later | 3 | 100 | 300 | SP Road | 🔴 |
| a13 | Wiring, headers, connectors | JST/Dupont, heat shrink, silicone wire | kit | 700 | 700 | SP Road | 🔴 |
| a14 | 3D printing filament | PETG preferred (better temperature resistance than PLA) | 1 kg | 1,200 | 1,200 | Local/online | 🟠 |
| a15 | Enclosure / avionics sled | 3D printed or fabricated | 1 | 300 | 300 | in-house | 🔴 |

**TIER (a) TOTAL ≈ ₹16,220**

> ⚠️ **Two rules you must not violate:** LiPo batteries are prohibited; Li-ion cells must be
> metal-cased like 18650s. And **spring contacts must not be used** for battery connections, because
> shock can cause momentary disconnects.

---

## TIER (b) — GROUND STATION

| # | Item | Spec | Qty | Unit ₹ | Total ₹ | Source | Pri |
|---|---|---|---|---|---|---|---|
| b1 | Radio pair | **XBee Series 1/2/Pro** or **LoRa SX1278/RFM95**. Rules require XBee/Zigbee or LoRaWAN | 2 | 1,800 | 3,600 | Robu.in, Element14 | 🔴 |
| b2 | Antenna | Quarter-wave whip with ground plane; **elevated** mount | 2 | 500 | 1,000 | Local electronics | 🔴 |
| b3 | USB-serial adapter | FTDI or CP2102 | 2 | 250 | 500 | SP Road | 🔴 |
| b4 | Laptop | ≥ 2 hours battery (rule 5.xii) | 1 | — | — | already available | 🔴 |
| b5 | Antenna mast / tripod | To elevate the ground station antenna | 1 | 1,200 | 1,200 | Local hardware | 🟠 |
| b6 | Portable enclosure | For transportability (rule 5.xiv) | 1 | 800 | 800 | Local hardware | 🟠 |
| b7 | Power bank | For laptop/radio backup | 1 | 1,000 | 1,000 | Local | 🟠 |

**TIER (b) TOTAL ≈ ₹8,100** (excluding the laptop)

---

## TIER (d) — OPTIONAL UPGRADES

| Item | Purpose | Approx ₹ | Pri |
|---|---|---|---|
| Thermocouple + MAX31855 | Motor case temperature during static fire | 1,200 | 🟢 |
| High-speed camera (or phone slow-mo) | Ignition transient, case rupture diagnosis | — | 🟠 |
| Load cell, spare | Because the first one may be destroyed | 2,500 | 🟠 |
| ADS1115 16-bit ADC | Better analog resolution than ESP32 internal ADC | 400 | 🟠 |
| Current sensor (INA219) | Servo and battery current monitoring | 300 | 🟢 |
| Vibration sensor | Structural qualification testing | 800 | 🟢 |
| Vibration/shock test rig | For the 15 g / 30 g structural requirement | 3,000 | 🟢 |
| Second COTS altimeter | True redundancy for the backup chain | 3,500 | 🟠 |

**TIER (d) TOTAL ≈ ₹11,700**

---

## COUNTERFEIT WARNING ⚠️

**IMU and barometer breakout boards are among the most commonly counterfeited electronics in India.**
Cheap modules frequently contain a different (or recycled) chip than the label claims, and fail in
ways that are hard to diagnose.

**How to avoid fakes:**

1. **Buy from authorised distributors** where possible — Element14, Mouser, Digi-Key India, or
   Robu.in for hobby-grade parts. Avoid no-name marketplace listings at implausibly low prices.
2. **Read the WHO_AM_I register** on any IMU before trusting it. Every genuine part returns a
   documented value. If it does not match the datasheet, the chip is not what it claims to be.
3. **Verify the I2C address** matches the datasheet.
4. **Sanity-check the data:** a barometer should read roughly 1013 hPa minus about 12 hPa per 100 m
   of altitude in Bengaluru (≈ 910 hPa at 900 m). An IMU at rest should read about 1 g on one axis
   and near zero on the others.
5. **Buy two of anything critical** and cross-check them against each other on the bench.
6. **Be suspicious of a price far below the distributor price** — it is usually a different chip.

---

## SOURCING NOTES FOR BENGALURU

| Source | Best for | Notes |
|---|---|---|
| **SP Road, Bengaluru** | Passive components, perfboard, wire, connectors, soldering equipment, multimeters | Cheapest for basics. Go in person, buy spares, test before you leave the shop. |
| **Robu.in** | Microcontroller boards, sensors, servos, radio modules | Good hobby-grade selection, reasonable shipping |
| **Element14 / Mouser / Digi-Key India** | Genuine ICs (INA122, regulators), strain gauges, precision parts | Authorised distributors — no counterfeits. Higher prices, longer lead time. |
| **IndiaMART / local industrial market** | Pressure transducers, load cells, copper tubing, flare fittings, steel | For the static test stand. Verify specs in person. |
| **Refrigeration / AC spares shops** | Copper tubing, flare fittings, flaring tools | Much cheaper than industrial suppliers for identical parts |
| **Local hardware** | Steel tube, plywood, fasteners, bolts, grease | The test stand structure |

**General rules:**
- **Buy spares of anything cheap.** A ₹25 regulator that fails on test day costs you the whole day.
- **Buy consumables in bulk** (wire, heat shrink, resistors, bolts) — the per-unit saving is large.
- **Keep every invoice.** The competition requires a complete bill of materials with estimate versus
  actual costs (record these in `00_ADMINISTRATION/BOM_and_Budget.xlsx`).
- **Record the supplier for every part** so you can reorder the exact same item later.
- **Photograph the packaging and label** of any precision part before you install it.

---

## RECOMMENDED PURCHASE ORDER

| Phase | Buy | Approx ₹ | Why |
|---|---|---|---|
| **1. Strand burner + pressure** | c1–c8, c27, c29–c34 | **≈ 12,000** | Unblocks the motor design. Highest value per rupee. |
| **2. Thrust + safety** | c9 or c10–c24, c35–c37 | **≈ 11,000** | Completes the test stand |
| **3. Flight computer** | Tier (a) | **≈ 16,200** | Desk work, heavily graded in competition |
| **4. Ground station** | Tier (b) | **≈ 8,100** | Needed for telemetry scoring |
| **5. Upgrades** | Tier (d) | as funds allow | |

**Phase 1 + 2 ≈ ₹23,000 gets you a fully instrumented static test capability.** That is the single
most important purchase the club will make this year, and it fits comfortably inside even the lean
budget tier.

---

## SOURCES

- Richard Nakka's Experimental Rocketry Site, pages `strainlc.html`, `pressure-measurement.html`,
  `static.html`, `sts5000f.html`, `safety.html` — extracted to
  `80_REFERENCE/nakka-technical-reference.md` and `80_REFERENCE/nakka_source_text/`.
- IN-SPACe Model Rocketry India Student Competition 2026 — Mission Requirements and Competition
  Guidelines (Doc No. IN-SPACe.MR.Model.CG.01, Issue No.1, dtd 24.03.2026). Rules 4.3, 5.xii, 5.xiv,
  5.xv.
- Indian pricing is indicative for 2026 and must be verified with quotations before purchase.
