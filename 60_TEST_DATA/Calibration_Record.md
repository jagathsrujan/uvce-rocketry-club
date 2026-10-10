# UVCE Rocketry Club — Calibration Record

**Folder:** `60_TEST_DATA/`
**Companion to:** `60_TEST_DATA/README.md`
**Parent context:** `40_SAFETY/Static_Test_Procedure.md` §3.3, §3.4, §7.1
**Maintained by:** the Safety Officer, who keeps the club's equipment calibration records
(`Safety_Manual_Master.md` §4.1)

> ## 🔴 AN UNCALIBRATED SENSOR MAKES THE DATA WORTHLESS FOR PERFORMANCE ANALYSIS.
>
> A thrust curve from an uncalibrated load cell is a **shape**, not a **measurement**. You cannot compute
> total impulse from it, you cannot compare it with a prediction, and you cannot use it to size a motor
> case. **A measurement you have not calibrated is not a measurement.**
>
> **Total impulse is the area under the thrust-time curve** (`Static_Test_Procedure.md` §7.1). If the
> curve's vertical scale is wrong, every number derived from it — impulse, delivered Isp, burn time
> against a pressure threshold, the comparison with the prediction — is wrong with it.

---

## 1. Scope

This record covers **every instrument whose reading is used to make a decision, take a measurement, or
produce a test result.** That is a wider list than just the load cell.

| Instrument type | Why it is on this list |
|---|---|
| **Load cell / thrust transducer** | Produces the thrust curve; total impulse is its integral |
| **Pressure transducer** | The chamber pressure trace is the single most diagnostic measurement in the test |
| **Reference pressure gauge / deadweight tester** | The standard the transducer is calibrated *against* |
| **Calibration masses (known masses)** | The standard the load cell is calibrated *against* — they must themselves be verified |
| **Proving ring** (if used) | Alternative load reference; must carry a valid certificate |
| **IR thermometer** | Used to hold the melt at 120–130 °C — a wrong reading is a safety issue, not just a data issue |
| **Probe / digital thermometer** | The cross-check against the IR reading; difference must be ≤ 2 °C |
| **Type-K thermocouple and logger** | Melt, case, and nozzle temperature measurement |
| **Precision scale** | Sets the 65/35 ratio — a wrong scale changes the propellant |
| **Anemometer** | Wind is a NO-GO criterion and must be measured, not estimated |
| **Barometric altimeter / flight computer** | Apogee and ejection timing |
| **IMU / accelerometer** | Flight dynamics, ejection events, recovery deployment |
| **Voltmeter / multimeter** | Continuity checks, battery voltage, igniter current |
| **Current-limited continuity tester** | Must be verifiably limited below 50 mA |
| **Oven / desiccator instrumentation** (if used) | Moisture checks on sorbitol |

**Any instrument on this list that has no current calibration record is out of service.** It is tagged,
removed from the flight/test kit, and reported to the Safety Officer as an equipment defect
(`Safety_Manual_Master.md` §8.1).

---

## 2. Calibration intervals

| Instrument | Interval | Pre-test verification required? |
|---|---|---|
| **Load cell** | Full calibration at least **every 6 months**, and after any event that could damage it (an over-range firing, a dropped instrument, a stand that moved) | **YES — verified immediately before the test with known masses. Before-and-after values recorded.** |
| **Pressure transducer** | Full calibration at least **every 6 months**, and after any exposure to combustion gas, over-pressure, or a thermal event | **YES — verified against a reference gauge or deadweight tester before the test** |
| **Reference gauge / proving ring / calibration masses** | Per the standard's own certificate, or **annually** where the certificate specifies no interval | YES — certificate must be in date |
| **Thermometers (IR and probe)** | **Every session**, cross-checked against each other and against a known reference (ice point / boiling point) | **YES — this session, recorded on FORM-02** |
| **Precision scale** | **Every session**, checked with a known mass | **YES — error must be ≤ 0.05 g** |
| **Anemometer** | Annually, or cross-checked against a second anemometer or a reliable weather station | YES — at the site |
| **Altimeter / flight computer** | Annually, or per the manufacturer's schedule | YES — zeroed and verified at the site |
| **IMU / accelerometer** | Annually, and checked for a static bias before each flight | YES |
| **Multimeter** | Annually, or against a known reference | YES |

**Session-level verification is not a substitute for full calibration.** A before-test check with known
masses **confirms** a calibration; it does not **replace** one.

**Where the club has no calibration capability** — pressure transducers usually — calibration is sent to
an external lab, and the **certificate is filed** in `60_TEST_DATA/calibration/` and referenced here by
certificate number.

---

## 3. How each instrument is calibrated

### 3.1 Load cell — calibrated with known masses

> **A load cell is calibrated with known masses** — or with a **lever arm amplifying a known mass**,
> where the lever ratio is documented and the calibration accounts for it.

**Method (direct known-mass loading):**

1. Mount the load cell **in the same orientation and mounting arrangement** it will be used in. A load
   cell calibrated on a bench and then installed on a lever arm is **not** calibrated
   (`Static_Test_Procedure.md` §3.3).
2. Zero the system, and record the **zero offset**.
3. Apply **known masses in ascending steps** across the expected working range — typically **five or
   more points**, from around 10% to around 100% of the expected peak thrust. For a load cell whose
   expected peak thrust is 50–80% of full scale, span the range that matters.
4. At each step, record the **applied load (N)** — mass in kg × 9.80665 m/s² — and the **indicated
   reading**.
5. **Apply, then remove**, and repeat in descending order, to expose hysteresis.
6. Hold each step long enough for the reading to settle. Record the settled value.
7. Fit a **linear regression** through the points. Record the **slope (N per count or N per volt)** and
   the **intercept (zero offset)**.
8. Record the **R² value** and the **maximum non-linearity** as a percentage of full scale.
9. **Before the test:** apply one or two known check masses and record the indicated value.
10. **After the test:** repeat the same check. **A drift of more than 2% of the reading invalidates the
    test data** — say so in the test report rather than adjusting the numbers.

**Lever-arm method (where used):**

- The lever ratio must be **documented and stable** — measure the arm lengths, do not assume them.
- The calibration must **account for the ratio**: the indicated load is the known mass × the ratio.
- The arm must be re-measured after any change to the mounting.
- Record the **arm lengths** in the notes column so the ratio can be recomputed later.

**Sizing rule:** the load cell must be sized so that **peak expected thrust is 50–80% of full scale**.
An oversized load cell loses resolution; an undersized one is destroyed.

**Sample rate reminder:** **≥ 100 Hz minimum, 1000 Hz preferred.** A 2-second burn at 100 Hz is only
200 samples. **Sample fast, always.**

### 3.2 Pressure transducer — calibrated against a reference gauge

> **A pressure transducer is calibrated against a reference gauge** (or a **deadweight tester**, which is
> the better primary standard where one is available).

**Method:**

1. Set up the transducer in a **pressure manifold** with the reference gauge and a controllable pressure
   source (a hand pump, a regulated gas bottle, or a hydraulic deadweight tester).
2. Confirm **no leaks** — a leak makes every point wrong and is the most common cause of a "drifting"
   transducer that was never drifting.
3. Record the **zero-pressure reading** (with the manifold vented to atmosphere).
4. Apply **ascending pressure steps** across the expected range — typically **five or more points**, from
   about 10% up to the maximum expected chamber pressure, and at least one point **above** the expected
   MEOP if the manifold allows it safely.
5. At each step, record the **reference gauge reading** and the **transducer output**.
6. **Apply, then bleed down**, and repeat in descending order, to expose hysteresis.
7. Fit a **linear regression**. Record the **slope (bar per volt or bar per count)** and the
   **zero offset**.
8. Record the **R² value**, the **maximum non-linearity**, and the **hysteresis** as percentages of full
   scale.
9. **Before the test:** a single-point check against the reference gauge.
10. **After the test:** the same check. **A drift of more than 2% of the reading invalidates the data.**

**Two hard requirements that go with the calibration:**

- **Rating:** the transducer must be rated to at least **2× the expected MEOP**. A transducer that
  saturates tells you nothing.
- **Thermal protection is mandatory:** a **grease-filled standpipe**, a **thermal barrier**, or a
  **standoff tube**. **A transducer exposed directly to combustion gas is destroyed within
  milliseconds** — and it will read plausibly right up to the moment it dies, which is worse than
  reading nothing.

**Sample rate:** same as thrust — **≥ 100 Hz**, preferably **1000 Hz**.

### 3.3 Other instruments — the short form

| Instrument | Method | Key acceptance criterion |
|---|---|---|
| **IR thermometer** | Compare against a calibrated probe thermometer or a known-temperature reference (ice point at 0 °C, boiling water at ~100 °C at the site's altitude) | Reading must agree with the reference; IR vs probe **difference ≤ 2 °C** |
| **Probe / digital thermometer** | Ice-point check (0 °C) and, where practical, a boiling-point check against the local boiling temperature | Within the manufacturer's stated accuracy |
| **Type-K thermocouple + logger** | Ice-point check and a comparison against the probe thermometer in a stirred water bath | Agreement within ± 2 °C |
| **Precision scale** | Check with a **known mass** at the working range | **Error ≤ 0.05 g** for batch work |
| **Anemometer** | Cross-check against a second anemometer, a vehicle-mounted reading, or a reliable local weather station on a calm and a windy day; or send for calibration | Agreement within ± 10% or ± 2 km/h, whichever is greater |
| **Altimeter** | Zero at the site's known elevation and compare against a surveyed or GPS altitude | Within the manufacturer's stated accuracy |
| **IMU / accelerometer** | Static six-face check; compare the magnitude of the gravity vector against 1 g on each axis | Within ± 2% of 1 g |
| **Multimeter** | Compare against a known voltage reference and a known resistance | Within the manufacturer's stated accuracy |
| **Continuity tester** | Verify the current limit with a series milliammeter into a dummy load | **Must be limited below 50 mA** — a continuity check that can fire the igniter is not a safety feature, it is a hazard |

### 3.4 Reference standards

**Every calibration references a standard.** Record which one, by ID or certificate number:

- **Known masses** — record the nominal mass, and note whether the mass set carries its own certificate
  or was verified on a calibrated balance.
- **Reference pressure gauge** — record the gauge ID, its range, its accuracy class, and its certificate
  number and expiry.
- **Deadweight tester** — record the instrument ID and its certificate number.
- **Proving ring** — record the certificate number and the expiry.
- **Ice point / boiling point** — record the method and the measured ambient pressure if using the
  boiling point.

**If the reference standard is out of date, the calibration it produced is void.** This is the failure
that catches people out: a perfectly performed calibration against an expired gauge is not a
calibration.

---

## 4. Calibration log

**One row per calibration event. Never overwrite a row — a re-calibration is a new row.** If an
instrument is re-calibrated, both rows stay, so the calibration history is visible.

| # | Instrument ID | Type | Serial no. | Calibration date | Method used | Reference standard (ID / certificate no.) | Result (slope, offset, R², max non-linearity, hysteresis) | Valid until | Performed by (name, or external lab) | Certificate filed | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | | ☐ | |
| 2 | | | | | | | | | | ☐ | |
| 3 | | | | | | | | | | ☐ | |
| 4 | | | | | | | | | | ☐ | |
| 5 | | | | | | | | | | ☐ | |
| 6 | | | | | | | | | | ☐ | |
| 7 | | | | | | | | | | ☐ | |
| 8 | | | | | | | | | | ☐ | |
| 9 | | | | | | | | | | ☐ | |
| 10 | | | | | | | | | | ☐ | |
| 11 | | | | | | | | | | ☐ | |
| 12 | | | | | | | | | | ☐ | |
| 13 | | | | | | | | | | ☐ | |
| 14 | | | | | | | | | | ☐ | |
| 15 | | | | | | | | | | ☐ | |
| 16 | | | | | | | | | | ☐ | |
| 17 | | | | | | | | | | ☐ | |
| 18 | | | | | | | | | | ☐ | |
| 19 | | | | | | | | | | ☐ | |
| 20 | | | | | | | | | | ☐ | |

**Column definitions:**

| Column | What goes in it |
|---|---|
| **Instrument ID** | The club's own label, e.g. `LC-001` (load cell), `PT-002` (pressure transducer), `TH-003`, `SC-001` (scale), `AN-001` (anemometer). **This ID is what goes on the field checklist.** |
| **Type** | Load cell, pressure transducer, reference gauge, IR thermometer, probe thermometer, thermocouple, scale, anemometer, altimeter, IMU, multimeter, continuity tester |
| **Serial no.** | The manufacturer's serial number, so a certificate can be matched to a physical unit |
| **Calibration date** | `YYYY-MM-DD` |
| **Method used** | Known masses / lever arm with ratio / reference gauge / deadweight tester / ice point / cross-check against a second instrument / external laboratory |
| **Reference standard** | The ID or certificate number of the standard used. **If this is blank, the calibration is void** |
| **Result** | The fitted slope and offset, the R², and the maximum non-linearity and hysteresis as percentages. For a simple check, the reading versus the reference |
| **Valid until** | `YYYY-MM-DD`. **Six months for a load cell or pressure transducer**, or the certificate's own expiry |
| **Performed by** | The club member's name, or the external laboratory's name and report number |
| **Certificate filed** | Whether the certificate is filed in `60_TEST_DATA/calibration/` |
| **Notes** | Anything that affects trust in the instrument: a drop, an over-range event, a repaired cable, a suspected thermal exposure |

---

## 5. Per-test calibration verification record

**Complete this block for every test.** The before-and-after values are what detect a sensor that
drifted or was damaged during the firing — and that is the difference between data you can use and data
you must throw away.

### Test: ______________________ Date: ______________________

| Instrument ID | Type | Before-test check value (applied / indicated) | Before drift (%) | After-test check value (applied / indicated) | After drift (%) | Drift within 2%? | Data valid? |
|---|---|---|---|---|---|---|---|
| | | ______ / ______ | ______ % | ______ / ______ | ______ % | ☐ Yes ☐ No | ☐ Yes ☐ **No** |
| | | ______ / ______ | ______ % | ______ / ______ | ______ % | ☐ Yes ☐ No | ☐ Yes ☐ **No** |
| | | ______ / ______ | ______ % | ______ / ______ | ______ % | ☐ Yes ☐ No | ☐ Yes ☐ **No** |
| | | ______ / ______ | ______ % | ______ / ______ | ______ % | ☐ Yes ☐ No | ☐ Yes ☐ **No** |

| Field | Entry |
|---|---|
| **Calibration record IDs referenced** | ______________________ ______________________ |
| **Calibration currency confirmed on the day** | ☐ Yes ☐ No |
| **Load cell sized so peak expected thrust was 50–80% of full scale?** | ☐ Yes ☐ No — peak expected ______ N of ______ N full scale |
| **Pressure transducer rated to ≥ 2× expected MEOP?** | ☐ Yes ☐ No — MEOP ______ bar, rating ______ bar |
| **Transducer thermal protection in place (standpipe / barrier / standoff)?** | ☐ Yes ☐ No |
| **Sample rate used** | ______ Hz (**≥ 100 Hz**) |
| **Any instrument fault or drift found?** | ☐ No ☐ Yes — describe: ______________________ |
| **Data marked unusable where an instrument failed?** | ☐ N/A ☐ Yes — affected channel: ______________________ |
| **Instrument removed from service and tagged?** | ☐ N/A ☐ Yes |

**Verified by (data operator):** ______________________ **Date:** __________

**Countersigned (Safety Officer):** ______________________ **Date:** __________

> **The raw data is never adjusted to compensate for a drift.** If the sensor drifted, **the data is
> invalid** — record that in the test report and fix the instrument. **Never "correct" a raw file.**

---

## 6. Instrument inventory

**Every instrument the club owns that appears in Section 1.** An instrument not on this list must not be
used to produce a test result.

| Instrument ID | Type | Make / model | Serial no. | Range | Accuracy / resolution | Location stored | In service? |
|---|---|---|---|---|---|---|---|
| | | | | | | | ☐ Yes ☐ No |
| | | | | | | | ☐ Yes ☐ No |
| | | | | | | | ☐ Yes ☐ No |
| | | | | | | | ☐ Yes ☐ No |
| | | | | | | | ☐ Yes ☐ No |
| | | | | | | | ☐ Yes ☐ No |
| | | | | | | | ☐ Yes ☐ No |
| | | | | | | | ☐ Yes ☐ No |
| | | | | | | | ☐ Yes ☐ No |
| | | | | | | | ☐ Yes ☐ No |
| | | | | | | | ☐ Yes ☐ No |
| | | | | | | | ☐ Yes ☐ No |

---

## 7. Calibration due-date watchlist

**Reviewed at every monthly club meeting and before every test campaign.** An instrument that is due
within 30 days must be booked in for calibration **before** the next test.

| Instrument ID | Type | Last calibrated | Valid until | Days remaining | Action required | Owner | Done |
|---|---|---|---|---|---|---|---|
| | | | | ______ | ☐ Book calibration ☐ Replace ☐ Retire | | ☐ |
| | | | | ______ | ☐ Book calibration ☐ Replace ☐ Retire | | ☐ |
| | | | | ______ | ☐ Book calibration ☐ Replace ☐ Retire | | ☐ |
| | | | | ______ | ☐ Book calibration ☐ Replace ☐ Retire | | ☐ |
| | | | | ______ | ☐ Book calibration ☐ Replace ☐ Retire | | ☐ |
| | | | | ______ | ☐ Book calibration ☐ Replace ☐ Retire | | ☐ |
| | | | | ______ | ☐ Book calibration ☐ Replace ☐ Retire | | ☐ |
| | | | | ______ | ☐ Book calibration ☐ Replace ☐ Retire | | ☐ |

**Overdue instruments:** ☐ None ☐ Present — instrument IDs: ______________________
**Overdue instruments tagged out of service?** ☐ Yes ☐ N/A

---

## 8. Records retention and filing

- **Calibration records are retained permanently** (`Safety_Manual_Master.md` §8.4). A grain cast in
  one year may be fired years later, and the instrument that measured it must still be traceable.
- **Certificates:** filed in `60_TEST_DATA/calibration/` as PDFs, named
  `CAL-<YYYY>-<###>_<YYYY-MM-DD>_<instrument-id>_certificate.pdf`.
- **Raw calibration data:** filed in `60_TEST_DATA/raw/calibration/` using the convention
  `CAL-<YYYY>-<###>_<YYYY-MM-DD>_calibration.csv`. **Raw calibration data is never edited** — see
  `60_TEST_DATA/README.md` §2.
- **The instrument ID used in this log is the same ID recorded on the field checklists** (`FORM-04`
  Phase A, `FORM-01` Section 6.1). That is how a published result is traced back to a calibration.
- **On an instrument's retirement or loss**, its rows stay in this log, with the retirement noted. **Do
  not delete the history.**

---

## 9. Quick reference

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│  AN UNCALIBRATED SENSOR MAKES THE DATA WORTHLESS FOR PERFORMANCE ANALYSIS.                 │
│                                                                                          │
│  LOAD CELL            Calibrate with KNOWN MASSES, or a LEVER ARM amplifying a known mass  │
│                       with the ratio documented. Verify immediately before AND after the   │
│                       test. Size so peak expected thrust is 50–80% of full scale.          │
│                                                                                          │
│  PRESSURE TRANSDUCER  Calibrate against a REFERENCE GAUGE or a deadweight tester.           │
│                       Rate to at least 2× expected MEOP. THERMAL PROTECTION IS MANDATORY.  │
│                       Sample at ≥ 100 Hz (1000 Hz preferred).                              │
│                                                                                          │
│  ANY OTHER INSTRUMENT Compare against a known reference or a second instrument.            │
│                                                                                          │
│  BEFORE THE TEST      Record the before-value.   AFTER THE TEST  Record the after-value.    │
│  DRIFT > 2%           The data is INVALID. Say so in the test report. Never adjust the raw  │
│                       file. Fix the instrument, not the numbers.                           │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

```
Calibration_Record  |  Rev 1.0  |  UVCE Rocketry Club Safety Officer  |  Retain PERMANENTLY
Companion to 60_TEST_DATA/README.md  |  Parent: 40_SAFETY/Static_Test_Procedure.md §3.3, §3.4, §7
```

*Total impulse is the area under the thrust-time curve. If the curve's vertical scale is wrong, every
number you derive from it is wrong with it.*
