# Learning Paths — Zero to Contributing Member

**UVCE Rocketry Club**

| | |
|---|---|
| **Purpose** | An on-ramp for people with **no prior knowledge**. Nobody joins knowing rocketry. |
| **Audience** | New members, juniors, and anyone who says *"I'm interested but I don't know where to start."* |
| **Design rule** | **Every path is free to start, and every path ends in something you built.** |

---

## Why this document exists

The most common reason interested students drift away is not lack of interest. It is **not knowing
what to do on day one**. "Come to the club" is not an instruction.

This gives every new member a concrete first task, a way to sample the subsystems before committing,
and a measurable way to know they are improving.

> 🔴 **Do not hand a new member a textbook.** Hand them Week 1 below. Reading without building does
> not stick, and a new member who spends three weeks reading will quit.

---

## How to use this

1. **Weeks 1–2 — everyone does the same thing.** [`01_Start_Here.md`](<01_Start_Here.md>). No
   exceptions, no specialisation yet. This is the common language the whole club shares.
2. **Week 3 — sample.** Pick **two** subsystem paths and do only their *Foundation* tier. You are
   shopping, not committing.
3. **Week 4 onward — choose one.** Go deep on the path that actually held your attention. Tell the
   Team Lead which one and why.
4. **Build something.** Every path has a *First Build*. It is not optional. It is the whole point.

---

## The paths

| Path | Covers | Best for people who… | Time to first build |
|---|---|---|---|
| **[01 Start Here](<01_Start_Here.md>)** | Rocketry fundamentals — **everyone does this** | Everyone | 2 weeks |
| **[02 Simulation](<02_Simulation.md>)** | OpenRocket, trajectory, stability, validation | Like computers, hate guesswork | 2 weeks |
| **[03 Propulsion](<03_Propulsion.md>)** | Propellant, grain design, nozzles, static testing | Are patient, meticulous, chemistry-curious | 4–6 weeks |
| **[04 Structures & Aero](<04_Structures_and_Aero.md>)** | Airframes, fins, materials, recovery, fabrication | Like building things with their hands | 3–4 weeks |
| **[05 Avionics](<05_Avionics.md>)** | Flight computer, sensors, telemetry, ground station | Code, solder, or debug electronics | 4–6 weeks |
| **[06 Tools & Software](<06_Tools_and_Software.md>)** | CAD, PCB, Python, Git — the shared toolkit | Anyone; do this alongside your path | ongoing |
| **[07 Communities](<07_Communities_and_Inspiration.md>)** | Where to ask questions; who to learn from | Everyone | — |

**Cross-cutting:** [`../40_SAFETY/Safety_Manual_Master.md`](<../40_SAFETY/Safety_Manual_Master.md>) is
**not** a path. It is mandatory reading for everyone, before any energetic work, ever.

---

## The 4-week induction

### Week 1 — Orientation (everyone, ~3 hours)

- [ ] Read [`01_Start_Here.md`](<01_Start_Here.md>) §1–3
- [ ] Read [`../40_SAFETY/Safety_Manual_Master.md`](<../40_SAFETY/Safety_Manual_Master.md>) §1–4
- [ ] Sign the safety induction and the role acceptance form in
      [`../00_ADMINISTRATION/Roles_and_Responsibilities.md`](<../00_ADMINISTRATION/Roles_and_Responsibilities.md>) §14
- [ ] Install OpenRocket (free) and open one of our `.ork` files
- [ ] **Deliverable:** change the motor mass in OpenRocket, note how apogee changes, write three
      sentences about why

### Week 2 — First flight (everyone, ~4 hours + a Saturday)

- [ ] Build a **water rocket** or a low-power kit rocket (see [`01_Start_Here.md`](<01_Start_Here.md>) §4)
- [ ] Fly it. Recover it. Fly it again.
- [ ] **Deliverable:** a photo of the rocket, its measured mass, and one thing that went wrong

> **Why water rockets / kits first:** they teach stability, fin alignment, recovery and range
> discipline at near-zero cost and near-zero risk. Nobody touches propellant in week 2.

### Week 3 — Sample two paths (~4 hours)

- [ ] Pick two paths from the table above
- [ ] Do only their **Foundation** tier
- [ ] **Deliverable:** tell the Team Lead which one you want, and why

### Week 4 — Choose and build (~5 hours)

- [ ] Commit to one path
- [ ] Start its **First Build**
- [ ] **Deliverable:** a first build in progress. Show it at the next meeting.

---

## Assigning people to subsystems

After the induction, use this to match people to work. The aim is **two people minimum per
subsystem** — one person per subsystem is a single point of failure, and it is how knowledge leaves
when someone graduates.

| Subsystem | Needs | If nobody volunteers |
|---|---|---|
| Propulsion | Patience, meticulousness, safety discipline | Team Lead recruits specifically; do not rush the hire |
| Structures | Hands-on, enjoys fabrication | Usually the easiest to fill |
| Avionics | Coding **or** electronics — both is rare, one is enough | Hardest to fill. Recruit deliberately from ECE/EEE/CSE. |
| Simulation | Comfort with software, attention to detail | Often the natural second skill for a structures person |
| Operations | Organisation, writing, follow-through | Frequently underrated; a good organiser is worth two engineers |

### Matching interests to subsystems

| If they say… | Point them at |
|---|---|
| "I like coding" | Avionics → ground station software first |
| "I like electronics / soldering" | Avionics → sensors and test-stand instrumentation |
| "I like chemistry" | Propulsion → propellant, but **only after** the safety induction |
| "I like building / working with my hands" | Structures → fabrication |
| "I like CAD" | Structures → design, then Simulation |
| "I like physics / maths" | Simulation → Barrowman, trajectory, validation |
| "I like organising / writing" | Operations → documentation, sponsorship, logistics |
| "I don't know yet" | Simulation. It touches everything and needs no special kit. |

---

## Progression and checkpoints

Each path has **three tiers** and a **checkpoint** at each. A checkpoint is a thing you can *do*, not
a thing you have *read*.

```
FOUNDATION ──► checkpoint ──► WORKING ──► checkpoint ──► ADVANCED
 (2-3 weeks)                  (4-8 weeks)                (months)
```

> **Nobody is "behind".** The tiers are not a race and there is no exam. The checkpoints exist so you
> can tell whether *you* are ready to move on — not so someone can grade you.

**The club's rule on learning:** if you cannot show someone else how to do it, you have not learned it
yet. Every member teaches the thing they just learned at the next meeting. This is how the club
retains knowledge when people graduate.

---

## Recommended reading (shared, in order)

| # | Resource | Cost | Why |
|---|---|---|---|
| 1 | [NASA Beginner's Guide to Rockets](https://www.grc.nasa.gov/www/k-12/rocket/) | Free | The clearest plain-language introduction that exists |
| 2 | [OpenRocket](https://openrocket.info/) + [User Guide](https://openrocket.readthedocs.io/en/latest/) | Free | You will use this constantly |
| 3 | [`../Technical_Reference_Nakka.md`](<../Technical_Reference_Nakka.md>) | Free | Our own consolidated propellant + safety reference |
| 4 | [NASA Beginner's Guide to Aeronautics](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/) | Free | Aerodynamics and stability, properly explained |
| 5 | *Handbook of Model Rocketry* — G. Harry Stine | ~₹1,500 | The classic. Buy it once the club has funds. |
| 6 | *Rocket Propulsion Elements* — Sutton & Biblarz | ~₹800 (Indian edition) | The propulsion textbook. Only for the propulsion path. |

---

## Notes for the person running this

- **Do not lecture.** Run the induction as a build session, not a class. People join rocketry to make
  things, not to attend seminars.
- **Keep the first task under two hours.** A new member who finishes something on day one comes back.
- **Pair people up.** Two new members on one task learn faster than two alone, and they keep each
  other accountable.
- **Let people change paths.** Somebody who tries propulsion and hates it should move to structures
  without anyone making it awkward. Better a happy structures person than a resentful propulsion one.
- **Document what they build.** Photos, dimensions, what failed. It goes in `60_TEST_DATA/` or the
  build log. This is how the club accumulates memory.

---

## A note on the honest difficulty

Rocketry has a steep middle. The first two weeks are easy and fun; the next two months are
frustrating, full of small failures, and often boring. **Everyone who has ever built a rocket has
been through this.** The members who stay are the ones who find the frustration interesting rather
than discouraging.

If a new member is losing momentum, the fix is almost always the same: **give them something small
they can finish this week.**

---

*Every path in this section is deliberately free to start. If a resource here requires payment, it is
marked and there is a free alternative listed alongside it.*
