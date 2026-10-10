# Stage 4 — Open Book Test

**UVCE Rocketry Club recruitment**

| | |
|---|---|
| **Format** | **Open book.** You may keep the Foundation Reader open. |
| **Time** | 45 minutes |
| **Total marks** | 50 |
| **Pass** | 30 (60%) |

> **This is not an exam about memory.** Everything is in the reader. We are testing whether you
> **read it, can find information in it, and can apply it.** A person who has never seen a rocket but
> reads carefully will pass. A person who skims will not.
>
> **Write in your own words.** Copied sentences score zero even if they are correct — we can tell,
> because we wrote the reader.

---

## Section A — Finding and using the reader (10 marks)

*These test whether you can locate information quickly. Cite the page number.*

**A1.** (2) What is the ideal cast density of KNSB, and what is it used to check?

**A2.** (2) What is the total impulse range of an **E-class** motor?

**A3.** (2) State the lower and upper limits of the acceptable descent rate, and the value we
actually design for.

**A4.** (2) What ratio must be kept at 2 or above, and what problem does it prevent?

**A5.** (2) What are the two structural shock/acceleration requirements the competition specifies?

---

## Section B — Understanding (15 marks)

*Explain in your own words. Two or three sentences each.*

**B1.** (3) Explain why the **CP must be behind the CG**. What happens if it is not?

**B2.** (3) Why is it a problem if the **static margin is too large**? Most people assume more
stability is always better — explain why that is wrong.

**B3.** (3) Our casing rule says it should burst at **no more than 2.5 × MEOP**. Explain why there is
an *upper* limit. Why is a very strong casing not automatically safer?

**B4.** (3) Explain why the KNSB grain is **freestanding** rather than bonded to the casing. Refer to
the material properties in your answer.

**B5.** (3) Explain why **KNSB being a "mesa" propellant** makes motor design harder than it would be
for a normal propellant.

---

## Section C — Calculation (10 marks)

*Show your working. Units matter.*

**C1.** (3) A motor produces an average thrust of **12 N for 2 seconds**. What is its total impulse,
and what class is it?

**C2.** (3) A rocket has a dry mass of **300 g** and carries **25 g** of propellant. What is its
propellant mass fraction, as a percentage?

**C3.** (4) A descending section has a mass of **1.2 kg**. Using `ρ = 1.2 kg/m³` and `C_d = 0.75`,
calculate the canopy area needed for a descent rate of **4 m/s**. Then state the canopy diameter.

*(Formula from page 7. `g = 9.81 m/s²`.)*

---

## Section D — Diagnosis (10 marks)

*The most important section. These are the situations you will actually face.*

**D1.** (5) A static test motor ignites but only reaches **1.2 MPa** instead of the predicted
**3 MPa**, and the burn takes **5.1 s** instead of **3.1 s**.

List **three plausible causes** and, for each, state what you would check or measure to confirm or
rule it out.

**D2.** (5) A rocket flies, but instead of going straight up it curves into the wind and loses most
of its altitude. It recovers intact.

- **(a)** What is this behaviour called?
- **(b)** What is the most likely cause?
- **(c)** Name two things you could change to fix it.

---

## Section E — Judgement (5 marks)

*There is no single right answer. We are looking at how you think.*

**E1.** (5) You are the Safety Officer at a static test. Everything is ready. The motor is mounted, the
igniter is installed, and the firing box is armed. The countdown is at **T−10 seconds**.

You notice that the person who installed the igniter **cannot clearly remember whether they shunted
the leads before connecting**, and there is no record on the checklist.

**What do you do, and why?**

---

---

# ANSWER KEY — FOR MARKERS ONLY

> Do not distribute this. Mark consistently and generously on Sections B, D and E: we are testing
> understanding, not phrasing. **Award full marks for a correct idea expressed clumsily.**

---

## Section A (10)

| Q | Answer | Page |
|---|---|---|
| **A1** | **1.841 g/cm³**. Used to check cast grain quality — comparing measured density against ideal reveals voids or air inclusion. | 5 |
| **A2** | **20 – 40 N·s** | 3 |
| **A3** | Lower **2 m/s**, upper **5 m/s**. We design for **~3.5 m/s** (middle of the band). | 7 |
| **A4** | **Port-to-throat area ratio** (A_port / A_t). Prevents **erosive burning** — KNSB is especially prone to *negative* erosive burning. | 5 |
| **A5** | Survive **15 g** launch acceleration and **30 g** shock. | 6 |

## Section B (15)

**B1 (3).** The CP is where aerodynamic forces act, the CG where gravity acts. With the CP *behind*
the CG, any disturbance causes the aerodynamic force to push the tail back into line, so the rocket
self-corrects. If the CP is *ahead* of the CG, the same disturbance pushes the nose further off
course and the rocket tumbles.
*(Award 3 for correct mechanism, 1–2 for stating the rule without explanation.)*

**B2 (3).** Too much static margin (above ~2 calibers) makes the rocket **over-stable**. Instead of
correcting only when disturbed, it aggressively turns to align with the relative wind — so when it
encounters a crosswind, it **weathercocks**, turning into the wind and flying sideways rather than
straight up. It loses most of its altitude and can be dangerous.
*(Key word: weathercocking. Award full marks if the concept is right.)*

**B3 (3).** A stronger, thicker casing **stores more energy before it fails**. When it eventually
bursts, it releases that stored energy more violently — larger fragments, higher velocity, worse
outcome. A casing sized to fail early and gently is safer than one built enormously strong. Margin is
for **uncertainty**, not for reassurance; beyond a point it adds risk rather than removing it.
*(Award full marks for the energy-storage reasoning.)*

**B4 (3).** KNSB is **strong in compression but weak in tension** — elastic modulus 5.84 GPa, tensile
strength only 7.2 N/mm². A **freestanding** grain is loaded almost purely in **compression** by
chamber pressure, which it handles reliably. A **case-bonded** grain is pulled in **tension** as the
casing expands, which cracks the brittle propellant, increasing burning area and causing a burst.

**B5 (3).** Most propellants follow a single power law (r = a·Pⁿ) across all pressures, so one set of
coefficients describes the motor. **KNSB does not** — its pressure exponent changes with regime and
becomes very small or negative over some ranges. So you must **measure `a` and `n` for your specific
materials within your actual operating pressure range**, which requires a strand burner. A single
global fit will mispredict chamber pressure and burn time.

## Section C (10)

**C1 (3).** `I_t = F × t = 12 × 2 = 24 N·s`. That is **E-class** (20–40 N·s).

**C2 (3).** Total mass = 300 + 25 = **325 g**. Fraction = 25 / 325 = **0.0769 = 7.7%**.
*(Award full marks for 7.7% or 7.69%. Accept 25/300 = 8.3% with a note — that is propellant/dry
ratio, not mass fraction — award 2.)*

**C3 (4).** 
```
v² = 2mg / (ρ Cd A)
A  = 2mg / (ρ Cd v²)
   = (2 × 1.2 × 9.81) / (1.2 × 0.75 × 16)
   = 23.544 / 14.4
   = 1.635 m²
```
**A ≈ 1.64 m²**

```
A = πD²/4  →  D = √(4A/π) = √(4 × 1.635 / 3.1416) = √2.082
D ≈ 1.44 m
```
**D ≈ 1.44 m** (about 1.4–1.5 m)

*(Award 2 for the area, 2 for the diameter. Follow-through marks if the area is wrong but the
diameter method is correct.)*

## Section D (10)

**D1 (5).** Accept any **three** of the following, each with a sensible check. Award ~1.7 per
well-reasoned cause-and-check pair.

| Cause | How to confirm |
|---|---|
| **Burn-rate coefficient `a` is lower than assumed** — very likely, since KNSB is mesa and as-obtained materials run lower | Measure it with a **strand burner** using the actual materials |
| **Throat is larger than intended** — a small drilling error has a big effect at small throats | Measure the throat with **calipers**; recalculate expected pressure |
| **Voids or low grain density** — excess burning area would normally *raise* pressure, but irregular burning can lower it | **Density check** against 1.841 g/cm³; **coin tap test** |
| **Propellant moisture** — residual water suppresses burn rate | Check dessication state; check casting records; remeasure with dried material |
| **Igniter too weak / delayed ignition** — poor initial pressurisation | Inspect the pressure trace for a slow ramp; try a slightly larger igniter |
| **Oxidiser particle size too coarse** | Check milling time and records; sieve analysis |

> **Note for markers:** the *longer burn time* is the key clue — lower pressure and lower burn rate go
> together. A candidate who notices this connection and reasons from it deserves full marks even if
> their listed causes differ.

**D2 (5).**
- **(a)** **Weathercocking** (1)
- **(b)** **Too much static margin** — over-stable, so it aligns with the relative wind instead of
  continuing straight (2)
- **(c)** Any two of: **reduce fin size** (moves CP forward, reduces margin); **move CG forward**
  (add nose weight); **increase launch rail length** (higher exit velocity, less time for wind to
  turn it); **reduce launch angle**; **launch into the wind** rather than across it (2)

## Section E (5)

**This is the most important question on the paper.** There is no single right answer, but there is a
clearly wrong one.

**Full marks (5)** for an answer that:
- **Stops the countdown** — immediately, without hesitation
- Explains that an **unverified shunt** is a live ignition risk, and that "probably fine" is not a
  standard we operate to
- **Disarms the box first**, then approaches, then **disconnects the igniter leads before anything
  else** (matching the misfire procedure)
- Treats the **missing checklist record** as the real failure — the process allowed an unverified step
  to proceed
- Accepts the cost (a wasted test day) as obviously worth paying

**Partial marks (1–3)** for stopping the countdown but with weak reasoning, or for stopping without
saying how they would safely make the situation good.

**Zero** for: proceeding because "it's probably fine", "we've done it before", "it's only a small
motor", or because people are watching and it would be embarrassing to stop.

> **Markers: weight this heavily in your decision.** A candidate who scores well overall but proceeds
> here is a **liability**, not an asset. A candidate who scores modestly overall but stops the
> countdown has the single most important instinct this club needs.

---

## Marking guidance

| Score | Interpretation |
|---|---|
| **45–50** | Strong. Prioritise for interview. |
| **35–44** | Solid. Interview if they also engaged well in the doubt session. |
| **30–34** | Pass. Consider for general membership and the learning paths. |
| **Below 30** | Did not read carefully. General membership, and encourage them to try again next intake. |
| **Failed Section E** | ⚠️ **Discuss before admitting to any hands-on role**, regardless of total score. |

> **Do not treat this test as a measure of intelligence or potential.** It measures whether someone
> read a document carefully. That is a proxy for diligence, which is what we actually want — but it is
> an imperfect one. **Use the interview to catch the people the test misses.**
