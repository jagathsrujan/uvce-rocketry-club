# 05 — Avionics Path

**Flight computer, sensors, telemetry, and the ground station.**

| | |
|---|---|
| **Time** | Foundation 3 weeks · Working 6–10 weeks · Advanced months |
| **Prerequisites** | [`01_Start_Here.md`](<01_Start_Here.md>) |
| **Cost** | ₹0 to learn on a breadboard. ~₹12,000 for the test-stand kit. |
| **You will need** | A laptop and about ₹1,500 of starter electronics |
| **Workspace docs** | [`../30_AVIONICS/`](<../30_AVIONICS/Flight_Computer_Architecture.md>) |

> **The club's hardest role to fill.** If you can write code *or* solder *or* debug a circuit, you are
> more valuable here than anywhere else. Both skills together is rare — one is enough to start.
>
> **Avionics is also the largest single workload.** The competition demands a flight computer, 5+
> sensors, 1 Hz telemetry, real-time ground station plotting, SD redundancy, a state machine, and an
> independent backup deployment chain. That is genuinely two people's work.

---

## FOUNDATION (3 weeks)

### Learn

1. **Electronics basics** — voltage, current, resistance, Ohm's law, and why a short circuit matters.
2. **What a microcontroller is** — a small computer with pins you can read and write.
3. **Digital vs analog** — a button is digital (on/off); a temperature sensor may be analog (a
   voltage that varies).
4. **The three sensor interfaces** — analog, I²C, SPI. When to use which.
5. **PWM** — how you make a microcontroller dim an LED or move a servo.
6. **Serial communication** — how your board talks to your laptop, and how you debug.

### Do

You will need a starter kit: an **ESP32 or Arduino Nano**, a breadboard, jumper wires, a couple of
LEDs, resistors, and a push button. **≈ ₹1,500.**

| # | Exercise | What it teaches |
|---|---|---|
| 1 | Blink an LED | That your toolchain works |
| 2 | Read a button, light an LED | Digital input |
| 3 | Read a potentiometer, print the value | Analog input, and that analog is noisy |
| 4 | Drive a servo to a commanded angle | PWM and actuators |
| 5 | Read a BMP280 or BMP390 barometer over I²C, print pressure | Real sensor, real protocol |
| 6 | Log those readings to a CSV on your laptop | Data capture — the actual job |

> **Exercise 5 is the moment it clicks for most people.** You are reading the same quantity the
> flight computer reads, and you can hold it in your hand.

### Checkpoint — you can:

- [ ] Explain Ohm's law and use it to size a resistor for an LED
- [ ] Explain the difference between analog, I²C and SPI, and name a sensor for each
- [ ] Read a sensor and log the data to a file
- [ ] Debug a circuit that is not working, methodically rather than randomly
- [ ] Explain why analog readings near a firing motor are noisy

---

## WORKING (6–10 weeks)

### Learn

1. **Sensor specifics** — barometer (range, resolution, why you must zero it at the pad), IMU
   (accelerometer ranges, gyro drift, calibration), GNSS (fix time, NavIC support, antenna placement).
2. **The load cell and strain gauges** — bridge configuration, excitation, amplification, calibration
   with known masses. This is the instrumentation that measures motor thrust.
3. **Pressure measurement** — transducer types, protective plumbing, why **flare fittings not
   compression**, and why the sensor inlet is packed with grease.
4. **Data acquisition** — sample rate, anti-aliasing, and why 100 samples/second is right for chamber
   pressure.
5. **State machines** — the flight software states, launch detection, apogee detection, and how to
   survive a processor reset.
6. **Reliability** — watchdog timers, brown-out detection, and designing for the failures you cannot
   prevent.

### Do — this is the important part

**Build the test stand instrumentation first.** Not the flight computer. Here is why:

| Reason | |
|---|---|
| **It is the critical path** | The propulsion team cannot finish the motor design without measured burn rate, which needs the strand burner, which needs instrumentation |
| **It is simpler** | A load cell and a pressure transducer are far less demanding than a flight computer with a telemetry link |
| **It teaches everything** | Sensors, ADC, amplification, calibration, logging, noise — the same skills the flight computer needs |
| **It produces visible results fast** | You will have a working thrust curve within weeks, which is motivating and demonstrable |

| # | Build | Skills |
|---|---|---|
| 1 | Load cell + HX711 or INA122 amplifier + logger | Bridge circuits, amplification, calibration with known masses |
| 2 | Pressure transducer + protective plumbing + logger | Analog signal conditioning, safety-critical plumbing |
| 3 | Calibration procedure with known masses | Metrology — and why uncalibrated data is worthless |
| 4 | **First static fire data capture** | The whole chain working under real conditions |
| 5 | Telemetry link — two radios, send a packet | RF, packet framing, link budget |
| 6 | Ground station — receive, parse, plot live, write CSV | Software, real-time display, the required telemetry format |

### Checkpoint — you can:

- [ ] Calibrate a load cell with known masses and verify linearity
- [ ] Capture a thrust curve from a real static fire
- [ ] Explain why the pressure sensor is protected by copper tubing and grease
- [ ] Send a telemetry packet over a radio link and decode it on a laptop
- [ ] Produce a CSV in the exact required competition format
- [ ] Explain what a watchdog timer does and why the flight computer needs one

---

## ADVANCED (months)

- **PCB design** — move from breadboard to a real board in KiCad
- **Sensor fusion** — complementary filter, then a Kalman filter, fusing barometer and accelerometer
- **RF properly** — link budgets, antenna design, interference mitigation, why rocket and payload need
  separate channels
- **Redundant deployment chains** — the independent COTS backup altimeter, and how to verify it works
  when the primary is disabled
- **Embedded C** — moving beyond Arduino libraries to direct register control
- **Vibration and thermal testing** — qualifying your electronics for the flight environment

### Checkpoint — you can:

- [ ] Design and order a working PCB
- [ ] Implement and tune a Kalman filter for altitude and velocity
- [ ] Compute a link budget and justify your antenna choice
- [ ] Prove your backup deployment chain works with the primary disabled
- [ ] Teach the Foundation tier to a new member

---

## First build

**The test stand instrumentation package.**

| Step | Output | Cost |
|---|---|---|
| 1 | Load cell (commercial 500 kg S-beam, or DIY bending beam) | ₹300–2,500 |
| 2 | Amplifier — INA122 circuit, or HX711 module | ₹450–900 |
| 3 | Pressure transducer + copper tubing + **flare** fittings + grease | ₹4,000 |
| 4 | DAQ — Arduino + ADS1115 (16-bit) + SD logger | ₹1,200 |
| 5 | Calibration with known masses | ₹0 |
| 6 | Enclosure and wiring | ₹500 |

**≈ ₹7,000–12,000** depending on whether you build the load cell. Full parts list in
[`../30_AVIONICS/Electronics_BOM_and_Sourcing.md`](<../30_AVIONICS/Electronics_BOM_and_Sourcing.md>)
Tier (c).

> 💡 **Strategy note from the source:** for a **new motor design**, measuring **chamber pressure only**
> is a good approach, because it avoids destroying an expensive load cell if the motor
> over-pressurises. Start with pressure.

---

## Resources

| Resource | Cost | What it is good for |
|---|---|---|
| [Arduino Learn](https://docs.arduino.cc/learn/) | Free | Official tutorials. Start at the beginning. |
| [Adafruit Learning System](https://learn.adafruit.com/) | Free | **The best sensor tutorials anywhere.** Every breakout board has a guide. |
| [SparkFun Tutorials](https://learn.sparkfun.com/tutorials) | Free | Excellent on the fundamentals — voltage, current, I²C, SPI, serial |
| [BPS.space](https://www.bps.space/) + Joe Barnard's YouTube | Free | **Watch everything he has made.** The best practical amateur avionics content in existence. Actual flight computers, actual failures, actual fixes. |
| [KiCad](https://www.kicad.org/) | Free | PCB design, when you get there |
| [`../30_AVIONICS/Flight_Computer_Architecture.md`](<../30_AVIONICS/Flight_Computer_Architecture.md>) | Free | Our own architecture and component choices |
| [`../30_AVIONICS/Sensors_and_Instrumentation.md`](<../30_AVIONICS/Sensors_and_Instrumentation.md>) | Free | Every sensor, calibration, load cell theory |
| [`../30_AVIONICS/Communications_and_Ground_Station.md`](<../30_AVIONICS/Communications_and_Ground_Station.md>) | Free | Radios, link budget, telemetry format |
| [`../30_AVIONICS/Recovery_Electronics_and_Control.md`](<../30_AVIONICS/Recovery_Electronics_and_Control.md>) | Free | **No-pyro deployment**, apogee detection, servos |

### Books (later)

| Book | Why |
|---|---|
| *The Art of Electronics* — Horowitz & Hill | The bible. Expensive (~₹5,000). The club should own one copy, not each member. |
| *Making Embedded Systems* — Elecia White | How to structure firmware properly |
| *Practical Electronics for Inventors* — Scherz & Monk | Friendlier than Horowitz & Hill, good for self-study |

### India-specific sourcing

| Source | Best for |
|---|---|
| **SP Road, Bengaluru** | Passive components, wire, connectors, soldering gear, multimeters. Cheapest. Go in person. |
| **Robu.in** | Microcontroller boards, sensors, servos, radio modules |
| **Element14 / Mouser / Digi-Key India** | Genuine ICs, precision parts. **No counterfeits.** Higher price, longer lead time. |
| **IndiaMART / industrial market** | Pressure transducers, load cells, copper tubing, flare fittings |

> ⚠️ **Counterfeit warning:** IMU and barometer breakout boards are among the most counterfeited
> parts in India. **Read the WHO_AM_I register** on any IMU before trusting it — every genuine part
> returns a documented value. Avoid implausibly cheap marketplace listings. Full guidance in
> [`../30_AVIONICS/Electronics_BOM_and_Sourcing.md`](<../30_AVIONICS/Electronics_BOM_and_Sourcing.md>).

---

## What NOT to do

| ❌ | Why |
|---|---|
| Start with the flight computer | Build the test stand instrumentation first — it is needed sooner and teaches the same skills |
| Trust a sensor without calibrating it | Uncalibrated data is worthless for performance analysis |
| Use an MPU6050 | Obsolete, and its clones are notoriously unreliable. Use ICM-20948 or BMI088. |
| Use LiPo batteries | **Prohibited by competition rules.** Li-ion must be metal-cased (18650). |
| Use spring contacts for batteries | **Prohibited by rules** — shock causes momentary disconnects. Solder or screw terminals. |
| Share a ground between the deployment chain and the flight computer | The two chains must be fully independent |
| Ignore the brown-out risk from servo stall | A stalled servo can draw 1–2 A and reset your flight computer at the worst moment |
| Build a PCB before it works on a breadboard | Debug on the breadboard, then commit to copper |
