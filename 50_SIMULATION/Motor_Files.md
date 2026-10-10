# Motor Files — Creating and Managing Motor Definitions

**UVCE Rocketry Club, Bengaluru — Simulation Guide 2 of 3**

Companion documents:
[OpenRocket_Workflow.md](OpenRocket_Workflow.md) (how to use the simulator) ·
[Simulation_Plan_and_Validation.md](Simulation_Plan_and_Validation.md) (error sources and validation)

**Purpose:** a club member should be able to take a static-fire CSV from the load-cell test
stand and turn it into a motor file that OpenRocket reads correctly, and to explain every
field and every number in that file to a reviewer.

---

## 1. Why the club needs its own motor files

OpenRocket ships with a database of commercial motors. It does not contain:

- our 24 mm KNSB motors,
- our 38 mm KN/sugar or KN/dextrose motors,
- the "same" commercial motor made by a different manufacturer with a different grain
  geometry,
- anything measured on our own test stand.

If you simulate a club rocket with a "similar" commercial motor you are simulating a
different rocket, and the error goes straight into the apogee, the delay choice and the
landing area.

**Three ways to get a motor into OpenRocket**

| Method | Format | When to use |
|---|---|---|
| Import a file | `.eng` (RASP, plain text) | Default for sharing, and what most tools export |
| Import a file | `.rse` (XML, RockSim) | Our own motors — units are unambiguous, so it is safer |
| Type it in | OpenRocket's motor editor | Quick order-of-magnitude work only |

---

## 2. Units and conventions — read this before writing any file

| Quantity | Unit used in `.eng` | Unit used in `.rse` |
|---|---|---|
| Time | seconds | seconds |
| Thrust | newtons | newtons |
| Diameter | millimetres | millimetres |
| Length | millimetres | millimetres |
| Propellant mass | **grams or kilograms — ambiguous!** | grams |
| Total (loaded) mass | **grams or kilograms — ambiguous!** | grams |
| Delay times | seconds | seconds |

The mass ambiguity in `.eng` is real and it is the single most dangerous thing in this
document. Files in circulation use both conventions for the same two fields. A file that
should say `20.0 68.0` (grams) may be written `0.020 0.068` (kilograms) by another tool, and
the importer has to guess.

**The only defence is verification.** After importing any motor file, open it in
OpenRocket and read back the reported **propellant mass**, **total mass**, **total impulse**
and **average thrust**. If any of them is off by a factor of 1000, or by any factor you
cannot explain, fix the file before you simulate.

> **Club rule 1:** in our own `.eng` files, masses are written in **grams** and the file
> carries a comment line stating the units.
>
> **Club rule 2:** the numbers that come out of OpenRocket are compared against the numbers
> in the file's comment block, every time. Measured, not assumed.
>
> **Club rule 3:** prefer `.rse` for our own motors. XML attributes say what they are.

Other conventions worth knowing:

- **Decimal separator:** always a **period** (`.`), never a comma. A file written on a
  machine with a comma-decimal locale will not import.
- **Encoding:** plain ASCII/UTF-8 without a byte-order mark. Use Notepad, VS Code, or
  TextEdit in **Format → Make Plain Text**. **Never** use Word or Google Docs — they add
  formatting and smart quotes.
- **Line endings:** Unix (LF) or Windows (CRLF) both work.
- **File extension:** `.eng` for RASP, `.rse` for XML. The extension matters — OpenRocket
  decides how to parse based on it.
- **One motor per file.** Not a hard requirement of every tool, but it is the only way to
  keep a library sane.
- **Never edit a certified commercial motor's data.** If you want a variant, create a new
  motor under the club's manufacturer name.

---

## 3. The RASP `.eng` format, line by line

A `.eng` file has exactly two parts: a header line and a thrust data block. Everything else
is comments.

### 3.1 Fully commented example

Every line below is explained in the comment above it. This is the club's standard 24 mm
KNSB motor — the same motor as in [OpenRocket_Workflow.md](OpenRocket_Workflow.md) §6.
Save as `50_SIMULATION/motors/E19KNSB.eng`.

```
; ==================================================================
; UVCE Rocketry Club - motor definition file (RASP .eng format)
; Motor   : E19KNSB  (24 mm KNSB, club-manufactured)
; File    : E19KNSB.eng        Revision: 2025-03-a
; Source  : static fire SF-2025-03-02, 10 kg load cell, 1 kHz
; Grain   : KNSB 65/35, 20.0 g, 24 mm OD, 9 mm core, 30 mm long
; Measured: Itot 24.6 N.s | Favg 19.0 N | Fpeak 22.5 N | burn 1.30 s
; Isp     : 126 s (sanity check: KNSB should land between 100 and 130 s)
; MASSES IN THIS FILE ARE IN GRAMS
;
; --- lines beginning with ';' are comments; blank lines are ignored ---
;
; --- header line: the ONLY line that is not a comment or data ---
; field 1: designation / motor name. No spaces. Convention is class letter
;          + average thrust, e.g. "E19". We append KNSB to make it unique.
; field 2: outer diameter of the motor in millimetres (must match the
;          motor mount tube in the design).
; field 3: overall length of the motor in millimetres (casing included).
; field 4: available ejection delays in seconds, separated by hyphens,
;          e.g. "4-6-8". "P" means plugged (no ejection charge) - use
;          electronic deployment. If your toolchain rejects "P", use "0".
; field 5: propellant mass in GRAMS (from weighing the grain).
; field 6: total loaded motor mass in GRAMS (case + nozzle + propellant +
;          hardware, weighed before the static fire).
; field 7: manufacturer. May contain spaces (it is the last field).
; -------------------------------------------------------------------
E19KNSB  24  100  P  20.0  68.0  UVCE Rocketry
; -------------------------------------------------------------------
; --- thrust data block: "<time> <thrust>" pairs, one per line ---
; time   in seconds, starting at 0.0, strictly increasing
; thrust in newtons
; The LAST point must exist and must have zero thrust, otherwise the
; simulator believes the motor is still burning at the end of the file.
; -------------------------------------------------------------------
0.00   0.0
0.04   6.0
0.08   14.0
0.15   19.0
0.30   21.0
0.50   22.0
0.70   22.5
0.90   22.5
1.05   21.0
1.15   18.0
1.22   11.0
1.28   4.0
1.30   0.0
; ===================== end of file ================================
```

### 3.2 Field-by-field reference

| Field | Position | Units | Rules and traps |
|---|---|---|---|
| Designation | 1 | text | No spaces. Standard form is class letter + average thrust (`E19`). OpenRocket sorts and filters on this. Make variants unique (`E19KNSB`, `E19KNSB-b`) so a simulation record can be traced to one file |
| Diameter | 2 | mm | Must equal the motor's outer diameter. If it is larger than the motor mount's inner diameter, the design is unbuildable and the simulator will not warn you |
| Length | 3 | mm | Casing length including the nozzle and forward closure. Affects where the motor's mass sits, and hence CG |
| Delays | 4 | s or `P` | Hyphen-separated list of *available* delays (`0-3-5-7`). `P` = plugged. `0` is also used for "no ejection charge" in some tools. The delay is measured **from burnout**, not from ignition |
| Propellant mass | 5 | **g** (ours) | Weighed grain mass. Used to derive the mass flow during the burn |
| Total mass | 6 | **g** (ours) | Loaded motor mass at ignition. Used for liftoff mass and CG |
| Manufacturer | 7 | text | Free text, may contain spaces. Use `UVCE Rocketry` for club motors so they group together in the motor list |

### 3.3 The data block

- **Two columns:** time (s), thrust (N). Separated by spaces or tabs.
- A **third column** appears in some RASP-derived files (remaining propellant mass at that
  time). OpenRocket generally derives the mass flow from the thrust curve and the declared
  propellant mass instead, so the third column can usually be omitted. If you include it,
  keep it consistent with the header's units and check the imported result.
- Times must be **strictly increasing**. Duplicate time values will confuse the parser or
  produce a vertical segment with an undefined area contribution.
- **Start at t = 0.0 with F = 0.0.** Some files start at the first non-zero thrust; that
  shifts the whole curve and makes the delay bookkeeping wrong. Start at zero.
- **End at zero thrust.** `1.30 0.0` is the last line of our example for a reason.
- **No negative thrust.** If the load cell produced a small negative tare, clamp to zero —
  negative thrust subtracts impulse and confuses the mass flow calculation.
- **Realistic precision:** 2 decimals on time, 2–3 significant figures on thrust. Writing
  15 decimal places does not make the data better; it makes the file unreadable and hides
  transcription errors.

---

## 4. The RSE format (XML) — the safer alternative

RockSim's `.rse` format is XML. OpenRocket imports it, and — critically — the mass units are
**grams** by definition, so there is nothing to guess.

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<engine-database>
  <engine-list>
    <!-- mfg      : manufacturer, shown in OpenRocket's motor list
         code     : designation (no spaces)
         Type     : "single", "reload" or "hybrid"
         dia, len : millimetres
         initWt   : loaded mass in GRAMS
         propWt   : propellant mass in GRAMS
         delays   : available delays; P = plugged
         auto-calc-mass / auto-calc-cg : let the tool derive mass and CG
                        during the burn from the thrust curve and propWt
         avgThrust, peakThrust, burn-time, Itot : documentation values;
                        the simulation uses the eng-data point list -->
    <engine mfg="UVCE Rocketry" code="E19KNSB" Type="single"
            dia="24.0" len="100.0" initWt="68.0" propWt="20.0" delays="P"
            auto-calc-mass="1" auto-calc-cg="1"
            avgThrust="19.0" peakThrust="22.5" burn-time="1.30" Itot="24.6">
      <comments>24 mm KNSB. Reduced from static fire SF-2025-03-02.
Itot 24.6 N.s, Favg 19.0 N, Isp 126 s. Masses in grams.</comments>
      <data>
        <!-- t = time (s), f = thrust (N).
             m = remaining propellant mass (g) and cg = propellant CG (mm)
             are optional when auto-calc-mass / auto-calc-cg are enabled. -->
        <eng-data t="0.00" f="0.0"/>
        <eng-data t="0.04" f="6.0"/>
        <eng-data t="0.08" f="14.0"/>
        <eng-data t="0.15" f="19.0"/>
        <eng-data t="0.30" f="21.0"/>
        <eng-data t="0.50" f="22.0"/>
        <eng-data t="0.70" f="22.5"/>
        <eng-data t="0.90" f="22.5"/>
        <eng-data t="1.05" f="21.0"/>
        <eng-data t="1.15" f="18.0"/>
        <eng-data t="1.22" f="11.0"/>
        <eng-data t="1.28" f="4.0"/>
        <eng-data t="1.30" f="0.0"/>
      </data>
    </engine>
  </engine-list>
</engine-database>
```

Notes on `.rse`:

- The tags and attribute names are case-sensitive. `<eng-data>` and `<engine-list>` are
  lowercase; attribute names are camelCase (`initWt`, `propWt`, `auto-calc-mass`).
- Attributes beyond those shown exist in the wild (case information, delay composition
  data, and so on). They are optional; if OpenRocket complains about your file, compare it
  against an `.rse` file that imports cleanly and add what is missing.
- If you would rather supply mass and CG explicitly at each point, switch
  `auto-calc-mass`/`auto-calc-cg` off and add `m="..."` and `cg="..."` to each `eng-data`
  element. Most club work does not need this.
- XML is unforgiving of syntax errors, but the error message tells you the line. Fix it
  rather than guess.

**Which to use?** Write `.eng` for sharing with other tools and people, and keep a `.rse`
master for the club's own motors. Generate both from the same spreadsheet so they cannot
drift apart.

---

## 5. How many thrust-curve points do you need?

The simulator connects your points with straight lines and integrates the resulting polygon.
So the question is: *where does the real curve bend?*

| Region | Point spacing needed | Why |
|---|---|---|
| Ignition transient (first 0.1–0.2 s) | every 10–20 ms, or at least 4–6 points | Sets the rail exit velocity and the initial acceleration |
| Steady burn | every 0.1–0.3 s | Almost straight; extra points add nothing |
| Tail-off (last 10–20 % of burn) | every 20–50 ms, 4–6 points | Sets the burnout velocity, and the burn-time number a reviewer checks |
| End | one final zero-thrust point | Defines the burn time |

Practical guidance:

- **13–40 points** is the normal range for a club motor. Our example uses 13.
- **20–60 points** if you have a real 1 kHz measurement and want fidelity through the
  ignition spike.
- **Never fewer than 4** for anything you intend to fly on.
- **More points ≠ better.** Points placed off the real curve bias the integral. If your
  reduction filter has smoothed the data, adding more points from the smoothed curve is
  fine; adding points from raw noise is not (see §7).
- **Check by re-integrating.** The trapezoid sum of the point list must equal the value you
  computed from the full-resolution data to within ~1 %. If it does not, you have
  under-sampled a bending region.

Worst-case error check for a straight-line segment of length Δt, where the true curve bows
away from the chord by a fraction `k` of the thrust: the missing area is roughly
`(2/3)·k·F·Δt`. For a 0.2 s segment, a 20 N thrust and a 10 % bow, that is 0.27 N·s —
about 1 % of a 24 N·s motor. That is the level of error you are managing.

---

## 6. Deriving total impulse, average thrust and burn time

For a point list `(t₀,F₀) … (tₙ,Fₙ)`:

```
Trapezoid rule (total impulse):
    I_total = Σ  (t(i+1) − t(i)) · (F(i+1) + F(i)) / 2          [N·s]

Burn time:
    t_burn  = t(last non-zero thrust) − t(first non-zero thrust)   [s]
              (for our motors: from the first rise to the final zero point)

Average thrust:
    F_avg   = I_total / t_burn                                   [N]

Peak thrust:
    F_peak  = max(F)                                             [N]

Delivered specific impulse (the honesty check):
    Isp     = I_total / (m_prop · g₀)      with m_prop in kg, g₀ = 9.80665 m/s²   [s]
```

**Spreadsheet recipe** (time in column A, thrust in column B, first data row = 2):

| Cell | Formula | Meaning |
|---|---|---|
| C2 | `=(A3-A2)*(B3+B2)/2` | Impulse of one segment |
| C14 | (fill C2 down to the second-to-last row) | …all segments |
| C15 | `=SUM(C2:C14)` | **Total impulse (N·s)** |
| C16 | `=A14-A2` | **Burn time (s)** |
| C17 | `=C15/C16` | **Average thrust (N)** |
| C18 | `=MAX(B2:B14)` | **Peak thrust (N)** |
| C19 | `=C15/((propMass_g/1000)*9.80665)` | **Delivered Isp (s)** |
| C20 | `=IF(AND(C19>95,C19<135),"KNSB plausible","CHECK THE DATA")` | Sanity gate |

Expected delivered Isp values:

| Propellant | Typical delivered Isp | If you compute more than this… |
|---|---|---|
| KNSB (potassium nitrate / sorbitol) | 100–130 s | Your load cell is under-reading, or the propellant mass is over-stated |
| KN/dextrose (caramel candy) | 90–120 s | Same |
| APCP (ammonium perchlorate composite) | 150–200 s | Your calibration is wrong, or you are measuring a different motor than you think |
| Commercial black powder | 60–90 s | — |

An Isp of 400 s is not a triumph. It is a broken calibration, and every simulation built on
it will be wrong in the dangerous direction.

---

## 7. From static fire CSV to `.eng` — the conversion procedure

### 7.1 What the test stand gives you

A typical club stand: a load cell under the motor, an amplifier (HX711 or a strain-gauge
bridge amplifier), a microcontroller or DAQ, and a CSV log with at least
`time_s, thrust_N` — or raw counts/volts that you convert yourself.

| Requirement | Value | Why |
|---|---|---|
| Sample rate | **≥ 200 Hz**, 1 kHz preferred | The ignition spike can rise in under 20 ms |
| Load cell range | 2–5× the expected peak thrust | Below 2× you clip; far above you lose resolution |
| Log length | ≥ 1 s before ignition and ≥ 2 s after burnout | Gives you a tare baseline and a clean tail |
| Calibration | Known masses across the expected range | A single-point calibration hides non-linearity |
| Repeatability | 2 fires of the same motor design before you trust the file | One fire is an anecdote |

### 7.2 The ten steps

1. **Calibrate the load cell.** With the stand assembled, record the reading for a set of
   known masses (e.g. 0.5 / 1 / 2 / 5 kg → 4.91 / 9.81 / 19.62 / 49.05 N). Fit a straight
   line `F = k·(reading − reading_zero)`; require R² > 0.999 and check that the residuals
   are not systematically curved (which would mean a bent or badly mounted cell). Record
   the constant in the test log. Do this **before every firing session**.
2. **Log a pre-ignition baseline** of 0.5–1.0 s and **tare to it** (subtract the mean
   baseline from the whole record). Do not assume the zero is zero — thermal drift in the
   stand is real.
3. **Convert to newtons** and clamp small negative values to zero.
4. **Filter lightly if at all.** A moving average over 5–9 samples at 1 kHz (5–9 ms) removes
   the worst electrical noise without touching the ignition transient. A 100 ms average
   destroys the spike and under-reports total impulse. **Never** filter more than 20 ms at
   1 kHz, and record the filter you used.
5. **Trim to the burn.** Find the **ignition point** as the first sample where thrust exceeds
   a threshold (use ~5 % of peak, held for ≥ 3 samples) and the **burnout point** as the
   last sample above that threshold. Keep the pre-rise sample as `t = 0`.
6. **Integrate at full resolution** with the trapezoid rule. This is your reference
   `I_total`, `F_avg`, `t_burn`, `F_peak` and `Isp` — the numbers that go in the file
   header comments and in the test log.
7. **Reduce to points.** Walk through the full-resolution data and pick points:
   - every 10–20 ms through the rise,
   - every 100–300 ms through the steady region (or wherever the slope changes),
   - every 20–50 ms through the tail,
   - plus a final hand-written `(last_time, 0.0)`.
   A simple systematic method that works well: keep every *n*-th sample, choosing *n* so
   the total is 20–40 points — but **always keep** the peak, the start of the tail, and the
   last non-zero sample.
8. **Re-integrate the reduced list** and compare with step 6. Accept if within ~1 %; if not,
   add points in the region where the two curves differ most.
9. **Write the file.** Header line with designation, diameter, length, delays, propellant
   mass (weighed, grams), total loaded mass (weighed, grams), manufacturer. Comment block
   with the fire reference, the reduced values, the Isp, and the mass units.
10. **Import and verify in OpenRocket.** Read back the mass, total impulse, average thrust
    and burn time and compare with the comment block. Then load it in the design and run a
    nominal simulation. If the apogee moves by a surprising amount, the file is wrong.

### 7.3 Worked example: reducing the raw CSV

**Raw extract** (as exported by the load cell DAQ; 1 kHz, so only every 10th–40th sample is
shown; the real file has ~2000 rows). Note the tare drift before ignition and the noise:

```
time_s, thrust_N
-0.500, -0.31
-0.250, -0.24
-0.100, -0.36
 0.000, -0.28      <- tare baseline ends here (mean ≈ -0.30 N)
 0.038,  2.10      <- first crossing of the 5 %-of-peak threshold (~1.1 N)
 0.042,  4.95
 0.055,  6.42
 0.070, 11.30
 0.090, 15.80
 0.120, 18.40
 0.160, 19.90
 0.300, 21.20
 0.500, 21.85
 0.700, 22.40
 0.900, 22.35
 1.050, 20.80
 1.150, 17.60
 1.220, 10.40
 1.280,  3.60
 1.295,  1.20
 1.310,  0.20
 1.400, -0.15
 1.600, -0.22
```

**Reduced point list** after taring, filtering (7-sample moving average), trimming and
reduction to 13 points. The `ΣI` column is the running total impulse — do this by hand once
so you understand where your motor class comes from:

| # | t (s) | F (N) | Δt (s) | F_mean (N) | ΔI (N·s) | ΣI (N·s) |
|---|---|---|---|---|---|---|
| 1 | 0.00 | 0.0 | — | — | — | 0.000 |
| 2 | 0.04 | 6.0 | 0.04 | 3.00 | 0.120 | 0.120 |
| 3 | 0.08 | 14.0 | 0.04 | 10.00 | 0.400 | 0.520 |
| 4 | 0.15 | 19.0 | 0.07 | 16.50 | 1.155 | 1.675 |
| 5 | 0.30 | 21.0 | 0.15 | 20.00 | 3.000 | 4.675 |
| 6 | 0.50 | 22.0 | 0.20 | 21.50 | 4.300 | 8.975 |
| 7 | 0.70 | 22.5 | 0.20 | 22.25 | 4.450 | 13.425 |
| 8 | 0.90 | 22.5 | 0.20 | 22.50 | 4.500 | 17.925 |
| 9 | 1.05 | 21.0 | 0.15 | 21.75 | 3.263 | 21.188 |
| 10 | 1.15 | 18.0 | 0.10 | 19.50 | 1.950 | 23.138 |
| 11 | 1.22 | 11.0 | 0.07 | 14.50 | 1.015 | 24.153 |
| 12 | 1.28 | 4.0 | 0.06 | 7.50 | 0.450 | 24.603 |
| 13 | 1.30 | 0.0 | 0.02 | 2.00 | 0.040 | **24.643** |

**Results:**

```
I_total = 24.64 N·s
t_burn  = 1.30 s
F_avg   = 24.64 / 1.30 = 18.96 ≈ 19.0 N
F_peak  = 22.5 N
Isp     = 24.64 / (0.0200 kg × 9.80665) = 125.6 s        -> plausible KNSB
Class   = E  (20.01 – 40.00 N·s)                          -> designation E19
```

Weighed masses: propellant grain 20.0 g before the fire (and ~0 g after); loaded motor
68.0 g. That gives the header line:

```
E19KNSB  24  100  P  20.0  68.0  UVCE Rocketry
```

### 7.4 Worked example: the same motor typed in manually (quick method)

When you need an answer in five minutes and the detailed curve is not ready, create the
motor in OpenRocket's motor editor, or write a 4-point file:

| time (s) | thrust (N) |
|---|---|
| 0.00 | 0.0 |
| 0.10 | 25.0 |
| 1.10 | 20.0 |
| 1.30 | 0.0 |

```
I_total = 0.10×(0+25)/2 + 1.00×(25+20)/2 + 0.20×(20+0)/2
        = 1.25 + 22.50 + 2.00 = 25.75 N·s
t_burn  = 1.30 s
F_avg   = 19.8 N        -> class E, designation would be E20
```

Within 5 % of the reduced curve on total impulse, but it hides the ignition transient
(which drives rail exit velocity) and the tail-off (which drives burnout velocity). Use it
for sizing, never for a design review, never for a delay decision.

---

## 8. Motor class letters explained

Motor classes are defined by **total impulse**, with each class being a factor of two wide.
The letter says how much total impulse the motor delivers; the number says roughly how hard
it pushes (average thrust in newtons). The two are independent: a slow-burning motor and a
fast-burning motor can be the same class.

| Class | Total impulse (N·s) | Typical use | Club relevance |
|---|---|---|---|
| 1/4A | 0.313 – 0.625 | Micro | — |
| 1/2A | 0.626 – 1.25 | Micro | — |
| A | 1.26 – 2.50 | Tiny test rockets | Stage 0 |
| B | 2.51 – 5.00 | Small | Stage 0 |
| C | 5.01 – 10.00 | Small | Stage 0 |
| D | 10.01 – 20.00 | Small | Stage 1 (light rockets) |
| **E** | **20.01 – 40.00** | **Small** | **Stage 1 — our KNSB E19 (24.6 N·s)** |
| F | 40.01 – 80.00 | Mid | Stage 2 |
| G | 80.01 – 160.00 | Mid | Stage 2 |
| H | 160.01 – 320.00 | High power (certification territory in the US) | Stage 3 |
| I | 320.01 – 640.00 | High power | Stage 3 |
| J | 640.01 – 1280.00 | High power | Stage 3 |
| K | 1280.01 – 2560.00 | High power | Stage 3+ |
| L | 2560.01 – 5120.00 | High power | Stage 3+ |
| M | 5120.01 – 10240.00 | High power | — |
| N | 10240.01 – 20480.00 | High power | — |
| O | 20480.01 – 40960.00 | High power | — |

(There are also fractional micro-classes below 1/4A; they are irrelevant to us. The exact
boundaries follow the NFPA 1125 / NAR convention — quote the table, not your memory.)

**How to determine the class of a motor:**

1. Compute `I_total` from the thrust curve by trapezoid integration (§6).
2. Find the range in the table that contains it.
3. The letter is the class. The number after the letter is the average thrust rounded
   (some high-power motors carry a decimal, e.g. `J350`).
4. Sanity check: `I_total ≈ F_avg × t_burn`. If the class letter implies a very different
   impulse from what the thrust curve gives, you have made an arithmetic error, not
   discovered a new motor class.

Rules of thumb that follow from the table:

- Doubling the total impulse moves you up exactly one class.
- A longer burn at the same thrust moves you up a class; a bigger throat at the same
  propellant mass mostly raises the thrust and shortens the burn, staying in the class.
- **Two motors of the same class are not interchangeable.** An `E19` (19 N for 1.3 s) and an
  `E40` (40 N for 0.6 s) both deliver ~25 N·s but need different rails, different fins and
  different delays. Always model the actual curve.

> **Regulatory note.** In many countries (including the US, under NFPA 1127) classes H and
> above are "high power" and require certification. Indian requirements are set through
> IN-SPACe and the launch range; confirm the current rules before ordering or building
> anything in the H+ range. Nothing in this document is an authorisation.

---

## 9. Delay grain selection and ejection timing

### 9.1 The one number you must get right

**Optimum delay** is the time from **burnout** to **apogee**. OpenRocket computes it for you
and shows it in the simulation results overview (labelled "Optimum delay" or "Optimal
delay"). Commercial motor designations and OpenRocket both measure the delay from **burnout**,
not from ignition.

Procedure:

1. Run the nominal simulation with the correct mass and the real motor file.
2. Read the **optimum delay** and the **time to apogee**.
3. Choose the available delay **closest to but not exceeding** the optimum.
4. Re-run the simulation with that delay selected and check the **deployment velocity** in
   the results. Under 10 m/s is good; under 20 m/s is the absolute limit; over 20 m/s means
   "do not fly this delay".
5. If no available delay is acceptable, the answer is **electronic deployment**, not
   wishful thinking.

### 9.2 Why both directions are bad

| Error | What happens | Consequence |
|---|---|---|
| Delay **too short** (e.g. 2 s early) | The chute opens while the rocket is still climbing fast | Opening load scales with v²: a chute opened at 40 m/s sees ~16× the load it would at 10 m/s. Shredded chute, zippered tube, snapped shock cord |
| Delay **about right** (±0.5 s) | Deployment within a few m/s of apogee | Lowest loads, most reliable |
| Delay **too long** (2–4 s) | Deployment while the rocket is descending fast, nose-first or tumbling | Zipper, chute stripped, or total recovery failure at 30–60 m/s |
| Delay **much too long / charge fails** | Ballistic descent | The rocket is destroyed and the landing area is unpredictable |

Practical band: aim for a delay within **±1 s of the optimum**, and never allow the
simulated deployment velocity to exceed 20 m/s.

### 9.3 Making your own delay grain

For a club-made delay grain that **ignites together with the propellant**, its burn must
cover both the thrust phase and the coast:

```
required delay grain burn time  =  t_burn + delay(from burnout)
required delay grain length     =  burn time × delay grain burn rate (mm/s)
```

So for our motor with a 4.5 s optimum delay: `1.30 + 4.5 = 5.8 s` of delay-grain burn. At a
measured 3.0 mm/s that is a 17.4 mm grain — but **only** if your 3.0 mm/s was measured under
the same conditions.

Two traps:

- **Pressure dependence.** A delay grain burns faster under chamber pressure during the
  thrust phase and slower after burnout. A burn rate measured on an open bench is not the
  burn rate in the motor. Measure the complete assembly end-to-end: a static fire with the
  delay grain installed and an ejection-charge witness (a small bag or a smoke puff), timed
  from ignition.
- **Ambient temperature.** Propellant and delay burn rates rise with grain temperature.
  Grains conditioned in a hot car will give a shorter delay than grains conditioned at dawn.

**Club recommendation:** fly plugged motors with electronic apogee deployment for Stage 1
and above. It removes the delay-grain problem entirely, it gives you a logged altitude for
validation (see
[Simulation_Plan_and_Validation.md](Simulation_Plan_and_Validation.md)), and it lets you
choose a deployment altitude rather than hoping a burn rate is repeatable.

### 9.4 If you do fly an ejection charge

- Size the charge by **ground testing**, not by formula: start at ~0.5 g of black powder for
  a 66 mm airframe with a friction-fit nose cone, and work up until the recovery train
  deploys reliably (usually 0.5–1.0 g for our sizes).
- Always use a **heat blanket or wadding**; melting a nylon chute is a common, silent,
  expensive failure.
- Ground-test with the **actual packed rocket**, cold, at the field, before the first flight
  of a new design. Log the charge mass in the design log.
- Remember that OpenRocket does not simulate the charge at all. The deployment in the
  simulation happens exactly when you tell it to; in reality it happens when the charge
  fires, which is a different thing.

---

## 10. Managing the club's motor library

### 10.1 Folder and naming convention

```
50_SIMULATION/
├── motors/
│   ├── E19KNSB.eng                  # distributed / sharing form
│   ├── E19KNSB.rse                  # club master (units unambiguous)
│   ├── E19KNSB_2025-03-a.eng        # frozen revision actually flown
│   ├── F42KNSB.eng
│   └── archive/                     # superseded revisions, never deleted
├── static_fire/
│   ├── SF-2025-03-02/E19KNSB_raw.csv
│   ├── SF-2025-03-02/calibration.csv
│   └── SF-2025-03-02/notes.md
└── designs/
    └── UVCE-S1_rev-A.ork
```

Rules:

- Filename = the motor designation, exactly as it appears in the file's first field.
- One motor per file.
- Keep every revision. A simulation record points at a specific file revision; if you
  overwrite the file, the record becomes unreproducible.
- **A `.ork` file does not contain your custom motor.** Send the motor file with the design,
  or zip them together, or the recipient will see a missing-motor error.

### 10.2 The motor register

Keep one CSV that lists every motor the club has ever defined. It is the index to the whole
library, and it is what you hand to a reviewer.

| Designation | Rev | Date | Class | I_total (N·s) | F_avg (N) | F_peak (N) | Burn (s) | Prop (g) | Loaded (g) | Isp (s) | Delays | Fire ref | File |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E19KNSB | 2025-03-a | 2025-03-02 | E | 24.64 | 19.0 | 22.5 | 1.30 | 20.0 | 68.0 | 126 | P | SF-2025-03-02 | E19KNSB.eng |
| E19KNSB-b | 2025-04-b | 2025-04-11 | E | 26.10 | 20.1 | 24.0 | 1.30 | 21.5 | 69.5 | 124 | P | SF-2025-04-11 | E19KNSB-b.eng |

### 10.3 Importing into OpenRocket

1. Put the files in the club motor folder (`50_SIMULATION/motors/`).
2. **Edit → Preferences → Motors** (wording varies): add that folder to the list of
   thrust-curve directories. OpenRocket scans it at startup.
3. Alternatively, use the motor-selection dialog's **Import motor** / **New motor** entry
   point, depending on version.
4. Restart OpenRocket if a newly added file does not appear.
5. **Verify** the imported numbers against the register before using the motor.

### 10.4 What to archive with every motor

- The raw static-fire CSV, unmodified.
- The load-cell calibration record for that session.
- The grain drawing or dimensions, and the propellant mix and batch.
- The ambient temperature and the propellant temperature at the fire.
- The reduced point list (a CSV is fine) and the final `.eng`/`.rse`.
- A note on anything unusual: a nozzle erosion observation, a chuff, a hard start.

A motor file without its fire record is a rumour. A year from now, the register plus the raw
CSV is the only thing that will let you answer "why did we think this motor was 24 N·s?"

---

## 11. Worked example, end to end: 24 N·s KNSB motor → valid `.eng`

**Step 1 — the fire.** Static fire SF-2025-03-02. Grain: KNSB 65/35, 20.0 g, 24 mm OD,
9 mm core, 30 mm long. Loaded mass 68.0 g. 1 kHz logging, 10 kg load cell, calibrated with
0.5/1/2/5 kg masses (R² = 0.9997). Burn observed with a clean ignition, no chuffing,
nozzle intact.

**Step 2 — reduce.** Tare, filter (7-sample moving average), trim, integrate at full
resolution, then reduce to 13 points. Reduced values: `I_total = 24.64 N·s`,
`t_burn = 1.30 s`, `F_avg = 19.0 N`, `F_peak = 22.5 N`, `Isp = 125.6 s`.

**Step 3 — classify.** 24.64 N·s falls in 20.01–40.00 N·s → **class E**. Average thrust
19 N → designation **E19**. Add the propellant to keep it unique: **E19KNSB**.

**Step 4 — check plausibility.**
- Isp 125.6 s is inside the KNSB band (100–130 s). ✔
- `F_avg × t_burn = 19.0 × 1.30 = 24.7 ≈ I_total`. ✔
- Propellant 20.0 g at 125 s Isp → 24.5 N·s. ✔
- Peak/average ratio 1.18 — a smooth, slightly progressive burn, typical of a cylindrical
  core burner. ✔
- Two consecutive fires of the same grain design within ±5 % of each other? If yes, publish
  the file. If not, investigate before publishing.

**Step 5 — write the file.**

```
; UVCE Rocketry Club - 24 mm KNSB motor
; File: E19KNSB.eng    Revision: 2025-03-a    MASSES IN GRAMS
; Source: static fire SF-2025-03-02 (10 kg load cell, 1 kHz, calibrated 2025-03-02)
; Grain: KNSB 65/35, 20.0 g, 24 mm OD, 9 mm core, 30 mm long; loaded mass 68.0 g
; Reduced: Itot 24.64 N.s | Favg 19.0 N | Fpeak 22.5 N | burn 1.30 s | Isp 126 s
; Class: E. Delays: P (plugged; electronic deployment)
E19KNSB  24  100  P  20.0  68.0  UVCE Rocketry
0.00   0.0
0.04   6.0
0.08   14.0
0.15   19.0
0.30   21.0
0.50   22.0
0.70   22.5
0.90   22.5
1.05   21.0
1.15   18.0
1.22   11.0
1.28   4.0
1.30   0.0
```

**Step 6 — import and verify.** Import into OpenRocket. Confirm that it reports roughly:
propellant 20 g, total 68 g, total impulse 24.6 N·s, average thrust 19 N, burn 1.30 s. Then
run the nominal UVCE-S1 simulation and confirm the apogee lands inside the hand-calculated
band from [OpenRocket_Workflow.md](OpenRocket_Workflow.md) §5.13 (roughly 150–220 m). If it
does not, the problem is in the design mass, not in the motor file — check that next.

**Step 7 — record.** Add the row to the motor register (§10.2), archive the raw CSV and the
calibration record, and add the file revision to the design log entry for UVCE-S1.

---

## 12. Troubleshooting motor import problems

| Symptom | Likely cause | Fix |
|---|---|---|
| Motor does not appear in the list at all | Wrong folder, wrong extension, or OpenRocket scanned before you added the file | Check the folder in Preferences → Motors, confirm the `.eng`/`.rse` extension, restart OpenRocket |
| Motor appears but with 0 N·s or no curve | Parser stopped at a malformed header line or bad data line | Check for a missing field in the header, a comma used as a decimal separator, an empty line inside the data block, or a stray character |
| Mass is 1000× too large or too small | Gram/kilogram ambiguity | Convert the mass fields and re-import; verify against the register |
| Thrust curve looks like a mirror image or a spike | Times not in increasing order, or a duplicated time value | Sort and de-duplicate; times must strictly increase |
| Burn time longer than expected | Missing final zero-thrust point | Add the explicit `last_time 0.0` line |
| "Two motors with the same designation" | Reused designation for a new revision | Give every revision a unique designation, or remove the old file from the scanned folder |
| Motor simulates but the rocket does not move | Thrust present but the motor mass is enormous, or the rocket mass is enormous | Verify masses and the design's liftoff mass |
| Simulation warnings about deployment at high speed | Delay too long for the actual apogee time | Re-read the optimum delay from the results and change the delay, or switch to electronic deployment |
| Results differ from last month's run for the same design | The motor file was overwritten in place | Revert to the archived revision, or restore the file from the design log's revision reference |

---

## 13. Quick reference card

```
.eng structure
--------------
; comment                      (anything after ';' is ignored)
DESIG  dia  len  delays  propMass  totalMass  manufacturer
t1  F1
t2  F2
...
tN  0.0                        (final zero-thrust point is mandatory)

Designation : class letter + average thrust, no spaces        E19KNSB
dia / len   : millimetres                                     24 / 100
delays      : hyphen list, or P for plugged                   P  or  4-6-8
masses      : GRAMS in our files (verify after import!)       20.0 / 68.0
thrust data : seconds, newtons, times strictly increasing

Key numbers
-----------
I_total = Σ (t(i+1)-t(i))·(F(i+1)+F(i))/2        [N·s]   -> class letter
F_avg   = I_total / t_burn                       [N]     -> number in the name
Isp     = I_total / (m_prop[kg] · 9.80665)       [s]     -> KNSB 100-130 s
Class   : A 1.26-2.5 | B 2.51-5 | C 5.01-10 | D 10.01-20 | E 20.01-40
          F 40.01-80 | G 80.01-160 | H 160.01-320 | I 320.01-640 | J 640.01-1280
          K 1280.01-2560 | L 2560.01-5120 | M 5120.01-10240 | N ..20480 | O ..40960

Delay
-----
The delay is measured FROM BURNOUT. Read OpenRocket's optimum delay, pick the
available delay closest to but not longer than it, and keep the simulated
deployment velocity under 10 m/s (20 m/s absolute limit).

Golden rules
------------
1. Verify every imported motor's mass and impulse. Always.
2. Never edit a certified commercial motor file.
3. Never fly a motor file that has no static-fire record behind it.
4. Ship the motor file with the design file - the .ork does not contain it.
```
