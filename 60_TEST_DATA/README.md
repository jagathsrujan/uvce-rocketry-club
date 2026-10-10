# UVCE Rocketry Club — Test Data

**Folder:** `60_TEST_DATA/`
**Parent context:** `UVCE_Rocketry_Roadmap.md`, `40_SAFETY/Static_Test_Procedure.md` §7
**Status:** Controlled. **Raw data in this folder is never edited.** See §2.

> **One test proves nothing. The data is the only thing that survives a motor.** A motor is consumed in
> two seconds. The thrust curve, the pressure trace, the video, and the calibration record are what the
> next team inherits. **A measurement you have not calibrated is not a measurement, and data you cannot
> align in time is data you cannot interpret.**

---

## 1. Folder structure

```
60_TEST_DATA/
├── README.md                     ← this file
├── Calibration_Record.md         ← the calibration tracking template (see §7)
├── raw/                          ← RAW DATA. Write-once. Never edited. See §2.
│   ├── static_fires/
│   │   ├── ST-001/
│   │   │   ├── ST-001_2027-01-10_thrust.csv
│   │   │   ├── ST-001_2027-01-10_pressure.csv
│   │   │   ├── ST-001_2027-01-10_video_sideon.mp4
│   │   │   ├── ST-001_2027-01-10_video_wide.mp4
│   │   │   ├── ST-001_2027-01-10_audio.wav
│   │   │   └── ST-001_2027-01-10_photos/       ← unedited originals
│   │   └── ST-002/
│   ├── strand_burner/
│   ├── flights/
│   │   ├── FL-001/
│   │   │   ├── FL-001_2027-03-02_altimeter.csv
│   │   │   ├── FL-001_2027-03-02_flightlog.csv
│   │   │   └── FL-001_2027-03-02_video.mp4
│   │   └── FL-002/
│   ├── hydrostatic_proof_tests/
│   └── calibration/
│       ├── CAL-2027-001_loadcell_10kg.csv
│       └── CAL-2027-002_pressure_40bar.csv
├── processed/                    ← Derived files. ANALYSIS PRODUCES NEW FILES HERE.
│   ├── ST-001_2027-01-10_thrust_analysis.ipynb
│   ├── ST-001_2027-01-10_thrust_filtered.csv
│   └── ST-001_2027-01-10_impulse_summary.csv
├── calibration/                  ← certificates, reference standard records, as-found/as-left sheets
├── documents/                    ← scanned procedure sheets, site sheets, test logs, permissions
└── archive/                      ← superseded datasets, kept but not active
```

**Rules for the structure:**

- **One folder per test ID** under the relevant activity. The test ID matches the one on the field
  checklist (`FORM-04`, `FORM-05`) and in the test log workbook.
- **Do not rename or move a raw folder once files are in it.** A moved raw file is a broken reference in
  every report that cites it.
- **Do not mix raw and processed data in the same folder**, ever. If it came out of a script, it belongs
  in `processed/`.
- **Photographs and video are data.** They go in the test folder with the same naming convention, in an
  unedited `photos/` subfolder. Do not crop, colour-correct, or re-encode the originals.

---

## 2. THE RULE: raw data is never edited

> ## 🔴 RAW DATA IS NEVER EDITED, OVERWRITTEN, OR "CLEANED".
> **The raw file is the record.** *(Static_Test_Procedure.md §7.3)*

What this means in practice:

| ✅ You may | ❌ You may never |
|---|---|
| **Copy** a raw file and work on the copy in `processed/` | **Edit, trim, splice, or re-save** a file in `raw/` |
| **Read** raw data in a script and write a **new** output file | **Overwrite** a raw file with a filtered, zeroed, or smoothed version |
| **Add** a new file to a test folder (a second camera, an audio track) | **Delete** a raw file, even a bad one — a bad file is evidence of a bad sensor |
| **Write a separate notes file** describing a problem with the raw data | **"Just fix" an offset, a spike, or a dropped sample** in place |
| **Document** a sensor fault in the test report and mark the data unusable | **Rename** a file to make it fit the convention after the fact — fix the convention instead |
| **Re-run** an analysis and save a new, versioned output | **Reuse a filename** for a different analysis revision |

**Why this is absolute:**

1. **A raw file that has been touched cannot be trusted, and cannot be defended.** If a curve looks
   wrong, the club must be able to go back to the untouched original and ask why.
2. **Analysis produces new files.** The chain from raw → processed → figure must be reconstructible by
   someone who was not there. That is the whole point of keeping data.
3. **A "cleaned" file hides an anomaly.** Anomalies are the most valuable output of a test — the spike
   tells you the igniter was oversized, the mountain curve tells you ignition was delayed, the dropout
   tells you the logger lost power. Cleaning them away destroys the lesson.
4. **Falsifying or altering a record is a disciplinary matter** (`Safety_Manual_Master.md` §9.3, Level 4).

**If a raw file is wrong:** do not fix it. **Write a note** next to it — `ST-003_2027-02-14_thrust_
SENSOR_FAULT.txt` — describing what is wrong and what it means, report it in the test report, and mark
the affected results as unusable. **Then fix the instrument, not the file.**

**Write-once practice:** after a test, set the raw files to read-only. Back up immediately — **two
copies, two separate devices, before anyone leaves the site** (`Static_Test_Procedure.md` §7.3).

---

## 3. Naming convention

> ### `<test-id>_<date>_<type>.<ext>`
>
> **Example:** `ST-003_2027-02-14_thrust.csv`

| Field | Format | Rules |
|---|---|---|
| **`<test-id>`** | `ST-###` static fire · `FL-###` flight · `SB-###` strand burner · `HP-###` hydrostatic proof · `CAL-YYYY-###` calibration | Uppercase. Hyphen. Zero-padded to three digits. **Must match the test log workbook and the field checklist.** |
| **`<date>`** | `YYYY-MM-DD` | ISO 8601. **Always zero-padded.** Sorts correctly, and cannot be misread as a different date. |
| **`<type>`** | See the table below | Lowercase, `snake_case` for multi-word types. |
| **`<ext>`** | `csv` `txt` `mp4` `wav` `jpg` `png` `ipynb` `pdf` `json` `bin` | Lowercase. |

**Standard `<type>` values — use these, do not invent new ones:**

| Type | Contents |
|---|---|
| `thrust` | Load cell thrust-time data |
| `pressure` | Chamber pressure-time data |
| `thrust_pressure` | Combined, single time base |
| `altimeter` | Barometric altimeter / flight computer log |
| `flightlog` | Flight log export (apogee, ejection events, timing) |
| `accel` / `gyro` | IMU axes |
| `temperature` | Thermocouple or thermistor channels |
| `video_sideon` | Side-on high-speed video |
| `video_wide` | Second, wider-framing camera |
| `video_onboard` | Onboard camera |
| `audio` | Audio track |
| `photo` | Still photograph (add a sequence number: `photo_01`) |
| `sync` | Sync-marker trace or event channel |
| `calibration` | Calibration data (as-found / as-left) |
| `filtered` | Processed derivative of a raw channel |
| `impulse_summary` | Reduced results (total impulse, burn time, Isp) |
| `notes` | Human-readable notes about the dataset |
| `sensorfault` | **Not used** — write `notes` and state the fault in the file |

**Examples:**

```
ST-003_2027-02-14_thrust.csv
ST-003_2027-02-14_pressure.csv
ST-003_2027-02-14_video_sideon.mp4
ST-003_2027-02-14_notes.txt
FL-007_2027-03-21_altimeter.csv
SB-002_2027-01-30_burnrate.csv
HP-001_2027-01-05_pressure.csv
CAL-2027-001_2027-01-04_calibration.csv
ST-003_2027-02-14_thrust_filtered.csv          ← lives in processed/, not raw/
```

**Where the naming convention differs from an instrument's own output:** the instrument's native
filename is **never** overwritten or renamed. **Copy it into `raw/` under the convention name, and keep
the native name in a `notes` file** that records the mapping. The convention applies to our copies, not
to the instrument's original export.

**Retention:** test data, calibration records, and test reports are **retained permanently**
(`Safety_Manual_Master.md` §8.4). **Nothing is deleted** — superseded data moves to `archive/`.

---

## 4. What belongs in this folder

| Belongs here | Notes |
|---|---|
| **Raw thrust curves** | Load cell output, as recorded. **≥ 100 Hz minimum, 1000 Hz preferred** |
| **Raw pressure curves** | Chamber pressure, thermally protected transducer. **The single most diagnostic measurement in the test** |
| **Flight logs** | Barometric and IMU logs, ejection event timing, apogee |
| **Altimeter data** | Raw and exported |
| **Calibration records** | As-found and as-left, with the reference standard used — see `Calibration_Record.md` |
| **Photographs** | Unedited originals, including the mounted motor (side-on and both ends), the igniter installation, and post-test component photographs |
| **Video references** | Side-on high-speed (**240 fps minimum, 1000 fps preferred**), wide-framing, and onboard. **Video files may be large — store on the club drive and keep the reference, checksum, and duration here** |
| **Hydrostatic proof test records** | Pressure, hold time, and observations (new motor designs) |
| **Strand burner data** | The measured burn rate — the foundation of the whole design chain |
| **Sync markers** | The clap, flash, or electrical pulse record that lets video and data be aligned in time |
| **Environment records** | Wind, temperature, humidity, and pressure at the time of the test, where they affect the result |

**Does NOT belong here:**

- **Analysed or filtered data** → `processed/`
- **The test report narrative** → `70_REPORTS/`
- **The safety checklist scans** → `40_SAFETY/forms/completed/` (reference them from here)
- **Design files, CAD, and drawings** → the design folder for the project
- **Personal photographs and social media content** — these are not records

---

## 5. Every test needs an entry in the test log workbook

> **Every test needs an accompanying entry in the test log workbook.** Data without a log entry is an
> orphan file that nobody can interpret in two years.

**The test log workbook** (`60_TEST_DATA/documents/Test_Log.xlsx`, one row per test) records, at minimum:

| Column | Example |
|---|---|
| Test ID | `ST-003` |
| Date | `2027-02-14` |
| Type | Static fire / flight / strand burner / proof test / calibration |
| Motor or rocket ID | `M-002` |
| Propellant batch ID | `KNSB-2027-003` |
| Grain ID(s) | `KNSB-2027-003-G1`, `-G2` |
| Grain density ratio | `0.98` |
| Tap test result | `PASS` |
| Igniter type and charge | `… / 1.2 g` |
| Test Director | `…` |
| Safety Officer | `…` |
| Site | `…` |
| Weather (wind, temp, humidity) | `…` |
| Data files (paths) | `raw/static_fires/ST-003/…` |
| Calibration record IDs used | `CAL-2027-001`, `CAL-2027-002` |
| Outcome | Fired / misfire / aborted / partial |
| Peak thrust (N) | `…` |
| Peak pressure (bar) | `…` |
| Burn time (s) | `…` |
| Total impulse (N·s) | `…` |
| Delivered Isp (s) | `…` |
| Anomalies | `…` |
| Test report reference | `70_REPORTS/…` |
| FORM-04 checklist reference | `40_SAFETY/forms/completed/2027/…` |

**The workbook is the index; this folder is the content.** If a file in this folder is not listed in the
workbook, the data is not yet usable. If a workbook row points at a missing file, that is a broken
record and must be fixed the same week.

**One test proves nothing.** You need **3–5 identical motors with overlapping thrust curves** before you
have a repeatable design. Change **one variable at a time** between tests — and record which variable
changed in the workbook row.

---

## 6. Data handling checklist — from the pad to the archive

- [ ] **Download and back up before anyone leaves the site.** Two copies, two separate devices
- [ ] Raw files set to **read-only** and copied into `raw/<activity>/<test-id>/`
- [ ] Files named to the convention `<test-id>_<date>_<type>.<ext>`
- [ ] Photographs and video copied as **unedited originals**
- [ ] Sync marker recorded and the alignment noted in a `notes` file
- [ ] Calibration before-and-after values recorded, with the calibration record IDs
- [ ] Environment at the time of the test recorded
- [ ] **Test log workbook row completed**
- [ ] Test report written **within 24 hours** and filed in `70_REPORTS/`
- [ ] Any anomaly, near miss, or incident logged — `FORM-06` and the incident log
- [ ] Data checked for integrity: sample rate, duration, no truncation, no gaps
- [ ] Long-term backup confirmed (club drive plus one offline copy)

---

## 7. Calibration

**Track every instrument's calibration in `Calibration_Record.md`.** The rule is simple:

> **An uncalibrated sensor makes the data worthless for performance analysis.**

- A **load cell** is calibrated with **known masses** (or a lever arm amplifying a known mass), with the
  lever ratio documented and the calibration accounting for it.
- A **pressure transducer** is calibrated against a **reference gauge** (or a deadweight tester).
- **Verify immediately before the test**, and **re-verify after the test**. Both values are recorded —
  the "after" value is how you detect a sensor that drifted or was damaged during the firing.
- The load cell must be sized so that **peak expected thrust is 50–80% of full scale**. An oversized
  load cell loses resolution; an undersized one is destroyed.
- The pressure transducer must be rated to at least **2× the expected MEOP**, and must be **thermally
  protected** — a grease-filled standpipe, a thermal barrier, or a standoff tube. **A transducer exposed
  directly to combustion gas is destroyed within milliseconds.**

---

## 8. Related documents

| Document | What it gives you |
|---|---|
| `40_SAFETY/Static_Test_Procedure.md` §3.3, §3.4, §7 | Instrumentation requirements, sample rates, data capture, data handling |
| `40_SAFETY/Static_Test_Procedure.md` §8.2 | Data analysis method: impulse, Isp, curve comparison |
| `40_SAFETY/forms/FORM-04_Static_Test_Checklist.md` | The field sheet that produces this data — Phase A data items, Phase F backup items |
| `70_REPORTS/Test_Report_Template.md` | Where the data is interpreted and compared against prediction |
| `60_TEST_DATA/Calibration_Record.md` | Instrument calibration tracking |
| `40_SAFETY/Safety_Manual_Master.md` §8.4 | Records retention — test data and calibration records are retained permanently |

---

*Raw data is never edited. Analysis produces new files. Two copies, two devices, before anyone leaves
the site.*
