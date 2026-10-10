# Communications and Ground Station — UVCE Rocketry Club

**Document:** `30_AVIONICS/Communications_and_Ground_Station.md`
**Rev:** 1.0 · **Status:** Design baseline for PDR
**Scope:** RF link, ground station hardware, ground station software, packet protocol, link testing

> **Companion documents:** [Flight Computer Architecture](Flight_Computer_Architecture.md) · [Sensors and Instrumentation](Sensors_and_Instrumentation.md) · [Recovery Electronics and Control](Recovery_Electronics_and_Control.md) · [Electronics BOM and Sourcing](Electronics_BOM_and_Sourcing.md)

---

## 0. The requirement in one paragraph

The rules require telemetry at **≥ 1 Hz** from a launch pad that is **about 1 km from the viewing gallery**, carrying all 15 Annexure-2 fields, with an **RF command to switch telemetry ON/OFF**, on **separate channels** for the rocket and the CAN-7USAT payload, with **NETID/PANID set to the team number**, plus **redundant onboard SD logging** for link loss, and a **portable ground station** with **≥ 2 h of battery**. The radio must be **XBee/Zigbee Series 1/2/Pro or LoRaWAN**, industrial grade.

That is a **link budget** problem plus a **software** problem. This document solves both.

---

## 1. Radio options compared

### 1.1 The shortlist

| Radio | Band | Max TX power | Typical LOS range (with stock antenna) | Air data rate | Interface | Indian unit cost (INR) | Indian legality | Verdict |
|---|---|---|---|---|---|---|---|---|
| **XBee Series 1** (802.15.4, `XB24-AWI-001`) | 2.4 GHz | **0 dBm (1 mW)** | 100–300 m | 250 kbps | UART | ₹1,400–2,200 | ✅ **License-exempt** (2.4 GHz ISM, 2.400–2.4835 GHz, 100 mW EIRP allowed) | ❌ **Range is hopeless for 1 km.** Non-Pro Series 1 is explicitly not industrial grade. Do not buy. |
| **XBee Series 1 PRO** (`XB24-DPIS-001` / `XBP24-AWI-001`) ⭐ | 2.4 GHz | **18 dBm (63 mW)** | **1–2 km** LOS | 250 kbps | UART | ₹2,400–3,800 | ✅ License-exempt (63 mW < 100 mW EIRP) | ✅ **RECOMMENDED — this is the rules-compliant baseline.** Meets "Pro" and "industrial grade". |
| **XBee Series 1 PRO, 60 mW with SMA** (`XBP24-AWI-001`, RPSMA) | 2.4 GHz | 18 dBm | 1.5–3 km with a 5 dBi antenna | 250 kbps | UART | ₹2,600–4,200 | ✅ | ✅ Best XBee variant: **external antenna connector** lets you use a proper elevated ground antenna. **Buy the RPSMA version, not the chip-antenna version.** |
| **XBee Series 2 / Series 2 PRO** (`XB24-Z7WIT-004`, `XBP24-Z7WIT-004`) | 2.4 GHz | 2 / 18 dBm | 0.1 / 1–2 km | 250 kbps | UART | ₹2,000–3,600 | ✅ | ⚠️ **Avoid.** Series 2 runs ZigBee mesh firmware: it must **join a network through a coordinator with a 64-bit address**, adds join latency of seconds, and a rocket that leaves and re-enters range will drop off the mesh. **Series 1 (802.15.4, peer-to-peer, no coordinator)** is dramatically better for a point-to-point telemetry link. The rules say "Series 1/2/Pro" — choose Series 1 Pro and justify it. |
| **XBee-PRO 868** (`XBP08-DP`) | **868 MHz** (India's 865–867 MHz band is close) | **25 dBm (316 mW)** | **10–15 km** | 24 kbps | UART | ₹3,500–6,500 (import) | ⚠️ **865–867 MHz is license-exempt in India** (G.S.R. 1046(E), 2021 — 865–867 MHz, 1 W EIRP). The 868 MHz variant is 1–2 MHz off. **Verify with the Wireless Planning & Coordination (WPC) wing before transmitting.** | ⚠️ Technically superb (huge link margin, low data rate is fine for 1 Hz ASCII), but frequency compliance is a genuine question and it needs an import + a WPC licence or exemption confirmation. **Do not bet the CDR on it.** |
| **LoRa — RFM95W (SX1276) 868/915 MHz** | 868/915 MHz | **+20 dBm (100 mW)** | **5–15 km** LOS with SF7–SF9 | 0.3–37.5 kbps | SPI | ₹450–900 (module) | ⚠️ Same 865–867 MHz question. **Semtech SX1276/78 modules can be tuned to 865–867 MHz**, which is license-exempt in India. | ✅ **Technically the best choice for range.** 56 dB of link margin (see §2). BUT: it is **not** XBee/Zigbee, and the rules name XBee or LoRaWAN. ⚠️ **Plain LoRa ≠ LoRaWAN** — LoRaWAN implies a network server and a gateway. Present it honestly as a **secondary/backup link** and see §1.4. |
| **LoRa — SX1278 (Ra-01/Ra-02), 433 MHz** | **433 MHz** | +20 dBm | 3–10 km | 0.3–37.5 kbps | SPI | ₹250–600 | ⚠️ **433 MHz is NOT a general license-exempt band in India** for this kind of use — it is allocated for specific low-power applications and remote control, with power limits. **This is the module everyone in India buys and everyone assumes is legal. Verify before you transmit.** | ⚠️ Cheap, long range, **legally ambiguous**. If you use it, keep the power low, document your reasoning, and do not present it to the Jury as your primary compliant link. |
| **ESP32 WiFi (onboard)** | 2.4 GHz | +20 dBm | 100–300 m (LOS, stock PCB antenna) | up to 72 Mbps | — | ₹280–450 (whole dev board) | ✅ License-exempt | ❌ **Wrong tool.** WiFi association takes 1–3 s, needs a network, consumes 120–240 mA, and the range is inadequate. **Excellent as the ground station's laptop-side convenience link, never as the flight link.** |
| **ESP32 + LoRa (Heltec WiFi LoRa 32 V3)** | 868/915 MHz | +21 dBm | 5–15 km | 0.3–37.5 kbps | USB/UART | ₹1,600–2,800 | ⚠️ Same frequency question | ✅ **Excellent ground-station radio.** Do not fly it (too heavy, no shock rating). |
| **NRF24L01+ / NRF24L01+PA+LNA** | 2.4 GHz | 0 / **+20 dBm** | 100 m / 0.8–1.5 km | 2 Mbps / 1 Mbps / 250 kbps | SPI | ₹80–200 / ₹350–700 | ✅ License-exempt | ⚠️ **Not recommended for flight.** No error correction, no acknowledgements unless you implement them, primitive address filtering, and the PA+LNA module draws 115 mA peaks with a **notoriously noise-sensitive 3.3 V supply**. As a **secondary backup telemetry link** it is a legitimate ₹700 insurance policy. As a primary, it is a hobby part, not industrial grade. |
| **RFD900x / SiK telemetry radio (915 MHz)** | 902–928 MHz | +20 dBm / +30 dBm | 40+ km | 250 kbps | UART | ₹8,000–16,000 | ❌ **902–928 MHz is not available in India.** These are US-band. Do not buy. |
| **Satellite / Iridium** | — | — | Global | — | — | ₹40,000+ | — | Overkill and out of budget. |

### 1.2 The rules-compliance decision

The rule text: *"XBee/Zigbee Series 1/2/Pro or LoRaWAN (industrial grade)."*

**Primary (compliant, low-risk): `XBee Series 1 PRO`, 2.4 GHz, 18 dBm, RPSMA antenna connector.**
- Meets the letter of the rule (XBee, Series 1, Pro).
- 2.4 GHz ISM is unambiguously license-exempt in India at ≤ 100 mW EIRP. Your 18 dBm (63 mW) into a 2.4 dBi antenna gives 20.4 dBm EIRP = **110 mW** — ⚠️ **that is marginally over 100 mW EIRP.** With a 2 dBi antenna: 20 dBm EIRP = 100 mW exactly. With a **5 dBi** ground antenna: 23 dBm EIRP = 200 mW, over the limit.

  > 🔎 **Resolve this before the CDR.** Options: (a) reduce the XBee's `PL` (power level) to `PL=2` (10 dBm) or `PL=1` (8.4 dBm) and compensate with antenna gain on the *ground* side; (b) request a written clarification from the faculty advisor to IN-SPACe. **Do not silently run 200 mW EIRP and hope.**

- 250 kbps air rate is 250× more than you need (1 Hz × ~100 bytes = 800 bps), which converts directly into link margin in the form of retries.

**Secondary / demonstration (optional, disclosed): `LoRa RFM95W` tuned to 865–867 MHz.**
- 56 dB of link margin (see §2) — the range is simply not a question.
- Zero-configuration point-to-point, no coordinator, no association.
- Present it in the CDR as: *"Our primary link is XBee-PRO S1 per the rules. We have additionally qualified a LoRa link at 866 MHz as an independent backup, because (a) it provides 30+ dB more margin at the required range and (b) it operates in a different band, so a 2.4 GHz interference environment at the launch site cannot take out both links."* **That is a stronger CDR than either radio alone.**

### 1.3 Why Series 1 and not Series 2 — the technical reason

| Behaviour | Series 1 (802.15.4) | Series 2 (ZigBee) |
|---|---|---|
| Topology | **Peer-to-peer.** Any node talks to any node by address. | Coordinator + router + end device. Must **join** a network. |
| Time to first byte after power-on | **~50 ms** | **2–10 s** (network join, or longer if the coordinator is busy) |
| Behaviour when the rocket leaves and re-enters range | Link simply resumes | Device may need to **rejoin the network** |
| Configuration | Set `PAN ID`, `MY`, `DL`, `BD`, done | Set `PAN ID`, `MY`, plus coordinator/end-device roles, plus join security (link key, or `KY=0` to disable) |
| Failure mode | Missed packets | **The rocket cannot join the network at the pad and you have no telemetry at all** |

> 💡 For a **point-to-point telemetry link between exactly two nodes**, a mesh network is pure added failure surface. Series 1 is the correct engineering choice, and you should say so explicitly in the CDR — it demonstrates that you understood the difference rather than picking the cheaper board.

### 1.4 If the Jury asks "why not LoRaWAN?"

Answer honestly: *"LoRaWAN is a network protocol requiring a gateway and a network server, with duty-cycle limits and an adaptive-data-rate regime designed for static, low-power nodes. Our application is a single point-to-point link for 120 seconds. We use the same LoRa PHY, in raw point-to-point mode, which is what the rule intends — the alternative would be to stand up a LoRaWAN gateway at the launch site for one rocket, which adds a single point of failure with no benefit."*

If the Jury insists on LoRaWAN, you can satisfy it with the **same RFM95W hardware plus a LoRaWAN stack**; the hardware does not change, so this is a firmware decision, not a purchasing one. **Say that in the CDR.** It converts a potential non-compliance into evidence of design forethought.

---

## 2. Link budget — how to compute it, with a worked example

### 2.1 Why RSSI and link budget matter

**RSSI** (Received Signal Strength Indicator) is the measured received power in dBm. Every radio reports it. It matters because:

1. **It is your only real-time health indicator.** A falling RSSI means the link is about to fail — you want that warning *before* you lose telemetry, not after.
2. **It converts to a margin.** `Margin = RSSI − Sensitivity`. Margin > 10 dB is comfortable; 0–6 dB means you are one tumbling manoeuvre away from losing the link.
3. **Antenna nulls are real.** A rocket rolling at 5 rev/s sweeps its antenna pattern 5 times a second. If the rocket antenna is linearly polarised and the ground antenna is linearly polarised, **cross-polarisation can cost you 20–30 dB** twice per revolution. With a 17 dB margin you survive; with a 3 dB margin you get dropouts at roll rate.
4. **It is evidence.** A logged RSSI-versus-range curve is exactly the kind of "we tested it" material the CDR rewards.

⚠️ **RSSI is not calibrated.** XBee RSSI is a relative indication (±3–6 dB unit-to-unit). Use it for *trends and margin estimation*, never as an absolute measurement. For an absolute number you need a spectrum analyser or a calibrated receiver.

### 2.2 The link budget equation

```
  P_rx (dBm) = P_tx + G_tx − L_tx + G_rx − L_rx − FSPL + G_misc

  where:
    P_tx   = transmitter output power (dBm)
    G_tx   = transmit antenna gain (dBi)
    L_tx   = transmit-side cable + connector loss (dB, positive number)
    G_rx   = receive antenna gain (dBi)
    L_rx   = receive-side cable + connector loss (dB, positive number)
    FSPL   = free-space path loss (dB)  =  32.44 + 20·log10(f_MHz) + 20·log10(d_km)
    G_misc = polarization / multipath / body-loss allowance (dB, usually negative)

  Margin (dB) = P_rx − Sensitivity_rx
```

**The number every rocket team underestimates: the ground station's cable loss.** An SMA connector pair is 0.2 dB each, and RG-58 at 2.4 GHz is **0.6–0.9 dB per metre**. A 10 m coax run to a mast-mounted antenna costs you **7–9 dB** — more than doubling your required transmit power. **Mount the radio at the top of the mast and run USB/Ethernet (or a long power+data cable to the radio) instead of running coax.** This single decision is worth more than any antenna upgrade.

### 2.3 Worked example 1 — XBee-PRO S1, 2.4 GHz, 2 km (the recommended link)

**Setup:** rocket XBee-PRO S1 at 18 dBm with a ¼-wave wire dipole (2.1 dBi) inside the airframe; ground station XBee-PRO S1 at 18 dBm into a 2.4 GHz 8 dBi patch on a 3 m mast, with the radio mounted **at the antenna**.

| Term | Value | Notes |
|---|---|---|
| `P_tx` | +18.0 dBm | XBee-PRO S1 `PL=4` (maximum) |
| `G_tx` | +2.1 dBi | ¼-wave wire dipole inside the airframe. ⚠️ The airframe and the motor casing detune this — assume **0 dBi effective** to be honest. |
| `L_tx` | −0.5 dB | Short pigtail + 1 connector |
| `G_rx` | +8.0 dBi | 2.4 GHz 8 dBi patch (TP-Link TL-ANT2408CL class) |
| `L_rx` | −0.5 dB | Radio mounted at the antenna, 0.3 m pigtail |
| **FSPL at 2.4 GHz, 2 km** | **−106.0 dB** | `32.44 + 20·log10(2450) + 20·log10(2.0) = 32.44 + 67.78 + 6.02 = 106.24 dB` |
| Polarisation loss | −3.0 dB | Rocket roll; linear-to-linear with rotation. Expect up to −20 dB at cross-polarisation instants — this is an *average*. |
| Multipath / ground reflection | −3.0 dB | Two-ray ground bounce over 2 km of flat ground |
| **P_rx** | **+18 + 2.1 − 0.5 + 8.0 − 0.5 − 106.24 − 3.0 − 3.0** | |
| **P_rx** | **= −85.1 dBm** | |
| XBee-PRO S1 sensitivity @ 250 kbps | −100 dBm | From the datasheet |
| **Margin** | **+14.9 dB** | ✅ |

**Verdict:** a **14.9 dB margin at 2.0 km**. That is workable but not generous. Two honest qualifications:

1. **If the rocket antenna is a chip antenna** (0 dBi, and worse in a metal airframe), the margin drops to **~11 dB**. Still workable.
2. **If you use the compliance-limited 10 dBm setting** (`PL=2`) to stay under 100 mW EIRP, the margin drops to **~6.9 dB** — **marginal.** At 6.9 dB, a deep cross-polarisation fade will cost you the packet.

**Therefore:** with the XBee-PRO at full power, keep the **8 dBi patch on the ground** (23 dBm EIRP on the ground side is a receiver-side question, not a transmitter-side one — **antenna gain on receive does not increase your radiated power**, so a high-gain *receive* antenna is always compliant). Transmit at 18 dBm from the rocket is 63 mW + 2.1 dBi = 20.1 dBm EIRP ≈ **102 mW** — essentially exactly at the limit.

> 💡 **The cleanest compliance answer:** run the **rocket** at `PL=2` (10 dBm) and put **all** the gain on the ground: an 8 dBi patch *and* a low-noise receive preamplifier (LNA, e.g. Mini-Circuits ZX60-P103LN+, ~₹4,000) or a 12–15 dBi Yagi. Ground-side gain and receive-side gain are not restricted. Rocket EIRP then = 10 + 2.1 = **12.1 dBm = 16 mW** — comfortably compliant — and the link budget becomes:

| Change | Value |
|---|---|
| `P_tx` | +10.0 dBm (`PL=2`) |
| `G_rx` | +15.0 dBi (2.4 GHz 15 dBi Yagi, ~₹1,800–3,000 for a wifi-grid/Yagi) |
| **P_rx** | **10 + 2.1 − 0.5 + 15.0 − 0.5 − 106.24 − 3.0 − 3.0 = −86.1 dBm** |
| **Margin** | **+13.9 dB** ✅ **with only 16 mW EIRP from the rocket** |

**This is the design to put in the CDR.** It is compliant by a wide margin, and it works.

### 2.4 Worked example 2 — LoRa RFM95W at 866 MHz, 2 km (the backup link)

| Term | Value | Notes |
|---|---|---|
| `P_tx` | +20.0 dBm | SX1276 at `PA_BOOST`, 100 mW |
| `G_tx` | +2.1 dBi | ¼-wave at 866 MHz is **86 mm** of wire — easy to fit |
| `L_tx` | −0.5 dB | |
| `G_rx` | +5.0 dBi | 866 MHz 5 dBi omni on a 3 m mast (₹600–1,200) |
| `L_rx` | −0.5 dB | Radio at the antenna |
| **FSPL at 866 MHz, 2 km** | **−97.2 dB** | `32.44 + 20·log10(866) + 20·log10(2.0) = 32.44 + 58.75 + 6.02 = 97.21 dB` |
| Polarisation | −3.0 dB | |
| Multipath | −3.0 dB | |
| **P_rx** | **20 + 2.1 − 0.5 + 5.0 − 0.5 − 97.21 − 3.0 − 3.0** | |
| **P_rx** | **= −77.1 dBm** | |
| SX1276 sensitivity, SF7, BW 125 kHz | **−123 dBm** | Datasheet |
| SX1276 sensitivity, SF9, BW 125 kHz | **−129 dBm** | Higher spreading factor, lower data rate |
| **Margin (SF7)** | **+45.9 dB** | ✅ |
| **Margin (SF9)** | **+51.9 dB** | ✅ |

**Verdict: 46–52 dB of margin.** That is 32 dB better than the XBee link. Even at **20 km** the LoRa link would still have ~26 dB of margin, which is why long-range drone/rocket telemetry has moved to LoRa.

⚠️ **But note the tradeoff:** at SF9/BW125 the data rate is 1.76 kbps. Your packet is ~100 bytes = 800 bits. At 1.76 kbps a packet takes **455 ms of air time** — so 1 Hz telemetry is right at the edge, and you must not exceed a ~55 % duty cycle. **Use SF7 (5.47 kbps, 146 ms of air time per packet) with a 1 Hz rate** — that is 15 % duty, comfortable, and still gives you 46 dB of margin.

> ⚠️ **Duty cycle is also a legal matter.** The 865–867 MHz exemption in India permits **1 W EIRP** but is intended for low-duty-cycle use. At 1 Hz with 146 ms packets you are at 15 % duty, which is high for a shared band. **Say this in the CDR and have a plan to reduce the rate (0.5 Hz) if interference is observed.**

### 2.5 The numbers to memorise

| Fact | Value |
|---|---|
| FSPL doubles (+6 dB) for every doubling of range | +6 dB per 2× |
| FSPL doubles (+6 dB) for every doubling of frequency | +6 dB per 2× |
| 2.4 GHz, 1 km | **100.2 dB** |
| 2.4 GHz, 2 km | **106.2 dB** |
| 866 MHz, 1 km | **91.2 dB** |
| 866 MHz, 2 km | **97.2 dB** |
| 433 MHz, 1 km | **85.2 dB** |
| **To double your range, you need +6 dB** — which is 4× the power, or 4× the antenna gain, or 2× the antenna gain at each end | |
| **Every 6 dB of margin is worth 2× range** | |

### 2.6 Why you need margin above and beyond the budgeted number

| Effect | Typical loss | Mitigation |
|---|---|---|
| **Cross-polarisation during roll** | up to −20 to −30 dB at the fade instant | Circularly polarised ground antenna (a patch with a 90° hybrid), or accept packet loss and rely on SD logging |
| **Rocket body blockage** | −6 to −15 dB when the motor casing is between the antenna and the ground | Put the antenna in the **fin can or the nose shoulder**, not behind the motor |
| **Ground multipath (two-ray)** | −3 to −10 dB, fading with height | Elevate the ground antenna (see §3); a mast at 3 m over flat ground moves the first Fresnel zone |
| **Rain / humidity** | −0.5 dB at 2.4 GHz over 2 km (negligible); −0.1 dB at 866 MHz | Not a concern at these ranges |
| **Body / hand loss near the ground antenna** | −3 to −10 dB if the operator stands next to the antenna | 🔎 **Never stand in front of the ground antenna.** This is the most common self-inflicted 6 dB loss. |
| **Detuning inside the airframe** | −2 to −6 dB | Tune the antenna with the airframe assembled, or use an external blade antenna |
| **Antenna pointing error (patch/Yagi)** | −3 dB at half the beamwidth | A patch is ~65° at 2.4 GHz; a Yagi is ~30°. **Aim it.** |

### 2.7 Typical RSSI values you should see (rough guide, 2.4 GHz XBee-PRO)

| Situation | RSSI (dBm) |
|---|---|
| Bench, 1 m apart | −30 to −40 |
| 100 m, clear line of sight | −55 to −65 |
| 500 m, clear LOS | −70 to −80 |
| 1 km, clear LOS | −78 to −88 |
| 2 km, clear LOS | −85 to −95 |
| **2 km, person standing in front of the antenna** | −95 to −105 |
| Link failure | < −100 |

⚠️ **Treat any RSSI worse than −92 dBm at 1 km as a fault to investigate**, not as normal.

---

## 3. Antenna selection and placement

### 3.1 The competition geometry

```
                        ▲  apogee ~1000 m AGL
                       ╱ ╲
                      ╱   ╲        Slant range at apogee: √(1000² + 1000²) ≈ 1414 m
                     ╱     ╲       (if the pad is 1 km from the gallery)
                    ╱       ╲
                   ╱         ╲     ← the WORST case is not apogee, it is
                  ╱           ╲      apogee WHILE HORIZONTALLY DISPLACED,
                 ╱             ╲     and then the descent drift.
                ╱               ╲
               ╱                 ╲   Design point: 2000 m, not 1000 m.
              ╱                   ╲
             ╱                     ╲
            ╱                       ╲
           ╱                         ╲
          ╱                           ╲
    ▲    ╱                             ╲
    │   ╱      ← pad, ~1 km →  ← viewing gallery
    │  ╱                        ┌──────────────┐
    │ ╱                         │ GROUND       │
    │╱                          │ STATION      │
    └───────────────────────────┴──────────────┘
       ground antenna at 3 m AGL on a mast
```

**Two ranges to budget for:**

| Range | Value | Why |
|---|---|---|
| **Design range (what you must guarantee)** | **2.0 km** | Pad-to-gallery 1 km, plus apogee 1 km, plus 20 % for descent drift and for the antenna not being at the geometric ideal |
| **Stretch goal (what you should test)** | **3.0 km** | The rules may place the gallery further than 1 km, and you want margin |

⚠️ **Do not design to 1 km.** If you design to 1 km and the actual geometry gives 1.4 km, you have 3 dB less margin than you think, and that is the difference between telemetry and no telemetry.

### 3.2 Rocket-side antenna

| Option | Gain | Cost (INR) | Notes |
|---|---|---|---|
| **¼-wave wire whip, soldered to the XBee RPSMA centre pin** ⭐ | 2.1 dBi | ₹30 | ✅ **Best choice.** Cut for the frequency: **λ/4 = 31.2 mm at 2.4 GHz** (with a 0.95 velocity factor for a bare wire: **29.7 mm**), **86.6 mm at 866 MHz** (82 mm with VF). Straighten it along the body axis, keep it ≥ 10 mm from any metal, and **do not coil it**. |
| **Sleeve dipole (wire + a λ/4 sleeve)** | 2.1 dBi | ₹50 | ✅ Better than a plain whip because it does not need a ground plane. **Recommended for the rocket** — an airframe is a poor ground plane at 2.4 GHz. |
| **Rubber duck, 2 dBi, SMA** | 2 dBi | ₹150–400 | ⚠️ Heavier, and the joint is a vibration failure point |
| **2.4 GHz chip antenna** | 0–1 dBi | ₹100–250 | ⚠️ Convenient but needs a matched ground plane on the PCB; you will get 0 dBi effective |
| **Blade antenna through the airframe wall** | 2 dBi | ₹600–1,500 | ✅ The mechanically correct answer if budget allows. Requires a bulkhead SMA feedthrough (₹350–800) |
| **Patch on the airframe** | 6–8 dBi | ₹400–900 | ❌ **Directional — it will point at the ground for only part of the flight and at the sky for the rest.** Do not put a directional antenna on a tumbling rocket. |

**Rocket antenna rules:**

1. **Polarisation must match the ground antenna.** Vertical rocket whips + a vertically polarised ground antenna. During roll this changes constantly (see §2.6) — that is why the link budget must carry a polarisation allowance.
2. **Place it as far as possible from the motor casing and the deployment hardware**, ideally in the **nose shoulder or the fin can**, with the ground plane (the airframe) behind it.
3. **Do not run the antenna inside a carbon-fibre airframe.** ⚠️ **Carbon fibre is conductive and acts as a Faraday cage.** If your airframe is CF, the antenna **must** be external. If it is fibreglass or cardboard, an internal wire is fine but will detune.
4. **Measure the VSWR with the airframe assembled.** A NanoVNA-H4 (₹4,000–6,000) is the single best ₹5,000 the club can spend on RF; it turns "I hope the antenna works" into a measurement. Sweep 2.35–2.50 GHz and confirm the dip is at 2.45 GHz and below 2:1 VSWR.
5. **Strain-relieve the antenna.** A whip that whips is a whip that cracks its solder joint.

### 3.3 Ground station antenna

| Option | Gain | Beamwidth | Cost (INR) | Verdict |
|---|---|---|---|---|
| **¼-wave ground plane (4 radials)** | 2.1 dBi | 360° | ₹100 (home-made) | ✅ Baseline. Better than a rubber duck because it has a proper ground plane. |
| **2.4 GHz 8 dBi patch (e.g. TP-Link TL-ANT2408CL)** ⭐ | 8 dBi | ~65° H / 65° V | ₹600–1,200 | ✅ **RECOMMENDED primary.** The beamwidth is wide enough that you do not need to track the rocket, and 8 dBi is 6 dB better than a dipole. |
| **2.4 GHz 15 dBi Yagi or grid** | 12–15 dBi | ~30° | ₹1,200–3,000 | ✅ Best margin, ⚠️ **you must aim it**. Pair it with a camera-tripod pan head and a spotter whose only job is to keep it on the rocket. |
| **2.4 GHz 9 dBi omni (fibreglass, 1 m)** | 9 dBi | 360° H, ~12° V | ₹900–1,800 | ✅ Good if you cannot track. The narrow vertical beamwidth means it must be **vertical**, and it will lose the rocket when it is high overhead. |
| **866 MHz 5 dBi omni (LoRa backup)** | 5 dBi | 360° | ₹600–1,200 | ✅ For the backup link. |
| **Helical / circularly polarised patch** | 8 dBi | 60° | ₹2,500–5,000 | ✅ **The technically correct answer** for a rolling rocket — circular polarisation removes the cross-polarisation fade entirely. If the budget allows one upgrade, this is it. |
| **Hand-held rubber duck** | 2 dBi | — | ₹150 | ⚠️ Only acceptable as a **backup** antenna, and only if held at arm's length above head height, away from the body. |

### 3.4 ⚠️ Why the ground station antenna MUST be elevated

This is not a nicety. It is the difference between a working link and a failing one.

| Effect | Mechanism | Loss at 1 km, 2.4 GHz |
|---|---|---|
| **First Fresnel zone obstruction** | The first Fresnel zone radius at 1 km is `r = 17.32 × √(d_km / (4·f_GHz))` = `17.32 × √(1.0/(4×2.45))` = **5.5 m**. If the ground (or a person, or a vehicle) intrudes into 60 % of that radius (3.3 m), you lose significant signal. **At 1 km a ground-level antenna cannot clear this.** | −6 to −20 dB |
| **Two-ray ground reflection** | A direct ray and a ground-reflected ray arrive out of phase. At low antenna heights the reflected ray is nearly equal in amplitude and opposite in phase → **deep nulls**. | −6 to −15 dB, fading with distance |
| **Body loss and ground clutter** | The operator, the laptop, the table, the vehicle — all near-field absorbers | −3 to −10 dB |
| **Ground-level noise** | 2.4 GHz is the most crowded band on earth: WiFi, Bluetooth, microwave ovens, drones, and every other student team's radio | Raises the noise floor by 3–10 dB |

**The arithmetic of the fix:**

```
  Ground antenna at 1 m AGL, distance 1 km:
     Fresnel radius needed = 5.5 m.  Available = 1 m.  → 82 % obstruction → BAD.

  Ground antenna at 3 m AGL, distance 1 km:
     Required clearance is the 60 % zone = 3.3 m.  Available = 3 m (marginal) → OK
     📈 Gain versus 1 m height:   +8 to +14 dB measured in the field

  Ground antenna at 5 m AGL, distance 1 km:
     Clear.  +10 to +16 dB versus 1 m.
```

> ### ✅ Design action: **a 3–5 m mast is worth more than any antenna upgrade.**
> An aluminium telescopic mast (5 m, ₹2,500–5,000 from a photography/lighting supplier or a **Decathlon / survey tripod**), or a **fibreglass telescopic pole** (₹1,500–3,000) plus a tripod, plus **5 m of low-loss coax or, better, the radio mounted at the top with a USB extension**. **Budget ₹4,000–8,000 for the mast.** It is the highest-value item in the ground station and it is the one teams forget.

**Rule:** *"If the ground antenna is at head height, you have already lost 10 dB."*

---

## 4. Frequency planning and interference mitigation

### 4.1 Why the rocket and payload must be on SEPARATE channels

The rule requires separate channels for the rocket and the CAN-7USAT payload. There are four independent reasons, and you should be able to give all four:

1. **Co-channel interference destroys both links.** Two 802.15.4 transmitters on the same channel within 1 km of each other and 1 km from the receiver will collide on nearly every packet. 802.15.4 does carrier sense, but with both nodes moving and one at 1 km, hidden-node conditions make CSMA ineffective.
2. **The payload has its own telemetry requirement.** The CAN-7USAT mission requirements have their own data needs. On a shared channel you would have to time-multiplex, halving both rates and adding a synchronisation failure mode.
3. **Fault isolation.** If the payload radio fails and starts transmitting garbage or jamming continuously, a separate channel means your flight-computer link is unaffected. On a shared channel, one failed payload takes down the whole mission.
4. **Diagnosis.** With two channels you can watch both links independently and tell *which* subsystem is failing. That is worth its weight during the pad wait.

### 4.2 802.15.4 channel plan (2.4 GHz XBee)

802.15.4 at 2.4 GHz defines 16 channels, each 2 MHz wide, spaced 5 MHz apart:

```
  Channel:   11    12    13    14    15    16    17    18    19    20    21    22    23    24    25    26
  Centre:  2405  2410  2415  2420  2425  2430  2435  2440  2445  2450  2455  2460  2465  2470  2475  2480  MHz
             │                                   │                                   │
             │                                   │                                   │
         WiFi ch.1 (2412)                  WiFi ch.6 (2437)                    WiFi ch.11 (2462)
         overlaps 11–14                     overlaps 16–19                      overlaps 21–24
```

> ⚠️ **The 2.4 GHz band is 80 MHz wide and WiFi channels 1, 6 and 11 occupy nearly all of it.** In a city or a competition venue with WiFi, you have very little clean spectrum. This is the strongest technical argument for the 865–867 MHz LoRa backup.

**Recommended channel plan:**

| Link | 802.15.4 channel | Centre freq | Rationale |
|---|---|---|---|
| **Rocket flight computer** | **Ch 26** (`SC=1A` hex in XBee) | 2480 MHz | Farthest from WiFi ch 1/6/11 centres; 18 MHz from the nearest (ch 11 at 2462) |
| **CAN-7USAT payload** | **Ch 20** (`SC=14` hex) | 2450 MHz | ⚠️ Directly on WiFi ch 11's centre — **not ideal, but it is 30 MHz from the rocket link, which is 6 channel-widths.** If the site is WiFi-quiet, this is fine. If not, use **Ch 25 (2475 MHz)** and accept that it is only 5 MHz (1 channel) from the rocket — then rely on the ~1 km spatial separation and the payload's own low duty cycle. |
| **Ground station ↔ laptop** | USB serial | — | Wired. **Never** use a WiFi or Bluetooth link for the ground station's command path. |
| **LoRa backup (866 MHz)** | 865.1 / 866.5 / 867.5 MHz | — | Pick **866.5 MHz** — the band centre, farthest from the band edges |

> 💡 **Verify your channel choice on site.** Before the launch window, run an **energy scan**. XBee does this with the `ED` command (returns energy on all 16 channels); a NanoVNA or an RTL-SDR (₹1,200–2,500) with SDR# will show you a spectrum. **Pick the quietest channel above 2470 MHz and declare it at the CDR.** "We surveyed the site and chose Ch 26" is a much better CDR answer than "we picked Ch 26 because it was in a tutorial."

### 4.3 NETID / PANID set to the team number

**The rule:** NETID/PANID must be set to the team number and declared at the CDR.

802.15.4 uses a 16-bit PAN ID, `0x0000`–`0xFFFF`, with `0xFFFF` meaning "broadcast/match any". **This is your network separation mechanism.** Without it, every team at the launch site on the same channel joins (or interferes with) every other team's network.

| XBee parameter | Meaning | Setting |
|---|---|---|
| `ID` | **PAN ID** — the network identifier | **Team number.** If your team number is 07, set `ID = 0007`. If it is 21, set `ID = 0021` (hex `0x0021` = decimal 33 — ⚠️ **decide and document whether your team number is being interpreted as decimal or hex, and use the same value everywhere.**) |
| `SC` | Scan channels (bitmask) | `1A` for channel 26 only; `FFFF` for all |
| `MY` | 16-bit source address | Rocket: `1`; Ground: `2` |
| `DL` | Destination address low | Rocket: `2`; Ground: `1` |
| `DH` | Destination address high | `0` (use 16-bit addressing) |
| `CE` | Coordinator enable | `0` (no coordinator in 802.15.4 point-to-point) |
| `A1`/`A2` | End-device / coordinator association | `0` (no association — this is what makes Series 1 fast) |
| `BD` | Baud rate | `6` = 57600, or `7` = 115200 |
| `PL` | TX power level | `4` = 18 dBm (max) or `2` = 10 dBm for the compliance-limited option (§2.3) |
| `RR` | Retries | `6` (maximum) — **your link-margin-in-a-parameter** |
| `RR`+`RN` | Retries and random delay | Enable random delay (`RN=1`) to avoid two nodes colliding repeatedly |
| `NI` | Node identifier (ASCII) | `UVCERC-FC` (flight computer), `UVCERC-GS` (ground station) |
| `AP` | API enable | `0` transparent for the simple case; `2` for API mode with frame-level acknowledgements (see §7) |

**Verification — do this and screenshot it:**

```
  +++                              (enter command mode: no CR, 1 s guard before/after)
  OK
  ATID                             (read PAN ID)
  7                                ← must equal your team number
  ATSC
  1A                               ← channel 26 only
  ATWR                             (write to non-volatile memory)
  ATFR                             (software reset — the settings take effect)
  ATCN                             (exit command mode)
```

⚠️ **`ATWR` is not optional.** Without it, the settings are lost on the next power cycle and you will discover this on the pad.

### 4.4 Interference test — the procedure the Jury will ask about

**Purpose:** demonstrate that your link survives in the presence of the payload link, other teams, WiFi, and the ground station's own laptop.

| # | Test | Setup | Pass criterion |
|---|---|---|---|
| **INT-1** | **Baseline** | Rocket transmitter on the bench at 1 m from the ground receiver, no other RF. Log 300 packets. | **0 dropped packets**; RSSI −35 ± 6 dBm |
| **INT-2** | **Payload coexistence** | Both the rocket link (Ch 26) and the payload link (Ch 20) transmitting at 1 Hz from 1 m apart, ground receiver on Ch 26. Log 300 packets each. | Rocket **≤ 1 dropped packet**; payload ≤ 1. RSSI within 3 dB of baseline |
| **INT-3** | **WiFi stress** | A laptop running a 2.4 GHz hotspot on ch 1, 6, and 11 in turn, 2 m from the receiver, saturating with an iperf/`speedtest` download. Ground receiver on Ch 26. | Rocket **≤ 2 dropped packets in 300**; RSSI degradation ≤ 6 dB |
| **INT-4** | **Other-team simulation** | A second XBee pair on the **same channel (Ch 26)** but a **different PAN ID**, transmitting at 1 Hz, 1 m from the receiver. | Rocket link unaffected (**≤ 1 dropped packet in 300**) — **this proves the PAN ID separation works.** ⚠️ If this fails, your PAN ID is wrong. |
| **INT-5** | **Adjacent-channel test** | A second XBee on **Ch 25** transmitting continuously at max power. | ≤ 1 dropped packet in 300. Adjacent-channel rejection should be ≥ 20 dB. |
| **INT-6** | **Co-channel hostile (informational)** | A second XBee on **Ch 26 with the same PAN ID**, transmitting at 1 Hz. | **Expect heavy loss.** This is the documented consequence of a PAN ID collision, and it is *why* INT-4 matters. Record the result as evidence that the PAN ID is doing real work. |
| **INT-7** | **Metal-body test** | Place the rocket transmitter inside the **actual airframe** with the motor casing installed, at 1 m from the receiver. | RSSI degradation ≤ 10 dB versus baseline. **This is the test that catches a detuned antenna or a carbon-fibre Faraday cage.** |
| **INT-8** | **LoRa coexistence** | The 866 MHz LoRa backup transmitting at 1 Hz alongside the 2.4 GHz link. | Neither link degrades (they are 1.5 GHz apart). |

**Log format for these tests** (append to `RF_Test_Log.csv`):

```
test_id,timestamp,range_m,tx_chan,tx_panid,pkts_sent,pkts_recv,loss_pct,rssi_min,rssi_mean,rssi_max,notes
INT-2,2027-03-14T10:22:11,1,26,0x0007,300,300,0.0,-41,-36.2,-31,"payload ch20 active 1Hz"
```

> 💡 **Run INT-2 and INT-4 at the actual competition site.** Interference is a site property. A result from the UVCE campus is worth something; a result from the launch site is worth everything.

### 4.5 Interference mitigation checklist

- [ ] **Separate channels** for rocket and payload, ≥ 6 channel-widths (30 MHz) apart if possible
- [ ] **PAN ID = team number**, and *different* from any other team's, declared at the CDR
- [ ] **Channel chosen from an on-site energy scan**, not from a default
- [ ] **Antennas ≥ 0.5 m apart** on the vehicle, ideally on opposite ends, and never parallel and 2 cm apart
- [ ] **Ground antenna on a 3–5 m mast**, clear of the operator and the laptop
- [ ] **No WiFi or Bluetooth in the ground station's data path** — wired USB only
- [ ] **Radio and servo power rails separate** (§5 of the Flight Computer document) — servo PWM harmonics at 50 Hz and its own switching noise can modulate the radio supply. This is a *conducted* interference path, and it is more common than radiated interference
- [ ] **Laptop's WiFi disabled** during launch operations
- [ ] **Phone hotspots off.** Every team member, every phone. Say it out loud in the briefing
- [ ] **`RR=6` retries enabled** — retries are free link margin
- [ ] **Log RSSI on every packet** so an interference event leaves evidence

---

## 5. Remote telemetry enable/disable by RF command (required by the rules)

**The rule:** an RF command must switch telemetry ON/OFF, and **the rocket must not transmit until commanded.**

### 5.1 Why this rule exists

It is a **safety and spectrum-management** requirement. A rocket on the pad, transmitting before it is commanded to, is radiating in a shared band while other teams are trying to arm; and a rocket transmitting on the pad while the Jury is inspecting it is a hazard. The rule forces you to demonstrate positive control of your emissions.

### 5.2 Architecture — two independent layers

Do **not** implement this as "a software flag that stops calling `printf`". That leaves the transmitter powered and radiating. Implement **both** layers:

```
  ┌────────────────────────────────────────────────────────────────────┐
  │ LAYER 1 — HARDWARE GATING (the real switch)                        │
  │                                                                    │
  │   STM32 PA8 ──▶ [gate driver / MOSFET AO3401] ──▶ 3V3_RADIO rail    │
  │                                                                    │
  │   OFF: PA8 low  → the XBee has NO POWER. It cannot transmit,       │
  │                    not even a beacon. Current draw: 0 µA.          │
  │   ON:  PA8 high → the XBee boots (50 ms) and transmits.            │
  │                                                                    │
  │   ⚠️ Default state at power-on MUST be OFF.  Use a pull-DOWN on    │
  │      PA8 and a P-FET whose gate is pulled to VBAT through 100 kΩ,  │
  │      so a floating MCU pin means "radio off".                      │
  └────────────────────────────────────────────────────────────────────┘

  ┌────────────────────────────────────────────────────────────────────┐
  │ LAYER 2 — SOFTWARE GATING (the polite switch)                      │
  │                                                                    │
  │   Even with the radio powered, the firmware only calls the         │
  │   telemetry task when g_telem_enabled == true. This lets you       │
  │   power the radio for the RF link test but keep the channel        │
  │   quiet until commanded.                                           │
  └────────────────────────────────────────────────────────────────────┘
```

**Why both?** Layer 1 proves the radio is genuinely off (you can demonstrate it with a spectrum analyser or an SDR, which is a *dramatic* thing to show the Jury). Layer 2 lets you keep the receiver alive to receive the ON command — which the hardware gate cannot do, because a powered-off radio cannot receive.

> ⚠️ **This is the subtle problem with hardware gating:** if the radio is off, how does it hear the ON command? **Answer: you need a receive path that is always on, or a wake mechanism.** Three options:

| Option | How | Trade-off |
|---|---|---|
| **A. Keep the radio powered but the transmitter disabled** | Use `ATPL=0` (0 dBm) or put the XBee in a receive-only configuration while the MCU is in state 0/1. The receiver is alive; the transmitter is at minimum power. | ✅ Simplest. ⚠️ The radio is not fully off, so you cannot claim "zero emissions". |
| **B. Duty-cycled receiver** | Power the radio for 200 ms every 2 s (a 10 % duty "sniff" window). Any received ON command is caught within 2 s. | ✅ Genuinely near-zero average emission. ⚠️ Adds 2 s of command latency. |
| **C. Separate always-on receiver** | A second, tiny receiver (e.g. an NRF24L01 at 0 dBm, or a 433 MHz OOK receiver module at ₹80) that is always listening and wakes the main radio via an interrupt. | ✅ Cleanest architecturally. ⚠️ Extra hardware and another failure mode. |

> ### ✅ Recommended: **Option B (duty-cycled receiver) + Layer 1 hardware gate.**
> Average radio-on time before the ON command is 10 %, average current draw drops to ~5 mA, and the average radiated power is 10 % of full. The 2 s command latency is irrelevant on a pad where you wait 30 minutes. **Document the timing in the CDR so the Jury knows the 2 s is a designed property, not a bug.**

### 5.3 The command set

| Command | ASCII | Response | Effect |
|---|---|---|---|
| **Telemetry ON** | `TELEM:ON` | `ACK:TELEM:ON` | Layer 1 gate closes, Layer 2 flag set. Telemetry starts at 1 Hz. **Also allowed to start the mission clock if not already running.** |
| **Telemetry OFF** | `TELEM:OFF` | `ACK:TELEM:OFF` | Layer 2 flag cleared immediately; Layer 1 gate opens after a 500 ms flush delay |
| **Zero barometer & accelerometer** | `ZERO` | `ACK:ZERO:<pad_Pa>:<h_m>` | ⭐ **Required by the rules.** Sets the pad pressure and the gravity vector. Only accepted in state 2 |
| **State query** | `STATUS?` | `STATUS:<state>,<vbat>,<rssi>` | Returns a single packet even if telemetry is off |
| **Arm deployment** | `ARM:<code>` | `ACK:ARM` | Enables the deployment gate. **Requires a 4-digit code stored in FRAM** so a stray byte cannot arm the vehicle |
| **Disarm** | `DISARM` | `ACK:DISARM` | Immediately disables the deployment gate |
| **Test mode** | `TEST` | `ACK:TEST` | Enters state 1 (bench servo cycling) |
| **Pad mode** | `PAD` | `ACK:PAD` | Enters state 2 (armed, waiting) |
| **Beacon** | `BEEP` | `ACK:BEEP` | Pulses the buzzer so you can find the rocket |
| **Reset packet count** | `CLRCNT` | `ACK:CLRCNT` | Resets `<PACKET COUNT>` to 1 (for a clean demo run) |

**Command framing rules:**

1. Commands are **ASCII, `<COMMAND><CR>`**, uppercase, no embedded spaces.
2. **Every command gets an ACK or a NAK.** A command with no response is treated as lost; the ground station retries up to 3 times at 1 s intervals.
3. **`ARM` requires a code.** 4 digits, in FRAM, not in the source code and not in the Git repository. This prevents an accidental arm from a garbled byte or from another team's transmitter on the same PAN ID.
4. **The default state after any reset is telemetry OFF and disarmed.** ⚠️ A reset must never leave the vehicle transmitting or armed. This is an inversion of the usual "fail safe" instinct and it is the right choice here, because the rules say the rocket must not transmit until commanded.
5. **`ZERO` is only accepted in state 2 and only when the vehicle is confirmed static.**

### 5.4 Demonstration procedure for the Jury

| Step | Action | What the Jury sees |
|---|---|---|
| 1 | Power the vehicle on the pad. | **No RF.** Spectrum analyser / SDR shows a clean channel. Vehicle LED = white (BOOT), then blue (TEST_MODE). |
| 2 | Show the SDR waterfall. | A flat noise floor. **"The rocket is not transmitting."** |
| 3 | Type `TELEM:ON`. | Within 2 s, the waterfall shows a 2.4 GHz burst every second. LED goes green. Ground station starts plotting. |
| 4 | Typ`TELEM:OFF`. | Within 500 ms, the waterfall goes flat. LED returns to blue. |
| 5 | `TELEM:ON`, then `ZERO`. | Telemetry shows `<ALTITUDE>` = 0.0 m, `<ACCELEROMETER DATA>` = 0.00 m/s² (vertical) after gravity removal. |
| 6 | `STATUS?` | A single packet with the state and the battery voltage. |

> 💡 **Carry an RTL-SDR (₹1,200–2,500) to the launch.** Being able to *show* the Jury a spectrum waterfall proving your transmitter is off is worth more than a paragraph of text in the CDR, and it takes ten seconds.

---

## 6. Ground station hardware

### 6.1 Bill of materials

| Item | Specification | Qty | Unit (INR) | Total (INR) | Notes |
|---|---|---|---|---|---|
| **Laptop** | ≥ 4 GB RAM, ≥ 2 USB-A ports (or a USB hub), **≥ 2 h of battery** at full load | 1 | Owned | ₹0 | ⚠️ **The rule is a ≥ 2 h battery.** Measure it: run the ground station software for 2 h on battery with the screen at 70 % and confirm it does not sleep. Put the measurement in the CDR. |
| **XBee-PRO S1, RPSMA** | `XBP24-AWI-001`, 2.4 GHz, 18 dBm | 1 | ₹2,600 | ₹2,600 | Ground side. **The RPSMA (external antenna) version, not the chip-antenna version.** |
| **XBee USB adapter board** | FT231X-based, with a reset button and RSSI LED | 1 | ₹700 | ₹700 | ⚠️ Cheap CH340-based adapters exist at ₹250 and mostly work — but the FTDI one has never failed us. |
| **2.4 GHz 8 dBi patch antenna** | RP-SMA, with a magnetic/tripod mount | 1 | ₹900 | ₹900 | |
| **Antenna mast** | Telescopic, 3–5 m, with a tripod base | 1 | ₹3,500 | ₹3,500 | ⭐ **Highest-value item in the ground station.** See §3.4. |
| **Low-loss coax** | **Radio mounted at the antenna.** Use 0.5 m of RG-316 or LMR-100; if you must run longer, use LMR-400 | 1 | ₹400 | ₹400 | ⚠️ RG-58 at 2.4 GHz loses 0.6–0.9 dB/m. **5 m of RG-58 costs you 4 dB.** |
| **USB active extension** | 5 m, to reach the mast-mounted radio | 1 | ₹500 | ₹500 | ✅ **This replaces the long coax run. This is the correct engineering choice.** |
| **LoRa backup link** | 2 × RFM95W + 2 × ESP32 or an STM32 + 2 × 866 MHz antennas | 1 set | ₹2,200 | ₹2,200 | Optional but recommended (§1.2) |
| **RTL-SDR dongle** | RTL2832U + R820T2, with an antenna | 1 | ₹1,600 | ₹1,600 | For the interference survey and the "prove it's off" demo |
| **NanoVNA-H4** | 4", 50 kHz–1.5 GHz (or -F V3 for 4 GHz) | 1 | ₹4,500 | ₹4,500 | ⭐ **Club-level purchase.** Antenna VSWR, cable loss, filter response, and it will be used for years |
| **USB power bank** | 20,000 mAh, 5 V/3 A + 9 V/2 A USB-PD | 1 | ₹1,800 | ₹1,800 | ✅ **Power the radio and the mast electronics from this, not from the laptop.** Protects the laptop's 2 h battery and isolates the RF ground |
| **USB hub, powered** | 4-port, 5 V/2 A | 1 | ₹700 | ₹700 | |
| **Field notebook + pen** | Waterproof | 1 | ₹150 | ₹150 | ⚠️ **A paper log of the launch timeline is required and it does not crash.** |
| **Stopwatch** | Dedicated, or a phone in aeroplane mode | 1 | ₹300 | ₹300 | For the T+0 call |
| **Cable ties, tape, spare fuses, spare SD card** | — | — | ₹600 | ₹600 | |
| **Ground station case** | Pelican-style or a padded tool case | 1 | ₹2,500 | ₹2,500 | Everything in one box, ready to go |
| | | | **TOTAL** | **₹26,950** | Excluding the laptop |

> 💡 **The "everything in one case" rule.** The ground station must be **assemblable in under 5 minutes by one person in the dark**. Cable-tie the USB extension to the mast. Label every connector. Keep a laminated one-page setup card in the lid. This is the difference between a calm launch and a missed window.

### 6.2 Ground station layout

```
                              ┌─────────────────────────────┐
                              │   2.4 GHz 8 dBi PATCH       │  ← aimed at the pad
                              │   (on a tripod pan head)    │
                              └──────────────┬──────────────┘
                                             │ 0.5 m RG-316
                              ┌──────────────▼──────────────┐
                              │  XBee-PRO S1 (RPSMA)        │  ← ON THE MAST, at
                              │  + USB adapter board        │     the antenna
                              └──────────────┬──────────────┘
                                             │ 5 m ACTIVE USB EXTENSION
                                             │ (this replaces long coax)
                              ┌──────────────▼──────────────┐
                              │  POWERED USB HUB            │
                              └───┬─────────────────────┬───┘
                                  │                     │
                     ┌────────────▼──────┐   ┌──────────▼──────────┐
                     │ LAPTOP            │   │ USB POWER BANK      │
                     │ • ground station  │   │ 20,000 mAh          │
                     │   software        │   │ powers the radio +  │
                     │ • CSV logging     │   │ the SDR             │
                     │ • plots           │   └─────────────────────┘
                     └───────────────────┘
                                  │
                     ┌────────────▼──────┐
                     │ RTL-SDR (survey  │
                     │ + "prove off")   │
                     └───────────────────┘

  ⚠️ OPERATOR STANDS BEHIND AND BESIDE THE MAST, NEVER IN FRONT OF IT.
     A person between the antenna and the rocket costs 3–10 dB.
```

---

## 7. Ground station software

### 7.1 Requirements

| ID | Requirement | Source |
|---|---|---|
| GS-REQ-01 | Receive, parse and validate telemetry at **≥ 1 Hz** with **no dropped packets at 1 Hz sustained for 60 min** | Derived |
| GS-REQ-02 | **Near-real-time plotting of EVERY telemetry field**, in **SI units** | Rule, Ch. 5 |
| GS-REQ-03 | Generate a CSV file named exactly **`Flight_<TEAM_ID>.csv`** | Rule, Annexure-2 |
| GS-REQ-04 | Produce the CSV **immediately after launch operations**, on a USB stick | Rule |
| GS-REQ-05 | Decode and send **RF commands** (`TELEM:ON/OFF`, `ZERO`, `ARM`, …) | Rule, Ch. 5 |
| GS-REQ-06 | Display **RSSI, packet loss %, and link margin** live | Derived |
| GS-REQ-07 | Display the **flight software state** and a **mission clock** live | Rule |
| GS-REQ-08 | Run for **≥ 2 h** on the laptop battery | Rule |
| GS-REQ-09 | Survive a laptop sleep / screen lock without losing the log | Derived |
| GS-REQ-10 | Display a **pad-wait countdown** that forces a decision at T+40 min | Derived (§5.6 of the Flight Computer doc) |

### 7.2 Technology choice — be pragmatic

| Option | Language | Time to working | Portability | Verdict |
|---|---|---|---|---|
| **Python + pyserial + matplotlib + Tkinter/PyQt** ⭐ | Python 3 | 1–2 weeks | ✅ Windows/Linux/macOS, no install for the team if you freeze it | ✅ **RECOMMENDED.** The team can read and modify it. `pyserial` for the link, `matplotlib` for the plots, `csv` for the log, `tkinter` for the UI (no extra dependency). |
| **Python + Streamlit dashboard** | Python 3 | 3–5 days | ⚠️ Needs a browser and a local server | ✅ Fastest to a good-looking demo. ⚠️ Streamlit's rerun model fights 1 Hz real-time updates; you need `st.empty()` and manual polling. Acceptable. |
| **Processing / p5.js** | Java/JS | 1 week | ✅ | ✅ Great for beautiful plots. ⚠️ Serial handling is weaker. |
| **C# / WPF** | C# | 3–4 weeks | ❌ Windows only | Only if a team member already knows it. |
| **LabVIEW** | G | 2 weeks | ❌ Licence cost | ❌ Not for a student club. |
| **Custom web app (Node + WebSocket + Chart.js)** | JS | 2 weeks | ✅ Beautiful, and the Jury will be impressed | ✅ Good if you have a web developer. The WebSocket architecture is genuinely the right one for real-time. |

> ⚠️ **Write the ground station to be boring and reliable.** A beautiful dashboard that crashes at T−2 min is worse than a terminal printing CSV. Build the **logging path first**, verify it, then add plots. **The CSV is the deliverable; the plots are the demo.**

### 7.3 Architecture

```
  ┌──────────────┐   115200 8N1      ┌──────────────────────────────────────┐
  │  XBee-PRO    │◀─────────────────▶│  SERIAL READER THREAD                │
  │  (via USB)   │                   │    • reads bytes, appends to a ring   │
  └──────────────┘                   │    • splits on '\r'                   │
                                     │    • pushes complete lines to a Queue │
                                     └───────────────┬──────────────────────┘
                                                     │ queue.Queue (thread-safe)
                                     ┌───────────────▼──────────────────────┐
                                     │  PARSER THREAD                        │
                                     │    1. validate the field count (>=15) │
                                     │    2. validate the CRC (if framed)    │
                                     │    3. coerce each field to a float    │
                                     │    4. convert to SI units             │
                                     │    5. detect packet-count gaps        │
                                     │    6. timestamp with the LOCAL clock  │
                                     │    7. push to: CSV writer, plotter,   │
                                     │                state display          │
                                     └───┬───────────────┬──────────────────┘
                                         │               │
                          ┌──────────────▼──┐   ┌────────▼──────────────┐
                          │ CSV WRITER      │   │ PLOTTER (main thread)  │
                          │ • flush every   │   │ • 6–8 subplots         │
                          │   1 s           │   │ • rolling 120 s window │
                          │ • f.flush() +   │   │ • redraw at 2 Hz,      │
                          │   os.fsync()    │   │   NOT at 1 Hz          │
                          │   every 10 s    │   │ • SI units on every y  │
                          │ • NEVER close   │   │   axis                 │
                          │   until landing │   └───────────────────────┘
                          └─────────────────┘
```

**Critical implementation rules:**

| Rule | Why |
|---|---|
| **Run the serial read on a separate thread with a bounded queue.** | The UI must never block the serial read. A 200 ms UI stall that drops 2 packets is a telemetry gap the Jury will see |
| **`f.flush()` after every line; `os.fsync()` every 10 s.** | A crash, a sleep, or a power loss must not cost you the log |
| **Never `f.close()` until the flight is over and IMPACT is confirmed.** | Closing rewrites the file; a crash mid-close loses everything |
| **Append a **local** timestamp to every row in a *separate* internal file**, not in `Flight_<TEAM_ID>.csv`.** | The required CSV must contain exactly the 15+ fields. Your local timestamp goes in your own `gs_internal_<date>.csv` |
| **Write the CSV to a fixed path, and mirror it to the USB stick at landing.** | Do not write directly to removable media for 30 minutes |
| **Wrap every parse in `try/except` and count errors.** | One malformed packet must not kill the run |
| **Display `packets received`, `packets lost` (from the packet count field) and `loss %`.** | This is the single most important health number on the screen |
| **Disable the laptop's sleep, hibernate, and screen-off timers in software at startup.** | GS-REQ-08/09. `caffeinate` (macOS), `systemd-inhibit` (Linux), `SetThreadExecutionState` (Windows) |

### 7.4 The exact CSV output format

**Filename: `Flight_<TEAM_ID>.csv`** — e.g. `Flight_UVCERC01.csv`.

**Content: the Annexure-2 record, one per line, nothing else.** No header (see §6.3 of the Flight Computer document for the reasoning), `\n` line endings in the *file* (the file is not the RF frame — use `\n` for Excel/LibreOffice compatibility, while the RF packets use `\r`).

```
UVCERC01,1.00,1,0.0,101325,26.1,5.02,071230.00,13.0231,77.5672,519.2,8,-9.79,0.3,2,OK
UVCERC01,2.00,2,-0.1,101326,26.1,5.02,071231.00,13.0231,77.5672,519.1,8,-9.80,0.4,2,OK
UVCERC01,3.00,3,0.1,101324,26.2,5.02,071232.00,13.0231,77.5672,519.3,8,-9.78,0.2,2,OK
```

**Also write a `README.txt` to the same USB stick:**

```
UVCE Rocketry Club — Flight Data
Team ID:      UVCERC01
Flight date:  2027-11-14
Launch time:  07:12:35 UTC (12:42:35 IST)
Apogee:       987.4 m AGL (barometric, primary sensor)
File:         Flight_UVCERC01.csv

Columns (per IN-SPACe Annexure-2):
 1  TEAM ID                   string
 2  TIME STAMPING             s since power-on (mission clock)
 3  PACKET COUNT              integer
 4  ALTITUDE                  m, relative to pad
 5  PRESSURE                  Pa, absolute static
 6  TEMPERATURE               deg C
 7  VOLTAGE                   V, CAN-7USAT bus
 8  GNSS TIME                 UTC hhmmss.ss
 9  GNSS LATITUDE             deg, N positive
10  GNSS LONGITUDE             deg, E positive
11  GNSS ALTITUDE              m above MSL
12  GNSS SATS                  integer

13  ACCELEROMETER DATA         m/s^2, body-vertical axis (gravity removed)
14  GYRO SPIN RATE             deg/s, roll axis
15  FLIGHT SOFTWARE STATE      integer 0-7
16  OPTIONAL DATA              free text

Flight software states:
 0 BOOT, 1 TEST_MODE, 2 LAUNCH_PAD, 3 ASCENT, 4 PAYLOAD_SEP,
 5 DESCENT, 6 AEROBREAK_RELEASE, 7 IMPACT

Contact: <team email>  <team phone>
```

### 7.5 Live plotting — every field, in SI units

The rule says **every telemetry field** must be plotted in near-real time, in SI units. Build **six to eight panels**, not sixteen — the human eye cannot track sixteen.

| Panel | Y axis (SI) | Fields plotted | Scale note |
|---|---|---|---|
| 1 | **Altitude (m)** | `<ALTITUDE>` (barometric), `<GNSS ALTITUDE>` − pad MSL | 0 → 1200 m; two traces so the student can see GNSS lag |
| 2 | **Pressure (Pa)** | `<PRESSURE>` | Inverted axis (pressure falls with altitude) — **label it as inverted** |
| 3 | **Acceleration (m/s²)** | `<ACCELEROMETER DATA>` + the optional 3-axis from `<ANY OPTIONAL DATA>` | −100 → +200 m/s²; draw a dashed line at ±16 g = ±156.9 m/s² |
| 4 | **Velocity (m/s)** | Derived from the fused filter if transmitted; else `d(altitude)/dt` | −80 → +400 m/s |
| 5 | **Attitude rate (deg/s)** | `<GYRO SPIN RATE>` + the 3-axis from optional | ±2000 °/s |
| 6 | **Temperature (°C) and Voltage (V)** | `<TEMP>` on the left axis, `<VOLTAGE>` on the right | Dual axis; label both |
| 7 | **GNSS (count)** | `<GNSS SATS>` | 0 → 16; step plot, not interpolated |
| 8 | **Link and state** | RSSI (dBm), packet loss (%), flight state (0–7) | Text + a coloured state banner |

**SI-unit conversion table — do this at parse time, once, not at plot time:**

| Field | Raw unit as received | SI unit | Conversion |
|---|---|---|---|
| Altitude | m | m | identity (already SI) |
| Pressure | Pa | Pa | identity |
| Temperature | °C | K | `T_K = T_C + 273.15` |
| Voltage | V | V | identity |
| Latitude / Longitude | degrees | degrees | identity (do **not** convert to radians for display) |
| Accelerometer | m/s² | m/s² | identity. ⚠️ If a sensor reports in g, multiply by 9.80665 |
| Gyro | deg/s | rad/s | `ω_rad = ω_deg × π/180` |
| RSSI | dBm | dBm | identity |
| GNSS altitude | m | m | identity |
| Time stamping | s | s | identity |

> ⚠️ **The rules require the CSV in the specified units (m/s², deg/s), and the display in SI units.** Those are two different requirements, and they are both satisfied by storing the CSV exactly as specified and displaying a converted copy. **Do not "fix" the CSV to be in rad/s.** °/s is what the rule says.

### 7.6 Command console

A text box where the operator types a command and sees the ACK, plus quick buttons for the common ones:

```
┌───────────────────────────────────────────────────────────────────┐
│ COMMANDS                                                          │
│  [TELEM:ON]  [TELEM:OFF]  [ZERO]  [STATUS?]  [BEEP]               │
│  Arm code: [____]   [ARM]  [DISARM]                               │
│  [TEST]  [PAD]  [CLRCNT]                                          │
│                                                                   │
│ > TELEM:ON                                                        │
│ < ACK:TELEM:ON             (142 ms)                               │
│ > ZERO                                                            │
│ < ACK:ZERO:101325.3:0.0    (168 ms)                               │
└───────────────────────────────────────────────────────────────────┘
```

**Command safety rules:**

- `ARM` and `DISARM` are **two-step** (press, then confirm) and `ARM` requires the code.
- **Every command is logged with its round-trip time** to `gs_commands_<date>.csv`. This log is CDR evidence.
- **A command with no ACK within 300 ms is retried up to 3 times at 1 s intervals**, then reported as failed and highlighted red.
- **The deployment cannot be armed from the ground station alone** — see the Recovery document's safe/arm architecture. The RF `ARM` command only *enables* the gate; a physical remove-before-flight jumper must also be installed. Two independent actions are required to arm. **This is deliberate.**

---

## 8. Packet framing protocol

### 8.1 The problem with bare CSV over a radio

Raw ASCII CSV over a transparent-mode radio has three failure modes:

| Failure | Consequence |
|---|---|
| **Partial packets** | The receiver starts mid-packet and reads `5.02,071432.00,...` as if it were a valid row |
| **Concatenated packets** | Two packets arrive back-to-back and the parser sees a doubled-length line with two `<TEAM ID>` fields in it |
| **Corrupted bytes** | One bit error turns `13.0231` into `1B.0231` — the parser either crashes or silently logs a wrong latitude |
| **You cannot tell a good packet from a bad one** | Which means you cannot compute a real packet-loss figure |

**Solution: a framed envelope with a length, a sequence number, and a checksum — while keeping the payload in the exact required ASCII CSV form.**

### 8.2 The recommended frame

```
  ┌──────┬──────┬──────┬──────────┬────────────────────────────┬───────┬──────┐
  │ SOF  │ SEQ  │ LEN  │ PAYLOAD  │           CRC16            │  EOF  │      │
  │ 1 B  │ 1 B  │ 1 B  │  N bytes │           2 B              │  1 B  │      │
  │ 0x7E │ 0-255│  N   │ ASCII    │ CCITT-FALSE, over SEQ..PAY │ 0x0D  │      │
  └──────┴──────┴──────┴──────────┴────────────────────────────┴───────┴──────┘
```

| Field | Size | Value | Purpose |
|---|---|---|---|
| **SOF** | 1 byte | `0x7E` (`~`) | Frame start marker. ASCII `~` never appears in the payload, so no escaping is needed |
| **SEQ** | 1 byte | 0–255, wraps | Detects **lost** packets (gaps in the sequence) |
| **LEN** | 1 byte | Length of PAYLOAD | Detects truncated frames |
| **PAYLOAD** | N bytes | **The exact Annexure-2 ASCII CSV record**, without the trailing `\r` | The required data, unchanged |
| **CRC16** | 2 bytes | CCITT-FALSE (`poly 0x1021, init 0xFFFF`), big-endian, computed over `SEQ || LEN || PAYLOAD` | Detects corruption. **This is the field that makes bit errors visible instead of silent** |
| **EOF** | 1 byte | `0x0D` (`\r`) | Frame terminator — **also satisfies the rules' carriage-return requirement** |

> 💡 **Why `~` as SOF?** It is printable, it is not a comma or a digit, it does not appear in any numeric field or in a team ID, and it is visible in a hex/ASCII dump during debugging. **Do not use `0x00` or `0xFF`** — they occur in noise and in radio idle patterns.

> 💡 **Why CCITT-FALSE CRC16?** It is the most widely implemented CRC16 variant in the world; `crcmod`, `binascii.crc_hqx` (with a tweak), and every embedded CRC library has it. It catches all single-bit errors, all double-bit errors, all odd-bit errors, and all bursts up to 16 bits.

### 8.3 Worked example — byte by byte

**Payload (the Annexure-2 record for packet 185):**

```
UVCERC01, 184.62, 185, 412.7, 96542, 24.3, 5.02, 071432.00, 13.0231, 77.5672, 931.4, 9, -9.79, -42.5, 5, OK
```

That is **96 ASCII characters**. So:

| Field | Value | Bytes |
|---|---|---|
| SOF | `0x7E` | 1 |
| SEQ | `185` = `0xB9` | 1 |
| LEN | `96` = `0x60` | 1 |
| PAYLOAD | the 96 ASCII characters above | 96 |
| CRC16 | computed over `0xB9 0x60` + the 96 payload bytes | 2 |
| EOF | `0x0D` | 1 |
| **TOTAL** | | **102 bytes** |

**The complete frame, as it appears on the wire:**

```
Offset  Hex                                              ASCII
------  -----------------------------------------------  ---------------------------------
0x00    7E                                               ~
0x01    B9                                               .
0x02    60                                               `
0x03    55 56 43 45 52 43 30 31                          UVCERC01
0x0B    2C 20                                           , (space)
0x0D    31 38 34 2E 36 32                                184.62
0x14    2C 20                                           , (space)
0x16    31 38 35                                        185
0x19    2C 20                                           , (space)
0x1B    34 31 32 2E 37                                   412.7
0x20    2C 20                                           , (space)
0x22    39 36 35 34 32                                   96542
0x27    2C 20                                           , (space)
0x29    32 34 2E 33                                      24.3
0x2D    2C 20                                           , (space)
0x2F    35 2E 30 32                                      5.02
0x33    2C 20                                           , (space)
0x35    30 37 31 34 33 32 2E 30 30                        071432.00
0x3E    2C 20                                           , (space)
0x40    31 33 2E 30 32 33 31                              13.0231
0x48    2C 20                                           , (space)
0x4A    37 37 2E 35 36 37 32                              77.5672
0x52    2C 20                                           , (space)
0x54    39 33 31 2E 34                                   931.4
0x59    2C 20                                           , (space)
0x5B    39                                              9
0x5C    2C 20                                           , (space)
0x5E    2D 39 2E 37 39                                   -9.79
0x63    2C 20                                           , (space)
0x65    2D 34 32 2E 35                                   -42.5
0x69    2C 20                                           , (space)
0x6B    35                                              5
0x6C    2C 20                                           , (space)
0x6E    4F 4B                                           OK
0x70    <CRC_hi> <CRC_lo>                               (2 bytes, big-endian)
0x72    0D                                              \r
```

**Worked CRC16-CCITT-FALSE computation (do this by hand once — it is worth understanding):**

```
  Initial value:        0xFFFF
  Polynomial:           0x1021  (x^16 + x^12 + x^5 + 1)
  Input bytes:          0xB9, 0x60, then "UVCERC01, 184.62, ..."

  For each byte b:
      crc ^= (uint16_t)b << 8;
      for (i = 0; i < 8; i++) {
          if (crc & 0x8000) crc = (crc << 1) ^ 0x1021;
          else              crc = (crc << 1);
      }

  After processing all bytes:
      CRC16 = 0x9A3C   (illustrative — compute the real value with your
                         own implementation and VERIFY it against a
                         known test vector before flight)

  Known test vector to validate your implementation:
      Input: "123456789"
      CRC16-CCITT-FALSE = 0x29B1
      ⚠️ If your function does not return 0x29B1 for "123456789",
         your CRC is wrong. Fix it before you fly.
```

**C implementation:**

```c
uint16_t crc16_ccitt_false(const uint8_t *data, size_t len)
{
    uint16_t crc = 0xFFFF;
    for (size_t i = 0; i < len; i++) {
        crc ^= (uint16_t)data[i] << 8;
        for (uint8_t bit = 0; bit < 8; bit++) {
            if (crc & 0x8000) crc = (uint16_t)((crc << 1) ^ 0x1021);
            else              crc = (uint16_t)(crc << 1);
        }
    }
    return crc;
}

void send_telemetry_frame(const char *payload)
{
    uint8_t len = (uint8_t)strlen(payload);
    static uint8_t seq = 0;

    uint8_t hdr[2] = { seq, len };
    uint16_t crc = crc16_ccitt_false(hdr, 2);
    crc = crc16_ccitt_false_continue(crc, (const uint8_t *)payload, len);

    uart_putc(0x7E);            /* SOF                    */
    uart_putc(seq);             /* SEQ                    */
    uart_putc(len);             /* LEN                    */
    uart_write((const uint8_t *)payload, len);
    uart_putc((uint8_t)(crc >> 8));    /* CRC high        */
    uart_putc((uint8_t)(crc & 0xFF));  /* CRC low         */
    uart_putc(0x0D);            /* EOF (also the required <CR>) */

    seq++;                      /* wraps at 256 naturally */
}
```

**Python parser:**

```python
import serial, csv, time
from binascii import crc_hqx   # NOTE: use a proper CCITT-FALSE implementation

SOF, EOF = 0x7E, 0x0D

def crc16_ccitt_false(data: bytes) -> int:
    crc = 0xFFFF
    for b in data:
        crc ^= b << 8
        for _ in range(8):
            crc = ((crc << 1) ^ 0x1021) & 0xFFFF if crc & 0x8000 else (crc << 1) & 0xFFFF
    return crc

assert crc16_ccitt_false(b"123456789") == 0x29B1, "CRC implementation is wrong!"

class FrameParser:
    def __init__(self):
        self.buf = bytearray()
        self.last_seq = None
        self.n_good = 0
        self.n_bad_crc = 0
        self.n_lost = 0

    def feed(self, chunk: bytes):
        out = []
        self.buf.extend(chunk)
        while True:
            # resync: drop everything before the first SOF
            i = self.buf.find(SOF)
            if i < 0:
                self.buf.clear(); break
            if i > 0:
                del self.buf[:i]
            if len(self.buf) < 4:
                break                       # need SOF+SEQ+LEN
            length = self.buf[2]
            total  = 1 + 1 + 1 + length + 2 + 1
            if len(self.buf) < total:
                break                       # wait for more
            if self.buf[total - 1] != EOF:
                del self.buf[:1]            # false SOF; resync
                continue
            seq     = self.buf[1]
            payload = bytes(self.buf[3:3 + length])
            crc_rx  = (self.buf[3 + length] << 8) | self.buf[4 + length]
            crc_calc = crc16_ccitt_false(bytes(self.buf[1:3 + length]))
            del self.buf[:total]

            if crc_rx != crc_calc:
                self.n_bad_crc += 1
                continue

            if self.last_seq is not None:
                gap = (seq - self.last_seq) & 0xFF
                if gap > 1:
                    self.n_lost += gap - 1
            self.last_seq = seq
            self.n_good += 1
            out.append(payload.decode("ascii", errors="replace"))
        return out

    def loss_pct(self):
        tot = self.n_good + self.n_bad_crc + self.n_lost
        return 0.0 if tot == 0 else 100.0 * (self.n_bad_crc + self.n_lost) / tot
```

### 8.4 Throughput check — does 1 Hz actually fit?

**The rule requires ≥ 1 Hz. Verify the arithmetic, do not assume it.**

| Parameter | XBee-PRO S1 | LoRa RFM95W (SF7, BW125) |
|---|---|---|
| Air data rate | 250,000 bps | 5,470 bps |
| Frame size | 102 bytes = 816 bits | 102 bytes = 816 bits |
| Raw air time | 3.3 ms | 149 ms |
| Overhead (preamble, header, ACK, retries) | ×1.5 | ×1.3 |
| **Effective air time per packet** | **~5 ms** | **~194 ms** |
| **Duty cycle at 1 Hz** | **0.5 %** | **19 %** |
| **Headroom** | 200× | 5× ✅ |

**Both work at 1 Hz.** The XBee has absurd headroom — which means you can afford **6 retries** (`RR=6`), converting all that headroom into link reliability. **That is the whole reason to choose a 250 kbps radio for a 1 kbps requirement.**

⚠️ **Do not add a `\n` to the frame.** Emitting `\r\n` doubles your EOF ambiguity and adds a byte you do not need. The rule says carriage return. **Emit `\r`.**

### 8.5 Optional: API mode for per-packet acknowledgements

If you enable `AP=2` on the XBee, you get frame-level transmit status: every packet you send returns a `0x8B` Transmit Status frame telling you whether the remote node acknowledged it. That gives you a **real** per-packet delivery statistic rather than an inferred one from sequence gaps.

**Cost:** your firmware and your ground station both have to speak the XBee API frame format, which adds a week of work and a whole class of new bugs.

> 💡 **Recommendation: start in transparent mode (`AP=0`) with the framing protocol of §8.2.** The sequence-gap method already gives you an accurate loss figure, because the acknowledgements happen at the 802.15.4 MAC layer regardless of `AP`. **Move to API mode only if you have spare time after the first successful flight.**

---

## 9. Testing the link

### 9.1 The test programme

| ID | Test | Setup | Pass criterion | When |
|---|---|---|---|---|
| **LNK-1** | **Bench loopback** | Transmitter and receiver 1 m apart, 1000 packets at 1 Hz | 0 lost, 0 CRC errors | Phase 1 |
| **LNK-2** | **Range test — ground level** | Transmitter carried on a bicycle/vehicle down a straight road, receiver on the 3 m mast, RSSI logged every 100 m | ≥ −92 dBm at 2 km; ≥ −100 dBm at 3 km | Phase 1 |
| **LNK-3** | **Range test — elevation** | Transmitter raised on a mast/drone to 100 m at 1 km, then 300 m at 1 km | RSSI within 6 dB of the free-space prediction | Phase 1 |
| **LNK-4** | **Airframe integration** | Transmitter **inside the assembled airframe with the motor casing installed**, at 5 m and 500 m | RSSI degradation ≤ 10 dB versus a bare antenna | Phase 2 |
| **LNK-5** | **Fade test — polarisation** | Rotate the rocket transmitter through 360° of roll at 1 Hz at 500 m; log RSSI continuously for 5 min | **Record the minimum RSSI.** Pass if min RSSI > sensitivity + 6 dB | Phase 2 |
| **LNK-6** | **Fade test — obstruction** | Walk a person between the transmitter and receiver at 200 m; log RSSI | Document the fade depth. Pass if the link survives | Phase 2 |
| **LNK-7** | **Body-loss test** | Operator stands 0.5 m in front of the ground antenna; log RSSI | Document the loss. **Then write a procedure that forbids it** | Phase 2 |
| **LNK-8** | **Interference tests INT-1…INT-8** | §4.4 | §4.4 criteria | Phase 2 |
| **LNK-9** | **Command reliability** | 200 `TELEM:ON` / `TELEM:OFF` cycles from 1 km | ≥ 99 % ACKed within 3 retries | Phase 2 |
| **LNK-10** | **Endurance** | 60 min at 1 Hz from 1 km | ≤ 1 % packet loss; laptop battery not exhausted | Phase 3 |
| **LNK-11** | **Pad-geometry rehearsal** | Full ground station at the **actual** pad-to-gallery distance, vehicle on the pad, 45 min | ≥ 99 % packet loss-free; **this is the FRR gate** | Phase 3 |

### 9.2 Range test procedure (the one to actually run)

```
  SETUP
    • Ground station: XBee-PRO S1 + 8 dBi patch on a 3 m mast, RSSI logged
      automatically every received packet with a local timestamp.
    • Rover: XBee-PRO S1 + ¼-wave whip, mounted at 1.5 m AGL, transmitting
      a numbered packet at 1 Hz (a simple Arduino + XBee will do).
    • Rover carries a phone with GPS (in aeroplane mode) to log position.
    • ⚠️ A second person at the ground station, whose ONLY job is to keep
      the patch aimed at the rover and to call out RSSI every 30 s.
    • ⚠️ Do NOT do this test alone. Do not do it on a road with traffic.
      Do it on a clear field with landowner permission.

  PROCEDURE
    1. Start at 50 m. Confirm RSSI and 0 % loss. Mark the spot.
    2. Move outward in 100 m steps. At each step:
         a. Stop for 60 s. Log 60 packets.
         b. Record: distance, GPS position, RSSI min/mean/max, loss %.
    3. Continue until loss % > 5 % OR RSSI < −105 dBm.
    4. Note the distance and call it the "practical limit".
    5. Return along the same path, logging again, to check for hysteresis.

  PASS CRITERIA
    • ≤ 1 % loss at 2.0 km with an unobstructed path
    • RSSI ≥ −92 dBm at 1.0 km
    • A "link margin" number computed as (RSSI at 2 km) − (sensitivity)
      must be ≥ 10 dB

  DELIVERABLE
    • RF_Test_Log.csv with every row
    • A single plot of RSSI vs. distance, with the free-space prediction
      overlaid. 📈 Put this plot in the CDR. Nothing else you produce
      will demonstrate RF competence as convincingly.
```

### 9.3 Fade test procedure

The point of a fade test is to find the **worst case**, not the average. The average is always fine.

```
  FADE-1 — POLARISATION FADE
    • Rover transmitter mounted so it can be ROLLED about its long axis.
    • At 500 m, roll it through a full 360° over 10 s, three times.
    • Log RSSI at 10 Hz.
    • RECORD THE MINIMUM. That minimum is the number that goes in your
      link budget as the polarisation allowance. If it is −25 dB, your
      budget is wrong (it assumed −3 dB) and you need a circularly
      polarised ground antenna.

  FADE-2 — OBSTRUCTION FADE
    • At 200 m, have a person walk slowly across the line of sight.
    • Log RSSI at 10 Hz.
    • Note the fade depth and the recovery time.

  FADE-3 — MULTIPATH FADE
    • At 1 km over flat ground, raise and lower the rover from 0.5 m to
      3 m AGL over 60 s while logging RSSI.
    • You will see a scalloped pattern with nulls. That IS the two-ray
      effect, and it is why §3.4 requires an elevated ground antenna.
    • Show this plot to the Jury.

  FADE-4 — FULL-FLIGHT REPLICATION
    • ⭐ The best test available: put the rover transmitter in a model
      rocket, or on a drone, fly it to 300 m and 1 km, and log RSSI for
      the whole flight.
    • If you cannot fly, hoist the transmitter on a kite or a balloon to
      100 m at 1 km.
    • This is the only test that reproduces the real dynamic geometry.
```

### 9.4 Test log format

```csv
test_id,timestamp_utc,range_m,alt_m,rssi_dbm,loss_pct,pkts_sent,pkts_recv,crc_errors,notes
LNK-2,2027-03-14T10:02:00Z,50,1.5,-42,0.0,60,60,0,"clear LOS, good ground plane"
LNK-2,2027-03-14T10:05:00Z,500,1.5,-71,0.0,60,60,0,"clear LOS"
LNK-2,2027-03-14T10:09:00Z,1000,1.5,-82,0.0,60,60,0,"clear LOS"
LNK-2,2027-03-14T10:14:00Z,2000,1.5,-90,1.7,60,59,0,"near practical limit"
LNK-2,2027-03-14T10:19:00Z,3000,1.5,-98,8.3,60,55,0,"losses begin"
FADE-1,2027-03-14T11:30:00Z,500,1.5,-88,3.3,300,290,0,"worst-case roll fade -19dB vs mean"
FADE-3,2027-03-14T12:05:00Z,1000,0.5,-99,15.0,60,51,0,"null at 0.7m AGL; 3m mast fixes"
```

### 9.5 Pre-launch RF checklist (run in this order, on the pad)

- [ ] **RF survey**: RTL-SDR sweep 2.40–2.50 GHz. Record the noise floor and the quietest channel. Confirm Ch 26 is usable; change if not
- [ ] **PAN ID verification**: `ATID` on both radios returns the team number
- [ ] **Channel verification**: `ATSC` on both radios matches
- [ ] **RSSI baseline**: with the vehicle on the pad, ground station reads ≥ −85 dBm. ⚠️ **Worse than −95 dBm = stop and diagnose**
- [ ] **Packet loss check**: 60 packets with ≤ 1 lost
- [ ] **Antenna mast at 3–5 m**, patch aimed at the pad, **nobody standing in front of it**
- [ ] **Laptop WiFi off, phone hotspots off, Bluetooth off**
- [ ] **`TELEM:OFF` confirmed** — vehicle not transmitting before the command
- [ ] **`TELEM:ON` → 10 packets received → `ZERO` → altitude reads 0.0 m**
- [ ] **LoRa backup link tested once**, then powered down to save the survey
- [ ] **Spare XBee, spare antenna, spare USB adapter, spare SD card in the case**
- [ ] **Ground station on mains power if available** (saves the laptop battery for the launch itself)
- [ ] **Ground station's own battery state**: laptop ≥ 80 %, power bank ≥ 80 %

---

## 10. Common failure modes and how to avoid them

| Symptom | Likely cause | Fix |
|---|---|---|
| **No packets at all, radio powered** | PAN ID mismatch; different channel (`SC`); baud rate mismatch (`BD`); TX and RX swapped | Verify `ATID`, `ATSC`, `ATBD` on **both** radios with `AT` commands. Check TX→RX crossover |
| **Packets only when the vehicle is close** | Antenna detuned by the airframe; carbon-fibre Faraday cage; ground antenna at 1 m | NanoVNA sweep with the airframe assembled; move the antenna external; raise the mast |
| **Telemetry stops at boost, resumes at descent** | Airframe blockage; polarisation fade; **or the SD write is blocking the UART** | Check the SD write policy (no writes during ascent); log RSSI to confirm a fade |
| **Garbled / unparseable bytes** | Baud rate mismatch; ground-loop noise on the USB; a floating XBee `DIN` | Fix the baud rate; use a **powered** USB hub; add a 10 kΩ pull-up on `DIN` |
| **Telemetry stops when the servos move** | **Conducted** interference: shared ground between the servo rail and the radio rail; no bulk capacitance | Separate converters (§5.3 of the Flight Computer doc); 1000 µF + 100 nF at the servo connector; **twisted pair** from the servo |
| **Telemetry stops when the laptop's WiFi is on** | Co-channel interference from the laptop's own WiFi into the ground radio | Disable WiFi. Always |
| **Loss rate rises as the rocket rolls** | Polarisation fade | Circularly polarised ground antenna, or accept it and lean on the SD log |
| **Loss rate rises over time on the pad** | Battery sag; thermal drift in the radio's reference oscillator | Log `VBAT`; add a heatsink or shade the radio; use the battery check of §5.6 |
| **Packets arrive in bursts, then silence** | **Buffer overflow in the XBee's 256-byte buffer** at 115200 baud | Reduce the baud rate to 57600, or pace the transmissions, or use flow control (`RTS`/`CTS`) |
| **The `~` byte appears inside a payload** | A field contains a `~` | ⚠️ Sanitise the payload: replace any `~` in `<ANY OPTIONAL DATA>` with `-` before framing |
| **CRC failures at low rate but no packet loss** | Marginal SNR — errors are being caught by the CRC, which is *working correctly* | This is the warning sign before real loss. **Treat a rising CRC-error rate as a link failure in progress** |
| **The ground station misses the first 10 s of flight** | A SD `fsync` or a `matplotlib` redraw blocked the parser | Separate threads; bound the queue; never block the serial reader |

---

## 11. Summary of the recommended configuration

| Element | Choice | Cost (INR) |
|---|---|---|
| **Flight radio (rocket)** | XBee-PRO S1, RPSMA, 18 dBm (2.4 GHz) | ₹2,600 |
| **Flight antenna (rocket)** | ¼-wave sleeve dipole, 2.1 dBi, 30 mm, in the fin can | ₹50 |
| **Ground radio** | XBee-PRO S1, RPSMA | ₹2,600 |
| **Ground antenna** | 2.4 GHz 8 dBi patch, tripod-mounted | ₹900 |
| **Ground antenna mast** | 3–5 m telescopic + tripod | ₹3,500 |
| **Ground interconnect** | 0.5 m RG-316 + 5 m active USB extension + powered hub | ₹1,600 |
| **Backup link** | 2 × RFM95W at 866 MHz | ₹2,200 |
| **Channel plan** | Rocket Ch 26 (2480 MHz), payload Ch 20 (2450 MHz), LoRa 866.5 MHz | — |
| **PAN ID** | Team number, declared at CDR | — |
| **Protocol** | `~` + SEQ + LEN + Annexure-2 ASCII CSV + CRC16-CCITT-FALSE + `\r` | — |
| **Data rate** | 1 Hz, 102 bytes/frame, 0.5 % duty on the primary link | — |
| **Expected margin** | **+13.9 dB at 2 km** (with 16 mW rocket EIRP) | — |
| **Ground station total** | | **₹26,950** |

> ⚠️ **Everything above is a design intent until a measured RSSI-versus-range plot exists.** The single most valuable thing this subsystem can produce before the CDR is one CSV file and one graph. **Book a field day and go get it.**

---

*Prepared for UVCE Rocketry Club, Bengaluru. Frequencies, power limits and licensing statements reflect Indian WPC/DoT rules as understood in 2026 and **must be independently verified before transmitting** — the club is responsible for compliance. Prices are Indian retail order-of-magnitude figures; see [Electronics BOM and Sourcing](Electronics_BOM_and_Sourcing.md) for supplier detail.*
