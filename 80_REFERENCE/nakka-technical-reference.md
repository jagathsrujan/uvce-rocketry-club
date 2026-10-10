# Richard Nakka Experimental Rocketry — Technical Reference Extract

**Source:** https://www.nakka-rocketry.net/ (canonical URLs cited per section)
**Retrieval note:** The live site returns **HTTP 403 "Access denied by Imunify360 bot-protection"** to
automated fetching (both `curl` and `web_fetch`). All content below was retrieved from **Wayback Machine
snapshots** (`web.archive.org`) of the canonical pages. Snapshot dates where positively identified are noted
in §11. Page "Last updated" dates are given per section — several pages are 20+ years old and the
`casebond`/`therm`/`inert` material is dated 1999–2002.

All fetched text was handled strictly as **data**. Capitalisation such as "Potasium" is quoted as-found.

---

## 1. Igniter design and formulations

Source: https://www.nakka-rocketry.net/igniter.html (last updated March 1, 2022)

### 1.1 Pyrotechnic "straw" igniter (baseline design)
- Construction: polyethylene drinking-straw tube filled with **Ignition Powder**, **sealed at both ends with
  polyethylene hot-melt glue**. Hot gases + molten combustion products both light the grain and pressurise
  the motor.
- Bridgewire: **nichrome** (nickel-chromium, high-resistance) wire, soldered to copper lead ends. Cost
  quoted **≈$0.20/ft**. Alternatives listed: one or two strands of coarse **steel wool**, or a strand of
  fine copper "speaker" wire.
- **Nichrome soldering method (exact):**
  1. Strip insulation from electrical leads, form **closed loops** with needlenose pliers; thread nichrome
     through the loops.
  2. Set spacing so the **nichrome span between loops is ≈5 mm**.
  3. Brush loops lightly with **acid soldering paste**; heat with a soldering gun and fill with solder
     (capillary action). Inspect under magnification that loops are fully filled.
  4. Remove excess paste by **swirling the igniter in alcohol**.
- Igniter charge sizes fired in a BEM (Ballistic Evaluation Motor), Fig. 2: **(a) 3 g, (b) 7 g, (c) 15 g**.
- **Over-charge warning (verbatim intent):** a much greater BP charge than Fig. 1 "may result in an initial
  pressure 'spike'"; over-pressurisation at startup "may result in motor failure characterized by **shearing
  of the safety bolts** retaining the rocket motor head." Effect is significant for small motors
  (**A-100, B-200, C-400**).
- Firing power supply: originally **4 × 1.25 V NiCad**; later **2 × 3.6 V NiMH cells (300 mAh each) in
  series = 7.2 V** (chosen for current delivery and cold-weather performance).
- All igniter leads are **shunted** (bared ends twisted together) for storage safety.

### 1.2 Ignition Powder (the standard primer/igniter composition)
- **Current formulation: 80 % potassium nitrate / 20 % charcoal by weight. No sulphur.**
  (Historic early mix was 75 % KN / 15 % charcoal / 10 % sulphur — conventional black powder.)
- Rationale for omitting sulphur: sulphur's role is to ease ignition; good for flintlocks, but "for safety
  reasons, it is not such a good feature for rocket motor igniters, nor is it really necessary."
- **Preparation:** charcoal must be *natural wood* (not briquettes); break up wrapped in cotton + hammer,
  pulverise in an electric coffee grinder. Grind KN to fine powder in a coffee grinder. Weigh out 80/20 and
  blend in a rotating mixer — **recommended blending time 3 hours per 100 grams**. Add enough water to form
  a fluid paste, spread on parchment paper, dry completely, break up with mortar & pestle, sift to required
  particle size with a flour sifter.

### 1.3 Chamber pressure from the igniter charge
- Equation given from **NASA SP-8051, *Solid Rocket Motor Igniters***, with `D = C/V` (loading density),
  `λ = RT/M` (effective force), `G` = fraction of charge consumed, `P_a` = atmospheric.
- **Impetus of commercial-grade black powder ≈ 100 000 ft·lb_f/lb_m**, so **λ = 1 200 000 in·lb_f/lb_m**.
- **Home-made IP impetus is only ~70–80 % of that value.**
- Spreadsheet: `IGNITER.XLS` (68 kB).

### 1.4 Pyrogen ignition (large motors, K-class and up)
- A pyrogen is "essentially a small rocket motor mounted at the bulkhead"; the Kappa pyrogen grain is
  **cast KNSU**, "chosen for its ease of ignition and rapid burn rate", ignited by a BP charge initially held
  in the canister by a **burst diaphragm** — which also aids motor pressurisation.

### 1.5 Mini-bulb ("exploding bridgewire") igniter
- Uses a **Xmas-tree mini-bulb** in place of nichrome. The **tungsten filament is instantly vaporised** on
  application of current (e.g. a 9 V battery). Credit: concept pioneered by **Rob Furtak**.
- Build: pull off and discard the plastic base; scrape the two copper leads clean of oxide; break the glass
  open by **slowly squeezing the upper half in a bench vise** with the bulb **wrapped in a tissue** to catch
  shards; safety glasses mandatory.
- **Remove the shunt** (fine wire/foil wrapped round the base of the leads) with a toothpick or tweezers,
  otherwise an ohmmeter test **falsely indicates** the filament is intact.
- Continuity: "Infinite" resistance = open circuit (filament/solder broken); zero = shorted leads.
  **Measured resistance may be anywhere from a couple of ohms to more than a hundred ohms and "does not
  provide any useful information other than to indicate an 'OK' condition."**
- Solder leads using **acid flux**. Then insert into a **2 in (5 cm) length of polyethylene soda straw**,
  seal the lead end with hot-melt glue, load **≈1 gram of Ignition Powder**, tamping periodically to
  eliminate voids, then tamp in a small ball of **glass wool** and seal with hot-melt glue.
- Robustness test: 20 bulbs mounted radially on an **8 in (20 cm) disc** spun on a lathe at **>120 g** — all
  functioned normally afterwards.

### 1.6 Ultra-low current igniter (Ken Tucker, for EARco)
- Base part: **RadioShack Part # 272-1139 Mini Lamp** (or equivalent), supplied with pre-attached leads.
- Rating: **1.5 V, 25 mA**; in practice fires at **1.2 V, 20 mA (= 25 mW)**.
- Build: record bulb resistance (typically **20–30 Ω**); grind a hole through the glass on a fine file or
  polishing stone (≈5 minutes), grinding with the **filament perpendicular to the hole** so shards do not
  strike it; re-check ohms (should be unchanged); place black powder loosely into the hole (do **not** pack —
  can damage the bridgewire); cover hole with Scotch tape.
- The bridgewire explodes and lands on the powder, so direct contact is not required.
- Output is match-like; to amplify, place the igniter in a tube ~1 in long of similar diameter, fill with
  black powder and seal the ends.
- Redundancy: **3 igniters in parallel require only 1.2 V and 60 mA (3 × 20 mA)**.
- Cold-soak test: a near-dead 9 V battery frozen at **−4 °F for 6 hours** (no-load 5 V, loaded 3 V) fired
  the igniter instantly. Reference loads quoted: new 9 V no-load 9.8 V / loaded 8.2 V; used 9 V no-load
  8.8 V / loaded 5.1 V.

### 1.7 "Ferocious" igniter (for RNX epoxy composite)
- Needed because the BP straw igniter will not light RNX (higher decomposition temperature); burns hot for
  **≈2 seconds**.
- Composition: **potassium perchlorate (KP)**, very finely ground (mortar & pestle) + **sulphur**, finely
  ground + **high-grade epoxy such as West System** — note **"adhesive grade is not satisfactory"**.
  Developmental version used **potassium chlorate (KC)**, replaced with KP **for safety**.
- Mix: manufacturer-recommended resin/hardener ratio; **0.5 g of epoxy is sufficient for 4–5 igniters**; add
  a sprinkling of sulphur only until the mix is distinctly yellow/light amber; blend ≥2 minutes with a
  wooden craft stick; add KP gradually "until the resulting mixture resembles a stiff paste."
- Forming: two **1 in × 1 in (25 × 25 mm)** polyethylene squares per igniter (cut from a sandwich bag).
  Place a dab of pyrolant ≈ the size of a **pencil eraser** on the bridgewire, cover and press.
  **Thickness must be no greater than 3 mm to prevent fracture of the pyrolant coating upon firing**, and if
  installed at the **grain outside surface**, press into a **disc no more than ~2 mm thick**. The disc form is
  recommended for the **Epoch** and **Paradigm** motors.
- Cure: overnight at room temperature, or **65 °C (150 °F) for ~½ hour** in a shop oven. Peel off poly sheet.
- For small throat diameters or outside-surface installation, use **30 AWG "wrapping wire"
  (RS p/n 278-501)**.
- Reliability: **over 30 motor firings, zero misfires.**

### 1.8 "Spitfire" / "Spitfire II" (Rob Furtak; best for composite)
- **Thermex Powder** (Spitfire): **65 % KP (finely ground, 200 mesh) / 20 % charcoal (ball milled) /
  10 % aluminium powder (400 mesh) / 5 % red iron oxide**. Blend in a rotating tumbler 1–2 hours.
- Pyrolant: Thermex blended with **neoprene contact cement at ≈2:1 by mass**; consistency "as stiff as
  toothpaste". Working time only a few minutes (solvent evaporation) — make only a few at a time. Cure a few
  hours (less if warm). Cover the filament completely and extend pyrolant down to the bulb base for
  resilience.
- **Spitfire II** — hotter version for the hard-to-light **A24 AN-based** composite. **Theoretical flame
  temperature 3180 °C.**
  **Thermex II: 66 % KP (200 mesh) / 16 % charcoal (ball milled) / 12 % Al (400 mesh) / 6 % red iron oxide.**
  Blended with **20 % by mass** neoprene-based contact cement, fully dried, then granulated for a standard
  straw igniter, or dissolved in **MEK or acetone** for dipping.

### 1.9 Hot-particle (thermite) igniter compounds
- **Copper/aluminium thermite** — stoichiometric CuO:Al mass ratio **4.56:1**; **10 g batch = 8.2 g CuO +
  1.8 g Al**. Produces molten copper + Al₂O₃, very little gas → "shockless". Used on ASP I/II/III and
  Super-Loki Dart. Hard to ignite; light with a mini-bulb EBW. **Batch/stored limit 10 g.**
- **Copper/magnesium thermite** — CuO:Mg **3.30:1**; **10 g batch = 7.7 g CuO + 2.3 g Mg**. Use coarser Mg,
  e.g. **60 micron (240 mesh)**, for safety. Readily lit by mini-bulb. **Limit 10 g.**
- **Teflon/magnesium** — reference formulation 40/60; Nakka prefers **55/45 teflon:magnesium** (more
  economical, higher theoretical combustion temperature). Combustion products at 55/45: **carbon (solid) 13 %,
  magnesium fluoride (gas/molten) 74 %, magnesium (molten) 13 %.** Micro-fine teflon powder sourced as a
  **piano knuckle lubricant, $6 USD/oz (28 g)**.

### 1.10 Nitrate-based igniters for composite propellant
- IP (KNO₃/charcoal) igniters remain reliable and safe for sugar motors but "fall short when used with RNX
  and other composite propellants that are harder to ignite by their very nature."
- Potassium chlorate/ammonium perchlorate igniters have low melting/ignition points and high caloric value
  but **KC compositions are sensitive to impact, friction and heat**; also may be hard to obtain.
- Two KNO₃-based, non-exotic compositions were developed (article by **Richard Nakka & Peter Lee Ericksson**,
  PDF on the page).

### 1.11 MDP Pyrolant / MDP Pyrogen (for sugar propellants)
- "MDP" = **Modified Dan Pollino**.
- **MDP Pyrolant, 40 g batch: 65 % KN = 26 g; 24 % sucrose = 9.6 g; 9 % sulphur = 3.6 g;
  2 % red iron oxide = 0.8 g.**
- Process: blend into **100 ml water**, boil in a pot/deep-fryer to drive off water; stop at wet paste
  consistency; spread on aluminium foil, dry fully; **granulate to 10–60 mesh**; store sealed with a
  **silica-gel pack**.
- MDP Pyrogen: plastic straw, one end closed with a tissue wad + hot glue, MDP firmly packed with a wooden
  dowel, loose MDP added, nichrome bridgewire assembly inserted, end sealed with hot glue, then **two slits
  cut in the side to act as 'nozzles'**. Inserted into the forward end of the motor. **Burn duration ≈½
  second.**

### 1.12 Fusion Pyrolant / Pyrogen
- Developed because chlorate/perchlorate pyrolants "burn very rapidly when confined" and a **sustained** burn
  (not a brief flash/pressure pulse) is wanted for propellants with a **high pressure exponent**, to avoid
  over-pressurisation at grain ignition. Based on Formula 2 propellant with polyurethane replaced by powdered
  sucrose.
- **Fusion Pyrolant, 40 g batch: 46 % KN = 18.4 g; 22 % aluminium powder = 8.8 g; 15 % sucrose = 6.0 g;
  14 % sulphur = 5.6 g; 3 % charcoal = 1.2 g.** KN milled fine; sucrose = finely powdered icing sugar; blend
  in a rotating tumbler ≥1 hour (a couple of small stones help break clumps).
- Fusion Pyrogen uses a **Xmas bulb** for initiation — "the tungsten filament gets much hotter than nichrome
  wire", which ensures ignition of this aluminium-rich pyrolant. Straw (paper preferred) loaded with Fusion
  using a straw cut at **45°** as the loading tool; end closed with a pressed (not bonded) tissue wad;
  **three slits ≈25 mm long** cut in the side to prevent pressure build-up.

### 1.13 Harvesting flake aluminium from paint (for Al-bearing igniters)
- **Flake (leaf) aluminium is superior to atomised/spherical** (e.g. West Systems 420) for igniters —
  spherical Al has a thicker oxide shell and needs more thermal energy; flake also ignites more readily by
  particle shape.
- Aluminium paint is largely linseed oil + metallic Al flake; **MSDS values 20 %–30 % Al by mass**. Typical
  harvest **15 %–20 % of paint mass**. Brands used: **TremClad** and **Rust-Oleum 7715** (TremClad slightly
  higher yield).
- From **½ pint (273 ml)** of paint, net harvest is typically **35–40 g (1.2–1.4 oz)** — enough for 100+
  igniters.
- Method: let the tin settle undisturbed for several weeks; siphon off the linseed oil with a turkey baster;
  fill with **acetone**, stir several minutes scraping the bottom/sides; stand overnight; draw off acetone;
  repeat the acetone wash (second wash removes residual linseed oil, otherwise the dried Al forms hard
  clumps); wick away the remaining acetone with paper towel; spread the slurry in a polyethylene pan and
  evaporate **a couple of days**; break up clumps with the convex side of a spoon; sift through a fine nylon
  kitchen sifter; store sealed.
- Safety: dust mask when sifting; nitrile/neoprene gloves with acetone; safety glasses at all times;
  **do not oven-dry the slurry (acetone is highly flammable)**; **do not use an electric coffee grinder on
  the Al clumps (aluminium dust is explosive and can be ignited by an electrical spark)**; recycle used
  acetone (excellent degreaser), stored in glass/metal marked "Used Acetone".
- Test formulation **HotFlash pyrolant: 30 % aluminium flake, 60 % KN, 10 % sulphur, with nitrocellulose (NC)
  lacquer as the bonding medium.**

---

## 2. The KNSB ignition primer — recipe and application

Sources: https://www.nakka-rocketry.net/ignexp.html ("Combustion Primer") and
https://www.nakka-rocketry.net/casting1.html ("ignition aid")

### 2.1 Recipe
- **Finely ground Ignition Powder (80 % KN / 20 % charcoal) mixed with 70 % isopropyl alcohol (rubbing
  alcohol).**
- Ignition Powder granules are first pulverised with a **mortar and pestle**; IPA is added **until the
  consistency is that of thick paint**. (Note: "thick paint" describes the *mix*, not the applied coat.)
- Alternative stated in casting1: "a few grams of Ignition Powder is finely ground up, then mixed with
  **70 % isopropyl alcohol (IPA)** such that the consistency is similar to thick paint."

### 2.2 Application — thin coat, not thick
- **Applied as a single coat with a fine paintbrush.**
- **Measured average coating thickness: 0.0075 in (200 micron)** in the controlled ignexp experiment.
- casting1 wording is explicit and consistent: the grain "should be painted with a **thin coat** of Ignition
  Powder"; "a brush is then used to apply a **light coating over the entire outer surface**. **It is not
  necessary to coat the core.**"
- Drying: ignexp allowed **minimum 24 hours**; casting1 allows **~half an hour in open air**, then into the
  desiccator to complete drying. The dried coating is described as **very durable** — it "will not rub off by
  normal handling or storage", and "adhered very well".
- Stated purpose: "to facilitate rapid ignition of **all** burning surfaces of the grain", giving "a nearly
  instantaneous motor chamber pressure rise to that of the design operating level", minimising impulse loss
  from delayed pressure rise. Pressure curves for **coated vs uncoated A-100M grains** differ strikingly
  (Fig. 5, casting1).

### 2.3 Why a thin coat — the stated mechanism
- On heating, the coating **melts rapidly over much of the surface with highly agitated bubbling**, then
  combustion initiates.
- Potassium nitrate **melts at 333 °C** with no energy absorbed by melting/decomposition of the charcoal
  fuel at that temperature; **only slightly further heating decomposes the KN at 400 °C**, evolving oxygen
  which then burns the charcoal particles in the coating matrix.
- The **black colour / high emissivity** of the coating facilitates **radiant heat transfer** from the flame.
- Caveat observed in testing: **flame spread over the surface was somewhat *less* rapid** than for bare
  specimens, even though ignition *initiation* was much faster.

### 2.4 Explicit thickness limits in the source (the only "too thick" failure mode documented)
The strongest quantitative thickness guidance on these pages is for the **Ferocious epoxy/KP pyrolant**, not
the KN/charcoal primer: **≤3 mm to prevent fracture of the pyrolant coating upon firing**, and **≤2 mm** when
pressed as a disc for outside-surface installation (https://www.nakka-rocketry.net/igniter.html). For the
IP/IPA primer the documented guidance is only "thin/light, single coat (~200 µm)".

> **Gap flagged:** none of the ten requested pages contains a "thick coat" variant or an explicit
> thin-vs-thick comparison for the KN/charcoal primer. The sources uniformly specify a *thin, light, single*
> coat. A thick-coat recommendation should **not** be attributed to these pages.

---

## 3. KNSB igniteability vs KNSU / KNDX — the quantitative finding

Source: https://www.nakka-rocketry.net/ignexp.html ("Propellant Igniteability Experiment")

**Observation:** KN-Sorbitol does not readily ignite under ambient conditions and requires sustained direct
flame exposure; KN-Sucrose and KN-Dextrose ignite much more readily.

**Method:** slugs cast in **1 in PVC pipe rings** onto galvanised sheet steel (one smooth test surface);
**0.931 in (24 mm) diameter × 0.40 in (10 mm) long, 8 g each**; batches of **123 g (80 g oxidiser / 43 g
fuel)**; dextrose oven-dried to anhydrous; all constituents coffee-ground and blended **3 hours** before
casting; KNSB cured **≥24 h** after casting. Ignition source: **butane "BBQ" lighter at 25 mm** from the
surface, flame normal to the surface, shield withdrawn to start timing; timing by videotape. Fixture:
vertically mounted steel plate **3.7 in square × 0.060 in thick** with a chamfered **21/32 in (17 mm)** hole,
specimen hot-glued concentric behind it.

**Time to ignition (seconds), uncoated, 5 specimens each:**

| Test # | KN-Sucrose | KN-Dextrose | KN-Sorbitol |
|---|---|---|---|
| 1 | 4.7 | 7.4 | 17.7 |
| 2 | 5.9 | 8.0 | 22.0 |
| 3 | 4.3 | 8.1 | 16.4 |
| 4 | 4.8 | 7.2 | 22.8 |
| 5 | 4.3 | 8.6 | 20.4 |
| **Avg.** | **4.8** | **7.9** | **19.9** |

**Normalised to KN-Sucrose: KN-Dextrose ratio = 1.64; KN-Sorbitol ratio = 4.15.**

**Primer-coated KN-Sorbitol (Combustion Primer, single coat, 200 µm):** 2.9, 4.8, 5.0, **12.8**, 3.3 s →
**average 5.8 s**; **excluding the single aberrant 12.8 s point, average 4.0 s**. Stated result:
"**Igniteability was increased, on average, by nearly a factor of 5**" (aberrant point neglected).

**Mechanistic explanation:** decomposition (caramelisation) dominates. KN-Sucrose is partly caramelised
during casting and decomposes most readily; KN-Dextrose caramelises slightly during casting; **KNSB does not
caramelise during casting and does not readily decompose on heating — only after sustained heating does
decomposition occur, forming visible carbon (carbonisation rather than caramelisation), with a
"significantly larger" blister than the other two.**

**Design consequences stated:**
- For a single-grain motor with a central core, a **pyrogen** igniter is most effective for rapid startup.
- **BATES grains are a specific problem:** the segment ends sit "pretty much in a region of stagnant flow"
  so timely ignition is doubtful regardless of igniter design. The **Combustion Primer is the proposed
  solution** — coat the **segment ends**, and coat the **central core part way near the segment ends**.
- Key ignition parameters: **placement, charge size and duration, and flame temperature**; the key mechanism
  is **convective heat transfer** (high-velocity flow over the surface).
- Delayed ignition is a **postulated cause of the peculiar results from static test KSB-001** of the
  Kappa-SB motor.

**Contradicting/countervailing evidence** (see §9): https://www.nakka-rocketry.net/knsbchar.html argues
ignition is *not* the cause of KNSB's odd behaviour, noting that Nakka's **KSB-002 ignition-initiator
experiment vs KSB-001 showed little difference** in thrust-curve shape — evidence that ignition spreads
quickly to all exposed surfaces. The knee on the leading edge of nearly every sorbitol thrust curve is cited
as evidence of fast, complete ignition.

---

## 4. Case bonding vs free-standing grains

Source: https://www.nakka-rocketry.net/casebond.html (last updated **August 23, 1999**)

**Two objectives of case bonding:** (1) inhibit burning at the grain/casing bondline, enabling end-burner or
longer-duration core-burner configurations; (2) **avoid exposing casing walls to hot combustion gases**,
because "the mechanical strength of the casing material is significantly reduced by high temperature
exposure, in particular, aluminium alloys."

**Why sugar propellants are problematic — elastic modulus (E = σ/ε), psi:**

| Propellant | Elastic Modulus (psi) |
|---|---|
| PVC/AP/Al | 250 |
| Polysulfide/AP/Al | 3 000 |
| PBAN/AP/Al | 3 300 |
| HTPB/AP/Al | 2 000 |
| Polyurethane/AP/Al | 20 000 |
| **KN/Sorbitol** | **850 000** |
| KN/Dextrose | TBD (similar) |
| KN/Sucrose | TBD (similar) |

High-modulus grains are "highly inflexible" — they develop high internal stress at tiny strain. All cast
sugar propellants fall in the high-modulus category.

**Two failure modes:**
1. **Disbonding** of grain from the casing wall (cohesive failure) as the casing expands under pressure while
   the grain resists. Likely if **grain length < casing length** (the casing expands more beyond the grain
   boundaries).
2. **Cracking of the grain web at multiple sites** when pressurisation-induced hoop-loading strain exceeds
   the propellant tensile strength.

**Both failure modes "would likely result in catastrophic motor failure due to overpressurization resulting
from unexpected increase in burning area."**

**Mitigations:** full-length grain + reinforced casing closures to locally minimise radial expansion (mode 1).
Sufficiently stiff casing — high modulus material (**steel rather than aluminium**) and/or thick wall
(mode 2).

**Design method:** casing diametral change from chamber pressure →
ε = ΔD/D; hoop stress σ_c = PD/2t; the grain must experience the same strain as the casing (bonded), and
with Poisson ratio ν_g ≈ 0.25–0.33 (dropped out by assuming it similar to the casing) this yields
**σ_c / σ_g = E_c / E_g** — the ratio of hoop stresses is proportional to the ratio of elastic moduli. So the
maximum allowable casing hoop stress follows from the allowable grain stress, and wall thickness from
`t = PD / (2σ_c,max)`. The analysis **ignores the structural contribution of the grain** (which in reality
helps resist hoop loading), so it is **slightly conservative**.

**Worked example:** case-bonded **KN-Sorbitol, 3.0 in diameter, MEOP 800 psi**, limit grain tensile stress to
**20 % of UTS**:
- E_g = **850 000 psi**; UTS = **1050 psi**; allowable = 0.20 × 1050 = **210 psi**.
- Steel: E_c = **29 000 000 psi** → allowable casing hoop stress = 210 × (29e6/850e3) ≈ **7 165 psi**
  → t = PD/2σ ≈ **0.17 in**. Page states resulting casing **mass 0.47 lb per inch of length**.
- Aluminium: E_c = **10 000 000 psi** → allowable casing hoop stress ≈ **2 471 psi**
  → t ≈ **0.41–0.49 in** depending on diameter convention. Page states **mass 0.38 lb per inch of length**.
- *Caveat: the final thickness expressions were presented as inline equation images and are not present in
  the page text. The thicknesses above are recomputed from the page's stated method, inputs and casing
  masses; the two agree for steel but differ by ~15 % for aluminium, indicating the page used a slightly
  different diameter/density convention. Treat the **stated masses (0.47 and 0.38 lb/in)** as the
  authoritative figures.*

**Conclusion quoted:** "Such a casing would be rather heavy" … "**case-bonding of a high-modulus propellant
is of questionable practicality**." Also: "**Once cast, it is not possible to detect flaws, such as voids or
bubbles**, which could locally weaken the grain or act as stress raisers."

**The recommended alternative (free-standing grain):** achieve both case-bonding objectives by other means:
- Inhibit outer-surface burning by casting the grain into a **burn-resistant or ablative liner, such as a
  cardboard tube, of diameter slightly less than the casing ID**.
- Protect the casing from hot gases with a **suitable ablative coating (polyester or epoxy resin)** or a
  **snug-fitting multilayered paper or cardboard liner**.
- "With such an arrangement, the grain can be **free-standing, and thus subjected to benign compressive
  stresses only**."

This is corroborated by the thermal page (https://www.nakka-rocketry.net/therm.html): "Thermal protection is
of particular importance for motors with **free-standing propellant grains**. Not only are the combustion
gases in constant and direct contact with the entire casing walls, more importantly, **convection of the
gases greatly increases heat transfer** to the casing walls."

---

## 5. Thermal insulation and liners

Source: https://www.nakka-rocketry.net/therm.html (last updated **February 27, 2000**)

### 5.1 When thermal protection is NOT needed
All three conditions must hold:
1. **Very short burn time (typically less than one second)**;
2. **Relatively low combustion temperature (e.g. KN-based propellants)**;
3. Casing material that does not weaken greatly at elevated temperature **and** a wall thick enough to
   contain the pressure at its reduced strength.

"This is the approach that has been taken for my **A-100, B-200 and C-400** motors." (All other cases, e.g.
the Kappa motor, need protection.)

### 5.2 Three practical forms of thermal protection
1. **Insulating (low-conductivity) layer on the casing inside walls** — a heat-resistant liner; the
   challenge is that most materials burn/melt away, so the layer must be thick enough that enough remains.
2. **Heat sink** — a thick-walled casing of high-conductivity material (e.g. aluminium alloy).
3. **Ablative layer** — a thermoset plastic or rubber that **decomposes rather than melts**, absorbing heat
   endothermically; pyrolysis gases form a protective boundary layer. "Probably the best approach" for high
   combustion temperature and/or long burn times.

### 5.3 Strength at elevated temperature
- **Aluminium 6061 has only ~80 % of room-temperature strength at 150 °C (300 °F).**
- **Low-carbon (mild) steel retains 80 %** of yield and ultimate strength at **240 °C (465 °F)** and
  **380 °C (720 °F)** respectively.
- The reductions are for **prolonged exposure (½ hour)**; rapid heating is less severe (shown for 2024-T3),
  but the ½-hour data are used for design because rapid-heating data are scarce — **conservative**.

**Table 1 — Melting point (°C):** low alloy steel **1480**; stainless steel AISI 301 **1400**;
aluminium 2024-T3 **500**; aluminium 6061-T6 **580**; mild steel SAE1020 **1530**; Inconel **1400**.

### 5.4 Heating of the casing wall
- Convective heat transfer: **q = h (T_g − T_i)**.
- Analysis tool: **FORTRAN program THERMCAS**, Schmidt method, **11 equally spaced nodal points** through the
  wall; distributed as `THERMCAS.ZIP` (62 kB, DOS executable + MSExcel97 spreadsheet).
- Reference case: initial casing **20 °C**, combustion temperature **1450 °C**, burn time **1.5 s**,
  **h = 1000 W/m²·K**; wall thicknesses **aluminium alloy 2.5 mm, stainless steel 2 mm, PVC 3.9 mm**; each
  successive plotted line is **0.13 s** apart, topmost line at burnout (t = 1.5 s). (For PVC the
  distribution shown is for ½ the wall thickness.)
- Thermal diffusivity **α = k/(ρ·C_s)**, room-temperature values **×10⁻⁷ m²/s**:
  **aluminium 6061-T6 = 690; stainless steel AISI 304 = 40; PVC = 3.4.**
- Findings: aluminium diffuses heat best (low, uniform wall temperature); stainless steel shows a pronounced
  gradient but still achieves a reasonably low wall temperature **because of steel's higher density/heat
  capacity**; PVC shows a **steep gradient** — the bulk stays cool but the inner surface gets very hot, which
  self-limits heat transfer. **PVC starts to decompose (carbonise) at about 225 °C** (not modelled in the
  analysis); decomposition reduces heat transfer — i.e. **ablative** protection.

### 5.5 Insulation sizing example
- **0.5 mm** insulation with α = 1.0 (typical paper/thermoset) on a **2 mm 6061 aluminium** casing, same
  heating conditions.
- **Design goal: keep the casing below about 150 °C**, where Ftu/Fty = 80 % of room-temperature values.
- Thicker insulation lowers temperature further, but the downside is **not mass** (insulation density is low)
  — it is **reduced casing diameter**, which reduces propellant volume and, more significantly, **decreases
  web thickness, thereby reducing burn duration**.

### 5.6 Insulation test programme (measured data)
- Test article: **6061-T6511 aluminium thin-wall tubing, 63.5 mm O.D., 1.65 mm wall** — identical to the
  Kappa motor casing.
- **Materials and thicknesses tested:**
  - **Brown "postal paper", measured average 0.15 mm per layer** — tested at **2 layers (0.29 mm)** and
    **7 layers (1.0 mm)**.
  - **Utility-grade polyester resin** (automotive body-repair type, fibreglass matrix), **single coating
    applied to the casing inside and allowed to harden fully while the casing was slowly and continuously
    rotated** — measured average final thickness **0.11 mm**.
  - **Two "control" tests with no insulation.**
- Instrumentation and method: hole cut in the tube side for a **propane torch** flame impinging on the far
  wall; **type K thermocouple soldered to the casing outside surface** directly in line with the flame
  contact zone; **nitrogen slowly fed in** to prevent combustion of the insulator with atmospheric oxygen;
  DAQ sample rate **3 readings per second**; steel shield withdrawn at t = 0; heating continued until the
  thermocouple detached (solder melted).
- Post-test condition: paper showed **some charring of the innermost layer(s)** but was otherwise intact;
  polyester had **no discernible degradation other than some discolouration**.
- Derived convection coefficient: **h = 55 W/m²·K**, obtained by trial-and-error matching of THERMCAS to the
  bare-specimen curve, assuming a flame temperature of **1800 °C** (propane/ideal air ratio is 1967 °C);
  results showed **low sensitivity** to that assumption. **Important caveat: this h is far lower than in a
  real motor because the test was at atmospheric pressure — "under the high pressure of a rocket motor, the
  convection coefficient would be perhaps 20 or 30 times as great, and the heating times would therefore be
  much shorter."**
- **Measured densities: paper 0.646 g/cm³; cast polyester 1.26 g/cm³.**

**Table 2 — published reference values**

| Material | Density (g/cm³) | Heat capacity (J/g·K) | Thermal conductivity (W/m·K) |
|---|---|---|---|
| Paper | 0.930 | 1.34 | 0.18 |
| Polyester | 1.2–2.0 | 1.3 | 0.19–0.50 |

- Measured k values came out **somewhat higher than published** values (partly because measured values are
  averages over the temperature range vs room-temperature published data), but both materials remain
  effective.
- **The 7-layer paper had lower conductivity than the 2-layer** — expected, because **trapped air between
  layers provides additional insulation**.
- Conclusion: "**layered paper and polyester coatings would both seem to be viable insulating materials for
  rocket motor casings.**"

### 5.7 Thermal considerations in structural sizing
- Simple approach: determine **maximum average wall temperature at burnout**, read strength at that
  temperature, size the casing to MEOP with appropriate safety factors (`CASING.XLS`).
- Refined approach: design the **thrust/pressure profile to be regressive** so MEOP occurs **early** in the
  burn while the walls are still cool, and pressure near burnout is lower so the heated casing sees lower
  structural loading.
- **PVC casings** need a different approach — a **"knock-down" factor on wall thickness**: define the
  effective thickness as that which stays below a threshold. **PVC begins to soften at about 100 °C**, so
  using the non-insulated PVC example (3.9 mm wall, α = 3.4):
  **t_eff = (1 − 9/22) × 3.9 = 2.3 mm.**

---

## 6. Static test stand design

Sources: https://www.nakka-rocketry.net/static.html (last updated May 14, 2020; originally posted Aug 10,
2000), https://www.nakka-rocketry.net/sts5000f.html (last updated May 25, 2020; originally posted Aug 6,
2000), and https://www.nakka-rocketry.net/safety.html

### 6.1 Historical progression
1. **"Thrustometer"** (c. 1972) — a **25 lb (11 kg) capacity scale** the motor pushed against; a piece of
   pencil lead on the dial etched an arc on paper taped to the scale face, recording **maximum thrust only**.
   Destroyed when a motor over-pressurised, severed the safety pin, blew the end plug, and broke the dial off.
2. **"Thrustograph"** (Dec 1972) — direct mechanical recording. Motor mounted **horizontally on a sled**
   running on rails, restrained by **a pair of powerful extension springs**. An arm drove a pen over
   recording paper fed by a pair of steel rollers with rubber rings, driven by a **120 V furnace motor at
   1720 RPM** geared to a **paper feed rate of 4.50 in/s (11.4 cm/s)**. Paper width **8.5 in (21.6 cm)**.
   Springs selected so maximum sled movement was **no greater than ~6 in (15 cm)**. Spring constant
   calibration: a **pair of 50 lb angler's scales**, or hanging known weights and measuring displacement.
   Fine for motors **under ~200 lb (900 N)** thrust.
3. **"Static Test Rig"** (begun early 1982) — first electronic system. **Force transducer salvaged from a
   digital bathroom scale** = small **cantilever beam fitted with four strain gauges**; conditioning circuit +
   A/D → computer, stored on digital tape. **Sampling rate 580 samples/sec.** Motor mounted **vertically,
   nozzle upward, in a tubular holder**; the holder's bottom sat on a **deflection bar acting as a beam
   supported at both ends with the load acting downward at midspan**; the force transducer contacted the
   deflection bar near midspan. **Deflection limited to ~0.25 in (6.4 mm)**; a **"stop"** was fitted under the
   deflection bar to prevent damage on over-thrusting or blow-out. Supporting structure: **heavy I-beam with
   three tubular legs welded to the I-beam ends**. Trial testing revealed **severe underdamped oscillation**;
   a **hydraulic damper with adjustable damping** was designed and built and attached to the deflection bar.
   Bar deflection: `y` at midspan from `F, L, E, b, d`. Calibrated with a **calibration arm** with weights
   hung at its end, amplifying the force applied at the deflection bar midspan.
4. **STS-5000 Static Test Stand** (designed 2000/2001) — current stand.

### 6.2 STS-5000 — structure and load path
- Purpose: motors up to **5000 Newtons (1100 lbs)** thrust, i.e. sizes up to **"M" class**.
- **Tripod** form: "the stand is self-levelling on any surface, with equal load distribution to each leg."
- **Motor mounted vertically, nozzle upward, firing upward**, so **the thrust force is reacted by the ground**
  the stand sits on. This eliminates the large mass/anchoring needed for horizontal stands. "There are no
  significant advantages to horizontal testing of motors." **The weight of the motor resting on the load cell
  can simply be subtracted from the measured thrust.** Precedent cited: the 260-inch AJ-260X (SL-2) Space
  Booster was fired vertically this way.
- **Load path:** thrust plate (motor bears on it) → **load cell** → **Base Plate** → **three Base Plate
  Supports** → **three vertical Thrust Struts** → **three Cross Beams** → tension load beamed out to the
  **three support Legs** → compression reacted at the **ground**, with **wooden pads under each leg foot** to
  distribute bearing load.
- **Three Leg Braces** prevent outward collapse of the legs. **Tension Rods** stabilise against lateral
  loading during firing — **recently replaced by a chain-turnbuckle arrangement** for faster field setup.
- **Construction:** **EMT (Electrical Metallic Tubing)** for the main structural components; cut with a
  standard tube cutter; lug ends formed by **squeezing the tubing flat in a vise**, then drilling a
  **1/4 in hole** through the lug. Lug ends of Leg Braces, Cross Beams and Base Plate Supports are **bent at
  an angle**; lug corners may be clipped to remove sharp-corner hazards. The **Thrust Strut has end lugs at
  right angles to one another**.
- **Fasteners:** components joined with **1/4 in bolts** (structural). **#10 machine screws** are the
  **non-structural** fasteners for mounting the rocket motor, Base Plate and load cell attachment brackets.
- **Motor mounting detail:** **hardwood "mushroom plugs"**, drilled part way through to accept the **#10 motor
  mount fasteners**, act as **motor guides**. **Two nuts, one on each side of the Thrust Strut, are adjusted
  so the guides touch lightly against the motor** — this allows the slight downward displacement of the motor
  while firing.
- **Base Plate:** **1/4 in (6 mm) steel or aluminium alloy plate**, cut as a triangle **4.75 in (120 mm)**
  along each side, corners cut off; a hole is drilled as required for load cell mounting.
- **Tension rods:** **1/8 in diameter steel rod**, a hook formed at one end (installed into a blind hole in
  the Leg) and the other end **threaded to accept a #5-32 nut**; the nut is tightened so the rod is under
  moderate tension. Chain-turnbuckle alternative: **eyebolts (#10-24)** attached to the Baseplate Supports,
  turnbuckle hooked to an eyebolt (#10-24) secured in the Leg; tension adjusted by rotating the turnbuckle
  shank.
- **Portability:** after detaching the three Leg Braces the stand **folds up neatly**. The bolt-together
  design also allows **easy replacement of parts damaged when the inevitable CATO occurs**. A **scaled-up
  custom version** was built and used for a successful "M-Class" dual-burn motor test for the **Sugar Shot to
  Space Program in 2006**.
- **Load cells used:** originally a **hydraulic load cell**; now a **strain-gauge load cell**, plus an
  electronic pressure transducer for chamber pressure. A **commercial 500 kg S-beam load cell** is shown
  installed (May 2020).

### 6.3 Safety practices and distances
Source: https://www.nakka-rocketry.net/safety.html
- **"When firing motors (either static or flight), distance is your greatest assurance of safety in case of
  catastrophic failure. I typically position myself (and others) 250–300 feet (75–100 m) away for 'proven'
  motors, even farther for new designs."**
- **Avoid "boilerplate" motor designs** — thick-walled heavy-duty casings "have the capability of storing an
  incredible amount of energy before bursting". **Casings should be sized to burst at no more than 2.5 ×
  MEOP (safety margin 2.5); a minimum safety margin of 1.5 is appropriate for motor design.**
- **Hydrostatic pressure test new motor designs** — fill a completed, sealed motor with water, pressurise
  with a grease gun or hydraulic jack fitted with a pressure gauge, **typically to 1.2 × MEOP**. Compressed
  water stores little energy, but **a plywood shield should nevertheless be placed between the motor and the
  operator in case trapped air is present.**
- **Igniters: leads shunted at all times**, un-shunted only just before connecting to the ignition box (also
  applies to parachute ejection charges).
- **If an igniter fails to initiate a motor, wait several minutes before cautiously approaching, then always
  disconnect the igniter electrical leads first.**
- **Use an ignition box with built-in safety checks** ensuring no current is inadvertently supplied. "**A
  Safe/Arm switch represents only partial security.**"
- When working with propellants, assume they could ignite at any time: **a dunk bucket full of water, a fire
  extinguisher, and a planned escape route** are "three items always present".
- Keep batch sizes of propellants and pyrotechnic materials to the **minimum needed for the job**.
- Energy context given: sugar propellant releases **≈2.7 kJ per gram**; 1 kg holds 2.7 MJ, "equivalent heat
  energy to that released by a 1000 watt heater over a period of 45 minutes", released "typically in 2 or 3
  seconds". AP-based propellants hold nearly double.
- High-energy oxidisers (chlorates/perchlorates) for igniter pyrolants: **limit to small quantities and use
  only proven formulations** such as those on the Igniters page.

---

## 7. Pressure and thrust measurement

### 7.1 Chamber pressure plumbing
Source: https://www.nakka-rocketry.net/pressure-measurement.html (last updated May 26, 2020; originally
posted Aug 1, 2018)

- Two methods: **(a)** an appropriate **analog pressure gauge + video camera** to record the readings —
  cheaper, and **used when testing motors with a higher risk of CATO** (new designs, uncharacterised
  propellants); **(b)** a **pressure sensor interfaced to an electronic DAQ**.
- **Sensor protection is essential and is achieved with a length of copper tubing**: the **cool trapped air
  in the tube compresses on firing and isolates the sensor from the hot gases**, and **copper absorbs some of
  the heat**. Additional protection for a sensor: **pack the inlet port with grease** — this protects the
  element from direct exposure to hot corrosive gases and keeps it cool. **"A heated pressure sensor may give
  erroneous readings."**
- **Fittings: flare fittings, not compression.** "In the aerospace field, flare fittings are used
  exclusively"; compression fittings are simpler but flare gives a much more reliable, leak-free connection
  that withstands repeated use. A **flaring tool** is required. "This is the only type of connection that
  I've ever used for any of my rocketry applications."
- **Exact plumbing:** the bulkhead needs a threaded hole (tapped **1/8 NPT or 1/4 NPT**). A **male adapter
  fitting** (one end flared, other end NPT) screws into the bulkhead with **teflon tape or pipe sealant**.
  **A small ball of medium steel wool inserted into the hole in the bulkhead acts as a filter** to stop liquid
  combustion residue entering — otherwise the residue cools, solidifies and **blocks the line**.
  **A three-foot (1 metre) length of copper tubing, 1/4 inch diameter**, is flared at both ends (slip the
  **flare nuts** on before forming the second flare), with **a full loop bent in the tube** for compactness
  and joint flexibility. One end attaches to the bulkhead male fitting; the other to a **flare female
  adapter** (one end flared, other end female NPT). The **gauge or sensor screws into this adapter**, again
  with teflon tape/sealant on the NPT threads. **Teflon tape/sealant is NOT used on the flared joint.**
- **Combined thrust + pressure setup:** replace the bulkhead male adapter with a **short steel nipple
  (1/8 NPT or 1/4 NPT)**. A **Tee** is connected to the other end. A **square-head plug** is screwed into the
  opposite end of the Tee — **the square head of the plug butts against the load cell, transferring the
  motor's thrust load.** The third Tee connection goes to the copper tube via a flare male adapter and flare
  nut. All three Tee joints are sealed with teflon tape or pipe sealant.
- **Pipe fitting rating note:** standard pipe fittings can be used **even if their "pressure rating" is well
  below the motor's expected MEOP** — for small fittings the actual burst pressure is much greater than
  rated, because the rating incorporates a large safety factor for wear, corrosion and rough handling. Use
  only undamaged (preferably new) fittings.
- **Sampling rate:** with the electronic DAQ, "**100 samples per second is just right**" for pressure. "Too
  high a sampling rate can result in 'noisy' data that needs to be software filtered." A video camera at
  **30 frames per second** is also "perfectly fine for most cases".
- **Delivered c-star for standard sugar propellants is typically 90–95 % of ideal.** Lower values suggest
  preparation shortcomings — inadequate mixing, large oxidiser particle size, or excessive residual moisture;
  chamber pressure plays a lesser role.
- **Thrust coefficient:** a nozzle that is a simple hole has Cf ≈ 1. **A well-designed sugar-propellant nozzle
  can deliver Cf = 1.6 or slightly better** (60 % thrust increase over a simple hole). Cf calculated from
  measured thrust and chamber pressure is only meaningful **during steady-state operation** (start-up and
  tail-off neglected). **If throat erosion occurs, use the average of the initial and final throat
  diameters.**

### 7.2 Strain-gauge load cell — design, wiring and practice
Source: https://www.nakka-rocketry.net/strainlc.html (last updated November 16, 2013)

**Cost rationale:** a basic (single-gauge) load cell built by this method costs **no more than $10–20 USD**;
a four-gauge version **about double**. The value proposition: an inexpensive "dispensible" load cell for
**maiden firings of new or modified designs** that might CATO, saving the commercial unit for proven designs.

**Concept:** a **bending-beam** cell — a **block of metal (steel, aluminium or brass) with a single hole
drilled through it and a slit cut on one side**, creating a **bending "bridge" on the opposite side** to which
the strain gauges are bonded. Force is applied at the bridge, producing combined bending and axial compressive
stress with **bending dominant**. The force/stress relationship is **linear**, hence the output is linearly
proportional to applied load. **Key advantage: total displacement under load is very small**, which "nearly
eliminates unwanted dynamic effects associated with mass and large displacement (e.g. spring) systems" — this
was the specific lesson from the earlier Static Test Rig, which needed a hydraulic damper.
- **Single gauge** — basic. **Two gauges side-by-side** — double the output (double sensitivity/resolution).
  **Full bridge (4 gauges)** — 2 **active** gauges measure strain, 2 **passive** gauges balance the bridge;
  gives excellent sensitivity and, when properly designed, **minimises adverse effects of temperature
  changes**. Mounting is by **a single bolt into a tapped hole at the base of the load cell**.

**Five geometrical variables:** body width **B**, body thickness **t**, hole diameter **D**, location of
applied load **b**, location of the hole **e**. Strain at the gauge (ε_gage) is **directly proportional to
applied load** and **inversely proportional to body thickness (t) and elastic modulus (E)**.

**Design limits (must be observed):**
- **B/3 ≤ D ≤ 2B/3**
- **B ≤ H ≤ 1.75B**
- **B/8 ≤ t ≤ B/2**
- **b ≥ B/2**

**Stress limits:**
- Maximum stress occurs at the **curved surface of the bridge** and is **compressive**; a **stress
  concentration factor k** is read from a chart.
- Design so that **maximum body stress under full load ≈ half the yield stress (Fty)** of the body material,
  to (1) prevent permanent strain affecting calibration and (2) ensure good linear response.
- **The body stress is the limiting factor, never the strain gauge.** A typical foil gauge takes **1 % strain
  (or more)** without damage — **at least double** what a steel or aluminium body can take without permanent
  deformation.
- **For best results, maximum gauge strain should be less than 2000 microstrain; a good design target is
  1500 microstrain.**

**Construction:**
- Design around on-hand material to minimise cutting. Only operations: **drill the body hole, cut the slot,
  drill & tap the mounting hole, and drill a shallow hole for the ball bearing.**
- **Critical:** the body hole location must be accurately marked out and **drilled as a series of
  progressively larger holes** to prevent the location "drifting" during drilling.
- The mounting hole is drilled at **approximately mid-width** then tapped.
- The **slot is simply cut with a hacksaw**.
- **A hardened steel ball bearing is epoxied into a shallow hole** — it "precisely determines the load
  application point" and has the strength to handle large loads. If damaged, it can be removed by **moderately
  heating the ball to soften the epoxy**.
- **Gauge bonding:** **cyanoacrylate or epoxy adhesive (epoxy is easier and perhaps more reliable)**. Lightly
  sand the bonding surface with **600 or finer grit** sandpaper, then clean with **acetone or lacquer
  thinner**. **Active gauges: grid lines running parallel to the long edge.** **Passive gauges (4-gauge
  version): may be mounted anywhere on the body, but the location shown is recommended, with grid lines
  running PERPENDICULAR to the active gauges.** After bonding, **cover the gauge with a protective layer of
  epoxy**, immersing a portion of the lead wires.
- **Exact strain gauges used: OMEGA SG-3/350-LY43 — $45 USD per package of 10.** These had **no lead wires**,
  only very tiny solder pads; **30 AWG wire-wrap wire** was soldered to the pads with an illuminated magnifier
  lamp. A similar type **with lead wires attached** would be **KFG-5-120-C1-11L1M2R — $59 USD per package of
  10**. (Nakka also sold packs of 8 gauges for $20 USD.)

**Prototype: 250 lb (1100 N) capacity load cell**
- Body: **6061 aluminium alloy** block. Dual active gauges + two dummy gauges forming a full bridge.
- Hole diameter, hole location and load application point chosen to achieve 250 lb based on the block's
  dimensions.
- **Maximum deflection under full load measured with a "feeler" gauge: a mere 0.0035 inch (0.09 mm).**
- Calibration: a **32 inch (80 cm) lever arm** amplifying a known load — a **container of water of known
  mass suspended at the end of the lever arm**; an amplifier circuit measured the resistance change as weight
  was added. Alternative: use a **hydraulic load cell** to precisely meter the force applied.

**200 lb (900 N) capacity 4-gauge load cell (for the A-100M motor)**
- 4-gauge arrangement with **2 active + 2 passive**, **all four gauges of the same type**;
  **temperature compensation achieved by mounting all four gauges in close proximity** on the body.
- **Strain gauge specifications:** **350 ohm; Constantan metal foil; phenol resin backing; 3 mm grid length;
  self-temperature compensation for aluminium; operational temperature −10 °C to 70 °C; Gage Factor 2.06;
  strain limit 2 %.**
- The four leads from the bridge attach to a **4-pin connector — RadioShack p/n 274-001 (plugs into p/n
  274-002)**. Alternatives from Digi-Key: **CP-1040-ND (plug) / CP-1240-ND (receptacle)**;
  **CP-1034-ND (locking plug) / CP-1234-ND (locking receptacle)**.

**Verification by FEM:** 3-D models with **more than 1000 tetrahedron elements**, solved with **NASTRAN**.
**Predicted gauge stress agreed well with FEM. Prediction of maximum body stress tended to be conservative by
about 10 percent.** (A 1000 lb / 4.45 kN capacity cell was modelled.)

**Design aid:** **`LOADCELL.XLS`** — enter desired load capacity, body dimensions and material; then choose
hole diameter, hole location and load application point such that maximum body stress does not exceed the
recommended values.

### 7.3 Amplifier circuit — exact topology and parts
- The four strain gauges **SG1–SG4** are arranged in a **Wheatstone bridge**; the bridge output goes to the
  **Vin+ and Vin− terminals of an INA122 instrumentation amplifier**.
- Amplifier output (**Vo and ground**) feeds an **A/D converter**.
- **Power: two 9V batteries**, with the INA122 supply rails regulated by **+5 V and −5 V regulators**; a
  single **DPST switch** powers the amplifier.

**Table 4 — amplifier parts list (Digi-Key P/N):**

| Item | Digi-Key P/N | Qty |
|---|---|---|
| Instrumentation Amplifier | **INA122PA-ND** | 1 |
| Positive Voltage Regulator, 5V | **LM78L05ACZFS-ND** | 1 |
| Negative Voltage Regulator, 5V | **LM320LZ-5.0-ND** | 1 |
| 1.0 microFarad capacitor | **P2105-ND** | 2 |
| Switch | **SW102-ND** * | 1 |
| Fixed resistor ** | — | 1 |
| 9V battery strap connector | **2243K-ND** | 2 |

\* or similar DPDT or DPST switch. \*\* R_G, sets the gain — see below.

**Gain-setting procedure:**
1. Calculate the maximum gauge strain (from the design equation or the spreadsheet).
2. Bridge output: `e = (E/4)·GF·(ε1 − ε2 + ε3 − ε4)` — the change in resistance with strain is given by the
   gauge's **Gage Factor (GF)**, and **E** is the **excitation voltage**.
3. Required gain `G = Vo/e`, where Vo is the desired amplifier output voltage.
4. `R_G` from the INA122 datasheet relation.

**Worked example (200 lb cell):**
- Maximum expected gauge strain from the design table: **1778 microstrain (1778 × 10⁻⁶ in/in)**.
- **GF = 2.06**, excitation **E = 5.0 V**. **SG2 and SG4 are passive, so their strain is always zero.**
- **Bridge maximum output voltage = 0.009157 V.**
- Output range chosen **0 to +5 V**, so required gain **G = 5.0 / 0.009157 = 546**.
- R_G is then computed from that gain.

**Bridge balance:** with zero strain the bridge output is ideally zero (all four gauges the same type, bridge
"balanced"). In reality small resistance differences give a small output that **may be positive or
negative**. This is not a problem — the output "can simply be **zeroed** using the analysis software".
**Alternative: use "balancing resistors" in the Wheatstone bridge** (method described in the Appendix; a
short guide by **Roman Lev** and an online calculator by **Lubos Kobes and Libor Ulcak** are linked).

### 7.4 DAQ hardware
- **DATAQ DI-154RS** — **four channel, 12-bit, up to 250 samples/second**, supplied with **WINDAQ** software.
- Alternative also suitable and affordable: **DATAQ DI-194RS**.
- A linked **"Practical Guide to Wiring Load Cell and Amplifier"** covers gauge mounting/wiring, amplifier
  wiring, and interfacing to a DATAQ unit.

### 7.5 Deriving performance from test data
Source: https://www.nakka-rocketry.net/static.html
- **Thrust coefficient from pressure only:** `F = Cf · Po · At`. For a well-designed, reasonably well-made
  **steel nozzle** (1000 psi operating pressure; **30° convergent half-angle; 12° divergent half-angle;
  expansion ratio > 8**), **Cf can conservatively be taken as 1.5 for sugar propellant**. Throat area from the
  measured diameter. **Measuring solely chamber pressure is a good strategy for new motor designs, because it
  avoids destroying an expensive load cell if the motor over-pressurises and blows out the nozzle or
  bulkhead.**
- **Diagnostics from the pressure trace:** slow ramp-up is often a consequence of an **underpowered igniter**;
  an extended tail-off may mean **delayed ignition of some propellant surface regions**; lower overall chamber
  pressure is often related to propellant preparation, **such as oxidiser particle size**.
- **c-star** is a figure of thermochemical merit indicating combustion efficiency, compared against ProPEP or
  similar. **Thrust coefficient** shows how well the nozzle "amplifies" the thrust versus a simple hole.

---

## 8. Casting and inert grain practice

Source: https://www.nakka-rocketry.net/casting1.html (last updated July 18, 2004) — written around the
**A-100M** motor.

### 8.1 General principle
"**The larger the grain (or rather the mould), the easier it is to cast.**" Small-diameter grains are
"quite tricky": sugar propellants are viscous and do not pour well (casting is "a combination of precise
pouring, hurried scooping and careful packing"); a smaller quantity of slurry **cools more quickly, becoming
even more viscous**; and the propellants are sticky. "After a lot of experimentation that resulted in **many
rejected grains**… a lot of practice may be needed in order to finally get the 'perfect' grain."

### 8.2 Supplies
Melting pot with thermostatically controlled oil bath or deep fryer; tablespoons (stainless or wood) for
stirring/scooping; craft sticks for scooping; **high-temperature grease — Superlube synthetic grease works
well, as does silicone grease** (for coating parts the propellant must not stick to); female mould (the
A-100M motor); mould base; open funnel; casting tube; coring tool; **solid plunger**; **hollow plunger**.

### 8.3 Casting tube (the non-stick liner)
- **Tagboard (file folder paper), cut to 18 × 18 cm**; glue stick; adhesive tape; a **1 in (2.5 cm) diameter
  mandrel** (wooden dowel, metal rod or tube).
- Draw a line **8 cm from one edge**; apply a thin layer of glue (complete coverage not necessary); **roll the
  tagboard around the mandrel starting at the glue-free edge**, tightly, so the finished tube ID equals the
  mandrel diameter; tape the free edge to stop it unrolling; press over the whole surface with a pen to bond
  the glue; **cure ~half an hour before removing from the mandrel**; then **grease the inside** of the tube.
- **Dual function:** it is a non-stick liner **and** it **reduces the cast grain diameter** so the grain is a
  **loose fit within the motor**. The propellant is cast directly into it and **after curing the tube is peeled
  away**.

### 8.4 Mould assembly
- **A light layer of grease is applied onto the nozzle convergent area** to prevent propellant bonding. The
  nozzle is assembled to the casing (**no o-ring needed**). The casting tube is fully inserted into the casing.
- **A small dab of 5-minute epoxy** is placed onto the casting tube **through the two bulkhead attachment
  holes** in the casing — a **"temporary joint"** that prevents the casting tube being **hydraulically forced
  out** when the slurry is compressed.
- **Mould base:** wood, with a **wooden or metal closing rod** protruding. **Closing rod: 1/4 in (0.635 cm)
  diameter** — slightly smaller than the **0.267 in nozzle throat** — a slightly loose fit so **trapped air can
  escape**. **Small vent holes are drilled in the base around the closing pin.** **The closing pin should
  protrude exactly half way up the throat — 1.57 in (4.0 cm) above the base.**
- The motor is placed on the base over the closing pin and **hot glue is applied around the nozzle periphery**
  to temporarily secure it.

### 8.5 Funnel
Open funnels beat closed funnels. Made from a **trapezoidal piece of sheet metal (galvanised steel or
aluminium)** or other heat-resistant material that holds its shape when bent, formed into a **semi-cone (a
cone split in half along its length)**, mounted with a couple of screws onto a wooden handle, and **supported
(vise or clamps) at a 45° angle with its spout directed over the mould**.

### 8.6 Coring rod and plungers
- **The coring rod is the "male mould"** forming the central core; it is **inserted into the molten slurry and
  left in place until the propellant cools and sets**.
- **Solid plunger: a plain circular rod 3/4 in (20 mm) diameter**, used to press the slurry down after loading.
- **Hollow plunger: diameter just slightly less than the mould**, used to compress the slurry and **squeeze out
  air bubbles**. **Its hole lets it slide over the coring rod, because plunging happens AFTER the coring rod
  is inserted.**
- Both plungers are **fabricated from metal**.

### 8.7 Casting sequence (exact)
**Before casting:**
1. **150 g** of powdered propellant mixture prepared and pre-mixed (to account for wastage).
2. **Plungers placed in a freezer at least one hour beforehand** — "the propellant does not stick to a frozen
   surface".
3. **Coring rod preheated in an oven at 300 °F (150 °C) for 15 minutes.**
4. Heating pot/deep fryer preheated to the casting temperature.

**During casting:**
5. Add the powder a few tablespoons at a time, stirring **nearly continuously** until the binder melts and
   forms a molten slurry.
6. At the casting temperature, transfer **about half** the slurry into the funnel with a spoon; coax it into
   the mould with a craft stick. **If the mould blocks, lift the mould and strike it against the table a few
   times** to get the slurry flowing to the bottom. Repeat with the remaining slurry.
7. **Press down gently with the solid plunger until it bottoms. Do not press excessively hard, or the
   propellant will flow past the closing pin.**
8. **Insert the coring rod all the way down into the mould.**
9. **Slide the hollow plunger over the coring rod** and press down for final packing. **Hold the end of the
   coring rod to stop it being forced out by the pressure. Do not press excessively hard.**
10. **Withdraw the plunger most of the way but leave it partly inserted to keep the coring rod centred.**

**Cooling before disassembly: KNDX 30–45 minutes; KNFR 60–75 minutes; KNSB must be allowed to cool and cure
for 24 hours.**

**Table 1 — recommended casting temperatures:**

| Formulation | Casting temperature |
|---|---|
| KNDX | **135 °C / 275 °F** |
| KNSB | **130 °C / 265 °F** |
| KNFR | **125 °C / 260 °F** |

### 8.8 Demoulding
- **Use a hairdryer to soften the hot glue** bonding the nozzle to the mould base.
- **Remove the coring rod by firmly gripping the protruding end in a vise or with locking pliers.**
- **Slide the female mould off.**
- **Grasp the grain and give it a quick rotational twist** — this breaks the weak "bond" between coring rod
  and propellant, allowing the rod to be pulled out.
- **Slit the casting tube lengthwise, then peel it off.**

### 8.9 Grain finishing, drying and coating
- The grain has a **thin residual grease coating on the outer and core surfaces — this must be cleaned off
  completely to prevent delayed or failed ignition**, using **acetone or lacquer thinner**.
- The grain may be **sticky** from residual moisture driven out of the mix by casting heat and **trapped at the
  casting-tube interface**. Dry it in a **desiccator** — a sealed container (e.g. Tupperware) with
  **calcium chloride, silica gel or other desiccant pellets**. **Pellets must not contact the grains**, or they
  dissolve and stick to them.
- **For long-term storage a desiccator must NOT be used** — evidence suggests the grain can get **overly dry,
  producing a burn rate greater than normal, which could result in a CATO**. Long-term: **zip-lock bag, then
  freezer**.
- Trim as required, then **record grain mass and dimensions** (key dimensions shown in Fig. 4).
- **Apply the thin Ignition Powder/IPA coat** (see §2).

### 8.10 Grain density check — the quantitative void/porosity assessment
- **Method:** compute grain volume from measured dimensions; **grain density = mass / V_g**; compare to the
  **ideal mass density** — that of a "perfect" grain with **no trapped air, inclusions, surface flaws, or
  other imperfections affecting grain volume**.
- **Density ratio (%) = (calculated grain density / ideal density) × 100.**
- **"I've typically obtained grain densities of 95 % ideal using the casting method described here."**
- **"If the measured grain density is less than around 90 %, this implies significant air inclusion
  (porosity) or the presence of significant flaws or air bubbles."**
- **External** air bubbles/flaws can be **repaired by opening a cavity and filling it with molten propellant**.
- **If density < 90 % and no external flaws are apparent, then either hidden voids exist or porosity is
  present, and the grain should be discarded. The consequence of firing such a grain could result in a CATO
  due to unpredictable burning-rate behaviour.**
- Tool: **`Graindensity.xls`** (Grain Density Check spreadsheet) — performs the volume/density calculation and
  provides **ideal densities for a wide variety of sugar propellants, including those doped with oxides or
  other ballistic modifiers** (Table A1).

> **Gap flagged:** the numeric ideal-density values of Table A1 are delivered as an image on the page and are
> not recoverable as text; only the *ratio* criteria (95 % typical, 90 % discard threshold) are in text.

### 8.11 INERT propellant grains
Source: https://www.nakka-rocketry.net/inert.html (last updated June 8, 2002)

- **Purpose:** to practise and refine the casting process — and to experiment with process modifications —
  without using real propellant. It is "rather convenient, less expensive, and indeed more safe." Achieving a
  satisfactory sugar grain "can be something of a challenge, especially for the neophyte"; the high-viscosity
  slurry thickens rapidly as it cools, so loading the mould must be "efficient and timely", usually by a
  **combination of pouring and scooping**, with care to **minimise the inclusion of air pockets**. Practice
  helps develop casting skill and "pinpoint process deficiencies".
- **Recipe: INERT propellant is prepared in exactly the same manner as genuine propellant, except that common
  table salt (sodium chloride) is substituted for potassium nitrate as the oxidiser.** **The O/F ratio remains
  the same (65/35)**, as do all other aspects of preparation (per the respective propellant pages). This
  applies to **KNSU, KNDX and KNSB**.
- **Fidelity:** "Both the melting rate and the viscosity of the melted slurry of the INERT propellant has been
  found to be **quite similar** to genuine propellant."
- **The one observed difference:** the **sucrose- and dextrose-based INERT propellants caramelise to a greater
  extent** — attributed to differences in thermochemical properties between KN and NaCl. This **does not
  adversely affect the simulated behaviour**, and is in fact **beneficial as a means of identifying INERT
  material**.
- **Identification is a safety requirement:** "It'd not bode well to inadvertently load an INERT grain into a
  rocket motor. **Of more serious concern, a grain of genuine propellant must never be inadvertently mistaken
  as a simulated grain!**" Recommendation: **add a drop of food dye or a pigment** to the mixture to identify
  the cast product as INERT.
- **Substitute materials investigated:** only **sodium chloride** and **potassium chloride** tried so far.
  **KCl gave more severe caramelisation than NaCl.** **Magnesium sulphate (MgSO₄)** may be an even better
  substitute — commonly available as **Epsom salts** — **but it is hydrated, containing approximately 30 %
  molecular-bound water, and so must first be desiccated.**
- **Explanation offered:** the difference lies in **specific heat capacity (C_s)**. NaCl's C_s is lower than
  KN's **over the full temperature range of interest**, and **KN experiences a step increase in C_s at
  approximately 125 °C due to a phase change of the solid material**, making the difference even more
  pronounced. KCl's C_s is **notably lower** still — consistent with the more severe caramelisation observed.

---

## 9. KNSB burn characteristics, defects and failure modes

Source: https://www.nakka-rocketry.net/knsbchar.html — **"Burn Characteristics of Sorbitol Based Propellants"
by Chuck Knight** (last updated March 9, 2003).

### 9.1 The three anomalies
1. **A slower burn rate in motors than predictions based upon strand burn rate tests.**
2. **An achieved specific impulse much less than the theoretical specific impulse.**
3. **A progressive burn characteristic, even with motors whose grains have been designed to provide a flat
   response.**

Observed by Richard Nakka with his **KSB** motors, by other experimenters, and in **PVC motors**. Theories
offered for these odd characteristics include **crack formation** and **delayed ignition**. Knight proposes
an alternative: **flushing**.

### 9.2 The flushing ("burn/flush") theory
1. **Upon ignition, there is no delayed ignition and all exposed surfaces ignite quickly.** Evidence: the
   **"knee" on the leading edge of almost every published thrust curve for sorbitol propellant** (sharpness
   varies motor-to-motor; grain geometry probably shapes it), typically showing thrust reaching a plateau,
   flattening, then peaking — very evident in the **"G" motor**. **Nakka's KSB-002 ignition-initiator
   experiment compared to KSB-001 showed little difference in thrust-curve shape**, "further evidence that
   ignition spreads quickly to all exposed surfaces."
2. **A process erodes the grain surface — not erosive burning, but a "flushing" action occurring FASTER than
   the propellant burn rate.** Two effects:
   - **(a) Performance loss** — propellant is expelled before it can burn and contribute impulse. First
     noticed comparing the **"G", "H" and "I" motors: the G and H had specific impulses of only 108 seconds
     while the I motor had 129 seconds.** Explanation: the **I motor's grain was twice as long**, allowing a
     more complete burn.
   - **(b) Progressive burn** — flushing results from heat melting the sorbitol plus rapidly moving gases
     pushing molten propellant out of the motor. **Gases flow slowest at the top of the grain and fastest near
     the nozzle**, so the core is shaped into a **cone with its base at the nozzle**. The **coning action
     increases Kn faster than predicted by conventional uniform burn rate models**, producing the progressive
     character.

### 9.3 Quantitative burn/flush rates (K1000 motor)
- **The flowing gases do NOT affect the burn rate at the top of the core or on the end surfaces. These are the
  only surfaces exhibiting the true burn rate of sorbitol propellant.** (Hence a uniform burn-rate model can
  be used to design a *regressive* curve that compensates for coning and yields a flat thrust curve.)
- Assuming ignition is very rapid, the **knee (point A)** of the thrust curve represents the **initial Kn** —
  "easily calculated" and "the only point during the burn that the Kn is known with any certainty". Flushing
  is ignored there because it has not had time to take effect.
- **Initial burn rate at the moment of ignition, rb = 0.279 in/sec.** The **strand-burn-test-based** burn rate
  at point A **computes to 0.305 in/sec** — "**the reason for the difference between the two burn rates is not
  clear**."
- **Point B** = the instant the flame front reaches the grain OD, i.e. has burned through a **web thickness of
  0.485 in**. **Time A→B = 1.53 seconds** → **combined burn/flush rate over that interval = 0.381 in/sec, or
  1.37 times faster than the initial burn rate.** "This accelerated rate is the flush rate of the propellant."
- **Total burn time 2.0 seconds**; **A to total burn = 1.74 seconds** → burn rate at the **top of the grain =
  0.279 in/sec**, exactly the rate calculated at point A. The model suggests the **web at the top of the core
  is not breached until the burn process comes to a complete end.**
- A spreadsheet computed and plotted Kn in **20 steps** across the top of the grain, with the progression rate
  nearest the nozzle adjustable by any **flush rate factor > 1.0**.
  - **Flush rate = 1.0** → Kn matches the regressive uniform-burn-rate prediction.
  - **Flush rate = 1.37** → **Kn takes a dramatic plunge near the end of the progression**, caused when the
    **bottom edge of the cone reaches the grain OD, leaving a wedge-shaped grain in the upper portion that
    shortens at an ever-increasing rate** as the cone tries to widen.
- **The wedge explains the low specific impulse:** propellant in the wedge "contributes little or nothing to
  the overall total impulse", but Isp = total impulse ÷ **total propellant weight including the
  non-contributing portion**, so the computed Isp is smaller than the instantaneous performance.
- The model found the **added conical surface area did NOT compensate** for the regressive curve; the flat
  thrust curve came about because **most propellant burned across the short flat portion**. The descending
  portion of the Kn plot is **concave**, a shape prevalent in published thrust curves and more pronounced as
  the flush rate increases.

### 9.4 Long-chamber experiment (direct performance evidence)
A **"G" motor was built with a 13 in chamber but a 7 in propellant grain** matching the original G design.
The grain was placed **at the top of the motor** with a **6 in spacer between grain and nozzle**, fired in the
same test stand as the rest of the PVC series.
- **Original "G" motor: Isp = 108 seconds. Long-chamber "G" motor: Isp = 124 seconds.**
- Conclusion: "Clearly, propellant is being **flushed from the grain and burned in the aft section of the long
  chamber** that boosts the performance of the motor."

### 9.5 Practical design guidance from this analysis
- Long, slender grains outperform short, fat ones.
- **"The minimum length of a Sorbitol grain to achieve optimum performance is on the order of 13" – 15"."**
- Traditional uniform burn-rate models are "good enough to compute approximations for motor designs that can
  be refined through experimentation".
- **Open question:** why burn rates (exclusive of flush rate) seem slower than strand-burn-test predictions —
  "may lie in the chemistry of Sorbitol, which is beyond the scope of this article."

### 9.6 Related failure modes documented elsewhere
- **Delayed ignition** is a *postulated* cause of the peculiar results from **static test KSB-001** of the
  Kappa-SB motor (https://www.nakka-rocketry.net/ignexp.html) — although Knight's KSB-002 evidence argues
  against ignition as the primary cause.
- **Crack formation** is the other listed theory for the sorbitol anomalies (knsbchar).
- **Grain web cracking and disbonding** are the two case-bonding failure modes, both leading to
  **catastrophic failure by over-pressurisation from an unexpected increase in burning area** (casebond).
- **Under-dense grains (<90 % of ideal) → CATO** from unpredictable burning-rate behaviour (casting1).
- **Over-dry grains → abnormally high burn rate → CATO** (casting1).
- **Oversized igniter charge → startup pressure spike → shearing of the motor-head safety bolts** (igniter).
- **Boilerplate casings store enormous energy before bursting**; design to burst at **≤2.5 × MEOP**, minimum
  safety margin **1.5** (safety).

---

## 10. Consolidated component / part-number index

| Item | Identifier | Source page |
|---|---|---|
| Strain gauge (no leads) | **OMEGA SG-3/350-LY43**, $45 USD / pkg 10 | strainlc.html |
| Strain gauge (leads attached) | **KFG-5-120-C1-11L1M2R**, $59 USD / pkg 10 | strainlc.html |
| Instrumentation amplifier | **INA122** (Digi-Key **INA122PA-ND**) | strainlc.html |
| +5 V regulator | Digi-Key **LM78L05ACZFS-ND** | strainlc.html |
| −5 V regulator | Digi-Key **LM320LZ-5.0-ND** | strainlc.html |
| 1.0 µF capacitor | Digi-Key **P2105-ND** (×2) | strainlc.html |
| Power switch | Digi-Key **SW102-ND** (or DPDT/DPST) | strainlc.html |
| 9 V battery strap | Digi-Key **2243K-ND** (×2) | strainlc.html |
| Load-cell connector | RadioShack **274-001** (plug) / **274-002** (receptacle) | strainlc.html |
| Load-cell connector alt. | Digi-Key **CP-1040-ND**/**CP-1240-ND**; **CP-1034-ND**/**CP-1234-ND** | strainlc.html |
| A/D converter | **DATAQ DI-154RS** (4-ch, 12-bit, ≤250 Hz) + WINDAQ; alt. **DI-194RS** | strainlc.html |
| Ultra-low current igniter lamp | RadioShack **272-1139** mini lamp | igniter.html |
| Fine bridgewire | **30 AWG "wrapping wire"**, RS p/n **278-501** | igniter.html |
| Commercial load cell | **500 kg S-beam** load cell | sts5000f.html |
| Design spreadsheets | `IGNITER.XLS`, `LOADCELL.XLS`, `Graindensity.xls`, `CASING.XLS`, `THERMCAS.ZIP`, `LOADCELL.XLS` | various |

---

## 11. Provenance and gaps

**Retrieval method.** The live host returns **HTTP 403 — "Access denied by Imunify360 bot-protection. IPs
used for automation should be whitelisted"** to automated retrieval. Content was therefore taken from
**Wayback Machine snapshots** of the canonical URLs. Confirmed snapshot dates: `igniter.html` 2025-01-09;
`therm.html` 2023-12-03; `casting1.html` 2026-04-14; `strainlc.html` 2019-12-17; `sts5000f.html` 2025-04-05;
`safety.html` 2026-04-14; the remainder from the nearest 2024 snapshot. Several snapshots for `therm.html`
and `strainlc.html` had captured Imunify360 challenge pages instead of content and were rejected; the
snapshots listed above returned verified content.

**Page revision dates (from page footers):** igniter 2022-03-01; casebond 1999-08-23; therm 2000-02-27;
static 2020-05-14 (orig. 2000-08-10); pressure-measurement 2020-05-26 (orig. 2018-08-01); strainlc 2013-11-16;
casting1 2004-07-18; inert 2002-06-08; knsbchar 2003-03-09; sts5000f 2020-05-25 (orig. 2000-08-06).
`ignexp.html` and `safety.html` carry no footer date.

**Gaps / items not found in the ten requested pages:**
1. **No "thick coat" primer variant.** All primer guidance on these pages specifies a **thin, light, single
   coat** (~200 µm / 0.0075 in); the only explicit *thickness limit tied to a failure mode* is the ≤3 mm
   (disc ≤2 mm) rule for the **Ferocious** epoxy/KP pyrolant, where a thicker coating **fractures on firing**.
2. **Ignition Powder / KNSB ideal density values** (Table A1, `Graindensity.xls`) are page images and are not
   recoverable as text; only the 95 %-typical / 90 %-discard ratios are stated in text.
3. **Case-bonding final wall thicknesses** were presented as inline equation images; the page's stated
   **casing masses (0.47 lb/in steel, 0.38 lb/in aluminium)** are the authoritative figures, and thicknesses in
   §4 are recomputed from the stated method and flagged.
4. **No specific pressure-transducer or gauge model number** is given on `pressure-measurement.html` — the
   page treats "analog pressure gauge" and "pressure sensor" generically. The only commercial transducer
   identified anywhere is the **500 kg S-beam load cell** on `sts5000f.html`.
5. **`knsb.html` does not exist** (Wayback returns a 404 page), so no separate KNSB propellant-formulation page
   was consulted. Formulation data (e.g. 65/35 O/F, 130 °C casting temperature) appears on `inert.html` and
   `casting1.html` as noted.
6. **Safety distances** appear on `safety.html` (250–300 ft / 75–100 m for proven motors), **not** on
   `static.html`, which contains no standoff guidance.
7. The **STS-5000 structural dimensions (Table 1 tube cut/hole-to-hole, Table 2 fasteners)** are page images
   and are not recoverable as text; the qualitative construction description and all text-stated dimensions
   are captured in §6.

**Extracted clean text of every page** (including `sts5000f` and `safety`) is saved under
`~/nakka_extract/txt/` with the original raw HTML under `~/nakka_extract/raw/`.
