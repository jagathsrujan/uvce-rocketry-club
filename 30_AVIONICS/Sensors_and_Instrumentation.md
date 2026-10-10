# Sensors and Instrumentation — UVCE Rocketry Club

**Document:** `30_AVIONICS/Sensors_and_Instrumentation.md`
**Rev:** 1.0 · **Status:** Design baseline for PDR
**Scope:** Every sensor on the vehicle and the static test stand — principle, specs, interface, cost, failure modes, calibration

> **Companion documents:** [Flight Computer Architecture](Flight_Computer_Architecture.md) · [Communications and Ground Station](Communications_and_Ground_Station.md) · [Recovery Electronics and Control](Recovery_Electronics_and_Control.md) · [Electronics BOM and Sourcing](Electronics_BOM_and_Sourcing.md)

---

## 0. Index and quick-reference

| § | Sensor | Interface | Cost (INR) | Criticality |
|---|---|---|---|---|
| 1 | **Barometric pressure** (MS5611 / BMP390 / BMP280) | I2C / SPI | ₹120–900 | ⭐ **Primary altitude source** |
| 2 | **IMU** (ICM-42688-P / BMI088 / ICM-20948) | SPI | ₹450–1,600 | ⭐ **Launch + apogee confirmation** |
| 3 | **GNSS** (u-blox NEO-M8N + NavIC options) | UART | ₹600–3,200 | Mandatory field |
| 4 | **Temperature** (baro on-die / DS18B20 / K-type + MAX31855) | I2C / 1-Wire / SPI | ₹0–1,500 | Mandatory field + test stand |
| 5 | **Voltage sensing** (divider + buffer) | Analog → ADC | ₹60 | ⭐ Mandatory field |
| 6 | **Current sensing** (INA219 / INA226 / ACS758) | I2C / analog | ₹180–1,100 | Test stand + housekeeping |
| 7 | **Load cell** (static thrust stand) | Analog → HX711 / INA125 | ₹350–8,000 | Test stand |
| 8 | **Pressure transducer** (chamber pressure) | Analog / I2C | ₹900–40,000 | Test stand |
| 9 | **Analog signal integrity** (noise, grounding, shielding, filtering) | — | — | Cross-cutting |
| 10 | **Calibration master schedule** | — | — | Cross-cutting |

### The five sensor rules for this club

1. **Never trust a datasheet resolution as your achievable resolution.** The BMP280 claims 0.16 Pa; in a real board next to a 2.4 GHz transmitter you will see 3–20 Pa of noise. **Measure your noise floor on every board and write it in the log.**
2. **Every sensor that reports a physical quantity needs a calibration record with a date, a method, and a person's name.** Put the record in the CDR.
3. **Zero at the pad, always.** Absolute accuracy is irrelevant for altitude; repeatability and drift over 30 minutes are everything.
4. **Cross-check every critical measurement with a second, physically different sensor.** Barometer vs. GNSS altitude, accelerometer-integrated velocity vs. barometric velocity, two barometers against each other.
5. **⚠️ Buy from a traceable supplier.** The Indian market for IMU and barometer breakouts is full of counterfeit, refurbished and mislabelled parts. See §11.

---

## 1. Barometric pressure sensor

### 1.1 Operating principle

A **piezoresistive MEMS pressure sensor** is a silicon diaphragm with four piezoresistors diffused into its edge, connected as a **Wheatstone bridge**. Applied pressure deflects the diaphragm; the resulting strain changes the resistors' values; the bridge produces a differential voltage proportional to pressure. On-chip circuitry amplifies, temperature-compensates, and digitises it.

```
        ┌─────────────────────────────────────────────────────────┐
        │  SILICON DIAPHRAGM (≈ 1 mm square, ≈ 5 µm thick)        │
        │                                                         │
        │        R1 ──────┬────── R2          R1..R4 are          │
        │                 │                   piezoresistors      │
        │              V_out +                  implanted at the  │
        │                 │                     diaphragm edge    │
        │        R4 ──────┴────── R3                              │
        │                 │                                       │
        │              V_out −                                    │
        │                                                         │
        │   ▲ PRESSURE applied from below → diaphragm bows up      │
        │     → R1,R3 in tension (R↑);  R2,R4 in compression (R↓)  │
        │     → bridge imbalance ∝ pressure                        │
        └─────────────────────────────────────────────────────────┘
                                 │
                                 ▼
        ┌─────────────────────────────────────────────────────────┐
        │  ASIC:  PGA  →  24-bit ΔΣ ADC  →  digital filter        │
        │         + on-chip temperature sensor for compensation   │
        │         + factory calibration coefficients in PROM      │
        └─────────────────────────────────────────────────────────┘
```

**Capacitive** variants (Infineon DPS368, some Bosch parts) measure diaphragm deflection as a capacitance change instead. They tend to have lower noise and better long-term stability, and they are less commonly counterfeited.

**Why this matters for a rocket:** the sensor is only as good as its **port**. A piezoresistive die behind a 0.5 mm hole in a plastic package, mounted inside an airframe with four 2 mm vent holes, has a **pneumatic low-pass filter** between the outside air and the diaphragm. That filter's cutoff frequency is what determines whether you can track a real flight. Get it wrong and you either (a) lag apogee by seconds, or (b) ring for seconds after a pressure transient.

### 1.2 The physics — how pressure maps to altitude

**International Standard Atmosphere (ISA), troposphere (0–11 km):**

```
  T(h)  = T0 − L·h            T0 = 288.15 K,  L = 0.0065 K/m
  P(h)  = P0 · (1 − L·h/T0)^(g·M/(R·L))
        = P0 · (1 − 2.25577e-5 · h)^5.25588

  Inverted (what you actually compute):
  h(P)  = 44330.77 · [ 1 − (P/P0)^(1/5.25588) ]        metres
```

**The sensitivity numbers to memorise:**

| Altitude | Pressure | dP/dh | Altitude change per 1 Pa | Altitude change per 1 hPa |
|---|---|---|---|---|
| **0 m (sea level)** | **101 325 Pa** | **−11.99 Pa/m** | **0.0834 m** | 8.34 m |
| 500 m | 95 461 Pa | −11.30 Pa/m | 0.0885 m | 8.85 m |
| **1000 m (your apogee)** | **89 875 Pa** | **−10.64 Pa/m** | **0.0940 m** | 9.40 m |
| 2000 m | 79 501 Pa | −9.42 Pa/m | 0.1062 m | 10.62 m |
| 5000 m | 54 020 Pa | −6.40 Pa/m | 0.1563 m | 15.63 m |

**The design consequence:** the rules require **0.1 m altitude resolution**. At 1000 m you need to resolve **10.6 Pa** to see 1 m, so **1.06 Pa to see 0.1 m**. Every sensor in §1.3 claims better than that on paper. But:

```
  ⚠️  Resolution ≠ accuracy ≠ noise floor.

  Datasheet "resolution" is the ADC LSB — the smallest NUMBER the sensor
  can output, not the smallest CHANGE it can reliably detect.

  Your achievable altitude resolution =
        (RMS pressure noise) × (dP/dh at that altitude)

  A BMP280 with 3 Pa RMS noise  →  3 × 0.094 = 0.28 m RMS
  ⚠️ That is WORSE than the 0.1 m the rules require, even though the
     datasheet says 0.16 Pa resolution (0.015 m).

  An MS5611 with 0.5 Pa RMS noise →  0.5 × 0.094 = 0.047 m RMS  ✅
```

> 🔬 **This is the single most important number in the avionics design.** Measure it: put the sensor on the bench, log 60 s at 100 Hz, remove the mean, and compute the standard deviation of the residual. That is your RMS noise. Multiply by 0.094 for your achievable resolution at 1000 m. **Put this measurement in the CDR.**

### 1.3 Sensor comparison

| Sensor | Principle | Range | ADC / resolution | Datasheet RMS noise | **Measured** noise (typical good board) | Sample rate | Interface | Addresses | Cost (INR) |
|---|---|---|---|---|---|---|---|---|---|
| **Bosch BMP280** | Piezoresistive | 300–1100 hPa | 20-bit, 0.16 Pa | 0.12 Pa (OSR×16, indoor) | **2–8 Pa** (⚠️ board-dependent) | up to 157 Hz | I2C `0x76`/`0x77` or SPI | 2 | ₹120–250 |
| **Bosch BME280** | BMP280 + humidity | 300–1100 hPa | 20-bit, 0.16 Pa | 0.12 Pa | 3–10 Pa | up to 157 Hz | I2C/SPI | 2 | ₹180–350 |
| **TE MS5611-01BA03** ⭐ | Piezoresistive, 24-bit ΔΣ | 10–1200 mbar | **24-bit, 0.012 Pa** | **0.05 Pa** (OSR 4096) | **0.3–1.5 Pa** | up to 100 Hz | I2C `0x76`/`0x77` or SPI | 2 | ₹450–900 |
| **TE MS5607-02BA03** | Same family, wider range | 10–1200 mbar | 24-bit | 0.06 Pa | 0.4–1.8 Pa | 100 Hz | I2C/SPI | 2 | ₹350–700 |
| **Bosch BMP390** ⭐ | Piezoresistive | 300–1250 hPa | 24-bit, 0.024 Pa | **0.03 Pa** | **0.4–2 Pa** | up to 200 Hz | I2C/SPI | 2 | ₹400–700 |
| **Bosch BMP581** | Piezoresistive | 300–1250 hPa | 24-bit, 0.0068 Pa | **0.0068 Pa** | 0.2–1 Pa | up to 240 Hz | I2C/SPI | 2 | ₹850–1,400 |
| **Infineon DPS368** | **Capacitive** | 300–1200 hPa | 24-bit, 0.002 Pa | 0.06 Pa | 0.5–3 Pa | up to 128 Hz | I2C/SPI | 2 | ₹350–600 |
| **Bosch BMP085/BMP180** | Piezoresistive | 300–1100 hPa | 19-bit, 3 Pa | 3 Pa | 10–30 Pa | 128 Hz | I2C `0x77` | 1 | ₹80–180 |

**Selection guidance:**

| Situation | Choose | Why |
|---|---|---|
| **Best available within budget** | **MS5611-01BA03** | 24-bit ΔΣ, 0.012 Pa LSB, and a real 10× noise advantage over the BMP280 in practice. This is what the professional amateur flight computers (Altus Metrum, Featherweight) have historically used |
| **Modern, best sourcing in India** | **BMP390** | Bosch's replacement for the BMP280 with 4× lower noise and genuine availability. If you cannot get a *verified* MS5611, take this |
| **Tightest budget, two sensors** | **2 × BMP280 from two different suppliers** | Two cheap sensors that agree is better than one expensive sensor you cannot cross-check. Cross-checking catches the failure mode that matters (drift/stuck) |
| **Avoid** | **BMP180/BMP085**, unbranded "pressure sensor" modules | Obsolete, 20× noisier, and the module market is saturated with fakes |
| **Avoid for flight** | **BME280** (humidity channel) | The humidity measurement self-heats the die by 0.5–1.5 °C; temperature drift shifts the pressure reading. In a sealed avionics bay, humidity is meaningless. **Use BME280 only for the ground station's weather station** |

### 1.4 Why you MUST zero at the pad

**The barometer measures absolute pressure. Altitude is a *derived* quantity that depends on the reference pressure `P0`.**

| Error source | Magnitude | Effect on altitude if not corrected |
|---|---|---|
| **Weather (synoptic) variation** | ±3 000 Pa (±30 hPa) seasonally | **±250 m** ⚠️ |
| **Daily weather change** | ±500 Pa over 12 h | ±42 m |
| **Bengaluru's altitude vs. sea level** | ~920 m → P ≈ 90 500 Pa | **~900 m** if you use 101 325 Pa as the reference |
| **Bench-to-pad temperature change** | 15 °C over 30 min | ~1–3 Pa of sensor offset drift → 0.1–0.3 m |
| **Door/hatch closure and body temperature** | 50–300 Pa transient | 4–25 m for minutes |

**The rule requires relative altitude** (`<ALTITUDE>` is relative to ground, resolution 0.1 m). So:

```
  ⭐ PROCEDURE (this is what the ground station's ZERO command does)

  1. Vehicle on the pad, at the launch angle, hatches closed, in FINAL
     flight configuration.
  2. Wait 90 s for thermal equilibration (the sensor warming from your
     hand to ambient is 0.5–3 Pa of offset).
  3. Sample the barometer at 100 Hz for 10 s.
  4. Compute a MEDIAN (not a mean — rejects a transient).
  5. Store as P0_pad. Report it in the ZERO ACK: ACK:ZERO:<P0>:<h>
  6. Also store the MEAN of the accelerometer over the same 10 s as
     the gravity vector g_body[3].
  7. All altitude thereafter: h = 44330.77 × [1 − (P/P0_pad)^(1/5.25588)]

  ⚠️ Re-zero if:
       • more than 20 minutes have passed since the previous zero
       • the vehicle has been moved
       • the ambient temperature has changed by more than 5 °C
       • the harbour/hatch has been opened
```

**Cross-check the reference:** you can sanity-check the zero against the **GNSS altitude at the pad** (which reads height above the WGS-84 ellipsoid or MSL depending on the module). They will differ by the geoid-ellipsoid separation (in Bengaluru, the geoid undulation is roughly **−60 to −90 m**), so do not expect them to match without a geoid model. **Use the GNSS altitude only as a coarse plausibility check (±150 m), and use the barometer for all precision work.** Document the distinction in the CDR.

### 1.5 Temperature compensation

Every one of these sensors is **temperature-dependent**, and the compensation is either internal (factory-calibrated coefficients in PROM) or your job.

**MS5611 — read the PROM and use it:**

```
  The MS5611 has a 6-coefficient calibration PROM that MUST be read
  once at startup and checked:

      C1 = Pressure sensitivity           (SENS_T1)
      C2 = Pressure offset                (OFF_T1)
      C3 = Temperature coefficient of pressure sensitivity  (TCS)
      C4 = Temperature coefficient of pressure offset       (TCO)
      C5 = Reference temperature          (T_REF)
      C6 = Temperature coefficient of temperature           (TEMPSENS)

  ⚠️ VALIDATION: read the PROM twice at startup. If any coefficient
     differs between reads, or if any is 0x0000 or 0xFFFF, the sensor or
     the I2C bus is faulty. FAIL LOUDLY — do not fly with an unvalidated
     PROM. A silent PROM failure gives you a pressure that looks
     plausible and is wrong by hundreds of metres.

  Typical genuine values: C1 ≈ 40000-50000, C2 ≈ 40000-50000,
                          C3 ≈ 250-350, C4 ≈ 200-300, C5 ≈ 32000-33000,
                          C6 ≈ 250-350
  ⚠️ If C5 is not near 32000 (i.e. 32768 × 1.0), something is wrong.
```

**The MS5611 second-order temperature compensation (required for full accuracy):**

```c
/* After the first-order computation, if the temperature is far from
   20 degC, apply the second-order correction: */
if (dT < -1500) {                     /* dT is the temperature difference
                                         from the reference, in centi-degC */
    temp2 = dT * dT / 2;              /* 2^1 scaling handled below        */
} else {
    temp2 = 0;
}

OFF2  = (5 * (temp - 2000) * (temp - 2000)) / 2;
SENS2 = (5 * (temp - 2000) * (temp - 2000)) / 4;

if (temp < -1500) {                   /* very cold */
    OFF2  += 7 * (temp + 1500) * (temp + 1500);
    SENS2 += 11 * (temp + 1500) * (temp + 1500) / 2;
}

OFF  -= OFF2;
SENS -= SENS2;
/* Then recompute pressure with the corrected OFF and SENS. */
```

> ⚠️ **A launch in November at an Indian launch site will see 8–20 °C on the pad at dawn and then 30–40 °C inside a black airframe in the sun.** That is a 20–30 °C swing, which is exactly the range where the second-order compensation matters (it is a 1–5 Pa effect, i.e. **0.1–0.5 m**). Implement it, and log the raw `dT` so you can post-analyse.

**BMP280/BMP390 — the factory `t_fine` path:**

```c
/* Bosch's compensation formula. The 't_fine' variable is a single
   temperature value used in BOTH the temperature and the pressure
   compensation — you MUST compute the temperature first. */

/* 1. Temperature */
var1 = (((double)adc_T) / 16384.0 - ((double)dig_T1) / 1024.0) * ((double)dig_T2);
var2 = ((((double)adc_T) / 131072.0 - ((double)dig_T1) / 8192.0) *
        (((double)adc_T) / 131072.0 - ((double)dig_T1) / 8192.0)) * ((double)dig_T3);
t_fine = (int32_t)(var1 + var2);
temperature = (var1 + var2) / 5120.0;          /* degC */

/* 2. Pressure — uses t_fine */
var1 = ((double)t_fine / 2.0) - 64000.0;
var2 = var1 * var1 * ((double)dig_P6) / 32768.0;
var2 = var2 + var1 * ((double)dig_P5) * 2.0;
var2 = (var2 / 4.0) + (((double)dig_P4) * 65536.0);
var3 = ((double)dig_P3) * var1 * var1 / 524288.0;
var1 = (var3 + ((double)dig_P2) * var1) / 524288.0;
var1 = (1.0 + var1 / 32768.0) * ((double)dig_P1);
pressure = 1048576.0 - (double)adc_P;
pressure = (pressure - (var2 / 4096.0)) * 6250.0 / var1;
var1 = ((double)dig_P9) * pressure * pressure / 2147483648.0;
var2 = pressure * ((double)dig_P8) / 32768.0;
pressure = pressure + (var1 + var2 + ((double)dig_P7)) / 16.0;   /* Pa */

/* ⚠️ Use double, not float. The intermediate terms reach 1e9 and
   float32's 24-bit mantissa loses you 2-3 Pa. This is a real,
   measurable bug. Bosch's own datasheet uses double. */
```

**Bosch `dig_*` validation:** the calibration registers are read at startup. Genuine BMP280 parts have `dig_T1` in the 26000–29000 range; `dig_P1` in the 36000–38000 range. **If `dig_T1` is 0 or 65535, you have a dead or fake part.**

### 1.6 Noise filtering

**Three-stage filter, in this order:**

```
  STAGE 1 — SENSOR-INTERNAL OVERSAMPLING
    MS5611:   OSR = 4096  (conversion time 9.04 ms → 110 Hz max rate,
                           but you only need 50 Hz)
    BMP390:   osr_p = ×4,  osr_t = ×2,  IIR filter coefficient 3
    BMP280:   osr_p = ×16, osr_t = ×2,  IIR filter coefficient 4

    ⚠️ Higher OSR = lower noise but slower. At 50 Hz you have 20 ms
       per sample, so OSR 4096 (9.04 ms) fits comfortably. Do NOT use
       OSR 4096 at 200 Hz — you will read the same conversion twice.

  STAGE 2 — MEDIAN FILTER (rejects spikes, not noise)
    Window: 5 samples
    Use:    to remove single-sample glitches from I2C bit errors or
            from a pressure transient (a hatch opening, a gust)
    Cost:   one sort of 5 floats per sample — trivial
    ⚠️ Do NOT use a mean here. A mean smears a spike across 5 samples;
       a median deletes it.

  STAGE 3 — MOVING AVERAGE / IIR LOW-PASS (reduces noise)
    Option A: 5-point moving average (simple, linear phase, 2 samples
              of group delay)
    Option B: 2nd-order Butterworth IIR, fc = 5 Hz at 50 Hz sample rate
              (better stopband, but non-linear phase)

    ⚠️ fc must be chosen against the PNEUMATIC cutoff of the vent
       (see below). There is no point filtering at 5 Hz if the airframe
       vent already limits you to 1.5 Hz.
```

**Choosing the anti-alias / anti-noise cutoff against the vent:**

```
  The airframe vent + sensor package is a pneumatic low-pass filter:

      f_c ≈ (a / (2π·L)) · √(A / V)       (Helmholtz-like approximation)

  where: a  = speed of sound ≈ 343 m/s
         A  = total vent hole area (m²)
         V  = internal cavity volume behind the vent (m³)
         L  = effective vent neck length ≈ port thickness + 1.7·r

  WORKED EXAMPLE for the UVCE vehicle:
      Vent:     4 holes × 2.0 mm diameter  →  A = 4 × π × (0.001)² = 1.257e-5 m²
      Cavity:   avionics bay 80 mm dia × 150 mm long
                →  V = π × (0.04)² × 0.15 = 7.54e-4 m³
      Neck:     wall thickness 2 mm, r = 1 mm
                →  L = 0.002 + 1.7 × 0.001 = 0.0037 m

      f_c ≈ (343 / (2π × 0.0037)) × √(1.257e-5 / 7.54e-4)
          = 14750 × √0.01667
          = 14750 × 0.1291
          ≈ 1905 Hz   ← ⚠️ This is FAR too high; the vent is not the limit

  ⚠️ Recompute for a SINGLE 2 mm hole:  A = 3.14e-6, √(A/V) = 0.0645,
     f_c ≈ 951 Hz. Still high.

  The real limit is the SENSOR PACKAGE's own port (typically 0.3-0.5 mm
  in a plastic LGA package), which gives f_c of 20-200 Hz.

  💡 CONCLUSION: with a 4 × 2 mm vent set you are NOT vent-limited for
     a 1 km flight. Filter in FIRMWARE at 5 Hz and you will track the
     real trajectory accurately. The vent's job is to reject the
     PRESSURE PULSE from a parachute charge and from angle-of-attack
     changes, not to set your bandwidth.

  ⚠️ Sanity check by MEASUREMENT: seal the bay, apply a step pressure
     change (a syringe through a port, or a vacuum chamber), and measure
     the 10-90 % rise time. Rise time ≈ 0.35 / f_c.
```

**The filter delay you must account for:**

| Filter | Group delay at 50 Hz |
|---|---|
| OSR 4096 conversion | 9.0 ms |
| 5-point median | 2 samples = 40 ms |
| 5-point moving average | 2 samples = 40 ms |
| **Total** | **≈ 90 ms** |

90 ms at 200 m/s of ascent is **18 m of altitude lag**. That is acceptable for a 0.1 m *reporting* requirement (which is about resolution, not real-time accuracy), but **it must not be inside your apogee detector's velocity estimate**. ⚠️ **Compute apogee velocity from the *unfiltered* (median-only) pressure, or explicitly compensate the lag.** This is exactly the kind of detail that separates a working apogee detector from a marginal one.

### 1.7 Achievable altitude resolution — the summary table

| Sensor + filtering | RMS pressure noise | RMS altitude noise at 1000 m | Peak-to-peak (6σ) | Meets 0.1 m? |
|---|---|---|---|---|
| BMP280, no filter | 8 Pa | 0.75 m | 4.5 m | ❌ |
| BMP280, OSR×16 + median 5 + MA 5 | 2.5 Pa | **0.24 m** | 1.4 m | ⚠️ No |
| BMP390, OSR×4 + median 5 + MA 5 | 0.8 Pa | **0.075 m** | 0.45 m | ✅ Yes |
| **MS5611, OSR 4096 + median 5 + MA 5** | **0.5 Pa** | **0.047 m** | **0.28 m** | ✅ **Yes, with 2× margin** |
| BMP581, OSR×8 + median 5 + MA 5 | 0.3 Pa | **0.028 m** | 0.17 m | ✅ Yes |
| **MS5611 + 20-point MA (0.4 Hz effective)** | 0.2 Pa | **0.019 m** | 0.11 m | ✅ Yes, but 400 ms of lag |

> ### ✅ Verdict
> **MS5611 with OSR 4096, a 5-point median, and a 5-point moving average** gives **0.047 m RMS** — comfortably inside the 0.1 m requirement, at 1 kHz IMU rate and 50 Hz barometer rate, with ~90 ms of total lag.
>
> ⚠️ **A bare BMP280 does NOT meet the requirement.** If you use a BMP280, you must state in the CDR that your achievable resolution is 0.24 m RMS, and describe how you mitigate it (longer averaging, lower bandwidth, explicit acknowledgement that the *reported* resolution is 0.1 m while the *measured noise* is 0.24 m). **Say it before the Jury finds it.**

---

## 2. Inertial measurement unit (IMU)

### 2.1 Operating principle

**MEMS accelerometer (capacitive):** a proof mass is suspended on silicon springs between fixed capacitor plates. Acceleration displaces the mass; the differential capacitance change is proportional to acceleration. Typically a **closed-loop (force-balanced)** design for good linearity.

```
       FIXED PLATES                          PROOF MASS
    ┌───────────────┐                    ┌───────────────┐
    │  ▓▓▓▓▓▓▓▓▓▓   │◀─── C1 ───────────▶│               │
    │               │                    │   █████████   │── spring ──┐
    │  ▓▓▓▓▓▓▓▓▓▓   │◀─── C2 ───────────▶│               │            │
    └───────────────┘                    └───────────────┘            │
                                                                      │
    a = 0:  C1 = C2                                       anchor ◀────┘
    a > 0:  mass moves right, C1 > C2
    ΔC ∝ a  →  demodulated, digitised, temperature-compensated

  ⚠️ A MEMS ACCELEROMETER MEASURES SPECIFIC FORCE, NOT ACCELERATION:
       a_measured = a_true − g_gravity_vector   (in the sensor frame)
     At rest, vertical axis reads +9.81 m/s². Free fall reads 0.
```

**MEMS gyroscope (tuning-fork):** two proof masses are driven into anti-phase oscillation. When the sensor rotates about the sense axis, the Coriolis force deflects the masses perpendicular to the drive; that deflection is sensed capacitively and is proportional to angular rate. This is why gyros have a **drive-loop** that must be running before the output is valid (~30–100 ms after power-on).

```
        DRIVE (in-plane, anti-phase)          SENSE (out-of-plane)
             ┌───────┐                             ▲
        ═══▶ │ mass1 │ ═══▶                        │ Coriolis
             └───────┘                             │ deflection
        ◀═══ │ mass2 │ ◀═══                        ▼
             └───────┘
        Ω (rotation about the sense axis) → Coriolis force
        F_c = 2·m·(v_drive × Ω)
```

### 2.2 ⚠️ The obsolescence and counterfeit problem — read before buying

**TDK InvenSense discontinued the MPU6050 and MPU9250 for new designs.** They remain in production only for existing customers. The consequences in the Indian market:

| Part you think you bought | What you often get | How to detect it |
|---|---|---|
| MPU6050 | A refurbished die pulled from scrap, re-lasered | `WHO_AM_I` returns `0x68` correctly (they re-mark it), but the gyro bias wanders 5–20 °/s and the temperature sensor is nonsense. **Detect by measuring bias stability over 10 minutes: a genuine part drifts < 1 °/s; a refurb drifts > 5 °/s** |
| MPU9250 | An MPU6500 (`WHO_AM_I` = `0x70`) with a fake or absent AK8963 | Read `WHO_AM_I` at `0x75` → should be `0x71`. Read the mag's `WIA` at `0x0C` → should be `0x48` |
| BMP280 | A different Bosch die with a rewritten calibration block | Compare `dig_T1`/`dig_P1` against the genuine ranges (§1.5). Log 60 s at 100 Hz and compute the noise — a fake gives 20–100 Pa instead of 2–8 Pa |
| MS5611 | A BMP280 in an MS5611-marked package | Read the PROM. The MS5611 returns 6 × 16-bit coefficients in a specific format; a BMP280 cannot answer that command sequence |
| "ICM-20948" | A genuine part, usually — it is current production, so the incentive to fake it is lower | Still verify `WHO_AM_I` = `0xEA` |

**Sourcing rules that actually work:**

1. **Buy from element14 India, Mouser India, DigiKey India, or RS Components India.** You pay 1.5–3× the marketplace price and you get a real part number, a lot code, and a datasheet-backed traceable supply chain. **This is the correct trade.**
2. **If you must buy from a marketplace, buy the *module* from a named Indian vendor with a physical address** (Robu.in, Robocraze, ThinkRobotics, Sunrom, Probots, Zbotic) and **verify the `WHO_AM_I` and the calibration values on arrival**.
3. **Buy two, from two different suppliers, and compare them.** If their noise floors differ by more than 2×, one is fake. This costs ₹300 and saves a launch.
4. **⚠️ Avoid unbranded listings with no part number, no datasheet link, and a price more than 40 % below the market.** That is the counterfeit signature.
5. 🔬 **Photograph the die markings under a magnifier and put the photo in the CDR sourcing annex.** It demonstrates procurement rigour and it is the sort of "Make in India / quality control" evidence the grading rewards.

### 2.3 IMU comparison

| IMU | Accel range | Accel noise | Gyro range | Gyro noise | Interface | `WHO_AM_I` | Cost (INR) | Verdict |
|---|---|---|---|---|---|---|---|---|
| **MPU6050** | ±2/4/8/16 g | 300 µg/√Hz | ±250…2000 °/s | 0.005 °/s/√Hz | **I2C only** | `0x68` | ₹90–220 | ❌ **Obsolete.** I2C-only caps you around 1 kHz on a shared bus. Clone risk severe. **Use only for the static test stand or for teaching.** |
| **MPU9250** | ±16 g | 300 µg/√Hz | ±2000 °/s | 0.01 °/s/√Hz | I2C/SPI | `0x71` | ₹250–600 | ❌ **Obsolete.** 9-axis, but the mag is a separate die that clones fake. |
| **TDK ICM-20948** | ±16 g | 230 µg/√Hz | ±2000 °/s | 0.015 °/s/√Hz | I2C/SPI | `0xEA` | ₹450–1,200 | ✅ **Safe, always-in-stock fallback.** Current production 9-axis. The magnetometer is genuinely useful for post-flight attitude reconstruction and for a yaw reference on the pad. Adds a second read path (the mag is behind an I2C master on the DMP) — budget a week of driver work. |
| **TDK ICM-42688-P** ⭐ | ±16 g | **70 µg/√Hz** | ±2000 °/s | **0.0028 °/s/√Hz** | SPI (24 MHz) / I2C | `0x47` | ₹600–1,100 | ✅ **RECOMMENDED.** 4× lower accel noise and 5× lower gyro noise than the ICM-20948, single-die but well-damped, 32 kHz-capable ODR, on-chip anti-alias filter, and genuinely available in India. **Best sourcing-to-performance ratio available today.** |
| **Bosch BMI088** ⭐ | **±24 g** | 175 µg/√Hz | ±2000 °/s | 0.014 °/s/√Hz | **SPI, dual CS** | accel `0x1E`, gyro `0x0F` | ₹900–1,600 | ✅ **The best technical choice for a rocket.** Two **separate dies** in one package — the accelerometer and gyro do not share a mechanical structure, which is precisely what you want under 15–30 g and violent vibration. Bosch documents its vibration robustness for exactly this reason. ⚠️ Harder to source in India; the dual-CS SPI driver is more work. |
| **ST ISM330DHCX** | ±16 g | 60 µg/√Hz | **±4000 °/s** | 0.0035 °/s/√Hz | SPI/I2C | `0x6B` | ₹900–1,500 | ✅ Industrial grade, **−40 to +105 °C**, excellent bias stability, and the **±4000 °/s** range means you will not clip the spin-rate field on a fast roll. Best choice if you care about the gyro range requirement. |
| **Bosch BMI270** | ±16 g | 130 µg/√Hz | ±2000 °/s | 0.008 °/s/√Hz | SPI/I2C | `0x24` | ₹400–800 | ✅ Cheap, low power, good. The onboard "feature engine" is undocumented-ish; use it in raw mode. |
| **Analog Devices ADIS16470** | ±40 g | 13 µg/√Hz | ±2000 °/s | 0.0005 °/s/√Hz | SPI | — | ₹45,000+ | ❌ Not for this budget. **Mention it in the PDR** to show you know what the professional tier looks like, and why you did not choose it (cost, mass, power). |

### 2.4 Range selection

**Accelerometer — the arithmetic (from the Flight Computer document, repeated because it matters):**

| Flight event | Expected | ×Margin | Required range |
|---|---|---|---|
| Launch (rule: survive 15 g) | 15 g | ×1.5 | 22.5 g |
| Thrust transient / resonant coupling | ~25 g | ×1.2 | 30 g |
| Parachute opening shock (rule: survive 30 g) | 30 g | ×1.5 | 45 g |

**Choose ±16 g for the primary channel** and be explicit about clipping:

```
  ±16 g = 156.906 m/s² full scale (16 × 9.80665)

  ⚠️ Any sample with |raw| > 0.97 × 156.906 = 152.2 m/s² is CLIPPED.
     Set a flag. Report it. Do NOT silently integrate a clipped sample —
     that under-integrates the velocity by however much you clipped.

  If you have a ±24 g part (BMI088) or a ±32 g part, use the higher
  range:  ±24 g = 235.4 m/s²,  ±32 g = 313.9 m/s²

  💡 BEST PRACTICE: log the clipped-sample count per flight in the
     post-flight summary. "3 samples clipped during the 30 g opening
     shock" is a much better CDR statement than silence.
```

**Gyroscope — choose ±2000 °/s minimum, ±4000 °/s if available:**

```
  Roll rate: a rocket with a small fin cant can roll at 5-15 rev/s.
     5 rev/s  =  5 × 360 =  1800 °/s
    10 rev/s  = 10 × 360 =  3600 °/s   ← ⚠️ CLIPS at ±2000 °/s
    15 rev/s  = 15 × 360 =  5400 °/s   ← ⚠️ CLIPS at ±4000 °/s

  The spin-rate field is a REQUIRED telemetry parameter. A clipped gyro
  means you report a wrong value at exactly the moment it is interesting.

  💡 If your part caps at ±2000 °/s:
     - state it in the CDR
     - flag clipped samples in the log
     - report the CLIP FLAG alongside the value so the Jury can see that
       you know the difference between "0 deg/s" and "clipped"
```

### 2.5 Calibration

**A. Accelerometer — the six-face static calibration**

This is the *only* correct accelerometer calibration, and it takes 20 minutes.

```
  PROCEDURE
    1. Mount the IMU on a machined or 3D-printed cube (a "calibration
       cube") with faces aligned to the sensor axes. A 40 mm cube with
       ±0.1 mm tolerances is enough.
    2. On a LEVEL surface (check with a spirit level — a 0.5° tilt is
       0.086 m/s² of error), record 2000 samples at 200 Hz for each of
       the six orientations:
            +X up, −X up, +Y up, −Y up, +Z up, −Z up
    3. For each axis, you now have two measurements at ±1 g:
            a_+ =  bias + scale × (+9.80665)
            a_- =  bias + scale × (−9.80665)
    4. Solve:
            scale = (a_+ − a_-) / (2 × 9.80665)
            bias  = (a_+ + a_-) / 2
    5. Also check OFFSET from the axes you were not measuring:
            when +Z is up, a_x and a_y should both read 0 ± 0.05 m/s².
            A larger value means the cube is misaligned or the sensor
            has cross-axis sensitivity.
    6. Store {bias[3], scale[3]} in FRAM, with a CRC and a date.

  PASS CRITERIA
    • scale within 0.98-1.02 on every axis
    • bias < 0.15 m/s² on every axis
    • cross-axis terms < 0.05 m/s²
    ⚠️ If scale is outside 0.95-1.05, the part is fake or damaged.
```

**B. Gyroscope — bias, Allan variance, and temperature drift**

```
  1. BIAS MEASUREMENT (essential, easy)
     • Sensor completely still, thermally soaked for 10 minutes at the
       expected flight temperature.
     • Record 60 s at 200 Hz.
     • bias = MEAN of each axis.
     • ⚠️ Do NOT use a single sample, and do NOT use the first 30 s
       after power-on (the drive loop is still settling).
     • Subtract the bias in firmware. A 0.5 °/s bias integrated over
       120 s of flight is 60° of attitude error.

  2. NOISE / ALLAN VARIANCE (characterises what you can and cannot do)
     • Record 1-4 HOURS of static data at 200 Hz. (Yes, hours. Do it
       overnight, in a thermally stable room.)
     • Compute the Allan deviation:
            σ(τ) for τ = 0.005 s ... 1000 s
     • Read off:
            • Angle Random Walk (ARW):  the −1/2 slope, in °/√hr
              → determines short-term noise; you cannot integrate
                through it, you can only filter it
            • Bias Instability:  the minimum of the curve, in °/hr
              → determines the best attitude you can hold over minutes
            • Rate Random Walk:  the +1/2 slope
              → determines long-term drift
     • Tool: a Python script with numpy. ~50 lines. Publishes a plot
       that looks superb in a CDR.

  3. TEMPERATURE DRIFT
     • Place the IMU in a temperature chamber (or a fridge then a warm
       room, slowly) and record bias vs. temperature from 5 to 45 °C.
     • Fit bias(T) = a + b·T + c·T².
     • Apply the correction using the IMU's own on-die temperature.
     ⚠️ THIS IS THE ONE MOST TEAMS SKIP AND MOST NEED. A 25-minute
        pad wait with a 15 °C temperature rise gives a bias shift of
        0.1-2 °/s on a consumer IMU. Over a 120 s flight that is up to
        240° of attitude error.
     💡 Cheaper alternative: after any 5 s static period in states
        0/1/2, RE-ZERO the gyro bias. That tracks thermal drift without
        a chamber.
```

**C. Magnetometer (if fitted, ICM-20948)**

```
  1. Hard-iron calibration: rotate the sensor through all orientations
     (a 3D figure-8, 60+ seconds) and fit a sphere to the raw data.
     The sphere's CENTRE is the hard-iron offset.
  2. Soft-iron calibration: fit an ELLIPSOID; the axis scale factors and
     the rotation correct for nearby ferrous material.
  3. ⚠️ Recalibrate WITH THE MAGNETOMETER IN THE ACTUAL AIRFRAME and
     with the motor installed. The motor casing and the deployment
     hardware are large ferrous masses 100 mm away — they will dominate
     the calibration.
  4. ⚠️ A magnetometer is nearly useless during boost (the vehicle is
     spinning and the field readings rotate with it), so use it only for
     a pad yaw reference and for post-flight attitude reconstruction.
```

### 2.6 Mounting — this is where vibration kills you

| Practice | Detail |
|---|---|
| **Rigid mounting plate** | 2 mm FR4 or 3 mm aluminium, **not** a 3D-printed bracket (PETG creeps and the natural frequency is too low) |
| **Silicone grommets, not foam** ⚠️ | Foam compresses permanently and lets the board slap against the standoff. Use M3 silicone grommets at the four corners, with a nylon standoff through each grommet so the screw cannot over-compress it. Target a mounted resonance of **150–400 Hz**, above the motor's vibration band's worst content but below the airframe's first bending mode |
| **Instrument the mount** | Put a spare accelerometer on the *frame* next to the IMU and compare. If the board-mounted IMU shows 3× the frame's vibration, your isolation is wrong (or it is resonating) |
| **Stake the package** | A dot of epoxy at the corners of the IMU package. Under 30 g the package itself can shear its solder joints |
| **Keep it away from the vent** | Don't put the IMU on the same board edge as the barometer vent holes — the pressure pulse that reaches the barometer also pushes on the IMU's own cavity |
| **Vibration rectification is real** ⚠️ | A MEMS accelerometer under broadband vibration produces a **DC offset** proportional to the vibration amplitude squared. Under 10 g RMS of motor vibration you can see 0.5–3 m/s² of false DC. This is why the BMI088's dual-die construction exists, and why you should **treat the accelerometer as a confirmation of the barometer, never as the primary truth source for altitude** |

---

## 3. GNSS

### 3.1 Operating principle

A GNSS receiver trilaterates its position from the **pseudoranges** to at least four satellites. Each satellite broadcasts a ranging code and a navigation message containing its ephemeris (orbit) and clock correction. The receiver measures the code phase to get a pseudorange, then solves four unknowns (x, y, z, clock bias).

```
   ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐
   │ SAT1 │  │ SAT2 │  │ SAT3 │  │ SAT4 │
   └───┬──┘  └───┬──┘  └───┬──┘  └───┬──┘
       │ ρ1      │ ρ2      │ ρ3      │ ρ4       ρ = c × (t_rx − t_tx)
       │         │         │         │
       └─────────┴────┬────┴─────────┘
                      ▼
     ┌────────────────────────────────────────┐
     │  ρi = √((xi−x)² + (yi−y)² + (zi−z)²)   │
     │       + c·δt_receiver + Ionospheric     │
     │       + Tropospheric + Multipath + ...  │
     │                                         │
     │  4 equations, 4 unknowns → solve        │
     │  More satellites → least squares,       │
     │  better geometry (lower DOP)            │
     └────────────────────────────────────────┘
```

**Constellations you might track:**

| System | Owner | Frequencies | Notes |
|---|---|---|---|
| **GPS** | USA | L1 1575.42, L2 1227.60, L5 1176.45 MHz | The baseline |
| **GLONASS** | Russia | L1 1602, L2 1246 MHz (FDMA) | Good high-latitude geometry, poorer at low latitudes |
| **Galileo** | EU | E1 1575.42, E5 1191.795 MHz | Good accuracy, no encryption on the open service |
| **BeiDou** | China | B1 1561.098, B2 1207.14 MHz | Excellent coverage over Asia — **genuinely useful in India** |
| **QZSS** | Japan | L1/L2/L5 | Regional, marginal over India |
| **NavIC / IRNSS** | **India** | **L5 1176.45, S 2492.028 MHz** | 3 GEO + 4 inclined GSO; covers India + ~1500 km. **L5-only, so any L5-capable receiver can in principle track it; the firmware and the antenna must support it** |
| **GAGAN** | India (SBAS) | L1/L5 | India's satellite-based augmentation system (a GPS augmentation, not a separate constellation). Broadcasts correction data, giving **~1–3 m** accuracy instead of 3–5 m |

### 3.2 Module comparison, with honest NavIC notes

| Module | Chipset | Constellations | NavIC / IRNSS | SBAS | Cold TTFF | Accuracy (CEP) | Update rate | Interface | Cost (INR) |
|---|---|---|---|---|---|---|---|---|---|
| **u-blox NEO-M8N** ⭐ | u-blox M8 | GPS, GLONASS, Galileo, BeiDou, QZSS | ❌ | **GAGAN, WAAS, EGNOS** | 26 s | 2.5 m | 10 Hz | UART/I2C/SPI, 3.3 V | ₹1,100–1,800 |
| **u-blox NEO-M9N** | u-blox M9 | GPS, GLONASS, Galileo, BeiDou | ❌ | ✅ | 24 s | 1.5 m | 25 Hz | UART/I2C/SPI | ₹2,000–3,200 |
| **u-blox ZED-F9P** (RTK) | u-blox F9 | GPS, GLONASS, Galileo, BeiDou | ❌ | ✅ | 24 s | **1 cm (RTK)** | 20 Hz | UART/USB/SPI | ₹12,000–20,000 |
| **Quectel L86** | MediaTek MT3333 | GPS, GLONASS, BeiDou, QZSS, Galileo | ❌ | ✅ | 35 s | 2.5 m | 10 Hz | UART | ₹600–1,100 |
| **Quectel L76K** | MediaTek | GPS, GLONASS, BeiDou, QZSS | ❌ | ✅ | 35 s | 2.5 m | 10 Hz | UART | ₹700–1,200 |
| **Quectel LC86G** | Quectel | GPS, GLONASS, BDS, Galileo, **NavIC L5** | ✅ **Claimed** | ✅ | 30 s | 1.5–2.5 m | 10 Hz | UART | ₹1,200–2,000 |
| **Telit SE868-V3** | — | GPS, GLONASS, BDS, **IRNSS** | ✅ **In datasheet** | ✅ | 30 s | 2.5 m | 10 Hz | UART | ₹1,500–2,500 |
| **Skylark C1 / Indian GNSS boards** | Various | Multi-constellation incl. IRNSS | ✅ | ✅ | 30–45 s | 2–5 m | 1–10 Hz | UART | ₹2,000–4,000 |
| **ATGM336H** | Zhongke Micro | GPS + BeiDou | ❌ | ❌ | 35 s | 2.5 m | 10 Hz | UART | ₹350–600 |
| **u-blox NEO-6M** | u-blox 6 | GPS only | ❌ | ❌ | 27 s | 2.5 m | 5 Hz | UART | ₹350–700 |

> ### ⚠️ The honest NavIC position for the CDR
>
> **Almost every "NavIC-capable" module sold in the Indian market is a GPS/GLONASS/BeiDou module with NavIC support in the marketing copy rather than in the firmware.** NavIC's L5 signal is at 1176.45 MHz, which is shared with GPS L5 — so a receiver that tracks GPS L5 *might* be able to correlate an IRNSS L5 signal if its firmware has the IRNSS PRN codes, but "might" is not a design.
>
> **Recommended CDR statement:**
>
> > *"The competition does not mandate NavIC support. Our primary navigation receiver is the u-blox NEO-M8N, selected for its maturity, 10 Hz update rate, and GAGAN (Indian SBAS) support, which provides 1–3 m accuracy over the Indian landmass. We have evaluated IRNSS-capable modules (Quectel LC86G, Telit SE868-V3) and will qualify one as a drop-in replacement before the Flight Readiness Review if the vehicle's GNSS performance with the NEO-M8N is inadequate. Our GNSS antenna is a wideband active patch covering 1559–1610 MHz (L1 band); an IRNSS L5 upgrade would require an L5-capable antenna and is therefore a hardware change, not a firmware one."*
>
> **That is a stronger answer than an unverifiable claim.** It shows you understand the difference between an L1 receiver, an L5 receiver, and a NavIC-capable receiver — which is more than most teams will be able to say.

### 3.3 Fix acquisition time

| Start type | Condition | Typical TTFF (NEO-M8N) | What makes it faster |
|---|---|---|---|
| **Cold start** | No almanac, no ephemeris, no position, no time | **26–35 s** | Nothing — this is physics (you must download the almanac at 50 bps) |
| **Warm start** | Almanac, coarse time and position, no ephemeris | 20–30 s | A backup battery keeping the RTC and the almanac alive |
| **Hot start** | Almanac + ephemeris + position within 25 km + time | **1–3 s** | A backup battery on `V_BCKP` |
| **Assisted (A-GNSS)** | Ephemeris delivered over the network | < 1 s | Not possible without a network link |
| **Reacquisition after signal loss** | Lock lost for < 30 s | 1–2 s | — |

**Design actions:**

1. **Fit an ML1220 or CR2032 coin cell to `V_BCKP`.** ~₹40 of parts. Turns a 30 s cold start into a 2 s hot start, and lets you power-cycle the GNSS on the pad to clear a hang without paying the cold-start penalty. **This is the single highest-value ₹40 in the avionics.**
   ⚠️ Check the module's `V_BCKP` current draw: some are 15–30 µA, which drains a CR2032 (220 mAh) in ~1 year. That is fine. Some draw 100 µA+, which is not — use the rechargeable ML1220 with a charging circuit instead.
2. **Acquire the fix on the pad, early, and keep the receiver powered.** Do not power-cycle it during the pad wait.
3. **Log the fix status and the last-known-good position.** If the receiver drops out at boost, your telemetry should show **stale coordinates with a no-fix flag**, never garbage.
4. **Budget 60 s in the countdown for the cold start** if the backup battery is dead. Actually budget 90 s, because the pad has obstructions.

### 3.4 Accuracy, and why you need a good sky view

| Error source | Typical magnitude (L1, single frequency) | Notes |
|---|---|---|
| **Ionospheric delay** | 5–15 m | The dominant error. Corrected by GAGAN/SBAS or by dual-frequency (L1+L5) |
| **Tropospheric delay** | 2–3 m | Modelled |
| **Satellite clock and orbit** | 1–2 m | Corrected by broadcast ephemeris |
| **Multipath** | 1–10 m | ⚠️ **The one you can control: keep the antenna away from reflecting surfaces** |
| **Receiver noise** | 0.5–2 m | — |
| **Geometric dilution of precision (DOP)** | ×1–×10 multiplier | ⚠️ **The one you can control: a good sky view and a good constellation mix** |
| **Total, open sky, SBAS on** | **1.5–3 m horizontal** | |
| **Total, with buildings/trees/vehicles nearby** | **5–25 m horizontal** | ⚠️ |

**Why sky view matters so much:**

```
  HDOP multiplies your measurement noise. Horizontal error = HDOP × σ_range.

     Open sky, 10 satellites well distributed:   HDOP 0.8-1.2
     Suburban, 7 satellites, some blocked:        HDOP 1.5-3.0
     Urban canyon / beside a vehicle / inside a
     metal building:                              HDOP 5-20  (or no fix)

  With σ_range = 2 m:
     HDOP 1.0  →   2 m error    ✅ Excellent
     HDOP 3.0  →   6 m error    ⚠️ Acceptable for recovery, not for
                                    trajectory analysis
     HDOP 10   →  20 m error    ❌ Useless
```

**Antenna placement rules for the rocket:**

| Rule | Reason |
|---|---|
| **Active patch antenna (25–30 dB LNA gain), 25 × 25 mm or 35 × 35 mm** | A passive antenna will not see satellites at 1 km through an airframe |
| **Mounted on the OUTSIDE of the airframe, or in a radome-clear nose section** | ⚠️ **A cardboard or fibreglass airframe attenuates 1–3 dB; a carbon-fibre airframe blocks it completely.** If you must mount internally, use fibreglass or a dedicated RF-transparent window |
| **Coaxial feed ≤ 100 mm, 50 Ω, with a proper U.FL→SMA pigtail** | Every 100 mm of thin coax costs 0.3–0.8 dB at 1.575 GHz |
| **Powered from a clean 3.3 V rail with a ferrite bead** | The LNA is sensitive to supply noise; a noisy rail raises the noise figure |
| **Keep it ≥ 50 mm from the 2.4 GHz antenna** | ⚠️ **A 2 W 2.4 GHz transmitter 10 mm from an L1 GNSS LNA will desensitise it completely.** If you cannot separate them, schedule the transmissions: a 1 Hz telemetry burst leaves 99 % of the time for the GNSS |
| **Ground plane under the patch ≥ 50 × 50 mm** | A patch antenna without a ground plane is a random piece of ceramic |

**The COCOM limits — a trap for the future:**

u-blox modules are firmware-limited to **515 m/s velocity** and **18 000 m altitude**, and will stop reporting a fix beyond either. At 1 km apogee you are nowhere near these, so it will not bite you. ⚠️ **But if the club ever flies higher, you cannot simply buy a different module — u-blox requires a signed NDA and an export-control declaration to lift the limits.** Note this in the roadmap as a future procurement constraint.

### 3.5 GNSS calibration and validation

| Test | Method | Pass criterion |
|---|---|---|
| **GNSS-1: Static accuracy** | Log 30 min at a surveyed point (or next to a phone with a known-good GPS app) | Horizontal error < 5 m CEP; HDOP < 1.5 |
| **GNSS-2: TTFF** | Cold start (battery removed 24 h), 5 trials | < 40 s outdoors with a clear view |
| **GNSS-3: Hot start** | Power cycle after a 5-minute fix | < 5 s |
| **GNSS-4: Airframe integration** | Antenna installed in the airframe, receiver on, 30 min outdoors | Fix achieved; ≥ 6 satellites; HDOP < 2.5 |
| **GNSS-5: Coexistence** | The 2.4 GHz radio transmitting at 1 Hz nearby | Satellite count degrades by ≤ 2 and the fix is retained |
| **GNSS-6: Dynamic test** | Drive/cycle with the receiver, comparing against a reference track | Position error < 10 m at 10 m/s |
| **GNSS-7: Altitude check** | Compare GNSS altitude at the pad against a surveyed value | Within 150 m (the geoid undulation is roughly −60 to −90 m at Bengaluru, so a *systematic* offset of that magnitude is expected and correct) |

⚠️ **Do not use GNSS altitude for apogee detection.** It has 5–15 m of vertical error, it updates at 10 Hz at best but often effectively at 1 Hz internally, and it lags badly during high dynamics. It is a required *telemetry field* and a useful cross-check, not a control input.

---

## 4. Temperature sensors

### 4.1 Options compared

| Sensor | Principle | Range | Accuracy | Resolution | Interface | Response time | Cost (INR) | Best use |
|---|---|---|---|---|---|---|---|---|
| **On-die (barometer/IMU)** | Silicon bandgap | −40…+85 °C | ±1 °C | 0.01 °C | Already on I2C/SPI | ~1 s (thermal mass of the package) | ₹0 | ⭐ **The reported telemetry temperature** and the sensor's own compensation |
| **DS18B20** | Bandgap + 12-bit ΔΣ | −55…+125 °C | ±0.5 °C (−10…+85) | 0.0625 °C | **1-Wire**, parasitic or 3-wire | 750 ms at 12-bit | ₹90–250 | ⭐ **Battery-pack and avionics-bay temperature.** Multiple sensors on one pin via 64-bit ROM addresses |
| **NTC 10 kΩ β=3950** | Thermistor (exponential R-T) | −40…+125 °C | ±0.2 °C with a good β model | Depends on the ADC | Analog divider → ADC | ~1–5 s (bead) | ₹10–40 | Cheapest. Motor casing skin temperature on the test stand |
| **TMP36 / LM35** | Bandgap, analog | −40…+125 °C | ±1 °C | — | Analog, 10 mV/°C | ~1 s | ₹80–180 | Teaching; ⚠️ needs a clean reference and is noisy on a rocket |
| **MCP9808** | Bandgap, I2C | −40…+125 °C | **±0.25 °C** | 0.0625 °C | I2C | ~1 s | ₹150–300 | ✅ Better than DS18B20 if you want I2C. ⚠️ Address conflicts with other I2C devices |
| **Si7021 / SHT31** | Capacitive RH + bandgap T | −40…+125 °C | ±0.3 °C | 0.01 °C | I2C | ~1 s | ₹250–500 | Ground-station weather station |
| **PT100 / PT1000 RTD** | Platinum resistance | −200…+600 °C | **±0.1 °C** | — | Analog, needs excitation | 1–10 s | ₹200–900 | ✅ **Test stand, if you need real accuracy.** Requires a 3- or 4-wire measurement and a stable current source |
| **K-type thermocouple** | Seebeck effect | −200…+1372 °C | ±1.5–2.5 °C | 0.25 °C | Analog µV, needs an amplifier + CJC | 0.1–1 s (exposed), 1–5 s (sheathed) | ₹600–1,500 (probe) | ⭐ **Motor casing, nozzle, plume, chamber-external** |

### 4.2 Thermocouples — the physics and the cold-junction problem

**Seebeck effect:** when two dissimilar metals are joined and the junction is heated, a small voltage appears. For a K-type (chromel/alumel) pair, the sensitivity is about **41 µV/°C** at room temperature.

```
  ⚠️ A THERMOCOUPLE MEASURES A TEMPERATURE DIFFERENCE, NOT AN ABSOLUTE
     TEMPERATURE. It reports T_hot − T_cold, where T_cold is the
     temperature of the terminals where the wires meet your PCB.

  ┌─────────────┐                                        ┌──────────────┐
  │  HOT        │  chromel (+)                           │  TERMINAL    │
  │  JUNCTION   │ ─────────────────────────────────────▶ │  BLOCK       │
  │  (in the    │                                        │  (on the     │
  │   plume /   │  alumel  (−)                           │   PCB, at    │
  │   casing)   │ ─────────────────────────────────────▶ │   T_cold)    │
  └─────────────┘                                        └──────┬───────┘
                                                                │
                                          ┌─────────────────────▼─────────┐
                                          │ MAX31855 / MAX31856           │
                                          │  • measures its OWN temperature│
                                          │    → that IS the cold junction │
                                          │  • adds the two voltages:      │
                                          │      V_total = V(T_hot) −      │
                                          │                V(T_cold) +     │
                                          │                V(T_cold)       │
                                          │      = V(T_hot)  ✅             │
                                          └────────────────────────────────┘

  ⚠️ THE TWO RULES THAT FOLLOW:
     1. The cold-junction sensor must be at the SAME TEMPERATURE as the
        terminal block. Keep the MAX31855 ≥ 20 mm from any regulator and
        pour copper under the chip to couple it to the connector.
        A 15 °C error here IS a 15 °C error in your reading.
     2. The wires from the probe to the terminal MUST be the correct
        THERMOCOUPLE ALLOY. If you extend a K-type with ordinary copper
        wire, you create two new junctions and the reading is garbage.
        Buy K-type EXTENSION wire (chromel/alumel), not copper.
```

**Breakout board comparison:**

| Board | Chip | Thermocouple types | Resolution | Conversion | Fault detection | Logic level | Cost (INR) | Verdict |
|---|---|---|---|---|---|---|---|---|
| **MAX6675 breakout** | MAX6675 | **K only** | 0.25 °C | 220 ms | Open thermocouple only | 5 V (⚠️ needs level shifting for 3.3 V MCUs) | ₹250–450 | ⚠️ Old. Fine for a first test stand. ⚠️ **The 5 V logic will damage a 3.3 V STM32 MISO pin without a divider.** |
| **MAX31855K breakout** ⭐ | MAX31855 | **K only** | 0.25 °C | 100 ms | Open, short-to-GND, short-to-VCC, and a fault bit | ⚠️ **Two variants: "K" (5 V) and "K 3V3".** Buy the **3V3** variant for a 3.3 V MCU | ₹350–700 | ✅ **RECOMMENDED for the test stand.** Simple SPI, real fault detection, 14-bit |
| **MAX31855 (J/N/T/S/E/R)** | MAX31855 | One type each | 0.25 °C | 100 ms | Same | Same | ₹400–900 | ✅ For other thermocouple types |
| **MAX31856 breakout** | MAX31856 | **Any: K, J, N, T, S, E, B, R** | 0.0078 °C (19-bit) | 100 ms (50/60 Hz rejection) | Open, over/under temperature, all four short faults | 3.3 V or 5 V | ₹900–1,600 | ✅ **Best.** Does **full NIST linearisation internally** — the MAX31855 assumes a linear K-type response, which is a 2–5 °C error near the extremes. Use this if absolute accuracy matters |
| **Adafruit-style thermocouple amplifier (AD8495)** | AD8495 | K only | Analog | Instantaneous | None | Analog 5 mV/°C | ₹700–1,200 | ✅ Fast (no conversion delay) → good for a **chamber-pressure-adjacent fast temperature**. ⚠️ Analog, so noise-sensitive |
| **Custom: AD595 / AD8495 + a 24-bit ADC** | — | K/J | 0.01 °C | — | — | — | ₹1,200–2,000 | For a serious test stand |

**Calibration of a thermocouple chain:**

```
  You CANNOT calibrate a thermocouple by putting it in boiling water
  (100 °C ± 2 % at Bengaluru's altitude, which is 93-94 °C — not a
  reference). Use ice:

  ICE POINT (0 °C) — the primary reference
    1. Fill a Dewar/vacuum flask with CRUSHED ice made from DISTILLED
       water, and add just enough distilled water to fill the gaps.
    2. Stir. Wait 5 minutes for equilibrium.
    3. Insert the probe to a depth of ≥ 10× its diameter, without
       touching the walls or the bottom.
    4. Record 60 readings. The mean must be 0.0 °C ± 1.5 °C (the K-type
       tolerance).
    5. ⚠️ This validates the WHOLE CHAIN: probe + extension wire +
       terminal + CJC + amplifier + your firmware's linearisation.
       If it reads 4 °C, the cold junction is 4 °C too warm.

  SECOND POINT — for a two-point calibration
    • A dry-block calibrator (₹25,000+) is the correct tool.
    • A cheaper alternative: a disposable cup of molten wax (paraffin,
      ~55 °C) or boiling distilled water at a MEASURED ambient pressure.
      Compute the true boiling point from the pressure:
          T_boil(°C) ≈ 100.00 + 0.0367·(P_hPa − 1013.25)
                     − 0.000023·(P_hPa − 1013.25)²
      At Bengaluru (P ≈ 905 hPa):  T_boil ≈ 96.0 °C
      ⚠️ NOT 100 °C. If you use 100 °C in Bengaluru you inject a 4 °C
         error into your calibration and never notice.

  RECORD
    • Date, operator, sensor serial, the two reference points, the
      measured values, the computed offset and gain, and the values
      written into FRAM.
```

---

## 5. Voltage and current sensing

### 5.1 Voltage sensing — resistor divider + buffer

**Design procedure:**

```
  STEP 1: Maximum input voltage
     2S Li-ion: 8.40 V (fully charged)     ← use this, not the nominal
     1S Li-ion: 4.20 V
     4× alkaline: 6.40 V
     6× NiMH: 8.40 V

  STEP 2: Target the ADC input at 85-90 % of VREF
     VREF = 3.300 V  →  target V_adc(max) ≈ 2.85 V
     (leave headroom for tolerance and for a 0.1 % resistor spread)

  STEP 3: Compute the ratio
     ratio = V_adc(max) / V_in(max) = 2.85 / 8.40 = 0.3393
     R2/(R1+R2) = 0.3393   →   R1/R2 = 1.948

  STEP 4: Choose the divider impedance
     ⚠️ The STM32 ADC wants a source impedance < 10 kΩ for full 12-bit
        accuracy at high sample rates. The parallel combination R1∥R2
        is the source impedance.
     ⚠️ But a low impedance costs current: I = 8.4 / (R1+R2)

     22 kΩ / 10 kΩ  →  R1∥R2 = 6.88 kΩ,  I = 8.4/32k = 263 µA
                                                    ⚠️ 263 µA × 45 min
                                                       = 0.20 mAh —
                                                       negligible, fine
  STEP 5: Add the buffer (this is mandatory, not optional)
     A rail-to-rail op-amp as a unity-gain follower:
        MCP6002 (₹40, dual, 1.8-6 V, rail-to-rail, 90 µA/ch)
        or TLV9002 (₹45, similar)
     ⚠️ WITHOUT the buffer, the ADC's sample-and-hold current spike
        discharges the high-impedance divider and your reading depends
        on which channel was sampled previously. This is THE most common
        "my voltage reading is wrong" bug in student flight computers.
```

**Recommended divider table:**

| Battery | R1 (top) | R2 (bottom) | Ratio | V_adc @ Vmax | Divider current | Buffer |
|---|---|---|---|---|---|---|
| **2S Li-ion (8.4 V max)** ⭐ | **22 kΩ** | **10 kΩ** | 0.3125 | 2.625 V | 263 µA | MCP6002 |
| 2S Li-ion, lower drain | 47 kΩ | 22 kΩ | 0.3188 | 2.678 V | 122 µA | MCP6002 |
| 1S Li-ion (4.2 V max) | 10 kΩ | 22 kΩ | 0.6875 | 2.888 V | 131 µA | MCP6002 |
| 4× alkaline (6.4 V max) | 22 kΩ | 15 kΩ | 0.4054 | 2.595 V | 173 µA | MCP6002 |
| 6× NiMH (8.4 V max) | 22 kΩ | 10 kΩ | 0.3125 | 2.625 V | 263 µA | MCP6002 |

**Mandatory additions:**

| Item | Value | Why |
|---|---|---|
| **Resistor tolerance** | **0.1 %** (Vishay MRS25 or similar) | 1 % resistors give ±2 % ratio error = ±0.17 V on an 8.4 V pack. The rules want 0.01 V *resolution*, which the ADC provides; **accuracy** is a separate requirement, and 1 % resistors destroy it |
| **Temperature coefficient** | 25 ppm/°C or better | A 25 °C pad-wait swing with 100 ppm/°C resistors gives 0.25 % = 21 mV of drift, which is 4× your resolution |
| **Capacitor at the ADC pin** | 100 nF X7R + 10 µF X5R | Anti-alias and charge reservoir |
| **Series resistor to the ADC pin** | 100 Ω | Current-limits the ADC's sampling spike and forms an RC with the 100 nF (fc = 16 kHz) |
| **Software calibration** | Measure each board against a bench DMM at 2 points; store `{offset, gain}` in FRAM | Turns a 0.1 % resistor pair into a 0.05 % measurement. **Do this — it is 10 minutes per board and it is what makes the 0.01 V field defensible** |

**Sample-rate and averaging:**

```
  Oversample 16× and decimate to gain 2 bits of effective resolution:
      V = (Σ 16 samples) / 16        →  12-bit → ~13.5-14 effective bits
  With a 3.3 V reference that is 3.3/2^13.5 = 0.27 mV per LSB.
  At 2S Li-ion with a 0.3125 ratio, that is 0.85 mV at the battery.
  ⚠️ The rules ask for 0.01 V = 10 mV. You have 12× margin. 
```

### 5.2 Current sensing

| Method | Part | Range | Resolution | Interface | Cost (INR) | Best for |
|---|---|---|---|---|---|---|
| **High-side shunt + I2C monitor** | **INA219** | ±3.2 A (with 0.1 Ω) | 0.8 mA | I2C | ₹180–350 | ⭐ Servo rail current, battery current. Also reports **bus voltage**. Easiest possible |
| **High-side shunt + I2C monitor** | **INA226** | ±10 A | 0.15 mA | I2C | ₹300–600 | ✅ Better. 16-bit, programmable alert pin for over-current |
| **High-side shunt + I2C monitor** | **INA228** | ±85 V, 20-bit | 0.3 µA | I2C | ₹600–1,200 | One part for the whole test stand |
| **High-side shunt + analog amp** | **INA240 / INA181** | ±50 A | Analog | Analog | ₹150–450 | When you need a fast analog output for a 1 kHz loop |
| **Hall-effect, isolated** | **ACS712-05B/20A/30A** | ±5/20/30 A | 66–185 mV/A | Analog | ₹180–350 | ⚠️ Noisy, offset drifts with temperature, needs a mid-rail bias. **Do not use for precision; fine for a gross over-current trip** |
| **Hall-effect, isolated** | **ACS758LCB-100U** | 0–100 A | 40 mV/A | Analog | ₹600–1,100 | ✅ Good for an ignition/deployment rail monitor. Fully isolated |
| **Shunt + a differential ADC** | ADS1115 + a 1 mΩ shunt | ±50 A | 0.05 mA | I2C | ₹350–700 | ✅ Good for a thrust-stand power monitor |

**Shunt design:**

```
  Choose the shunt so that the FULL-SCALE current gives 50-100 mV
  across it (a good compromise between dissipation and resolution):

      R_shunt = V_fullscale / I_max

  For a 3 A servo rail at 75 mV full scale:
      R_shunt = 0.075 / 3 = 0.025 Ω

  Choose from standard values: 0.025 Ω is available as a 2512
  1 % 1 W part, or use two 0.05 Ω in parallel.

  ⚠️ POWER DISSIPATION:  P = I²R = 3² × 0.025 = 0.225 W
     So a 1 W part is required, and it will get warm. Design the
     copper to spread that heat and keep the shunt away from the
     barometer (a 0.225 W heat source 20 mm away shifts the pressure
     reading by ~1 Pa = 0.1 m of apparent altitude drift).

  ⚠️ KELVIN (4-WIRE) CONNECTION IS MANDATORY:
     Route the sense traces from INSIDE the shunt's pads, not from
     the current-carrying pads. A 2-terminal connection includes the
     solder-joint resistance (0.1-1 mΩ) in your measurement, which is
     a 4 % error on a 0.025 Ω shunt.
```

---

## 6. Load cell for a static test stand

### 6.1 Strain gauge theory

A **strain gauge** is a thin metal foil pattern bonded to a substrate, glued to the test article. When the article strains, the foil stretches and its resistance rises:

```
      R = ρL/A          (ρ = resistivity, L = length, A = cross-section)

      Stretching increases L and decreases A  →  R increases

      GAUGE FACTOR:   GF = (ΔR/R) / ε
      where ε = strain = ΔL/L  (dimensionless, in µm/m or "microstrain")

      Metal foil gauges:  GF ≈ 2.0
      Semiconductor gauges: GF ≈ 100-200 (far more sensitive, far more
                                         temperature-sensitive)

      PRACTICAL SENSITIVITY:
         A typical foil gauge has R = 350 Ω.
         ε = 1000 µm/m (0.1 % strain, a typical working level)
         ΔR/R = GF × ε = 2.0 × 0.001 = 0.002
         ΔR   = 350 × 0.002 = 0.7 Ω

      ⚠️ 0.7 Ω out of 350 Ω is 0.2 %. You cannot measure that with a
         multimeter. You MUST use a bridge and a differential amplifier.
```

**The Wheatstone bridge:**

```
                ┌──────── R1 ────────┬──────── R2 ────────┐
                │                    │                    │
              V_exc              V_out+                    │
                │                    │                    │
                │                 [ G ]  ← the amplifier sees V_out+ − V_out−
                │                    │                       │
                │                 V_out−                   │
                │                    │                    │
                └──────── R4 ────────┴──────── R3 ────────┘
                                     │
                                    GND

      V_out = V_exc × [ R2/(R1+R2) − R3/(R3+R4) ]

      At BALANCE (all R equal):  V_out = 0
      One gauge changes by ΔR:   V_out ≈ V_exc × ΔR/(4R)   for small ΔR
```

**Bridge configurations:**

| Config | Gauges | Sensitivity (relative) | Temperature compensation | Cost | Verdict |
|---|---|---|---|---|---|
| **Quarter bridge** | 1 active gauge + 3 fixed resistors | **1×** | ❌ None — a 10 °C change in the gauge's temperature gives a false reading larger than the load signal | ₹100 | ⚠️ **Only acceptable for a demonstration.** Every load cell you buy is NOT this |
| **Half bridge** | 2 active gauges (one in tension, one in compression) | **2×** | ✅ Good — both gauges see the same temperature, and their drifts cancel | ₹250 | ✅ Acceptable for a home-built beam |
| **Full bridge** ⭐ | 4 active gauges (2 tension, 2 compression) | **4×** | ✅ **Excellent** — all four see the same temperature | ₹500–900 | ✅ **What every commercial load cell uses. Use this.** |
| **Commercial load cell** ⭐ | Full bridge, factory-bonded, temperature-compensated, sealed | **4×** | ✅ Factory-compensated | ₹350–8,000 | ✅ **Strongly recommended for the UVCE test stand.** Building a reliable full bridge by hand, with correct bonding and temperature compensation, is a multi-week skill |

**Recommended load cells for a thrust stand:**

| Load cell | Capacity | Type | Accuracy | Output | Cost (INR) | Verdict |
|---|---|---|---|---|---|---|
| **TAL220 / YZC-133 (bar type)** | 1 / 5 / 20 / 50 kg | Half bridge (⚠️ needs 2 external resistors to complete the bridge) | ±0.05 % FS | ~1 mV/V | ₹250–600 | ✅ Cheapest. ⚠️ The `HX711` **does** provide the two completion resistors on-board; without them you have a half bridge and half the sensitivity. Buy the 5 kg and the 20 kg versions and use the right one for the motor |
| **Single-point platform load cell (e.g. CZL601)** | 5 / 10 / 20 / 50 kg | Full bridge | ±0.02 % FS | 2 mV/V | ₹400–1,200 | ✅ Better. Full bridge, better temperature compensation, aluminium |
| **S-type load cell (e.g. DYLY-103)** | 50 / 100 / 200 / 500 kg | Full bridge, stainless | ±0.03 % FS | 2 mV/V | ₹1,800–5,000 | ✅ **The right answer for a 2800 N·s motor.** A 2800 N·s K-class motor can peak at 800–1500 N, so a **200 kg (1960 N) S-type cell** gives you a 1.3–2.5× overload margin. A 50 kg cell would be destroyed |
| **Button/compression load cell (e.g. DYLY-108)** | 100 / 200 / 500 kg | Full bridge | ±0.05 % FS | 1.5 mV/V | ₹1,500–4,000 | ✅ Compact, easy to mount in a thrust plate. Good choice |
| **Load pin / custom** | — | Full bridge | — | — | ₹5,000+ | For a permanent stand |

### 6.2 ⚠️ Sizing the load cell — do the arithmetic first

```
  ⚠️ THE MOST COMMON TEST-STAND MISTAKE: buying a load cell that is
     too small and destroying it on the first fire.

  START FROM THE MOTOR:
     Total impulse:      2800 N·s  (rule 5.vii limit)
     Burn time:          assume 3.0-4.0 s  → CONFIRM from the thrust curve
     Average thrust:     2800 / 3.5 = 800 N
     Peak thrust:        ⚠️ 1.3-2.0 × average for a progressive-burning
                         grain = 1040-1600 N

  ADD THE MOUNTING AND ALIGNMENT ERRORS:
     Off-axis loading, thrust-plate misalignment, and vibration can add
     20-50 % to the apparent axial load.
     Design peak:        1600 × 1.5 = 2400 N

  APPLY AN OVERLOAD MARGIN:
     Load cells are rated for 150 % safe overload and 200-300 % ultimate.
     You want to operate at NO MORE THAN 50 % of rated capacity, so that
     a mis-fires or a hard start does not destroy the cell.
     Required capacity:  2400 / 0.5 = 4800 N  ≈  490 kg

  ⭐ THEREFORE: for the 2800 N·s K-class motor, buy a
     **500 kg (4900 N) S-type or button load cell.**
     A 200 kg cell gives you only 1.2× margin at the design peak and
     WILL be damaged by a hard start.
     A 50 kg cell will be destroyed on the first fire.

  ⚠️ But do not go absurdly large either: a 500 kg cell measuring a
     100 N idle load is at 2 % of full scale, where the accuracy spec
     (±0.03 % FS = 1.5 N) is still fine but the signal is small.
     ⭐ IF BUDGET ALLOWS: buy TWO cells (200 kg and 500 kg) and use the
     appropriate one. The 200 kg cell gives better resolution for small
     motors; the 500 kg cell survives the K-class.
```

### 6.3 Excitation and amplification

**The signal you are trying to measure:**

```
  Load cell:  2 mV/V output at rated capacity, 500 kg (4900 N) rated
  Excitation: 5.0 V

  Full-scale output:  2 mV/V × 5.0 V = 10.0 mV at 4900 N
  Sensitivity:        10.0 mV / 4900 N = 2.04 µV/N

  ⚠️ An Arduino's ADC has 4.9 mV per LSB (10-bit, 5 V ref).
     THE ENTIRE LOAD CELL OUTPUT (10 mV) IS TWO ADC COUNTS.
     You cannot measure thrust without an amplifier. Period.

  Required gain to use a 5 V, 10-bit ADC well:
     Want full scale (10 mV) to map to ~4.5 V  →  gain = 450
  Required gain for a 3.3 V, 12-bit ADC (0.806 mV/LSB):
     Want 10 mV → 2.9 V  →  gain = 290
     ⭐ With a 24-bit ADC (HX711) you need far less gain — the ADC
        does the work.
```

**Amplifier options:**

| Option | Chip | Resolution | Sample rate | Gain | Interface | Cost (INR) | Verdict |
|---|---|---|---|---|---|---|---|
| **HX711 breakout** ⭐ | Avia HX711 | **24-bit ΔΣ** | **10 or 80 SPS** | 32/64/128 (selectable) | 2-wire bit-banged | ₹90–250 | ✅ **RECOMMENDED for a first stand.** On-board bridge-completion resistors, on-chip regulator, differential input, and a 24-bit ADC. ⚠️ **80 SPS maximum** — see §6.5 |
| **HX717** | Avia HX717 | 24-bit | **320 SPS** | 32/64/128 | 2-wire | ₹250–450 | ✅ **The upgrade for 1 kHz sampling.** 4× faster than the HX711 |
| **INA125** | TI INA125 | Instrumentation amp, gain set by one resistor | **Analog, instantaneous** | 4–10 000 | Analog → any ADC | ₹350–700 | ✅ **The right answer for 1 kHz.** Gain = 4 + 60 kΩ/R_g. Pair with a fast external ADC (ADS1115 at 860 SPS, or the STM32's internal ADC at 1 MSps) |
| **INA333 / AD8236** | TI / ADI | Instrumentation amp | Analog | 1–1000 | Analog | ₹250–600 | ✅ Excellent modern in-amp, low offset drift |
| **ADS1232** | TI | 24-bit ΔΣ, **PGA** | **10/80 SPS** | 1–128 | SPI | ₹600–1,200 | ✅ Reference-grade weigh-scale ADC. 80 SPS limit again |
| **ADS1256** | TI | **24-bit ΔΣ, 8-channel** | **30 kSPS** | 1–64 | SPI | ₹1,200–2,500 | ✅ **The professional answer for a 1 kHz stand.** Overkill for one channel but superb |
| **MCP3421 / ADS1115** | Microchip / TI | 18-bit / 16-bit ΔΣ | 3.75 / 860 SPS | 1–8 (ADS1115 PGA) | I2C | ₹180–450 | ⚠️ 16-bit gives 0.15 mV/LSB at ±4.096 V — with a gain of 200 that is 0.77 µV, which is adequate. **ADS1115 at 860 SPS + an INA333 is a good 1 kHz-ish combination** |

**HX711 wiring (the standard configuration):**

```
                    ┌──────────────────────────────────────┐
   LOAD CELL        │            HX711 MODULE              │
  ┌──────────┐      │                                      │
  │  RED  ───┼──────┼──▶ E+   (excitation +)               │
  │  BLACK ──┼──────┼──▶ E−   (excitation −)               │
  │  WHITE ──┼──────┼──▶ A−   (signal −)                   │
  │  GREEN ──┼──────┼──▶ A+   (signal +)                   │
  │  (SHIELD)┼──────┼──▶ GND  (⚠️ shield to GND at the     │
  └──────────┘      │          HX711 end ONLY, not both)   │
                    │                                      │
                    │  VCC ◀── 5.0 V (⚠️ see note)         │
                    │  GND ◀── GND (analog star point)     │
                    │  DT  ──▶ MCU GPIO (data, 3.3 V OK)   │
                    │  SCK ──▶ MCU GPIO (clock, 3.3 V OK)  │
                    └──────────────────────────────────────┘

  ⚠️ HX711 VCC: the module's on-board regulator and the excitation
     voltage come from VCC. 5.0 V gives you the full 2 mV/V output.
     At 3.3 V you lose 34 % of your sensitivity but the logic becomes
     directly compatible. ⭐ RUN IT AT 5.0 V and check that the module's
     DT/SCK outputs are 3.3 V-safe (most HX711 modules have a 5 V
     output on DOUT — add a 10 kΩ/20 kΩ divider or a 74LVC1T45 level
     shifter). ⚠️ A 5 V DOUT into a 3.3 V STM32 pin will eventually
     destroy the pin.

  ⚠️ The HX711's E+ is the excitation source for the bridge. If your
     load cell is a HALF bridge (TAL220), the module's on-board 1 kΩ
     resistors complete the bridge. If it is a FULL bridge (S-type),
     do not add anything.
```

**Noise and layout for a load cell front end — non-negotiable:**

| Rule | Why |
|---|---|
| **Twisted pair for the signal wires, shielded cable overall** | 2 µV/N is deep in the noise floor. Thermocouple effects at the terminals alone are ~1 µV/°C |
| **Shield grounded at ONE end only (the amplifier end)** | Grounding both ends creates a ground loop; the loop current appears directly in your measurement |
| **Keep the load cell cable away from the ignition wiring and the servo wiring** | A 5 A ignition pulse induces tens of mV into a parallel cable |
| **Separate the excitation supply from the digital supply** | Use a dedicated low-noise LDO (or the HX711's own regulator) for excitation, not the same 5 V rail as the SD card |
| **Star-ground the analog section** | Return all analog grounds to one point at the HX711's GND pin |
| **Physically separate the load cell from the motor casing** | A 40 °C temperature rise in the load cell changes its zero by 0.01–0.05 % FS, which on a 500 kg cell is **0.5–2.5 kg of false thrust**. Use a thermal break (a ceramic or phenolic washer) between the motor mount and the load cell |
| **⚠️ Preload the load cell** | A thrust stand should apply 5–10 % of rated capacity as a static preload, so the cell never goes into tension and never leaves its linear region. This also makes the mounting stiff, which raises the stand's resonant frequency |

### 6.4 Calibration with known masses

```
  ⭐ THE DEAD-WEIGHT CALIBRATION PROCEDURE

  APPARATUS
    • Known masses. ⚠️ Do NOT use "a 5 kg dumbbell" — you do not know
      what it weighs.
      BEST:  a set of calibrated test weights (₹3,000-8,000 for a
             1 mg - 5 kg set, or borrow from the college's physics lab)
      GOOD:  a 20 kg digital kitchen scale (₹800-2,000) with 1 g
             resolution, used to weigh whatever you load
      TRACEABLE-ISH: 5 L of water = 4.99 kg at 20 °C, weighed on a
             kitchen scale
    • A stable, level, rigid mounting for the load cell.
    • The load cell mounted EXACTLY as it will be in the stand —
      same bolts, same torque, same preload, same cable routing.

  PROCEDURE
    1. Zero the system with NO load. Record 2000 samples at the target
       rate. Compute the mean and the standard deviation.
          → the standard deviation is your NOISE FLOOR in counts.
          → convert to newtons using a provisional scale factor.
          → ⚠️ If the noise floor is > 0.1 % of full scale, fix the
             grounding/shielding before continuing.

    2. Apply masses in a MONOTONIC INCREASING sequence:
          0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 % of the
          expected peak thrust, expressed as mass.
          For a 1600 N design peak: 0, 16, 33, 49, 65, 82, 98, 114,
          130, 147, 163 kg
          ⚠️ Use masses appropriate to the stand. Never exceed the
             cell's rated capacity.

    3. At each step: wait 10 s for the cell to settle and for creep to
       stabilise, then record 2000 samples. Use the MEAN.

    4. Repeat the sequence DECREASING (to expose hysteresis) and then
       INCREASING a third time (to expose repeatability).

    5. Fit a straight line (least squares) to the INCREASING and
       DECREASING means combined:
            F_counts = a × mass_kg + b
       with g = 9.80665 m/s² locally... ⚠️ Actually use the local g:
            g at Bengaluru (12.97° N, 920 m) = 9.7877 m/s²
            ⚠️ NOT 9.80665. A 0.2 % error in g is a 0.2 % error in
               every thrust measurement.

    6. Compute the residuals. PASS if:
            • R² > 0.9999
            • max residual < 0.2 % of full scale
            • hysteresis (max difference between the increasing and
              decreasing curves at the same load) < 0.3 % of full scale
            • repeatability (difference between the 1st and 3rd
              increasing runs) < 0.1 % of full scale

    7. Store {a, b, g_local, date, operator, cell serial} in FRAM and
       in the calibration log. Print a calibration certificate for the
       CDR.

  ⚠️ RE-CALIBRATE if:
       • the load cell is remounted or re-torqued
       • the amplifier gain or the excitation voltage changes
       • the stand has been transported
       • more than 3 months have passed
```

### 6.5 Building a thrust stand that samples at 1 kHz

**Why 1 kHz:**

```
  A K-class motor's thrust curve has structure at 10-100 Hz:
     • ignition spike (a few ms)
     • grain surface regression and sliver effects
     • erosive burning onset (a step change)
     • burn-through / chuffing (10-200 Hz oscillations)
     • combustion instability (often 100-2000 Hz)

  ⚠️ NYQUIST: to see 100 Hz you must sample at > 200 Hz. To CHARACTERISE
     a 100 Hz oscillation you want 10 samples per cycle = 1 kHz.
     To catch a 5 ms ignition spike you need ≥ 1 kHz.

  ⭐ 1 kHz is the standard for amateur motor testing. Do not settle
     for less.

  ⚠️ BUT: at 1 kHz, an HX711 running at 80 SPS gives you 12.5 ms of
     data smeared across one sample — a 5 ms ignition spike is INVISIBLE.
     THE HX711 CANNOT DO 1 kHz.
```

**Two viable 1 kHz architectures:**

| | Architecture A — Analog in-amp + fast ADC | Architecture B — HX717 at 320 SPS |
|---|---|---|
| Front end | INA333 or INA125, gain 200–500 | HX717 |
| ADC | STM32 internal ADC (1 MSps, 12-bit) or ADS1115 (860 SPS, 16-bit) | On-chip 24-bit ΔΣ |
| Effective rate | **1–10 kHz** ✅ | **320 SPS** ⚠️ |
| Effective resolution | 12-bit over 3.3 V with a gain of 300 → 3.3/(4096×300) = **2.7 µV** = **1.3 N** ✅ | 24-bit with a gain of 128 → sub-newton ✅ |
| Complexity | Medium (analog layout matters) | Low |
| Verdict | ✅ **Required for 1 kHz** | ⚠️ Fine for a 100 Hz-class characterisation, not for 1 kHz |

**Recommended 1 kHz thrust stand:**

```
  ┌──────────────┐   2 mV/V   ┌────────────┐  0-3 V   ┌─────────────────┐
  │ LOAD CELL    │───────────▶│  INA333    │─────────▶│ STM32 ADC       │
  │ 500 kg       │  shielded  │ gain=300   │  RC      │ PA0, TIM2-trig  │
  │ full bridge  │  twisted   │ R_g = 202Ω │  1 kΩ +  │ 1 kHz, DMA      │
  └──────────────┘    pair    └────────────┘  100 nF  └────────┬────────┘
        ▲                                                       │
        │ excitation                                            │ DMA buffer
        │                                                       ▼
  ┌─────┴──────────┐                            ┌─────────────────────────┐
  │ 5.000 V REF    │                            │ SD CARD (SPI, 20 MHz)    │
  │ REF5050 (₹450) │                            │ 1 kHz × 32 B = 32 kB/s   │
  │ or LT1027       │                            │ ⚠️ Must sustain this     │
  │ ⚠️ NOT the 5 V  │                            │    continuously          │
  │   buck rail     │                            └─────────────────────────┘
  └────────────────┘

  ⚠️ THE EXCITATION MUST BE RATIOMETRIC OR REGULATED:
     • Ratiometric: use the SAME reference for the bridge excitation and
       the ADC reference. Then a reference drift cancels exactly.
       ⭐ THIS IS THE RIGHT ANSWER. Feed the ADC VREF+ and the bridge
       excitation from the same REF5050.
     • Regulated: a separate precision reference for each. Works, but
       you must characterise both drifts.

  ⚠️ SD CARD SUSTAINED THROUGHPUT:
     1 kHz × 32 bytes = 32 kB/s. A Class 10 card does 10 MB/s, so there
     is 300× headroom — BUT you must write in 512-byte block chunks
     (16 samples) and use a double buffer, or the card's 100 ms write
     latency will stall your DMA. Use the STM32's DMA + a 4 kB ring
     buffer and flush to the card in the main loop.

  ⚠️ DATA VOLUME: a 4-second burn at 1 kHz × 32 bytes = 128 kB.
     Add the pressure channels at 1 kHz: another 64 kB.
     ⭐ Totally manageable on an SD card. Log for 30 s before and after
     the burn so you capture the ignition transient and the tail-off.
```

**Other channels to log at 1 kHz alongside thrust:**

| Channel | Sensor | Why 1 kHz |
|---|---|---|
| **Chamber pressure** | See §7 | The primary diagnosis of a CATO, an over-pressure, or erosive burning. **Thrust alone cannot tell you why a motor failed** |
| **Thrust** | Load cell | The performance measurement |
| **Motor casing temperature** | K-type at the casing | ⚠️ 10 Hz is enough — thermal mass is slow. Do not waste bandwidth |
| **Ambient temperature** | DS18B20 | 1 Hz |
| **Supply voltage** | Divider | 1 kHz, because a brown-out during the burn is a real failure mode |
| **Ignition current** | Shunt + INA240 | 1 kHz, to see the igniter's actual firing profile |

**A 1 kHz thrust-stand checklist:**

- [ ] Load cell rated ≥ 2× the expected peak thrust, preloaded to 5–10 %
- [ ] Precision excitation (REF5050 or equivalent), **not** the buck rail
- [ ] Ratiometric ADC reference = bridge excitation
- [ ] Shielded twisted-pair signal cable, shield grounded at the amplifier end only
- [ ] Analog star ground, separate from the digital ground
- [ ] Thermal break between the motor mount and the load cell
- [ ] **Calibrated with known masses on the assembled stand**, R² > 0.9999
- [ ] 1 kHz sampling verified by injecting a known square wave and confirming the recorded edges are ≤ 1 ms wide
- [ ] SD card write verified at sustained 32 kB/s for 60 s **before** the fire
- [ ] A hardware **arming** switch and a mechanical **safe/arm** so the stand cannot be triggered accidentally
- [ ] The stand anchored to ≥ 50 kg of ballast or bolted to a concrete pad
- [ ] **⚠️ Remote operation from behind hard cover. No exceptions.**

---

## 7. Pressure transducer for chamber pressure

### 7.1 Why chamber pressure is the single most valuable test-stand measurement

Thrust tells you *what* the motor did. **Chamber pressure tells you *why*.**

| Observation | Diagnosis |
|---|---|
| Pressure spike at ignition, then normal | Normal ignition transient |
| **Pressure plateau 30–50 % below design** | ⚠️ **Nozzle erosion, or a grain crack, or a low-density grain** |
| **Pressure rising steadily through the burn** | ⚠️ **Erosive burning** — the port-to-throat ratio is dropping below ~2. **A CATO precursor.** Shut down the programme and fix the grain geometry |
| **Sharp pressure spike then a drop to zero** | ⚠️ **CATO** — the casing failed or the grain cracked |
| Pressure oscillating at 100–2000 Hz | Combustion instability |
| Pressure decaying too early | Grain sliver, or an incomplete burn |
| Kn (burning area / throat area) computed from P and the burn rate | ✅ **The fundamental design verification** — compare against your predicted Kn |

### 7.2 Transducer types

| Type | Principle | Range | Accuracy | Response | Cost (INR) | Verdict |
|---|---|---|---|---|---|---|
| **Strain-gauge pressure transducer** (e.g. **Honeywell MIP / PX3**, **Ashcroft**, **Sensata**) | A strain gauge bonded to a diaphragm; the same Wheatstone bridge as a load cell | 0–10, 0–25, 0–70 bar | ±0.25–0.5 % FS | **1–5 ms** (mechanical diaphragm) | ₹4,000–18,000 | ✅ **RECOMMENDED for a student test stand.** Robust, cheap relative to piezo, tolerant of a rough environment, and the slow response is *acceptable* for a burn-rate/Kn analysis |
| **Piezoresistive silicon transducer** (e.g. **Keller 4LD/7LD**, **MEAS MSP300**) | Silicon diaphragm with diffused piezoresistors | 0–10 to 0–1000 bar | ±0.1–0.5 % FS | 1–2 ms | ₹6,000–25,000 | ✅ Better accuracy, faster, more expensive. A good middle ground |
| **Piezoelectric transducer** (e.g. **PCB Piezotronics 113B**, **Kistler 601C**) | A quartz crystal generates charge proportional to *dynamic* pressure change | 0–70 to 0–700 bar | ±1 % FS | **1–10 µs** ✅ | ₹35,000–2,00,000 | ⚠️ **The correct instrument for combustion instability** — it resolves the 100–2000 Hz oscillations. But: (a) it only measures *changes*, so you need a static reference; (b) it needs a **charge amplifier** (another ₹25,000+); (c) the cost is out of reach. **Mention it in the CDR as the professional instrument and explain why you did not use it** |
| **Piezo-resistive MEMS on a breakout** (e.g. **MPX5700**, **MPX5010**) | Silicon piezoresistive | 0–700 kPa (MPX5700) | ±2.5 % FS | ~1 ms | ₹600–1,600 | ⚠️ Cheap but 2.5 % FS is ±17 kPa on a 700 kPa range — **not enough to see a Kn deviation**. OK for a "did it fire?" check. ⚠️ **Check the temperature rating: most are 0–85 °C and the port will see 200–1000 °C gas** |
| **Inexpensive industrial 0–10 bar / 0–25 bar transmitter** (e.g. **Autonics**, **Wika**, generic Chinese 4–20 mA) | Piezoresistive, 4–20 mA or 0–5 V output | 0–10 to 0–100 bar | ±0.5 % FS | 1–5 ms | ₹1,800–6,000 | ✅ **The pragmatic student answer.** A 0–25 bar (0–2.5 MPa) 4–20 mA transmitter costs ₹2,000–4,000, and 4–20 mA is immune to cable noise. ⚠️ Verify the **temperature at the transducer**: fit a **standoff tube** filled with silicone oil or grease |

### 7.3 Range selection — the arithmetic

```
  ⚠️ A KNSB / commercial K-class motor's chamber pressure:
     Design point (typical for a KNSB amateur motor): 2-4 MPa
                                                     (20-40 bar)
     Commercial APCP K-class:                          4-7 MPa
                                                     (40-70 bar)
     CATO / over-pressure transient:                   2-5× design
                                                     (up to 200-350 bar
                                                      momentarily)

  ⭐ SELECTION RULE:
     Range = 2.5-3× the expected peak chamber pressure.

     For a 4 MPa (40 bar) design with a 3× CATO transient:
        Required range = 4 × 3 = 12 MPa = 120 bar
     ⚠️ But a 0-120 bar sensor measuring a 40 bar nominal is at 33 % FS,
        where a ±0.5 % FS sensor has ±0.6 bar of error (1.5 % of reading).
        That is acceptable.

  ⭐ PRACTICAL CHOICE:
     • For a 38-54 mm KNSB motor (2-4 MPa):  0-10 MPa (0-100 bar) transducer
     • For a 75-94 mm motor (3-6 MPa):       0-16 MPa (0-160 bar)
     • ⚠️ NEVER use a 0-100 bar sensor on a motor that can transient to
       200 bar. You will destroy the sensor AND lose the data from the
       one event you most needed to record.

  ⚠️ AND CHECK THE OVERPRESSURE RATING:
     Most strain-gauge transducers survive 2× rated pressure without
     damage and 3-5× without bursting. So a 0-10 MPa sensor survives a
     20 MPa transient. Confirm the spec: "proof pressure" and "burst
     pressure" are different numbers.
```

### 7.4 ⚠️ Safe mounting — this is a safety-critical item

| Requirement | Detail |
|---|---|
| **Thermal protection** ⭐ | Chamber gas is **1500–2500 °C**. A transducer's diaphragm is rated to 80–125 °C. **You MUST isolate it thermally.** The standard method is a **standoff tube** (a 50–150 mm long, 2–3 mm ID tube) filled with **silicone oil, high-temperature grease, or RTV**, connecting the chamber port to the transducer face. The gas pushes on the grease, the grease pushes on the diaphragm, and the grease column is a thermal barrier. ⚠️ The grease column also **low-pass filters** the response — a 100 mm grease column can limit you to ~50 Hz. **Trade-off: thermal safety versus bandwidth. State which you chose and why** |
| **Mechanical isolation** | The transducer must NOT be rigidly coupled to the motor casing's vibration. Use a short flexible capillary or a soft-mounted bracket. ⚠️ A transducer that resonates with the motor gives you a pressure trace full of garbage |
| **Pressure port orientation** | Mount with the port **downward or horizontal** so that any condensed combustion products drain away from the diaphragm. An upward-facing port fills with slag |
| **Sealing** | Use a **copper crush washer** or an **O-ring in a machined gland**, never PTFE tape alone on a high-pressure port. ⚠️ PTFE tape extrudes under pressure and the joint fails |
| **Restraint** ⚠️ | The transducer is a **projectile** if the fitting fails. A 200 g transducer at 4 MPa can be launched across the test cell. **Fit a physical restraint** (a bracket or a strap) independently of the pressure fitting |
| **Cabling** | 4–20 mA over a shielded twisted pair. Shield grounded at the DAQ end only. Route the cable **away from the ignition wiring** |
| **Zeroing** | Zero the transducer **at atmospheric pressure immediately before the fire**, with the stand at operating temperature. Log the zero and the ambient pressure |
| **Calibration** | Dead-weight tester (the correct tool, ₹40,000+) or a **comparison calibration against a known-good gauge** at 0, 25, 50, 75, 100 % FS. ⚠️ **A pressure transducer is a safety instrument — a wrong reading means an over-pressure event goes undetected.** Calibrate before every test campaign |
| **⚠️ NEVER** | Never pressurise a chamber with the transducer installed and no restraint. Never test a transducer's range by hitting it with a known pressure above its rating. Never leave a pressurised system unattended |

**Recommended mounting schematic:**

```
   ┌─────────────────────────────────────────────────────────────┐
   │  MOTOR CASING / TEST CHAMBER                                │
   │                                                             │
   │   ┌──── pressure port (machined, 1/4" NPT or M10×1) ────┐   │
   │   │                                                     │   │
   └───┼─────────────────────────────────────────────────────┼───┘
       │                                                     │
       ▼                                                     │
   ┌───────────────────────────────┐                         │
   │  STANDOFF TUBE                │  ⭐ 100 mm long, 2 mm ID │
   │  ╔═══════════════════════════╗│     filled with          │
   │  ║  silicone oil / HT grease ║│     high-temp silicone   │
   │  ╚═══════════════════════════╝│                         │
   └───────────────┬───────────────┘                         │
                   │  copper crush washer                    │
                   ▼                                         │
   ┌───────────────────────────────┐                         │
   │  PRESSURE TRANSDUCER          │                         │
   │  0-10 MPa, 4-20 mA            │                         │
   │                               │                         │
   │  ┌─────────────────────────┐  │                         │
   │  │ ⚠️ RESTRAINT BRACKET    │  │  ← independent of the   │
   │  │    (steel strap)        │  │    pressure fitting     │
   │  └─────────────────────────┘  │                         │
   └───────────────┬───────────────┘                         │
                   │                                         │
                   ▼  shielded twisted pair                  │
   ┌───────────────────────────────┐                         │
   │  250 Ω sense resistor         │  4-20 mA → 1-5 V        │
   │  → ADC (or a dedicated        │                         │
   │    4-20 mA receiver)          │                         │
   └───────────────────────────────┘                         │
                   │                                         │
                   ▼                                         │
   ┌───────────────────────────────┐                         │
   │  DAQ at 1 kHz                 │                         │
   │  ⚠️ ADC shares the reference  │                         │
   │     with the sense resistor   │                         │
   └───────────────────────────────┘                         │
```

---

## 8. ADC noise, grounding, shielding, and filtering

### 8.1 ⚠️ Why analog signals near a firing motor are noisy

This is not a theoretical concern. A firing motor produces one of the harshest electromagnetic environments a student will ever work in:

| Noise source | Mechanism | Magnitude | Frequency content |
|---|---|---|---|
| **Igniter firing** | A 5 A current step through a wire loop. `V = −L·di/dt` — a 1 m loop with 1 µH and a 1 µs rise gives 5 V of induced spike in any nearby parallel conductor | **1–10 V** on an unshielded parallel wire | DC–100 MHz |
| **Piezo ignition / spark sources** | Broadband impulsive EMI | kV/m field strength at 100 mm | DC–1 GHz |
| **Motor vibration** | Triboelectric effect in cables — a cable that flexes generates charge | 10 µV–10 mV | 10 Hz–10 kHz |
| **Combustion instability** | Pressure oscillations mechanically coupling into the transducer | 1–20 % of the pressure signal | 100–2000 Hz |
| **Servo PWM and stall current** | 50 Hz PWM with 1–3 A edges on the same ground return as the analog section | 10–500 mV of ground bounce | 50 Hz + harmonics to 10 MHz |
| **DC-DC converters** | Switching at 500 kHz–2 MHz, plus the diode's reverse recovery | 10–100 mV ripple | 500 kHz–50 MHz |
| **Radio transmitter** | 2 W at 2.4 GHz, coupling capacitively into a high-impedance analog node | 1–100 mV of rectified DC offset | 2.4 GHz |
| **Ground loops** | Two "grounds" at different potentials, connected by a signal wire | 10 mV–2 V | 50 Hz (mains) + DC |
| **Thermocouple junctions** | Every dissimilar-metal junction is a temperature-dependent voltage source | 1–10 µV/°C per junction | DC (drifts with temperature) |

> **The consequences for a 2.04 µV/N load cell:** the noise sources above are **1000–1 000 000× larger** than the signal you are trying to measure. **Analog signal integrity is not a refinement; it is the difference between a measurement and a random number generator.**

### 8.2 Noise reduction — in order of effectiveness

| Rank | Technique | Effectiveness | Cost | When to use |
|---|---|---|---|---|
| **1** | **Go digital as early as possible** | Removes 90 % of the problem | — | ⭐ **Always.** An I2C/SPI sensor (MS5611, ICM-42688-P, DS18B20, MAX31855) is immune to cable-induced noise because the signal is already a bitstream. **Prefer digital sensors wherever a digital option exists.** This is why the avionics uses I2C/SPI for everything except the voltage divider |
| **2** | **Use a differential input** (instrumentation amp or a differential ADC) | 20–40 dB | ₹250–700 | ⭐ **Always for a load cell, thermocouple, or pressure transducer.** A differential input rejects common-mode noise by its CMRR (80–120 dB for a good in-amp) |
| **3** | **Twisted pair for every signal** | 10–30 dB of magnetic pickup reduction | ₹20/m | ⭐ **Always.** Twisting makes the loop area of each half-turn cancel. Two parallel wires pick up 10–100× more |
| **4** | **Shielded cable, shield grounded at ONE end** | 20–40 dB against electric fields | ₹50–150/m | ✅ Signal cables > 100 mm, especially anything near the ignition wiring. ⚠️ **Grounding both ends creates a ground loop that injects MORE noise than the shield removes** |
| **5** | **4–20 mA current loop instead of a voltage signal** | Effectively immune to cable resistance and induced voltage | ₹500–2,000 | ✅ Any signal that must travel > 1 m in a noisy environment, e.g. the chamber pressure transducer |
| **6** | **Physical separation** (route signal cables ≥ 100 mm from power cables, and never parallel) | 20–40 dB | ₹0 | ⭐ **Always, and it is free.** Cross at 90° if you must cross |
| **7** | **Star grounding** — all analog returns to ONE point at the ADC's ground pin | 20–40 dB | ₹0 | ⭐ **Always.** Never daisy-chain analog grounds |
| **8** | **Single-point analog/digital ground tie** | Removes ground-loop currents from the ADC reference | ₹0 | ⭐ **Always.** Tie at the MCU's `VSSA` pin |
| **9** | **RC low-pass at the ADC input** (1 kΩ + 100 nF → fc = 1.6 kHz) | 20 dB/decade above fc | ₹5 | ✅ Every analog input. Serves double duty as an anti-alias filter |
| **10** | **Ferrite bead in the supply of every analog IC** (600 Ω @ 100 MHz) | 10–20 dB | ₹5 | ✅ Always |
| **11** | **Oversampling + decimation** (average 16 samples) | 2 bits of ENOB, ~4× noise reduction | ₹0 (CPU time) | ⭐ **Always, and it is free.** This is the single cheapest noise improvement available |
| **12** | **Separate, quiet LDO for analog** | 20–40 dB | ₹45 | ⭐ **Always.** Never run an ADC from the same rail as the SD card |
| **13** | **Guard ring around high-impedance nodes**, tied to analog ground | 10–20 dB against surface leakage and capacitive coupling | ₹0 | ✅ For the load-cell input pins and the op-amp inputs |
| **14** | **Conformal coating** | Prevents humidity-induced leakage currents | ₹800/can | ✅ After all calibration is done. ⚠️ It also makes rework hard |
| **15** | **Shielding the whole avionics bay** (aluminium foil or a metal can) | 20–40 dB | ₹200–600 | ✅ If you have an RF-coupling problem. ⚠️ Ensure the shield does not block the antenna |

### 8.3 Grounding — the star topology

```
   ⭐ RULE: there is exactly ONE point where analog ground and digital
      ground meet. Everything else is a star from its own local point.

   ┌───────────────────────────────────────────────────────────────────┐
   │                                                                   │
   │   ANALOG GROUND ISLAND              DIGITAL GROUND ISLAND         │
   │   ─────────────────────             ─────────────────────         │
   │                                                                   │
   │   ┌──────────────┐                  ┌──────────────┐              │
   │   │ MS5611 GND   │                  │ STM32 VSS    │              │
   │   └──────┬───────┘                  └──────┬───────┘              │
   │   ┌──────┴───────┐                  ┌──────┴───────┐              │
   │   │ IMU GND      │                  │ SD card GND  │              │
   │   └──────┬───────┘                  └──────┬───────┘              │
   │   ┌──────┴───────┐                  ┌──────┴───────┐              │
   │   │ MCP6002 GND  │                  │ FRAM GND     │              │
   │   └──────┬───────┘                  └──────┬───────┘              │
   │   ┌──────┴───────┐                  ┌──────┴───────┐              │
   │   │ ADC VREF−    │                  │ XBee GND     │              │
   │   └──────┬───────┘                  └──────┬───────┘              │
   │          │                                 │                     │
   │          └────────────┬────────────────────┘                     │
   │                       │                                          │
   │              ⭐ THE SINGLE TIE POINT                              │
   │                 (at the MCU's VSSA/VREF− pin,                     │
   │                  with a 0 Ω link or a ferrite)                    │
   │                       │                                          │
   │                       ▼                                          │
   │              ┌─────────────────┐                                 │
   │              │  POWER GROUND   │  ← bucks, battery, servos       │
   │              │  (high current) │                                 │
   │              └─────────────────┘                                 │
   │                                                                   │
   │   ⚠️ THE SERVO GROUND RETURNS TO THE POWER GROUND, NEVER THROUGH  │
   │      THE ANALOG OR DIGITAL ISLAND. A 2.5 A servo stall through   │
   │      the digital ground raises it by 50-200 mV and corrupts       │
   │      every ADC reading.                                          │
   └───────────────────────────────────────────────────────────────────┘
```

### 8.4 ADC-specific practices

| Practice | Detail |
|---|---|
| **Use the ADC's own reference, not VDD** | `VREF+` from a dedicated LDO or a precision reference (REF3033, ₹250). ⚠️ **If VREF is VDD and VDD sags 50 mV, every reading changes by 1.5 %** |
| **Ratiometric where possible** | If the sensor's excitation and the ADC reference come from the same source, supply drift cancels. ⭐ **Use this for the load cell and the pressure transducer** |
| **Sample the ADC with a timer + DMA, never in a loop** | Deterministic timing, no jitter, and the CPU is free |
| **Discard the first sample after a channel change** | The sample-and-hold needs to settle |
| **Add a dummy read** | Many SAR ADCs need one conversion to settle after a MUX change |
| **Oversample and decimate** | 16× oversampling gains ~2 bits of ENOB for a 4× slower rate. **Free accuracy** |
| **Calibrate the ADC's own offset and gain** | Measure a known reference (e.g. an LM4040 2.500 V shunt) on each channel at two points and store the correction in FRAM. ⚠️ The STM32's ADC has a gain error of up to ±3 % and an offset of ±3 LSB — **uncorrected, that is 100 mV on a 3.3 V range, which is 10× the voltage field's 0.01 V requirement** |
| **Read the internal temperature sensor and the VREFINT channel** | The STM32 has an internal reference (`VREFINT`, 1.21 V nominal) whose *factory calibration value* is stored in system memory. Reading it tells you the actual VDD, which lets you ratiometrically correct every other channel. **This is what professionals do and it costs nothing** |

### 8.5 The measurement noise floor — the test you must run

```
  ⭐ THE NOISE FLOOR TEST (do this for EVERY analog channel)

  PROCEDURE
    1. Build the board in its final configuration.
    2. Short the analog input to analog ground (or apply a known,
       stable input).
    3. Power everything up — MCU, radio, SD card, servos, the works.
    4. Log 60 s at the final sample rate.
    5. Compute:
          mean   = ?
          stddev = ?    ← this is your RMS noise in counts
          p-p    = max - min
    6. Convert the stddev to physical units.
    7. REPEAT with the radio transmitting at full power.
    8. REPEAT with both servos stalled.
    9. REPEAT with the SD card writing continuously.

  PASS CRITERIA (as a fraction of full scale)
     • Idle:               RMS < 0.02 % FS,  p-p < 0.15 % FS
     • Radio transmitting: RMS within 2× of idle
     • Servos stalled:     RMS within 3× of idle
     • SD writing:         RMS within 2× of idle

  ⚠️ IF THE RADIO INCREASES YOUR NOISE BY MORE THAN 2×:
     you have an RF-coupling problem. Fixes, in order:
        1. Move the analog section further from the antenna
        2. Add a 100 pF capacitor across the analog input
        3. Add a ferrite bead in the analog supply
        4. Shield the analog section with a small metal can
        5. Change the antenna's orientation
     ⚠️ DO NOT FLY until this is fixed. A barometer with 6× the noise
        will not detect apogee reliably.

  📊 PUT THE PLOT IN THE CDR. Four traces — idle, radio, servos, SD —
     on one axes, with the RMS annotated. It is one of the most
     convincing figures you can produce.
```

---

## 9. Sensor calibration master schedule

| Sensor | What to calibrate | Method | Frequency | Record |
|---|---|---|---|---|
| **MS5611 / BMP390** | PROM/coefficient validity; noise floor; zero at pad | Read PROM twice and compare; 60 s static noise log; ZERO command on the pad | PROM: every boot. Noise: every board build. Zero: every launch | FRAM + calibration log |
| **IMU accelerometer** | 6-face bias and scale | Calibration cube, 6 orientations × 2000 samples | Every board build; after any remount | FRAM `{bias[3], scale[3]}` + certificate |
| **IMU gyroscope** | Bias; Allan deviation; temperature drift | 60 s static; 1–4 h static for Allan; temperature chamber | Bias: every boot after 5 s static. Allan: annually per part. Temp: once per board type | FRAM bias + a report |
| **Magnetometer** | Hard and soft iron | 3D figure-8 rotation, sphere/ellipsoid fit | Once, **with the airframe assembled** | FRAM `{offset[3], matrix[3][3]}` |
| **GNSS** | Static accuracy; TTFF | 30 min at a surveyed point; 5 cold starts | Once per module | Test report |
| **Voltage divider** | Offset and gain | Bench DMM at 2 points (6.0 V and 8.0 V) | Every board build | FRAM `{offset, gain}` |
| **Current shunt** | Offset and gain | Known current at 2 points (100 mA and 2 A) | Every board build | FRAM |
| **Load cell** | Offset, gain, linearity, hysteresis | Dead weights, increasing/decreasing/increasing | Before every test campaign; after any remount | Certificate + FRAM |
| **Pressure transducer** | Zero and span | Dead-weight tester or a comparison gauge at 0/25/50/75/100 % FS | Before every test campaign | Certificate + FRAM |
| **Thermocouple chain** | Offset and gain | Ice point (0.0 °C) + a second reference point | Once per chain; after any rewiring | Certificate + FRAM |
| **DS18B20** | Offset | Ice point; compare against a reference thermometer | Once per batch | Log |
| **All analog channels** | ADC offset and gain | A precision reference (LM4040 2.500 V) at 2 points | Every board build | FRAM |

**Calibration record template (paste this into the calibration log and the CDR):**

```
═══════════════════════════════════════════════════════════════════════
CALIBRATION RECORD
Sensor:            MS5611-01BA03
Serial / board:    FCB-REV-C / U3
Date:              2027-03-12
Operator:          <name>
Method:            PROM validation + 60 s static noise floor at 100 Hz
Reference:         NPL-traceable digital barometer (college physics lab)
Ambient:           24.3 degC, 905.2 hPa, 61 % RH

Results:
  PROM read 1:  C1=40123 C2=41345 C3=289 C4=241 C5=32768 C6=312
  PROM read 2:  C1=40123 C2=41345 C3=289 C4=241 C5=32768 C6=312   ✅ match
  PROM sanity:  ✅ all coefficients in the genuine range
  Noise floor:  mean = 90521.4 Pa,  stddev = 0.52 Pa   ✅
  Achievable altitude resolution at 1000 m:  0.52 × 0.094 = 0.049 m  ✅
  Zero-point check:  against the lab barometer, offset = -0.3 Pa   ✅

Conclusion:        PASS
Stored in FRAM:    board_id=FCB-REV-C, cal_date=20270312, crc=0x5A3F
Signature:         _______________
═══════════════════════════════════════════════════════════════════════
```

---

## 10. Summary — the recommended sensor suite

| Function | Part | Interface | Cost (INR) | Why |
|---|---|---|---|---|
| **Primary barometer** | **TE MS5611-01BA03** | SPI | ₹450–900 | 0.012 Pa LSB, measured 0.5 Pa RMS noise → **0.047 m resolution at 1000 m** ✅ |
| **Redundant barometer** | **Bosch BMP390** | I2C | ₹400–700 | Cross-check; a disagreement flags a sensor fault |
| **Primary IMU** | **TDK ICM-42688-P** | SPI @ 20 MHz | ₹600–1,100 | 70 µg/√Hz accel, ±2000 °/s gyro, 32 kHz ODR, genuinely available |
| **Alternative IMU** | **Bosch BMI088** | SPI, dual CS | ₹900–1,600 | Separate accel/gyro dies = best vibration robustness |
| **Fallback IMU** | **TDK ICM-20948** | SPI | ₹450–1,200 | Always in stock; adds a magnetometer |
| **GNSS** | **u-blox NEO-M8N** + active patch + CR2032 backup | UART | ₹1,100–1,800 | 10 Hz, GAGAN, mature, hot start in 2 s |
| **NavIC option** | **Quectel LC86G** or **Telit SE868-V3** | UART | ₹1,200–2,500 | IRNSS L5 — verify the datasheet before claiming it |
| **Temperature (reported)** | On-die in the barometer | — | ₹0 | Meets the 0.1 °C resolution requirement |
| **Temperature (bay/battery)** | **DS18B20** ×3 on one pin | 1-Wire | ₹270–750 | Cheap, digital, multiple on one wire |
| **Temperature (test stand)** | **K-type TC + MAX31855K 3V3** | SPI | ₹950–2,200 | Fault detection, 0.25 °C, 5 Hz is plenty |
| **Voltage** | 22 kΩ/10 kΩ 0.1 % + **MCP6002** buffer | Analog → ADC | ₹80 | Buffered divider with a software-calibrated gain |
| **Current (housekeeping)** | **INA226** | I2C | ₹300–600 | 16-bit, alert pin, bus voltage included |
| **Load cell (test stand)** | **500 kg S-type**, full bridge | → **INA333 + STM32 ADC @ 1 kHz** | ₹1,800–5,000 + ₹600 | Survives a K-class CATO; 1 kHz is achievable |
| **Chamber pressure** | **0–10 MPa, 4–20 mA industrial transmitter** | 250 Ω → ADC @ 1 kHz | ₹2,000–6,000 | 4–20 mA is noise-immune; grease-filled standoff for thermal protection |
| **Navigation filter** | Complementary (ship) → Kalman (upgrade) | — | ₹0 | Barometer + accelerometer, 3-state vertical channel |
| **Total sensor cost** | | | **₹7,800–15,000** | Flight sensors only; test-stand sensors are separate |

---

*Prepared for UVCE Rocketry Club, Bengaluru. Prices are Indian retail order-of-magnitude figures (2026) and must be re-quoted at purchase. **Counterfeit IMU and barometer breakouts are a genuine and widespread problem — see [Electronics BOM and Sourcing](Electronics_BOM_and_Sourcing.md) §"Counterfeit parts" for detection and avoidance.** All sensors must be calibrated and their calibration records carried into the CDR. Never fly an uncalibrated or unverified sensor.*
