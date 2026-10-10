# UVCE Rocketry Club — Master Safety Manual

**Document:** `40_SAFETY/Safety_Manual_Master.md`
**Issuing authority:** UVCE Rocketry Club Safety Committee
**Applies to:** every club member, mentor, faculty advisor, guest, and visitor — without exception
**Status:** Controlled document. Changes only via the Safety Officer with Safety Committee approval.
**Review cycle:** every 6 months, and immediately after any incident, near miss, or propellant formulation change.

> **This document is the parent of the four subordinate procedures:**
> - `PPE_and_Equipment_Register.md` — what equipment must exist before any energetic work
> - `Propellant_Handling_SOP.md` — how propellant is ground, mixed, cast, stored, transported
> - `Static_Test_Procedure.md` — how a motor is fired on a test stand
> - `Flight_Operations_Safety.md` — how a rocket is flown
>
> If a subordinate document conflicts with this one, **this one wins** and the subordinate document is
> wrong and must be corrected.

---

## 1. Purpose

This manual exists so that members of the UVCE Rocketry Club can do serious experimental work with
energetic materials and **go home uninjured, with all their fingers, eyesight, and hearing**, and
without injuring or endangering anyone else or damaging anyone else's property.

It is written for people who have never done this before. It assumes no prior experience. It assumes
you are intelligent but untrained. It therefore states things that an experienced person would
consider obvious, because **the things that are obvious in hindsight are exactly the things that hurt
beginners.**

### 1.1 Scope

**In scope:**

- Handling, grinding, mixing, casting, curing, storing and transporting potassium nitrate / sorbitol
  (KNSB) propellant
- Manufacture and handling of pyrotechnic igniters and ignition powder
- Static firing of experimental solid rocket motors
- Flight of model and experimental rockets
- Workshop activity in support of the above (machining, drilling, cutting, composite and adhesive work)

**Out of scope, and prohibited without separate written authorisation from the Safety Committee and
the faculty advisor:**

- Ammonium perchlorate (AP), potassium perchlorate, potassium chlorate, or any perchlorate/chlorate
  propellant — see §3.4
- Any propellant formulation not listed in `Technical_Reference_Nakka.md` §1.1
- Any high-power motor above the club's current demonstrated scale (see the scaling ladder in
  `UVCE_Rocketry_Roadmap.md` §7 — **do not skip steps**)
- Liquid propulsion, hybrids, and any pressure vessel above 5 bar
- Anything involving confined quantities above the limits in §5.4

### 1.2 How to use this manual

1. Read §2 and §3 **once, fully**, before your first session. Not skimmed. Read.
2. Before **every** energetic operation, read the relevant subordinate procedure end to end. Do not
   work from memory.
3. Sign the pre-work checklist for that operation. If it is not signed, the operation does not happen.
4. If anything in this manual is unclear to you, **stop and ask the Safety Officer.** Not knowing is
   safe. Guessing is not.

---

## 2. Safety philosophy: zero tolerance for shortcuts

### 2.1 The governing principle

> **Every rule in this manual exists because someone, somewhere, was injured or killed without it.
> You are not smarter than the rule.**

### 2.2 The four membership criteria

These are taken directly from Richard Nakka's Experimental Rocketry Site (nakka-rocketry.net), the
primary technical reference for this club. They are not aspirational statements — **they are the
club's membership filter.** They are applied literally.

| # | Criterion | Test for yourself |
|---|---|---|
| 1 | **If you are a risk taker**, amateur rocketry is not for you. | Do you skip steps when you are behind schedule? Do you "just quickly" do something without the checklist? Do you find safety briefings boring? |
| 2 | **If you are a careless person**, amateur rocketry is not for you. | Do you lose tools? Do you leave things where you were told not to? Do you forget your PPE? Do you leave the dunk bucket empty? |
| 3 | **If you are not willing to religiously and without fail follow requisite safety practices**, amateur rocketry is not for you. | "Without fail" means *every single time*, including the boring 40th time, including when you are tired, including when it is a tiny 20 g batch that "can't do anything". |
| 4 | **If you do not have complete respect for the safety and property of yourself and others, including the general public**, amateur rocketry is not for you. | Your neighbour's dry field. The landowner's fence. A walker on a footpath you did not check. Your teammate's eyes. |

**Applying these criteria is not optional and not personal.** A member who demonstrates any of these
four traits during club activity is removed from energetic work immediately, by the Safety Officer,
with no discussion required at the time. Discussion happens afterwards, in the disciplinary process
of §9.

### 2.3 Why: the energy argument

This is the single most important piece of numerical context in this manual. Read it until it is
instinctive.

- Sugar-based propellants (including KNSB) release approximately **2.7 kJ per gram** when burned.
- Therefore **1 kg of KNSB propellant contains about 2.7 megajoules (2.7 MJ) of stored chemical
  energy**.
- 2.7 MJ is equivalent to a **1000 W electric heater running continuously for 45 minutes**.
- In a rocket motor, that energy is released in **2 to 3 seconds**.

Read those four lines again, slowly.

**A 1 kg propellant batch is a 2.7 MJ event that you are holding in a bowl.** If it releases that
energy in the open, it is a fire you cannot outrun and possibly a fire you cannot extinguish. If it
releases that energy inside a motor case, the case fails and becomes shrapnel.

- **Ammonium perchlorate (AP) composite propellants hold nearly double that energy density** —
  roughly 5–5.5 kJ/g. This is why §3.4 prohibits them for this club. Per Nakka: perchlorates "have
  the potential to be frighteningly hazardous when combined with incompatible binders or additives,
  and even small motors can explode with shocking violence."

**The 24-gram reality check.** Our current first motor holds 24 g of KNSB — about **65 kJ**, roughly
equivalent to a 1000 W heater for 65 seconds, released in about 2 seconds. That is a hand grenade's
worth of thermal energy in an object the size of your thumb. **There is no such thing as a "small
safe batch" of propellant. There is only a small batch of propellant that is being handled
correctly.**

### 2.4 The second principle: knowledge replaces common sense

Nakka's framing, which this club adopts:

> **Is amateur experimental rocketry hazardous?** No — otherwise sensible people would not do it.
> **Are there hazards to be concerned with?** Definitively yes. The responsibility is to *recognise*
> those hazards and take the necessary precautions. **Knowledge takes over where common sense leaves
> off** — because some risk factors are not obvious.

Concretely, this means:

- Molten KNSB will not auto-ignite below **300 °C**, and normal casting happens below **135 °C**. That
  is a real and valuable margin of safety — **and it is not a licence to be careless.** The tolerance
  documented by Nakka applies to *already-molten* slurry. It does **not** mean you can use a heater
  with an exposed element, because powder added to a hot exposed element can ignite immediately
  (`Propellant_Handling_SOP.md` §5.3).
- KNSB is genuinely stubborn to ignite — that is why it is comparatively forgiving to handle. It is
  **not** a reason to treat it casually.
- The failures that *do* happen come from causes that are not obvious: static discharge, a short
  circuit, an un-shunted igniter, a grain with a hidden crack, an inhibitor that debonded, a
  teammate who walked downrange while you were looking at a screen.

> **Inadvertent ignition from static, electrical short, or simple distraction must always be treated
> as a real possibility. Plan for it every time.**

### 2.5 Zero tolerance for shortcuts — what this means operationally

| Shortcut | Consequence |
|---|---|
| "I'll just do this one small thing alone." | Immediate removal from energetic work. See §5.1. |
| "The dunk bucket is empty but I'm only stirring, not heating." | Immediate stop. The bucket is filled before any propellant is uncovered. |
| "I'll skip the shunts, it's not connected to anything." | Immediate stop. Igniter leads are shunted until the moment of connection, every time. |
| "We're behind schedule, let's do one more test today." | Test Director refuses. Schedule pressure is never a reason. |
| "It's only 20 grams, the rules don't apply." | The rules apply most of all to small batches, because small batches are when attention lapses. |
| "That number looks wrong but the sim said it's fine." | Test is disqualified. Anomalies are investigated, never rationalised. |

**There is no penalty for stopping work.** There is a penalty for not stopping work. See §7 and §9.

---

## 3. Hazard awareness

### 3.1 What we are actually working with

| Material | Hazard | Key numbers |
|---|---|---|
| Potassium nitrate (KNO₃, "saltpetre") | Strong oxidiser. Grinding creates respirable dust. Intensifies any fire. | Finely divided dust is a dust-explosion risk in bulk; keep batches small |
| Sorbitol (C₆H₁₄O₆) | Combustible solid, low hazard alone. Suspended dust is explosive. | Melts 110–112 °C |
| **KNSB mixed powder** | **Readily combustible** once oxidiser and fuel are blended | Treat as a flammable solid from the moment of blending |
| **Molten KNSB** | Very hot (120–130 °C), sticky, severe burn risk, can ignite if overheated or electrically initiated | Auto-ignition > 300 °C; decomposition onset ~175 °C |
| Ignition powder (80% KNO₃ / 20% charcoal) | Genuinely pyrotechnic, extremely easy to ignite, burns violently in the open | Never mix more than 50 g at a time; check the local rules |
| Pyrotechnic igniters | Function on milliamps of stray current | **Shunt the leads. Always.** |
| Motor hardware under test | Catastrophic failure → shrapnel, blast, fire | Distance is the primary protection (§3.3) |
| Compressed gases, adhesives, solvents | Standard workshop hazards | Ventilation, no ignition sources |

### 3.2 Sodium and potassium nitrate — the Indian legal context (awareness)

> **This section is awareness, not legal advice.** Before the club purchases, stores, or transports
> oxidiser in any quantity, the Safety Officer must confirm the current position with the faculty
> advisor and, if required, the local authority.

- Potassium nitrate is a **restricted oxidiser** in India. Its sale, possession, transport and use are
  governed by the **Explosives Act 1884 and the Explosives Rules 2008**, administered by the
  **Petroleum and Explosives Safety Organisation (PESO)** under the Department of Industrial Policy
  and Promotion. State-level licensing and the district administration may also be involved.
- Agricultural-grade potassium nitrate (**13-0-45 or 14-0-45 fertiliser**) is sold legitimately at
  farm supply stores for fertiliser use. Buying it for that stated purpose and then diverting it is
  **not** a way around the rules — the club does not do this. We buy only what our documented,
  authorised work requires, from a supplier who knows what we are doing, and we keep the paperwork.
- **Practical consequences the club must respect:**
  1. **Keep total holdings small and documented.** See §5.4.
  2. **Keep a purchase register and a stock register** for every kilogram of oxidiser that enters or
     leaves the club's possession.
  3. **Never transport propellant or oxidiser in a way that could be mistaken for concealment.**
     Containers are labelled, visible, and accompanied by the authorisation paperwork
     (`Propellant_Handling_SOP.md` §9).
  4. **Expect questions.** Custom propellant may trigger a PESO question from the district
     administration. Plan for the paperwork; do not be surprised by it.
- **IN-SPACe advisory context.** IN-SPACe's advisory guidelines on sub-orbital launches and model
  rocketry set authorisation thresholds based on total impulse. As recorded in the club roadmap:
  **below 10,000 N·s, inform the local administration; between 10,000 and 40,960 N·s, 30 days' prior
  intimation plus advisory; IN-SPACe authorisation is required above 40,960 N·s (≈ O-class).** All of
  the club's current and near-term work sits far below these thresholds. **We still inform.** Being
  under a threshold is not the same as being invisible.

### 3.3 Distance is your primary safety assurance

> **Nakka positions himself and all other personnel 250–300 ft (75–100 m) away from a *proven* motor,
> and even farther for a new design.**

This is not a suggestion. Distance is what protects you, because **you cannot outrun a motor case
failure and you cannot predict it.** A burst case throws fragments hundreds of metres at lethal
velocity; a nozzle failure can send a jet of flame laterally.

- **75–100 m minimum for a proven motor design** (proven = at least 3 successful firings of the
  identical design).
- **150 m or more for a new design**, new propellant batch, new case, or new nozzle geometry.
- **More again as impulse rises.** Scale the distance with propellant mass, not with confidence.
- **Hard cover matters more than raw distance.** A trench, an earth berm, a concrete wall, or the far
  side of a vehicle's engine block converts distance into protection. A person standing in the open at
  100 m is less safe than a person crouched behind a berm at 50 m.

### 3.4 The "beginners stay with proven things" rule

Straight from Nakka's safety rules, and binding on this club:

1. **Beginners should work only with well-proven propellants and well-proven motor designs.**
   Propellant development is for people with real experience and theoretical knowledge. Even small
   amounts of certain additives dramatically change burning characteristics and can cause catastrophic
   failure of an otherwise proven design.
2. **High-energy oxidisers (chlorates, perchlorates) for igniter pyrolants: small quantities only,
   proven formulations only.**
3. **High-energy oxidisers for propellants — potassium perchlorate, ammonium perchlorate — are for
   people with years of experience working safely with lower-energy oxidisers such as the nitrates.**
   This club does not have that experience. **This club does not use them.**
4. **Do not "improve" the formula.** KNSB is 65% KNO₃ / 35% sorbitol by mass. That is the formula. If
   you want to change it, that is a research programme with its own authorisation, its own hazard
   analysis, and its own test series — not an afternoon experiment.
5. **Avoid "boilerplate" motor designs.** Thick-walled heavy contraptions store an incredible amount
   of energy before bursting, which *increases* risk on failure. Cases should be sized to burst at
   **no more than 2.5 × MEOP**; **1.5 is the minimum acceptable safety margin**.
6. **Hydrostatic proof test every new motor design.** Fill the sealed motor with water, pressurise to
   **1.2 × MEOP**, with a **plywood shield between the motor and the operator** in case trapped air is
   present. Compressed water stores little energy, but trapped air does not forgive.

### 3.5 Recognised causes of amateur motor failure, ranked by how often they bite

| Rank | Cause | Prevention |
|---|---|---|
| 1 | **Grain cracks and voids** | Slow insulated cooling, tap the mould, density check every grain, careful demoulding |
| 2 | **Inhibitor debonding** | Tap test on every segment after full cure; reject inconsistent segments |
| 3 | **Over-pressurisation from an oversized igniter** | Scale the igniter to the motor; start small; never add "a bit more powder to be sure" |
| 4 | **Erosive burning** | Port-to-throat area ratio ≥ 2 throughout the burn; KNSB is prone to *negative* erosive burning |
| 5 | **Nozzle erosion or blockage** | Correct material, correct throat, igniter sized so it cannot plug the throat |
| 6 | **Case burst from wrong material or undocumented repair** | Documented design, 2.5 × MEOP burst margin, no field repairs |
| 7 | **Uncommanded ignition from stray current or static** | Shunted leads, grounded work, verified safe/arm circuit, distance |

---

## 4. Roles, responsibilities, and authority

### 4.1 Safety Officer

**Appointment:** nominated by the club, approved by the faculty advisor, and **independent of the
project being tested** wherever possible. A Safety Officer does not also act as Test Director on the
same operation.

**Duties:**

- Owns this manual and all subordinate procedures. Keeps them current. Runs the 6-month review.
- Runs safety induction for every new member before they attend any energetic session, and records it.
- **Inspects and signs off** the PPE and equipment register before every energetic session: dunk
  bucket filled, extinguishers in date and pressurised, first aid kit complete, escape route clear,
  grounding verified, thermometers calibrated.
- Verifies that every person present is trained, fit for duty, and wearing the required PPE.
- Verifies that only authorised, documented materials are present, and that quantities are within the
  §5.4 limits.
- Maintains the **incident and near-miss log** (§8).
- **Has the authority to stop any activity, at any time, for any reason, without needing to justify it
  in the moment.** This authority cannot be overruled by the Test Director, the project lead, the
  faculty advisor, or anyone else present.
- Signs the written **go / no-go** decision before each test.
- Leads the post-incident investigation.
- Maintains the club's safety training records and equipment calibration records.

**Minimum qualifications:** a club member with at least 6 months of continuous involvement, who has
attended (not merely watched) at least **3 static fires** and **2 propellant casting sessions**, and
who has read this manual and the four subordinate procedures in full.

### 4.2 Test Director

**Appointment:** for each individual test, named in writing in the test plan. One person, named, per
test. Never "whoever is around".

**Duties:**

- Owns the test plan and the countdown. Is the only person who issues firing commands.
- Verifies that the test article matches the design that was analysed and proof-tested. **No
  undocumented changes.**
- Runs the pre-test briefing: hazards, sequence, abort criteria, medevac route, who does what.
- Confirms the checklist is complete, signed by the Safety Officer, before arming.
- **Controls the arming key.** It is physically on their person, not "on the table".
- Calls the countdown, calls the abort, calls the misfire.
- Owns the data: ensures recording is running and synced to the fire command *before* arming.
- Writes the test report within 24 hours.

**Minimum qualifications:** has acted as Test Director under supervision for at least 2 tests, or has
been formally signed off by the Safety Officer and faculty advisor.

### 4.3 Range Safety

**Appointment:** one person per test day, distinct from the Safety Officer and Test Director where
club size allows. For very small tests these roles may be combined, and if so, the combination must be
explicitly recorded in the test plan.

**Duties:**

- Owns the **exclusion zone**: physically checks that the perimeter is clear before each arming, and
  confirms verbally, on the radio or by signal, that it is clear.
- Owns the **downrange check**: nobody and nothing downrange, on the line of flight or the blast
  fan, including in the lateral ±45° sectors.
- Confirms the **fire cover** is present and usable.
- Confirms **communications**: everyone in the party can hear a shouted "STOP" or an audible horn.
  If the site is big enough that shouting does not work, a horn, whistle, or radio is mandatory.
- Owns the **weather watch**: wind speed and direction, gusts, lightning within 10 km, visibility,
  remaining daylight.
- Owns **site access control**: no vehicles, no walkers, no livestock, no curious public.
- Owns the **escape routes**: physically walks them before the test and confirms they are clear.
- **Announces "RANGE IS CLEAR" or "RANGE IS NOT CLEAR".** Only Range Safety says this. Nobody else may
  say it, and no arming happens without it.
- **Has independent abort authority identical to the Safety Officer's.**

### 4.4 The authority to abort

> **ANY person present — member, mentor, faculty advisor, or visitor — may call "ABORT" or "STOP" at
> any time, for any reason, and the operation stops immediately.**

Rules governing this authority:

1. **No justification is required in the moment.** You do not have to explain, defend, or be right.
2. **No one may overrule an abort.** Not the Test Director, not the project lead, not a mentor, not a
   senior member, not the faculty advisor. The operation is stopped. Discussion happens afterwards.
3. **There is no penalty, ever, for calling a false abort.** The club will thank you. A false abort
   costs a few hours. A missed abort costs an eye.
4. **Anyone who is pressured, mocked, or penalised for calling an abort is reported to the Safety
   Committee** — the person applying the pressure is disciplined under §9, not the person who aborted.
5. **On hearing "ABORT" or "STOP":** stop what you are doing, do not touch anything, do not move
   towards the hazard, and await instructions from the Test Director or Safety Officer.
6. **On hearing "FIRE" or "EMERGENCY":** move away from the hazard along the pre-briefed escape route,
   to the pre-briefed muster point, and stay there. Do not re-enter until the Safety Officer says so
   explicitly.

### 4.5 The mandatory "STOP WORK" authority vested in every member

This is broader than abort authority and applies to **all** club activity, not just tests:

> **Every member, of every seniority, including first-week members with no experience whatsoever, has
> the unconditional authority to stop any activity they believe is unsafe.**

This includes:

- Stopping another member's propellant work
- Stopping a machining operation
- Stopping a launch
- Stopping a senior member or a mentor
- Stopping a session because *you personally* are too tired, distracted, or unwell to continue safely

**Using it is expected. Not using it, when you had a concern, is itself a disciplinary matter.** If you
saw something wrong and said nothing, you are part of the problem.

---

## 5. Personal conduct rules

### 5.1 The two-person rule — no lone working with propellant

> **No member may ever be alone with propellant, oxidiser, mixed powder, molten propellant, ignition
> powder, or a loaded motor. Minimum two people, always.**

Reasons, stated plainly:

1. If you are burned, you cannot drive yourself to hospital and you may not be able to use a phone.
2. If a fire starts, one person cannot both fight it and get help.
3. **Someone who is alone and slightly uncertain will guess. Someone with a colleague watching will
   check.** The second person is a procedural safeguard as much as a rescue capability.

**The second person must be:**

- Awake, present, and actively watching — not in another room, not in a vehicle, not on their phone
- Trained in the relevant procedure and the emergency actions of §7
- Able to raise an alarm, call emergency services, and reach a hospital
- **Not a member of the public, not a child, not an untrained friend who "just wants to watch"**

**Both persons must know where the nearest working telephone is and how to describe the location to
emergency services.** For every session, the location is written down and posted before work starts —
in an emergency, you will not remember it.

### 5.2 Fitness for duty

| Condition | Rule |
|---|---|
| **Tired** | No propellant work. If you have had less than 6 hours' sleep, or you have been working on your feet for more than 10 hours, you do not handle energetics. |
| **Rushed** | No propellant work. If there is a hard deadline in the next 2 hours, reschedule. **Schedule pressure is a hazard, and it is a hazard that we can see coming.** |
| **Alcohol** | **Zero. No alcohol in your system within 12 hours of any energetic work**, and none on site at any time. There is no threshold, no exception for "just one beer", and no discussion. |
| **Recreational drugs / impairing medication** | Zero on site. Prescription medication that causes drowsiness or impairs judgement must be disclosed to the Safety Officer, who decides whether you work. |
| **Illness** | Fever, vomiting, dizziness, or a hand injury that affects grip: no propellant work. |
| **Emotional distress** | Significant personal stress, argument, or distraction: tell the Safety Officer and stand down. **This is not weakness. This is the rule.** |
| **Time pressure from a competition or review** | Not a valid reason to compress any step. Ever. |
| **Heat** | Bengaluru summer site work: hydration and shade mandatory. Heat exhaustion looks like carelessness and causes the same mistakes. |

### 5.3 Phone-free and distraction-free during energetic operations

> **From the moment propellant is uncovered, or a motor is brought to the pad, until the operation is
> closed out: phones are away.**

- **No phone in hand.** Photographs and video are taken by the **designated documentarian only**, who
  is briefed on where they may stand and **may never enter the exclusion zone** to get a better shot.
- **No calls, no messages, no scrolling.** A phone in the hand of a person holding a thermometer is a
  person not reading the thermometer.
- **The documentarian's position is fixed and briefed before arming.** "Just one step closer" has
  killed people.
- **No headphones.** You must be able to hear "ABORT", "FIRE", or a shout from any direction.
- **Visitors and onlookers:** permitted only at the pre-briefed viewing point, behind the firing line,
  only with the Safety Officer's explicit consent, only with the PPE appropriate to their distance,
  and only after a short safety brief. **No visitor ever enters the exclusion zone for any reason.**

### 5.4 Quantity discipline

> **Keep batch sizes to the minimum needed for the job at hand.** (Nakka safety rule 5)

| Activity | Club limit |
|---|---|
| Oxidiser out of storage at one time | 500 g |
| Mixed dry powder at one time | 250 g |
| Molten propellant in the vessel at one time | 250 g |
| Total propellant per casting session | 1 kg |
| Ignition powder mixed at one time | 50 g |
| Finished propellant stored in the club's possession | 3 kg, separated and registered |
| Propellant in transit in one vehicle | 2 kg, in one sealed labelled container |
| Propellant on the test site (excluding the motor being fired) | 250 g |

These limits stand **until the Safety Committee raises them in writing**, based on demonstrated
heritage — a track record of successful, documented, incident-free sessions at the current level.

### 5.5 PPE — non-negotiable minimum

Full detail and quantities are in `PPE_and_Equipment_Register.md`. The non-negotiable minimum for any
propellant work:

- **Chemical splash goggles** (not plain safety glasses) — for molten propellant and any liquid
- **Full face shield** over the goggles whenever molten propellant is being poured or a motor is being
  approached after firing
- **Heat-resistant gloves** for handling hot vessels and moulds
- **Cotton or flame-resistant (FR) clothing, full sleeves, full-length trousers, closed shoes.** **No
  synthetics** near propellant — see the box below.
- **Leather apron** for casting
- **Ear defenders** at any firing

> ### 🔴 NO SYNTHETIC CLOTHING NEAR PROPELLANT
> Nylon, polyester, rayon, and synthetic blends **melt** when exposed to flame or molten propellant and
> **fuse into skin**. Molten polymer burns are far worse than equivalent flash burns, are much harder
> to treat, and routinely require grafting. **Wear cotton or FR-treated fabric, full coverage, with
> nothing synthetic against the skin.** This includes synthetic inner layers, synthetic socks, and
> synthetic hoodies. It also applies to synthetic fleece — a fleece jacket will melt onto your torso.

---

## 6. Emergency equipment — the three-item rule

> **Nakka safety rule 3: when working with propellants, always be alert and take the approach that
> such could ignite at any time. THREE items must ALWAYS be present:**
> 1. **A dunk bucket full of water**
> 2. **A fire extinguisher**
> 3. **A planned escape route**

Every one of the three must be present and verified **before** propellant is uncovered, not fetched
after something goes wrong. The Safety Officer's pre-session inspection checks all three and records
it. Full specification and quantities: `PPE_and_Equipment_Register.md`.

**The dunk bucket** is a large bucket or drum of clean water positioned **within 2 metres of the
workstation**, with enough depth to fully submerge a hand and forearm. Its purpose is immediate
cooling of a burn and extinguishing of clothing or a small quantity of burning propellant. It must be
**full** — an empty or half-full bucket is a failure of the three-item rule and stops the session.

**The fire extinguisher** must be **in date, pressurised (gauge in the green), and appropriate to the
fire class** — see `PPE_and_Equipment_Register.md` §4 for which type goes where. Water must never be
used on an electrical fire or on burning metal.

**The planned escape route** is a physical route away from the hazard to a muster point, **walked and
confirmed clear by Range Safety before the session**, and known to every person present. It must not
be the route along which the hazard will travel, and it must not be blocked by equipment, vehicles, or
a locked gate. **A planned escape route that exists only in conversation is not an escape route.**

---

## 7. Emergency procedures

> **Read this section before you need it. In an emergency you will not have time to read it.**

### 7.0 Universal first actions

Whoever notices the emergency:

1. **Shout clearly and loudly** — "FIRE", "BURN", or "EMERGENCY" — so that everyone knows, in words
   everyone understands.
2. **Move people away from the hazard**, along the pre-briefed escape route, to the muster point.
3. **Account for everyone** at the muster point, by name, out loud.
4. **Call for help** — 108 (ambulance) or 112 (all emergencies, India). Give the **written location**
   from the session sheet, the number and type of injuries, and your callback number.
5. **Do not become a second casualty.** No heroic entries into a burning area for equipment. Equipment
   is replaceable; you are not.

### 7.1 Fire — small (a container, a small spill, a small propellant piece)

Only attempt to fight it if **all** of the following are true: the fire is smaller than roughly a
wastebasket; you are between the fire and the escape route; you have the correct extinguisher in hand;
and there is a second person present. Otherwise, evacuate.

1. **Sound the alarm** — "FIRE".
2. **Remove ignition sources and unburned propellant from the vicinity if it is safe to do so.**
   Spreading the fire is the thing you are trying to prevent.
3. **Use the correct extinguisher** (see `PPE_and_Equipment_Register.md` §4) with the **PASS**
   technique: **P**ull the pin, **A**im at the base of the fire, **S**queeze the handle, **S**weep
   side to side.
4. **For burning propellant, water in quantity is your friend** — a large volume of water cools the
   propellant below its ignition temperature and is the single most effective agent available to us.
   Use the dunk bucket and the water bucket. **Do not use a small amount of water on molten
   propellant** — spattering spreads it.
5. **Alternatively, smother it** with the fire blanket, or with dry sand. Sand is effective on small
   pool fires and molten-propellant fires.
6. **Do not use a CO₂ or dry-powder extinguisher as the primary means on a propellant fire.** These
   suppress the flame but do **not** cool the propellant, which can reignite the moment air returns.
   Use them only to knock down a flame while you bring water, or on surrounding Class A/B fires.
7. **Keep back.** A propellant fire can transition to a violent burn of the whole batch without warning.
8. **If it does transition, evacuate immediately.** Propellant fires are not fought. They are waited
   out, from a distance. KNSB burns hot and produces large volumes of smoke — assume everything within
   10 m is destroyed.

### 7.2 Fire — large, or growing, or involving a motor

1. **Evacuate immediately.** Do not attempt to extinguish.
2. **Withdraw to at least 100 m**, ideally behind hard cover, and account for everyone.
3. **Call 101 (fire service) and 108 (ambulance).** Give the written location.
4. **Warn others off** — stop traffic, keep the public away.
5. **Assume the site is contaminated** with unburned oxidiser and hot debris. **Nobody re-enters until
   the Safety Officer, with the fire service if present, declares it safe.**
6. **Preserve the scene** for investigation once it is safe — do not clean up before it is documented.

### 7.3 Burn injury

Severity drives the response. When in doubt, treat as more severe.

| Severity | Signs | Action |
|---|---|---|
| **Minor (superficial)** | Redness, mild pain, no blistering, small area | **Cool with clean running water for 20 minutes.** Do not use ice. Cover with a sterile non-adherent dressing. |
| **Partial thickness** | Blistering, wet appearance, significant pain | **Cool with clean running water for 20 minutes.** Do not burst blisters. Cover loosely with a sterile non-adherent burn dressing. **Seek medical assessment.** |
| **Full thickness** | White, charred, waxy, or leathery; may be painless at the centre | **Do not cool extensively** (risk of hypothermia). Cover with a clean dry sterile dressing. **Emergency transport immediately.** |
| **Any burn to face, hands, feet, joints, or genitals; any burn larger than the casualty's palm; any chemical burn; any burn with inhaled smoke** | — | **Emergency transport immediately. Call 108.** |
| **Molten propellant on skin** | Adherent, hot, sticky material | **Cool immediately with copious water; do not attempt to pick off solidified propellant** — you will tear skin. Cover and transport. |

**Golden rules for burns:**

- **Do not apply** ice, butter, ghee, oil, toothpaste, turmeric, toothpaste, cotton wool, or any home
  remedy. These are the standard Indian first-aid mistakes and they make burns worse and complicate
  treatment.
- **Do not burst blisters.**
- **Do not remove clothing that is stuck to a burn.** Cut around it.
- **Cooling must start within seconds** and continue for **20 minutes**. The dunk bucket exists for
  exactly this. **Immediate cooling measurably reduces the final depth of a burn** — a 3-second delay
  is a worse injury.
- **Remove rings, watches, and tight items from the affected limb before swelling begins.**
- **Keep the casualty warm and calm** after cooling; treat for shock (lie down, elevate the legs, do
  not give food or drink).
- **Every burn beyond trivial gets medically assessed.** A burn that looks minor on day one can
  become infected and serious. The club's incident log records the injury and the treatment.

### 7.4 Eye injury

**Any eye injury or suspected eye injury is an emergency. Call 108 / go to hospital immediately.**

| Cause | Immediate action |
|---|---|
| **Chemical (dry powder, molten propellant, oxidiser solution)** | **Irrigate immediately with clean water or eyewash for at least 15 minutes**, holding the eyelid open and rolling the eye. Irrigate from the inner corner outwards so the runoff does not enter the other eye. **Do not use neutralising agents.** Continue irrigating en route to hospital. Remove contact lenses if present and easily removable. |
| **Foreign body / dust** | **Do not rub the eye.** Irrigate with clean water. **Do not attempt to remove an embedded object.** Cover both eyes loosely (to stop the uninjured eye's movement moving the injured one) and go to hospital. |
| **Thermal / flash** | Cool the surrounding skin with clean water, cover both eyes loosely, transport immediately. |
| **Blunt impact / blast** | **Do not press, rub, or apply pressure.** Shield the eye with a rigid eye shield or the bottom of a clean paper cup. Transport immediately, lying down if possible. |

**Everyone on site must know where the eyewash station or eyewash bottle is before work starts.** The
nearest tap must be identified at the start of each session — in the field this is often a water
container, and it must be filled and located at the workstation.

### 7.5 Accidental ignition of propellant

Signs: sudden flame, hissing, bright light, smoke, a sharp report.

1. **Do not look at it.** Turn your face away and close your eyes as you turn — you are protecting
   against flash and ejecta.
2. **Move away immediately, at right angles to the plume.** Never along the axis of a burning jet, and
   never through the smoke.
3. **Do not attempt to retrieve anything.** Nothing on the bench is worth your hand.
4. **Shield your face and eyes with your arm as you move.**
5. **Once clear, account for everyone**, then treat injuries (7.3, 7.4) and call for help.
6. **One member is designated to check for secondary ignition** — the ignition may have thrown burning
   material onto other propellant, dry grass, or a container. Address this **only from a position of
   safety**, and only after the primary event has clearly finished.
7. **Everyone exposed to the smoke or fumes is assessed medically.** Potassium-based smoke and
   decomposition products are respiratory irritants. Anyone with coughing, wheezing, or shortness of
   breath is transported.

### 7.6 Misfire — and the "wait then approach" rule

> **This is the single most dangerous routine situation in amateur rocketry, because it invites exactly
> the wrong instinct. The motor did not fire. Your instinct is to go and look. That instinct kills
> people.**

**The rule:**

> **If an igniter or motor fails to initiate: WAIT. Then approach cautiously, and ALWAYS disconnect the
> igniter leads FIRST.**
> *(Nakka safety rule 7)*

**The procedure:**

1. **Continue the count.** If the motor has not ignited within **5 seconds** of the fire command, call
   **"MISFIRE"**.
2. **Make safe immediately, without approaching:**
   - Turn the **ARM switch to SAFE**.
   - **Remove the arming key** and put it in your pocket.
   - **Disconnect the firing-circuit power source** (battery) at the box, or have the person at the box
     do so on your instruction.
   - **Announce "SYSTEM SAFE"** — and everyone keeps waiting anyway.
3. **WAIT.** Minimum waiting times, and these are minimums, not targets:

   | Situation | Minimum wait before anyone approaches |
   |---|---|
   | Igniter did not initiate; motor clearly unburned | **5 minutes** |
   | Motor smoked, sparked, or partially burned, then stopped | **15 minutes** |
   | Motor ignited and burned, and appears finished | **10 minutes**, and follow the static test post-fire procedure |
   | Any situation you do not understand | **30 minutes**, and the Safety Officer decides |

   **Why wait?** A slow-burning igniter, a smouldering grain, or a delayed pyrotechnic reaction can
   initiate late. Heat-soaked hardware can also reignite propellant when air reaches it. **The wait is
   cheap. The alternative is a motor starting while your hand is on it.**

4. **Approach cautiously.** Two people minimum. Safety Officer leads. Walk on the side of the motor
   where you are not exposed to the nozzle or the case ends. Do not run. Do not reach.
5. **DISCONNECT THE IGNITER LEADS FIRST — BEFORE ANYTHING ELSE.**
   - Disconnect the igniter leads from the firing circuit at the **far end** from the motor first if
     the run is long.
   - **Then disconnect the igniter from the motor.**
   - **Then, and only then, touch or inspect anything else.**
   - **Never tug on the igniter wires.** A tug can move the igniter inside the grain, or mechanically
     disturb a hot grain.
   - **Immediately shunt the igniter leads** (twist the bared ends together) once they are free.
6. **Do not attempt to re-fire the motor on the same igniter** unless the Test Director explicitly
   authorises it after inspection, and the motor has been verified cold and undamaged.
7. **Do not extract a partially burned grain from a case by force.** Treat it as live propellant.
8. **Log the misfire** in the incident log with the full history: the igniter type and weight, the
   circuit, the measured current, the timing, the weather. Misfires are data. They are also warnings.

### 7.7 Emergency contacts and muster point

Before **every** session, the session sheet records and posts:

- **Site location in words a stranger could follow** (road, landmark, GPS coordinates if available)
- **Nearest hospital** with a burns/emergency capability, its distance, and the route there
- **Emergency numbers:** 112 (all-in-one), 108 (ambulance), 101 (fire)
- **The muster point** and the escape routes
- **Who is the first-aider / who holds the first aid kit**
- **Names of every person on site**, and their emergency contact numbers
- **The faculty advisor's and Safety Officer's phone numbers**

**The muster point is where everyone goes and stays.** It is fixed before work begins, it is upwind of
the work area, it has a clear route out, and **nobody leaves it to re-enter the hazard area until the
Safety Officer says so, by name.**

---

## 8. Reporting and incident logging

### 8.1 What must be reported

| Category | Definition | Timeline |
|---|---|---|
| **Incident** | Any injury, any fire, any unplanned ignition, any motor case failure (CATO), any property damage, any emergency-services call | **Immediately** to the Safety Officer, and a written report **within 24 hours** |
| **Near miss** | Any event that could have caused injury or damage but did not — a dropped grain, a spill, a stray-current indication, an un-shunted lead discovered, a person found downrange, an extinguisher found empty, an abort called | Written report **within 48 hours**, no matter how trivial it seemed |
| **Anomaly** | A test or flight that produced unexpected data — off-nominal pressure curve, early/late ignition, unexpected nozzle erosion, grain defect found after the fact | Written note in the test report, and flagged at the next club meeting |
| **Equipment defect** | Failed PPE, expired extinguisher, damaged grounding strap, faulty thermometer | Report to the Safety Officer immediately; equipment removed from service and tagged |

> **Near misses are the most valuable data the club has.** They are free lessons. Hiding one — through
> embarrassment, or through a belief that it was trivial — is a serious disciplinary matter (§9). The
> accident you prevent by reporting a near miss is the one that would have injured the next member.

### 8.2 Incident report contents

Every incident and near-miss report contains:

1. **Date, time, and location** (exact, with coordinates if available)
2. **People present**, by name and role (Safety Officer, Test Director, Range Safety, others)
3. **What was being done** — the exact operation, step in the procedure, and batch or motor identifier
4. **Materials involved** — formulation, batch number, mass, age, and where it came from
5. **What happened** — factual, chronological, no interpretation
6. **What was expected to happen**
7. **Injuries** — nature, severity, treatment given, and medical follow-up
8. **Damage** — to equipment, property, or the environment
9. **Immediate actions taken**
10. **Witness statements** — each in their own words, as soon as possible, before discussion
11. **Photographs and video** if any exist
12. **Root cause analysis** — see §8.3
13. **Corrective actions** — specific, with a named owner and a deadline
14. **Effect on this manual or the subordinate procedures** — what text changes as a result

### 8.3 Investigation

- The **Safety Officer leads** the investigation. For serious incidents, the faculty advisor is
  involved and the Safety Committee reviews.
- **The purpose is to find causes, not to find someone to blame.** Blame produces silence; silence
  produces the next accident.
- **Ask "why" at least five times.** "The igniter did not fire" → "the circuit was open" → "the shunt
  was not removed" → "the checklist was not read" → "we were running late and skipped it" → the real
  cause is the schedule pressure, not the person holding the wires.
- **Investigate the procedure, not just the person.** If a competent, trained member made a mistake,
  the procedure is at fault for allowing it.
- **Look for the second cause.** Almost every incident has more than one.
- **Findings are written down** and distributed to all members.
- **Corrective actions are tracked to closure** and verified at the next session.

### 8.4 Records retention

- Incident and near-miss reports: **retained permanently** by the club, with a copy to the faculty
  advisor. These survive member graduation — that is the point.
- Test reports, batch records, and calibration records: **retained permanently.**
- Training and authorisation records: **retained while the member is active, plus 3 years.**

---

## 9. Disciplinary process and consequences

### 9.1 Philosophy

The club's disciplinary process exists for one purpose: **to prevent the next accident.** It is not
retributive. But it is **not negotiable either**, because the alternative to enforcement is an injury,
and an injury to a student in a club activity is unacceptable and entirely preventable.

### 9.2 Immediate actions (taken in the moment, by the Safety Officer, no discussion)

| Finding | Immediate action |
|---|---|
| Working alone with propellant | **Full stop.** Session ends. Member stood down from all energetic work pending review. |
| Working under the influence of alcohol or drugs | **Full stop.** Member removed from site. Escorted if necessary. |
| Igniter leads un-shunted when they should be shunted | **Full stop.** Session ends. Review. |
| Dunk bucket empty / extinguisher missing / escape route blocked while propellant is uncovered | **Full stop.** Session ends. Review. |
| PPE not worn as required | **Full stop.** Member corrects it or leaves the work area. |
| Someone downrange during arming | **Full stop.** Session ends. Review. |
| A person entering the exclusion zone without authorisation | **Full stop.** Session ends. Review. |
| Deliberate bypass of a safety step, or falsifying a checklist | **Full stop.** Referred directly to the Safety Committee. |
| Pressuring or mocking someone for calling an abort or a stop-work | **Full stop.** Referred directly to the Safety Committee. |

### 9.3 Escalation ladder

| Level | Trigger | Consequence |
|---|---|---|
| **1 — Verbal correction** | First minor lapse: forgetting a glove, leaving a tool where it should not be, minor checklist omission caught before harm | Corrected in the moment. Recorded in the session log. **No further action, provided it does not recur.** |
| **2 — Written warning** | Repeat of a minor lapse, or a single moderate lapse: an un-shunted lead, PPE removed in a hazardous area, phone use during an energetic operation | Written warning issued by the Safety Officer and copied to the faculty advisor. **Mandatory re-reading of the relevant procedure and a re-brief before returning to energetic work.** |
| **3 — Suspension from energetic work** | A serious lapse, or three written warnings: any §9.2 finding short of deliberate sabotage; failure to report a near miss | **Suspended from all propellant, igniter, and firing activity for a minimum of 30 days.** May continue non-energetic work (design, simulation, documentation) at the Safety Committee's discretion. Return requires a re-brief and a signed acknowledgement. |
| **4 — Removal from the club** | Deliberate violation of a safety rule; falsifying records; concealing an incident or near miss; retaliation against someone who called a stop; bringing prohibited materials to club activity; a third suspension | **Removed from the club.** Notified in writing, with reasons. The faculty advisor and head of institution are informed. |
| **5 — Referral to authorities** | Any incident involving injury to a member of the public; damage to third-party property; possession or use of prohibited or unlicensed materials; any event requiring police or fire service attendance | **Reported to the faculty advisor, the head of institution, and the relevant authority** (police, PESO, or the district administration) as the law and the circumstances require. |

### 9.4 Principles of enforcement

1. **Consistency.** The rules apply identically to first-years, final-years, office bearers, mentors,
   and the faculty advisor. **A senior member is held to a higher standard, not a lower one.**
2. **Speed.** Immediate action happens immediately. Review happens within 7 days.
3. **Right of explanation.** The member may explain their account to the Safety Committee before a
   Level 3 or 4 consequence is applied. This is a right to be heard, not a right of appeal against the
   facts.
4. **No retaliation.** Any member who reports a violation or calls a stop-work is protected. Action
   against them for doing so is itself a Level 4 matter.
5. **Recording.** Every consequence at Level 2 and above is recorded in the safety records.
6. **Restoration.** A member who completes a suspension and demonstrates corrected behaviour returns
   with no residual penalty and is not treated as a liability. The purpose is correction.
7. **The final authority on a Level 4 or 5 matter** rests with the faculty advisor and the head of
   institution, not with the club officers alone.

---

## 10. Training and authorisation

No member performs any energetic operation without the following, recorded in the club's training
register:

| Stage | Requirement | Who signs off |
|---|---|---|
| **Safety induction** | Read this manual and all four subordinate procedures in full. Attend a briefing by the Safety Officer. Sign the acknowledgement. | Safety Officer |
| **Observation** | Attend at least **2 propellant sessions** and **2 static fires** as an observer only, from the viewing point, with no hands-on involvement. | Safety Officer |
| **Supervised participation** | Perform each task under direct supervision of a competent member: grinding, sifting, weighing, mixing, casting, igniter preparation | Safety Officer |
| **Authorisation** | Demonstrated competence in a task, assessed on a real session, with the correct procedure followed without prompting. Recorded by name and task. | Safety Officer + one other competent member |
| **Test Director / Safety Officer** | Additional requirements per §4.1 and §4.2 | Faculty advisor |

**Authorisation is per-task and does not expire with convenience** — it expires after **6 months of
inactivity** on that task, after which a re-brief is required. Authorisation is revoked automatically
on any Level 3 or higher disciplinary consequence.

---

## 11. Pre-session safety sign-off (the checklist that gates everything)

**This sheet is completed, signed, and physically present at every energetic session. No signature, no
session.**

```
UVCE ROCKETRY CLUB — PRE-SESSION SAFETY SIGN-OFF
Session type: [ ] Propellant prep  [ ] Casting  [ ] Static fire  [ ] Flight
Date: ____________  Location: ______________________________________
Safety Officer: ______________  Test Director: ______________  Range Safety: ______________
Persons present (names + roles): ___________________________________________________
```

**A. Authority and paperwork**

- [ ] Written authorisation for this activity on file, with the correct signatories
- [ ] Test plan / session plan present and briefed to everyone present
- [ ] Landowner / site permission valid and on site (for field work)
- [ ] Local administration informed, where required by the IN-SPACe advisory thresholds

**B. The three-item rule (mandatory whenever propellant is present)**

- [ ] **Dunk bucket** — full, clean water, within 2 m of the workstation, ≥ 20 L
- [ ] **Fire extinguisher** — correct type for the hazard, in date, gauge in the green, within 5 m
- [ ] **Escape route** — physically walked, clear, known to everyone, muster point agreed

**C. People**

- [ ] Minimum two persons present; **no one will be alone with propellant at any time**
- [ ] Everyone fit for duty — no fatigue, no alcohol (12 h), no impairing medication, no illness
- [ ] Everyone's PPE checked: goggles, face shield, gloves, cotton/FR clothing, closed shoes
- [ ] Everyone knows the emergency numbers, the muster point, and the location description
- [ ] Phones away from the work area; documentarian position briefed

**D. Equipment and environment**

- [ ] Thermometer(s) present and verified against a known reference
- [ ] Heating vessel is **thermostatically controlled with no exposed elements**
- [ ] Non-sparking tools only, at the workstation
- [ ] Grounding strap and rod connected and tested for continuity
- [ ] Fire blanket, sand, and spill kit present
- [ ] First aid kit complete, in date, with burn dressings and eyewash
- [ ] Igniter leads **shunted** (firing activities)
- [ ] Safe/Arm box tested — continuity check functional, no current to the igniter when SAFE
- [ ] Ignition system battery fresh; arming key held by the Test Director only
- [ ] Weather checked: wind, gusts, lightning within 10 km, rain, visibility, remaining daylight
- [ ] Exclusion zone defined, physically marked, and cleared; downrange verified clear

**E. Data and documentation**

- [ ] Batch record / motor serial number recorded
- [ ] Data logging and video recording verified **before** arming
- [ ] Camera positions fixed and outside the exclusion zone
- [ ] Incident log and blank report forms on site

**Signatures**

```
Safety Officer: ____________________  Time: ______  Decision: [ ] GO   [ ] NO-GO
Test Director:  ____________________  Time: ______  Decision: [ ] GO   [ ] NO-GO
Range Safety:   ____________________  Time: ______  Decision: [ ] GO   [ ] NO-GO
```

**A single NO-GO from any of the three stops the session.** No discussion required. No override exists.

---

## 12. Document control

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | — | First issue | UVCE Rocketry Club Safety Committee |

**Related documents:**

- `40_SAFETY/PPE_and_Equipment_Register.md`
- `40_SAFETY/Propellant_Handling_SOP.md`
- `40_SAFETY/Static_Test_Procedure.md`
- `40_SAFETY/Flight_Operations_Safety.md`
- `Technical_Reference_Nakka.md` — the technical reference this manual's numbers are drawn from
- `UVCE_Rocketry_Roadmap.md` — programme context and regulatory thresholds

**Primary external sources:**

- **Richard Nakka's Experimental Rocketry Site** (nakka-rocketry.net) — safety guidance, KNSB
  propellant data, ignition, static testing. The four membership criteria, the energy figures, the
  three-item rule, the shunting rule, the misfire rule, the distance figures, and the "no boilerplate"
  and "beginners stay with proven things" rules all originate here.
- **IN-SPACe advisory guidelines on sub-orbital launches and model rocketry** — authorisation
  thresholds, site and landowner requirements, launch checklist and advisory proforma.
- **IN-SPACe Model Rocketry Competition Guidelines** (Doc No. IN-SPACe.MR.Model.CG.01) — competition
  safety rules where the club is flying in that context.
- **Explosives Act 1884 and Explosives Rules 2008, India; PESO** — referenced for awareness of the
  legal framework around oxidiser possession, storage and transport. **Not legal advice.** Confirm
  every specific requirement with the faculty advisor and the competent authority.

---

*This manual is written by students, for students. It is not a substitute for professional advice, for
the source material it cites, or for your own judgement. Where it is incomplete, incomplete means
"stop and ask" — never "assume".*
