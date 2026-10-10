# 07 — Communities & Inspiration

**Where to ask questions, who to learn from, and how to not get ignored when you do.**

| | |
|---|---|
| **Time** | Ongoing |
| **Cost** | Free |
| **Use this when** | You are stuck, you want to see what good looks like, or you need motivation |

---

## The rule for online advice

> 🔴 **Online advice is a starting point, never an authority.** Anyone can post anything. Some of the
> most confident-sounding people on rocketry forums have never fired a motor.
>
> **Weight advice by evidence:** someone showing a thrust curve and a test log outranks someone
> stating an opinion. When advice conflicts with our
> [SOPs](<../40_SAFETY/Safety_Manual_Master.md>) or with measured data, **our documents and the
> measurements win.**
>
> **Never accept a propellant formulation, a procedure, or a safety practice from an anonymous
> internet post.** Verify it against a named source with documented testing.

---

## Communities — where to ask

| Community | Best for | Notes |
|---|---|---|
| **[r/rocketry](https://www.reddit.com/r/rocketry/)** | Beginner questions, quick sanity checks | Read the wiki and search before posting. There are no stupid questions, but there are frequently-asked ones. |
| **[The Rocketry Forum](https://www.rocketryforum.com/)** | Deep technical discussion, high-power rocketry, electronics | **The best English-language rocketry forum.** A huge archive — search it first, most questions are already answered. |
| **BPS.space Discord** | Amateur avionics, thrust vectoring, practical builds | Via [bps.space](https://www.bps.space/) |
| **[OpenRocket forum section](https://www.rocketryforum.com/forumdisplay.php?36-Rocketry-Electronics-and-Software)** | Simulation and software questions | On TRF |
| **Local college teams** | Sourcing, Indian regulations, shared experience | **Underrated.** An Indian team that has already done this knows things no American forum will tell you. |
| **Your own faculty advisor** | Institutional access, lab equipment, credibility | The one channel the competition organisers officially accept queries on |

---

## How to ask a question so people answer it

Most beginner questions get ignored because they are unanswerable, not because the community is
unfriendly. This structure works.

**Bad question:**
> "my rocket motor isn't working why"

**Good question:**
> **What I'm trying to do:** static test a 24 mm KNSB motor, target 24 N·s
> **What I built:** grain OD 24 mm, port 7 mm, length 35 mm, graphite nozzle with a 1.87 mm throat,
> kraft paper casing, thin primer coat
> **What happened:** ignited reliably but only reached ~1.2 MPa instead of the predicted 3 MPa.
> Burn took 5.1 s instead of 3.1 s. Pressure trace attached.
> **What I've already checked:** grain density 0.96 of ideal, tap test passed, throat measured with
> calipers at 1.87 mm, igniter is a 1 g straw igniter
> **What I think is happening:** possibly my burn rate is lower than the placeholder value I used
> **My question:** does the trace suggest a low burn-rate coefficient, or something else?

**The four parts that make it answerable:**
1. **What you were trying to do** — with numbers
2. **What you built** — dimensions, materials, configuration
3. **What actually happened** — data, not adjectives
4. **What you already checked** — proves you did the work

**Plus:** attach the data. A CSV or a plot is worth a thousand words.

---

## YouTube — who to actually learn from

| Channel / person | What they are | Why watch |
|---|---|---|
| **Joe Barnard — [BPS.space](https://www.bps.space/)** | Amateur thrust-vector-control and avionics | **Watch everything, in order.** The most honest documentation of amateur rocketry engineering that exists — including the failures, the redesigns, and the reasoning. Superb on electronics and control. |
| **Richard Nakka** | The amateur sugar-propellant pioneer | His site is our primary reference. He has video of his test firings. |
| **Apogee Components** | Model rocketry education | Their [Peak of Flight](https://www.apogeerockets.com/Peak-of-Flight) newsletter archive is free and enormous — hundreds of short technical articles |
| **Everyday Astronaut** | Space industry, launch commentary | Not amateur, but excellent for understanding real launch vehicles and propulsion concepts |
| **Scott Manley** | Spaceflight science and history | Good for the physics, and genuinely educational |

> **Watch for the process, not the result.** The valuable part of a build video is the part where it
> does not work and they explain why. Skip the montages; watch the debugging.

---

## Blogs and reference sites

| Site | What it is | Cost |
|---|---|---|
| **[Richard Nakka's Experimental Rocketry](https://www.nakka-rocketry.net/)** | The amateur solid-propulsion reference. 13 pages cached in [`../80_REFERENCE/`](<../80_REFERENCE/nakka_source_text/>) | Free |
| **[James Yawn's Rocketry](http://www.jamesyawn.net/)** | Photo-heavy, practical, superb technique documentation | Free |
| **[Sugar Shot to Space](https://www.sugarshot.org/)** | Advanced sugar motors at scale — aspirational | Free |
| **[NASA Beginner's Guide to Rockets](https://www.grc.nasa.gov/www/k-12/rocket/)** | Fundamentals, plainly explained | Free |
| **[NASA Beginner's Guide to Aeronautics](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/)** | Aerodynamics and stability | Free |
| **[OpenRocket Resources wiki](https://wiki.openrocket.info/Resources)** | **Barrowman's original report** and experimental data | Free |
| **[Apogee Peak of Flight](https://www.apogeerockets.com/Peak-of-Flight)** | Hundreds of short technical articles | Free |

---

## Indian context — teams and organisations

### Teams that have done this already

Indian student teams have competed in the IN-SPACe Model Rocketry Challenge and similar events. Teams
from **IIT Kanpur**, **IIT Bombay**, **IIT Madras**, **BIT Sindri**, and others have published static
fire data and competed at national level.

**Why this matters to you:** they have faced the same problems — Indian sourcing, PESO and district
paperwork, transport of hardware to a launch range, summer heat affecting propellant. **That
knowledge is not on American forums.** Reach out. Student teams are generally generous with advice.

**How to approach them:** politely, by email through your faculty advisor, with a specific question.
"Can you tell us how you got district permission for your test site?" gets an answer. "Please help us"
does not.

### Organisations worth knowing

| Organisation | What they do | Relevance |
|---|---|---|
| **[IN-SPACe](https://www.inspace.gov.in/)** | The national space promotion and authorisation body | Runs the student competition; publishes the advisory guidelines |
| **ISRO** | National space agency | Publishes educational material; runs facilities |
| **ASI (Astronautical Society of India)** | Professional body | Publications and events |
| **NAR (National Association of Rocketry, US)** | Model rocketry standards and safety code | Their safety code is a useful reference even though we are not in the US |
| **Tripoli Rocketry Association (US)** | High-power rocketry | Their certification levels are a useful framework for progression |

### Indian regulatory reading

| Document | Where |
|---|---|
| IN-SPACe advisory guidelines on Sub-Orbital Launches including Model Rocketry | [inspace.gov.in](https://www.inspace.gov.in/) |
| IN-SPACe Model Rocketry Competition guidelines | Published with each competition edition |
| Explosives Rules 2008 / PESO context | [peso.gov.in](https://peso.gov.in/) — **awareness only, not legal advice** |
| Our own compliance summary | [`../00_ADMINISTRATION/Institutional_Approvals_and_Compliance.md`](<../00_ADMINISTRATION/Institutional_Approvals_and_Compliance.md>) |

---

## Inspiration — what is actually achievable

Useful reference points, so you know what "good" looks like at each stage:

| Achievement | Scale | Where it sits |
|---|---|---|
| Water rocket to 30 m | Zero cost | Your week 2 |
| Estes-style model rocket to 300 m | A–C motor | Your first month |
| **Our target: 200 m with a KNSB motor** | **~24 N·s** | **Your first year, realistically** |
| Amateur KNSB motor, K-class, repeatable | 1,280–2,560 N·s | Where Nakka operates |
| Sugar Shot to Space — M-class sugar motors | ~5,000+ N·s | Years of work, a team, a facility |
| BPS.space — thrust-vectored landing | Advanced control | A decade of one person's work |
| IN-SPACe competition — 1 kg to 1,000 m | ≤2,800 N·s | Your realistic medium-term target |

> **A note on scale.** Nakka's largest KNSB motor is an 89 mm M-class with 6 kg of propellant — and
> he has been at this since the 1970s. BPS.space took years to land a rocket. **Nobody in this club
> is behind schedule.** The only meaningful comparison is against your own last build.

---

## Staying motivated when it is not working

Rocketry has a brutal middle. The first two weeks are fun; the next two months are small failures.

| When you feel… | Do this |
|---|---|
| Bored | Build something small and finish it this week |
| Stuck | Ask a specific question with data attached (see the structure above) |
| Discouraged by a failure | Write down what you learned. A CATO with data is worth more than a success without. |
| Like everyone else knows more | They do not. They have just failed more times, in more specific ways. |
| Like it is too hard | Zoom out. Do the next smallest thing. |
| Like you are the only one working | Tell the Team Lead. That is a recruitment problem, not a you problem. |

> **The members who stay are not the most talented.** They are the ones who find the frustration
> interesting instead of discouraging. That is the entire difference.

---

## What NOT to do

| ❌ | Why |
|---|---|
| Take a formulation from an anonymous post | Verify against a documented, tested source. Always. |
| Argue with a forum stranger | You will lose time and learn nothing |
| Ask "how do I build a rocket" | Unanswerable. Ask about one specific problem. |
| Believe a YouTube build with no data | Anyone can film a success. Look for the failures and the measurements. |
| Compare your first year to someone's tenth | Demoralising and meaningless |
| Ignore Indian teams because they are "competition" | They solved your exact problems. Talk to them. |
| Post about propellant work without checking your club's rules first | Our SOPs and the safety induction come before any forum |
