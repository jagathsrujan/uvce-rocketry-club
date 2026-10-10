# Flight Computer Architecture — UVCE Rocketry Club

**Document:** `30_AVIONICS/Flight_Computer_Architecture.md`
**Rev:** 1.0 · **Status:** Design baseline for PDR
**Target vehicle:** single-stage, commercial IN-SPACe-vendor motor, ≤ 2800 N·s, 1000 m ± 100 m apogee, 1.0 kg CAN-7USAT payload
**Applicable rules:** IN-SPACe Model Rocketry India Student Competition, Doc No. IN-SPACe.MR.Model.CG.01, Issue 1 (Annexure-2 telemetry spec, Ch. 5 vehicle rules, Ch. 7 recovery rules)

> **Companion documents:** [Communications and Ground Station](Communications_and_Ground_Station.md) · [Sensors and Instrumentation](Sensors_and_Instrumentation.md) · [Recovery Electronics and Control](Recovery_Electronics_and_Control.md) · [Electronics BOM and Sourcing](Electronics_BOM_and_Sourcing.md)

---

## 0. How to use this document

| Section | Read it when |
|---|---|
| §1 Requirements | Writing the PDR requirements trace |
| §2 Architecture | Deciding what boards exist and how they interconnect |
| §3 MCU selection | Buying the processor |
| §4 Sensor suite | Buying sensors |
| §5 Power | Sizing the battery, choosing regulators |
| §6 Logging | Writing the SD driver and CSV schema |
| §7 State machine | Writing flight software |
| §8 Watchdog / BOR | Making it survive flight |
| §9 Fusion | Getting altitude and velocity that behave |
| §10 PCB | Layout, or deciding perfboard is fine |
| §11 Budgets | Mass and power budget for PDR |

**Notation:** ✅ = mandatory by rule · ⚠️ = common failure mode · 💡 = practical tip from field experience.

---

## 1. System requirements derived from the competition rules

### 1.1 Traceability table

| ID | Requirement | Source | Verification method |
|---|---|---|---|
| AV-REQ-01 | Telemetry transmitted at **≥ 1 Hz** | Ch. 5 / Annexure-2 | Count packets in ground-station log over a 60 s bench run |
| AV-REQ-02 | Telemetry contains **all 15 mandatory fields** in the exact order of Annexure-2 | Annexure-2 | Byte-compare decoded line against the Annexure-2 template |
| AV-REQ-03 | Field resolutions: altitude 0.1 m, pressure 1 Pa, temperature 0.1 °C, voltage 0.01 V, lat/long 0.0001°, GNSS alt 0.1 m, sats integer, accel m/s², gyro deg/s | Annexure-2 | Inspect formatted output strings; unit test the formatter |
| AV-REQ-04 | ASCII comma-separated, terminated by **carriage return** | Annexure-2 | Hex dump of serial output shows `0x0D` terminator |
| AV-REQ-05 | Redundant **onboard micro-SD logging in .csv** | Ch. 5 | Remove card after flight, open in Excel/LibreOffice, count rows |
| AV-REQ-06 | **Independent COTS backup altimeter** wired to a redundant deployment chain | Rule 5.xv | Two physically independent deployment paths documented in CDR; teams without this **are not permitted to launch** |
| AV-REQ-07 | Flight software state must be **telemetered** and must be **recoverable after processor reset** | Ch. 5 | Reset injection test: pull NRST mid-`ASCENT`, confirm state and clock continuity |
| AV-REQ-08 | Mission clock must **survive reset** | Ch. 5 | Same test as above; timestamp must continue, not restart at 0 |
| AV-REQ-09 | **RF command to switch telemetry ON/OFF**; rocket must not transmit until commanded | Ch. 5 | Demonstrated to the Jury |
| AV-REQ-10 | NETID/PANID = **team number**, declared at CDR | Ch. 5 | Screenshot of XBee configuration in CDR annex |
| AV-REQ-11 | **Separate channels** for rocket and CAN-7USAT payload | Ch. 5 | Channel plan table in CDR + interference test log |
| AV-REQ-12 | Battery must survive **≥ 30 min of pad wait with margin** | Ch. 5 | 45 min soak test on the pad, voltage logged every 10 s |
| AV-REQ-13 | **LiPo PROHIBITED.** Li-ion only if metal-cased (e.g. 18650); alkaline/NiMH/NiCad allowed | Ch. 5 | Battery datasheet + photograph of the metal can in the BOM annex |
| AV-REQ-14 | Survive **15 g** launch acceleration and **30 g** shock | Ch. 5 / 7.4 | 3-axis shaker or drop-table test; FEA of the mounting plate |
| AV-REQ-15 | Ground station must command **zero-setting of barometric altitude and accelerometer at the pad** | Ch. 5 | Command `Z` acknowledged; telemetry altitude reads 0.0 m ± 0.1 m |
| AV-REQ-16 | **No pyrotechnic devices anywhere in the rocket** | Ch. 5.xi | Design review of every energetics-adjacent part |
| AV-REQ-17 | Descent rate 2–5 m/s ± 0.5 | Ch. 7 | Logged barometric descent rate over the last 30 s |
| AV-REQ-18 | Make-in-India content gets weightage | Ch. 5 grading | Sourcing table in the BOM identifies Indian vendors/manufacturers |

### 1.2 Derived engineering requirements (not in the rules, but required to meet them)

| ID | Derived requirement | Rationale |
|---|---|---|
| AV-DER-01 | Sensor sample rate ≥ 50 Hz for the IMU, ≥ 20 Hz for the barometer; telemetry decimated to 1 Hz | 1 Hz telemetry cannot detect apogee; onboard detection needs high-rate data |
| AV-DER-02 | Barometric altitude resolution ≤ 0.25 m after filtering | 0.1 m is the *reported* resolution; the achievable noise floor must be below it |
| AV-DER-03 | Apogee detection latency ≤ 0.5 s | At 2–5 m/s descent you must deploy before the vehicle falls far; see §7.3 |
| AV-DER-04 | Deployment action is **fail-safe on power loss** for at least one path | Redundancy is only real if the backup path is electrically and mechanically independent |
| AV-DER-05 | Non-volatile state record written on every state transition, plus a heartbeat every 100 ms | Reset recovery |
| AV-DER-06 | Single-event latch-up tolerance: watchdog kick ≤ 8 s, hard reset on watchdog timeout | COTS parts in a vibrating, ESD-rich environment |
| AV-DER-07 | Total avionics bay mass ≤ 500 g including battery | Mass budget discipline, rule 5.i (±5 % lift-off mass) |

---

## 2. Architecture overview

### 2.1 Avionics block diagram

```
                    ┌──────────────────────────────────────────────────────┐
                    │            AVIONICS BAY (stacked PCB)                │
                    │                                                      │
   ┌──────────┐     │  ┌────────────────────────────────────────────────┐  │
   │ 2S Li-ion│     │  │  FLIGHT COMPUTER BOARD (FCB)                   │  │
   │ 18650 ×2 │─────┼─▶│                                                │  │
   │ 7.4 V    │     │  │   VBAT ──▶ [Buck 5.0 V] ──▶ [LDO 3.3 V]        │  │
   │ metal can│     │  │               │                 │              │  │
   └──────────┘     │  │               │                 ├─▶ STM32F411   │  │
        │           │  │               │                 ├─▶ MS5611      │  │
        │           │  │               │                 ├─▶ ICM-42688-P │  │
        │  ┌────────┴───┴──▶ [Divider + buffer] ─────────┤   (SPI)       │  │
        │  │        │  │               │                 ├─▶ MB85RC256V  │  │
        │  │        │  │               │                 │   FRAM (I2C)  │  │
        │  │        │  │               └─▶ [Buck 6.0 V] ─┼─▶ SD card     │  │
        │  │        │  │                   (servo rail)  │   (SPI)       │  │
        │  │        │  └───────────────────┬─────────────┴───────────────┘  │
        │  │        │                      │                                │
        │  │        │        ┌─────────────▼────────────┐                   │
        │  │        │        │ DEPLOYMENT DRIVER BOARD  │                   │
        │  │        │        │  ┌────────────────────┐  │                   │
        │  │        │        │  │ ARM jumper + gate  │  │                   │
        │  │        │        │  │ + flyback + TVS    │──┼──▶ DROGUE servo   │
        │  │        │        │  │ ARM jumper + gate  │──┼──▶ MAIN servo     │
        │  │        │        │  └────────────────────┘  │                   │
        │  │        │        └───────────▲──────────────┘                   │
        │  │        │                    │ BACKUP TRIGGER (dry contact)     │
        │  │        │        ┌───────────┴──────────────┐                   │
        │  │        │        │ COTS BACKUP ALTIMETER    │                   │
        │  │        │        │ (independent power,      │                   │
        │  │        │        │  independent sensors)    │                   │
        │  │        │        └──────────────────────────┘                   │
        │  │        └───────────────────────────────────────────────────────┘
        │  │
        │  └──▶ [Buck 3.3 V radio rail, LC filtered] ──▶ XBee-PRO (rocket)
        │
        └──────── (separate pack) ──▶ CAN-7USAT payload + its own radio, DIFFERENT CHANNEL

   GROUND STATION (1 km away) ── XBee-PRO + 8 dBi patch on mast ── laptop
```

### 2.2 Why the electronics are split across three boards

| Board | Contents | Why separate |
|---|---|---|
| **FCB** (flight computer board) | MCU, baro, IMU, FRAM, SD, regulators (3.3 V + 5 V) | Sensitive analog/digital, must be shock-isolated |
| **RADIO board** | XBee socket, level shifting, RF enable gate, its own LC filter | Keeps a 2 W transmitter's switching noise off the ADC ground plane; allows swapping radios without re-spinning the FCB |
| **DEP board** (deployment) | High-current servo rail, arm jumpers, gate drivers, TVS, connectors | High-current transients must not share a ground return with the ADC reference |

For a first vehicle, the FCB + a hand-wired DEP board is acceptable. **Do not** put the SD card and the ADC reference on the same ground return.

---

## 3. Microcontroller selection

### 3.1 Candidate comparison

Prices are single-unit Indian retail (Robu.in / Robocraze / Amazon.in / element14 India / Mouser India), mid-2026 street levels, inclusive of GST where applicable. Treat as ±25 %.

| MCU / board | Core & clock | ADC | RAM | Flash | Usable GPIO | Logic | Unit cost (INR) | Suitability for this vehicle |
|---|---|---|---|---|---|---|---|---|
| **Arduino Uno R3** (ATmega328P) | 8-bit AVR @ 16 MHz | 10-bit, ~9.6 kSps, ±2 LSB INL | 2 KB SRAM | 32 KB | 20 | 5 V | ₹450–700 (clone), ₹1,200–2,200 (genuine) | ❌ **Not viable.** 2 KB RAM cannot hold a 1 Hz telemetry buffer + SD FAT + a 3-state Kalman filter with any margin. No FPU. 1 hardware UART — you need one for radio *and* one for debug. |
| **Arduino Nano** (ATmega328P) | Same as Uno | Same | 2 KB | 32 KB | 22 | 5 V | ₹250–450 (clone), ₹1,800+ (genuine) | ❌ Same limits, smaller. Fine as a **test-stand auxiliary** (load cell only). |
| **ESP32-WROOM-32 DevKitC** (ESP32-D0WD-V3) | Xtensa LX6 dual @ 240 MHz | 12-bit SAR, **nonlinear**, 2 channels usable cleanly | 520 KB SRAM | 4 MB | ~25 | 3.3 V | ₹280–450 | ⚠️ **Not recommended as primary.** WiFi/BT radio in the same die as the ADC = catastrophic noise on the barometer/analog front end for a rocket. Also the ADC is famously nonlinear and needs `esp_adc_cal`. Its 2.4 GHz radio is not the licensed link you want. **Excellent as the ground-station companion/logger.** |
| **RP2040 / Raspberry Pi Pico** | Dual Cortex-M0+ @ 133 MHz | 12-bit, 500 kSps, **INL ±1 LSB** (best in class here) | 264 KB SRAM | 2 MB (external QSPI) | 26 | 3.3 V | ₹350–500 (Pico), ₹250–400 (clones, YD-RP2040) | ✅ **Strong runner-up.** Best ADC of the low-cost set, dual core lets you run logging on core 1 while the control loop runs on core 0. Downsides: no EEPROM (mitigated by FRAM), no hardware FPU (soft-float is fine at 133 MHz), no CAN, and the QSPI flash is a single point of failure for code. |
| **STM32F103C8T6 "Blue Pill"** | Cortex-M3 @ 72 MHz | 12-bit, ~1 MSps | 20 KB SRAM | 64 KB | 32 | 3.3 V (5 V-tolerant pins) | ₹180–350 | ⚠️ 20 KB RAM is tight once you hold a 1 Hz packet buffer, the FAT layer, and filter state. Also the most counterfeited STM32 (relabelled C8T6 from rejects). Acceptable **only** if you verify with `STM32_ReadID`. |
| **STM32F411CEU6 "Black Pill"** ⭐ | Cortex-M4F @ 100 MHz | 12-bit, 2.4 MSps | **128 KB SRAM** | **512 KB** | 30+ | 3.3 V | **₹550–900** | ✅ **RECOMMENDED.** Hardware single-precision FPU (Kalman filter runs in microseconds), 3× SPI + 3× USART + 2× I2C, 128 KB RAM, 512 KB flash, and a real `RTC` with a `BKP` domain that survives reset. WeAct / RobotDyn boards are widely stocked in India. |
| **STM32F405RGT6** (custom or dev board) | Cortex-M4F @ 168 MHz | 12-bit, 2.4 MSps | 192 KB | 1 MB | 50+ | 3.3 V | ₹1,400–2,600 | ✅ If you go to a **custom PCB**, this is the right choice: more timers, CAN for future work, and it is what most amateur flight computers (e.g. Altus Metrum TeleMetrum) use. |
| **Teensy 4.0** (i.MX RT1062) | Cortex-M7 @ 600 MHz | 12-bit ×2, ~1 MSps | 1 MB | 2 MB | 40 | 3.3 V | ₹3,200–4,500 (imported; no reliable Indian stock) | ⚠️ **Overkill and a sourcing risk.** Magnificent hardware (1 kHz IMU + 1 kHz SD logging with zero effort) but 5–7× the cost of a Black Pill, and genuine vs. clone is a real problem. Use only if a sponsor donates one and you have a fallback. |
| **Teensy 4.1** | Same + Ethernet + SD socket | Same | 1 MB | 8 MB | 55 | 3.3 V | ₹4,500–6,500 | Nice-to-have only. |

### 3.2 Recommendation

> ### ✅ Primary choice: **STM32F411CEU6 "Black Pill"** (WeAct Studio v3.0 board), ₹550–900

**Justification, in the order the Jury will ask:**

1. **Headroom to not fail.** 128 KB SRAM / 512 KB flash means the telemetry ring buffer, the SD/FAT layer, the sensor-fusion state, the state-recovery record and the state machine all fit with ≥ 3× margin. A 2 KB AVR does not, and "we ran out of RAM" is a design failure that shows up two weeks before launch.
2. **FPU.** A 3-state Kalman filter at 50 Hz on a Cortex-M0+ costs you ~8–12 % CPU in soft float. On an M4F it is under 1 %. That CPU is then available to service the SD card without missing IMU samples.
3. **Peripheral count matches the job exactly.** SPI1 → IMU (20 MHz, needed for 1 kHz ODR), SPI2 → SD card, I2C1 → barometer + FRAM, USART1 → XBee, USART2 → debug/GNSS, USART3 → spare, 4 timers for the mission clock, servo PWM and watchdog.
4. **`RTC` + `BKP` registers.** The STM32 has a battery/backup domain that keeps a 32-bit counter and 20 backup registers alive across a reset and across a brief brown-out. This is the cleanest way to satisfy AV-REQ-07/08 (state + mission clock survive reset) with zero extra parts.
5. **Cost and availability.** Under ₹900, stocked by Robu.in, Robocraze, ThinkRobotics, and Sunrom. It is *not* a single-source exotic part — if one board dies two days before launch you can buy three more.
6. **Make-in-India narrative.** The STM32F411 die is imported, but you can buy boards assembled/stocked domestically, and the *ground station* can be built around an Indian-made PCB with Indian-assembled modules. Document this honestly in the BOM — do not overclaim.

> ### ✅ Fallback / parallel choice: **Raspberry Pi Pico (RP2040)**, ₹350–500
> Choose this if the team's comfort zone is MicroPython/C SDK rather than STM32 HAL. The RP2040's ADC (INL ±1 LSB) is genuinely better than the STM32's for the voltage-divider channel, and dual-core lets you pin the SD writer to core 1. You lose the FPU and the backup-domain RTC, so add an external **MB85RC256V FRAM** and a **DS3231SN** RTC (or accept that the mission clock restarts and compensate by logging a monotonic counter — weaker, and the Jury may probe it).

> ### ❌ Not recommended: Arduino Uno/Nano as the primary computer
> Keep them for the **static test stand** and for teaching. 2 KB of RAM and no FPU make the competition requirements painful to meet.

### 3.3 Wiring plan for the recommended Black Pill

| Black Pill pin | Net | Notes |
|---|---|---|
| `PA5/PA6/PA7` (SPI1) | IMU `SCLK/MISO/MOSI` | Keep traces < 30 mm; 100 Ω series on SCLK if the IMU is on a flying lead |
| `PA4` | IMU `CS` | 10 kΩ pull-up |
| `PA0` | IMU `INT1` | EXTI, rising edge — the sample clock. **Do not poll the IMU.** |
| `PB13/PB14/PB15` (SPI2) | SD `SCK/MISO/MOSI` | 4.7 kΩ pull-ups on MISO+MOSI |
| `PB12` | SD `CS` | 10 kΩ pull-up |
| `PB6/PB7` (I2C1) | MS5611 + FRAM | 4.7 kΩ pull-ups to **3.3 V** (not 5 V) |
| `PA9/PA10` (USART1) | XBee `DIN/DOUT` | Plus `RTS`/`CTS` if you use flow control |
| `PA2/PA3` (USART2) | Debug header + GNSS | Bring out on a 0.1" header |
| `PA8` | Radio enable gate | Drives the load switch on the XBee 3.3 V rail (AV-REQ-09) |
| `PB0` | Buzzer / finder | Pulsed at 1 Hz after landing |
| `PB1` | Status LED (state colour code) | See §7.5 |
| `PA1` | Battery divider (ADC1_IN1) | After the buffer |
| `PB4` | IWDG already internal; use `PB4` for the ARM jumper sense | Read at boot only |
| `NRST` | Reset button + programming | Also driven by the watchdog |

---

## 4. Sensor suite

### 4.1 Barometric pressure sensor

The barometer is the **primary altitude source** and the primary apogee detector. Resolution and *repeatability* matter far more than absolute accuracy, because you zero at the pad (AV-REQ-15).

**International Standard Atmosphere relationship used throughout:**

```
h = 44330 × [ 1 − (P / P0)^(1/5.255) ]        (metres, P0 = pad pressure in Pa)
```

At sea level `dP/dh ≈ −12.0 Pa/m`. So **1 Pa of pressure resolution ≈ 0.083 m of altitude resolution.** This is the number to quote in the PDR.

| Sensor | Type | Pressure range | Resolution (Pa) | RMS altitude noise (m, after OSR×8) | Interface | Indian unit cost (INR) | Verdict |
|---|---|---|---|---|---|---|---|
| **Bosch BMP280** | Piezoresistive MEMS | 300–1100 hPa | 0.16 Pa (ultra-high-res mode) | ~0.10–0.15 | I2C (0x76/0x77) or SPI, 3.3 V | ₹120–250 (breakout) | ✅ Good cheap workhorse. Absolute accuracy ±1 hPa (≈ ±8 m) — irrelevant, you zero it. **Heavily counterfeited** (see §4.7). |
| **Bosch BME280** | BMP280 + humidity | 300–1100 hPa | 0.16 Pa | ~0.10–0.15 | I2C/SPI | ₹180–350 | ⚠️ The humidity channel is useless in a sealed avionics bay and adds a self-heating error of 0.5–1.5 °C that *degrades* the pressure reading. Prefer BMP280 or BMP390. |
| **TE MS5611-01BA03** ⭐ | Piezoresistive, **24-bit ΔΣ** | 10–1200 mbar | **0.012 Pa** (ADC LSB at OSR 4096) | **0.02–0.05** | I2C/SPI, 3.3 V | ₹450–900 (breakout), ₹350–600 (bare SOIC-8 from element14/Mouser) | ✅ **RECOMMENDED for the flight barometer.** ~10× the resolution you need, giving a 2–3 m margin against the 0.1 m reporting requirement *after* filtering. Requires a **real** calibration PROM read — verify `C1..C6` are not all-zero or all-0xFF. |
| **Bosch BMP390** | Piezoresistive | 300–1250 hPa | 0.024 Pa (0.03 hPa equiv.) | ~0.03–0.06 | I2C/SPI, 3.3 V | ₹400–700 | ✅ Modern, low-noise, excellent. Bosch's own successor to BMP280. If you cannot source a genuine MS5611, take this. |
| **Bosch BMP581** | Piezoresistive | 300–1250 hPa | 0.0068 Pa (0.0051 hPa) | ~0.02 | I2C/SPI, 1.65–3.6 V | ₹850–1,400 | Nice-to-have. Best-in-class noise but ~2× the price of an MS5611 for little practical gain at 1 km apogee. |
| **Infineon DPS368** | Capacitive MEMS | 300–1200 hPa | 0.002 Pa | ~0.02 | I2C/SPI | ₹350–600 | Alternative to the MS5611; capacitive sensing is less prone to the counterfeit piezoresistive-module problem. |
| **HP03M / HP20x** | — | — | — | — | — | ₹600–1,200 | ❌ Obsolete/rare, avoid. |

**Decision:** **MS5611-01BA03** as the flight barometer (SPI mode), with a **BMP390** as the redundant/second barometer on the backup chain if budget allows. If budget is tight: **two BMP390s** on separate I2C addresses beats one MS5611 — cross-checking two independent sensors catches the failure mode that matters (a stuck or drifting sensor), and disagreement between them is itself a detectable fault.

**Failure modes:** condensation on the port at altitude (mitigate: conformal coat the PCB *except* the port, add a Gore-Tex or PTFE vent membrane); light ingress into the port (mitigate: internal baffle); I2C bus lock-up from a clock-stretch hang (mitigate: bus-recovery routine that bit-bangs 9 clocks on SCL — with SPI you do not have this problem); counterfeit die (§4.7).

### 4.2 Inertial measurement unit (IMU)

#### ⚠️ Important obsolescence note — read this before buying

**InvenSense (now TDK) discontinued the MPU6050 and MPU9250 for new designs.** They remain in production for legacy customers only, and the Indian market is saturated with:

- **Refurbished/re-marked MPU6050 dies** — pulled from scrap boards, re-lasered, sold as new. Symptoms: gyro bias wander of 5–20 °/s, random I2C NACKs, temperature sensor reading nonsense.
- **"MPU9250" modules that contain an MPU6500 + a fake or absent AK8963 magnetometer.** You can detect this: read `WHO_AM_I` (should be `0x71` for MPU9250, `0x70` for MPU6500) and `WIA` of the mag at `0x0C` (should be `0x48`).
- **Genuine-Bosch-labelled BMP280s** that are actually a different die with a rewritten calibration block, giving 3–10 m of altitude noise instead of 0.15 m.

**Rule for this club: never buy an IMU or barometer breakout from a marketplace listing with no part-number-level traceability.** Buy from element14 India, Mouser India, DigiKey India, or a named Indian vendor who will give you a batch/lot photo. Budget ₹100–200 extra per part for provenance; it is cheaper than losing a launch.

#### IMU comparison

| IMU | Accelerometer range / noise | Gyro range / noise | Interface | Who_Am_I | Indian cost (INR) | Verdict |
|---|---|---|---|---|---|---|
| **MPU6050** (TDK InvenSense) | ±2/4/8/16 g, 300 µg/√Hz | ±250…±2000 °/s | I2C only (400 kHz max) | `0x68` | ₹90–220 (breakout) | ❌ **Obsolete.** I2C-only caps you at ~1 kHz sample on a shared bus, and the clone problem is severe. Acceptable for a *teaching* board and for the static test stand. Not for flight. |
| **MPU9250** (TDK) | ±16 g, 300 µg/√Hz | ±2000 °/s | I2C/SPI | `0x71` | ₹250–600 | ❌ **Obsolete.** Same clone problem, and the 9-axis is a 6-axis + separate AK8963 die that many clones fake. |
| **TDK ICM-20948** | ±16 g, 230 µg/√Hz | ±2000 °/s | I2C/SPI | `0xEA` | ₹450–1,200 | ✅ Good, current-production 9-axis. The magnetometer is genuinely useful for yaw reference on the pad and for post-flight attitude reconstruction. For a rocket, though, the mag saturates/rotates uselessly during spin and adds complexity (needs its own 1 kHz-safe read path). Take it if you want the compass; skip it if you do not. |
| **Bosch BMI088** ⭐ | **±24 g**, 175 µg/√Hz (accel), separate dies | ±2000 °/s | SPI (dual CS) | accel `0x1E`, gyro `0x0F` | ₹900–1,600 (genuine, may need import) | ✅ **The best technical choice.** Two *separate* dies in one package — the accelerometer and gyro do not share a mechanical structure, which is exactly what you want under 15–30 g and violent vibration. Bosch's own vibration-robustness documentation makes it the drone/rocketry standard. Downside: hard to source in India, and the dual-CS SPI driver is more work. |
| **TDK ICM-42688-P** | ±16 g, **70 µg/√Hz** | ±2000 °/s | SPI/I2C | `0x47` | ₹600–1,100 | ✅ **Excellent alternative to the BMI088**, easier to source, lower noise, single-die but well-damped. If BMI088 is unavailable, this is the pick. |
| **ST ISM330DHCX** | ±16 g, 60 µg/√Hz | ±4000 °/s | SPI/I2C | `0x6B` | ₹900–1,500 | ✅ Industrial-grade, −40…+105 °C, excellent bias stability. Great if you can get it. |
| **Analog Devices ADIS16470** | ±40 g | ±2000 °/s | SPI | — | ₹45,000+ | ❌ Not for this budget. Mention in the PDR as the "if we had ₹1 lakh" option to show you know what the professional tier looks like. |

**Decision:** **TDK ICM-42688-P** as first choice (best sourcing-to-performance ratio in India today), **Bosch BMI088** if a sponsor or an import order can supply it, **ICM-20948** as the safe, always-in-stock fallback.

#### Accelerometer range selection — the arithmetic

| Flight event | Expected acceleration | Margin needed | Range required |
|---|---|---|---|
| Launch (rule 5: survive 15 g) | 15 g axial | ×1.5 for transients | 22.5 g |
| Motor thrust spike / resonant coupling | up to ~25 g | ×1.2 | 30 g |
| Parachute opening shock (rule 7.4: survive 30 g) | 30 g | ×1.5 | 45 g |

**Set the accelerometer to ±16 g for the primary flight channel** — this is what the rules expect you to report ("accelerometer data" in m/s²) and it gives 16 g × 9.80665 = **156.9 m/s²** full scale, which covers launch with margin as long as you are honest that transient spikes may clip.

**Set the accelerometer to ±24 g or ±32 g if the part supports it** (BMI088 goes to ±24 g; ICM-42688-P caps at ±16 g). If your part caps at ±16 g, **document clipped samples** rather than letting them alias: mark any sample where `|raw| > 0.97 × full_scale` with a clip flag in the SD log. A clipped sample that quietly reads 156.9 m/s² when the true value was 200 m/s² corrupts your velocity integration.

> 💡 **Practical:** the ±16 g setting is what you *report*; you can very often read a second, higher-range channel or switch range mid-flight. If you must choose one range, choose ±16 g and be explicit in the CDR about the clipping risk during the 30 g opening shock. Report `max_g` in the post-flight analysis with the clip flag visible.

**Gyro range:** set **±2000 °/s**. A rocket rolling at 5–15 rev/s is 1800–5400 °/s. At ±2000 °/s you will clip on a fast roll. If the part supports ±4000 °/s (ISM330DHCX does), use it — the spin-rate reporting requirement is better served by not clipping. If you are stuck at ±2000 °/s, the barometer still gives you apogee, so a clipped gyro degrades a *reported* field rather than the mission.

### 4.3 GNSS with NavIC / IRNSS support

**NavIC (Navigation with Indian Constellation, formerly IRNSS)** is India's regional GNSS: 3 geostationary + 4 inclined geosynchronous satellites, covering India plus ~1500 km beyond, broadcasting in **L5 (1176.45 MHz)** and **S (2492.028 MHz)** bands. It is **not** a replacement for GPS — it is an *additional constellation* you can track to improve satellite count and, in principle, geometry. The competition does not test NavIC directly; the "Make in India" grading and the fact that you are an Indian team make it worth supporting and documenting honestly.

**Truthful sourcing situation:** most "NavIC-capable" modules sold in India are GPS+GLONASS modules with NavIC support *claimed* in the marketing copy. What actually matters is whether the receiver firmware can track IRNSS satellites and whether the antenna covers the L5 band.

| Module | Chipset | Constellations | NavIC / IRNSS | Interface | Update rate | Indian cost (INR) | Notes |
|---|---|---|---|---|---|---|---|
| **u-blox NEO-M8N** | u-blox M8 | GPS, GLONASS, Galileo, BeiDou, QZSS, **SBAS/GAGAN** | ❌ No IRNSS | UART/I2C/SPI, 3.3 V | 10 Hz | ₹1,100–1,800 (breakout + antenna) | ✅ Most reliable, best-documented, supports **GAGAN** (India's SBAS, on GPS L1/L5) which is the practically important Indian augmentation. **This is the safe choice.** |
| **u-blox NEO-M9N** | u-blox M9 | GPS, GLONASS, Galileo, BeiDou | ❌ No IRNSS | UART/I2C/SPI | 25 Hz | ₹2,000–3,200 | Overkill; higher update rate is genuinely useful for post-flight trajectory reconstruction. |
| **Quectel L86 / L76K** | MediaTek MT3333 | GPS, GLONASS, BeiDou, QZSS, **Galileo** | ❌ | UART, 3.3 V | 10 Hz | ₹600–1,100 | Cheap, works, patch antenna onboard, ~₹800. Good budget pick. |
| **Quectel LC86G** | Quectel | GPS, GLONASS, BDS, Galileo, **NavIC (L5)** | ✅ Claimed | UART | 10 Hz | ₹1,200–2,000 | One of the few genuinely IRNSS-capable modules available through Indian distributors. Verify with the datasheet before claiming it in the CDR. |
| **Skylark C1 / Indian GNSS receiver boards** | — | Multi-constellation incl. IRNSS | ✅ | UART | 1–10 Hz | ₹2,000–4,000 | Domestic Indian GNSS makers. Good Make-in-India story. Availability is project-dependent — verify stock before you commit in the PDR. |
| **Telit SE868-V3** | — | GPS, GLONASS, BDS, **IRNSS** | ✅ | UART | 10 Hz | ₹1,500–2,500 | Genuine IRNSS support in the datasheet. Import or distributor order. |
| **ATGM336H** | Zhongke Micro | GPS + BeiDou | ❌ | UART | 10 Hz | ₹350–600 | Cheapest option that works. No NavIC. Fine if NavIC is not a stated requirement for you. |

**Decision:** **u-blox NEO-M8N** as the primary (mature, 10 Hz, GAGAN-capable, ₹1,100–1,800), **plus** an honest CDR statement: *"NavIC/IRNSS support is a design goal; our primary receiver is GAGAN-capable. We will evaluate an IRNSS-capable module (Quectel LC86G / Telit SE868-V3) as a drop-in replacement before FRR."* That is a stronger, more defensible position than claiming NavIC you cannot demonstrate.

> ⚠️ **GNSS in a rocket is hard.** A rocket under 15 g with a tumbling body and a 2.4 GHz transmitter 5 cm away will:
> - lose lock during boost (patch antennas are not designed for 25 g or for 300 m/s),
> - report **COCOM velocity limits** (u-blox modules cap at 500 m/s and 18 km altitude by default — you will not hit these at 1 km, but if you ever fly higher, u-blox requires a signed NDA to lift them),
> - take 30–60 s for a cold fix and 1–5 s for a hot fix.
>
> **You must therefore acquire a fix on the pad before launch and log the last-known-good position.** If the receiver drops out at boost, your ground station shows stale coordinates with a "no-fix" flag rather than garbage.

**Time-to-first-fix budgeting:**

| Start condition | Typical TTFF | When it happens |
|---|---|---|
| Cold (no almanac, no RTC backup) | 26–35 s | First power-up at the field |
| Warm (almanac + coarse time, no ephemeris) | 20–30 s | After a brief power cycle |
| Hot (almanac + ephemeris + position ≤ 25 km) | 1–3 s | Re-power on the same pad |
| Assisted (backup battery keeps the receiver's RTC + almanac alive) | 1–5 s | **Design for this** — a 3 V coin cell on `V_BCKP` |

**Design action:** wire a **CR2032 or ML1220 rechargeable coin cell to the module's `V_BCKP` pin**. This is ~₹40 of parts and turns a 30 s cold start into a 2 s hot start. On a pad where you may sit for 30 minutes, it also lets you power-cycle the GNSS to clear a hang without paying the cold-start penalty.

### 4.4 Temperature sensing

| Sensor | Range | Accuracy | Interface | Indian cost (INR) | Use |
|---|---|---|---|---|---|
| **On-die sensor in the barometer/IMU** | −40…+85 °C | ±1 °C | Already on I2C/SPI | ₹0 | The **reported** telemetry temperature (Annexure-2 needs 0.1 °C resolution — you get that by formatting, and ±1 °C accuracy is fine because the rules specify *resolution*, not accuracy). Use it for barometer temperature compensation too. |
| **DS18B20** (Maxim/Dallas) | −55…+125 °C | ±0.5 °C (−10…+85) | **1-Wire**, 12-bit | ₹90–250 (TO-92), ₹120–200 (waterproof probe) | ✅ Best choice for **battery-pack and avionics-bay temperature**. Parasite-powerable over a 3-wire cable, and you can put 4–6 on one pin with unique 64-bit ROM addresses. 750 ms conversion at 12-bit — fine for a 1 Hz housekeeping channel. |
| **NTC 10 kΩ β=3950 thermistor** | −40…+125 °C | ±0.2 °C with a good β model | Analog divider → ADC | ₹10–40 | Cheapest. Requires Steinhart–Hart or β-equation linearisation and a stable reference resistor (use a 0.1 % 10 kΩ). Use for **motor casing skin temperature** on the test stand. |
| **MAX6675 breakout** | 0…+1024 °C, K-type only | ±2–3 °C | SPI, 5 V | ₹250–450 | ⚠️ Old, only 0.25 °C resolution and 180 ms conversion, and no fault detection beyond open thermocouple. Fine for a first test stand. |
| **MAX31855K breakout** ⭐ | −200…+1350 °C, K-type | ±2 °C | SPI (read-only), 3.3 V logic (needs 3.3 V supply on the "K" 3V3 variant) | ₹350–700 | ✅ **Recommended thermocouple front end.** 14-bit, 0.25 °C resolution, ~100 ms conversion, and it reports open-circuit / short-to-GND / short-to-VCC faults in the status word. Genuine Maxim die vs. clone is a real concern — buy from element14/Mouser. |
| **MAX31856 breakout** | Any type (K/J/N/T/S/E/B/R) | ±0.7 °C + thermocouple error | SPI, 3.3 V | ₹900–1,600 | ✅ Best. Does the full linearisation internally (the MAX31855 does not — it assumes a linear K-type response, which is a 2–5 °C error near the extremes). Use if you care about absolute temperature, not just trend. |
| **Thermocouple, K-type, 1/8" inconel sheath, 150 mm** | −200…+1250 °C | Type K tolerance ±2.5 °C | — | ₹600–1,500 each | ⚠️ Buy a **grounded-junction, stainless or inconel sheath** probe. Exposed-bead probes die instantly in a motor plume. |

**Cold junction compensation (CJC):** a thermocouple measures only a *temperature difference* between its hot junction and the point where its wires land on the PCB. Every MAX31855/MAX31856 has an internal cold-junction sensor at its own terminals. Two consequences you must design for:

1. **The chip must be at the same temperature as the terminal block.** If the chip is 15 °C warmer (because it sits next to a buck converter), your reading is 15 °C low. → Keep ≥ 20 mm clearance from regulators, and add a copper pour under the chip to thermally couple it to the connector.
2. **Long thermocouple leads must be the correct alloy all the way to the terminal.** If you extend a K-type with ordinary copper wire, you create two new junctions and the reading is garbage. → Buy the correct K-type **extension** wire (chromel/alumel) or keep the probe's own leads long enough.

### 4.5 Voltage sensing

Resistor divider into the ADC. Design rules:

```
V_adc = V_batt × R2 / (R1 + R2)

Choose R1 + R2 so that:  I_divider ≈ 0.1 mA  (low enough for battery life,
                                              high enough to swamp ADC leakage)
Target:  V_batt_max (8.4 V for 2S) → V_adc ≈ 2.9 V  (leaves headroom under 3.3 V)
```

| Battery | R1 | R2 | V_adc at 8.4 V | Divider current at 7.4 V | ADC counts/LSB (12-bit, 3.3 V ref) |
|---|---|---|---|---|---|
| 2S Li-ion (8.4 V max) | 22 kΩ | 10 kΩ | 2.63 V | 0.23 mA | 12.9 mV/count → 33 mV/count at the battery |
| 2S Li-ion, lower drain | 47 kΩ | 22 kΩ | 2.69 V | 0.11 mA | same ratio |
| 1S Li-ion (4.2 V max) | 10 kΩ | 22 kΩ | 2.89 V | 0.13 mA | — |
| 4×AA alkaline (6.4 V max) | 22 kΩ | 15 kΩ | 2.59 V | 0.17 mA | — |

**Mandatory additions:**

1. **0.1 % resistors.** With 1 % resistors, the ratio error alone is ±2 %, i.e. ±0.17 V on an 8.4 V pack. The rules want **0.01 V** resolution — you will get that from the ADC, but your *accuracy* would be terrible. Use 0.1 % (₹3–8 each from element14) or calibrate each board against a bench DMM and store the correction in FRAM.
2. **100 nF + 10 µF at the ADC pin.** The ADC sample-and-hold draws a current spike; a high-impedance divider without a capacitor gives you a reading that depends on the previous channel.
3. **A rail-to-rail buffer (MCP6002, ₹40) or at minimum a follower.** The STM32's ADC wants a source impedance under ~10 kΩ for full 12-bit accuracy at 2.4 MSps. Your divider is 32 kΩ (22k ∥ 10k). Either lower the divider to ~5 kΩ total (costs you 1.5 mA — unacceptable for a 30-minute pad wait) **or** add a buffer. **Add the MCP6002.** This is the single most common "why is my voltage reading wrong" bug in student flight computers.
4. **Reverse-polarity protection** upstream of the divider: a P-channel MOSFET (AO3401, ₹8) beats a series Schottky by 20× on loss.

**Current sensing** (for the deployment rail and the static test stand):

| Method | Part | Range | Cost (INR) | Notes |
|---|---|---|---|---|
| High-side shunt + current-sense amp | **INA219** breakout | ±3.2 A, 12-bit | ₹180–350 | ✅ Easiest. Reports bus voltage *and* current over I2C. 0.1 Ω shunt → 10 mA resolution. |
| High-side shunt + amp | **INA226** | ±10 A, 16-bit | ₹300–600 | ✅ Better resolution, alert pin for over-current. |
| High-side shunt + amp | **INA228** | ±85 V, 20-bit | ₹600–1,200 | For the test stand if you want one part to do everything. |
| Hall-effect, isolated | **ACS712-30A** | ±30 A | ₹180–350 | ⚠️ Noisy, offset drifts, needs ±5 V or a mid-rail bias. Fine for a thrust-stand current monitor, poor for precision. |
| Hall-effect, isolated | **ACS758LCB-100U** | 0–100 A | ₹600–1,100 | Better than the ACS712; good for the ignition/deployment rail. |

---

## 5. Power architecture

### 5.1 Battery selection — the rules constrain you

> **Rule 5 (battery):** LiPo is **PROHIBITED**. Li-ion is permitted **only if metal-cased** (e.g. 18650-type cylindrical cans). Alkaline, NiMH and NiCad packs are also acceptable.

This rules out every "LiPo 3S 1000 mAh" pouch cell, every LiHV pack, and every soft-pouch "lithium polymer" battery — even though they are the obvious choice on mass and current capability. Plan around it from the start; do not show up at the CDR with a pouch cell in the BOM.

| Chemistry | Form | Nominal V | Capacity | Usable energy | Peak current | Cost (INR) | Verdict |
|---|---|---|---|---|---|---|---|
| **2× 18650 Li-ion, metal can, protected** ⭐ | 2S pack with holder or spot-welded | 7.4 V | 2× 2600 mAh = **19.2 Wh** | ~17 Wh | 5 A continuous | ₹350–700/cell + ₹150 holder | ✅ **RECOMMENDED.** Metal-cased (complies), high energy density, 5 A capability covers servos, and 19 Wh is ~4× what you need for 30 min of pad wait. |
| **1× 18650 Li-ion, protected** | 1S | 3.7 V | 2600–3400 mAh (9.6–12.6 Wh) | ~10 Wh | 5 A | ₹350–700 | ✅ Viable **only if** you use a boost converter for the 5 V servo rail, which adds switching noise and a failure mode. Prefer 2S. |
| **2× 18650 LiFePO4** | 2S | 6.4 V | 2× 1500 mAh = 19.2 Wh | ~17 Wh | 10 A | ₹900–1,800/pack | ✅ Safer chemistry (no thermal runaway propagation), flatter discharge, but lower energy per cell and a different charger. Good if the club already owns LiFePO4. |
| **4× AA alkaline** | 4S holder | 6.0 V | ~2000 mAh @ 100 mA (much less at 1 A) | ~9 Wh (at low drain) | ~500 mA useful | ₹120–250 | ⚠️ **Only as a backup/comms-independent pack.** Alkaline internal resistance rises steeply: at 1 A you lose 30–50 % of capacity, and voltage sags to 4.5 V. **Do not use alkaline for the servo rail.** Fine for the COTS backup altimeter. |
| **6× AA NiMH (Eneloop)** | 6S holder | 7.2 V | 1900–2000 mAh | ~14 Wh | 2–3 A | ₹900–1,600 | ✅ Genuinely good. Flat discharge, 2000+ cycles, no shipping restrictions, no thermal runaway. Slightly heavier. **Excellent choice if you want the lowest-risk battery.** |
| **9 V PP3 alkaline** | — | 9 V | 500 mAh (at 20 mA!) | ~4.5 Wh | 100 mA | ₹40–120 | ❌ **Trap.** A 9 V "transistor battery" is six tiny AAAA cells in series. It will not run a servo, and its capacity at 500 mA is closer to 150 mAh. Never power a flight computer from a 9 V block. |
| **Any LiPo / LiHV pouch** | — | — | — | — | — | — | ❌ **PROHIBITED BY RULE.** |
| **Coin cell (CR2032)** | — | 3 V | 220 mAh | — | 1 mA | ₹15–40 | ✅ Use it **only** for the GNSS `V_BCKP` backup supply. Not for anything else. |

**Recommended power tree:**

```
  2S Li-ion pack (7.4 V nominal, 8.4 V full, 6.0 V cutoff)  [2 × 18650 protected]
      │
      ├── [F1: 3 A polyfuse] ── [Q1: AO3401 P-FET reverse-polarity] ── VBAT_SW
      │                                                                   │
      │   ┌───────────────────────────────────────────────────────────────┤
      │   │                                                               │
      │   ▼                                                               ▼
      │  [U1: MP1584EN buck]                                          [U3: MP1584EN buck]
      │   8.4 V → 5.0 V @ 2 A                                          8.4 V → 6.0 V @ 3 A
      │   η ≈ 88 %                                                     (servo rail, separate)
      │   │                                                               │
      │   ├── [LC: 10 µH + 100 µF] ── 5V_CLEAN ──┬── SD card              ├── [2200 µF bulk] ── SERVO_RAIL
      │   │                                       ├── MAX31855            │        │
      │   │                                       └── (spare)             │        ├── DROGUE servo
      │   │                                                               │        └── MAIN servo
      │   ▼                                                               ▼
      │  [U2: MCP1700-3302E LDO]                                      [ARM jumper]
      │   5.0 V → 3.3 V @ 250 mA, dropout 178 mV @ 250 mA              │
      │   │   (SOT-23, ₹45; quiescent 1.6 µA)                          ▼
      │   ├── [Ferrite + 10 µF + 100 nF] ── 3V3_ANALOG ── MS5611, ADC ref, MCP6002
      │   ├── [Ferrite + 10 µF + 100 nF] ── 3V3_DIGITAL ── STM32, FRAM, SD logic
      │   └── [LC + load switch (AO3401 or TPS22918)] ── 3V3_RADIO ── XBee-PRO
      │                                                                 (gated by PA8, AV-REQ-09)
      │
      └── [Divider 22k/10k + MCP6002 buffer] ── PA1 (ADC1_IN1)   ← battery voltage telemetry
```

### 5.2 Power budget and the 30-minute pad wait (AV-REQ-12)

**The requirement:** 30 minutes of pad wait, *with margin*. The competition's own rule is 30 minutes; the club standard should be **45 minutes**, because your pad wait will include the Jury walking the pad, a safety briefing, and a weather hold.

**Pre-launch (pad wait) power budget — everything on, nothing transmitting except 1 Hz telemetry:**

| Load | Voltage rail | Current | Notes |
|---|---|---|---|
| STM32F411 @ 100 MHz, all peripherals on | 3.3 V | 32 mA | Measured, not datasheet-typical |
| MS5611 barometer (OSR 4096, 1 Hz) | 3.3 V | 0.9 mA | Datasheet 1.4 mA peak, ~0.6 mA avg |
| ICM-42688-P IMU @ 1 kHz | 3.3 V | 0.6 mA | Low-power mode is unnecessary |
| MB85RC256V FRAM (idle + 10 Hz heartbeat write) | 3.3 V | 0.3 mA | Write current 200 µA at 1 MHz I2C |
| SD card (Class 10, idle between writes) | 5.0 V | 2 mA avg (30 mA during a 20 ms write) | ⚠️ Idle SD cards are not zero-current; some are 5–15 mA |
| microSD module + pull-ups + LDO quiescent | — | 1.5 mA | |
| GNSS NEO-M8N (tracking) | 3.3 V | 30 mA | 45 mA during acquisition — budget the higher figure for the first 5 min |
| XBee-PRO S1 (2.4 GHz, 18 dBm, ~1 % duty) | 3.3 V | 45 mA | 215 mA **during** a transmit burst; average at 1 Hz × 60 ms bursts ≈ 13 mA + 32 mA receive |
| Buck U1 (5 V) efficiency loss | 7.4 V | ~6 mA | 88 % efficient, ~0.28 W loss |
| Buck U3 (6 V, servos idle) | 7.4 V | 1 mA | Servos hold no load until armed |
| LDO U2 drop (7.4→5→3.3) losses | — | ~8 mA equiv | Included above via efficiency terms |
| Status LEDs (1 × 2 mA) | 3.3 V | 2 mA | 💡 Keep it to one LED, PWM it at 20 % |
| **TOTAL at the battery** | **7.4 V** | **≈ 130 mA** | |

**Endurance calculation:**

```
Pack:      2 × 18650, 2600 mAh nominal, 7.4 V  →  19.2 Wh
Derate:    −10 % for cold (field temperature 10–15 °C in Nov)
           −15 % for aging + cutoff at 6.0 V (do not deep-discharge)
           − 5 % for converter efficiency uncertainty
Usable:    19.2 Wh × 0.70  =  13.4 Wh
Drain:     7.4 V × 0.130 A  =  0.96 W
Endurance: 13.4 Wh / 0.96 W = 14.0 hours

Required:  45 min = 0.75 h
Margin:    14.0 / 0.75  =  18.6×   ✅
```

> **Conclusion:** a single 2S 18650 pack gives you **~14 hours** of pad-wait endurance against a 45-minute requirement — an 18× margin. You are **not** power-limited; you are *failure*-limited. The real risks are (a) a stuck-on radio or servo, (b) a software hang that never sleeps, and (c) a connector that vibrates loose.

**Design consequences of that conclusion:**

1. **Do not optimise for power.** Optimise for *not hanging*. A 130 mA idle draw is irrelevant next to a firmware bug that leaves the servo stalled at 2.5 A.
2. **Add a second, independent battery for the COTS backup altimeter.** Almost every commercial altimeter wants its own 9 V or 1S LiPo. This is not optional — "independent" in rule 5.xv means independent power too. Budget ₹250–500 for it.
3. **Log the battery voltage every 10 seconds during the pad wait** so you have the discharge curve in the CDR. This directly answers "how do you know you can wait 30 minutes?"
4. **Set a low-voltage warning at 6.8 V (2S)** and a hard "abort launch" threshold at 6.4 V. Below that, the servo rail cannot reliably move a loaded servo.

**Flight-phase budget (a 120-second flight):**

| Phase | Duration | Current at battery | Energy |
|---|---|---|---|
| Boost (servos armed, telemetry 1 Hz) | 5 s | 0.9 A | 0.009 Wh |
| Coast + apogee (deployment fires) | 25 s | 2.0 A for 0.4 s (servo stall), then 0.3 A | 0.003 Wh |
| Descent (1 Hz telemetry, buzzer on) | 90 s | 0.20 A | 0.033 Wh |
| **Total flight** | **120 s** | — | **≈ 0.05 Wh** |

**The flight itself costs 0.26 % of the pack.** This is worth stating in the CDR: the design driver is pad endurance and fault tolerance, not flight energy.

### 5.3 Regulation: LDO vs. buck converter

| | Linear LDO (e.g. MCP1700, AMS1117) | Switching buck (e.g. MP1584, TPS5430) |
|---|---|---|
| Efficiency at 7.4 V → 3.3 V | **45 %** (you burn 4.1 V as heat) | **85–92 %** |
| Heat at 250 mA | P = (7.4−3.3) × 0.25 = **1.03 W** — an SOT-23 will hit 150 °C and shut down | ~0.14 W |
| Output noise | **10–50 µV RMS** — essentially clean | 10–40 mV ripple at the switching frequency + harmonics |
| Part count | 2 (in + out cap) | 6–8 (inductor, diode/sync FET, caps, feedback) |
| Cost | ₹15–60 | ₹60–450 (module) |
| Failure modes | Thermal shutdown, dropout when the battery sags | Inductor saturation, feedback divider drift, EMI into the ADC |
| When to use | **Post-regulation** and low-current analog rails | **Bulk step-down** and the servo rail |

**The correct architecture is a cascade, and this is not a compromise — it is what the professional flight computers do:**

```
VBAT (7.4 V) ──[BUCK]──▶ 5.0 V ──[LDO]──▶ 3.3 V ──[ferrite bead]──▶ 3V3_ANALOG
                88 %              65 %          (the LDO cleans the buck's ripple)
               combined ≈ 57 % — still 2× better than a 7.4→3.3 single LDO (45 %)
               and the analog rail is quieter than either alone
```

**Where the rails go:**

| Rail | Source | Consumers | Noise requirement |
|---|---|---|---|
| `VBAT` | Pack, through polyfuse + P-FET | Buck inputs only | — |
| `5V_CLEAN` | MP1584EN, 2 A | SD card, MAX31855, spare 5 V sensors | Moderate |
| `3V3_DIGITAL` | MCP1700 from `5V_CLEAN` | STM32, FRAM, SD logic, LEDs | Moderate |
| `3V3_ANALOG` | MCP1700 *separate* from `5V_CLEAN`, + ferrite | MS5611, ICM-42688-P, MCP6002, ADC `VREF+` | **Critical** |
| `3V3_RADIO` | Its own LC from `5V_CLEAN`, gated by a load switch | XBee-PRO only | Isolated so a 2 W transmit burst cannot modulate the analog rail |
| `SERVO_RAIL` | Separate MP1584EN at 6.0 V, 3 A, + 2200 µF bulk | Deployment servos only | High current, high transients — **never shared with logic** |

> ⚠️ **The `5V_CLEAN` and `SERVO_RAIL` must be separate converters, not one converter with two loads.** A servo stall at 2.5 A will sag a shared 5 V rail below the STM32's brown-out threshold in microseconds. This is the single most common cause of "the flight computer reset when the parachute fired."

### 5.4 Decoupling

Placement matters more than the value. The rule: **the smallest capacitor goes closest to the pin.**

| Location | Capacitors | Why |
|---|---|---|
| Every STM32 `VDD`/`VSS` pin pair | **100 nF X7R 0402/0603**, ≤ 2 mm from the pin, with a via directly to the ground plane | High-frequency supply impedance |
| Each IC's supply pin | 100 nF + **1 µF X7R** | Mid-frequency |
| Each rail, at the entry point | **10 µF X5R** + 100 nF | Bulk |
| MS5611 and IMU | 100 nF + 1 µF, **plus** a 10 Ω series resistor or ferrite in the supply | Keeps digital switching noise out of the sensing die |
| ADC `VREF+` | **1 µF X7R + 100 nF**, fed through a ferrite from `3V3_ANALOG` | Reference noise appears directly in your counts |
| SD card socket | **10 µF** close to the socket, plus 100 nF | Write bursts draw 30–100 mA |
| XBee socket | **100 µF** low-ESR electrolytic + 10 µF + 100 nF | 215 mA transmit bursts at 2.4 GHz |
| Servo connectors | **1000–2200 µF** per servo, at the connector, plus a 100 nF | Stall inrush; this is what actually prevents a brownout |
| Buck input and output | Per the datasheet — do not substitute values | Loop stability |

💡 **Do not use a single 100 µF electrolytic in place of ten 100 nF ceramics.** They cover different frequency decades; you need both.

### 5.5 Inrush and hot-plug protection

**The problem:** an uncharged 2200 µF servo bulk capacitor on a 6 V rail looks like a short for the first few milliseconds. `I = C × dV/dt`; at 6 V in 1 ms that is **13 A**. This will (a) trip a polyfuse, (b) collapse the battery, (c) reset the MCU, or (d) weld a connector.

**Fixes, in order of preference:**

1. **Inrush-limiting NTC thermistor** (e.g. Ametherm SL12 1R010, or a generic 5 Ω NTC) in series with the servo rail input. Cold resistance ~5 Ω limits inrush to ~1.5 A; it self-heats and drops to ~0.2 Ω within a second. Cost ₹25–60. **Simplest and most effective.** ⚠️ Downside: it stays warm for ~30 s after a power cycle — do not power-cycle and immediately expect full servo torque.
2. **P-channel MOSFET with an RC-delayed gate** (soft-start): a 100 kΩ/10 µF gate network gives ~1 s of ramp. Cost ₹10. Slightly more design work, no thermal residual.
3. **Active hot-swap controller** (TPS2410, LTC4211) — correct engineering, ₹300–600, overkill here.
4. **Sequencing:** always bring up `3V3_DIGITAL` **before** `SERVO_RAIL`, and arm the servo rail only on the `ARM` command. This makes the inrush event a deliberate, logged action rather than a power-on surprise.

**Also required:**

- **Polyfuse (PPTC) on the battery input:** 3 A hold, 6 A trip (e.g. Bourns MF-R300). ₹15–40.
- **TVS diode across the servo rail:** SMAJ6.0A or P6SMB6.8A. Servos are inductive loads; a stalled or suddenly-reversed servo generates a spike that will kill a gate driver. ₹10–20.
- **Flyback diodes across any relay or solenoid coil:** 1N4148 for small, 1N5819 Schottky for larger. ₹2–8.
- **Reverse-polarity P-FET (AO3401 / DMP3098L):** ₹8. Do it. Someone will connect the battery backwards at 05:00 on launch day.

### 5.6 Guaranteeing 30+ minutes of pad wait — the actual procedure

The battery arithmetic in §5.2 gives 14 hours. Proving it requires a test:

| Step | Action | Pass criterion |
|---|---|---|
| 1 | Fully charge the pack. Measure with a bench DMM. | 8.35–8.40 V |
| 2 | Connect the **flight configuration** — full avionics, radio transmitting at 1 Hz, GNSS locked, SD logging, servos armed but idle | — |
| 3 | Start the 45-minute soak. Log `VBAT` every 10 s to SD **and** to the ground station | — |
| 4 | At T+15, T+30, T+45 min: command a full servo **deployment** cycle and verify it completes | Servo reaches both end stops |
| 5 | At T+45 min: verify the pack voltage | **≥ 6.8 V** |
| 6 | Compute the discharge slope | Extrapolate to 6.0 V; the projected time must exceed **90 min** |
| 7 | Repeat at the **coldest expected field temperature** (put the pack in a 10 °C cooler for 2 h first) | Same criteria |

> 💡 **The margin is not the battery — it is the plan.** Write a **pad-wait clock** into the ground station: a countdown that alerts the team at T+25 min and forces a decision at T+40 min (launch, or power down and swap packs). A rule the Jury can see you following is worth more than a bigger battery.

---

## 6. Data logging

### 6.1 SD card over SPI — the practical constraints

**Wiring:**

```
  STM32 SPI2                 microSD socket (SPI mode)
  ───────────                ────────────────────────
  PB13 SCK  ──── 100 Ω ────▶ CLK
  PB14 MISO ◀── 4.7 k↑ ───── DO
  PB15 MOSI ─── 4.7 k↑ ────▶ DI
  PB12 CS   ─── 10 k↑  ────▶ CS
  3V3       ────────────────▶ VDD  (3.3 V — NOT 5 V)
  GND       ────────────────▶ GND
                              CD  ──▶ PA0? NO — leave unconnected or use a
                                      separate pin; do not share with the IMU INT
```

**Hard-won rules:**

| Rule | Why |
|---|---|
| **Use 3.3 V logic.** Many microSD cards work at 3.3 V only. | A 5 V module with an onboard AMS1117 will work but wastes 60 mA and heats up. |
| **Set the SPI clock to 400 kHz for init, then raise to 10–25 MHz.** | Cards require ≤ 400 kHz for the first 74 clocks and the CMD0/CMD8/ACMD41 handshake. After init, faster is better. |
| **Add 4.7 kΩ pull-ups on MISO and MOSI.** | The card tri-states its DO line; without a pull-up you get spurious bytes when CS is inactive. |
| **Never hot-insert a card.** | Inserting a card with power on can latch the card into an undefined state and, occasionally, kill it. Power down, insert, power up. |
| **Format as FAT32 with 32 KB clusters.** | exFAT and NTFS are not worth implementing. Cards > 32 GB ship as exFAT — reformat them, or buy an 8–16 GB card. |
| **Use a genuine, quality card.** | Counterfeit cards report 64 GB and hold 4 GB. Use a **SanDisk Industrial**, **Samsung EVO**, or **Transcend** card bought from an authorised seller. Test with `H2testw` before the flight. |
| **Card must be tested at temperature.** | Cheap cards fail below 0 °C. If your launch site is cold, test in a fridge. |

### 6.2 ⚠️ Why you must not write to the SD card during high-G

This is a genuine, frequently-underestimated failure mode.

| Effect | Mechanism | Consequence |
|---|---|---|
| **Card ejects / contact bounce** | The microSD socket's spring contacts have ~0.1 N of normal force. Under 15–30 g, the card's own mass (0.5 g) produces only 0.15 N — but the *board flex* and the *rotational* accelerations do the damage. | Write returns an error mid-sector → corrupted FAT → **the whole log is unreadable.** |
| **Write latency spikes to 250 ms** | SD cards perform internal garbage collection and wear-levelling. A single write can block for 100–250 ms unpredictably. | The SPI bus is held, the main loop stalls, and you miss IMU samples or the apogee detection window. |
| **Peak current 100 mA** | Erase/program bursts | Rail sag during the highest-vibration, highest-G moment of the flight |
| **Filesystem corruption is unrecoverable** | FAT32 has no journal. A partially-written directory entry can make the file vanish. | ⚠️ **The rule requires an SD log. Losing it fails AV-REQ-05.** |

**Mitigation strategy — the write scheduler:**

```
  Flight phase          SD POLICY
  ─────────────────────────────────────────────────────────────────────
  BOOT / TEST_MODE      Write freely. fsync+close after every test.
  LAUNCH_PAD            Write freely at 1 Hz. This is where you log the
                        30-minute pad-wait voltage curve.
  ASCENT  (T+0 → apogee)  ⛔ NO SD WRITES. Buffer everything in RAM.
  PAYLOAD_SEP / DESCENT   ⛔ NO SD WRITES until 3 s after apogee detection
  APOGEE + 3 s onwards    Resume 20 Hz writes from the RAM ring buffer
  IMPACT                  Flush and close the file. Then stop.
```

**The RAM cost:** at 50 Hz × 30 s of ascent + coast, with a compact **binary** record of 24 bytes (timestamp u32, pressure i32, accel×3 i16, gyro×3 i16, state u8, flags u8 = 24 B), that is `50 × 30 × 24 = 36 kB`. **The STM32F411's 128 kB SRAM absorbs this with room to spare.** This is a concrete reason for choosing the F411 over a Blue Pill (20 kB) — the buffer alone would not fit.

**On-disk format:** two files.

1. **`raw_<TEAM_ID>_<YYYYMMDD>_<HHMMSS>.bin`** — the binary ring buffer, dumped after landing. This is your *primary* engineering record: full-rate, lossless, compact (30 s of ascent ≈ 36 kB; a 4-minute flight at 50 Hz ≈ 300 kB — a 16 GB card holds a thousand flights).
2. **`Flight_<TEAM_ID>.csv`** — the 1 Hz Annexure-2-format text log, written live during the pad wait and descent. This is the file the Jury may ask for.

> 💡 **Post-flight, regenerate the CSV from the binary.** With the full-rate binary you can produce a *perfect* `Flight_<TEAM_ID>.csv` with every sample interpolated to exactly 1.000 s intervals — better than what the live 1 Hz writer could do under load. Do this before handing the USB stick over, but keep both files on it.

**The one thing you must never do:** `fopen`/`fwrite`/`fclose` once per second. Every `fclose` rewrites the FAT directory entry, so a power loss at the wrong instant loses the file. **Open once, write, `f_sync()` every 10 s, and close only at IMPACT.**

### 6.3 The exact competition CSV telemetry format

**Annexure-2 field order — this is normative. Do not reorder, do not rename.**

```
<TEAM ID>, <TIME STAMPING>, <PACKET COUNT>, <ALTITUDE>, <PRESSURE>, <TEMP>,
<VOLTAGE>, <GNSS TIME>, <GNSS LATITUDE>, <GNSS LONGITUDE>, <GNSS ALTITUDE>,
<GNSS SATS>, <ACCELEROMETER DATA>, <GYRO SPIN RATE>, <FLIGHT SOFTWARE STATE>,
<ANY OPTIONAL DATA>
```

**Field specification:**

| # | Field | Units | Resolution | Format string | Example |
|---|---|---|---|---|---|
| 1 | `<TEAM ID>` | — | string | `%s` | `UVCERC01` |
| 2 | `<TIME STAMPING>` | s since power-on (mission clock, survives reset) | 0.01 s | `%.2f` | `184.62` |
| 3 | `<PACKET COUNT>` | — | integer, increments once per packet | `%lu` | `185` |
| 4 | `<ALTITUDE>` | m, **relative to pad** | 0.1 m | `%.1f` | `412.7` |
| 5 | `<PRESSURE>` | Pa, **absolute static** | 1 Pa | `%.0f` | `96542` |
| 6 | `<TEMP>` | °C | 0.1 °C | `%.1f` | `24.3` |
| 7 | `<VOLTAGE>` | V, **CAN-7USAT bus** | 0.01 V | `%.2f` | `5.02` |
| 8 | `<GNSS TIME>` | UTC `hhmmss.ss` | — | `%s` | `071432.00` |
| 9 | `<GNSS LATITUDE>` | ° (signed, N positive) | 0.0001° | `%.4f` | `13.0231` |
| 10 | `<GNSS LONGITUDE>` | ° (signed, E positive) | 0.0001° | `%.4f` | `77.5672` |
| 11 | `<GNSS ALTITUDE>` | m above MSL (ellipsoid/geoid note in CDR) | 0.1 m | `%.1f` | `931.4` |
| 12 | `<GNSS SATS>` | integer count | 1 | `%u` | `9` |
| 13 | `<ACCELEROMETER DATA>` | m/s² | 0.01 m/s² | `%.2f` | `-9.79` |
| 14 | `<GYRO SPIN RATE>` | deg/s (roll axis) | 0.1 deg/s | `%.1f` | `-42.5` |
| 15 | `<FLIGHT SOFTWARE STATE>` | integer 0–7 | 1 | `%u` | `5` |
| 16 | `<ANY OPTIONAL DATA>` | free | — | `%s` | `OK` |

**Notes that go in the CDR:**

- **Field 7 is the CAN-7USAT bus voltage, not the flight-computer battery.** Route the payload bus through your own divider (or read the payload's telemetry) and report *that*. Reporting your own 7.4 V pack here is a misreading of the rules and a Jury will catch it.
- **Field 13, `<ACCELEROMETER DATA>`.** The rules say "accelerometer data" in m/s². Report the **vertical (body-Z) axis** so the value is physically meaningful during boost, and put the full 3-axis vector plus `|a|` in `<ANY OPTIONAL DATA>`:
  `...,5.02,071432.00,13.0231,77.5672,931.4,9,-9.79,-42.5,5,ax=1.23;ay=0.44;az=-9.79;amag=9.90;clip=0`
- **Field 14, `<GYRO SPIN RATE>`.** "Spin rate" = roll rate about the body longitudinal axis. Report the roll-axis gyro, deg/s. Sign convention: positive = right-hand rule about the nose→tail axis. **State your axis convention explicitly in the CDR.**
- **Separator is `, ` (comma + space) or `,`?** The rules show a comma-separated list with spaces for readability. **Emit a bare comma with no space** (`13.0231,77.5672`) — it is unambiguously parseable and every CSV reader handles it. If you want to match the document's visual style, keep the space — but then parse tolerantly.
- **Terminator is `\r` (carriage return, `0x0D`), not `\n`.** This is explicitly stated in the rules. Emit `\r` and, for your own convenience, `\r\n` — but verify that the Jury's parser tolerates the `\n`. **Safest: emit exactly `\r` as the rules say, and configure your own ground station to accept both.**
- **No header row in the transmitted packet.** The rules define a data record. You *may* write a header as the first line of the CSV file — but if the Jury's tooling does not expect it, it will misparse row 1. 💡 **Recommendation: no header in `Flight_<TEAM_ID>.csv`.** Put the column legend in the CDR appendix and in a separate `README.txt` on the USB stick. Do not risk it.

**Exact example line (a single Annexure-2 record):**

```
UVCERC01, 184.62, 185, 412.7, 96542, 24.3, 5.02, 071432.00, 13.0231, 77.5672, 931.4, 9, -9.79, -42.5, 5, OK\r
```

**Exact example CSV file (three records, captured at 1 Hz):**

```
UVCERC01,1.00,1,0.0,101325,26.1,5.02,071230.00,13.0231,77.5672,519.2,8,-9.79,0.3,2,OK
UVCERC01,2.00,2,-0.1,101326,26.1,5.02,071231.00,13.0231,77.5672,519.1,8,-9.80,0.4,2,OK
UVCERC01,3.00,3,0.1,101324,26.2,5.02,071232.00,13.0231,77.5672,519.3,8,-9.78,0.2,2,OK
```

**File naming:** `Flight_<TEAM_ID>.csv` — handed to the Jury on USB **immediately after launch operations.**

### 6.4 Onboard log schema (superset — used to regenerate the required CSV)

`data_<TEAM_ID>_<date>_<time>.csv`, written at 1 Hz during the pad wait and descent, and the high-rate binary file for ascent. The text superset:

```
UVCERC01,185,184.62,412.7,96542,24.3,5.02,071432.00,13.0231,77.5672,931.4,9,-9.79,-42.5,5,OK,7.41,101.2,23.9,9.90,1.23,0.44,-9.79,-42.5,1.8,0.9,0,3,1,0
     │   │     │     │     │     │    │      │       │       │      │  │    │     │   │  │   │     │     │    │    │    │     │     │   │  │  │  │  │
     │   │     │     │     │     │    │      │       │       │      │  │    │     │   │  │   │     │     │    │    │    │     │     │   │  │  │  │  └ 30: SD ok
     │   │     │     │     │     │    │      │       │       │      │  │    │     │   │  │   │     │     │    │    │    │     │     │   │  │  │  └── 29: GNSS fix
     │   │     │     │     │     │    │      │       │       │      │  │    │     │   │  │   │     │     │    │    │    │     │     │   │  │  └──── 28: mag field
     │   │     │     │     │     │    │      │       │       │      │  │    │     │   │  │   │     │     │    │    │    │     │     │   │  └─────── 27: pyro/arm
     │   │     │     │     │     │    │      │       │       │      │  │    │     │   │  │   │     │     │    │    │    │     │     │   └────────── 26: roll rate
     │   │     │     │     │     │    │      │       │       │      │  │    │     │   │  │   │     │     │    │    │    │     │     └────────────── 25: pitch rate
     │   │     │     │     │     │    │      │       │       │      │  │    │     │   │  │   │     │     │    │    │    │     └──────────────────── 24: yaw rate
     │   │     │     │     │     │    │      │       │       │      │  │    │     │   │  │   │     │     │    │    │    └───────────────────────── 23: az
     │   │     │     │     │     │    │      │       │       │      │  │    │     │   │  │   │     │     │    │    └────────────────────────────── 22: ay
     │   │     │     │     │     │    │      │       │       │      │  │    │     │   │  │   │     │     │    └─────────────────────────────────── 21: ax
     │   │     │     │     │     │    │      │       │       │      │  │    │     │   │  │   │     │     └──────────────────────────────────────── 20: |a|
     │   │     │     │     │     │    │      │       │       │      │  │    │     │   │  │   │     └────────────────────────────────────────────── 19: IMU temp
     │   │     │     │     │     │    │      │       │       │      │  │    │     │   │  │   └──────────────────────────────────────────────────── 18: baro temp
     │   │     │     │     │     │    │      │       │       │      │  │    │     │   │  └───────────────────────────────────────────────────────── 17: baro pressure
     │   │     │     │     │     │    │      │       │       │      │  │    │     │   └──────────────────────────────────────────────────────────── 16: VBAT
     └───┴─────┴─────┴─────┴─────┴────┴──────┴───────┴───────┴──────┴──┴────┴─────┴───┴──┴───┴─────┴─────┴────┴────┴────┴─────┴─────┴───┴──┴──┴──┴──┘
      1-15 = the exact Annexure-2 fields, in order  |  16-30 = extra engineering fields (safe to append)
```

**Because fields 1–15 are byte-identical to the required format, you can generate `Flight_<TEAM_ID>.csv` with a one-line `cut -d, -f1-15`.** Design the log so that this is true from day one.

---

## 7. Flight software state machine

### 7.1 The required states (normative — these numbers are what you telemeter)

| # | State | Meaning | Entry condition | Exit condition | Actions |
|---|---|---|---|---|---|
| **0** | `BOOT` | Power-on / reset | Any reset | Self-test passes | Init clocks, load state record from FRAM **before** anything else, verify sensors, report `BOOT` for exactly N packets |
| **1** | `TEST_MODE` | Bench / ground test | Boot self-test pass, or commanded `T` | Command `P` (to pad) | Servos cycle, radio loopback, barometer zeroing, full telemetry, SD write enabled. **Never reachable in flight unless commanded.** |
| **2** | `LAUNCH_PAD` | Armed, waiting for launch | Command `P`, or state recovery | Launch detected | 1 Hz telemetry, GNSS fix monitoring, pad-pressure zeroing, **log the 30-minute voltage curve**, watch for launch |
| **3** | `ASCENT` | Boost + coast, under thrust or coasting up | **Launch detected** (§7.2) | Apogee detected | ⛔ **No SD writes** — buffer in RAM. Track max altitude, max g, max Mach estimate |
| **4** | `PAYLOAD_SEP` | CAN-7USAT separation commanded at 1000 m ± 100 m | Altitude ≥ 900 m **and** ascending | 2 s elapsed, or descent detected | ⭐ Actuate the **payload separation** mechanism. Log the command and the altitude at which it fired |
| **5** | `DESCENT` | Under drogue/main parachute | Apogee detected, **or** 1 s after `PAYLOAD_SEP` | Touchdown detected | ⭐ **Apogee deployment** fires on entry to this state. Resume SD writes 3 s after entry. Track descent rate |
| **6** | `AEROBREAK_RELEASE` | Aerodynamic braking / reefing release | Configurable: a timer after apogee, a pressure threshold, or a commanded event | Timer expiry | Release the aero-brake / reef the main. **Must be reachable from `DESCENT` and must be harmless if it never fires** |
| **7** | `IMPACT` | Landed | Touchdown detected (§7.4) | — (terminal) | **Flush and close the SD file.** Buzzer on. Reduce telemetry to 1 packet / 2 s. Keep transmitting until the battery dies or the team arrives |

**State diagram:**

```
                         ┌──────────────────────────────┐
                         │            (any reset)       │
                         ▼                              │
                    ┌─────────┐                         │
              ┌────▶│ 0 BOOT  │──── self-test fail ─────┤ (retry ×3,
              │     └────┬────┘                          │  then stay in
              │          │ self-test pass                │  TEST_MODE
              │          ▼                               │  and beacon)
              │    ┌─────────────┐   cmd 'P'       │
              │    │ 1 TEST_MODE │─────────────────┘
              │    └──────┬──────┘
              │           │ cmd 'P' / recovered state == 2
              │           ▼
              │    ┌──────────────┐
              │    │ 2 LAUNCH_PAD │◀── recovered state 2 (pad reboot)
              │    └──────┬───────┘
              │           │ LAUNCH DETECTED (§7.2)
              │           ▼
              │    ┌──────────────┐
              │    │  3 ASCENT    │  (buffer only — no SD writes)
              │    └──────┬───────┘
              │           │ alt ≥ 900 m AND ascending
              │           ▼
              │    ┌──────────────────┐
              │    │ 4 PAYLOAD_SEP    │  ⭐ separation actuates
              │    └────────┬─────────┘
              │             │ 2 s OR descent detected
              │             ▼
              │      ┌─────────────┐   APOGEE ─── ⭐ deployment actuates
              │      │  5 DESCENT  │◀──────────── (also entered directly
              │      └──────┬──────┘               from 3 on apogee)
              │             │
              │             ├──────────────▶ ┌──────────────────────┐
              │             │  brake event   │ 6 AEROBREAK_RELEASE  │
              │             │                └──────────┬───────────┘
              │             │                           │ timer done
              │             │◀──────────────────────────┘
              │             │ TOUCHDOWN
              │             ▼
              │      ┌─────────────┐
              └──────│  7 IMPACT   │  (terminal — flush SD, beacon)
                     └─────────────┘
```

### 7.2 Launch detection

**The single hardest decision in the flight software: distinguishing "on the pad, wind buffeting the rocket" from "launch."** A false positive throws you into `ASCENT` on the pad, which (with a naive apogee detector) can fire your deployment while the team is still walking away.

**Recommended detector — require ALL FOUR conditions simultaneously:**

| # | Condition | Threshold | Why |
|---|---|---|---|
| 1 | Axial acceleration (low-pass filtered, body-Z, gravity-removed) | **> 3.0 g** sustained | Real launch is 8–15 g; wind gusts are < 0.5 g |
| 2 | Sustain time | **≥ 200 ms continuously** | Rejects single-sample spikes from a bump or an ESD event |
| 3 | Barometric altitude | **> 15 m above the zeroed pad altitude** | Confirms real displacement, not just a vibration spike. **Do not use this alone** — the barometer lags by 100–300 ms and is noisy at the pad |
| 4 | Velocity estimate | **> 10 m/s upward** | A second, independent confirmation |

**Also required:**

- **Remove the gravity vector before thresholding.** On a pad tilted 5° from vertical, the body-Z accelerometer reads 9.77 m/s², not 9.81. If you compare raw `az` against 3 g you have a 0.2 g bias that changes with launch angle. Compute the gravity direction during the pad-wait period (average 2000 samples while static) and subtract it.
- **Arm the detector only in state 2, and only after `ARM` is asserted.** Before that, no launch detection is even evaluated. This is why `TEST_MODE` must be unreachable in flight.
- **Log the detection event with all four raw values** so you can post-analyse a false trigger.
- **Set a "launch lockout" of 2.0 s after the ARM command** so the arm switch itself (a mechanical event) cannot trigger detection.

```c
/* Launch detector — evaluated at 100 Hz in state 2 */
typedef struct {
    float a_vert_filt;      /* low-pass filtered vertical accel, m/s^2 */
    float v_fused;          /* fused vertical velocity, m/s   */
    float h_rel;            /* altitude above pad, m          */
} flight_t;

bool launch_detected(flight_t *f, uint32_t dt_since_arm_ms)
{
    if (dt_since_arm_ms < 2000) return false;          /* arm lockout      */
    static uint16_t sustain = 0;

    const float A_THRESH   = 3.0f * 9.80665f;   /* 29.4 m/s^2  (3 g)      */
    const float V_THRESH   = 10.0f;             /* 10 m/s upward          */
    const float H_THRESH   = 15.0f;             /* 15 m above pad         */
    const uint16_t SUSTAIN = 20;                /* 20 samples @ 100 Hz    */

    bool ax_ok = (f->a_vert_filt > A_THRESH);
    bool v_ok  = (f->v_fused  > V_THRESH);
    bool h_ok  = (f->h_rel    > H_THRESH);

    if (ax_ok && v_ok && h_ok) {
        if (++sustain >= SUSTAIN) { sustain = 0; return true; }
    } else {
        sustain = 0;
    }
    return false;
}
```

### 7.3 Robust apogee detection

**Requirement: latency ≤ 0.5 s (AV-DER-03).** At 2 m/s descent, half a second is 1 m of extra fall — irrelevant. The real risk is not latency, it is a **false trigger at high altitude**, which deploys the parachute while the rocket is still doing 200 m/s. That shreds the airframe.

**The four false-trigger sources you must design against:**

| # | Source | Signature | Mitigation |
|---|---|---|---|
| 1 | **Motor burn-out spike** | A sharp *positive* acceleration discontinuity of 5–30 g as thrust cuts off and the airframe unloads (often an oscillating "ring"). In a poorly-fused velocity estimate this looks like a velocity reversal. | ⛔ **Hard inhibit: no apogee detection for the first 1.5 s after launch detection**, and none while `a_vert_filt > 0`. Burn-out at 1–3 s is *the* classic false-apogee event. Also: low-pass the accelerometer at 20 Hz before integrating — the ring is 50–300 Hz. |
| 2 | **Mach transition pressure glitch** | Crossing Mach 0.8–1.2, the static port sees a pressure *discontinuity* (a shock sits on the port). The barometer can jump 200–800 Pa, i.e. **17–67 m of false altitude change**, in under a second. If the rocket is near apogee at Mach 1 (unusual but possible on a high-thrust motor) you get a false apogee. | ⛔ **Mach inhibit: no apogee detection while the estimated Mach number is between 0.7 and 1.3.** Estimate Mach from the barometric speed and an ISA temperature: `M = v / sqrt(1.4 × 287 × T)`. At 1000 m apogee and a heavy 2800 N·s motor you will very likely be transonic on the way up — **this inhibit is not theoretical for your vehicle.** Also: place the static port ≥ 4 body diameters back from the nose shoulder, in a region of low pressure gradient, with a **4-hole 2 mm port set** to reduce sensitivity to angle of attack. |
| 3 | **High-altitude barometric noise** | Above ~2000 m the pressure change per metre shrinks (`dP/dh ∝ P`), so the same sensor noise becomes a larger altitude noise, and the velocity estimate gets noisier. At 1 km apogee this is a mild effect, but design for it. | Use the **MS5611** (§4.1) and an OSR of 4096 with a 5-sample moving average. Require *both* a barometric velocity reversal **and** an accelerometer-integrated velocity reversal. |
| 4 | **Vibration rectification** | Under high vibration, a MEMS accelerometer's output includes a DC offset proportional to vibration amplitude ("rectification error"). This biases the integrated velocity. | ⚠️ Real effect: BMI088's dual-die construction exists precisely to mitigate it. Mount the IMU on a rigid aluminium or 2 mm FR4 plate with **silicone grommets**, not foam, and use the **barometer as the truth source** with the accelerometer as a *confirmation*, not a primary. |

**Recommended detector — the "3-of-3 with inhibits" scheme:**

```
  INHIBITS (any true ⇒ apogee detection DISABLED)
    I1:  t_since_launch < 1.5 s
    I2:  a_vert_filt > 0            (still accelerating)
    I3:  0.7 < Mach_est < 1.3       (transonic)
    I4:  state != ASCENT

  CANDIDATE CONDITIONS (evaluated at 50 Hz, all must hold for
                       8 consecutive samples = 160 ms)
    C1:  v_baro   < 0  AND  v_baro_prev > 0      (barometric reversal)
    C2:  v_fused  < 0                             (fused velocity negative)
    C3:  h_rel > 50 m                             (never fire near the pad)

  APOGEE  =  (C1 AND C2 AND C3) AND NOT (I1 OR I2 OR I3 OR I4)
             sustained 160 ms
```

**Backup: the timer.** Independently of the above, arm a **hard apogee timer** on entry to `ASCENT`:

```
  t_apogee_backup = t_launch + t_burn_expected + t_coast_expected + 1.5 s

  For a ~2800 N·s motor on a ~10 kg vehicle:
    t_burn    ≈ 3.5 s  (confirm from the actual thrust curve)
    t_coast   ≈ 13–16 s to apogee (from OpenRocket, worst case)
    t_backup  = 3.5 + 18 + 1.5 = 23 s  after launch detection
```

If the timer expires while still in `ASCENT`, **force the transition to `DESCENT` and deploy**, and **flag the event** in telemetry (`apogee_src=2`). A timer-forced deployment is a mission *save*, not a success — the post-flight analysis must explain why the primary detector did not fire.

### 7.4 Touchdown detection

```
  IMPACT when ANY 2 of:
    T1:  |a_vert| > 3 g for ≥ 3 samples         (landing shock)
    T2:  descent rate < 0.5 m/s for ≥ 2 s       (stopped falling)
    T3:  altitude change < 0.5 m over 5 s       (no longer moving)
```

Then: **flush the SD file, `f_close()` it, and never write again.** This is the most important line in the whole firmware — a flight that lands safely and loses its log is a failed flight.

### 7.5 Processor reset and state recovery

**Requirement AV-REQ-07/08: the state must be recoverable and the mission clock must survive a reset.**

**Where to store it — three options:**

| Storage | Writes | Endurance | Survives reset | Survives power loss | Cost | Verdict |
|---|---|---|---|---|---|---|
| STM32 internal flash (emulated EEPROM) | 10 k cycle/page | 10 k | ✅ | ✅ | ₹0 | ⚠️ Endurance is marginal at a 10 Hz heartbeat (11 days). Fine at a per-transition write only. Flash erase blocks the CPU for ~20 ms. |
| STM32 `BKP` registers (backup domain) | unlimited | ∞ | ✅ | ❌ (unless `VBAT` is backed) | ₹0 | ✅ **Use this for the mission clock and the "reset count"**, backed by a CR2032 on `VBAT`. 20 × 32-bit registers survive a reset and a brown-out. |
| **MB85RC256V FRAM (I2C, 32 kB)** | **10¹² cycles** | effectively ∞ | ✅ | ✅ | ₹180–350 | ✅ **RECOMMENDED primary store.** Unlimited writes means you can checkpoint at 10 Hz with zero endurance worry, and it is non-volatile through a total power loss. Also radiation-tolerant enough for this application. |

**Recommended scheme — belt and braces:**

```
  BKP_DR1  : mission clock seconds  (u32, written 10 Hz)   ← survives reset + brownout
  BKP_DR2  : reset count            (u32, incremented in the reset handler)
  BKP_DR3  : last committed state   (u8)  + CRC8 in BKP_DR4

  FRAM  0x0000 : struct state_record {          ← survives total power loss
                     uint32_t magic;        // 0x55564345 "UVCE"
                     uint32_t seq;          // monotonically increasing
                     double   mission_t;    // seconds since power-on, never reset
                     float    pad_pressure; // Pa, for the 30-min pad wait
                     float    pad_altitude; // m
                     float    max_altitude; // m
                     float    max_g;        // m/s^2
                     float    max_velocity; // m/s
                     uint8_t  state;        // 0..7
                     uint8_t  arm_state;
                     uint16_t crc16;
                 };

  WRITE POLICY
    - On every state transition  : write the full record, fsync, verify readback
    - Every 100 ms in states 3,5,6: write only { mission_t, max_altitude, seq }
    - Every 10 s in state 2       : write the pad reference + battery voltage
```

**Boot sequence with recovery — order matters:**

```c
void boot(void) {
    /* 1. Hardware first: clocks, then the watchdog LAST (see §8) */
    clock_init();
    gpio_init();
    fram_init();       /* I2C — must be up before we read state */
    baro_init();
    imu_init();

    /* 2. Recover state BEFORE initialising anything that could block */
    state_record_t rec;
    bool recovered = false;
    if (fram_read_record(&rec) && rec.magic == 0x55564345
                               && crc16_ok(&rec)) {
        float age = (float)(rtc_seconds() - rec.mission_t);
        /* Only trust the record if it is recent (see below) */
        if (age < 30.0f) {
            g_state       = rec.state;
            g_mission_t   = rec.mission_t;      /* ← CLOCK CONTINUITY */
            g_pad_pressure= rec.pad_pressure;
            g_max_alt     = rec.max_altitude;
            recovered     = true;
        }
    }

    /* 3. If we cannot trust the record, be conservative */
    if (!recovered) {
        g_state     = STATE_BOOT;
        g_mission_t = 0.0;
        /* 💡 If ANY record exists but is untrusted, that means we were
           in flight when things went wrong. Do NOT silently start
           from BOOT while the vehicle is airborne. */
        if (rec.magic == 0x55564345) {
            g_state = STATE_SAFE_HOLD;   /* deploy on the conservative
                                            timer, beacon the fault */
        }
    }

    /* 4. Only NOW start the watchdog */
    iwdg_start(IWDG_1S);
}
```

> ⚠️ **The single worst boot bug in amateur flight computers:** on reset, the code re-runs the normal boot path, decides it is in `BOOT`, and waits for a ground command that will never come — while the rocket is falling. **Every reset must resolve to a *safe* state, never to a state that requires human input.** If you were in `ASCENT` and reset, the correct recovered state is **`DESCENT` with immediate deployment**, not `ASCENT` from zero.

**Reset-source handling:**

| Reset cause | Register flag | Interpretation | Correct state action |
|---|---|---|---|
| Power-on | `RCC_CSR_PORRSTF` | Genuine cold start | `BOOT` — normal flow |
| External `NRST` | `RCC_CSR_PINRSTF` | Someone pressed reset (bench) | `BOOT`, but if a pre-flight record says "in flight", go to `DESCENT` |
| **Independent watchdog** | `RCC_CSR_IWDGRSTF` | **Firmware hang in flight** | Recover the pre-reset state; if it was `ASCENT`, **go to `DESCENT` and deploy now** |
| Software reset | `RCC_CSR_SFTRSTF` | Deliberate | Per the deliberate reason |
| Brown-out | `RCC_CSR_BORRSTF` | Supply sagged | Recover state; treat the battery as suspect; **enter `DESCENT` if it was `ASCENT`** |
| Low-power | `RCC_CSR_LPWRRSTF` | — | Log it; rarely seen here |

**Pen the reset cause to FRAM, always, before anything else in `main()`.** You will need it in the post-flight analysis.

### 7.6 State LED colour code (for the pad team)

| State | Colour | Pattern |
|---|---|---|
| 0 `BOOT` | White | Solid |
| 1 `TEST_MODE` | Blue | Slow blink 1 Hz |
| 2 `LAUNCH_PAD` | Green | Solid (this is what the Jury should see on the pad) |
| 2 `LAUNCH_PAD`, armed | Green | Fast blink 4 Hz |
| 3 `ASCENT` | — | **LED off** (do not waste current or light) |
| 4 `PAYLOAD_SEP` | Magenta | 2 pulses |
| 5 `DESCENT` | Yellow | 2 Hz |
| 6 `AEROBREAK_RELEASE` | Cyan | 5 Hz |
| 7 `IMPACT` | Red | 1 Hz + buzzer |
| Any fault | Red/Blue alternate | Continuous |

---

## 8. Watchdog timers and brown-out detection

### 8.1 The independent watchdog (IWDG)

**Use the IWDG, not the window watchdog (WWDG), as the primary.** The IWDG runs from the **independent 32 kHz LSI oscillator**, so it keeps counting even if the main PLL, the HSE crystal, or the system clock stops. The WWDG runs from the APB clock, so a clock failure takes the watchdog with it.

| Parameter | Recommended value | Rationale |
|---|---|---|
| Timeout | **1000 ms** | The main loop must complete in ≪ 1 s. A 1 s hang during boost is 300 m of unmonitored flight. |
| Prescaler / reload | LSI 32 kHz, prescaler 32 → 1 kHz, reload 999 | Compute from the actual LSI frequency — **measure your LSI**; it can be 26–56 kHz across temperature and parts, which is a ±40 % timeout error. |
| Kick location | **One place only**, at the bottom of the main superloop, and only if every task reported "alive" | ⚠️ **Never kick the watchdog inside an ISR.** A stuck main loop with a happily-firing timer ISR will keep kicking forever; the watchdog becomes decoration. |
| Kick condition | `if (imu_alive && baro_alive && sd_alive_or_not_needed && state_task_ok)` | This is a **supervisory** watchdog, not just a hang detector. |

```c
/* The main superloop — the ONLY place IWDG_KR is written */
while (1) {
    task_heartbeat_update();     /* sets the per-task alive flags      */
    task_sensors();              /* IMU + baro, must complete < 20 ms  */
    task_fusion();               /* Kalman/complementary, < 2 ms       */
    task_state_machine();        /* < 1 ms                             */
    task_logging();              /* buffered — never blocks            */
    task_telemetry();            /* non-blocking UART TX               */
    task_housekeeping();         /* battery, temperature, 10 Hz        */

    /* Kick ONLY if every critical task met its deadline this cycle */
    if (hb_imu_ok() && hb_baro_ok() && hb_state_ok() && hb_fusion_ok()) {
        IWDG->KR = 0xAAAA;       /* ← the one and only kick */
    }
    /* If a task is late, we deliberately do NOT kick, and the reset
       handler will land us in a safe state. */
}
```

**Peripheral-level watchdogs you should also use:**

| Peripheral | Failure it catches | Setting |
|---|---|---|
| **I2C bus timeout** (`I2C_TIMEOUTR`) | A slave holding SDA low forever (very common with a brown-out barometer) | Enable, timeout 25 ms |
| **SPI underrun/overrun** | SD card or IMU desync | Enable the error interrupt and reset the peripheral |
| **UART idle-line + noise detection** | Garbled frames from a marginal RF link | Enable, use framing/parity errors to trigger a re-sync |
| **RTC wakeup timer** | Gives you a 1 Hz heartbeat independent of the main loop | Not a watchdog, but a good independent liveness check |

### 8.2 Brown-out detection (BOR)

| Setting | Value | Why |
|---|---|---|
| STM32 internal BOR level | **Level 2 (≈ 2.7 V)** or the highest available | Below 2.7 V, flash reads are unreliable and the CPU executes garbage. |
| External supervisor | **Optional but recommended: TPS3839 or MCP131** (₹60–150) | The internal BOR is coarse. An external supervisor gives a clean, fast reset assert below 2.93 V. |
| `PWR_CR` | `DBP` set if you use the backup domain | — |
| **Supercapacitor or 1000 µF on `3V3_DIGITAL`** | Hold-up for ~50 ms | Gives the firmware time to write the state record to FRAM during a brown-out before the rail collapses. **This is what makes state recovery actually work.** |

**Brown-out firmware behaviour:**

```c
/* In the PVD (programmable voltage detector) interrupt — fires BEFORE
   the rail drops below the BOR threshold, while there is still hold-up
   energy in the bulk capacitor. */
void PVD_IRQHandler(void) {
    uint32_t t0 = micros();
    if (PWR->CSR & PWR_CSR_PVDO) {
        /* Voltage has fallen below the PVD threshold (~2.9 V) */
        g_flags.brownout_seen = 1;
        fram_write_record_now();        /* ~200 µs on FRAM @ 400 kHz */
        sd_flush_now();                 /* best-effort, 5 ms budget   */
        servos_to_safe();               /* do NOT deploy on brownout  */
        enter_stop_mode_or_halt();
    }
    (void)t0;
}
```

> ⚠️ **Do not deploy on brownout.** A brownout at T−0.5 s on the pad (someone bumps the battery connector) must not fire the parachute. Deploy, or do not deploy — decide, and make the decision explicit in the state machine: **brownout in state 2 ⇒ do not deploy; brownout in state 3/5 ⇒ the backup altimeter is responsible.**

**Test procedure for the watchdog and BOR (put this in the CDR):**

| Test | Method | Pass |
|---|---|---|
| WDT-1 | Insert `while(1);` in the main loop | Board resets within 1.1 s; the reset cause in FRAM reads `IWDGRSTF` |
| WDT-2 | Block only the sensor task | No kick; reset within 1.1 s. **Proves the supervisory logic works** |
| WDT-3 | Reset mid-`ASCENT` | State recovers to `DESCENT`, mission clock continues, deployment fires |
| BOR-1 | Slowly ramp the supply down with a variac/bench supply | Clean reset at 2.7–2.9 V; state record intact in FRAM |
| BOR-2 | Momentary 10 ms interruption of the battery during the pad wait | No reset; no deployment; fault logged |
| BOR-3 | Same interruption during `ASCENT` simulation | Backups take over; primary recovers to `DESCENT` |

---

## 9. Sensor fusion basics

### 9.1 The problem

| Source | Strengths | Weaknesses |
|---|---|---|
| **Barometer** | Absolute, drift-free, no integration error | Noisy (0.1–1 m RMS), 10–50 ms of lag through the vent, **and it cannot tell you velocity without differentiating, which amplifies noise** |
| **Accelerometer** | Fast (1 kHz), no lag, directly measures specific force | Biased, drifts without bound when integrated twice, sensitive to vibration and mounting |

Fusing them gives you an altitude and a velocity that is **both fast and drift-free** — which is exactly what reliable apogee detection needs.

### 9.2 Option A — complementary filter (start here)

The simplest thing that works. The barometer provides the low-frequency truth; the accelerometer provides the high-frequency detail.

```
  h_fused  =  α × (h_fused_prev + v_fused × dt)  +  (1 − α) × h_baro
  v_fused  =  v_fused_prev + (a_vert − g_eff) × dt     then corrected:

  Full form with a velocity correction term:

      h_pred = h + v·dt
      v_pred = v + (a − g)·dt

      h = h_pred + Kp_h × (h_baro − h_pred)
      v = v_pred + Kv   × (h_baro − h_pred)      ← the correction also
                                                    fixes velocity drift
```

**Choosing the gains — the crossover frequency:**

```
  ω_c = desired crossover (rad/s). Rule of thumb: the filter trusts the
        barometer below ω_c and the accelerometer above it.

  Kp_h = 2ζω_c
  Kv   = ω_c²

  For rocketry:  ζ = 0.7 (critically damped), ω_c ≈ 0.5 rad/s (0.08 Hz)
      Kp_h = 2 × 0.7 × 0.5 = 0.70
      Kv   = 0.5² = 0.25
```

⚠️ **Tuning note that matters:** pick ω_c too high and the filter follows the barometer's noise, so your velocity estimate is garbage exactly when you need it (near apogee). Pick it too low and the filter lags the true apogee by seconds. **0.3–0.7 rad/s is the right band for a vehicle that reaches apogee in 15–20 s.** Tune it against a recorded flight or a simulated trajectory, not by feel.

**Discrete implementation (run at 50 Hz):**

```c
#define DT        0.02f          /* 50 Hz                        */
#define KP_H      0.70f
#define KV        0.25f
#define G         9.80665f

void complementary_update(float h_baro, float a_vert_meas, float *h, float *v)
{
    float h_pred = *h + (*v) * DT;
    float v_pred = *v + (a_vert_meas - G) * DT;
    float err    = h_baro - h_pred;

    *h = h_pred + KP_H * err;
    *v = v_pred + KV   * err;
}
```

### 9.3 Option B — 1-D Kalman filter (the upgrade)

**State vector** (3 states, vertical channel only — a full 6-DOF attitude filter is out of scope for a first vehicle):

```
  x = [ h    ]     altitude above pad (m)
      [ v    ]     vertical velocity (m/s)
      [ b_a  ]     accelerometer bias (m/s^2)   ← estimating this is the
                                                  whole point
```

**Prediction (every 20 ms, driven by the accelerometer):**

```
  F = [ 1   dt  −dt²/2 ]
      [ 0   1   −dt    ]
      [ 0   0    1     ]

  x⁻ = F x
  P⁻ = F P Fᵀ + Q          Q = diag(q_h, q_v, q_ba)
```

**Update (every 100 ms, when a barometer sample arrives):**

```
  H = [ 1  0  0 ]          (the barometer measures altitude directly)

  y = h_baro − H x⁻                      innovation
  S = H P⁻ Hᵀ + R                        R = barometer variance (m²)
  K = P⁻ Hᵀ S⁻¹                         Kalman gain (3×1)
  x = x⁻ + K y
  P = (I − K H) P⁻
```

**Tuning values that work for a 1 km flight:**

| Parameter | Value | How to get it |
|---|---|---|
| `dt` | 0.02 s (50 Hz) | Fixed — do not use a measured `dt`; a jittery `dt` injects noise into `Q` |
| `R` (barometer measurement variance) | `(0.3 m)² = 0.09` | **Measure it:** log 60 s of barometer data on the pad and compute the variance of `h` after a 5-sample moving average. Do not guess. |
| `q_h` (altitude process noise) | `(0.05 m)² per s` | Small — the altitude process is smooth |
| `q_v` (velocity process noise) | `(0.5 m/s²)² per s` | Larger — the real acceleration is not exactly what the accelerometer says |
| `q_ba` (bias random walk) | `(0.001 m/s²)² per s` | Very small — bias changes slowly |
| `P0` | `diag(100, 100, 1)` | Large initial uncertainty |

⚠️ **A Kalman filter that is badly tuned is worse than a complementary filter**, because it lies with confidence. **If you are short on time, ship the complementary filter** (§9.2). It has two gains you can reason about, and it degrades gracefully. Ship the Kalman filter only if you have bench data to tune it against and time to validate it in a drop test.

### 9.4 The gravity-subtraction detail that trips everyone up

An accelerometer measures **specific force**, not acceleration:

```
  a_measured = a_true + g_vector        (in the body frame)
```

On the pad, at rest, a vertical-axis accelerometer reads **+9.81 m/s²**, not 0. During boost it reads `thrust_accel + 9.81`. If you integrate the raw reading you get a velocity that grows by 9.81 m/s every second — a 150 m/s error by apogee.

**Correct approach:**

1. During the pad wait, average 2000 samples while static. That average **is** the gravity vector in the body frame (plus the mounting misalignment).
2. Store it as `g_body[3]`.
3. In flight, `a_vert = -(a_body · z_body) - g_eff` where `g_eff` is the component of the stored gravity along the body axis.
4. Better (and this is the professional approach): **estimate the bias inside the Kalman filter** — that is what the third state in §9.3 is for. It removes the need for a perfect pre-flight gravity measurement and compensates for the accelerometer's temperature drift over the pad wait.

💡 **Re-zero the accelerometer whenever the vehicle has been static for 5 s in states 0, 1, or 2.** That way, a 25-minute pad wait with a 15 °C temperature rise does not leave you integrating a stale bias.

### 9.5 Validation plan for the fusion

| Test | Method | Pass criterion |
|---|---|---|
| FUSE-1 | Static, 10 minutes on the bench | `h_fused` stays within ±0.5 m; `v_fused` stays within ±0.1 m/s |
| FUSE-2 | Lift the vehicle 3 m by hand, hold 10 s, lower it | `h_fused` peaks at 3.0 m ± 0.3 m; returns to 0 ± 0.3 m |
| FUSE-3 | **Vacuum chamber test** — pull a vacuum equivalent to 1000 m in 20 s, hold, release | `h_fused` tracks the known pressure-derived altitude; apogee detector fires **exactly once**, at the pressure minimum |
| FUSE-4 | **Drop test** — drop the avionics bay from 10 m into a soft catch | Apogee detector fires at the top of the drop, not during the fall or on impact |
| FUSE-5 | Simulated flight — replay a recorded acceleration/pressure profile through the filter | `h`, `v` match the reference within 5 % and 0.5 m/s |
| FUSE-6 | Motor burn-out profile replay (the spike) | **No false apogee trigger** |

> 💡 **The vacuum test is the one that wins the CDR.** A hand vacuum pump and a cheap acrylic chamber (₹800–2,000 total) lets you demonstrate apogee detection end-to-end without flying. No other team will have done it.

---

## 10. PCB design guidance

### 10.1 Perfboard vs. custom PCB — make the decision explicitly

| Factor | Perfboard / veroboard | Custom PCB (2-layer) | Custom PCB (4-layer) |
|---|---|---|---|
| Cost (one-off) | ₹50–150 + wire | **₹600–1,800 for 5 boards** (JLCPCB/PCBWay + ₹350 shipping, or ₹900–2,500 from Indian houses like **Robu PCB**, **Elecrow India**, **LionCircuits (Bengaluru)**, **PCB Power (Gandhinagar)**) | ₹2,000–5,000 for 5 |
| Lead time | Same day | 7–14 days (China), 5–10 days (India) | 10–20 days |
| Vibration survival | ⚠️ Poor — through-hole leads fatigue and crack, wires chafe | ✅ Good | ✅ Good |
| Repeatability | ❌ Every build is different | ✅ Identical copies | ✅ |
| Ground plane | ❌ None | ✅ One continuous plane | ✅ Two |
| Noise on the ADC | ⚠️ 50–500 mV of digital hash | ~10–30 mV | ~5–15 mV |
| Debuggability | ✅ Easy to rework | ⚠️ Needs hot air | ⚠️ |
| Time to first working unit | 4–10 h of soldering | 2–3 weeks | 3–4 weeks |
| CRD/grading optics | ❌ Looks like a school project | ✅ Looks like engineering | ✅ |

**Recommendation for UVCE Rocketry:**

| Stage | Build this | Why |
|---|---|---|
| **Phase 0–1 (learning, static tests, first low-power flights)** | **Perfboard.** Build the FCB on 2.54 mm FR4 perfboard with a **hand-wired ground bus** and point-to-point sensor wiring on short leads. | You will change the pinout 5 times. Perfboard lets you. |
| **Phase 1–2 (the competition vehicle)** | **Custom 2-layer PCB** for the FCB, 1.6 mm FR4, with a ground pour on both layers. Keep the deployment driver on a **separate perfboard or a second small PCB**. | Vibration, repeatability, the CDR, and the fact that you want **two flight computers** (flight + spare) that behave identically. |
| **Only if you have noise problems you cannot solve** | 4-layer (signal / GND / PWR / signal) | Fixing a grounding problem with a stackup is legitimate; doing it preemptively at this scale is not. |

### 10.2 Layout rules for a 2-layer flight board

```
  ┌───────────────────────────────────────────────────────────────────┐
  │  LAYER 1 (TOP)                                                    │
  │    • Ground pour, stitched to bottom with vias every 5 mm         │
  │    • Signals routed on top where possible                        │
  │    • ANALOG ZONE (left): MS5611, ADC divider, MCP6002, VREF       │
  │    • DIGITAL ZONE (centre): STM32, FRAM, crystal                  │
  │    • POWER ZONE (right): bucks, inductors, servo connectors       │
  │    • ⛔ No traces cross a zone boundary except at one point       │
  ├───────────────────────────────────────────────────────────────────┤
  │  LAYER 2 (BOTTOM)                                                 │
  │    • Continuous ground plane — NO SLOTS, NO LONG SIGNAL TRACES    │
  │    • If you must route on the bottom, keep the ground return      │
  │      continuous underneath the trace (no plane cuts)              │
  └───────────────────────────────────────────────────────────────────┘
```

| # | Rule | Reason |
|---|---|---|
| 1 | **Single-point analog/digital ground tie**, under the MCU's `VSSA` pin. Star from there. | Prevents digital return currents flowing through the analog reference |
| 2 | Keep the **buck converter's hot loop** (input cap → switch pin → inductor → output cap) under **10 mm** of loop area | The switching loop is the antenna. A big loop radiates into everything |
| 3 | **Never route SPI under the barometer.** Route around it, or on the other layer with the ground plane intact between | SPI at 20 MHz couples capacitively into a 0.012 Pa sensor |
| 4 | **Guard the IMU and barometer with a ground ring** connected to the plane with vias | Shields against the RF field from the XBee |
| 5 | **Keep the XBee ≥ 25 mm from the barometer** and, ideally, on a separate board | A 2 W 2.4 GHz transmitter 10 mm from a MEMS pressure sensor is a bad idea |
| 6 | **Crystal/oscillator: ≤ 10 mm from the MCU, no traces under it, guard ring, ground island** | Clock noise is broadband |
| 7 | **Series-terminate fast signals** (SPI clock 22–100 Ω at the source) | Ringing on a 20 MHz clock is a real EMI source |
| 8 | **Connector retention: through-hole, or SMD with a mechanical anchor.** Add a **strain-relief hole** for every wire | Wires pull off SMD pads under vibration |
| 9 | **Silkscreen every net name.** Put `VBAT`, `3V3A`, `3V3D`, `GND`, `SCK` on the silk next to the pad | You will be debugging this at 05:00 on launch day |
| 10 | **Test points on every rail + the ADC input + the reset line.** 1 mm pads, labelled | Same reason |
| 11 | **Fiducials** on three corners | Assembly and inspection |
| 12 | **Mark the board with the club name, revision, and date in copper** | The CDR photographs look better and you will need to tell rev A from rev C |
| 13 | **Add a mounting-hole pattern that matches your shock grommets** — 4 × M3 at a 40 × 40 mm pitch is a good default | Standardisation |

### 10.3 Mechanical and environmental design (this is where flights fail)

| Concern | Design action |
|---|---|
| **Vibration (15 g axial, broadband)** | Mount the FCB on **4 × silicone grommets** (M3, 60 Shore A) — **not** foam, which compresses and lets the board slap. Put a **nylon standoff through the grommet** so the screw cannot over-compress it. |
| **Shock (30 g opening)** | Every component > 1 g needs a mechanical anchor: through-hole, or SMD with an **epoxy dot** ("staking") at the corners. The SD socket and the servo connectors are the two parts that will come off. |
| **SD card retention** | A microSD in a push-push socket under vibration **will** walk out. Use a **push-pull socket with a locking tab**, or put a **zip tie / Kapton tape strap** across the card. ⚠️ **Do not rely on friction.** |
| **Battery retention** | 18650 cells are 45 g each. Under 30 g they exert 13 N. Use a **holder with a locking clip or a soldered tab**, plus a strap. A cell that ejects becomes a projectile inside the bay. |
| **Condensation / humidity** | Conformal coat (silicone or acrylic, e.g. MG Chemicals 422B) everything **except**: the barometer port, the SD socket contacts, the servo connector pins, and any test points. |
| **Thermal** | Bucks dissipate 0.3–0.6 W. Give them copper pour and ≥ 10 mm clearance from the barometer (self-heating corrupts the pressure reading by ~0.4 Pa/°C at constant altitude — a slow altitude drift). |
| **Bay venting** | **Four 2 mm holes** in the airframe at the barometer location, arranged around the circumference, with an internal light baffle. This gives an acoustic cutoff around 1 Hz: fast enough to track the flight, slow enough to reject the pressure pulse from the parachute charge and from angle-of-attack changes. ⚠️ A single large hole gives you a resonance that will ring for seconds at apogee. |
| **EMI from the XBee** | Keep the antenna oriented so its null pattern is away from the avionics. Never coil the antenna against the FCB. |

### 10.4 Bring-up and test sequence for a new board

| Step | Action | Expected |
|---|---|---|
| 1 | Visual inspection under magnification **before** power | No solder bridges, no tombstoned parts |
| 2 | Resistance to GND on `VBAT`, `5V_CLEAN`, `3V3_DIGITAL`, `3V3_ANALOG` | > 10 kΩ each. **If it is < 100 Ω, find the short before applying power.** |
| 3 | Current-limited bench supply at 7.4 V, **50 mA limit** | < 20 mA idle |
| 4 | Verify each rail with a scope (not just a DMM) | 3.30 V ± 3 %, ripple < 20 mV on digital, < 5 mV on analog |
| 5 | MCU alive: blink an LED | — |
| 6 | FRAM read/write/verify | Pass |
| 7 | Barometer `WHO_AM_I` / PROM read | Correct ID; PROM values sane (not all 0x00/0xFF) |
| 8 | IMU `WHO_AM_I` | Matches the datasheet |
| 9 | SD card init + write + read back + verify | Pass with a known test pattern |
| 10 | Servo sweep under load | No rail sag below 5.0 V |
| 11 | **Radio at full power, transmitting continuously** | Repeat steps 4 and 7. **Barometer noise must not increase by more than 2×.** If it does, you have an RF-coupling problem — fix it before flight. |
| 12 | 45-minute soak logging `VBAT` | §5.6 criteria |
| 13 | Vibration / shake test (paint shaker, or a speaker-driven plate) | No resets; log intact; no false launch detection |

---

## 11. Where the flight computer sits in the mass and power budget

### 11.1 Mass budget (avionics bay)

| Item | Mass (g) | Notes |
|---|---|---|
| FCB (50 × 60 mm, 1.6 mm FR4, populated) | 28 | Include the connectors |
| Radio board + XBee-PRO S1 (no antenna) | 22 | XBee-PRO is 3 g; the board and socket dominate |
| Deployment driver board | 18 | Relays/MOSFETs, bulk caps, connectors |
| Antenna (¼-wave whip + SMA + coax) | 18 | Or 12 g for a wire dipole |
| 2 × 18650 protected cells | 96 | 45–48 g each |
| 18650 holder / soldered tabs | 14 | |
| Avionics sled (3 mm ply + 3D-printed PETG brackets) | 55 | |
| SD card | 1 | |
| Wiring harness (22 AWG silicone) | 35 | Silicone insulation stays flexible in the cold |
| GNSS module + patch antenna + CR2032 | 22 | |
| **COTS backup altimeter + its own battery** | **65** | ⚠️ **Mandatory** — budget for it |
| Switch, arming plugs, connectors, fasteners | 30 | |
| **Total** | **≈ 404 g** | Against AV-DER-07 (≤ 500 g) ✅ |
| **With margin for the unexpected** | **≈ 480 g** | ✅ |

### 11.2 Where the mass actually matters

At a ~10 kg lift-off mass, 404 g of avionics is **4 % of the vehicle**. Rule 5.i requires lift-off mass within **±5 %** of the design value — so avionics is a first-order contributor to a rule you can fail. **Weigh every single board on a jewellery scale and put the measured values in the CDR.** Estimated masses are how teams lose the ±5 % margin.

### 11.3 Power and mass interface to the rest of the vehicle

| Interface | Value | Goes in the CDR as |
|---|---|---|
| Battery pack | 2S 18650, 7.4 V nominal, 2600 mAh, 19.2 Wh | With a photograph of the metal-can cells |
| Pad-wait endurance | ≥ 14 h computed, 45 min required | §5.6 test log |
| Peak current | 2.5 A (both servos stalled simultaneously) | Motor/battery interface budget |
| Servo rail | 6.0 V, 3 A converter, 2200 µF bulk | |
| Telemetry | 1 Hz, ≥ 15 fields, `<CR>`-terminated ASCII | Annexure-2 compliance table |
| Avionics mass | 404 g (measured) | Mass budget |
| Centre of gravity shift | Compute from the actual sled position | Stability margin |

---

## 12. Assembly checklist — a compact reference

- [ ] Battery is **metal-cased 18650 / NiMH / alkaline** — no LiPo anywhere in the vehicle
- [ ] Battery voltage logged every 10 s during the 45-minute soak; slope extrapolates to > 90 min
- [ ] Barometer zeroed at the pad; altitude reads 0.0 m ± 0.1 m
- [ ] Accelerometer zeroed at the pad with the vehicle at launch angle
- [ ] **COTS backup altimeter present, independently powered, wired to a redundant deployment path**
- [ ] FRAM state record verified: power-cycle mid-state and confirm recovery
- [ ] IWDG enabled at 1 s, kicked from exactly one place
- [ ] `RCC_CSR` reset flags logged on every boot
- [ ] PVD at 2.9 V; hold-up capacitor sized and verified
- [ ] SD card tested with `H2testw`, formatted FAT32, write-verified
- [ ] ⛔ SD writes disabled from launch detection to apogee + 3 s
- [ ] Telemetry ON/OFF verified by RF command from the ground station
- [ ] Telemetry packet byte-compared against the Annexure-2 template
- [ ] NETID/PANID == team number, screenshot in the CDR
- [ ] Rocket and payload on **different channels**; interference test logged
- [ ] Apogee inhibit windows (1.5 s post-launch, positive accel, transonic) verified by replay
- [ ] Timer backup armed and its expiry value documented
- [ ] Touchdown detection verified by a ground drop test
- [ ] Every board weighed; total avionics mass in the mass budget
- [ ] **Vacuum chamber test passed: apogee detector fires exactly once**
- [ ] Spare FCB built, flashed, and functionally identical

---

*Prepared for UVCE Rocketry Club, Bengaluru. Prices are Indian retail order-of-magnitude figures (2026) and must be re-quoted at the time of purchase — see [Electronics BOM and Sourcing](Electronics_BOM_and_Sourcing.md) for supplier-specific sourcing, counterfeit-avoidance guidance, and the priced BOM.*
