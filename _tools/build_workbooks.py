#!/usr/bin/env python3
"""Build the UVCE Rocketry engineering workbooks."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xlsx_writer import Sheet, write_xlsx  # noqa: E402

ROOT = "/Users/jagathsrujan/Documents/uvce rocketry club"

# style ids (see xlsx_writer combos)
D, B, T, IT, HDR, SEC, NUM2, NUM3, LBLUE, INPUT, WARN, GOOD, LEFT, CTR = (
    0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14
)


def cell(v, st=D):
    """Cell dict; strings starting with '=' become real formulas."""
    if isinstance(v, str) and v.startswith("="):
        return {"f": v[1:], "s": st}
    return {"v": v, "s": st}


def hdr(cells):
    return [{"v": c, "s": HDR} for c in cells]


def sec(title):
    return [{"v": title, "s": SEC}]


# =============================================================================
# 1. MASS BUDGET
# =============================================================================
def mass_budget_v2():
    """Mass budget and CG tracker. All row references are computed, never hard-coded."""
    s = Sheet("Mass Budget", widths={0: 32, 1: 28, 2: 7, 3: 13, 4: 13, 5: 10, 6: 40},
              freeze="A5")

    def r(v, st=D):
        if isinstance(v, str) and v.startswith("="):
            return {"f": v[1:], "s": st}
        return {"v": v, "s": st}

    s.add([r("UVCE ROCKETRY - MASS BUDGET & CG TRACKER", T)])                       # 1
    s.add([r("Amber cells are inputs. Everything else is calculated. Mass in grams; "
             "CG is measured in mm from the nose tip.", IT)])                       # 2
    s.blank()                                                                       # 3

    # ---------------------------------------------------------------- component table
    s.add(sec("COMPONENT BREAKDOWN"))                                               # 4
    s.add(hdr(["Component", "Material / source", "Qty", "Unit mass (g)",
               "Total mass (g)", "CG (mm)", "Notes"]))                              # 5

    first_data = 6

    starter = [
        ("Nose cone", "balsa / 3D print", 1, 25, 60, "ogive, hollow"),
        ("Body tube", "kraft paper 40 mm OD", 1, 90, 450, "main airframe"),
        ("Motor casing + nozzle", "see motor design", 1, 55, 700, "EMPTY case mass"),
        ("Propellant grain", "KNSB 65/35", 1, 24, 690, "CONSUMABLE - excluded from dry mass"),
        ("Fins (set)", "plywood 3 mm", 3, 6, 820, "trapezoidal"),
        ("Centring rings", "plywood", 2, 4, 700, ""),
        ("Motor retention", "aluminium + screws", 1, 8, 700, "positive mechanical retention"),
        ("Parachute", "ripstop nylon", 1, 20, 300, "sized for 2-5 m/s descent"),
        ("Shock cord", "Kevlar", 1, 8, 400, ""),
        ("Avionics bay", "3D print / tube", 1, 30, 350, "flight computer + battery"),
        ("Battery", "Li-ion 18650 or NiMH", 1, 45, 350, "LiPo is PROHIBITED"),
        ("Launch lug / rail buttons", "plastic / alu", 2, 3, 500, ""),
        ("Paint + primer", "fluorescent pink/red/orange", 1, 15, 450, "mandatory hi-vis colour"),
    ]
    n_rows = len(starter) + 26          # leave room to add more components

    total_formula = ('=IF(G{r}="","",IF(LEFT(G{r},10)="CONSUMABLE",0,C{r}*D{r}))')
    for k in range(n_rows):
        i = first_data + k
        if k < len(starter):
            name, mat, qty, unit, cg, note = starter[k]
            s.add([r(name, INPUT), r(mat, INPUT), r(qty, INPUT), r(unit, INPUT),
                   r(total_formula.format(r=i), NUM2), r(cg, INPUT), r(note, LEFT)])
        else:
            s.add([r(None, INPUT), r(None, INPUT), r(None, INPUT), r(None, INPUT),
                   r(total_formula.format(r=i), NUM2), r(None, INPUT), r(None, LEFT)])

    last_data = first_data + n_rows - 1
    dry_range = f"E{first_data}:E{last_data}"
    cg_range = f"F{first_data}:F{last_data}"

    s.blank()
    s.add([r("TOTAL DRY MASS", B), r(None), r(None),
           r(f"=SUM({dry_range})", NUM2), r("g   excludes CONSUMABLE rows", IT)])
    s.add([r("TOTAL LAUNCH MASS", B), r(None), r(None),
           r(f"=SUM({dry_range})+E{first_data + 3}", NUM2),
           r("g   dry mass + propellant", IT)])
    s.blank()
    s.add([r("A row is excluded from dry mass when its Notes cell begins with "
             "CONSUMABLE. The propellant is tracked this way so dry mass and launch "
             "mass both stay honest.", IT)])
    s.blank()

    # ---------------------------------------------------------------- summary
    # Insert the summary ABOVE the table by rebuilding: simplest is to append a
    # clearly-labelled summary block after the table (kept below for clarity).
    s.add(sec("SUMMARY - key figures"))

    def put(label, value, fmt=D, note="", input_cell=False):
        rn = len(s.rows) + 1
        s.add([r(label, B), r(value, INPUT if input_cell else fmt), r(note, IT)])
        return rn

    r_dry = put("Dry mass (calculated)", f"=SUM({dry_range})", NUM2,
                "g   <- excludes CONSUMABLE rows")
    r_tgt = put("Dry mass (target)", 250, NUM2, "g   <- your design target", True)
    r_mar = put("Margin vs target", f'=IFERROR((B{r_dry}-B{r_tgt})/B{r_tgt},"")', NUM2,
                "want within +/-5%")
    put("STATUS",
        f'=IF(B{r_tgt}=0,"SET TARGET",IF(ABS(B{r_mar})<=0.05,'
        f'"PASS  (+/-5% required)","FAIL  (+/-5% required)"))', GOOD)
    r_hi = put("Maximum acceptable dry mass", f"=B{r_tgt}*1.05", NUM2,
               "g   <- target + 5%")
    put("Remaining mass to cut", f"=MAX(0,B{r_dry}-B{r_hi})", NUM2,
        "g   <- must reach zero to pass")
    s.blank()
    r_prop = put("Propellant mass", 24, NUM2,
                 "g   <- from the motor design calculator", True)
    put("LAUNCH MASS", f"=B{r_dry}+B{r_prop}", NUM2, "g   <- dry mass + propellant")
    s.blank()
    r_cg = put("Overall CG from nose tip",
               f'=IFERROR(SUMPRODUCT({cg_range},{dry_range})/B{r_dry},"")', NUM2,
               "mm   <- mass-weighted over dry mass")
    put("Overall length", 900, NUM2, "mm", True)
    r_cp = put("CP from nose tip", 0, NUM2,
               "mm   <- paste from OpenRocket", True)
    r_dia = put("Body diameter", 40, NUM2, "mm", True)
    r_sm = put("Static margin", f'=IFERROR((B{r_cp}-B{r_cg})/B{r_dia},"")', NUM2,
               "calibers   (want 1.0 - 2.0)")
    put("STABILITY",
        f'=IF(B{r_cp}=0,"ENTER CP FROM OPENROCKET",'
        f'IF(AND(B{r_sm}>=1,B{r_sm}<=2),"PASS  (1-2 calibers)","REVIEW  (want 1-2)"))', GOOD)
    s.blank()
    s.add([r("HOW TO USE: enter component masses as you design them. Watch the STATUS "
             "and Static margin rows. If STATUS reads FAIL, cut mass or revise the "
             "target before you cut material.", IT)])
    return s
def bom_sheet():
    s = Sheet("BOM", widths={0: 6, 1: 30, 2: 34, 3: 6, 4: 6, 5: 11, 6: 12,
                             7: 24, 8: 12, 9: 30},
              freeze="C3", autofilter="A2:J2")

    s.add([{"v": "BILL OF MATERIALS — estimate vs actual (required by competition CDR)", "s": T}])
    s.add(hdr(["#", "Item", "Specification", "Qty", "Spare",
               "Unit (INR)", "Estimate (INR)", "Supplier", "Actual (INR)", "Notes"]))

    items = [
        # -- Phase 1: strand burner + first motor
        ("Potassium nitrate", "14-0-45 fertiliser grade, 98-99%", 2, 0, 250, "Farm supply / agri store", "", "kg"),
        ("Sorbitol", "powder, food grade", 1, 0, 400, "Online / confectionery supplier", "", "kg"),
        ("SLES surfactant", "Sodium Laureth Sulfate 70-80%, 500 ml", 1, 0, 500, "Online", "", "casting aid, 0.1% by mass"),
        ("Coffee grinder", "for milling KN only — never food use after", 1, 0, 1200, "Local / online", "", ""),
        ("Deep fryer", "THERMOSTAT controlled, no exposed element", 1, 0, 2500, "Online", "", "safety-critical item"),
        ("Infrared thermometer", "-50 to 400 C", 1, 0, 900, "Online", "", "most convenient for casting"),
        ("Digital scale", "0.01 g resolution, 500 g capacity", 1, 0, 1500, "Online", "", "weighing accuracy is critical"),
        ("Silicone spatula", "for mixing and scooping", 2, 0, 150, "Local", "", ""),
        ("Dunk bucket", "water, mandatory whenever propellant present", 1, 0, 200, "Local", "", "SAFETY — mandatory"),
        ("Fire extinguisher", "CO2 or dry powder, 2 kg", 1, 0, 2000, "Local safety supplier", "", "SAFETY — mandatory"),
        ("Face shield", "full face, impact rated", 1, 0, 700, "Local safety supplier", "", "SAFETY — mandatory"),
        ("Safety goggles", "chemical splash type, sealed", 2, 0, 250, "Local safety supplier", "", "SAFETY — mandatory"),
        ("Heat resistant gloves", "leather or aramid", 2, 0, 500, "Local safety supplier", "", ""),
        ("Nitrile gloves", "box of 100", 1, 0, 400, "Local / online", "", ""),
        ("Ear defenders", "", 2, 0, 600, "Local safety supplier", "", ""),
        ("First aid kit", "incl. burn dressings and eyewash", 1, 0, 1200, "Pharmacy", "", "SAFETY — mandatory"),
        ("Kraft paper tube", "motor casing stock, assorted ID", 5, 0, 100, "Local / online", "", ""),
        ("Graphite rod", "nozzle stock, 20-25 mm dia", 1, 0, 800, "Online / industrial", "", ""),
        ("Drill bits", "1.5-3.0 mm, good quality (throat drilling)", 1, 0, 600, "Local", "", "throat accuracy drives chamber pressure"),
        ("Nichrome wire", "30 AWG", 1, 0, 300, "Online", "", "igniter bridgewire"),
        ("Charcoal", "natural wood only, NOT briquettes", 1, 0, 200, "Local", "", "for ignition powder"),
        ("Load cell", "5-20 kg, with HX711 amplifier", 1, 0, 800, "Online", "", "thrust measurement"),
        ("Pressure transducer", "0-10 MPa, strain gauge type", 1, 0, 3500, "Online / industrial", "", "single most valuable data"),
        ("Microcontroller", "Arduino Nano or ESP32", 2, 1, 500, "Online", "", ""),
        ("Jumper wires, breadboard", "", 1, 0, 400, "Online", "", ""),
        ("Steel tubing", "test stand / blast shield frame", 1, 0, 1500, "Local metal supplier", "", ""),
        ("Misc fasteners", "M3-M6 bolts, nuts, washers", 1, 0, 600, "Local", "", ""),
    ]
    for n, (name, spec, qty, spare, unit, supplier, actual, note) in enumerate(items, start=1):
        s.add([
            {"v": n, "s": CTR},
            {"v": name, "s": INPUT},
            {"v": spec, "s": LEFT},
            {"v": qty, "s": INPUT},
            {"v": spare, "s": INPUT},
            {"v": unit, "s": INPUT},
            {"f": f"IFERROR(D{n+2}*F{n+2},0)", "s": NUM2},
            {"v": supplier, "s": LEFT},
            {"v": actual if actual == "" else actual, "s": INPUT},
            {"v": note, "s": IT},
        ])

    last = len(items) + 2
    s.blank()
    s.add([{"v": "SUBTOTAL (estimate)", "s": B}, {"v": ""}, {"v": ""}, {"v": ""}, {"v": ""},
           {"v": ""}, {"f": f"SUM(G3:G{last})", "s": NUM2}])
    s.add([{"v": "SUBTOTAL (actual)", "s": B}, {"v": ""}, {"v": ""}, {"v": ""}, {"v": ""},
           {"v": ""}, {"v": ""}, {"v": ""}, {"f": f"SUM(I3:I{last})", "s": NUM2}])
    s.add([{"v": "Variance", "s": B}, {"v": ""}, {"v": ""}, {"v": ""}, {"v": ""},
           {"v": ""}, {"v": ""}, {"v": ""}, {"f": f"IFERROR(I{last+3}-G{last+2},0)", "s": NUM2}])
    s.add([{"v": "Contingency @ 15%", "s": B}, {"v": ""}, {"v": ""}, {"v": ""}, {"v": ""},
           {"v": ""}, {"f": f"G{last+2}*0.15", "s": NUM2}])
    s.add([{"v": "TOTAL WITH CONTINGENCY", "s": B}, {"v": ""}, {"v": ""}, {"v": ""}, {"v": ""},
           {"v": ""}, {"f": f"G{last+2}+G{last+5}", "s": NUM2}])
    return s


def bom_phases():
    s = Sheet("Budget Tiers", widths={0: 34, 1: 16, 2: 16, 3: 16, 4: 40})
    s.add([{"v": "BUDGET TIERS — what each level of funding actually buys", "s": T}])
    s.blank()
    s.add(hdr(["Item", "Lean (INR)", "Working (INR)", "Ambitious (INR)", "Notes"]))
    rows = [
        ("Safety equipment (non-negotiable)", 6000, 12000, 20000, "Never cut this line"),
        ("Strand burner + instrumentation", 3000, 8000, 15000, "Highest-value first build"),
        ("Motor materials (10 motors)", 4000, 10000, 25000, "consumables"),
        ("Static test stand", 4000, 12000, 25000, "load cell + structure"),
        ("Airframes (3 rockets)", 5000, 15000, 40000, "progressively harder"),
        ("Avionics + ground station", 8000, 25000, 60000, "heavily graded in competition"),
        ("Low-power commercial motors", 2000, 8000, 20000, "for the first flights"),
        ("Ground support / launch pad", 3000, 10000, 30000, "team-designed for competition"),
        ("Travel & test site logistics", 2000, 10000, 30000, ""),
        ("Contingency", 3000, 10000, 35000, ""),
    ]
    for i, (name, a, b, c, note) in enumerate(rows):
        s.add([{"v": name, "s": LEFT},
               {"v": a, "s": INPUT}, {"v": b, "s": INPUT}, {"v": c, "s": INPUT},
               {"v": note, "s": IT}])
    last = len(rows) + 3
    s.add([{"v": "TOTAL", "s": B}, {"f": f"SUM(B4:B{last})", "s": NUM2},
           {"f": f"SUM(C4:C{last})", "s": NUM2}, {"f": f"SUM(D4:D{last})", "s": NUM2}])
    s.blank()
    s.add([{"v": "REALITY CHECK", "s": SEC}])
    notes = [
        "The lean tier buys a strand burner, safety kit, and a handful of motors. It does NOT buy a flight campaign.",
        "The working tier is the realistic minimum for a first instrumented static fire and three small flights.",
        "The ambitious tier is what a competition attempt actually costs once you add the payload, motor and travel.",
        "IN-SPACe provides NO funding to competing teams. Registration is INR 10,000, plus INR 15,000 after the workshop.",
    ]
    for n in notes:
        s.add([{"v": n, "s": LEFT}])
    return s


# =============================================================================
# 3. MOTOR DESIGN CALCULATOR
# =============================================================================
def motor_design():
    """Motor design calculator. Row references are computed, not hard-coded."""
    s = Sheet("Motor Design", widths={0: 40, 1: 16, 2: 12, 3: 52}, freeze="A3")
    s.add([{"v": "KNSB MOTOR DESIGN CALCULATOR", "s": T}])                       # 1
    s.add([{"v": "MESA PROPELLANT WARNING: a single power law is NOT valid for KNSB across all "
                 "pressures. The a and n below apply ONLY within the pressure regime they were "
                 "measured in. Measure yours with a strand burner before trusting any output here.",
            "s": IT}])                                                            # 2
    s.blank()                                                                     # 3

    # ---- inputs: record the row each input lands on
    s.add(sec("PROPELLANT INPUTS"))                                               # 4
    inputs = [
        ("a", "Burn-rate coefficient a", 1.99, "mm/s/MPa^n",
         "PLACEHOLDER from a 2-point fit - REPLACE with strand-burner data", True),
        ("n", "Pressure exponent n", 0.30, "-",
         "PLACEHOLDER - must be measured per regime (target 0.3-0.6)", True),
        ("rho", "Propellant density", 1.841, "g/cm3",
         "verified ideal cast density (Nakka)", False),
        ("cstar", "Characteristic velocity c*", 900, "m/s",
         "from techsht-knsb ideal performance (pending)", True),
        ("Cd", "Discharge coefficient Cd", 0.95, "-", "typical value", False),
        ("Pc", "Target chamber pressure", 3.0, "MPa", "design point", True),
        ("It", "Target total impulse", 24, "N.s", "from flight mechanics", True),
        ("Dg", "Target grain OD", 24, "mm", "constrained by casing ID", True),
        ("port", "Target core port", 7, "mm", "sets port/throat ratio", True),
    ]
    R = {}
    for key, label, val, unit, note, is_input in inputs:
        R[key] = len(s.rows) + 1
        s.add([{"v": label, "s": B},
               {"v": val, "s": INPUT if is_input else D},
               {"v": unit, "s": IT},
               {"v": note, "s": IT}])
    s.blank()

    # ---- derived
    s.add(sec("DERIVED - geometry and performance"))
    mp_kg = f"($B${R['It']}/1000*1000)/($B${R['rho']}*1000)"   # not used directly
    derived = [
        ("Burn rate at target Pc",
         f"=$B${R['a']}*$B${R['Pc']}^$B${R['n']}", "mm/s", "r = a * Pc^n"),
        ("Grain cross-section area",
         f"=PI()/4*($B${R['Dg']}^2-$B${R['port']}^2)/100", "cm2",
         "annular area = pi/4 * (OD^2 - port^2)"),
        ("Propellant mass (g)",
         f"=$B${R['It']}/$B${R['cstar']}*1000", "g",
         "It / c*"),
        ("Grain volume required",
         f"=($B${R['It']}/$B${R['cstar']}*1000)/$B${R['rho']}", "cm3",
         "propellant mass (g) / density (g/cm3)"),
        ("Grain length",
         "=IFERROR(V_B19/V_B20*10,0)", "mm", "volume (cm3) / area (cm2) x 10 = mm"),
        ("Web thickness",
         f"=($B${R['Dg']}-$B${R['port']})/2", "mm", "(OD - port) / 2"),
        ("Burn time",
         "=IFERROR(V_B22/V_B18,0)", "s", "web / burn rate"),
        ("Average mass flow",
         "=IFERROR(V_mp/V_B23/1000,0)", "kg/s", "propellant mass (g) / burn time / 1000"),
        ("Required throat area",
         "=IFERROR(V_mdot*V_cstar/(V_Cd*V_Pc*1E6)*1E6,0)", "mm2", "mdot*c* / (Cd*Pc)"),
        ("Required throat diameter",
         "=IFERROR(SQRT(4*V_At/PI()),0)", "mm", "PRECISION PART - see notes"),
        ("Port / throat area at ignition",
         f"=IFERROR((PI()/4*$B${R['port']}^2)/V_At,0)", "-", "want >= 2"),
        ("Erosive burning check",
         '=IFERROR(IF(V_ratio>=2,"PASS","FAIL - increase port or throat"),"")', "-",
         "KNSB is prone to NEGATIVE erosive burning"),
    ]
    # resolve symbolic references now that we know each row number
    row_of = {}
    for label, formula, unit, note in derived:
        row_of[label] = len(s.rows) + 1
        s.add([{"v": label, "s": B}, {"v": None, "s": NUM2},
               {"v": unit, "s": IT}, {"v": note, "s": IT}])

    def sub(formula):
        """Replace symbolic V_ tokens with real B-cell references."""
        rep = {
            "V_B18": f"$B${row_of['Burn rate at target Pc']}",
            "V_B19": f"$B${row_of['Grain volume required']}",
            "V_B20": f"$B${row_of['Grain cross-section area']}",
            "V_B22": f"$B${row_of['Web thickness']}",
            "V_B23": f"$B${row_of['Burn time']}",
            "V_mp": f"$B${row_of['Propellant mass (g)']}",
            "V_mdot": f"$B${row_of['Average mass flow']}",
            "V_At": f"$B${row_of['Required throat area']}",
            "V_cstar": f"$B${R['cstar']}",
            "V_Cd": f"$B${R['Cd']}",
            "V_Pc": f"$B${R['Pc']}",
            "V_ratio": f"$B${row_of['Port / throat area at ignition']}",
        }
        for k, v in rep.items():
            formula = formula.replace(k, v)
        return formula

    for label, formula, unit, note in derived:
        rn = row_of[label]
        s.rows[rn - 1][1] = {"f": sub(formula)[1:], "s": NUM2}
    s.blank()

    s.add(sec("CRITICAL NOTES"))
    for n in [
        "Every output above is only as good as the measured a and n. A 2-point fit is NOT sufficient for a mesa propellant.",
        "Throat diameter is a precision part. A +/-0.1 mm error on a 2.2 mm throat is a +/-9% chamber pressure change.",
        "The grain must be FREESTANDING, not case-bonded - KNSB is weak in tension and strong in compression.",
        "Casing must burst at no more than 2.5x MEOP; absolute minimum design margin 1.5x.",
        "Prime all burning surfaces THINLY. A heavy primer coat causes delayed ignition.",
        "Do NOT use a burst diaphragm - documented cause of motor failure on Flight C-18.",
        "KNSB starts reluctantly because its low-pressure exponent sits near the bottom of the usable band.",
    ]:
        s.add([{"v": n, "s": LEFT}])
    return s


def static_test_log():
    s = Sheet("Test Log", widths={0: 8, 1: 12, 2: 12, 3: 12, 4: 12, 5: 12,
                                   6: 12, 7: 12, 8: 12, 9: 30},
              freeze="A3", autofilter="A2:J2")
    s.add([{"v": "STATIC TEST LOG — one row per motor fired", "s": T}])
    s.add(hdr(["Test #", "Date", "Grain batch", "Prop mass (g)",
               "Measured density", "Density ratio", "Peak Pc (MPa)",
               "Total impulse (N.s)", "Burn time (s)", "Outcome / anomalies"]))

    for i in range(3, 43):
        s.add([
            {"v": i - 2, "s": CTR},
            {"v": None, "s": INPUT},
            {"v": None, "s": INPUT},
            {"v": None, "s": INPUT},
            {"v": None, "s": INPUT},
            {"f": f"IFERROR(E{i}/1.841,\"\")", "s": NUM3},
            {"v": None, "s": INPUT},
            {"v": None, "s": INPUT},
            {"v": None, "s": INPUT},
            {"v": None, "s": LEFT},
        ])
    s.blank()
    s.add([{"v": "Density ratio target: >= 0.97. Below 0.95 indicates significant voids — do not fly.", "s": IT}])
    s.add([{"v": "Outcome codes: NOMINAL / CATO / NO-IGNITION / PARTIAL / ANOMALY", "s": IT}])
    return s


def grain_batch_log():
    s = Sheet("Grain Batches", widths={0: 12, 1: 12, 2: 12, 3: 12, 4: 12, 5: 12,
                                       6: 12, 7: 12, 8: 12, 9: 26},
              freeze="A3")
    s.add([{"v": "GRAIN BATCH RECORD — traceability for every grain cast", "s": T}])
    s.add(hdr(["Batch ID", "Cast date", "KN mass (g)", "Sorbitol (g)",
               "Cast temp (C)", "Cure days", "Grain mass (g)", "Density (g/cc)",
               "Tap test", "Notes / defects"]))
    for _ in range(3, 33):
        s.add([{"v": None, "s": INPUT} for _ in range(6)] +
              [{"v": None, "s": INPUT},
               {"v": None, "s": INPUT},
               {"v": None, "s": INPUT},
               {"v": None, "s": LEFT}])
    s.blank()
    s.add([{"v": "Kn mass : Sorbitol must be 65 : 35 by mass. Record actual weighed masses, not targets.", "s": IT}])
    s.add([{"v": "Tap test: every tap around the inhibitor must sound identical. Reject any grain that differs from its batch-mates.", "s": IT}])
    return s


# =============================================================================
# BUILD
# =============================================================================
def main():
    made = []

    p = os.path.join(ROOT, "20_AEROSTRUCTURES", "Mass_Budget_and_CG.xlsx")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    write_xlsx(p, [mass_budget_v2()])
    made.append(p)

    p = os.path.join(ROOT, "00_ADMINISTRATION", "BOM_and_Budget.xlsx")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    write_xlsx(p, [bom_sheet(), bom_phases()])
    made.append(p)

    p = os.path.join(ROOT, "10_PROPULSION", "Motor_Design_Calculator.xlsx")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    write_xlsx(p, [motor_design()])
    made.append(p)

    p = os.path.join(ROOT, "60_TEST_DATA", "Static_Test_Log.xlsx")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    write_xlsx(p, [static_test_log(), grain_batch_log()])
    made.append(p)

    for m in made:
        print(f"OK  {os.path.getsize(m):>7} B  {m}")


if __name__ == "__main__":
    main()
