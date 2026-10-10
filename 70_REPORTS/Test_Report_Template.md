# UVCE Rocketry Club — Test Report

```
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║  UVCE ROCKETRY CLUB — TEST REPORT                                                         ║
║  Template: Test_Report_Template.md  |  Rev 1.0  |  Issued: ____________                   ║
║                                                                                          ║
║  REQUIRED WITHIN 24 HOURS of a static fire (Static_Test_Procedure.md §8.3), and within a   ║
║  week of a flight day. Written while the detail is fresh, before the debrief fades.        ║
║                                                                                          ║
║  ⚠  THIS REPORT MUST COMPARE MEASURED PERFORMANCE AGAINST THE DESIGN PREDICTION AND        ║
║     EXPLAIN ANY DISCREPANCY. A report that presents numbers without the comparison is      ║
║     an unfinished report.                                                                  ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝
```

---

## 1. Test identification

| Field | Entry |
|---|---|
| **Test ID** | ______________________ e.g. `ST-003` / `FL-007` |
| **Report ID** | ______________________ e.g. `TR-2027-003` |
| **Revision** | ______________ |
| **Supersedes** | ______________________ or "—" |
| **Date of test** | ______________________ |
| **Time of test** | __________ hrs |
| **Report written on** | ______________________ at __________ hrs |
| **Time from the test to this report** | ______ hours ☐ Within 24 hours ☐ **Late — explain:** ______________________ |
| **Test type** | ☐ Static fire ☐ Flight ☐ Strand burner ☐ Hydrostatic proof test ☐ Component / coupon test ☐ Recovery ground test ☐ Other: ______________ |
| **Motor ID / serial** | ______________________ |
| **Rocket / airframe ID** | ______________________ ☐ N/A |
| **Test number on this motor / configuration** | ______ of ______ |
| **Location** | ______________________________________________ |
| **GPS coordinates** | Lat __________________ Long __________________ |
| **Test Director** | ______________________ |
| **Safety Officer** | ______________________ |
| **Report author** | ______________________ |
| **Related documents** | Test plan: ______________ · Checklist: ______________ · Data folder: ______________ · Prior test report: ______________ |

---

## 2. Objective

**What was this test meant to determine?** State it as a question with a measurable answer, written
**before** the test was run.

**Primary objective:**

______________________________________________________________________________

**Secondary objectives:**

1. ______________________________________________________________________________
2. ______________________________________________________________________________
3. ______________________________________________________________________________

**Hypothesis / expected outcome, stated in advance:**

| Quantity | Predicted value | Basis of the prediction |
|---|---|---|
| | | |
| | | |
| | | |

**Success criteria, stated in advance:**

| Criterion | Threshold | Pass? |
|---|---|---|
| | | ☐ Pass ☐ Fail |
| | | ☐ Pass ☐ Fail |
| | | ☐ Pass ☐ Fail |

> **A pass/fail rule written after the test is not a criterion.** If the criteria above were written
> after the test, say so here: ______________________

**Which single variable is this test changing relative to the previous test?**

______________________________________________________________________________

*(One test proves nothing. A repeatable design needs **3–5 identical motors with overlapping thrust
curves**, changing **one variable at a time**.)*

**Was the test completed as planned?** ☐ Yes ☐ No — describe: ______________________
**Misfire, abort, or early termination?** ☐ No ☐ Yes — reference: ______________________

---

## 3. Article under test

### 3.1 Configuration

| Field | Entry |
|---|---|
| **Motor designation** | ______________________ |
| **Configuration revision** | ______________ |
| **Case ID / serial** | ______________________ |
| **Case material and wall thickness** | ______________________ |
| **Case proof test date and pressure (new design)** | ______________________ / ______ bar (**1.2 × MEOP**) |
| **Case history** | ☐ New ☐ Previously fired ______ times ☐ Repaired/retested — reference: ______________ |
| **Case disposition after this test** | ☐ Serviceable ☐ **Retired** |
| **Nozzle ID** | ______________________ |
| **Nozzle material** | ______________________ |
| **Throat diameter before test** | ______ mm |
| **Throat diameter after test** | ______ mm **Erosion: ______ mm** |
| **Expansion ratio** | ______ |
| **Forward closure / head end** | ______________________ |
| **Retaining system** | ______________________ **Torque applied:** ______ N·m |
| **O-rings and seals (part numbers)** | ______________________ |
| **Liner / inhibitor** | ______________________ |
| **Total motor mass (dry / loaded)** | ______ g / ______ g |
| **Number of grains / segments** | ______ |
| **Inter-segment spacing** | ______ mm |
| **Port-to-throat area ratio at start of burn** | ______ (**must be ≥ 2**) |

### 3.2 Propellant

| Field | Entry |
|---|---|
| **Formulation** | **KNSB — 65% KNO₃ / 35% sorbitol by mass** |
| **Batch ID** | ______________________ |
| **Grain ID(s) installed** | ______________________ |
| **Date cast** | ______________________ |
| **Date fired (age of grain)** | ______________________ (______ days) |
| **Grain mass** | ______ g |
| **Grain dimensions (L × OD × core)** | ______ × ______ × ______ mm |
| **Actual measured ratio (KNO₃ : sorbitol)** | ______ : ______ |
| **Density ratio (actual ÷ ideal 1.841 g/cm³)** | **______** |
| **Density band (per FORM-03)** | ☐ A (≥ 0.95) ☐ B (0.90–0.95) ☐ C (below 0.90, external bubble — repaired) ☐ D (below 0.90, no visible flaw) |
| **Coin tap test result** | ☐ Pass ☐ Fail — **performed after full cure?** ☐ Yes ☐ No |
| **Tap test notes (batch comparison)** | ______________________ |
| **External defects** | ☐ None ☐ Repaired external bubble ☐ Other: ______________ |
| **Residual grease film cleaned off (acetone / lacquer thinner)?** | ☐ Yes ☐ No |
| **Primer coat** | ☐ None — **fired unprimed (current default)** ☐ Thin primer applied: ______________ ☐ **Heavy coat — prohibited** |
| **Storage before test** | ______________________ duration: ______ |
| **Grain inspection before installation** | ☐ No cracks ☐ No chips ☐ No discolouration ☐ Not soft or tacky |
| **Was the grain dropped at any point?** | ☐ No ☐ **Yes — the grain must have been scrapped** |

### 3.3 Igniter

| Field | Entry |
|---|---|
| **Igniter type** | ______________________ |
| **Charge mass** | ______ g |
| **Construction** | ______________________ |
| **Positioned to ignite the core and forward end face?** | ☐ Verified |
| **Verified it cannot plug the throat?** | ☐ Verified |
| **Was the igniter sized to the motor?** | ☐ Yes — basis: ______________ ☐ No |
| **Leads shunted until the moment of connection?** | ☐ Yes ☐ No |

### 3.4 Airframe and recovery *(flight tests only)*

| Field | Entry |
|---|---|
| **Airframe ID and club marking** | ______________________ |
| **Total liftoff mass** | ______ g |
| **Centre of gravity / centre of pressure** | ______ / ______ **Stability: ______ calibres** |
| **Fins (material, span, root chord)** | ______________________ |
| **Recovery system** | ______________________ **Descent rate predicted: ______ m/s** |
| **Ejection method and timing** | ______________________ |
| **Avionics / altimeter** | ______________________ |
| **Recovery system packed and verified?** | ☐ Yes ☐ No ☐ First flight of this design |
| **Launch angle** | ______ ° from horizontal ☐ Locked ☐ Verified |
| **Pad and rod/rail** | ______________________ |

### 3.5 Deviations from the reviewed design

> **No undocumented changes.** Every departure from the design reviewed at the CDR must be listed here,
> with its authorisation.

| # | Deviation from design | Reason | Authorised by | Reference | Expected effect |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

**Was the article tested the article that was analysed and reviewed?** ☐ **Yes** ☐ **No — this
invalidates the test as a verification of the design. Explain:** ______________________

---

## 4. Instrumentation and calibration validity

> **An uncalibrated sensor makes the data worthless for performance analysis.** Every instrument used
> must be traceable to a calibration record that was **valid on the day of the test**.

| # | Instrument ID | Type | Serial no. | Range | Sample rate | Calibration record ID | Calibrated on | Valid until | Valid on test day? |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | Load cell | | | ______ Hz | | | | ☐ Yes ☐ No |
| 2 | | Pressure transducer | | | ______ Hz | | | | ☐ Yes ☐ No |
| 3 | | Thermocouple | | | ______ Hz | | | | ☐ Yes ☐ No |
| 4 | | Anemometer | | | — | | | | ☐ Yes ☐ No |
| 5 | | Thermometer | | | — | | | | ☐ Yes ☐ No |
| 6 | | Altimeter | | | ______ Hz | | | | ☐ Yes ☐ No |
| 7 | | IMU / accelerometer | | | ______ Hz | | | | ☐ Yes ☐ No |
| 8 | | Camera (side-on) | | | ______ fps | — | — | — | ☐ N/A |
| 9 | | Camera (wide) | | | ______ fps | — | — | — | ☐ N/A |
| 10 | | Audio recorder | | | — | — | — | — | ☐ N/A |

### 4.1 Calibration checks on the day

| Instrument | Before-test check (applied / indicated) | Before drift | After-test check (applied / indicated) | After drift | Within 2%? | Data valid? |
|---|---|---|---|---|---|---|
| Load cell | ______ / ______ | ______ % | ______ / ______ | ______ % | ☐ Yes ☐ No | ☐ Yes ☐ **No** |
| Pressure transducer | ______ / ______ | ______ % | ______ / ______ | ______ % | ☐ Yes ☐ No | ☐ Yes ☐ **No** |
| | ______ / ______ | ______ % | ______ / ______ | ______ % | ☐ Yes ☐ No | ☐ Yes ☐ **No** |

| Field | Entry |
|---|---|
| **Load cell sized so peak expected thrust was 50–80% of full scale?** | ☐ Yes ☐ No — peak expected ______ N of ______ N full scale |
| **Pressure transducer rated to ≥ 2× expected MEOP?** | ☐ Yes ☐ No — MEOP ______ bar, rating ______ bar |
| **Transducer thermal protection** | ☐ Grease-filled standpipe ☐ Thermal barrier ☐ Standoff tube ☐ **NONE — this is a finding** |
| **Load cell mounting** | ☐ In line with the thrust axis ☐ Lever arm — **ratio ______, documented and accounted for in the calibration** |
| **Sample rate meets the requirement?** | ☐ Yes (**≥ 100 Hz; 1000 Hz preferred**) ☐ No |
| **Data logging redundancy** | ☐ Micro-SD logging ☐ Live laptop display ☐ **Both** ☐ **One only — a single failed link loses the entire test** |
| **Sync marker method** | ☐ Clap ☐ Torch flash ☐ Electrical pulse |
| **Sync marker captured in both video and data?** | ☐ Yes ☐ No — **data you cannot align in time is data you cannot interpret** |
| **Side-on camera used?** | ☐ Yes ☐ **No — this is a finding** |
| **Camera framing verified before arming?** | ☐ Yes ☐ No |
| **Any instrument fault found?** | ☐ No ☐ Yes: ______________________ |
| **Data marked unusable where an instrument failed?** | ☐ N/A ☐ Yes — channel: ______________ |

---

## 5. Procedure reference

| Field | Entry |
|---|---|
| **Procedure followed** | ☐ `Static_Test_Procedure.md` ☐ `Flight_Operations_Safety.md` ☐ `Propellant_Handling_SOP.md` ☐ Other: ______________ |
| **Procedure revision** | ______________ |
| **Phases completed** | Static fire: ☐ A Setup ☐ B Arming prep ☐ C Final arming ☐ D Countdown ☐ E Immediately after ☐ F Post-fire · Flight: ☐ Before departure ☐ On arrival ☐ Per flight ☐ Before leaving |
| **Completed field checklist** | ☐ `FORM-04` (static test) ☐ `FORM-05` (flight day) ☐ `FORM-01` (pre-session) |
| **Checklist reference / file** | ______________________ |
| **Was every checklist item signed?** | ☐ Yes ☐ No — unsigned items: ______________ **Any unsigned item is a NO-GO** |
| **Was the pre-session sign-off signed by all three signatories?** | ☐ Yes ☐ No |
| **Was any step skipped, repeated, or reordered?** | ☐ No ☐ Yes — describe: ______________________ |
| **Was any abort, hold, or stop-work called?** | ☐ No ☐ Yes — by whom: ______________ at which step: ______________ reason: ______________ |
| **Was the misfire procedure invoked?** | ☐ No ☐ Yes — reference: ______________ |
| **Any incident or near miss?** | ☐ None ☐ Yes — **`FORM-06` reference:** ______________ |
| **Personnel present and their roles** | TD: ______________ · SO: ______________ · RS: ______________ · Data operator: ______________ · Documentarian: ______________ · Observers: ______________ |

> **The motor is the motor that was analysed.** A test of a different configuration verifies nothing
> about the reviewed design.

---

## 6. Environmental conditions

| Parameter | Value | Limit / note | Verdict |
|---|---|---|---|
| **Date and time** | ______________________ at __________ | — | |
| **Ambient temperature** | ______ °C | Above 38 °C: reassess heat stress | ☐ Noted |
| **Humidity** | ______ % RH | Above 70 % RH degrades KNSB | ☐ Noted |
| **Barometric pressure** | ______ mbar | — | |
| **Wind — sustained** | ______ km/h | Static: **> 20 NO-GO** · Flight: **> 32 NO-GO** | ☐ GO ☐ NO-GO |
| **Wind — gusts** | ______ km/h | Static: **> 25 NO-GO** · Flight: **> sustained + 10 NO-GO** | ☐ GO ☐ NO-GO |
| **Wind direction** | ______ ° from ______________ | Drift must be into the clear area | ☐ GO ☐ NO-GO |
| **Measured with an anemometer?** | ☐ Yes ☐ **No — guessed winds are not measurements** | — | |
| **Sky / cloud** | ______________________ | — | |
| **Cloud ceiling** | ______ m | Flight: must exceed expected apogee by **≥ 2×** | ☐ GO ☐ NO-GO |
| **Precipitation** | ☐ None ☐ Rain | **Any rain = NO-GO** | ☐ GO ☐ NO-GO |
| **Lightning within 10 km** | ☐ None ☐ Present | **Any = NO-GO** | ☐ GO ☐ NO-GO |
| **Visibility of the pad from the firing point** | ☐ Clear ☐ Insufficient | **Insufficient = NO-GO** | ☐ GO ☐ NO-GO |
| **Remaining daylight** | ______ minutes | **< 90 minutes = NO-GO** | ☐ GO ☐ NO-GO |
| **Vegetation condition** | ☐ Green / mown / bare ☐ Dry and uncontrolled | **Dry and uncontrolled = NO-GO** without a fire watch | ☐ GO ☐ NO-GO |
| **Ground condition** | ☐ Dry ☐ Wet | **Wet = NO-GO** | ☐ GO ☐ NO-GO |
| **Personnel distance from the motor** | ______ m | **75–100 m proven; 150 m or more for a new design** | ☐ Met ☐ Not met |
| **Hard cover at the firing point?** | ☐ Yes ☐ No — **a person in the open at 100 m is less safe than a person behind a berm at 50 m** | — | |
| **Fire cover** | ☐ Bulk water at the pad ☐ Extinguisher at pad ☐ Extinguisher at firing point ☐ Dunk bucket | — | ☐ Complete |

**Assessed by (Range Safety):** ______________________ **Time:** __________

---

## 7. Results

### 7.1 Summary of measured performance

| Quantity | Measured value | Units | Source data file |
|---|---|---|---|
| **Peak thrust** | ______ | N | ______________________ |
| **Mean thrust (burn duration)** | ______ | N | ______________________ |
| **Peak chamber pressure** | ______ | bar | ______________________ |
| **Mean chamber pressure** | ______ | bar | ______________________ |
| **Burn time** | ______ | s | ______________________ |
| **Ignition delay after the fire command** | ______ | s | ______________________ |
| **Total impulse (area under the thrust-time curve)** | ______ | N·s | ______________________ |
| **Propellant mass consumed** | ______ | g | ______________________ |
| **Delivered Isp = I ÷ (m_p × g)** | ______ | s | ______________________ |
| **Characteristic velocity c\*** *(if computed)* | ______ | m/s | ______________________ |
| **Nozzle throat erosion** | ______ | mm | FORM-04 §9.1 |
| **Apogee** *(flight)* | ______ | m | ______________________ |
| **Descent rate** *(flight)* | ______ | m/s | ______________________ |
| **Drift distance** *(flight)* | ______ | m | ______________________ |

**Data files referenced (list every file this report relies on):**

| # | File path | Description | Integrity checked? |
|---|---|---|---|
| 1 | `60_TEST_DATA/raw/…` | Thrust-time data | ☐ Yes |
| 2 | `60_TEST_DATA/raw/…` | Pressure-time data | ☐ Yes |
| 3 | `60_TEST_DATA/raw/…` | Side-on video | ☐ Yes |
| 4 | `60_TEST_DATA/raw/…` | Wide-framing video | ☐ Yes |
| 5 | `60_TEST_DATA/raw/…` | Audio | ☐ Yes |
| 6 | `60_TEST_DATA/processed/…` | Analysis notebook / reduced results | ☐ Yes |

> **Raw data is never edited.** Every derived figure in this report must be reproducible from the raw
> files plus the analysis notebook named above.

### 7.2 Data plots

**Every plot references its data file and the analysis that produced it. Every axis has a unit.**

| Figure | Description | Data file | Axes | Notes |
|---|---|---|---|---|
| **Figure 1** | Thrust vs time | ______________________ | Time (s) vs Thrust (N) | |
| **Figure 2** | Chamber pressure vs time | ______________________ | Time (s) vs Pressure (bar) | |
| **Figure 3** | Thrust and pressure on a **common time base** | ______________________ | Time (s) vs Thrust (N) / Pressure (bar) | **Required — a pressure trace and a thrust trace on different time bases cannot be compared** |
| **Figure 4** | Total impulse accumulation vs time | ______________________ | Time (s) vs Impulse (N·s) | Area under the thrust curve |
| **Figure 5** | Predicted vs measured thrust | ______________________ | Time (s) vs Thrust (N), two series | See §8 |
| **Figure 6** | Predicted vs measured pressure | ______________________ | Time (s) vs Pressure (bar), two series | See §8 |
| **Figure 7** | Video frame strip — ignition transient | ______________________ | — | Frames at ______ ms intervals |
| **Figure 8** | Video frame strip — burn and tail-off | ______________________ | — | |
| **Figure 9** | Post-test hardware photographs | ______________________ | — | Case, nozzle, grain remnants, O-rings, liner |
| **Figure 10** | Altitude vs time *(flight)* | ______________________ | Time (s) vs Altitude (m) | |

**Figure files stored at:** ______________________

### 7.3 Pressure curve shape

**The chamber pressure trace is the single most diagnostic measurement in the entire test.** Describe
its shape and what it indicates.

| Shape observed | Indicates | Observed? |
|---|---|---|
| **Flat / neutral** | Nominal, uniform burning | ☐ |
| **Mountain-shaped (rise then fall)** | **Delayed end-face ignition** — characteristic of KNSB | ☐ |
| **Spike at ignition** | **Oversized igniter** — a startup spike can shear retaining bolts and burst the case | ☐ |
| **Slow rise** | Reluctant start | ☐ |
| **Rapid rise to failure** | The last thing the sensor ever records — it tells us what to change | ☐ |
| **Plateau or step** | Channelling, crack, or inhibitor disbonding | ☐ |
| **Tail-off characteristics** | Sliver burning, unburned propellant remaining | ☐ |

**Description of the pressure trace:**

______________________________________________________________________________
______________________________________________________________________________

**Cross-check against the grain remnants:** *(a mountain-shaped KNSB curve comes from delayed end-face
ignition — check the grain remnants for confirmation)*

______________________________________________________________________________

### 7.4 Post-test inspection findings

**Photograph everything before disturbing it.** Once a component is removed, the evidence of how it
failed is gone.

| Item | What was looked for | Finding | Verdict |
|---|---|---|---|
| **Case exterior** | Bulging, ovality, discolouration, cracking, paint loss | | ☐ Serviceable ☐ **Retired — any permanent deformation retires the case** |
| **Case interior** | Erosion, charring, heat damage, liner condition | | |
| **Head end / forward closure** | Blow-by, seal damage, thread condition, deformation | | |
| **Nozzle** | Throat diameter (measured), erosion pattern, cracking, wear | | |
| **O-rings and seals** | Compression set, cuts, burning, hardening | | |
| **Grain remnants** | Sliver shape, unburned propellant, cracks, channelling, end-face ignition pattern | | |
| **Inhibitor** | Disbonding, burning behind the inhibitor, charring | | |
| **Igniter** | Position, consumption, residue in the throat | | |
| **Thrust stand** | Movement, deformation, fasteners loosened, deflector condition | | ☐ Data valid ☐ **Data invalidated by stand movement** |
| **Airframe and fins** *(flight)* | Heat damage, cracking, deformation | | |
| **Recovery system** *(flight)* | Deployment, damage, packing evidence | | |

**Was the thrust stand found to have moved?** ☐ No ☐ **Yes — the thrust data is a measurement of the
stand, not the motor. State the effect on the results:** ______________________

**Retired components:** ______________________________________________

**Reusable components and their condition:** ______________________________________________

---

## 8. Comparison against prediction

> ## THIS SECTION IS MANDATORY.
> **The report compares measured performance against the design prediction and explains any
> discrepancy.** A report that presents numbers without the comparison is an unfinished report — and a
> discrepancy that is rationalised instead of investigated is a **disqualified test**
> (`Safety_Manual_Master.md` §2.5).

### 8.1 Predicted versus measured

| Quantity | Predicted | Measured | Difference (absolute) | Difference (%) | Within prediction uncertainty? | Explained? |
|---|---|---|---|---|---|---|
| **Peak thrust (N)** | ______ | ______ | ______ | ______ % | ☐ Yes ☐ No | ☐ Yes ☐ No |
| **Mean thrust (N)** | ______ | ______ | ______ | ______ % | ☐ Yes ☐ No | ☐ Yes ☐ No |
| **Burn time (s)** | ______ | ______ | ______ | ______ % | ☐ Yes ☐ No | ☐ Yes ☐ No |
| **Total impulse (N·s)** | ______ | ______ | ______ | ______ % | ☐ Yes ☐ No | ☐ Yes ☐ No |
| **Peak pressure (bar)** | ______ | ______ | ______ | ______ % | ☐ Yes ☐ No | ☐ Yes ☐ No |
| **Mean pressure (bar)** | ______ | ______ | ______ | ______ % | ☐ Yes ☐ No | ☐ Yes ☐ No |
| **Delivered Isp (s)** | ______ | ______ | ______ | ______ % | ☐ Yes ☐ No | ☐ Yes ☐ No |
| **Ignition delay (s)** | ______ | ______ | ______ | ______ % | ☐ Yes ☐ No | ☐ Yes ☐ No |
| **Propellant mass consumed (g)** | ______ | ______ | ______ | ______ % | ☐ Yes ☐ No | ☐ Yes ☐ No |
| **Apogee (m)** *(flight)* | ______ | ______ | ______ | ______ % | ☐ Yes ☐ No | ☐ Yes ☐ No |
| **Descent rate (m/s)** *(flight)* | ______ | ______ | ______ | ______ % | ☐ Yes ☐ No | ☐ Yes ☐ No |

**Prediction source:** ☐ `70_REPORTS/design_reviews/…` reference: ______________
☐ Strand burner data reference: ______________
☐ Simulation reference: ______________

### 8.2 Curve comparison — the shape, not just the numbers

**Overlay the predicted and measured thrust curves on a common time base, and do the same for
pressure. Describe the differences in shape, not only in magnitude.**

| Feature | Predicted | Measured | Difference and likely cause |
|---|---|---|---|
| **Ignition transient** | | | |
| **Rise to peak** | | | |
| **Peak location in time** | | | |
| **Plateau / steady region** | | | |
| **Tail-off** | | | |
| **Total burn duration** | | | |
| **Pressure curve shape** (mountain / flat / spiked) | | | |

### 8.3 Explanation of every discrepancy

**For each quantity outside the prediction uncertainty, give a hypothesis and the evidence for it.**
"Within measurement error" is acceptable **only** where the difference actually is within the stated
uncertainty — say what that uncertainty is.

| # | Discrepancy | Magnitude | Hypothesis | Supporting evidence | Confidence (L/M/H) | How to test the hypothesis next |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |

### 8.4 Measurement uncertainty

**State the uncertainty on every headline number, so the comparison is honest.**

| Source of uncertainty | Magnitude | Effect on the measurement |
|---|---|---|
| Load cell calibration | ± ______ % | Thrust, impulse, Isp |
| Load cell zero drift | ± ______ N | Thrust |
| Pressure transducer calibration | ± ______ % | Pressure, burn time |
| Sample rate / timing | ± ______ ms | Burn time, ignition delay |
| Propellant mass measurement | ± ______ g | Isp, c\* |
| Grain density ratio | ± ______ | Burn rate, pressure |
| Stand compliance / movement | ______ | **Thrust — potentially dominant** |
| Environmental (temperature, humidity) | ______ | Burn rate |
| **Combined uncertainty on total impulse** | **± ______ %** | |

### 8.5 The honest answer

**Did this test meet its objective?** ☐ Yes ☐ Partially ☐ No

**Why or why not:**

______________________________________________________________________________

**Was any anomaly rationalised rather than investigated?** ☐ No ☐ **Yes — the test is disqualified and
must be re-run after investigation**

---

## 9. Anomalies observed

**An anomaly is anything unexpected. Every anomaly is recorded, whether or not it is understood.**

| # | Anomaly | When it occurred | Observable evidence | Suspected cause | Investigated? | Outcome |
|---|---|---|---|---|---|---|
| 1 | | | | | ☐ Yes ☐ No | |
| 2 | | | | | ☐ Yes ☐ No | |
| 3 | | | | | ☐ Yes ☐ No | |
| 4 | | | | | ☐ Yes ☐ No | |
| 5 | | | | | ☐ Yes ☐ No | |

**Anomaly types observed:**

- [ ] Off-nominal pressure curve (spike, plateau, tail-off, unexpected duration)
- [ ] Early or late ignition
- [ ] Unexpected nozzle erosion
- [ ] Grain defect found after the fact
- [ ] Case deformation or discolouration
- [ ] Seal blow-by or gas leakage
- [ ] Inhibitor disbonding
- [ ] Thrust stand movement
- [ ] Instrument dropout, saturation, or drift
- [ ] Video or data capture failure
- [ ] Recovery anomaly (premature, late, or no deployment)
- [ ] Unexpected drift or landing point
- [ ] Other: ______________________

### 9.1 Near misses at this test

> **Near misses are the most valuable data the club has.** Recording one is not an admission of failure;
> it is the accident the club did not have.

| # | Near miss | What could have happened | Reported on `FORM-06`? |
|---|---|---|---|
| 1 | | | ☐ Yes ☐ No |
| 2 | | | ☐ Yes ☐ No |
| 3 | | | ☐ Yes ☐ No |

**Any incident?** ☐ None ☐ Yes — **`FORM-06` reference:** ______________

**Any equipment defect found?** ☐ None ☐ Yes — equipment removed from service and tagged? ☐ Yes ☐ N/A

---

## 10. Conclusions

### 10.1 What this test established

**State the conclusions that the data supports — and only those.** Distinguish what was **measured** from
what is **inferred**.

| # | Conclusion | Confidence | Basis (data / analysis) |
|---|---|---|---|
| 1 | | ☐ High ☐ Medium ☐ Low | |
| 2 | | ☐ High ☐ Medium ☐ Low | |
| 3 | | ☐ High ☐ Medium ☐ Low | |
| 4 | | ☐ High ☐ Medium ☐ Low | |

### 10.2 What this test did NOT establish

**Explicitly state the limits of what was learned.** A single test does not demonstrate repeatability,
does not characterise a burn rate, and does not validate a design on its own.

______________________________________________________________________________
______________________________________________________________________________

### 10.3 Design impact

| Field | Entry |
|---|---|
| **Does this test validate the reviewed design?** | ☐ Yes ☐ Partially ☐ No |
| **Does any margin need to be revised?** | ☐ No ☐ Yes — which: ______________ |
| **Does any requirement status change?** | ☐ No ☐ Yes — which: ______________ |
| **Does the CDR need to be re-opened?** | ☐ No ☐ Yes |
| **Does the design change as a result?** | ☐ No ☐ Yes — describe: ______________ |
| **Does any procedure or form change as a result?** | ☐ No ☐ Yes — which: ______________ |

### 10.4 The next action — the single variable

> **Change one variable at a time between tests.** State explicitly what will change next, and why.

**The single variable that will change in the next test:**

______________________________________________________________________________

**Why that variable, and what the next test is expected to show:**

______________________________________________________________________________

**Repeatability status:**

| Field | Entry |
|---|---|
| **Identical firings of this configuration to date** | ______ |
| **Required for a repeatable design** | **3–5 identical motors with overlapping thrust curves** |
| **Are the thrust curves overlapping so far?** | ☐ Yes ☐ No ☐ Not yet enough data |
| **If not repeatable, what is the working hypothesis?** | ______________________ |

### 10.5 Next test planned

| Field | Entry |
|---|---|
| **Next test ID** | ______________________ |
| **Planned date** | ______________________ |
| **Objective** | ______________________ |
| **Variable to be changed** | ______________________ |
| **Design review required first?** | ☐ No ☐ Yes — **nothing gets built without a passed design review** |

---

## 11. Lessons learned

**What should the next team know that this report has not already said?** Write these so they are useful
to someone who was not there — including the things that went right, and the things that nearly went
wrong.

### 11.1 Technical lessons

| # | Lesson | Evidence | Action taken / recommended |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

### 11.2 Procedural and safety lessons

| # | Lesson | Evidence | Document to change | Owner |
|---|---|---|---|---|
| 1 | | | ☐ Safety_Manual_Master ☐ Propellant_Handling_SOP ☐ Static_Test_Procedure ☐ Flight_Operations_Safety ☐ FORM-______ | |
| 2 | | | ☐ Safety_Manual_Master ☐ Propellant_Handling_SOP ☐ Static_Test_Procedure ☐ Flight_Operations_Safety ☐ FORM-______ | |
| 3 | | | ☐ Safety_Manual_Master ☐ Propellant_Handling_SOP ☐ Static_Test_Procedure ☐ Flight_Operations_Safety ☐ FORM-______ | |

### 11.3 What went well

**Record this too.** A technique that worked, a check that caught something, an instrument setup that
gave clean data — these are as valuable as the problems.

______________________________________________________________________________
______________________________________________________________________________

### 11.4 What we would do differently

______________________________________________________________________________
______________________________________________________________________________

---

## 12. Sign-off

### 12.1 Report completeness check

- [ ] Test identification complete, with the batch and grain IDs
- [ ] Objective stated, with success criteria written in advance
- [ ] Article under test described, with configuration and batch ID
- [ ] **Instrumentation listed, with calibration validity for every instrument**
- [ ] Before-and-after calibration values recorded
- [ ] Procedure and revision referenced, with the completed field checklist attached
- [ ] Environmental conditions recorded
- [ ] Results presented, **each referenced to its raw data file**
- [ ] **Thrust and pressure plotted on a common time base**
- [ ] Post-test inspection findings recorded, component by component
- [ ] **Measured performance compared against the design prediction**
- [ ] **Every discrepancy explained, with a hypothesis and evidence**
- [ ] Measurement uncertainty stated
- [ ] Anomalies and near misses recorded
- [ ] Conclusions stated, with their limits
- [ ] **The single next variable stated**
- [ ] Lessons learned recorded
- [ ] Raw data backed up — **two copies, two devices**
- [ ] Data filed in `60_TEST_DATA/` and the test log workbook row completed
- [ ] `FORM-06` filed for any incident, near miss, or anomaly requiring it

### 12.2 Approval signatures

| Role | Name (print) | Signature | Date |
|---|---|---|---|
| **Test Director** — owns the test plan, the countdown, and the data | ______________________ | ______________________ | __________ |
| **Safety Officer** — owns the go/no-go and the safety record | ______________________ | ______________________ | __________ |
| **Data operator** — confirms the results match the raw data | ______________________ | ______________________ | __________ |
| **Design lead** — confirms the comparison against the design prediction | ______________________ | ______________________ | __________ |
| **Faculty advisor** (where the report makes a design claim affecting the CDR) | ______________________ | ______________________ | __________ |

**Report filed at:** `70_REPORTS/test_reports/______________________`
**Filed on:** ______________________ **Revision:** ______________

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│  ONE TEST PROVES NOTHING.                                                                 │
│                                                                                          │
│  You need 3–5 IDENTICAL MOTORS WITH OVERLAPPING THRUST CURVES before you have a            │
│  repeatable design. Change ONE VARIABLE AT A TIME between tests.                           │
│                                                                                          │
│  Anomalies are INVESTIGATED, never rationalised. A discrepancy that is explained away is   │
│  a test that has been disqualified.                                                        │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

```
Test_Report_Template  |  Rev 1.0  |  UVCE Rocketry Club  |  Retain PERMANENTLY
Parent: 70_REPORTS/README.md §5  |  Static fire report due WITHIN 24 HOURS
```

*The motor is expendable. The data is valuable. The people are irreplaceable. Act accordingly.*
