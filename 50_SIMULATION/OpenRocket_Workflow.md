# OpenRocket Workflow — From Zero to a Trustworthy Simulation

**UVCE Rocketry Club, Bengaluru — Simulation Guide 1 of 3**

| Companion documents | What they cover |
|---|---|
| [Motor_Files.md](Motor_Files.md) | `.eng` / `.rse` motor files, static-fire data reduction, motor classes |
| [Simulation_Plan_and_Validation.md](Simulation_Plan_and_Validation.md) | Error sources, off-nominal cases, dispersion, design-review checklist |

**Who this is for:** a club member who has never opened a rocket simulator. No prior
knowledge of aerodynamics, Java, or file formats is assumed. By the end you should be able
to build a small solid-motor rocket in OpenRocket, enter your own KNSB motor, run a
simulation, and know whether the answer is believable or nonsense.

**Flight programme this guide supports**

| Stage | Motor | Target apogee | New skills needed |
|---|---|---|---|
| 0 | Commercial A–D (if available) | 30–80 m | Build the model, read the outputs |
| **1** | **Club KNSB, ~10–25 N·s (D/E class)** | **100–200 m** | **Custom motor files, rail exit check, mass discipline** |
| 2 | KNSB F/G class, 40–160 N·s | 300–600 m | Dual deployment, tracking, dispersion analysis |
| 3 | Commercial/ammonium-perchlorate H+ | 1 km+ | Certification, waivers, RASAero/RocketPy, structural analysis |

Everything in Stage 1 is covered here. Stage 2 and 3 additions are flagged as you go.

> **Safety and permissions come first.** This document is about software. Before any
> flight, check the club's own SOPs, the launch site's rules, local district/police
> permission, and the current [IN-SPACe](https://www.inspace.gov.in/) authorisation
> requirements for your activity. Bengaluru is surrounded by controlled airspace
> (Kempegowda International, HAL, Yelahanka) — site selection and notification are not
> optional. Software never makes a flight legal or safe on its own.

---

## 1. What OpenRocket is

OpenRocket is a **free, open-source** rocket design and flight simulation program. It is
the standard starting point for student and amateur teams worldwide.

Key facts:

- **Licence:** open source (GPL). Free forever, no licence key, no student trial.
- **Language:** written in **Java**. That means it needs a **Java runtime** on your
  computer (see §2). Java is free and takes five minutes to install.
- **Platforms:** runs on **Windows, macOS and Linux**. Because it is Java, the same
  program works on all three; only the installer differs.
- **What it does:** 3D flight simulation (the trajectory plus the rocket's attitude, so
  wind and weathercocking are modelled), the Barrowman centre-of-pressure method with
  extended corrections, a semi-empirical drag build-up, mass and CG bookkeeping, motor
  thrust-curve modelling, staging, and recovery-device simulation.
- **Home page / downloads:** `openrocket.info` (also mirrored on GitHub under
  `openrocket/openrocket`).
- **File format:** designs are saved as `.ork` files. These are ZIP archives of XML — they
  are small, diff-able in principle, and safe to email or keep in Git.
- **Versions you will meet:**
  - **15.03** — the long-standing release from 2015 that most old tutorials use. Needs Java 8+.
  - **22.02** — modernised UI, added **Monte Carlo simulation**, rail buttons, shock cords,
    better motor handling. Needs Java 11+.
  - **23.09 and later** — current line, requires **Java 17**, larger UI and model updates.
  - Advice: **install the newest version you can**, but when you share a `.ork` file with
    the club, write down which version produced it. Screenshots in this guide are
    described in words precisely because labels move between versions.

**What OpenRocket does not do:** it does not validate your glue joints, it does not know
your real Cd, it does not model your ejection charge, it does not know the wind at your
field today, and it does not check whether your parachute was packed properly. Treat it as
a very good calculator that is only as honest as the numbers you type in.

---

## 2. Installing OpenRocket

### 2.1 The Java question, in plain language

OpenRocket is not a normal double-click program in the way Word is; it is a Java
application. There are two ways to get it running:

1. **Bundled installer (easiest).** The Windows `.exe`/`.msi` and macOS `.dmg` downloads
   from `openrocket.info` **include their own Java runtime**. You install one file and you
   are done. Use this if it is available for your version.
2. **The `.jar` file (universal).** A `.jar` is the program itself without Java. You must
   install Java first, then open the `.jar`. This is the route for Linux, for old
   machines, and for the latest version.

If you ever see an error like *"Java not found"*, *"To open OpenRocket you need a Java
runtime"*, or a window that flashes and closes, you took route 2 without Java. Fix: install
Java (§2.2/§2.3) or use the bundled installer.

### 2.2 macOS

**Option A — disk image with bundled Java (recommended)**

1. Go to `openrocket.info` → **Download / Get OpenRocket**.
2. Download the macOS `.dmg` (choose the Apple Silicon build if offered and your Mac is
   M1/M2/M3/M4; the installer usually handles both).
3. Open the `.dmg`, drag **OpenRocket** into **Applications**.
4. First launch: if macOS says the app is from an unidentified developer, open
   **System Settings → Privacy & Security**, scroll to the message about OpenRocket and
   click **Open Anyway**. (You can also right-click the app → **Open** → **Open**.) You
   only do this once.

**Option B — `.jar` plus Java**

1. Install a free OpenJDK build such as **Eclipse Temurin** (`adoptium.net`). Pick the
   **macOS / aarch64** package for Apple Silicon, or **macOS / x64** for Intel. Install the
   `.pkg`.
2. Alternatively, with Homebrew installed:
   `brew install --cask temurin`
3. Verify in **Terminal**: `java -version` should print a version 17 or newer for
   OpenRocket 23.09+.
4. Download the **Generic `.jar`** from `openrocket.info`.
5. Run it from Terminal:
   `java -jar ~/Downloads/OpenRocket-23.09.jar`
   (Adjust the version number to the file you actually downloaded.) Keep the `.jar` in a
   permanent folder such as `~/Applications/` rather than `Downloads`.

### 2.3 Windows

**Option A — installer with bundled Java (recommended)**

1. Go to `openrocket.info` → **Download**.
2. Download the Windows installer (`.exe` or `.msi`).
3. Run it. If **Windows SmartScreen** warns about an unrecognised app, click
   **More info → Run anyway**. This is normal for small open-source projects.
4. Launch OpenRocket from the Start menu.

**Option B — `.jar` plus Java**

1. Install **Eclipse Temurin** from `adoptium.net`: choose **Windows / x64** (or ARM64 on
   a Snapdragon laptop) and run the `.msi`.
2. Verify: open **Command Prompt** and type `java -version`. If Windows does not know the
   command, the installer needs the "Set JAVA_HOME" / "Add to PATH" option enabled — rerun
   the installer and enable it.
3. Download the **Generic `.jar`** from `openrocket.info`.
4. Create a folder such as `C:\OpenRocket\` and move the `.jar` there.
5. Double-click the `.jar` (if Java is registered as the handler) or run:
   `java -jar "%USERPROFILE%\Downloads\OpenRocket-23.09.jar"`

### 2.4 Linux

Use the **Generic `.jar`** (or an AppImage if your distribution's page offers one), then
either run `java -jar OpenRocket-<version>.jar` or create a desktop launcher. OpenRocket
behaves well under Wayland/X11 with a modern OpenJDK 17+.

### 2.5 First-launch sanity check

Do this once, before you build anything:

1. Open OpenRocket. You should see an empty design view and a part tree containing just
   **Rocket**.
2. Open the example rockets: **File → Open example** (or open the `examples/` folder that
   ships with the program) and load a simple single-stage design. Any version ships a few.
3. Go to the **Flight simulations** tab and run the existing simulation (a green "play" /
   **Run simulations** button, or right-click the simulation → **Run**).
4. Double-click the finished simulation to open the results. If you see a table of numbers
   with an apogee and a plot, **your installation is correct**.
5. Close the example **without saving over it**.

### 2.6 Preferences worth setting on day one

Look under **Edit → Preferences** (on macOS, the menu may be under **OpenRocket →
Settings/Preferences**). Settings that matter to us:

- **Units:** set everything to **metric (SI)** — metres, millimetres, grams/kilograms,
  m/s, °C, hPa/mbar. Mixed units are the number one source of silent factor-of-1000 errors.
- **Motors / thrust curves:** there is a page listing the folders OpenRocket searches for
  `.eng` and `.rse` motor files, with buttons to add a folder. Point it at the club's
  shared motor folder (for us: `50_SIMULATION/motors/`). See
  [Motor_Files.md](Motor_Files.md).
- **Graphics/3D:** if the program feels slow on an old laptop, reduce the 3D view quality.
- **Auto-save / backup:** enable regular backup if your version offers it. Simulation work
  is hours of your life.

---

## 3. The interface, laid out in words

OpenRocket's main window is a set of tabs across the top, with different tools inside
each. The names below match recent versions; a few labels moved between 15.03 and 23.09,
so if a name does not match exactly, look for the equivalent in the same area of the
window.

### 3.1 The two top-level tabs you will live in

1. **Rocket design** — where the rocket is built and where its mass, CG and stability are
   shown. Contains the part tree, the rocket figure, and the component configuration panel.
2. **Flight simulations** — where simulations are created, configured and run, and where
   their results are stored. Also contains the **Motors & Configuration** style controls
   that tie motors to the design (in some versions this appears as a tab inside the design
   view instead).

### 3.2 The part tree (left side of the design view)

The **part tree** is a nested list of every object in the rocket. It is a hierarchy, not a
list — components are *inside* their parent, and that nesting is what makes the mass and
CG calculation correct. Typical nesting:

```
Rocket
└── Stage (Sustainer)
    ├── Nose cone
    └── Body tube
        ├── Inner tube        ← the motor mount
        │   └── Centring ring  (rings usually attach to the body tube, not the tube)
        ├── Fin set
        ├── Launch lug
        ├── Parachute
        ├── Mass component
        └── ...
```

Rules of the tree:

- **Selecting** a component shows its parameters in the configuration panel on the right.
- **Right-clicking** a component opens a context menu with an **Add** submenu; the toolbar
  above the tree usually has the same "add component" actions. Only physically sensible
  children are offered, which is OpenRocket's way of stopping you from putting a nose cone
  inside a fin.
- **Double-clicking** a name renames it. **Rename everything** ("Main chute 450 mm",
  "Avionics + battery", "Nose weight") — future-you will thank present-you.
- **Dragging** a component re-parents it. This is how you move a mass component from the
  body tube into the nose cone.
- Deleting is **Delete/Backspace** or right-click → **Delete**.

### 3.3 The configuration panel (right side / lower area)

This is a tabbed form showing the parameters of whatever is selected in the tree. The tabs
are broadly consistent across component types:

| Tab | What lives there |
|---|---|
| **Design** (sometimes the main tab) | Geometry: lengths, diameters, thicknesses, positions, shapes, materials, surface finish |
| **Shoulder** | Only for nose cones and transitions: the part that slides inside the tube |
| **Motor** | Only for a motor-mount inner tube: motor selection, delay override, ignition settings |
| **Deployment** | Only for parachutes/streamers: what triggers deployment and any delay |
| **Override** | **Override mass** and **Override CG** checkboxes with value fields — the most important tab in this guide (§9) |
| **Appearance** | Colour, opacity, texture — cosmetic, but used by the photo studio and 3D view |

Two habits:

1. Watch the **"Automatic"** checkboxes. Many diameter fields default to *Automatic*,
   meaning "inherit from the parent". That is usually right; it is wrong when you are
   modelling a tube that is deliberately a different diameter.
2. When a number does not seem to change anything, check whether you edited the parent
   instead of the child.

### 3.4 The rocket figure and the stability readout

The centre of the design view draws the rocket to scale, with the **CG** (centre of
gravity) and **CP** (centre of pressure) marked, usually as two coloured dots or
crosshairs with a dimension between them. Below or beside the figure there is a summary
line giving something like:

```
Stability: 1.62 cal     CG: 41.3 cm     CP: 51.1 cm     Mass: 0.274 kg
```

(Exact wording and which numbers are shown vary by version.) Read this constantly. **"cal"
means calibers, i.e. multiples of the body tube's maximum diameter** — the standard measure
of static stability (§8.5).

The **3D view** (a tab, button or View-menu item in the design view) lets you orbit the
model. It is a good way to catch a fin that is 200 mm away from where you thought it was.
The **View** menu also has zoom and fit controls, and the figure can usually be toggled
between a shaded and a wireframe/outline style.

### 3.5 The simulation panel

Go to the **Flight simulations** tab. You get a **table of simulations**, one row each:

| Column (typical) | Meaning |
|---|---|
| Name | Your label, e.g. "Nominal E19, no wind" |
| Configuration | Which motor/configuration set it uses |
| Launch conditions | Summarised rod length/angle/wind |
| Apogee, Max velocity, Max Mach, Max acceleration, Flight time, Ground hit velocity | Results, filled in after the run |
| Warnings | A yellow/red marker if something about the run is suspicious |

Buttons in this area typically include **New simulation**, **Run simulations**, **Edit**,
**Delete**, **Export**, and plot/analyse actions. Right-clicking a row usually offers the
same actions as the buttons.

### 3.6 Menus worth knowing

- **File** — new/open/save `.ork`, open example designs, import from other tools.
- **Edit** — undo/redo and **Preferences**.
- **View** — zoom, fit, view style (2D/3D).
- **Rocket** (in some versions) — actions on the currently selected rocket object.
- **Tools** — the analysis power tools: **Component analysis**, **Component optimization**,
  **Component sizing**, and **Photo studio** (renders a nice picture of your rocket for the
  design-review document). These are advanced; visit them once you are comfortable with the
  basics. Component analysis, in particular, breaks the drag down into friction, pressure,
  base and fin contributions — genuinely useful when you cannot work out where the drag is
  coming from.
- **Help** — version info, and a link to the documentation/wiki.

---

## 4. The part tree of a typical single-stage rocket

Below is the tree for a real, flyable, single-stage, single-motor, parachute-recovery
rocket — the kind of thing Stage 1 requires — with what each part *is* physically and why
the simulator needs it.

```
Rocket                                    (the whole vehicle; global settings)
└── Stage: "Sustainer"                    (one stage; multi-stage adds more)
    ├── Nose cone: "NC-66 ogive"          (aerodynamic front, hollow, carries nose weight)
    ├── Body tube: "BT-66 x 550"          (the airframe; everything else hangs off it)
    │   ├── Inner tube: "MMT-24"          (motor mount tube; holds the motor)
    │   │   └── (motor is selected here, not a part in the tree)
    │   ├── Inner tube: "Stuffer/AV bay"  (optional second tube for electronics)
    │   ├── Centring ring: "CR fwd"       (centres the MMT in the airframe)
    │   ├── Centring ring: "CR aft"       (also acts as the thrust ring)
    │   ├── Engine block: "Thrust ring"   (stops the motor moving forward — optional if the
    │   │                                  aft centring ring does the job)
    │   ├── Fin set: "3x trapezoid"       (stabilisers; usually one fin set object = all fins)
    │   ├── Launch lug: "LL-6"            (slides on the rod/rail)
    │   ├── Rail button: "RB x2"          (alternative to a lug for a rail launcher)
    │   ├── Parachute: "Main 450 mm"      (recovery device)
    │   ├── Shock cord: "4 m tubular"     (connects the two halves; mass matters)
    │   ├── Mass component: "Avionics"     (your electronics, as a lump of mass)
    │   ├── Mass component: "Motor casing" (only if you are not letting the motor file do it)
    │   ├── Mass component: "Recovery hw"  (quick links, blanket, wadding)
    │   └── Mass component: "Paint+glue"   (the mass everybody forgets)
    └── Stage: "Booster" (Stage 2+ only)
```

Component-by-component notes:

| Component | Physics it represents | Notes that bite beginners |
|---|---|---|
| **Nose cone** | Forebody drag, and a big chunk of the CG position | Its *shoulder* length is hidden inside the tube and adds mass; the nose weight is a separate **mass component** inside the cone, not a nose-cone parameter |
| **Body tube** | Skin friction drag, base drag at the aft end, internal volume | Wall thickness × material sets the mass. Change the material and the mass changes silently |
| **Transition** | A diameter change (boat-tail, reducer) | Adds pressure drag unless it is a smooth taper; check the "shape" and the fore/aft diameters |
| **Inner tube** | The motor mount (and stuffer tubes / electronics bays) | The inner tube must be **marked as a motor mount** for the motor tab to appear. Its diameter must match the motor's diameter or the motor will not fit the mount |
| **Centring ring** | Structural: centres the motor mount, transfers thrust | Each ring is a thin annulus: you give it a length (=thickness), an outer diameter and an inner diameter. Two rings per mount is normal |
| **Engine block** | The forward thrust ring that stops the motor climbing the tube | Optional; the aft centring ring plus the motor's own thrust ring often does the job |
| **Fin set** | Stability (moves the CP aft) and a large share of the drag | One fin-set object makes *N* identical fins. Fin **cant angle** makes the rocket spin. Fin **cross-section** (square/rounded/airfoil) changes the drag noticeably |
| **Launch lug** | The thing that keeps the rocket straight for the first metre | Easy to forget; also contributes drag and mass. A rocket with no lug cannot be modelled as leaving a rail |
| **Rail button** | Same job, for a rail launcher | Available in newer versions; model it as a small cylinder or use the dedicated component |
| **Parachute / streamer** | Descent rate and landing velocity | Diameter **and** Cd both matter. The packed size affects whether it fits |
| **Shock cord** | Mass, and the recovery train's layout | Small but real mass; same for the heat shield/blanket |
| **Mass component** | Anything that is not geometry: avionics, battery, ballast, hardware, paint | The single most useful component in the whole program (§9) |

**Motor mount bookkeeping.** OpenRocket does not have a "motor" part in the tree. You
select a motor *on the inner tube that is marked as the motor mount*, and OpenRocket then
adds that motor's mass, CG and thrust to the vehicle automatically. If you also add a "motor
casing" mass component while the motor file already includes case mass, you have
double-counted. Read the motor file's mass fields (see
[Motor_Files.md](Motor_Files.md)) before deciding.

---

## 5. Build your first rocket, step by step

### 5.0 The reference rocket: "UVCE-S1 Trainer"

We will build one specific rocket so every parameter below is concrete. These are
**starting values** — real builds use whatever tube you can actually buy, so treat the
diameter as adaptable.

| Parameter | Value | Why |
|---|---|---|
| Class / role | Single stage, single motor, parachute recovery | Simplest thing that flies |
| Airframe OD | 66 mm | Big enough to be easy to work with, small enough to be light |
| Overall length | ~780 mm | Length/diameter ≈ 12 — comfortably stable |
| Target apogee | 100–200 m | Stage 1 goal |
| Motor | Club KNSB, 24 mm, ~24.6 N·s (E class), plugged + electronic deploy, or with a delay grain | See [Motor_Files.md](Motor_Files.md) |
| Liftoff mass target | 0.26–0.30 kg | Sets the apogee; weigh it, do not guess |
| Fins | 3 × trapezoidal, plywood 4 mm | Stable, cheap, easy to align |
| Recovery | Single 450 mm flat chute, ~5–6 m/s descent | Fits the field |
| Rail | 2 m rail or 1.5 m rod | Needed for rail exit velocity (§8.5) |

**Geometry to enter**

| Part | Field | Value |
|---|---|---|
| Nose cone | Shape | Ogive |
| | Length | 140 mm |
| | Base diameter | 66 mm (Automatic from the body tube, if it offers that) |
| | Thickness | 2 mm |
| | Shoulder length | 30 mm |
| | Shoulder diameter | 64 mm (2 mm under the tube ID, so it fits inside) |
| Body tube | Outer diameter | 66 mm |
| | Length | 550 mm |
| | Thickness | 0.6 mm (thin kraft — if you use thicker tube, re-weigh) |
| | Material | Paper/kraft, or your actual tube material |
| Motor mount (inner tube) | Outer diameter | 25 mm |
| | Inner diameter | 24 mm |
| | Length | 120 mm |
| | Axial offset (from the tube's fore end) | 410 mm (i.e. the mount's aft end is flush with the body tube's aft end) |
| | "Motor mount" flag | **On** |
| Centring rings (×2) | Outer diameter | 66 mm (to match the tube ID) |
| | Inner diameter | 25 mm |
| | Length (= thickness) | 6 mm |
| | Axial offsets | 415 mm and 520 mm from the tube's fore end |
| Fin set | Number of fins | 3 |
| | Root chord | 90 mm |
| | Tip chord | 45 mm |
| | Sweep length | 55 mm |
| | Height (span) | 70 mm |
| | Thickness | 4 mm |
| | Cross section | Rounded or airfoil (square is draggier) |
| | Position | Relative to the **bottom** of the parent body tube, axial offset 0 (fins flush with the aft end) |
| Launch lug | Length | 60 mm |
| | Outer diameter | 7 mm |
| | Inner diameter | 6 mm |
| | Axial offset from the tube's fore end | 300 mm |
| Parachute | Diameter | 450 mm |
| | Drag coefficient | 0.8 (default; correct it after your first flight, §9/Validation guide) |
| | Shroud lines | 6 lines × 500 mm |
| | Deployment | Ejection charge (or Apogee, if you are modelling electronic deploy) |

### 5.1 Create the design and the first stage

1. **File → New**. You get a bare `Rocket`.
2. The rocket already contains one **Stage**. Rename it "Sustainer".
3. **Save immediately** as `UVCE-S1_rev-A.ork` in a folder such as
   `50_SIMULATION/designs/`. Save after every few edits. OpenRocket has no autosave you can
   rely on.

### 5.2 Nose cone

1. Select the **Stage**, right-click → **Add → Nose cone** (or use the toolbar's add
   button).
2. On the **Design** tab enter the shape, length, base diameter and thickness from the
   table above. If the base-diameter field has an **Automatic** checkbox, tick it — then
   the cone always matches the tube.
3. On the **Shoulder** tab enter the shoulder length and diameter. Get this wrong and the
   nose cone either falls out or will not fit.
4. Add the nose weight: right-click the **Nose cone** → **Add → Mass component**. Name it
   "Nose weight", mass **20 g**. Put its **axial offset** near the tip (e.g. 30 mm from the
   cone's fore end) because a nose weight at the tip does far more for stability than the
   same mass at the shoulder.
5. Watch the CG marker move forward as you do this. That is the entire point of nose weight.

### 5.3 Body tube

1. Select the **Stage** → **Add → Body tube**. Enter OD, length, thickness and material.
2. Check the resulting **mass** in the summary line or the component's mass display. If the
   number is wildly different from the tube you can buy (a 550 mm long, 66 mm kraft tube is
   roughly 50–70 g), your material density or thickness is wrong. Fix it now, or **override
   the mass** with the real measured value (§9).

### 5.4 Motor mount inner tube

1. Select the **Body tube** → **Add → Inner tube**. Enter OD 25 mm, ID 24 mm, length
   120 mm, axial offset 410 mm.
2. Make sure the **"motor mount"** option is enabled (a checkbox on the inner tube's
   design/motor tab, wording varies). A new **Motor** tab appears.
3. Leave the motor selection empty for now; we do that after importing our motor (§6).

### 5.5 Centring rings

Add two **Centring ring** components inside the **Body tube** with the dimensions in the
table. Note the fields are *length* (= ring thickness), *outer diameter*, *inner diameter*
and *axial offset*. If you set the inner diameter smaller than the motor's outer diameter,
the motor physically cannot fit — OpenRocket will still happily simulate it, which is
exactly the kind of mistake the software cannot catch for you.

### 5.6 Thrust ring / engine block (optional)

Add an **Engine block** (or a very short inner tube) just forward of the motor's forward
end so the motor cannot climb the tube under thrust. On many club motors the motor's own
forward closure and the friction fit do this job, but the simulator should include whatever
you actually build.

### 5.7 Fin set

1. Select the **Body tube** → **Add → Fin set → Trapezoidal** (the other shapes —
   elliptical, freeform — are available too).
2. Enter the fin parameters from the table.
3. Set **position relative to the bottom of the parent** and axial offset 0 so the fin's
   root trailing edge lines up with the tube's aft end. This is the usual arrangement and
   puts the fins as far aft as possible, which maximises stability.
4. Two structural checks the simulator can hint at but not decide for you:
   - **Fin flutter.** Thin, large fins on fast rockets flutter and shed. As a rule of
     thumb, plywood fins of 4 mm are fine at the 60–100 m/s our Stage 1 rockets reach;
     above ~200 m/s, use thicker G10/fibreglass and do a proper flutter calculation.
   - **Fin root attachment.** The fillet is not modelled, but it is what actually holds
     the fin on. Add its mass as a mass component near the aft end.

### 5.8 Launch lug (or rail buttons)

Add a **Launch lug** inside the **body tube**, length 60 mm, OD 7 mm, ID 6 mm, positioned so
that it is on the tube's surface (OpenRocket places lugs against the parent tube
automatically). For a rail launcher, add **Rail buttons** instead (newer versions have a
dedicated component). Do not skip this: it affects drag, mass, and — more importantly —
OpenRocket will not be able to tell you the rail exit velocity honestly unless the launch
interface exists in the model.

*Practical detail:* the lug must be long enough and positioned so the rocket is still
guided when the centre of gravity has passed the top of the rod. A lug well forward of the
CG plus a 2 m rail is the standard solution.

### 5.9 Parachute, shock cord and recovery hardware

1. Select the **Body tube** → **Add → Parachute**. Diameter 450 mm, Cd 0.8, 6 shroud lines
   of 500 mm.
2. On the **Deployment** tab choose the trigger. For Stage 1 with a motor delay, use
   *ejection charge*; if you are flying electronic apogee deployment, use *apogee* (and, in
   newer versions, an altitude trigger is available for dual deployment in Stage 2).
3. Add a **Shock cord** (if your version has it) or a **Mass component** named "Shock cord +
blanket + links" with the real weighed mass, roughly **30–35 g** for 4 m of tubular nylon,
a heat blanket and two quick links.
4. Check the packed size: the parachute's packed diameter/length fields exist so you can
   confirm it fits in the tube. OpenRocket will warn if it does not, but do the physical
   check too.

### 5.10 Mass components: avionics, casing, paint

Add these now, not later. See §9 for the full method. For UVCE-S1:

| Mass component | Place it | Mass |
|---|---|---|
| Nose weight | In the nose cone | 20 g (adjust to set your stability) |
| Avionics (logger / altimeter + sled + battery) | In the body tube, forward of the motor mount | 25–40 g |
| Recovery hardware (cord, blanket, links, wadding) | In the body tube | 30–35 g |
| Paint, primer, epoxy fillets, glue | Spread along the tube (put it at the tube's mid-point) | 15–20 g |
| Motor casing | **Do not add** if your motor file already includes case mass | 0 g |

### 5.11 Check stability, then iterate

Look at the stability line under the rocket figure. You want **1.0–2.0 calibers** for a
first flight; 1.5 is a comfortable target.

- Too little (under 1.0): add nose weight or make the fins bigger/more aft.
- Too much (over 2.0): remove nose weight, or move mass aft. Over-stable rockets
  weathercock into the wind and fly a curved, lower, less predictable path (§8.5).

Change one thing at a time and watch the CG/CP markers move. That feedback loop — nudge,
read, nudge — is the core of rocket design, and it costs nothing in software.

### 5.12 Write down the mass budget

Keep this table in your design log and update it with **weighed** values as the build
progresses:

| Item | Estimated (g) | Weighed (g) | Where in the model |
|---|---|---|---|
| Nose cone + shoulder | 22 | | Nose cone, override mass |
| Nose weight | 20 | | Mass component |
| Body tube | 55 | | Body tube, override mass |
| Fins (3) | 27 | | Fin set, override mass |
| Epoxy fillets | 6 | | Mass component near the aft end |
| Motor mount + 2 rings | 18 | | Inner tube + rings |
| Launch lug | 3 | | Launch lug |
| Parachute + cord + hardware + blanket | 35 | | Parachute + mass component |
| Paint, primer, glue | 20 | | Mass component at mid-tube |
| Avionics | 25 | | Mass component |
| **Dry total** | **231** | | |
| Motor loaded (E19) | 68 | | Motor file |
| **Liftoff total** | **299 g** | | |

### 5.13 Hand-check before you trust the simulator

Do this once per design. It takes two minutes and catches gross errors.

1. **Rough burnout velocity:**
   `Δv ≈ I_total / m_liftoff − g·t_burn/2`
   For UVCE-S1: `24.6 / 0.299 − 9.81 × 1.30 / 2 = 82 − 6.4 ≈ 76 m/s` (upper bound — ignores drag).
2. **Rough apogee:** `h ≈ v²/(2g) + h_burnout`
   `76² / 19.62 ≈ 294 m + ~20 m ≈ 314 m`. This is the **no-drag ceiling**. Real apogee will
   be much lower, typically 50–70 % of it for a 66 mm rocket at these speeds, i.e.
   **150–220 m**. If OpenRocket says 900 m, something is wrong with your inputs (usually
   the mass or the motor).
3. **Thrust-to-weight:** `F_avg / (m·g) = 19 / (0.299 × 9.81) = 6.5` — fine (want ≥ 5).
4. **Rail exit:** `v = √(2·a·L)` with `a = (F_avg − m·g)/m`.
   `a = (19 − 2.93)/0.299 = 53.7 m/s²`; on a 2 m rail `v = √(2 × 53.7 × 2) = 14.7 m/s`.
   That is only just acceptable (§8.5) — a real design driver for low-thrust KNSB motors.

Write these four numbers in the log. When the simulation disagrees by more than about
30 %, find out why before flying.

---

## 6. Entering a custom motor

### 6.1 Why bother

No commercial motor database contains your club's KNSB motor. If you simulate with a
"similar" commercial motor you are simulating a different rocket. Full details, file
formats and the static-fire reduction procedure are in
[Motor_Files.md](Motor_Files.md); this section is the minimum you need to keep moving.

### 6.2 Parts of a motor you must know before you simulate

| Quantity | Symbol | Where it comes from |
|---|---|---|
| Total impulse | `I_total` (N·s) | Area under the thrust curve; sets the motor class letter |
| Average thrust | `F_avg` (N) | `I_total / burn time`; the number in the motor's name |
| Peak thrust | `F_peak` (N) | Highest point of the curve; sets your structural and rail-exit case |
| Burn time | `t_burn` (s) | Length of the thrust curve |
| Propellant mass | `m_prop` (g) | Weigh the grain before and after the static fire |
| Total motor mass | `m_total` (g) | Weigh the loaded motor before the fire (case + propellant + hardware) |
| Delay(s) | s, or "P" for plugged | Your delay grain, or electronic deployment |
| Delivered specific impulse | `Isp ≈ I_total / (m_prop·g)` | A **sanity check**: KNSB lands at roughly 100–130 s. 400 s means a broken load-cell calibration |

### 6.3 The `.eng` file in 30 seconds

A RASP `.eng` file is a plain text file (make it in Notepad, TextEdit in plain-text mode,
or VS Code — **not** Word). The structure is:

```
; comments start with a semicolon
; designation  diameter(mm)  length(mm)  delays  prop mass(g)  total mass(g)  manufacturer
E19KNSB        24           100         P       20.0           68.0           UVCE Rocketry
; then time (s) and thrust (N) pairs, one per line, time always increasing
0.00   0.0
0.04   6.0
...
1.30   0.0
```

The last point must be a **zero-thrust point at the end of the burn**, otherwise OpenRocket
thinks the motor is still burning.

### 6.4 Worked example: the club's 24 mm KNSB "E19"

This is the measured-and-reduced curve for the club's standard 24 mm KNSB motor: 20 g of
propellant, 24.6 N·s total impulse, 19 N average thrust, 1.30 s burn, plugged forward
closure (electronic deployment). Save as `50_SIMULATION/motors/E19KNSB.eng`:

```
; UVCE Rocketry Club - 24 mm KNSB motor
; File: E19KNSB.eng    revision: 2025-03-a
; Reduced from static fire SF-2025-03-02 (load cell, 1 kHz, 10 kg cell)
; Propellant: KNSB 65/35, 20.0 g grain, 24 mm OD, 9 mm core, 30 mm long
; Total impulse 24.6 N.s | Average thrust 19.0 N | Burn 1.30 s | Isp 126 s
; Delays: P = plugged (no ejection charge; use electronic deployment)
; ---------------------------------------------------------------
; designation  dia  len  delays  propMass  totalMass  manufacturer
E19KNSB        24   100  P       20.0      68.0       UVCE Rocketry
; time(s)  thrust(N)
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

That is 13 data points — enough, because each point sits where the curve changes slope.
More points are not automatically better; wrongly placed points are worse.

> **Units warning.** The mass fields in `.eng` files are the classic trap: files in the
> wild use **both grams and kilograms** for the same two fields. Write your file, import
> it, and then **look at the mass OpenRocket reports for the motor**. For this motor it
> must say approximately 20 g of propellant and 68 g total. If it says 0.02 g, or 20 000 g,
> your file's units were misread: swap between grams and kilograms, re-import, and check
> again. Never fly a motor file you have not visually verified. (If you want units that
> cannot be misread, use the XML `.rse` format instead — [Motor_Files.md](Motor_Files.md).)

### 6.5 Importing it

1. Put the `.eng` file in a folder, e.g. `50_SIMULATION/motors/`.
2. **Edit → Preferences → Motors** (name varies): add that folder to the list of thrust-curve
   directories. OpenRocket scans the folder at startup.
3. Alternative/additional route: **Motor selection dialog** (opened from the motor-mount
   inner tube's **Motor** tab, or from the **Motors & Configuration** area) — there is
   usually a button such as **Import motor** / **Load motor file** / **New motor** in that
   dialog. Use whichever your version offers.
4. Restart OpenRocket if the new motor does not appear; folder-scanning happens at startup
   in most versions.
5. Search the motor list for `E19KNSB` and **check the reported mass, total impulse and
   average thrust** against §6.4. These three numbers are your proof the file imported
   correctly.

### 6.6 Typing a motor in by hand (quick approximation)

When you only need an order-of-magnitude answer, most versions let you create a motor
inside OpenRocket with a short point list. A 4-point idealisation of the same motor:

| time (s) | thrust (N) |
|---|---|
| 0.00 | 0 |
| 0.10 | 25 |
| 1.10 | 20 |
| 1.30 | 0 |

Trapezoid area: `0.1×(0+25)/2 + 1.0×(25+20)/2 + 0.2×(20+0)/2 = 1.25 + 22.5 + 2.0 = 25.8 N·s`,
average thrust `19.8 N` — within 5 % of the detailed curve. Good enough for sizing; **not**
good enough for a design review or a delay-time decision, because it hides the ignition
transient and the tail-off that set your rail exit and your structural loads.

### 6.7 Selecting the motor on the rocket

1. Select the motor-mount inner tube → **Motor** tab.
2. Choose the motor from the list (e.g. `E19KNSB`).
3. Set the **ejection delay** that the simulation should use. For our plugged motors choose
   "no delay"/plugged; for delay-grain motors pick a listed delay or use the override.
4. If your version has an ignition setting, confirm the motor is ignited at launch.

---

## 7. Running a simulation

### 7.1 The simulation types

| Type | What it does | When to use it |
|---|---|---|
| **Single** | One flight with one motor configuration and one set of launch/wind conditions | Every design iteration. This is 90 % of your runs |
| **Batch** | Runs the same rocket many times while sweeping one or more parameters (motor, wind speed, wind direction, launch rod length, launch rod angle/tilt, launch direction, temperature, pressure, rocket mass) | Wind sweeps, rail-length studies, off-nominal mass/thrust cases, dispersion |
| **Multi-level** | Runs a multi-stage flight, assigning a configuration and an ignition delay to each stage | Stage 2+ only. Not needed for Stage 1 |
| **Monte Carlo** (22.02+) | Draws parameters from distributions you specify (mean and standard deviation) and runs many random flights | Dispersion statistics for range safety and the IN-SPACe technical assessment |

### 7.2 Creating a single simulation

1. Go to **Flight simulations → New simulation**.
2. Give it a name that says what it is: `Nominal_E19_calm_2m-rail`.
3. In the options dialog, work through the tabs/sections (the exact tab names vary; you are
   looking for these four groups of settings):

   **a. Motor / configuration.** Select which motor(s) this simulation uses. If you have
   several configurations (§10), pick one.

   **b. Launch conditions.**
   - **Launch rod/rail length** — the distance the rocket is guided. Enter what you own:
     1.5 m rod or 2.0 m rail. This parameter has a huge effect on the rail exit velocity
     and therefore on whether the flight is safe.
   - **Launch rod angle / tilt** — degrees from vertical. 0° is vertical. Use 0° for the
     nominal case, then study ±2° and ±5° (§ validation guide).
   - **Launch direction / azimuth** — degrees; the compass direction the rod points.
   - **Launch altitude (ASL)** — **Bengaluru sites are around 850–950 m**. Enter the real
     value, not 0. The air is ~10–15 % thinner than at sea level, which raises apogee.
   - **Temperature and pressure** — e.g. 28 °C and ~910 hPa for a Bengaluru afternoon at
     900 m. Or let OpenRocket compute a standard atmosphere from the altitude, and note
     which you did.

   **c. Wind.**
   - **Average wind speed** — m/s.
   - **Wind direction** — degrees. Check your version's tooltip for whether this is the
     direction the wind comes *from* or blows *towards*; for dispersion work, sweep all 360°
     so the convention cannot bite you.
   - **Turbulence intensity / standard deviation** — leave at **0** for repeatable runs.
     Turn it on only for Monte Carlo studies, because non-zero turbulence makes every run
     slightly different.

   **d. Time step / accuracy.** Smaller time steps are more accurate and slower. Defaults
   are fine for Stage 1; if a result looks jittery, halve the step and see whether the
   answer moves. If it does, the step was too big.

4. **Run** the simulation (Run button, or right-click → Run). A short flight simulates in
   well under a second.
5. Double-click the row to open the results window.

### 7.3 The results window

Three areas matter:

- **Overview** — the summary numbers (apogee, max velocity, max Mach, max acceleration,
  time to apogee, flight time, ground hit velocity, launch rod velocity, deployment
  velocity, optimum delay). Start here.
- **Plot** — the flight profile graph. Choose the X quantity (usually *time*) and the Y
  quantity from drop-downs, and add several series to one plot. Line up "altitude vs time",
  "velocity vs time" and "vertical acceleration vs time" in three stacked plots: that trio
  tells you almost everything about a flight.
- **Data** — the raw time-history table, which is also what you export to CSV.

---

## 8. Reading the output

### 8.1 The numbers that matter, and what "good" looks like

| Quantity | Where it appears | What it tells you | Stage 1 target |
|---|---|---|---|
| **Apogee** (m AGL) | Overview | Peak altitude | 100–200 m for Stage 1 |
| **Max velocity** (m/s) | Overview | Sets dynamic pressure, fin flutter risk, chute loads | 40–100 m/s |
| **Max Mach number** | Overview | Above ~0.8 your drag model stops being trustworthy | **< 0.5** for Stage 1 |
| **Max acceleration** (m/s² or g) | Overview | Structural and avionics loads; is the airframe strong enough? | < 15 g |
| **Launch rod velocity** (m/s) | Overview | Speed at the moment the rocket leaves the rail | **≥ 4 × wind speed, and never < 15 m/s** |
| **Time to apogee** (s) | Overview | Recovery timing; sanity-check against your hand calc | 5–10 s |
| **Optimum delay** (s) | Overview ("Optimal delay" in some versions) | Time from **burnout** to apogee. Pick your delay from this | 3–6 s for Stage 1 |
| **Deployment velocity** (m/s) | Overview | The speed at which the chute opens. Sets the opening load | **< 10 m/s ideal**, never > 20 m/s |
| **Ground hit velocity** (m/s) | Overview | Landing speed | 4–7 m/s |
| **Flight time** (s) | Overview | How long until you can walk out | 30–60 s |
| **Static stability margin** (cal) | Design view summary + plot vs time | How much restoring force the fins give | 1.0–2.0 cal at launch, and it should grow (never drop below ~1) through the burn |
| **Max dynamic pressure** (Pa) | Plot/data in newer versions; otherwise compute `q = ½ρv²` from max velocity | Fin flutter and structural check | ≤ ~6 kPa for Stage 1 |

### 8.2 The flight profile plot

The classic plot set for a design review is four stacked graphs sharing the time axis:

1. **Altitude vs time** — the flight profile. Look for a smooth rise, a rounded apogee, then
   a fast drop (drogue/streamer/ballistic) or a steady descent (main chute). A jagged
   apogee means the time step is too big.
2. **Vertical velocity vs time** — should cross zero exactly at apogee. If it does not, your
   mass or motor data is inconsistent.
3. **Total acceleration vs time** — a spike at ignition, a plateau during the burn, then a
   negative plateau near `−g` in coast, then a sharp negative spike when the chute opens
   (the deployment shock). That spike is the load that breaks shock cords.
4. **Stability margin vs time** — see §8.3.

### 8.3 Stability margin over time

The static margin is `(CP − CG)` divided by the body's maximum diameter, in calibers. Both
move during the flight: the **CG moves forward** as propellant burns (so the margin
generally *increases*), and the **CP moves aft** as the Mach number rises.

Read the *minimum* value across the whole burn, not just the launch value. A rocket that
launches at 1.4 cal but dips to 0.7 cal at Mach 0.6 is a rocket that will wobble. On the
plot, pick "stability margin" as the Y axis against time.

The static margin is a *static* measure. It says nothing about dynamic behaviour; a rocket
with a huge margin can be dynamically unstable (slow oscillation that grows), which
OpenRocket will show as an angle-of-attack trace that wanders or grows. Check the
**angle of attack** plot: steady near zero with small decay is good; growing oscillation is
a warning sign, usually from a very large margin plus flexible fins.

### 8.4 Good result vs warning sign, at a glance

| Looks good | Warning sign | What to do |
|---|---|---|
| Static margin 1.0–2.0 cal at launch, never below ~1.0 | < 1.0 cal, or a dip mid-burn | Bigger/more aft fins, or nose weight |
| Static margin steady, no oscillation | > 2.5 cal | Remove nose weight, move mass aft; accept the drift, or move the fins forward slightly |
| Angle of attack ≈ 0, decaying | Oscillating or growing angle of attack | Check margin and fin stiffness; reduce margin |
| Launch rod velocity ≥ 4 × wind | 8–12 m/s off the rail | Longer rail, lighter rocket, higher-thrust motor, or fly only in near-calm |
| Max Mach < 0.5, drag rising smoothly | Mach > 0.8 with a drag spike | Move up to RASAero/RocketPy, thicken and stiffen fins |
| Deployment velocity < 10 m/s | Deployment at 20–40 m/s | Fix the delay or use electronic deployment; uprate the chute and cord |
| Ground hit velocity 4–7 m/s | > 9 m/s | Bigger chute, or stronger airframe (and say which one you chose) |
| Vertical velocity crosses zero at apogee | Apogee not where the velocity crosses zero | Inconsistent mass or motor data |
| Simulation warnings: none | "Recovery device deployment at high speed", "high speed deployment" | Do not ignore the yellow warning column |

### 8.5 The four warning signs in detail

**(a) Static margin too low (under 1 caliber).** The rocket does not have enough restoring
moment. It will fly at an angle, arc over, or tumble. Under 0.5 cal it is dangerous. Fixes,
in order of preference: move the fins aft; increase the fin span or chord (span is more
effective per gram); add nose weight (costs apogee); lengthen the body (moves the CG forward
relative to the fins). Re-check the rail exit velocity afterwards — every gram of nose
weight makes it worse.

**(b) Static margin too high (over about 2 calibers).** The rocket is over-stable and
**weathercocks**: as it leaves the rail and meets a crosswind, the fins generate a strong
restoring moment that turns the nose *into* the wind. The rocket then flies a curved path
upwind, loses altitude, and can travel a long way horizontally before apogee. Two calibers
is a sensible working maximum for a small rocket; 4–5 cal is an admission that the design
was never trimmed. Fix: remove nose weight, shift heavy components aft, or reduce the fin
span. (A tiny amount of weathercocking is unavoidable; you are managing it, not eliminating
it.)

**(c) Rail exit velocity too low.** The rail (or rod) is the only thing keeping the rocket
pointing the right way before the fins start working. If it leaves the rail too slowly, the
slightest wind or thrust misalignment tips it, and the flight goes wherever it wants.
The widely used rule of thumb is **exit velocity ≥ 4 × the steady wind speed**, with an
absolute floor of about **15 m/s (50 ft/s)** — and whichever your range requires, the
higher number wins. Our 24 mm KNSB motor at 19 N average thrust on a 300 g rocket gives
only ~14–15 m/s off a 2 m rail: that means **no flying in wind above ~3 m/s**. That is a
design conclusion, not a nuisance. Fixes: longer rail, lighter rocket, higher-thrust
(faster-burning) propellant grain, or a bigger nozzle throat for more thrust.

**(d) Excessive descent rate / high deployment velocity.** The descent rate is set by the
chute: `v_desc ≈ √(2mg / (ρ·Cd·A))`. Landing at 9–10 m/s will break fins, crack tubes and
kill electronics. Target 4–7 m/s for our builds (roughly 5–6 m/s for a 450 mm chute on a
300 g rocket).

Deployment velocity is a different and more dangerous number. Under a nominal delay the
chute opens at apogee where the speed is nearly zero. If the delay is 2 s too long, the
rocket is already falling at 20 m/s, and the opening load scales with `v²` — **16 times the
load** at 20 m/s compared to 5 m/s. That is how nose cones get zippered off and shock cords
snap. Keep the deployment velocity under about 10 m/s, and under 20 m/s absolutely. If a
motor delay cannot achieve that, use electronic deployment.

---

## 9. Realistic mass modelling — the single biggest source of error

### 9.1 Why it dominates everything

In the drag-free limit, apogee goes as

```
h ≈ I_total² / (2 · g · m²)        →        h ∝ 1/m²
```

so a **10 % mass error produces roughly a 20 % apogee error** — and in the wrong direction
if you under-estimate. A student rocket's mass is routinely under-estimated by 15–30 %
because of the things nobody types in: epoxy fillets, primer, three coats of paint, the
heat blanket, the wadding, the quick links, the shock cord, the altimeter sled, the screws,
the launch lug glue, the nose-cone shoulder you forgot, the motor's own case mass. Simulate
a 230 g rocket as 180 g and you will predict an apogee hundreds of metres higher than
reality, and then pick a landing area that is wrong.

Rule for the club: **every mass component in the model must correspond to something you
have weighed or can point at.**

### 9.2 The weighing discipline

- Buy a kitchen scale with 1 g resolution for the big parts, and a jeweller's scale with
  0.01 g resolution (a few hundred rupees online) for fins, hardware and propellant.
- Weigh **as you build**: each part before it is glued, then the whole sub-assembly after
  gluing, and finally the complete rocket **ready to fly, with the motor installed**.
- Weigh the motor loaded (this is a number you must have for the simulation anyway).
- Measure the CG of the finished rocket (§9.4). This is the other half of the mass model.
- Keep the numbers in the design log and in your `.ork` overrides. When the design changes,
  update the numbers the same day.

### 9.3 Overriding mass and CG for a component

Every component's configuration has an **Override** tab (wording varies: *Override mass*,
*Override CG*, sometimes "use this value instead of the calculated one"). The workflow:

1. Look at the component's *calculated* mass/CG first. Note where it disagrees with reality.
2. Tick **Override mass** and enter the **weighed** value in grams (or kg — match your
   preference setting).
3. Tick **Override CG** and enter the **measured** CG position. **Check the reference
   point**: OpenRocket measures a component's CG either from the front of that component or,
   for a nose cone, from the tip. The field's tooltip/label states which. Getting this wrong
   moves your CG by centimetres and your simulation by tens of metres.
4. If a component's mass is unknown, do not invent a number: put in an estimate, mark the
   simulation "unvalidated", and fix it after the first weighing.

Use overrides for: nose cones (real ones are heavier than the ideal geometry), 3D-printed
or hand-made parts, tubes of unknown material, and anything with glue on it.

Use **mass components** for things with no geometry worth modelling: avionics, batteries,
paint, ballast, hardware.

### 9.4 Measuring the real CG

The practical shop method:

1. Remove the motor. Balance the empty rocket on a knife edge, a triangular file, or a
   length of angle stock clamped in a vice, sliding it until it balances. Mark that point.
2. Measure from a **fixed, repeatable reference** — for us, the tip of the nose cone — to
   the balance point, along the rocket's axis. Record it in millimetres.
3. Repeat with the loaded motor installed (the CG will shift aft; this is the number the
   simulator really wants for launch stability).
4. In OpenRocket, read the CG from the design view summary using the same reference, and
   compare. If they differ by more than ~5 mm, find out why: usually a missing mass
   component, or an override CG entered from the wrong reference point.

A nose-heavy rocket is stable but draggy and low; a tail-heavy rocket is unstable. The CG
measurement is how you catch an unstable rocket **before** it is on the rail.

### 9.5 Paint, glue and the other invisible masses

A typical Stage 1 rocket gains 15–30 g from finishing and assembly. Do not distribute it
randomly: glue and fillets belong at the fin roots (aft), paint belongs roughly along the
tube (mid-length), the epoxy inside the nose cone belongs forward. Where you put the mass
moves the CG, and the CG is what you are actually simulating.

---

## 10. Configurations: one rocket, many motors

A **configuration** (older docs may say "motor configuration") is a named set of motor
choices and stage settings for a single design. One `.ork` file can therefore hold:

- `Config A — E19KNSB, plugged, electronic deploy`
- `Config B — E19KNSB with 5 s delay grain`
- `Config C — D-class test motor, no avionics` (lighter)
- `Config D — E19KNSB + 40 g avionics`

How to work with them:

1. Find the configuration controls — usually a **Motors & Configuration** tab or panel in
   the design view, or a **Configurations** area in the simulation options.
2. **New configuration**, name it, then select the motor for the motor mount within that
   configuration. Each configuration keeps its own motor, delay and (in multi-stage
   designs) stage ignition settings.
3. In each **simulation**, choose which configuration it uses. This is how you compare
   motors without ever duplicating the rocket.
4. Add a configuration for every mass change you expect to fly (with and without avionics,
   different nose weight) — it is much safer than editing the design between simulations,
   because the design you reviewed and the design you flew must be the same file.

Common trap: you edit the design (add 30 g of avionics) but run an old simulation that was
created before the change. Simulations do not automatically re-run. **After any design or
mass change, re-run every simulation you intend to quote.**

---

## 11. Exporting results for a design review

### 11.1 One flight: full data

1. Open the simulation results → **Data** tab.
2. **Export** (button or right-click) → save as CSV, e.g.
   `UVCE-S1_rev-A_nominal_E19_data.csv`. This file has one row per time step and a column
   per quantity. It is the evidence behind every claim in your review document.
3. On the **Plot** tab, save or copy the plots. Most versions offer a save/copy action for
   the plot; if not, a clean screenshot is perfectly acceptable — but make the axes and the
   legend readable, and title it with the design revision and the case name.

### 11.2 Many flights: the summary table

In the **Flight simulations** tab you can usually select several simulations and **Export**
a summary CSV containing one row per simulation with apogee, max velocity, max Mach,
launch rod velocity, ground hit velocity, flight time and so on. This is the table that
becomes "Table 3: nominal and off-nominal results" in the design review. Build it once,
copy it into the document, and keep the CSV in the flight folder.

### 11.3 Pictures of the rocket

**Tools → Photo studio** renders a presentable image of the rocket (with a nicer finish
than a screenshot of the design view). Use it for the cover figure of the design review.
The design view's own figure is fine for showing CG/CP and stability.

### 11.4 What a design review must contain

At minimum, for the revision under review:

1. The `.ork` file itself, with the revision name in the filename, plus the exact
   OpenRocket version that produced the results.
2. The mass budget table (estimated vs weighed) and the measured CG.
3. The motor file(s) used, with their revision/date, and the static-fire reference.
4. The nominal case: apogee, max velocity, max Mach, max acceleration, rail exit velocity,
   static margin at launch and minimum through the burn, optimum delay, deployment velocity,
   descent rate, flight time.
5. The off-nominal cases from
   [Simulation_Plan_and_Validation.md](Simulation_Plan_and_Validation.md): worst-case high
   and low apogee, worst-case landing distance and direction, and the wind limit.
6. The flight profile plots (altitude, velocity, acceleration, stability).
7. The assumptions and the known unknowns, stated plainly. A review that says "Cd is a
   guess until flight 2" is a *better* review than one that quietly pretends otherwise.

---

## 12. Common beginner mistakes

**Modelling mistakes**

1. **Not modelling the recovery hardware.** The chute, cord, blanket and links are 25–35 g
   sitting in the tube. Ignoring them is a free 10 % apogee error.
2. **Not modelling paint and glue.** See above. Add 15–20 g and mean it.
3. **Forgetting the motor's own mass**, or double-counting it (adding a "casing" mass
   component when the motor file already includes the case).
4. **Leaving the launch altitude at 0 m.** At 900 m ASL in Bengaluru the air is thinner;
   ignoring it under-predicts apogee.
5. **Default Cd or default parachute Cd forever.** Fix the chute Cd from your own descent
   measurement after the first flight.
6. **Leaving the default Cd and drag model untouched for a rocket with a camera shroud,
   rail buttons and a launch lug.** Every protuberance adds drag.
7. **Wrong inner-tube diameter** so the motor "fits" in the model but not in reality.
8. **A fin set positioned relative to the wrong end of the tube** — 100 mm of fin movement
   is a completely different rocket.
9. **No launch lug / rail interface** in the model, then wondering why the rail exit
   velocity is meaningless.
10. **Modelling a rocket that flies with the motor mount empty** (no motor selected).
11. **Copying a design and forgetting to re-run the simulations** after the edit.
12. **Simulating a mass that was never weighed.**

**Reading-the-result mistakes**

13. **Quoting the apogee and nothing else.** Velocity, acceleration, rail exit, stability
    and deployment velocity are what make the apogee safe or unsafe.
14. **Ignoring the minimum stability through the burn** and reporting only the launch value.
15. **Accepting > 2.5 cal static margin** as "extra safe". It is not: it is weathercocking.
16. **Ignoring the warning column** in the simulation table.
17. **Reporting Mach 0.9 results from a Barrowman-based tool** as if they were reliable.
18. **Confusing AGL and ASL altitude** when comparing with an altimeter or with site data.
19. **Comparing a simulation against a flight with different wind** and concluding the drag
    model is wrong.
20. **Using one flight to "validate" a model.**

**Process mistakes**

21. **Overwriting a design revision that was already reviewed.** Save a new revision
    instead: `UVCE-S1_rev-B.ork`.
22. **Not recording the OpenRocket version and motor file revision** with the results.
23. **Simulating once, three days before the launch.** Simulate as you design.
24. **Flying a rocket whose stability was never checked with the actual motor installed and
    the actual CG measured.**
25. **Treating the simulator as an authority instead of a hypothesis.** A simulation is a
    claim to be tested by a flight and an altimeter, not a certificate.

---

## 13. Where to go next

**Stage 2 (300–600 m, F/G class) additions**

- Dual deployment: drogue at apogee, main at a low altitude, both modelled as separate
  parachute components with different deployment triggers.
- Tracking (radio/GPS) becomes mandatory rather than optional; add its mass.
- Monte Carlo dispersion analysis becomes a requirement, not a nice-to-have.
- Move the transonic drag question to RASAero II or RocketPy (see
  [Simulation_Plan_and_Validation.md](Simulation_Plan_and_Validation.md), §9).

**Stage 3 (1 km+, H class and above)**

- Certification/licensing and site permissions become the critical path.
- Proper structural analysis (fin flutter, tube buckling, thrust-plate loads) in FEA.
- 6-DOF Monte Carlo in a Python tool with a proper wind model.

**Then close the loop.** Every flight you simulate, fly, and then compare against its
altimeter log makes the next simulation better. That loop is described in
[Simulation_Plan_and_Validation.md](Simulation_Plan_and_Validation.md), and the motor side
of it in [Motor_Files.md](Motor_Files.md).

---

## Appendix A — UVCE-S1 parameter cheat sheet

```
NOSE CONE      ogive, L 140 mm, base dia 66 mm, wall 2 mm,
               shoulder L 30 mm / dia 64 mm, nose weight 20 g at 30 mm from the tip

BODY TUBE      OD 66 mm, L 550 mm, wall 0.6 mm, kraft/paper
               surface finish: smooth/painted

MOTOR MOUNT    inner tube OD 25 / ID 24 mm, L 120 mm, aft end flush with tube aft end
               marked as motor mount; motor E19KNSB, plugged or delay as configured
               2 centring rings, OD 66 / ID 25 mm, 6 mm thick, at 415 and 520 mm

FINS           3, trapezoidal: root 90 mm, tip 45 mm, sweep 55 mm, span 70 mm,
               thickness 4 mm ply, rounded cross-section, aft edge flush with tube aft end

LAUNCH LUG     60 mm x 7 mm OD, 300 mm from tube fore end

RECOVERY       450 mm flat chute, Cd 0.8, 6 lines x 500 mm, deploy: apogee/ejection
               4 m cord + blanket + 2 links = 30 g as a mass component

MASSES         nose cone 22 g | nose weight 20 g | tube 55 g | fins 27 g
               fillets 6 g (aft) | MMT + rings 18 g | lug 3 g | recovery 35 g
               paint/glue 20 g (mid-tube) | avionics 25 g (fwd of MMT)
               dry ~231 g, loaded with 68 g motor ~299 g

LAUNCH         rail 2.0 m vertical, site ~900 m ASL, 28 C, ~910 hPa,
               design wind 3 m/s, hard limit ~3 m/s (4x rail exit rule)
```

## Appendix B — glossary

- **Apogee** — the highest point of the flight (we quote it in metres AGL).
- **Barrowman method** — the standard hand-calculation method for CP location; what
  OpenRocket uses (with extensions).
- **Caliber** — one body-tube diameter. "1.5 cal static margin" means the CP is 1.5 tube
  diameters behind the CG.
- **CG** — centre of gravity, the balance point.
- **CP** — centre of pressure, where the aerodynamic forces effectively act.
- **Cd** — drag coefficient (dimensionless), referenced to a stated area.
- **Dispersion** — the spread of possible landing points and apogees from a family of
  nearly identical flights.
- **Mach number** — speed divided by the local speed of sound (~345 m/s at 28 °C).
- **Motor class** — the letter (A…O) determined by total impulse; see
  [Motor_Files.md](Motor_Files.md).
- **Static margin** — `(CP − CG)/diameter`, in calibers.
- **Weathercocking** — the tendency of an over-stable rocket to turn into the wind.

## Appendix C — version differences worth remembering

| Feature | 15.03 | 22.02 | 23.09+ |
|---|---|---|---|
| Java required | 8+ | 11+ | 17 |
| Bundled-Java installers | Limited | Yes (Win/macOS) | Yes (Win/macOS) |
| Monte Carlo simulation | No | Yes | Yes |
| Rail buttons, shock cords | No | Yes | Yes |
| Motor import UI | Preferences → Motors + selection dialog | Improved | Improved |
| "Motors & Configuration" placement | Design view tab | Design view tab / dialog | Similar, tidied |

When in doubt, use the in-program **Help → About** to check your version, and write that
version number in your design log.
