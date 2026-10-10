# 06 — Tools & Software

**The shared toolkit. Do this alongside your chosen path, not instead of it.**

| | |
|---|---|
| **Time** | Ongoing — learn each tool when you first need it |
| **Cost** | **₹0.** Everything here is free, or free for students. |
| **Rule** | **Do not learn a tool you have no use for yet.** Tools are learned by using them. |

---

## The principle

Every tool below is learned best at the moment you need it. Reading a CAD tutorial when you have
nothing to design teaches you nothing. **Have a problem first, then learn the tool.**

So: pick your path, hit a problem, then come here and learn the tool that solves it.

---

## CAD — for designing parts

| Tool | Cost | Runs on | Best for | Notes |
|---|---|---|---|---|
| **[Onshape](https://www.onshape.com/en/education/)** | **Free for students** | Browser | **Recommend starting here** | Nothing to install, works on any laptop, real parametric CAD. Your work is in the cloud, so no lost files. |
| **[Fusion 360](https://www.autodesk.com/education/edu-software/fusion)** | Free for students | Windows/Mac | CAD + CAM + simulation | More powerful, heavier, and the student licence needs renewing each year |
| **FreeCAD** | Free, open source | Windows/Mac/Linux | When you want no licence at all | Steeper learning curve, less polished |

**What we actually design in CAD:**
- Motor casing, nozzle, and grain geometry
- Thrust plate and centring rings (these must match the motor *exactly*)
- Nose cone and fin profiles
- Avionics sled and enclosures
- Test stand components

> **Start with a centring ring.** It is a circle with a hole in it. If you can model that, dimension it,
> and export a drawing, you have learned the core of CAD.

**Learning path:**
1. Sketch a circle, extrude it, put a hole in it → that is a centring ring
2. Learn to dimension properly (a drawing without dimensions is a picture)
3. Learn to export STL for 3D printing
4. Learn to make an assembly → thrust plate + motor + airframe
5. Learn to make a proper engineering drawing with title block and tolerances

---

## Simulation — for predicting flight

| Tool | Cost | Best for |
|---|---|---|
| **[OpenRocket](https://openrocket.info/)** | Free | **The default.** Everything we do in [`02_Simulation.md`](<02_Simulation.md>) |
| **[RASAero](https://www.rasaero.com/)** | Free | Better supersonic drag modelling; use later |
| **Python + NumPy/SciPy** | Free | Your own trajectory integrator, when you want to understand assumptions |

See [`02_Simulation.md`](<02_Simulation.md>) for the full learning path.

---

## Programming — for analysis and avionics

| Language | Where you will use it |
|---|---|
| **Python** | Data analysis, plotting thrust curves, trajectory code, ground station software |
| **C / C++ (Arduino)** | Flight computer firmware, test stand logging |
| **Bash** | Glue scripts, file handling (optional, learn when needed) |

### Python — what to learn, in order

1. Variables, lists, loops, functions
2. Reading and writing CSV files — **your data lives in CSVs**
3. `numpy` for arrays and maths
4. `matplotlib` for plotting — **you will plot every thrust curve you ever measure**
5. Numerical integration — so you can write your own trajectory simulation

| Resource | Cost | Notes |
|---|---|---|
| [Python official tutorial](https://docs.python.org/3/tutorial/) | Free | Dry but complete |
| [Automate the Boring Stuff](https://automatetheboringstuff.com/) | Free online | **Best beginner Python resource.** Practical, not academic. |
| [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html) | Free | When you need arrays |
| [Matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html) | Free | When you need plots |

**First useful Python script:** read a static fire CSV, plot thrust against time, and compute total
impulse by summing `F × dt`. That is a real engineering tool, and it takes an afternoon.

### Arduino / embedded

| Resource | Cost |
|---|---|
| [Arduino Language Reference](https://docs.arduino.cc/language-reference/) | Free |
| [Arduino Learn](https://docs.arduino.cc/learn/) | Free |
| [Adafruit Learning System](https://learn.adafruit.com/) | Free |

---

## Version control — Git

**Why a student club needs Git:** because "final_v2_REAL_final.xlsx" is how knowledge gets lost, and
because the member who wrote the code graduates before you do.

| What to put in Git | What not to |
|---|---|
| All documentation (Markdown) | Large binaries (videos, CAD files) |
| Code — firmware, ground station, analysis scripts | Raw test data over ~10 MB |
| Design files that are text-based | Anything with credentials in it |
| This workspace | |

| Resource | Cost |
|---|---|
| [Pro Git — Getting Started](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) | Free |
| [GitHub Skills](https://skills.github.com/) | Free, interactive |

> **Minimum viable Git:** `init`, `add`, `commit`, `push`, `pull`. That is 90% of what a club needs.
> Do not let anyone tell you it is complicated.

---

## Circuit design and simulation

| Tool | Cost | Best for |
|---|---|---|
| **[Falstad Circuit Simulator](https://www.falstad.com/circuit/)** | Free, browser | **Start here.** Watch current flow in real time. Brilliant for building intuition. |
| **[KiCad](https://www.kicad.org/)** | Free, open source | Real PCB design, when you outgrow breadboards |
| **LTspice** | Free | Analog circuit simulation, more rigorous than Falstad |

**Learning path:** Falstad to understand a voltage divider → Falstad to understand your load cell
bridge → KiCad when you need a real board.

---

## Documentation — Markdown

Every document in this workspace is Markdown. It is plain text, so it never becomes unreadable, and
it works with Git.

| Syntax | Renders as |
|---|---|
| `# Heading` | Heading |
| `**bold**` | **bold** |
| `- item` | bullet |
| `[text](url)` | link |
| `` `code` `` | `code` |
| `\| a \| b \|` | table |

- [Markdown Guide](https://www.markdownguide.org/) — free, 10 minutes to learn

**Editors:** VS Code (free, excellent Markdown preview), Obsidian (free, good for linked notes), or
any plain text editor.

---

## The maths you actually need

You do **not** need advanced mathematics to start. This is the honest list.

| Topic | Where it is used | Do you need it now? |
|---|---|---|
| **Arithmetic and ratios** | Everything — propellant ratios, mass fractions | ✅ Yes |
| **Algebra and rearranging equations** | Every design calculation | ✅ Yes |
| **Geometry and trigonometry** | Fin shapes, altitude measurement, Barrowman | ✅ Yes |
| **Units and unit conversion** | **The single biggest source of errors** | ✅ Yes |
| **Basic statistics** | Measurement uncertainty, dispersion | 🟡 Soon |
| **Calculus — integration** | Total impulse from a thrust curve, trajectory | 🟡 Soon — but numerically, not analytically |
| **Differential equations** | 6-DOF dynamics, internal ballistics | 🟢 Later |
| **Linear algebra** | Kalman filtering, FEA | 🟢 Later |

> 🔴 **Units will bite you before calculus does.** The most common error in amateur rocketry is a
> unit mistake — millimetres mixed with metres, grams with kilograms. **Write the units next to every
> number, every time.** It feels pedantic. It will save you a motor.

| Resource | Cost |
|---|---|
| [Khan Academy](https://www.khanacademy.org/) — algebra, trig, calculus | Free |
| [MIT OpenCourseWare](https://ocw.mit.edu/) | Free |

---

## Communication and project tools

| Need | Tool | Cost |
|---|---|---|
| Group chat (broadcast) | WhatsApp announcement group | Free |
| Subsystem working groups | WhatsApp, separate per subsystem | Free |
| File storage | Google Drive / OneDrive | Free |
| Code and docs | GitHub | Free |
| Task tracking | A shared spreadsheet is genuinely enough | Free |
| Video calls | Google Meet / Zoom | Free |

> **Resist tool proliferation.** A club with five members does not need Jira. A spreadsheet and a
> WhatsApp group will carry you until you have twenty members and real deadlines.

---

## The order to learn things

Do not try to learn all of this. Learn in this order, as your work demands it:

| When you… | Learn… |
|---|---|
| Join | Markdown (10 min), then OpenRocket |
| Start designing | Onshape or Fusion |
| Start measuring | Arduino + Python + `matplotlib` |
| Have data to analyse | `numpy`, CSV handling, numerical integration |
| Start a real project | Git |
| Need a PCB | KiCad |
| Need to understand a circuit | Falstad |
| Have a team | GitHub for docs, a shared spreadsheet for tasks |

---

## What NOT to do

| ❌ | Why |
|---|---|
| Learn CAD with no part to design | You will forget it in a week |
| Install six tools before using one | Tool collecting is a form of procrastination |
| Buy expensive software | Everything you need is free. Fusion, Onshape, KiCad, OpenRocket, Python, VS Code. |
| Use a tool you do not understand | A number from software you cannot explain is not an engineering result |
| Store the club's only copy on your laptop | Git, or a shared drive, or it does not exist |
