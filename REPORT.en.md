# US Debt After $40 Trillion — Debt, the Dollar, and Financial Repression 2.0

> **Research date**: 2026-08-30 ｜ **Time-sensitive figures current to**: **2026-09-07**
>
> **The conclusion in one paragraph**: total US debt passed **$40 trillion** on 2026-08-18, and net interest is growing (+10.8%) at **3.4×** the rate of net receipts (+3.2%) — compounding has taken over the fiscal path. But **the crisis will not take the shape of a default; it will take the shape of a "debasement tax"**: a 30-year auction stop of 5.216% (the highest since 2001) alongside a 5-year CDS of only 42bp is the market pricing *inflation, not hard default*. **The way out is not a future tense, it is a present participle** — stablecoins mandated into short bills (the GENIUS Act), the eSLR relaxed, the Fed buying bills again, the Treasury doubling long-end buybacks: what is being assembled is a modern replica of the 1946-1980 "financial repression" playbook. The one missing part is a **negative real policy rate** — and Warsh has turned hawkish since taking office, so the monetary and fiscal authorities are now **pulling in opposite directions at the two ends of the curve**. That is the sharpest policy conflict on the board. **The "petrodollar agreement expiring" is fiction** (there is no agreement that could expire); the real erosion is a slow variable — a 8.4pp fall in the dollar's reserve share over a decade — while stablecoins are simultaneously *re-dollarising* the world. **Timing is not forecastable** (the CBO's own words: there is no identifiable tipping point), but the conditional window is **densest in 2027-2028** (the $1.45T financing gap TBAC warned about + the next debt-limit X-date + the overlap of Dalio's and Rogoff's verbal windows).
>
> **How to read this page**: this report predicts no dates. It pins down **mechanisms** and **falsifiable conditions**. Every figure carries a source grade (✅ primary / 🔶 primary + own calculation / ⚠ single source / ❔ widely accepted but not adversarially verified / ❌ falsified); the grades and the citation rules are in **§10.1**. The six triggers in §8.3 have fixed adjudication sources, were back-filled with their reading on the day they were registered, and are **never revised after they fire**. Throughout, where a figure is easy to misread, the wrong reading and the right one are given side by side; §10 registers the six load-bearing claims that adversarial verification overturned — that is not an appendix, it is the method. **Not investment advice.**

---

## 1. The debt itself: an anatomy of $40 trillion (all primary)

### 1.1 Size and measures (⚠ the four "total debt" numbers are not the same thing)

| Measure | Value (**🔄 refreshed 2026-09-03**) | Note |
|---|---|---|
| **Total public debt** | **$40.103T** (08-27: $40.078T) | held by the public **$32.42T** + intragovernmental **$7.68T**; **first crossed $40T on 08-18** ✅ Fiscal Data API `debt_to_penny` |
| **Debt held by the public** | **$32.42T** | this is the numerator in CBO's debt/GDP (about 101% for FY2026) |
| **Marketable debt** | $31.455T (07-31; MSPD is monthly and not yet updated) | Bills $6.99T / Notes $16.17T / Bonds $5.49T / TIPS $2.15T / FRN $0.65T ✅ MSPD |
| Debt subject to limit | ceiling $41.1T, **headroom $997B** | the OBBBA embedded +$5T; 🔴 **extrapolating the last 91/182/365-day net growth rates puts the ceiling date at 2026-12-07 ~ 2027-01-10 — almost exactly on the seating of the new Congress (2027-01-03)** |

Treasury Secretary Bessent, 08-20: "there is no magic to the number $40 trillion." Rhetorically true; arithmetically, see §2.

### 1.2 Structure: heavily front-loaded

> 📖 **Terminology: what "bills" means throughout this report**
>
> | Name | Maturity | Coupon | |
> |---|---|---|---|
> | **Bills** | **≤1 year** (4/8/13/17/26/52 weeks) | **zero-coupon, sold at a discount** (bought below par, redeemed at par) | the short end |
> | Notes | 2–10 years | semi-annual | intermediate |
> | Bonds | 20–30 years | semi-annual | long end |
>
> The 30Y auction stop of 5.216%, the term premium and the long-end buybacks in this report all refer to the notes/bonds end; **"short end" and "bills" are used interchangeably throughout**.
> ⚠ **Two guards against misreading, both bearing directly on the argument**:
> 1. **"The Fed buying bills again" ≠ QE** — QE buys long paper (absorbing duration risk, compressing the term premium); buying bills is a **reserve management purchase** (the Fed's own term) and absorbs no duration risk. **Its function inside this report's framework is to supply the short end with a price-insensitive official buyer** (that is exactly what the corresponding row in §6.2's table means);
> 📖 **Three questions on "the Fed buying bills", to pin down who does what and where the money comes from**
>
> **Q1 — Who issues the bills?** The **Treasury** (to cover deficits and roll maturing debt); the Fed is only one buyer among many. Two institutions: the Treasury is the government's cashier, the Fed is the central bank. **By law the Fed may not subscribe to new issues in the primary market**; it buys in the secondary market through primary dealers, or rolls its maturing holdings at auction in equal amount.
> **Q2 — What does the Fed pay with?** **Bank reserves it creates itself**: the payment is a credit to the selling bank's reserve account at the Fed, and **those reserves come into existence at the moment the payment is made**. Treasuries go on the asset side, an equal amount of reserves on the liability side; the balance sheet expands.
> **Q3 — Is that "printing money"?** **Mechanically yes** (electronic reserves are the modern form of printing), **but the equation "printing ⇒ stimulus" does not hold for these purchases**: QE actively buys long paper to compress the term premium; this is a **reserve management purchase** — once QT ended, growth in currency in circulation and the TGA automatically drains reserves, and buying bills passively replaces them to maintain an "ample reserves" regime. ⚠ **Both sentences must travel together; quoting only one is a misquote: the motive is plumbing maintenance, the mechanical consequence is a price-insensitive official buyer at the short end** (that is the full reading of the row in §6.2).
>
> 🔴 **Which closes a loop worth spelling out (the mechanics of partial monetisation)**: the Treasury issues bills → the Fed creates reserves and buys them → the interest the Treasury pays the Fed (net of the Fed's costs) **flows back to the Treasury** ⇒ **the net interest cost of debt held by the Fed tends to zero**. ⚠ **That remittance is currently switched off**: because the Fed pays more on reserves than it earns on assets, it is running a cumulative loss — a **deferred asset of $233.5B** (H.4.1 "Earnings remittances due to the U.S. Treasury" = -$233,518M, 2026-08-26, ✅ primary). Remittances resume only after that loss is fully worked off.

**The sequence (computed from the full weekly FRED series `RESPPLLOPNWW`, matching H.4.1 digit for digit)**:

| Year | Avg. fed funds | Deferred asset, year-end | Deterioration that year |
|---|---|---|---|
| 2010-2021 | 0.1-2.2% | **positive (remittances flowing to Treasury)** | — |
| **2022** | 1.68% | **-$18.0B** | -$19.9B (**first year negative = the year the hiking cycle began**) |
| **2023** | **5.02%** | -$131.5B | 🔴 **-$113.5B** |
| **2024** | **5.14%** | -$215.2B | -$83.7B |
| 2025 | 4.21% | -$242.7B (trough) | -$27.5B |
| **2026 (to 08-26)** | 3.64% | **-$233.5B** | **+$9.2B (starting to refill)** |

**Three readings**: ① **the turn was mechanical, not chosen** — it flipped negative in 2022, the year hiking began, and the pace of deterioration tracks the policy rate closely; ② **2023 alone burned $113.5B, roughly the order of a decade of remittances** — that is the direct cost of fighting inflation, written on the fiscal ledger; ③ **the inflection has arrived (+$9.2B year to date) but at this pace filling the hole takes decades**; the realistic path is a policy rate coming down (lower liability costs) plus old low-coupon assets rolling into higher yields (rising asset income), accelerating from both ends — **even optimistically, "several years at minimum" holds**.

⇒ **This adds a third channel to §6.2.4b's "authorities pulling against each other"**: the original text has the monetary authority pushing rates up against the fiscal authority pushing the long end down. The table shows a third — **every notch of policy rate the Fed holds enlarges its own bill to the Treasury; part of the cost of tightening is deducted straight from federal revenue.** ⇒ **A hawkish stance is, on the fiscal ledger, a persistent implicit expenditure that never enters the deficit debate.**

🔴 **The accounting boundary (a question that always comes): the Fed's losses are counted in NO official government debt measure.** Three parts:
1. **Not counted**: the deferred asset is a line on the Fed's own balance sheet, **not a Treasury liability**. It is not in the $40.08T total, not in debt held by the public, not in the debt-limit measure; nor does it render the Fed insolvent (bankruptcy law does not apply to it and the Treasury has no obligation to recapitalise it);
2. **But it enters the deficit for real, in the form of missing revenue**: remittances are budgeted as **miscellaneous receipts** — **$50-100bn a year** through 2015-2021, peaking near $109bn in 2021. **That revenue went to zero from 2022** ⇒ **the deficit is larger by the same order every year, and that is already inside the deficit figures in §2 — there is simply no line item labelled "Fed losses"**;
3. ⇒ **What that implies about measures**: **the debt measures understate the fiscal cost of monetary tightening**. On economic substance, the interrupted remittances should be treated as several years of implicit fiscal expenditure; under current accounting they are silently spread into the deficit as revenue that isn't there. **This belongs to the same family as §6.2.6's "cannot be attributed and therefore not measured": nothing carries its name, which is not the same as it not existing.** ⇒ **On magnitude: at the Fed's recent net income run-rate, reconnecting the loop is a matter of years at least** — until then the interest the Treasury pays the Fed is a real outlay with no offsetting return flow, and the machinery of "partial monetisation" has only its buying leg turning while the return leg is cut. ⇒ **What Warsh controls is the rate end of exactly this loop** — the fiscal side stuffs volume into the short end, the monetary side sets the price at which that volume is held. **T6 (the real policy rate turning negative) is the moment this loop slides from "plumbing maintenance" into "the tax being levied".** The three classes of arranged short-end buyers (stablecoins / money funds / the Fed) differ in where their money comes from and how price-sensitive it is; see §6.

> 2. **Bills are zero-coupon ⇒ there is no coupon to lock in** — the holder's return is entirely determined by the rate at which the position is rolled. That is the mirror image of §1.2's "interest cost is at a historic high in its sensitivity to front-end rates": **the Treasury and bill holders sit on opposite sides of the same front-end rate**. The GENIUS framework locks stablecoin reserves onto that end (the issuer takes the discount income, the holder is barred by statute from receiving any), so three sources of demand (stablecoins / the Fed / the Treasury's own issuance tilt) crowd into the short end — quantified in §6.1b.

- **Bills are 22.2% of marketable debt** (2026-07-31), above TBAC's recommended 15-20% band; weighted average maturity 71 months (GAO, 2025-09);
- **$10.48T matures within 12 months ≈ 33.3% of marketable** (computed security by security across 887 MSPD lines, cross-checked against GAO's independent 33%); 2026-2028 maturities total $15.5T ≈ 49%;
- ⚠ **Guard against misreading**: that 33% includes the routine monthly roll of bills. It is an **arithmetic consequence** of a front-loaded structure, not a cliff meaning "a third has to be repaid within a year". What it actually means is: **interest cost is at a historic high in its sensitivity to front-end rates** — every 100bp at the front passes through to a third of the stock within one year.

### 1.3 Holders: the marginal buyer has completed a rotation

| Holder | Latest | Change at the margin |
|---|---|---|
| Foreign, total | $9,299.0B (2026-06) | **+$205B** y/y, but falling for two straight months from the **$9,489B peak of 2026-02** (⚠ this is **not** "a record high") |
| — foreign official | $3,778.1B | **-$114B** y/y (a net seller) |
| — Japan (largest) | $1,116.7B | **-$123B over the four months from the February peak** — the largest single-holder move of 2026 |
| — China (third) | $633.4B | **lowest since the Lehman month of 2008-09**, -$98B y/y |
| — UK (up to second) | $939.9B | +$84B y/y; Belgium + Luxembourg together $917B ≈ China's direct holdings |
| Fed (SOMA) | $4,545.7B | after QT ended on **2025-12-01**, +**$343B in nine months, essentially 100% bills** (+$346B) ✅ H.4.1 |
| Money market funds | $3,426B (2026Q1) | already the second-largest single holding sector, the mirror image of bill supply |

**Three readings**:
1. **"Foreigners are dumping Treasuries" does not hold in aggregate** — monthly TIC flows through H1 2026 are consistently net purchases, and **private-led**. What does hold is at the sector and country level: official down, private up. This is *hedging rather than selling* (the BIS confirmed rising hedge ratios in 2025; part of that has since been given back in 2026);
2. ⚠ **The Euroclear paradox (registered explicitly as undecidable)**: Belgium (Euroclear) has always been the prime suspect channel for Chinese official custody transfers — if part of that +$52B is China changing custodian, then both "China at its lowest since 2009" and "official → private rotation" have to be discounted. **TIC is measured by custody location; this cannot be resolved here, and we do not pretend it can be**;
3. **The Fed is materially back in the market**: an operation described as technical "reserve management" absorbed $346B of bills in nine months — far larger than "technical" usually suggests.

### 1.4 Auction health: the primary market is "weak but not failing", while the secondary market and official behaviour show "impaired function" — both hold at once, on one consistent measure

- **Three weak auctions on 2026-03-24/25/26** (intermediates): 2Y tail 1.8bp, primary dealers forced to take **24%** (average 11%); 5Y/7Y also weak;
- **2026-08-13**, the $25B 30Y stopped at **5.216%, the highest auction rate since 2001**, but with a tail of only 0.4bp and PD takedown of 11.5%; on 08-19 the 20Y stopped at 5.204% (result sheet checked at source, indirects 62.9%);
- **08-18**, the secondary-market 30Y touched **5.33-5.34%, the highest since 2007**; July saw the longest stretch above 5% since 2007;
- **09-01**, the 10Y closed at **4.80%, the highest since 2023-10-31** (30Y 5.27, still below the 5.31 of 08-17; see §7.4 for the measurement: ordinary speed, record levels);
- The Treasury Secretary himself called 30-year liquidity "very poor", and doubled the size of each long-end buyback operation ($2B→$4B, 09-09 ~ 11-04).

**⚠ Ruling on measures (so that two chapters cannot each take the half they like)**: "the auctions have not failed" and "long-end function is impaired" **do not contradict each other** — **quantity always clears (there has been no failed auction); the anomaly is in price and liquidity**: the clearing price has moved up to a 25-year high, and market-making liquidity deteriorated far enough for officials to step in. The correct formulation is: **the market has substituted "clearing on price" for "refusing on quantity"**. Crisis monitoring should therefore watch price and official behaviour, and should not wait for a failed auction — in the structure of the Treasury market, one will almost never occur.

📌 **A data trap, found in practice**: the traditional `mfh.txt` on ticdata.treasury.gov has been frozen at **2023-01** and is no longer updated; current holdings only live under the `slt_table5` path — an old bookmark or an automated script will silently pick up a three-year-old table.

---

## 2. The fiscal path: compounding interest has taken over

### 2.1 Current figures (primary, MTS)

- **FY2025 final**: receipts $5,234.6B / outlays $7,010.0B / deficit **$1,775.4B**; ⚠ the apparent "$41B improvement" year on year contains roughly **$200B of accounting revaluation on the student-loan portfolio** (one-off, non-cash) — stripping it out, the underlying deficit actually rose;
- **First 10 months of FY2026**: deficit **$1,798.8B, +10.5% y/y**; the $432B deficit in July alone was the largest single month since 2021-03; the CBO has revised the full year up to **$2.1T** (+18%);
- **Net interest**: FY2025 **$970.4B = 18.5% of receipts**, already above defence; $931.4B in the first 10 months of FY2026, **+10.8% — 3.4× the growth of net receipts (+3.2%)** (⚠ caliber: using **gross** receipts as the denominator gives 2.7×; this report uses **net** receipts throughout);
- 🔄 **09-07 refresh**: the latest MTS period is still **2026-07-31** (the August report lands around 09-11) ⇒ the readings in this section and T1 are **unchanged this period**. ✅ **The registered value was independently recomputed and confirmed**: rolling 12 months (2025-08 → 2026-07) net interest **$1,061.0B** / net receipts **$5,373.3B** = **19.75%**, matching the 19.7% registered in §8.3;
  ⚠ **Caliber pinned down (a trap this recomputation exposed, now written into the criterion)**: the denominator of T1 **must** be **MTS Table 4's `current_month_net_rcpt_amt` (net receipts, refunds already deducted)**. Using Table 1's monthly receipts field instead gives $5,180.2B → 20.48%; using Table 4's **gross** gives $5,900.4B → 17.98% — **one word, "receipts", three measures, three answers, sitting 2.25 / 1.52 / 4.02pp from the threshold**. Filed under the error family "two different tables behind one indicator name";
- **Gross interest**: $1,170B in the first 10 months of FY2026, on track to exceed **$1.4T** for the year (⚠ do not mix gross and net: gross includes interest paid to intragovernmental accounts).

<div style="overflow-x:auto;margin:1.1em 0;"><svg viewBox="0 0 860 430" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#0d1117;border:1px solid rgba(255,255,255,.08);border-radius:6px;">
<text x="64" y="24" fill="#edf1f6" font-size="15" font-weight="bold">Net interest vs federal receipts: y/y growth (left axis) and net interest as a share of receipts (right axis, gold bars)</text>
<rect x="40.6" y="265.6" width="46.8" height="92.4" fill="rgba(211,181,119,.13)"/><rect x="113.8" y="259.4" width="46.8" height="98.6" fill="rgba(211,181,119,.13)"/><rect x="187.0" y="235.7" width="46.8" height="122.3" fill="rgba(211,181,119,.13)"/><rect x="260.2" y="223.2" width="46.8" height="134.8" fill="rgba(211,181,119,.13)"/><rect x="333.4" y="232.0" width="46.8" height="126.0" fill="rgba(211,181,119,.13)"/><rect x="406.6" y="249.4" width="46.8" height="108.6" fill="rgba(211,181,119,.13)"/><rect x="479.8" y="236.9" width="46.8" height="121.1" fill="rgba(211,181,119,.13)"/><rect x="553.0" y="173.3" width="46.8" height="184.7" fill="rgba(211,181,119,.13)"/><rect x="626.2" y="134.6" width="46.8" height="223.4" fill="rgba(211,181,119,.13)"/><rect x="699.4" y="127.1" width="46.8" height="230.9" fill="rgba(211,181,119,.13)"/><rect x="772.6" y="98.4" width="46.8" height="259.6" fill="rgba(211,181,119,.13)"/><line x1="64" y1="330.6" x2="796" y2="330.6" stroke="rgba(255,255,255,.07)"/><text x="56" y="334.6" text-anchor="end" fill="#8b95a5" font-size="12">-10%</text><line x1="64" y1="275.9" x2="796" y2="275.9" stroke="rgba(255,255,255,.07)"/><text x="56" y="279.9" text-anchor="end" fill="#8b95a5" font-size="12">+0%</text><line x1="64" y1="221.2" x2="796" y2="221.2" stroke="rgba(255,255,255,.07)"/><text x="56" y="225.2" text-anchor="end" fill="#8b95a5" font-size="12">+10%</text><line x1="64" y1="166.4" x2="796" y2="166.4" stroke="rgba(255,255,255,.07)"/><text x="56" y="170.4" text-anchor="end" fill="#8b95a5" font-size="12">+20%</text><line x1="64" y1="111.7" x2="796" y2="111.7" stroke="rgba(255,255,255,.07)"/><text x="56" y="115.7" text-anchor="end" fill="#8b95a5" font-size="12">+30%</text><line x1="64" y1="56.9" x2="796" y2="56.9" stroke="rgba(255,255,255,.07)"/><text x="56" y="60.9" text-anchor="end" fill="#8b95a5" font-size="12">+40%</text><text x="804" y="362.0" fill="rgba(211,181,119,.55)" font-size="12">0%</text><text x="804" y="237.2" fill="rgba(211,181,119,.55)" font-size="12">10%</text><text x="804" y="112.4" fill="rgba(211,181,119,.55)" font-size="12">20%</text>
<line x1="64" y1="275.9" x2="796" y2="275.9" stroke="rgba(255,255,255,.28)"/>
<path d="M64.0,272.9 L137.2,267.8 L210.4,273.6 L283.6,254.0 L356.8,282.6 L430.0,175.7 L503.2,160.9 L576.4,327.0 L649.6,216.8 L722.8,240.7 L796.0,258.4" fill="none" stroke="#5aa7d6" stroke-width="2.4"/>
<path d="M64.0,233.3 L137.2,225.7 L210.4,146.9 L283.6,190.1 L356.8,320.9 L430.0,263.9 L503.2,85.0 L576.4,63.8 L649.6,91.2 L722.8,220.8 L796.0,216.9" fill="none" stroke="#e06c5a" stroke-width="2.6"/>
<circle cx="64.0" cy="233.3" r="3.4" fill="#e06c5a"/><circle cx="137.2" cy="225.7" r="3.4" fill="#e06c5a"/><circle cx="210.4" cy="146.9" r="3.4" fill="#e06c5a"/><circle cx="283.6" cy="190.1" r="3.4" fill="#e06c5a"/><circle cx="356.8" cy="320.9" r="3.4" fill="#e06c5a"/><circle cx="430.0" cy="263.9" r="3.4" fill="#e06c5a"/><circle cx="503.2" cy="85.0" r="3.4" fill="#e06c5a"/><circle cx="576.4" cy="63.8" r="3.4" fill="#e06c5a"/><circle cx="649.6" cy="91.2" r="3.4" fill="#e06c5a"/><circle cx="722.8" cy="220.8" r="3.4" fill="#e06c5a"/><circle cx="796.0" cy="216.9" r="3.4" fill="#e06c5a"/><circle cx="64.0" cy="272.9" r="3.4" fill="#5aa7d6"/><circle cx="137.2" cy="267.8" r="3.4" fill="#5aa7d6"/><circle cx="210.4" cy="273.6" r="3.4" fill="#5aa7d6"/><circle cx="283.6" cy="254.0" r="3.4" fill="#5aa7d6"/><circle cx="356.8" cy="282.6" r="3.4" fill="#5aa7d6"/><circle cx="430.0" cy="175.7" r="3.4" fill="#5aa7d6"/><circle cx="503.2" cy="160.9" r="3.4" fill="#5aa7d6"/><circle cx="576.4" cy="327.0" r="3.4" fill="#5aa7d6"/><circle cx="649.6" cy="216.8" r="3.4" fill="#5aa7d6"/><circle cx="722.8" cy="240.7" r="3.4" fill="#5aa7d6"/><circle cx="796.0" cy="258.4" r="3.4" fill="#5aa7d6"/><text x="64.0" y="378" text-anchor="middle" fill="#8b95a5" font-size="12">FY16</text><text x="137.2" y="378" text-anchor="middle" fill="#8b95a5" font-size="12">FY17</text><text x="210.4" y="378" text-anchor="middle" fill="#8b95a5" font-size="12">FY18</text><text x="283.6" y="378" text-anchor="middle" fill="#8b95a5" font-size="12">FY19</text><text x="356.8" y="378" text-anchor="middle" fill="#8b95a5" font-size="12">FY20</text><text x="430.0" y="378" text-anchor="middle" fill="#8b95a5" font-size="12">FY21</text><text x="503.2" y="378" text-anchor="middle" fill="#8b95a5" font-size="12">FY22</text><text x="576.4" y="378" text-anchor="middle" fill="#8b95a5" font-size="12">FY23</text><text x="649.6" y="378" text-anchor="middle" fill="#8b95a5" font-size="12">FY24</text><text x="722.8" y="378" text-anchor="middle" fill="#8b95a5" font-size="12">FY25</text><text x="796.0" y="378" text-anchor="middle" fill="#8b95a5" font-size="12">FY26*</text>
<line x1="796.0" y1="46" x2="796.0" y2="358" stroke="rgba(211,181,119,.4)" stroke-dasharray="4,4"/>
<text x="790.0" y="204.8" text-anchor="end" fill="#e06c5a" font-size="13" font-weight="bold">+10.8%</text>
<text x="790.0" y="276.4" text-anchor="end" fill="#5aa7d6" font-size="13" font-weight="bold">+3.2%</text>
<text x="790.0" y="62" text-anchor="end" fill="#d3b577" font-size="13" font-weight="bold">3.4×</text>
<rect x="74" y="54" width="12" height="3" fill="#e06c5a"/><text x="92" y="60" fill="#c6ceda" font-size="12.5">Net interest y/y (FY26* = first 10 months)</text>
<rect x="74" y="74" width="12" height="3" fill="#5aa7d6"/><text x="92" y="80" fill="#c6ceda" font-size="12.5">Net receipts y/y</text>
<rect x="74" y="92" width="12" height="9" fill="rgba(211,181,119,.35)"/><text x="92" y="100" fill="#c6ceda" font-size="12.5">Net interest / receipts (right axis) 7.4%→20.8%</text>
<text x="64" y="422" fill="#6b7585" font-size="11.5">Source: Treasury MTS Table 9 (Net Interest) / Table 4 (Total Receipts), fiscal-year basis, pulled from the primary API on 2026-08-30; FY26* is the y/y for the first 10 months. Ratios are meaningless in the negative-growth years FY20/FY23 and are not shown.</text>
</svg></div>

**Reading the chart**: from FY2022 the red line (net interest growth) sits above the blue (receipts growth). The 34-39% prints of FY22-24 were a one-off step from rate repricing; **the FY25-26 readings of 10-11% are still 1.6-3.4× the growth of receipts, and that is what "compounding has taken over" looks like in its normal state**. The gold bars (net interest as a share of receipts) climb from 7.4% in FY16 to **20.8%** in the first 10 months of FY26, with only a brief dip in FY20-21 (zero rates plus a receipts surge) — **falling rates have reversed this curve before, which is the other side of §6's fight over who controls the ignition switch**. ⚠ In FY20 and FY23 receipts shrank, so the ratio is meaningless and is not plotted.

### 2.2 A shock almost nobody puts a variable on: the judiciary

**On 2026-02-20 the Supreme Court ruled 6-3 that the IEEPA does not authorise presidential tariffs** (Learning Resources v. Trump); collection stopped that day and refunds have already exceeded $100B:
- FY2026 tariff receipts are running roughly **$250B (-60%) below forecast**; **net tariffs for July 2026 were negative (-$8.5B: refunds exceeded collections)** — the "tariffs will fill the hole" story collapsed inside a single quarter;
- The tariffs that survive on other authority (§232/§301) are worth only about $0.7T over ten years, against **the OBBBA's +$4.1T over ten years (including interest)** — an order of magnitude too small to offset.

### 2.3 The long path: the deterioration is almost entirely interest-driven

CBO's long-term outlook (2026-03): debt/GDP **101% (FY2026) → 120% (2036) → 175% (2056)**; net interest **3.3% → 6.9% of GDP**, overtaking Social Security in FY2048 to become the **single largest** line of spending — while the **primary deficit stays around 2% of GDP throughout**. That is: **the problem is no longer "spending too much", it is the compounding of interest.** The CBO revised its own 2055 projection up by 16pp within a single year (mostly the OBBBA) — **that is how wide the error band on distant figures is; these are current-law extrapolations, not schedules.**

- **Trustees 2026 (06-09)**: OASI trust-fund depletion **pulled forward to 2032Q4**, entering a "within six years" window for the first time; ⚠ depletion means **an automatic cut of about 22% (78% still payable)** — a political bomb, **not a default event**;
- **Ratings**: after Moody's cut to Aa1 on 2025-05-16, S&P (2026-06-26) and Fitch (2026-08-13) both affirmed AA+ stable **after** the tariff collapse and the deficit revision — **the agencies' tolerance band is far wider than the fiscal data would suggest**; ⚠ Fitch's "deficit of 7.4% of GDP" is on a general-government basis (states and localities included, calendar year), **1.5pp+ away from the 5.8-6% federal fiscal-year figure; the two must not be mixed**;
- **⚠ Threshold, guarded against misreading**: net interest / receipts is about 18.6% in 2026, "already past the 1991 peak" — but **what followed the same crossing in 1991 was 1990s growth and fiscal consolidation, not a crisis**. Crossing a threshold ≠ the start of a countdown; this indicator has been reversed before;
- **Debt-limit calendar**: the OBBBA raised the ceiling by $5T to $41.1T; $2.9T of that was consumed by 2026-05 (more than half). BPC puts **the next X-date between late 2027 and mid-2028** — squarely inside §8's conditional window.
- The fastest-deteriorating line on the spending side is not actually interest: **Medicare +16% ($131B) in the first 10 months of FY2026**, faster than interest (+11%) — ~~worth a separate investigation, not pursued here (registered)~~ ✅ **investigated, see §2.4: roughly $60-80B of that is a payment-calendar artefact; adjusted, the growth is about +8~10%, and "faster than interest" does not hold on the adjusted measure**.

### 2.4 Tracing the Medicare +16% (primary, MTS Table 5)

**① First, split it down to the trust-fund level (FYTD first 10 months, net outlays):**

| Fund | FY2026 | FY2025 | y/y | Δ |
|---|---:|---:|---:|---:|
| **HI (Part A, inpatient)** | $407.6B | $367.2B | **+11.0%** | +$40.4B |
| **SMI (Parts B+D, outpatient / drugs)** | $721.1B | $609.3B | 🔴 **+18.3%** | +$111.8B |
| **Total** | **$1,128.7B** | **$976.5B** | **+15.6%** | **+$152.2B** |

⚠ Caliber note: the "+16% / $131B" in the last bullet of §2.3 is on the functional classification (function 570, net of premiums); this table is on the Table 5 trust-fund basis — **the two agree in direction and magnitude, and differing numbers are normal**. ⇒ **The deterioration is concentrated in SMI (Parts B/D), not on the inpatient side** — which rules out the most common intuitive explanation, runaway inpatient utilisation.

**② 🔴 The prime suspect, confirmed: a payment-calendar artefact (the fiscal version of "the window boundary ate the truth")**

Medicare Advantage and Part D monthly capitation payments are made on **the first of each month**, and are **pulled forward to the previous business day when that falls on a weekend**:
- 🔴 **2026-08-01 was a Saturday ⇒ the entire August payment moved to 07-31, landing inside FY26's "first 10 months" window** ⇒ the window contains **11** monthly payments;
- **2025-08-01 was a Friday ⇒ the same FY25 window contains the normal 10** (the weekend shifts in February, March and June of FY25 all happened *inside* the window, so they cancel out and produce no boundary effect).

**The shift is directly visible in monthly net outlays** (MTS Table 5):

| Month | SMI | HI |
|---|---:|---:|
| 2026-04 | $67.6B | $37.4B |
| 2026-05 | $66.7B | $37.0B |
| 2026-06 | $76.8B | $46.1B |
| 🔴 **2026-07** | **$130.0B** | **$62.2B** |
| (vs 2025-07) | $74.1B | $41.5B |

**⇒ July alone is nearly double its own normal month.** The excess over this year's April-June baseline is roughly $55-60B for SMI and $20B for HI, so **about $60-80B in total is the mechanical effect of counting one extra monthly payment, not a deterioration in spending** (the range is wide because the baseline months carry their own intra-week payment-timing noise; we do not force a point estimate).

**③ ⇒ The real growth rate after adjustment:**
> **Of the $152.2B year-on-year increase, roughly $60-80B is a calendar artefact ⇒ adjusted, Medicare's first-10-month growth is about +8% ~ +10%.**
> 🔴 **⇒ The statement "Medicare is growing faster than interest (+11%)" therefore [does not hold, or is doubtful] on the adjusted measure** — adjusted Medicare is on par with or slightly below net interest (+10.8%), and **the judgement that "the fastest-deteriorating line is not interest" rests on the unadjusted measure**. ⚠ The **CBO Monthly Budget Review** (its "adjusted for timing shifts" basis) is the recommended final adjudication source.

**④ The +8~10% that survives adjustment is real growth. Candidate mechanisms (⚠ directions are public record; magnitudes not verified item by item, no ruling given):**
- **MA rates**: the final CY2026 Medicare Advantage benchmark update was about **+5.06%** (announced 2025-04, the largest in recent years), affecting months 1-7 of the FYTD;
- **Part D restructuring (IRA)**: after the $2,000 out-of-pocket cap, costs shift onto plans ⇒ higher direct subsidy and premium-stabilisation outlays;
- **Demographics**: the baby boom entering the programme, beneficiaries growing 2-3% a year;
- FFS payment updates and utilisation.

**Method, on the record**: this case belongs to the "the window boundary ate the truth" family — **a timing shift inside the window is harmless because the total is conserved; a shift that happens to cross the window boundary lands whole inside the growth rate**. Whenever you quote a "first N months, year on year", first check whether the payment dates at either end of the window fall on a weekend.

**⑤ Ruling (2026-08-31; final adjudication source = CBO MBR 2026-07 plus the BPC's restatement)**:
1. ✅ **The range in §2.4 is confirmed by an independent source**: citing CBO's timing-adjusted basis, the BPC puts **adjusted Medicare at +9% for July alone**; CRFB reports total July outlays at +$135B unadjusted but only +$37B adjusted (i.e. about $98B was shifted that month, including Medicare as well as military pay, veterans' benefits and others) — **"about +8~10% adjusted" stands**;
2. ✅ **The same-basis check on interest (the self-check flagged at the end of this section)**: **net interest is not among the shifted payment categories** (CBO's MBR shift adjustment covers whole monthly benefit payments; interest follows each security's own coupon calendar and has nothing to do with the 8/1 weekend) — **the headline "net interest +10.8% vs net receipts +3.2% = 3.4×" is unaffected by this artefact and stands**. Both compared growth rates are now confirmed to be on the same unshifted basis, so the comparison is valid;
3. **The true ranking after adjustment**: on the adjusted measure, **interest is again (or jointly) the fastest-deteriorating line of spending** — which *strengthens* §2's central claim that compounding has taken over; "Medicare is faster than interest" was a counter-example manufactured by the payment calendar.

---

## 3. The dollar: the devaluation happened in 2025; 2026 is "debasement trade" and "reserve resilience" at the same time

### 3.1 The exchange rate

- **DXY**: **-10.8% in H1 2025, the worst first half since 1973**; about -9.4~-9.7% for the full year, closing near 98. **2026 is stabilisation, not continued decline**: a 95.5-101.5 range, 99.1-99.9 at the end of August, roughly +1.4% YTD; 🔄 **09-07 refresh: DXY 99.13, a one-month range of 98.80-100.01 — during the global rate shock in §7.4 the dollar did NOT strengthen, which supports reading that episode as globally synchronised rather than a US-credit event**;
- ✅ **USDCNY 6.72 confirmed at source** (Fed H.10, daily 08-17 to 08-21: 6.7399 → 6.7210): the renminbi has appreciated about **7.9% in two years** from 7.26-7.27 in 2024-07. The driver is not speculation: **a goods surplus above $1T a year plus roughly $37bn a month of exporters' accumulated dollars being converted**; **the PBOC has been tapping the brakes with a weaker-than-expected fix since 2025-11** — the wheel is turned the other way (a complete reversal from "defend 7.3 against depreciation" in 2019-2024). Institutional forecasts cluster at 6.70-6.80 for end-2026;
- ⚠ A data-capture lesson, on the record: the H.10 history page `dat00_ch.htm` produced a false reading ("7.28" with a Saturday date) when read through a summarising model; it was discarded in favour of the current release page — **even two pages from the same source must be cross-checked**.

### 3.2 The reserve side: a slow erosion that actually reversed this quarter

- **COFER dollar share, 2026Q1 = 57.13%** (2025Q4 56.42%, **up quarter on quarter**; the IMF attributes about half of that to the valuation effect of a modestly stronger dollar); the ten-year cumulative change is **-8.4pp** (65.5% → 57.1%); the renminbi is only **1.99%**;
- **Central bank gold buying**: 863 tonnes in 2025 (the lowest since 2021, still the fourth highest on record); 244 tonnes net in 2026Q1 (the fastest in a year);
- **Gold in 2026 was a roller-coaster, not a one-way move**: a January blow-off to a record (**intraday $5,586-5,602 / highest close $5,318.40, both on 01-29** — ⚠ the extreme is marked on two measures, cross-checked against `GC=F` at source) (+29.5% for the month) → **-11~12% in a single day on 01-30** (the worst day since the early 1980s; silver fell a record 26% the same day) → a July low of $3,986 (**the `GC=F` continuous series close on 2026-07-16, when the August contract was front month; on the December-contract basis the equivalent is 4,048.70, on the GLD basis 364.96** — two independent paths differing by 0.1pp) → an August rebound to $4,647 (+15~19%, the strongest month since 1999-09). ⚠ **August was not a new high — the record is still January** (which closes the earlier open question of a suspected all-time high: the level was $4,600-4,660 and the ATH remains January); ⚠ **the gold figures in this bullet are on a narrative basis (spot and continuous futures mixed) and are not used as an input to any criterion** — a criterion-grade citation must be pinned to a single contract (the continuous `GC=F` produces a 1%+ non-price step at every roll, demonstrated 08-30);
- **TIC flows**: through H1 2026 foreign investors were **consistently net buyers of US long-term securities, private-led**; the official sector (China in particular) was a seller.

### 3.3 The failure of the "dollar smile" is conditional

After the "Sell America" week of 2025-04 (10Y +50bp in a week, DXY at a three-year low, equities/bonds/currency down together), the BIS found empirically that **the safe-haven correlation between Treasuries and the VIX has been close to zero since 2025-04, while Bunds held up** — **the failure occurs only when the United States is itself the source of risk**, a condition that still held intermittently in 2026 (on the August Iran-sanctions risk-off day the dollar actually weakened).

**⚠ Ruling on measures (so that two chapters cannot each take the half they like)**: "DXY stabilised in 2026" (annual scale) and "a three-month low in late August" (weekly scale, the week of Warsh's speech and the fiscal intervention) **coexist without contradiction** — any citation must carry the time scale.

---

## 4. The petrodollar: an agreement that never existed, and a funeral running ahead of the data

### 4.1 The claim, dismantled: "the 50-year US-Saudi petrodollar agreement expired on 2024-06-09" — ❌ fiction (✅ confirmed by adversarial verification)

- **No formal agreement requiring Saudi Arabia to sell oil in dollars has ever existed.** What actually existed in 1974 was: (a) the Kissinger-Fahd **joint statement** of 06-08 establishing the US-Saudi Joint Economic Commission (JECOR); (b) a **non-treaty, secret arrangement** reached during Treasury Secretary Simon's July visit — arms sales and security guarantees in exchange for Saudi oil revenue buying Treasuries through an off-market "add-on" channel (Faisal demanded strict secrecy, and the Treasury did not break out Saudi holdings separately until a **Bloomberg FOIA request in 2016**);
- **The only formal document that had an expiry (a technical cooperation agreement) was terminated on 2000-02-12** — "expiring in 2024" does not even match on the year; GAO officials confirmed there is **no oil-for-dollars clause** in the commission's documents (RFA fact check, 2024-07);
- 📌 **Filed under the error family "a number passed along, subject never checked"**: the thing said to be "expiring" is an agreement that does not exist. Saudi Arabia's decades of all-dollar oil sales are a **behavioural convention, not a legal obligation** — and that substitution is precisely what the story smuggles in.

### 4.2 De-dollarisation in practice: every line has to be split into "announced" vs "actually landed"

| Indicator | Data | Reading |
|---|---|---|
| **BIS Triennial Survey (2025-04 data)** | the dollar is on one side of **89.2%** of FX turnover, **up** from 88.4% in 2022 ✅ primary | As a medium of exchange, de-dollarisation is **not in evidence** |
| Oil trade settled in dollars | still about **80%** (JPM estimate, 2023; the 20% non-dollar share is already a multi-decade high) | Mostly sanctioned Russian and Iranian trade, not a voluntary switch |
| Saudi settlement in renminbi | as of 2026-08, **not one cargo has been found**; only a RMB 50bn central-bank swap line from 2023-11; Aramco's CEO called the reports "speculation" | **Announced ≠ landed** |
| Russia | "rouble-isation", not "renminbi-isation": the renminbi share of export settlement **halved from a peak near 50% to 25.7%** (2025-09), while the rouble rose to 59.6% | The **opposite** of the mainstream story |
| India buying Russian oil | mostly in **UAE dirhams** (pegged to the dollar = economically quasi-dollar settlement) plus some rupees; renminbi about 10% | Discount the de-dollarisation content accordingly |
| SWIFT renminbi share | 2026-06: **3.10% on the all-currency basis (5th) / 2.38% excluding intra-euro-area (6th)** (⚠ the 2.18% that circulates in second-hand accounts was checked against SWIFT's own PDF and **does not exist on either basis**; versus the 2023-11 peak of 4.6% this is a fall of **about a third**, not "more than half"); CIPS volumes at a record (RMB 180tn a year) | The divergence between the two indicators still holds but is narrower = part of renminbi flow **bypasses SWIFT messaging**; ⚠ SWIFT publishes two tables under the same name — always cite which basis |
| mBridge | about **$55.5bn** cumulatively over four years, **95% of it e-CNY**; the BIS exited in 2024-10 | **Three orders of magnitude** below CIPS's $25tn a year; putting them side by side is a magnitude error |
| **The counter-trend: stablecoins** | dollar stablecoins at about **$308-310bn** (2026-08, slightly below the year's peak); the GENIUS Act mandates 1:1 cash + short-bill reserves; **Tether's total Treasury exposure is about $141bn ≈ the 17th largest holder in the world if it were a sovereign** ⚠ self-reported attestation basis | **"De-dollarisation" and "stablecoin re-dollarisation" are happening at the same time** |

**Reading**: the petrodollar's anchor was never that non-existent agreement. It is three things — **the arms-and-security exchange, the depth of the Treasury market, and network effects**. The real erosion is a slow variable (an 8.4pp fall in reserve share over a decade, central-bank gold buying) moving on a **decadal** timescale; telling that slow variable as "the agreement expires and it collapses" is the signature narrative error of this field.

---

## 5. A taxonomy of historical resolutions: how high debt has actually come down

### 5.1 The post-war United States: "growing out of the debt" is mostly a myth (✅ NBER paper, full text extracted locally)

Debt/GDP fell from a FY1946 peak of 106% to 23% in FY1974, a total of **-83pp**. The Acalin-Ball decomposition (NBER WP 31577):

| Contribution | Size | Nature |
|---|---|---|
| r−g, total | **-48pp** | of which **only 12pp comes from undistorted real growth (r*−g)** |
| — rate distortion (surprise inflation + the pre-1951 rate peg) | **-36pp** | **financial repression** |
| Primary surpluses | -30pp | post-war austerity (year-by-year basis; the counterfactual-scenario basis gives 17pp — the two must not be mixed) |

**The counterfactual**: with no surpluses and no rate distortion, on growth alone — **debt/GDP would still have been 84% in 2022**, i.e. 76 years of natural deleveraging worth only 22pp.

### 5.2 The "liquidation tax" of financial repression (🔶 revised to the published version's basis)

Reinhart-Sbrancia: between 1945 and 1980, **years with a negative real rate accounted for 50% of the time in the US and 60% in the UK**; the average annual "liquidation tax" collected through negative real rates was about **2-3% of GDP (20-30pp of debt/GDP over a decade)**. The key insight: **inflation does not have to be high, and does not have to be entirely unexpected — moderate inflation plus a rate cap is enough.** The prototype tool: the Fed's 1942-1951 yield peg (30-year ≤2.5%), with CPI averaging 7.1% over 1947-51.

### 5.3 Britain: losing reserve-currency status was *managed* into a 30-year slow process

- Sterling's share of global reserves fell from **80%+** after the war to **<10%** by the mid-1970s — about 30 years; debt fell from 270% of GDP to 50% **while the budget was on average still in deficit** — entirely on nominal growth, inflation and repression;
- **The holders paid**: the 14.3% devaluation of 1967-11 **was not disclosed in advance to sterling-area members** (Kuwait's single-event loss was about 5.89% of its GDP); the **1968 Basel agreement** gave Britain's official sterling holders a 90% dollar-value guarantee in exchange for a commitment to a *minimum sterling share* that barred them from reducing holdings — **financial repression in its cross-border form: the exit was closed before the crisis, not after**;
- **What that implies for today's Treasury holders**: historically, creditors of a reserve-currency issuer are not defaulted on — they are **locked in and then taxed**.

### 5.4 Japan as a control case: why 260% has not blown up, and where its breakpoint is

The BoJ holds 47.9% of JGBs (2026-03); but after the exit from YCC, the 30Y jumped 42bp in two days in 2026-01 to **a record 3.91% (intraday; 3.89% on a closing basis)**, and the June and August tenders were consecutively weak. ⚠ **The common claim that "JGBs are all held domestically" no longer holds at the short end: foreign investors hold 55.6% of T-bills** — the roll depends on foreign money, which is the potential channel from turbulence to a liquidity crisis. ⚠ Japan's debt/GDP is quoted on two bases, 256% and 235-237%; this report does not adjudicate between them and does not cite either alone.

### 5.5 The remaining precedents, one line each

- **Nixon closing the gold window, 1971**: a unilateral abrogation of the convertibility promise made to foreign central banks (most of the literature calls it a "technical default" or a rule rewrite); CPI subsequently ran 11.0% in 1974 and 13.5% in 1980;
- **The Plaza Accord, 1985**: the three preconditions for coordinated devaluation (allied official holdings + a tradition of fixed intervention + concentrated holdings) are **all absent today** (China and the Gulf are not allies, holdings are concentrated in private hands, central banks do not intervene routinely) — a "Mar-a-Lago Accord" style coordinated devaluation is highly improbable (TD, ING and the Atlantic Council concur);
- **Reinhart-Rogoff**: of the 26 episodes since 1800 in which an advanced economy's debt/GDP exceeded 90%, 20 lasted more than a decade, **averaging 23 years**; the dominant historical resolution for large domestic-currency debt is **inflation, repression, and mixtures of the two** — "growing out of it quickly" is the rare case.

### 5.6 🔴 The critical joint: one part of the 1946 playbook cannot be reproduced today — which is why §6 exists

**The historical playbook, in which 36pp came from "surprise inflation + a rate peg", is discounted directly by the debt structure documented in §1 of this report**: the 1946 stock was **long-duration, fixed-rate, with no TIPS and with capital controls** — inflation could burn it away slowly. Today **bills are 22.2%, 33% matures within 12 months, TIPS are $2.15T and capital moves freely** — surprise inflation is **repriced away by a third of the stock within a year**, and the tax base shrinks sharply.

⇒ **For financial repression to be reproduced in 2026, the "creditors will run" problem has to be solved first: either lock in long duration again, or manufacture price-insensitive captive buyers.** The latter is exactly what was legislated into existence in 2025-2026 (§6). **The other side of front-loading**: the repression tax base shifts from "long-bond holders" to "short-bill rollers plus everyone who bears the inflation" — **a lower rate on a wider base, and politically far more invisible**.

---

## 6. The exit being assembled: short-end demand engineering (2026, as it stands)

### 6.1 The three-piece set (all in force — none of this is conceptual)

| Tool | Status | Effect |
|---|---|---|
| **GENIUS Act** (signed 2025-07-18) | ✅ law; Treasury NPRM out for comment 2026-08-17 | Payment stablecoins must **hold cash + ≤93-day T-bills 1:1 by statute**; new T-bill demand by 2030 estimated at **$0.4-2.3T** (⚠ an extremely wide range, and much of it may be nothing more than money moving out of money funds and deposits — net new demand is doubtful, a reservation the original research already made). **This is the sterling area's "minimum share" commitment for the digital age**: a statutory, price-insensitive buyer of short bills |
| **eSLR recalibration** (finalised 2025-11-25, effective 2026-04-01) | ✅ permanent rule | GSIB leverage buffer 6% → about 4-5%; ⚠ **the "Treasuries excluded from the denominator" that the market widely expected in 2025 did not happen** — the capacity released is far less than the optimistic case, which lines up in time with the long-end buyers' strike since late June |
| **The Fed buying bills again** (QT ended 2025-12-01) | ✅ **ongoing (re-checked 09-07, still true)** | "Reserve management purchases": +$346B of bills in nine months — in practice absorbing a substantial share of the Treasury's increased bill issuance. 🔄 **Refresh: H.4.1 Treasury holdings $4,519.7B on 07-29 → $4,552.3B on 09-02, +$32.7B over five weeks (about +$6.5B/week); the pace has not stopped** ✅ FRED `TREAST` |

### 6.1b Decomposing the three tools: they do not act on the same axis, so split the axes before quoting percentages

**One is a pump (flow), one is a lock (stock + an option), one is a sluice gate (capacity) — only what sits on the same axis can be compared.**

**Axis one: realised incremental absorption (aligned window: QT ending 2025-12-01 → 2026-08-30, nine months):**

| Tool | Realised increment in that window | Share |
|---|---:|---:|
| 🔴 **Fed reserve management purchases** | **+$346B** (H.4.1, the figure in §6.1) | **≈ 99%** |
| **GENIUS / stablecoins** | **+$3.9B** (total stablecoins $305.5B → $309.4B; measured on DefiLlama, third-party basis) | 🔴 **≈ 1%** |
| **eSLR** | direct purchases are $0 by definition (it buys nothing); **the indirect effect through the banking channel cannot be attributed and therefore cannot be measured** (changes in bank Treasury holdings cannot be separated into an eSLR component) | **excluded from the percentages** (🔴 ruling: "cannot be attributed" must not be written as "measured at 0%" — not measured ≠ measured as zero) |

⚠ The stablecoin increment uses the change in total supply as a proxy for its bill purchases, which is an **upper bound** (reserves are not 100% bills).

**Axis two: locking the stock (GENIUS's real form of force)** — it welds the reserve composition of the existing **~$309B** pool to "cash + ≤93-day T-bills" (largely true before the law as well; **the statute turns a convention into something irreversible**). For scale: **the Fed's nine-month increment ($346B) on its own equals 112% of the entire stablecoin pool** ⇒ as a buyer of short bills, stablecoins' **stock position is real, their incremental position is currently negligible**.

**Axis three: future flow (an option, not a present value)** — GENIUS's $0.4-2.3T (by 2030, as cited in §6.1; a very wide range with doubtful net-new content) vs the Fed's ≈$460B annualised if the pace holds (policy-set). ⇒ **The only member of the three-piece set that could overtake on the future axis is GENIUS, but on measured data (stablecoin supply +9.8% y/y and negative over 90 days) that option is currently out of the money.**

**eSLR: a sluice gate is not a pump, and there is no percentage to give it** — it relaxes a constraint on holding Treasuries, permits buying, and produces none; §6.1 already records that the capacity released was far below expectations ("Treasuries out of the denominator" never happened). ⚠ Ruling on wording: **no empirical reading of eSLR can be given for this window** — direct purchases are zero by definition, and the indirect channel (bank purchases) exists in the data but cannot be attributed. "≈0" may be stated as a definition and must not be stated as a measurement. "Below the story told at the time of legislation" stands (§6.1 provides primary evidence).

> **Synthesis: the three tools are "in force" in three different senses — the Fed is in force as money (99% of the present-day force), GENIUS is in force as law (locking a $309B stock plus one wide-ranged, out-of-the-money option), and eSLR is in force as a rule (which did not release the water it was expected to).**
> ⚠ **Guard against misreading: outside the three-piece set, the genuinely second-largest marginal buyer is money market funds ($3,426B, the table in §1.3)** — a three-tool narrative that pushes them out of view will overstate how much of total demand is "engineered".

### 6.2 A quasi-YCC on the fiscal side: the first hand of intervention is not the Fed's, it is the Treasury's

- 🔴 **On 08-19 the Treasury announced it was doubling each long-end buyback operation ($2B→$4B, 09-09 ~ 11-04)** — **🔄 status as of 09-07: the first doubled operation is on 09-09, this Wednesday, and has not yet run ⇒ from this week this line moves from "announced" to "observable"** — the textbook crisis script (Fed twist or QE first) is inverted. The 30Y fell 9bp that day and **recovered the entire move within 24 hours** (⚠ n=1; not enough to extrapolate that fiscal-side intervention is doomed to fail); Bessent described it as "partly a signal";
- The Treasury has already bought back **$202B** in the first three quarters of FY2026 (far more than the widely held impression of a "small 2024 pilot") — this is now routine market-function support;
- **The TGA has been built up to about $950B-1.05T**; "drawing on ~$1T of the TGA to support buybacks" remains a **rumour** (CNBC, anonymous sources, never officially announced — registered as trigger T5 in §8);
- TBAC warned on 08-05 that, at current auction sizes, there is a **$1.45T financing gap in FY2027-28** (⚠ single source: Fortune relaying TBAC minutes; the minutes themselves have not been seen — **this figure is one of the four anchors of the 2027-28 window in §8; downgrading it weakens that window, and it is registered as pending verification**).

### 6.3 🔴 The authorities pulling against each other, at the two ends of the curve

**In the same week**: Fed Chair Warsh (Jackson Hole debut, 08-28, ✅ official transcript) took **headline PCE at 3.7% / 4.1% annualised over six months** as his central indicator, said there was "more work to do", hinted at a possible **hike**, narrowed forward guidance, and **avoided the balance sheet and fiscal questions entirely**; Treasury Secretary Bessent ran a watered-down Operation Twist at the long end. ⇒ **The monetary authority is pushing rates up while the fiscal authority pushes them down** — CNBC ran it under the headline that Warsh faces an independence test while Bessent encroaches on the central bank's turf.

Three ironies, which together make the 2026 rate path the largest uncertainty on the board:
1. Warsh was nominated on an expectation of *cuts* (confirmed 54-45, the narrowest in the modern era) and turned hawkish within three months;
2. Warsh was, in 2025, the advocate of a "new Treasury-Fed accord" — and is now pulling against the Treasury;
3. The positions in the ATI (activist issuance) debate have fully reversed: Bessent amplified the criticism of Yellen's "use bills to suppress the long end" in 2024, and by 2026 Bloomberg was calling him the most interventionist Treasury Secretary in decades.

### 6.4 Verdict

**The exit is being assembled**: compulsory and semi-compulsory short-bill buyers (stablecoins + MMFs + the Fed + banks) + price intervention on the fiscal side + long-end buybacks. **The missing part is locking in a negative real rate** — which needs "a rate cap plus 3%+ inflation", and Warsh is doing the opposite. ⇒ **The machinery of Financial Repression 2.0 is in place; the ignition switch (monetary cooperation) has not been pressed. That "assembled but not ignited" state is the root of every disagreement in current asset pricing**: gold prices "it will eventually be ignited", the long end prices "the standoff before ignition", equities price "nominal growth during the standoff".

- The "Mar-a-Lago Accord" (century bonds / gold revaluation / coerced debt swaps): **zero implementation at the conceptual level** — gold is still carried at $42.22/oz and there are no century bonds; **everything that has actually landed is a functional substitute**.

---

## 6b. The mechanism in detail: how "Financial Repression 2.0" collects its tax — a machine that is built but not ignited

> (This chapter unpacks the mechanism behind the conclusions of §5-§6; it introduces no new data, and every figure comes from earlier sections and has been adversarially verified.)

### 6.2.1 The original playbook: how the 1946-1980 "liquidation tax" was actually collected

Debt/GDP fell from 106% to 23% after the war. The popular story is "growth", but the decomposition (§5.1, ✅ NBER, primary) is: **real growth contributed only 12pp, fiscal surpluses 30pp, and "surprise inflation + the rate peg" 36pp — financial repression is the single largest item.**

The mechanism: **from 1942 to 1951 the Fed pegged long rates below 2.5% while CPI averaged 7.1%** (⚠ the 7.1% is the five-year FY1947-51 figure, not an average over 1946-1980 — the full-period compound rate is about 4.4% (CPI 1946→1980) and extremely uneven, see §6.2.1b; there was also no PCE measure at the time, the yardstick is CPI) — bondholders lost 4-5 points a year in real terms, and that loss *is* the write-down of the government's debt. Reinhart and Sbrancia call it a "liquidation tax": in **half of all years** between 1945 and 1980 the real rate on US government debt was negative, liquidating debt worth about **2-3% of GDP** a year (§5.2, revised basis).

**Three points**: ① **hyperinflation is not required** — moderate inflation plus a rate cap suffices; ② **no default is required** — creditors are made whole in nominal terms to the cent; ③ **it is politically invisible** — no tax bill, no default headline, just the everyday experience of "savings not keeping up with prices", with no identifiable culprit. **Its political cost is the lowest available, which is exactly why it is the dominant historical resolution for high debt** (§5.5, the R-R taxonomy).

### 6.2.1b The follow-up question: in the original playbook, how was high inflation *sustained*? Four walls — and an ending in which the playbook went bankrupt

> (The institutional history in this section is widely accepted record and is marked as such; where it connects to earlier figures, verified values are used.)

**First, correct the measure**: CPI over 1946-1980 compounds at only about **4.4%** a year (index compounding 1946→1980; the arithmetic mean is slightly higher because of the high-inflation years), and it is extremely uneven — **three pulses rather than a sustained high**: ① the 1946-48 removal of price controls (peaking near 14%, with deflation in 1949); ② the Korean War in 1950-51 (~9%); **between them, 1952-65 averaged only 1-2%**; ③ the great inflation of 1966-1980 (11.0% in 1974, 13.5% in 1980). ⇒ **The right question is therefore not "how was 7% sustained" but "why did surprise inflation succeed again and again while creditors failed to defend themselves for 35 years".**

**Four walls: why creditors had nowhere to go (historical record)**

| # | Wall | Content |
|---|---|---|
| ① | **Rates sealed by regulation** | the Fed pegged directly in 1942-51; even after the 1951 Accord, **Regulation Q** capped deposit rates (into the 1980s), and money market funds were not invented until 1971 — deposit rates were held down by a statutory ceiling (2-5.5% depending on the era; a 5.25% cap against 13% inflation in the late 1970s), and **savers had no legal alternative** |
| ② | **Capital controls + gold illegal** | Bretton Woods controlled cross-border capital; **private gold ownership was illegal in the US from 1933 to 1974** — both escape doors, foreign-currency assets and gold, were welded shut |
| ③ | **No TIPS, no floaters** | creditors did not even have an instrument with which to demand inflation compensation; only fixed-rate nominal bonds existed |
| ④ | **Creditors were politically weak** | memories of the Depression made full employment override everything (the Employment Act of 1946); unions were strong, savers were dispersed, and nobody spoke for "rentiers" |

**⇒ These four walls are the entire content of §5.6's "creditors cannot run": high inflation could be *sustained* not because the public liked it, but because disliking it made no difference.**

**🔴 One layer deeper: surprise inflation is a consumable — and the playbook did eventually go bankrupt.** Repression works through **expectations lagging reality** (adaptive expectations): each wave of inflation arrived with bond buyers under-compensated, the ex-post real rate was negative, and each "surprise" collected the tax once. **But every use educates the creditor.** By the late 1970s expectations had caught up: long yields went to double digits, nobody would buy fixed-rate long bonds, and a wage-price spiral formed — **the "surprise" was no longer surprising, the liquidation tax could no longer be collected, and all that remained was the damage from inflation itself**. The end point was Volcker taking rates to 19% in 1980-81 and beating expectations back down with a deep recession. ⇒ **1946-1980 lasted three decades because it was the first large-scale use and all four walls were intact; once expectations adapted, the same playbook has never worked in its original form again.** (This is the mirror of point 2 in §6.2.4b: **every use educates the creditors.**)

**Three implications for today**:
1. **Not one of the four walls exists today** (Reg Q repealed, capital free, gold legal, TIPS available) ⇒ any replica has to **build new walls first** — statutory stablecoin bill-holding, eSLR — which is why the parts come in the order set out in §6.2.2;
2. **This time the creditors have taken the course** — everyone has read the 1970s textbook, so expectations will adapt far faster than last time ⇒ even if Repression 2.0 is ignited, **the liquidation tax per unit of time will most likely be below the original's 2-3% of GDP a year**, requiring either more time or stronger lock-in (⚠ mechanism inference, not a calculation);
3. This explains why the original could tolerate 7% pulses while today's Fed is nervous at 3.7%: **the original squandered "surprise" against unsophisticated expectations behind four intact walls; today's Fed defends a 2% anchor with sharp expectations and no walls at all** — and once the anchor goes, the market's retaliation is ten times faster than in the 1970s (§3.3, the "Sell America" week: the 10Y rose 50bp in one week in 2025-04, the largest weekly move since 2001).

**In one line**: it is not that the United States *can* sustain high inflation for long. It is that **creditors were institutionally locked in, and took 30 years to learn to defend themselves; once they had, that playbook never worked in its original form again.**

### 6.2.2 The part a replica has to build first: buyers who cannot run

The original had one precondition: **creditors could not run** (long-duration lock-in + no TIPS + capital controls). None of the three exists today (§5.6: bills 22.2%, 33% maturing within 12 months, TIPS $2.15T) — **surprise inflation is eaten by the repricing of a third of the stock within a year, and the tax base shrinks sharply**. So the first step of a replica is not to push rates down; it is to **manufacture price-insensitive compulsory demand**. Every piece that landed in 2025-2026 does exactly that:

| The modern part (§6.1-6.2, all in force) | What it replicates |
|---|---|
| **GENIUS Act**: stablecoins must hold cash + short bills 1:1 by statute | **A statutory captive buyer** — buying USDT is indirectly buying Treasuries, regardless of the rate. The digital version of the 1968 Basel agreement locking in sterling-area holders (a "minimum sterling share") |
| **eSLR relaxation** (effective 2026-04) | regulation steering banks into Treasuries |
| **The Fed's "reserve management purchases"**: +$346B of bills in nine months | the central bank absorbing supply — the original rate peg ran on exactly this, the Fed buying without limit |
| **The Treasury doubling long-end buybacks** (08-19) | **the act of pushing rates down itself** — except the first hand is now the Treasury's, and the force is still weak |

### 6.2.3 The missing part: a negative real rate — the line between the machine idling and the machine firing

Having the parts ≠ having output. The moment financial repression actually *collects* is when **the rate is below inflation**. Right now it is precisely the opposite:

| | Rate | Inflation | Real rate |
|---|---|---|---|
| Policy end | fed funds 3.50-3.75% | core PCE 3.34% | **about +0.2~0.4% (positive)** |
| Long end | 30Y 5.2-5.3% | as above | **about +1.9% (clearly positive)** |

**Creditors are not being taxed right now — they are earning a positive return. The machine is idling while the debt keeps growing.** Ignition requires "inflation around 3% with the rate pressed below it".

Which is the deeper meaning of §6.3's "authorities pulling against each other": **Warsh is pouring water into the fuel tank** — his 08-28 debut hinted at a hike on headline PCE of 3.7%, and that day the nominal rate rose 5bp while breakevens fell 2bp, so **the real rate rose 7bp** (derived from the identity, verified against a two-day 0bp residual) — one speech pushed ignition one step further away. In the same week the Treasury was pushing the long end the other way. **What the monetary and fiscal authorities are fighting over is, in substance, control of this machine's ignition.**

### 6.2.4 Four paths to ignition, and why the trigger is T6

When does it ignite? **① inflation rises above the rate on its own** (the Fed only has to stand still); **② the Fed changes stance** (forced by a crisis — the end point of scenario B in §7 — or forced politically; Warsh's nomination logic and his behaviour have already diverged once, and a further reversal is not unimaginable); **③ nominal rates are capped administratively** (YCC-type, with the 1942-1951 precedent); **④ central-bank independence is eroded by the Fed's own financial predicament** (see below). All four converge on the same observable: **core PCE > the fed funds rate**. That is why **T6** is registered in §8.3 — **it is not one more macro indicator, it is the mechanical signal that repression has started work and that holders of dollar cash and long bonds have begun paying the tax.**

#### 6.2.4c The fourth path: the Fed's losses are not a fiscal black hole, they are a political soft spot

**First, switch off a mistaken worry: the Fed's losses will not become "the next multi-trillion black hole" — they are not on the same scale as the debt, and they are self-limiting.**

| | Fed losses | Federal debt |
|---|---|---|
| Denominator | **$3-3.5T of interest-bearing liabilities** (reserves + reverse repo), not $40T | a $40.08T stock |
| Annual magnitude | a negative spread of about 1.5-1.8pp ⇒ **$50-110bn a year** (measured peak -$113.5bn in 2023) | net interest of $970bn a year, and compounding |
| Direction | 🔴 **self-limiting**: ① old low-coupon paper matures into 4%+ (the asset side repairs itself) ② each 1pp of cuts saves about $32bn ③ QT has already shrunk the balance sheet by 25% (a smaller base) | 🔴 **self-reinforcing**: the stock grows, interest compounds, the deficit adds $2.1T a year |
| Measured | deterioration -113.5 → -83.7 → -27.5 → **+9.2bn (positive in 2026)**, **the peak has passed** | §2.3: the deterioration is almost entirely interest-driven |

⇒ **To lose "trillions" would require a negative spread above 10pp sustained, i.e. a policy rate of 12%+ — at which point this is no longer a fiscal problem but a hyperinflation problem, and the Fed's losses are a symptom rather than a cause** (discussing them would be discussing the thermometer). **§2's central claim is unchanged: what is unsustainable is the fiscal side, not the central bank side.**

**🔴 But the real risk is not accounting, it is politics — and that is the fourth path to ignition:**

> **A central bank with negative net worth that has remitted nothing to the Treasury for years is politically indefensible.**

The attack writes itself, and is hard to rebut: "*the Fed pays banks hundreds of billions a year in interest on reserves, has gone to negative net worth doing it, and gives the taxpayer nothing.*" And the "solution" it points to is precisely **weakening central-bank independence** — capping IORB (interest on reserves), demanding a congressional audit, moving part of the balance-sheet decision to the Treasury.

⚠ **The report already contains the set-up**: **Warsh himself advocated a "new Treasury-Fed accord" in 2025**, arguing for something modelled on the 1951 Accord that would give the Treasury more say over major balance-sheet decisions (recorded in §6.3). ⇒ **The Fed's financial predicament is the best available ammunition for exactly that argument**; and the table in §1.2 quantifies the ammunition: **remittances to zero from 2022, cumulative -$233.5bn.**

**⇒ The mechanism of this fourth path differs fundamentally from the first three**:
- ①②③ have the **Fed deciding, or being forced to decide**, to ignite;
- ④ has the **Fed weakened to the point where it cannot refuse** — **not a voluntary turn, but the loss of the ability to say no**. This is also the path most compatible with point 5 of §6.2.4b ("this tax can only be collected if nobody signs for it"): **institutional weakening requires nobody to announce ignition at all.**

**⇒ The thing to monitor is therefore not the size of the loss but what the loss gets used for** (registered as a leading observation for T6, not as a separate trigger — legislative initiatives have no mechanical threshold): **whether bills appear that would cap IORB, audit the Fed, or rewrite the central bank-Treasury relationship**. ⚠ Per this report's discipline, that item is a **qualitative observation** and must not be written as an adjudicable trigger; its adjudicable downstream remains T6.

### 6.2.4b The follow-up question: why the Fed will not cooperate with ignition — five reasons, and the possibility that the conflict is not a fault but the process

> (This section introduces no new data.)

**First, the root of the conflict: the two authorities keep different ledgers on different clocks.** The Treasury's ledger is **this quarter's** — a $2.1T annual deficit, a $1.45T FY27-28 gap (⚠ single source), a third of the stock rolling within twelve months, and **auctions that have to clear every quarter** — hence the pressure on the long end. The Fed's ledger is **the decade's** — its only asset is the market's belief that it will bring inflation back to 2%. **At 2% inflation the two do not conflict; at 3.7% the two mandates collide by construction** — the conflict is not anyone's mistake.

**Five reasons the Fed will not ignite**:

1. **Its statutory mandate is being violated right now**: 3.3-3.7% against a 2% target, with inflation breadth at 54% (32% pre-pandemic). Cutting the rate below inflation at this moment would be publicly signing away the 2% target;
2. 🔴 **Cooperating early is self-defeating — the market front-runs it** (the other side of the §5.6 joint): the repression of 1946-1951 worked because creditors could not run; today capital moves freely, TIPS exist, and a third of the stock reprices within a year — **if the market can see that the real rate is being made negative deliberately, long-bond holders immediately demand a higher term premium ⇒ the long end rises rather than falls, and the low rates repression wants are destroyed by the act of igniting it**. The 24-hour failure of the Treasury's 08-19 buyback intervention is a small-scale rehearsal of exactly that mechanism (⚠ n=1): **price suppression without credibility backing is simply eaten by the market. For financial repression to work, the inflation has to look like an accident, not like a policy**;
3. **Warsh's personal position forces him to overshoot the other way**: nominated on an expectation of cuts (confirmed 54-45, the narrowest chair confirmation **in the modern era**), suspected market-wide of being the White House's man ⇒ **a credibility deficit requires over-collateralisation**. Any step he takes toward the Treasury will be read as confirming fiscal dominance, so the cost is doubled and he must post excess hawkishness as collateral for independence. Add the institutional trauma: Burns yielded to political pressure in the 1970s and produced the great inflation, and **nobody wants to be the second Burns** (Warsh himself was a well-known QE2 sceptic in 2010);
4. **The other half of the machine is not built, so the timing is not ripe**: the captive buyers (the stablecoin $0.4-2.3T is a 2030 estimate; eSLR released less capacity than expected) cannot yet absorb the selling that overt ignition would trigger — ignite now and there is not enough of a bid, the long end goes straight out of control, and **that is scenario B in §7, not repression**;
5. **Political economy: this tax can only be collected if nobody signs for it.** A negative real rate is a tax on savers and pensions, and the only politically viable form of it is one that **looks like an accident** ("inflation was stubborn, the Fed did its best"). A Fed that visibly cooperates in manufacturing negative real rates takes the entire blame; a Fed that "loses to inflation" does not. ⇒ **The equilibrium path is therefore exactly the status quo: the Fed resists until a crisis forces its hand — and at that point cooperation looks like a rescue rather than a conspiracy.** That is the deeper meaning of Rogoff's "action will wait for a major shock to force it", and the reason §8 writes the end point of scenario B as "merging back into the baseline".

**⇒ One layer further: this conflict may not be a fault, it may be the process.** **In a democracy with free capital markets, financial repression can only arrive in the form of an emergency response; it cannot be announced as a policy.** The Fed's present resistance is, objectively, husbanding credibility for future cooperation — **the more credible its resistance, the less the market will read the eventual QE as monetisation when it is forced to act.**

The most ironic footnote: **Warsh was himself the advocate of a "new Treasury-Fed accord" in 2025** — he understands the framework for cooperation and has even designed one. His current hawkishness says exactly this: **whoever understands this machine knows that before ignition you must first perform "I don't want to ignite" until the market believes it.** Which again shows what T6 is worth: **when it fires, whatever the official narrative says, the machine is already running.**

⚠ **Guard against misreading**: points 2, 3 and 5 of this section are mechanism inference (an explanation built on verified facts, not facts themselves), under the same discipline as §4's "announced vs landed" — **a citation must not say "the Fed has decided X", only "the current incentive structure points to X".**

### 6.2.5 This chapter explains every current disagreement in the market

None of the three markets is wrong; they are betting on different moments of the same machine:

- **Gold** prices "it will eventually be ignited" (central-bank buying + expectations of the debasement tax);
- **The long end at 5.3%** prices "the standoff before ignition" (refusing to lend cheaply in an era of positive real rates);
- **Equities** price "nominal growth during the standoff" (nominal GDP is still expanding).

⇒ **Reading discipline**: when watching this machine, do not ask "will rates be cut" (that is a trading question). Ask **"when, and by which path, does the real rate turn negative"** (that is the mechanism question). The former generates noise daily; the latter has exactly one adjudication point, T6.

#### 6.2.5b The follow-up question: why a decade-long equity bull market cannot resolve the debt

**First, concede that the bull market really is paying down debt — through two real channels, and ones the United States uniquely has**: ① **realised capital gains raise federal receipts** (receipts routinely beat forecasts in bull years; 2021 is the classic case); ② **wealth effect → consumption → nominal GDP → the denominator of debt/GDP** — **a channel China essentially lacks** (the mirror of §8.2.2: 30% of US household assets are in equities, 1-2% in China). ⇒ **So the question is not "does the bull market help", it is "why is the help not enough". Three structural reasons**:

**① 🔴 The numerator compounds while the denominator is linear — this is mathematics, not policy.**
The receipts a bull market adds are **linear and one-off** (this year's extra capital-gains tax is gone next year unless markets rise again); interest is **compounding and automatic** (the $40T stock rolls at the prevailing rate and new debt replaces old at higher coupons, **without anyone deciding anything**). **A linear addend cannot catch a compounding multiplier.** The CBO path in §2.3 makes this decisive: **the primary deficit stays around 2% of GDP for the whole projection while the total deficit rises to 9.1% — the deterioration is almost entirely interest.** ⇒ **What a bull market improves is precisely the primary component, and the primary component was never the problem.**

**② The fuel of the bull market is low rates, and low rates are being destroyed by the debt problem.**
A large part of the last decade's bull market was a **denominator move**; and the journey from 0 to 4.7% is precisely the process that kills multiples. One measured tension: **after a large earnings beat NVDA's PE fell to the 0th percentile of its own five-year range, and it still fell 4.6% in a single day on 08-28 (Warsh's hawkish day) — the 0th percentile is no defence against a shock to the denominator.** ⇒ **"Solve the debt with a bull market" is internally contradictory: debt deteriorates → the long end rises → the valuation basis of the bull market is pulled away. You cannot simultaneously assume rates high enough to make the debt a problem and rates low enough for the bull market to continue.**

**③ 🔴 A bull market raises [the stock of wealth]; the fiscal problem needs [a flow of cash].**
US household net worth is long past **$160T** against $40T of debt — **on a "wealth covers debt" view America is rolling in money**. But **the government taxes flows (income and payroll), and appreciation in a stock is only taxed when realised**. Short of a wealth tax (politically impossible), **most of the bull market's stock appreciation never reaches the Treasury at all.**
⇒ **Against the framework of this chapter, this is the crucial point: financial repression is the historically dominant resolution precisely because it is the only instrument that taxes the [stock]** — inflation does not ask whether you realised anything, it dilutes nominal assets directly. **The bull market raises the stock and inflation dilutes the stock — those two are opponents on the same plane; capital gains tax merely scrapes a flow off the edge of the stock.**

**④ History has already answered this once (§5.1, the NBER decomposition)**: the last time the US worked down high debt (106% → 23%), **real growth contributed only 12pp, financial repression 36pp, primary surpluses 30pp**; the counterfactual — with no surpluses and no rate distortion, growth alone — leaves **debt/GDP still at 84% in 2022**. ⇒ **No country has ever grown, or rallied, its way out of high debt.** The bull market's help is real in accounting terms and, in magnitude, is part of that 12pp.

**🔴 ⑤ A reverse angle that deserves more worry: the bull market is also manufacturing part of the problem.**
A bull market makes **the revenue structure more fragile** — the tax base migrates toward financial asset prices (an isomorphic case on the China side: 2026 stamp duty **+99.2%**, personal income tax +14.9%; the US analogue is the same: the larger the capital-gains share, the more procyclical receipts become). ⇒ **When the crisis actually arrives (scenario B in §7), the fiscal position takes two hits at once: rising rates raise interest outlays while falling equities remove capital-gains receipts.** **The "fiscal improvement" of a bull market is borrowed, and the bear market collects with interest.** This played out once in 2000: after the Nasdaq crash federal receipts fell for three consecutive years and the budget flipped from surplus straight to deficit (⚠ widely accepted record; not re-verified item by item here).

> **⇒ In one line: the bull market is paying the small change on the interest bill while the bill itself compounds; it raises untaxed stock wealth while the Treasury needs flow cash; and the low rates it depends on are exactly what the debt problem is destroying.**
> ⚠ **An honest qualification that must not be dropped**: this **does not mean the bull market is irrelevant** — it is one of the reasons the baseline scenario in §8 (~60%) can persist, and **without it the United States might have reached scenario B sooner**. ⇒ **The accurate statement is not "a bull market cannot resolve the crisis" but: a bull market can lengthen the period of muddling through; it cannot change the end state — which is still the debasement tax, arriving later.** Which again confirms the reading discipline of §6.2.5: **watch T6, not the S&P.**

#### 6.2.5c The follow-up question: the US government owns enormous assets — why not sell some to work down the debt

**First, concede that the intuition is right: the US government is the largest single asset holder in the world and is nowhere near "insolvent".**

| Asset | Magnitude | ⚠ Basis |
|---|---|---|
| Federal land | **640 million acres ≈ 28% of the country** | Interior/BLM basis, including unextracted mineral rights |
| Gold | **261 million ounces (about 8,133 tonnes)** | 🔴 carried at **$42.22/oz** = about $11bn on the books; **about $1.1 trillion at market** (the book price is recorded in §6.4) |
| Student loan portfolio | about **$1.6 trillion** receivable | the government is the largest consumer-credit creditor |
| SPR / military bases / buildings / spectrum | hundreds of billions to trillions | a single spectrum auction has raised tens of billions |

⇒ **The problem was never a shortage of assets; it is the nature of the assets. Four gates**:

**① The magnitudes do not match (arithmetic)**: an optimistic sum of what could be sold is **a few trillion dollars**, against $40T of debt, **a $2.1T annual deficit and $970bn of annual net interest**. ⇒ **Even a one-off sale of $3 trillion covers only 1.5 years of deficit, and the debt keeps compounding the year after.** This is the other version of the arithmetic in §6.2.5b: **a one-off receipt (linear) cannot catch compounding (a multiplier) — selling the family silver is a one-dose medicine for a chronic disease.**

**② Politically impossible, and already demonstrated**: every proposal to sell federal land is killed by both parties together (western voters, environmental groups, tribal rights). **Gold revaluation** is technically the easiest — restate the $42.22 at market and the Treasury conjures about **$1.1 trillion** of book equity — **but Bessent explicitly clarified in 2025-02 that "this is not what I meant"** (recorded at source in §6.4), because it **amounts to monetisation by another name** and would damage the dollar-anchor brand he is selling.

**③ 🔴 Selling the asset weakens the power behind the asset — the sharpest difference from a company selling assets**: federal land is not a financial asset, it is **the basis of sovereignty** (military, strategic minerals, energy independence); **8,133 tonnes of gold is not a portfolio, it is the physical backing of the dollar's last line of credibility** — even though it has long been legally inconvertible, **the signalling value of selling it would be catastrophic: it would announce "we need to sell gold to pay our debts"**. ⇒ **For a hegemon the strategic value of an asset far exceeds its book value; selling means trading permanent power for one-off cash.**

**④ Even the accounting improvement is temporary**: a one-off receipt does not change the structure of the primary deficit, and next year's deficit arrives regardless. ⚠ The IMF's finding on emerging-market privatisation: **privatisation receipts unaccompanied by structural fiscal reform see the debt ratio return to where it was within 3-5 years** (⚠ widely accepted; not re-verified item by item here).

**🔴 ⑤ The genuinely counter-intuitive answer: the US does not sell because it has a better tool than selling — the subject of this chapter.**

| | Selling assets | Financial repression (the debasement tax) |
|---|---|---|
| Form of receipt | one-off, capped at a few trillion | **annual, sustainable, uncapped** |
| Political cost | very high (every sale is a fight in Congress) | **close to zero** (nobody signs; §6.2.4b point 5) |
| Cost in power | **permanent surrender of sovereign assets** | none |
| Who bears it | **US taxpayers** (public assets lost) | **holders of dollar claims worldwide** |
| Reversible | no | yes, at any time (bring inflation down) |

⇒ **For a country that can borrow in a currency it prints, "sell assets to repay" is the worst available option.** That is the full meaning of this chapter's thesis: **the resolution of a debt problem is not raising money, it is dilution** — and the cost of dilution falls on **whoever holds your currency**, not on your own citizens and sovereign assets. **What hegemony actually means is not "assets large enough to repay" but "not having to repay — repaying slowly out of the creditor's purchasing power instead".**

> **⇒ In one line: the reason $40 trillion has never provoked a discussion about selling the family silver is that inside the dollar system it was never a debt that had to be repaid out of assets.**
> ⚠ **The feeling that this is "unbelievable" points at a real question, but the subject has to be swapped**: the unbelievable part is not "the hegemon cannot repay $40 trillion" but "**the hegemon can go on not repaying, and the world keeps paying for it**" — and the whole of this report is an inquiry into how long that arrangement can last and in what form it ends (answer: not default, but a debasement tax; the mechanical signal is T6, not the balance sheet).
> 📌 **The clearest contrast**: the countries that genuinely have to sell assets to repay are the ones that **cannot borrow in their own currency** — Greece selling ports and airports in 2010, Argentina selling state enterprises. **The United States has never reached that point, because it always has the dilution option. "Sell assets" is the solution for a country without monetary sovereignty, not for the issuer of the reserve currency.**

### 6.2.6 The objection, and the ruling: creditors have learned to defend themselves — how can a replica work at all? — it replicates the FUNCTION, not the MECHANISM

> (This is the strongest objection to the chapter's thesis. The ruling **refines and quantitatively downgrades** the thesis rather than overturning it. It includes one primary verification: the GENIUS Act's interest ban.)

**The part of the objection that holds**: §6.2.1b already established it — surprise inflation is a consumable, and once creditors spent 30 years learning to defend themselves the original playbook never worked in its original form again. **If "replica" means the original mechanism, the word does not apply.**

**Ruling: what is replicated is the FUNCTION (transferring real resources from dollar creditors to the sovereign without a default and without legislating a tax), not the MECHANISM (surprise inflation × locked-in long-bond holders). The new machine is designed on the premise that creditors have already learned to defend themselves.**

**(1) The creditors' counter-move not only exists — the whole of §3 is a record of it in progress**: the long end at 5.3% with the term premium at **0.678→0.875** (✅ NY Fed ACM `THREEFYTP10`) (free investors demanding compensation), the dollar -10% in 2025 with 863 tonnes of central-bank gold buying (cross-border creditors voting with their feet), Japan cutting $123B in four months. ⇒ **Bond vigilantes are not an obstacle to Repression 2.0, they are its boundary condition** — which is why the new machine **does not intend to tax free long-bond investors at all**, and is the deeper reason issuance is being pushed to the short end (bills 22.2%): **the tax is levied only where there is a captive population.**

**(2) The new tax base: three groups that cannot run even having learned.** The original's walls locked in *information* (you didn't see it coming); the new walls lock in **identity and use** (you can see it and still cannot leave):

| # | Tax base | Why the counter-move fails |
|---|---|---|
| ① | **Holders of money** (the most important) | ✅ **the GENIUS Act expressly forbids issuers from paying stablecoin holders any interest or yield** (§4(a)(11); **the proposed anti-circumvention rule, verified at source with its limits, is in §6.2.6b**) — the issuer takes about a 3.8% spread (matching the bill rates in §1) and the holder is barred by statute from receiving any; at 3% inflation the real tax rate is -3%, **fully knowable in advance and collectable anyway**, because the motive for holding is use (payments, quote currency, dollarised savings) rather than yield. **This is the ancient logic of seigniorage: for monetary assets, a negative real rate does not require a surprise** |
| ② | **Fiduciary and regulated institutions** | MMF charters restrict them to short paper, banks are pinned by liquidity regulation, pension funds are locked by duration rules, foreign central banks must hold for exchange-rate management — **the constraint is law and charter, not information. Learning defeats a surprise; it does not defeat a mandate. That is what the table in §6.2.2 actually means: the new walls do not block your view, they block your legs** |
| ③ | **Dollar debtors** | anyone holding dollar-denominated debt, trade or contracts, for whom dollar assets are a liability hedge; running away means creating a currency mismatch. **As long as the dollar is the unit of account (BIS: 89.2%), this tax base exists** |

**(3) Two modern demonstrations: having learned ≠ being able to leave**
- **Japan 2013-2024 is an existence proof of repression working in the post-learning era**: capital is free and everyone has read the textbook, and the BoJ pinned rates at zero anyway; inflation ran 2-4% in 2022-24 with deeply negative real rates, and creditors largely did not leave (home bias + mandates). The liquidation tax was collected for a decade. ⚠ **The pressure escaped through the exchange rate instead**: the yen fell about 40% — **in a world of free capital the escape valves from repression are the currency and gold, which is exactly what the dollar's -10% and the gold price in §3 mean**; the dollar's reserve status makes that valve tighter (escape into which larger pool?);
- **The US 2022-2024 demonstrated how slow depositors are**: the Fed went to 5% and trillions of deposits sat still at 0.5% — **"creditors have learned to defend themselves" is true at the institutional level and still only half true at the household level**;
- One more old tool that all four walls could never block: **taxing nominal returns** — inflation raises nominal gains and tax is levied on the nominal, including on the inflation compensation of TIPS themselves, so **post-tax real returns can be negative under high inflation even if every hedge was chosen correctly**; and TIPS are only $2.15T — **the supply of the escape instrument is controlled by the party collecting the tax.**

**(4) The quantitative downgrade (this section's net conclusion)**

| | Original, 1946-1980 | Repression 2.0 |
|---|---|---|
| Tax base | all bondholders (long bonds included) | **only monetary holders + mandated holders** |
| Method | surprise inflation | **a knowable-in-advance negative real rate** (no surprise needed for a monetary base) |
| Rate | 2-3% of GDP a year | **most likely around 1%** (⚠ mechanism inference) |
| Result | debt/GDP 106% → 23% (**liquidation**) | **in the baseline, debt/GDP still rises to 120% (pain relief)** |

🔴 **Note the last row — the debt ratio keeps rising in this report's own baseline, which is itself an implicit concession to the objection**: the new machine's tax does not offset the deficit. **It cannot liquidate; it can only muddle through more cheaply than either default or hyperinflation.** And the 25-30% on scenario B in §8 is the probability that the creditors' counter-move wins and the machine is overturned — **the counter-move is priced in this report.**

⇒ **The qualification on "the one missing part is a negative real rate"** (written back into the headline conclusion): the sentence narrows in two directions — **for the monetary tax base, a negative real rate needs no "surprise" and collection begins the moment T6 fires; for free long-bond investors, the new machine has given up on taxing them** (their demand for compensation is the current 5.3% long end). Ignition lights the former, not the latter.

---

#### 6.2.6b How far the interest ban reaches: a two-legged presumption, and where it does not reach

**✅ Primary (Federal Register API + word-by-word search of the full text)**: OCC document **2026-04089**, *Implementing the GENIUS Act…* (RIN 1557-AF41 / Docket OCC-2025-0372), published 2026-03-02, comments closed 2026-05-01, 🔴 **still a Proposed Rule as of 2026-09-01 — there is no final rule**.

Rather than enumerate ways around the ban, the proposed §15.10(c)(4)(i) creates a **presumption**: satisfying both legs presumes the issuer is paying interest — **(A)** the issuer has an arrangement to pay interest or yield with an affiliate or related third party; **and (B)** that third party has an arrangement to pay yield to **holders** of the stablecoin the issuer issues. The legal basis is GENIUS **§4(h)**, "prevent evasion thereof".

⚠ **The two legs are exactly what marks out where it does not reach**: an independent third party with **no arrangement at all** with the issuer (a lending protocol, or an exchange running a yield programme at its own expense) does not fall inside the presumption — leg (A) fails.

**Measured: how much of the stablecoin float actually receives yield (2026-09-01, direct on-chain reads + exchange disclosures)**

| Measure | Reading | The question it answers |
|---|---|---|
| **Economic leakage** (flow basis) | **≈9.9%** | how much yield actually reaches holders today |
| **Structural leakage** | **≈5.1%** | how much of that the regulatory presumption cannot reach |
| Balances receiving no yield at all | **≈90.1%** | the actual size of the tax base |

⚠ The two must be kept apart: **regulatory closure is read off structural leakage, the current tax rate off economic leakage**; treating them as complements of each other is a dimensional error. ⚠ This set of readings has now been revised upward twice in the same direction (2.1% → 5.1%); under the discipline that "consecutive same-direction revisions are a signal about the method", a third same-direction revision requires re-examining the judgement that leakage is small, not simply changing the number again.

⇒ **Reading: the OCC's presumption blocks the bulk of it (the issuer-distributor chain), and almost nobody currently uses the part it cannot reach**; but "nobody uses it" is **behavioural** (the spread is not wide enough), not **legal** — it moves with rates and the leverage cycle, and it is not a moat.

🔴 **That behavioural conclusion has an explicit range of validity, which must not be dropped when quoting it**: it was measured under a **switching incentive of ≈3-4pp** (the measurement window happens to be a trough in the leverage cycle); **under an incentive of ≈9pp, as in the 2024 run-up, this conclusion has never been tested**. ⇒ The correct statement is "**at the current level of incentive, holders have not gone to collect that yield**", not "holders do not want that yield" — the latter goes beyond the evidence.

#### 6.2.6c A dimensional correction: the holder's loss ≠ the Treasury's gain

**These two quantities are not comparable and must not be set against each other.** The yield holders forgo under the interest ban **does not flow to the Treasury** — it flows to **issuers and distribution channels**: on published financial-statement figures, intermediaries retain about **$2.19bn** a year net, of which the Treasury collects **≤$0.46bn a year** through corporate income tax ⇒ **the ranking of beneficiaries is intermediaries : Treasury ≈ 4.8 : 1**.

⇒ **Two implications**:
1. **The "pain relief" character of Repression 2.0 is therefore even more complete** — 🔴 **less than 20% of this money ends up at the Treasury** (through corporate tax alone); the rest sits with issuers and distributors. ⚠ **Anything written as "a repression tax of hundreds of billions a year" will be read as federal revenue, which is precisely the dimensional mismatch this report itself once made**: what the Treasury gets is **financing convenience** (somebody buys the bills), not **debt-reducing revenue**;
2. **T6 firing (the real policy rate turning negative) changes [who takes it], not [how much the holder pays]**: the holder's real loss is set by the inflation rate, the intermediary's income by the bill yield — rate cuts compress the latter. ⇒ **The two curves are not synchronised and must not be conflated in a citation.**

⇒ **Which gives a general conclusion often mistaken for a single claim**: stablecoins push money into the short end. As an argument about a **financing mechanism** (who buys the bills) that holds; as an argument about a **debt-reduction mechanism** (saving the Treasury money) it does not.

---

## 7. The shape of the crisis: not default but a debasement tax — and its three breakpoints

### 7.1 The shape the market has already priced

- **In the same month as a 30Y auction stop of 5.216% (the highest since 2001), the 5-year CDS was only about 42bp** (⚠ single source, MacroMicro; and 42bp is in fact **elevated** against the 10-25bp that was normal before 2023, so it must not be extended into "historically low, nothing to worry about") — **the long end is pricing inflation, duration and a fiscal risk premium, and is not pricing hard default at all**;
- **"Chronic debasement" already has six years of evidence**: TLT's nominal total return is **-41.9%** from its 2020 peak, and **-55.1%** deflated by CPI; ⚠ **guard against the screenshot taken out of context**: most of that is duration repricing from a zero-rate starting point, and any hiking cycle would produce a drawdown of the same order — **it cannot all be read as debasement**. But the directional lesson stands: long-bond holders have been paying a "debasement tax" for six consecutive years;
- This corroborates Rogoff's judgement: the shape of the crisis is **"inflation + financial repression + partial default at most"** (2025-08); and his latest comment, on 2026-08-28 as the $40T mark was passed: "we will have some kind of debt crisis", and "action will most likely wait for a major shock to force it".

### 7.2 Three possible breakpoints (listed mechanically)

1. **The basis trade / leverage plumbing**: the 2020-03 precedent (the basis blew up → unlimited QE, $1T bought in weeks); ⚠ **an explicit data gap in this research: OFR basis-trade size, CFTC net futures shorts, MOVE and the SRF spread were not obtained — we have holdings snapshots but no picture of the funding-leverage plumbing; registered as outstanding**; 🔄 **09-07, partly filled: official series obtained for both MOVE and ACM** — MOVE 77.9 (09-01) / 73.1 (09-04) = the 22nd percentile of five years; **the ACM term premium is upgraded from ⚠ single source to ✅ an official daily series** (NY Fed, FRED `THREEFYTP10`). ⚠ **That upgrade simultaneously exposed a numerical error in the earlier text; see below.** OFR basis size, CFTC net shorts and the SRF spread are still missing, so **the basis-leverage channel itself remains at zero data**; "deeply negative swap spreads" is still a second-hand citation.
2. **Contagion from Japan**: a record JGB 30Y + foreign investors holding 55.6% of Japanese T-bills + Japan being simultaneously the largest foreign holder of Treasuries and a $123B seller over four months — **JGB yields rise → Japanese money comes home → Treasuries lose their largest marginal buyer**. The breakpoint in the two markets is the same pool of money;
3. **The policy standoff going out of control**: if a September hike lands while the long end simultaneously breaks loose, every rescue tool the Fed has (QE / twist / YCC) is **currently incompatible with its price mandate** (restarting QE at 3.7% inflation destroys its own credibility), while the fiscal side's ammunition (TGA / buybacks) is limited and the market has already watched it fail once within 24 hours.

### 7.3 What the crisis looks like

**Not a failed auction** (quantity always clears), but three things stacking: **the clearing price moving persistently higher + fiscal intervention losing traction at the margin + inflation expectations un-anchoring**, which makes the rate-deficit spiral explicit and finally forces politics to choose between two roads: **fiscal consolidation** (which historically requires a major shock to force it) or **the full installation of financial repression** (a rate cap plus inflationary liquidation — i.e. igniting the machine of §6). Official institutions have said this as strongly as they can: **the BIS Annual Report 2026: "fiscal space may contract well before the limits implied by long-run fundamentals"**; the IMF's April 2026 Fiscal Monitor names "the erosion of the safety premium on US Treasuries".

---

### 7.4 A real-time test: "BREAKING BLACK SWAN! Global bond rout" (2026-09-02) — measurement, attribution, and what follows

> **Discipline**: "black swan" is a label that can be tested against a distribution. This section first places the week's moves inside the distribution since 1990, and only then discusses attribution and what follows. All readings are primary (FRED / Yahoo closes / TreasuryDirect), as of the **2026-09-01 close and 09-02 intraday**.

#### 7.4.1 Measured: the speed was ordinary, the levels were records

**Treasuries (FRED from 1990, n≈9,170 days, including the 09-01 Yahoo close)**:

| Tenor | 09-01 close | 5-day change | **percentile of \|5-day change\|** | 10-day | 1-month |
|---|---|---|---|---|---|
| 5Y | 4.56 | **+21bp** | **88%** | +19bp | +16bp |
| **10Y** | **4.80** | **+16bp** | **80%** | +9bp | +10bp |
| 30Y | 5.27 | +10bp | 62% | 🔴 **−1bp** | +4bp |

- **Speed**: +16bp on the 10Y in a week sits at the 80th historical percentile — **a move that occurs about once every five weeks**; the 30Y's ten-day net change was **−1bp**, i.e. the long end did not participate in the "rout" at all;
- **Volatility**: **MOVE 77.9 = the 22nd percentile of five years** (five-year median 101, the usual stress line above 120) — **firmly in a low-volatility regime**;
- **Levels**: the 10Y at 4.80 is **the highest since 2023-10-31** (marginally above 4.79 on 2025-01-13); the 30Y at 5.27 is **below** its own 5.31 of 08-17 and the 5.33-5.34 intraday of 08-18.

**Globally (reference grade, tradingeconomics 09-01/02)**:

| | 10Y | Change | Record |
|---|---|---|---|
| 🔴 **UK** | **5.22%** | **+8bp/day, +27bp/month** | **highest since 2008-06**; 30Y 5.86% |
| 🔴 **Japan** | **3.02%** | +2bp/day, +19bp/month | **highest since 1996**; 30Y 4.20% / 40Y 4.27%, +91bp y/y |
| Germany | 3.34% | +19bp/month | — |
| Australia | 5.20% | +21bp/month | — |

> 🔴 **Ruling: this was not a black swan.** A black swan is an event in **speed and distribution**; this week's Treasury moves sat inside the normal distribution and volatility was low. **The headline passed off [a new high in levels] as [a shock in speed]** — what actually happened is a trend already a year old (JGBs +91bp y/y, the US 10Y +59bp over a year) **taking one more step, while several markets simultaneously crossed memorable round numbers** (UK 5.2% / Japan 3% / US 4.8%). Trend continuation and a black swan have opposite trading implications: the former can be handled with the criteria you already have, and only the latter requires abandoning your criteria to survive.

#### 7.4.2 Attribution: real rates rose while inflation expectations did not move — this was a policy-driven bear flattening, not an un-anchoring

**Decomposing the nominal 10Y (FRED, 08-26 → 08-31/09-01)**:

| | 08-26 | 08-31 / 09-01 | Change |
|---|---|---|---|
| Nominal 10Y | 4.66 | 4.75 / 4.80 | +9 / +14bp |
| **Real 10Y (DFII10)** | 2.34 | **2.44** | 🔴 **+10bp** |
| **Breakeven inflation (T10YIE)** | 2.32 | **2.31 / 2.35** | **−1 / +3bp** |
| 10Y−2Y | 0.47 | 0.41 / 0.40 | **−7bp (bear flattening)** |
| 30Y−5Y | 81bp | 71bp | **−10bp (bear flattening)** |

**The catalysts over the same period (reference grade, consistent across sources)**:
1. **Oil**: Brent **95.45** (**+19.3%** from the 08-04 low, +6.9% over five days), WTI 90.74 — renewed US-Iran hostility (directly connected to the Middle East variable in §4);
2. **The Fed**: Warsh's 08-28 speech (full transcript, primary) plus Governor Barr's "if inflation does not come down we should be prepared to hike" ⇒ **the probability of a September hike went from 40% to 66-70%** (reference grade);
3. **The UK**: BRC shop-price inflation at a two-year high, with the market pricing 32bp of BoE hikes this year;
4. **Japan**: rising expectations of a BoJ hike this month (Bessent publicly urging Ueda to be "decisive") and the Takaichi government's expansionary fiscal stance.

> 🔴 **⇒ What the decomposition says: oil rose 19% while 10-year inflation expectations moved only +3bp, so almost the entire rise in nominal rates was the real rate — the market is pricing "Warsh will suppress the pass-through from oil", not "inflation is about to un-anchor".** The bear flattening (the short end rising more than the long) is consistent with that: **this was a repricing around the central bank's reaction function, not around fiscal sustainability.** ⇒ **The crisis shape in §7 (un-anchored expectations + a rising clearing price + failing fiscal intervention, all three together) currently satisfies only part of the second item.**

⚠ **A cross-asset corroboration**: **DXY 99.77 (+0.1% over five days)** — the US real rate rose 10bp and the dollar did not strengthen, **because the UK, Japan, Germany and Australia moved with it**. This was a **globally synchronised rate shock**, not a US-specific "Treasury credit" event; ⇒ it does **not** touch the mechanisms behind T3/T4 (reserve share / Japanese selling), **but** it pushes breakpoint 2 of §7.2 (contagion from Japan) to the front — see below.

#### 7.4.3 Checked against this report's triggers (snapshot, 2026-09-02)

| Trigger | This week's reading | Status |
|---|---|---|
| **T1** (interest / receipts >22%) | the curve +30bp over three months ⇒ marginal issuance cost rising; **the stock of interest rolls monthly, so the reading is unchanged this week (19.7%)** | ✅ not triggered; **direction unfavourable** |
| 🔴 **T2** (long-end auction tail >3bp and PD >20%) | **no long-end auction this week. Next: 09-08 3Y / 09-09 10Y reopening / 09-10 30Y reopening** (TreasuryDirect, primary) | ✅ not triggered; **09-10 is the first test of quantity at a 5.27% long end** |
| 🔴 **T3** (Japan −$50B in a month, confirmed by flows) | JGB 10Y 3.02% (highest since 1996) + expectations of a BoJ hike this month ⇒ **the price conditions for Japanese repatriation are forming**; TIC data lags two months | ✅ not triggered; **the mechanism is at "preconditions met, flows still to be observed"** |
| T4 (constant-FX dollar share) | DXY flat, move globally synchronised ⇒ no implication for share | ✅ not triggered |
| T5 (TGA / buyback escalation officially announced) | long-end buybacks already doubled (from 09-09, §1.4); **no new announcement this week** | ✅ not triggered |
| 🔴 **T6** (core PCE > EFFR) | core PCE 3.34 vs EFFR 3.63 = **+0.29pp**; **a 25bp hike on 09-16 would widen the gap to +0.54pp** | ✅ not triggered; 🔴 **this week's events point toward [postponing ignition]** |
| §7.2 breakpoint 1 gap | **MOVE now obtained (77.9, 22nd percentile of five years), partly filling the gap**; basis size and CFTC net shorts still missing | registered |

> 📌 **A counter-intuitive implication**: the direction in which an oil shock acts inside this framework is **[undetermined] before 09-16**. It is tempting to write "oil is a decelerator, because it triggers a hike and the hike pushes T6 further away" — but **the premise of that sentence (that the Fed responds to the oil pass-through) is, before the FOMC, only the 55% baseline of §7.4.4, not a fact.** The correct formulation is:
> - **If the hike lands on 09-16** ⇒ the gap widens from +0.29pp to +0.54pp and **oil is a decelerator**;
> - **If the Fed stands still** (about 25%) ⇒ the gap is unchanged while inflation rises, and **the same oil shock becomes fuel instead**.
>
> 🔴 **⇒ 09-16 is therefore not "one more data point", it is the [switch] on the oil variable — it decides the sign with which oil enters this framework.** The reading discipline does not change: watch T6, not the oil price; **oil enters this framework only through the single channel of "how the Fed responds", and the direction of that channel is not revealed until 09-16.** 📌 Filed under this report's discipline: **a baseline scenario must never be written as something that has already happened** (the same family as "a pre-registered indicator must not be claimed retroactively" — one is after the fact, one is before it).

#### 7.4.4 What follows: three paths, and what to watch for each

| Path | Probability (subjective, falsifiable) | Shape | Observable signals |
|---|---|---|---|
| **A · the repricing ends at the FOMC** (baseline) | **~55%** | a 25bp hike lands on 09-16; the 10Y in a 4.7-5.0 range, the 30Y testing 5.31-5.34 **without breaking**; MOVE <100; bear flattening continues | ① breakevens hold ≤2.4; ② 30Y−5Y keeps narrowing; ③ the 09-10 30Y auction tails ≤1bp; ④ DXY does not strengthen |
| 🔴 **B · the long end joins and the term premium takes over** | **~25%** | the 30Y **breaks 5.34** (the post-2007 high) **with breakevens rising alongside** and the curve turning to a **bear steepening**; gilts and JGBs lead lower, Japanese repatriation begins | ① T10YIE >2.5; ② 30Y−5Y widens rather than narrows; ③ the 09-10 auction shows **a tail >3bp and PD >20% (= T2 fires)**; ④ MOVE >100; ⑤ Japan's monthly TIC decline approaches −$50B |
| **C · data weaken and hike expectations collapse** | **~20%** | a weak 09-04 payrolls print ⇒ hike odds fall below 40% and the 10Y gives back 15-20bp; **but the oil-driven inflation expectation does not fall** | ① the real rate falls while breakevens do not (**the combination to watch most**: falling real rates + rising inflation expectations = the gap to T6 narrowing); ② gold rebounds harder than equities |

**Near-term calendar (all primary)**: 09-02 ADP → **09-04 payrolls** → **09-08 3Y / 09-09 10Y / 09-10 30Y auctions** (the T2 test) → CPI around 09-10/11 (⚠ the BLS schedule page could not be read directly this time; per usual practice) → **the 09-15/16 FOMC (with SEP)** → the BoJ's September meeting (⚠ date not obtained directly).

> 🔴 **Path B is the entrance to the crisis shape of §7, and every one of its signals is readable within eight days**: **the 30Y reopening on 09-10 is the first test of quantity at the 5.27% level** — if the tail and the PD takedown both cross their lines, T2 fires and this report switches from a "clearing on price" reading to a "refusing on quantity" reading; if it clears smoothly, path A's probability is revised up. **No direction is given before then.**

> **In one line**: this week was not a black swan. It was a **globally synchronised, policy-driven, real-rate-led** bear flattening; it **postponed** this report's ignition signal (T6), **advanced** the Japanese contagion channel (T3's preconditions), and installed the first adjudication switch for the entire §7 crisis shape on **the 30Y auction of 09-10**.

#### 7.4.6 🔄 Follow-up (2026-09-07): path A leads for now, but the adjudication point has not arrived

**Five trading days after the three paths were pre-registered in §7.4.4, the readings are (✅ FRED / Yahoo, primary):**

| | 09-01 (shock peak) | **09-04** | Change |
|---|---|---|---|
| 10Y | 4.80 (month high) | **4.78** | -2bp |
| 30Y | 5.27 | **5.25** (**-1.2%** from the 5.31 month high of 08-17) | -2bp |
| **MOVE** | 79.71 (month high, 09-02) | 🔴 **73.10** | **-8.3%** |
| Breakeven (T10YIE) | 2.35 | 2.35 | **unchanged** |
| DXY | 99.77 | **99.13** | did not strengthen |

**⇒ Current reading against the three paths (⚠ the adjudication point has not arrived; no conclusion is drawn)**:

- ✅ **All four signals of path A (repricing ends at the FOMC, ~55%) currently hold**: the 30Y has not broken 5.34, breakevens are ≤2.4 and did not move at all, MOVE fell rather than rose (to 73), and the dollar did not strengthen;
- 🔴 **Path B's (term premium takes over, ~25%) only hard adjudication point is still ahead**: **the $22B 30Y reopening on 09-10**;
- ⚠ **Path C (data weaken) is half falsified**: the 09-04 payrolls came in at **162K against an expected 56K** — the data did not weaken; **yet hike odds still fell from 63% to 52%** (Waller's data-dependent remarks on 09-03, reference grade) ⇒ **a fourth shape has appeared that none of the three paths anticipated: hawkish data with falling odds.** 📌 **Under the rule §7.4.4 set for itself about shapes that do not fit, this counts as "the market pricing something outside the pre-registered set" and should be investigated separately rather than forced into one of the paths**; the cause is registered as disagreement within the committee.

> ⚠ **This section updates readings only; it does not modify the pre-registered probabilities in §7.4.4** — under this report's discipline, probabilities may not be adjusted on interim readings before the adjudication point arrives.

---

## 8. Forecasting the timing: an honest framework (conditional windows, not dates)

### 8.1 The academic floor: the timing is not forecastable

- **The CBO's own words: "there is no identifiable tipping point"**;
- Reinhart-Rogoff's 90% threshold was shown by Herndon and others to rest on flawed data, and Eberhardt-Presbitero demonstrated that **no common cross-country threshold exists**;
- Greenwood-Hanson-Shleifer: even with credit and asset prices both hot, all you can do is raise the **probability** of a crisis "within three years", and the object is banking crises rather than sovereign ones;
- ⇒ **Every "it blows up in X years" — including Dalio's "three years, give or take one or two" (original date 2025-03) — is a verbal estimate with no power to forecast timing. What this section offers is conditional windows and graded probabilities, not dates.**

### 8.2 Three scenarios (⚠ probabilities are this report's subjective judgement, not a calculation; calibration disclaimer: judgements of this kind have historically over-estimated the speed of change)

**Baseline (about 60%) — no acute crisis, Financial Repression 2.0 arriving gradually**
Nominal growth + moderate inflation (3%±) + continued absorption through short-end demand engineering; debt/GDP creeping up; long-bond holders continuing to pay the debasement tax; politics forced into partial repairs before the OASI cliff in 2032. **This is a low-spec rerun of the 1946-1980 playbook on a decadal timescale.** Beneath the appearance of "nothing happening", the wealth transfer proceeds every day — which is exactly why the scenario is sustainable: **no single-day news means no political cost.**

**Scenario B (about 25-30%) — an acute repricing event**
Triggers: the long end going out of control / the basis trade blowing up / contagion from Japan / the policy standoff losing control. **The window where conditions are densest: 2027-2028** — not a forecast, but the overlap of four calendar anchors:
- TBAC's warning of a **$1.45T financing gap in FY2027-28** (⚠ single source, see §6.2);
- the next debt-limit **X-date: late 2027 to mid-2028** (BPC);
- the start of the overlap between Dalio's verbal window (2027±1-2) and Rogoff's (4-7 years, i.e. 2029-2032);
- the inertia toward fiscal concessions before the 2028 election (further lowering the odds of consolidation).
The script after it triggers: the fiscal side holds the line first (already rehearsed) → it fails → the Fed is forced to choose between its price mandate and market function → if inflation is still above 3%, it will still ultimately choose market function (a 2020-03-style $1T in a week), **at the cost of higher inflation afterwards — i.e. scenario B's end point merges back into the baseline, with the debasement tax collected in one lump instead.**

**Scenario C (about 10-15%) — fiscal consolidation forced by a shock**
Rogoff: "action will wait for a major shock." Historically consolidation almost never precedes the crisis; if it does happen, it is the friendliest path of the three for long bonds.

**⇒ The key distinction from a "collapse"**: none of the three paths ends in hard default (domestic-currency denomination + reserve-currency status + military dependency relationships; the historical precedent, Britain, walked the same road — devaluation and repression, zero formal default). **What risk assets should actually fear is not a Treasury default but the repricing process of scenario B itself** (a discount-rate shock), and, in the baseline, the chronic underperformance of nominal assets against real purchasing power.

### 8.3 The mechanical trigger register (for routine weekly tracking; adjudication sources fixed, judgeable in both directions)

| # | Trigger | Adjudication source | Meaning |
|---|---|---|---|
| T1 | **rolling 12-month** net interest / **rolling 12-month** net receipts **>22%**, met in six consecutive MTS monthly reports | MTS Table 9 + Table 4 (monthly, primary; 🔴 caliber pinned: "annualised" without a stated method is polluted by seasonality, FYTD annualisation especially — hence rolling 12 months) | the compounding spiral shifting up a gear |
| T2 | a **≥10-year** (10/20/30Y) coupon auction with **a tail >3bp AND PD takedown >20%** in the same auction | TreasuryDirect result sheets (the maturity restriction was added because tail/PD distributions differ structurally by tenor, and mixing them is "two economically different instruments under one indicator name"; the proposition here is about the long end) | demand anomaly (the March 2Y had PD at 24% but a tail of 1.8bp — not a trigger on either the old or new definition) |
| T3 | Japanese holdings falling **$50B or more in a month, AND confirmed as net selling by the monthly TIC flow tables** | TIC Table 5 stocks + the monthly flow release (⚠ two-month lag) | the Japanese contagion channel. 🔴 The second test is essential: **stocks include valuation changes, and a price fall by itself reduces the holding value — that is not selling.** Reading stocks alone violates the discipline "a change in balance ≠ a sale" |
| T4 | the dollar share falling **0.5pp or more in a quarter on the constant-FX basis** (the IMF briefing's constant-FX figure) | IMF COFER quarterly briefing (🔴 corrected twice: an earlier review claiming "there is no official valuation-adjusted series" was **wrong** — the IMF briefing has published a constant-FX basis since 2025; and back-filling proves a raw-share threshold would misfire: **2025Q2 showed -1.47pp on the raw share, of which 92% was an FX valuation effect, with the constant-FX basis down only -0.12pp** — the original design would have reported an FX beta as reserve-diversification alpha. The constant-FX basis moves ±0.1-0.2pp normally, so -0.5pp is anomalous) | the reserve side turning from a slow variable into a fast one |
| T5 | **drawing on the TGA / another doubling of buybacks moving from rumour to official announcement** | Treasury press releases | escalating fiscal ammunition = escalating pressure |
| T6 | **core PCE y/y > the monthly average EFFR** (the real policy rate turning negative) | BEA (core PCE) + NY Fed EFFR, daily, averaged monthly (🔴 the adjudication quantity is pinned: the fed funds target is a **range**, and 3.50-3.75 against 3.6% inflation falls inside the range and cannot be adjudicated — the quantity must be a single value, hence EFFR) | **the formal ignition signal of financial repression** |

**Birth-date back-fill check (a threshold must be back-filled with the reading on the day it is registered — an indicator that triggers on its birthday has no early-warning value)**:

| # | Reading at registration (2026-08-30/31) | Status |
|---|---|---|
| T1 | rolling 12M = 1,061.0/5,373.4 = **19.7%** (threshold 22%, 2.3pp away) | ✅ not triggered |
| T2 | the August 30Y had a 0.4bp tail and 11.5% PD; no 2026 auction has crossed both lines together | ✅ not triggered |
| T3 | Japan's largest monthly decline in 2026 was about $40B (and not confirmed by flows) | ✅ not triggered |
| T4 | on the constant-FX basis 2026Q1 was **a rise**; 2025Q2 was only -0.12pp | ✅ not triggered (**the raw-share version would have misfired in 2025Q2 and was discarded**) |
| T5 | drawing on the TGA is still a rumour, never announced | ✅ not triggered |
| T6 | EFFR ≈3.6%+ > core PCE 3.34% | ✅ not triggered (the real policy rate is still positive) |

##### 🔄 Register refresh (2026-09-07; all re-checked at source)

| # | 09-07 reading | Distance to threshold | Status and change |
|---|---|---|---|
| **T1** | ✅ **independently recomputed and confirmed at 19.75%** (1,061.0/5,373.3; the latest MTS period is still 2026-07-31) | **2.25pp** | ✅ not triggered, **reading unchanged**; ⚠ the August MTS lands around 09-11 and will be refreshed then |
| 🔴 **T2** | **three auctions this week: 09-08 3Y $58B / 09-09 10Y reopening $39B / 09-10 30Y reopening $22B** (✅ TreasuryDirect, primary) | — | ✅ not triggered, **but 09-10 is the first test of quantity at a 5.25% 30Y**; a tail >3bp together with PD >20% would fire it |
| **T3** | no new TIC (two-month lag); ⚠ **the preconditions are in place**: JGB 10Y at 3.02% (highest since 1996) + expectations of a BoJ hike in September | — | ✅ not triggered, **observation frequency raised to every TIC release day** |
| **T4** | no new COFER (quarterly); 🔄 DXY 99.13, and it did not strengthen through the §7.4 shock | — | ✅ not triggered |
| **T5** | the rumour is still unannounced; 🔄 **but the first doubled buyback runs on 09-09** | — | ✅ not triggered (⚠ the criterion is "another doubling / an announced TGA drawdown"; the doubling already announced does not constitute a trigger) |
| 🔴 **T6** | core PCE **3.34%** vs EFFR **3.63%** = **+0.29pp** | **0.29pp** | ✅ not triggered; **a 25bp hike on 09-16 widens the gap to +0.54pp; standing still leaves the gap unchanged while inflation rises** — the direction is decided by the FOMC (§7.4.3) |

> 🔴 **Net position after this refresh: all six triggers are un-fired, and the two closest are T6 (0.29pp) and T1 (2.25pp). ⇒ There are three readable adjudication points within ten days: the 09-10 auction (T2), the 09-11 CPI (the hike-odds line, not T6), and the 09-16 FOMC (T6's direction).**

⚠ Caliber discipline: T1-T6 are **slow-variable** triggers and belong to a different timescale from **fast-variable** scoring such as equity-index drawdowns; **the two do not adjudicate each other.**

---

## 9. Limits of the evidence and known gaps (registered explicitly, not papered over)

1. **Zero data on the leverage side of the basis trade**: OFR basis size, CFTC net shorts, MOVE and the SRF spread were all unobtainable — the fastest channel of crisis transmission is precisely the chapter with the least data (the completeness review flagged this; it is correct);
2. **The term-premium decomposition is incomplete**: ~~ACM at 0.80% is a ⚠ single source~~ ✅ **upgraded on 09-07 to an official daily series (FRED `THREEFYTP10`), with the value corrected (see item 7)**; but there is still no TIPS breakeven / 5y5y — **so the 30Y at 5.33% cannot be decomposed quantitatively into "inflation expectations vs term premium"**, and that decomposition determines whether the crisis shape is "debasement" or "a real-rate penalty", which have opposite portfolio implications;
3. **The Euroclear / Belgium custody paradox is undecidable** (§1.3);
4. **Two measures left unadjudicated**: Japan's debt/GDP (256 vs 235-237) and the COFER decimal (56.42 vs 56.77, ±0.35pp);
5. **The 41.6bp CDS is a single source**; the September hike probability is an 08-28 snapshot;
6. ~~The Medicare +16% was not traced~~ ✅ traced (§2.4: about $60-80B is a payment-calendar artefact, adjusted growth is +8~10%, "faster than interest" is doubtful, and the CBO MBR's adjusted basis is the final adjudicator); the **quantitative** decomposition of the USDCNY appreciation's effect on exporters' margins was not done.

7. 🔴 **The ACM term premium: a misreading in circulation** — the common claim is "widening rapidly from **0.51%** in June to 0.80% on 08-13". ✅ **The official daily series (NY Fed ACM, FRED `THREEFYTP10`)**:

| | Official reading |
|---|---|
| 2026-06 range | **0.678 – 0.808%** (🔴 **0.51% never occurred in June**) |
| 2026-08-13 | **0.823%** (close to "about 0.80%" ✅) |
| 2026-08-28 (latest) | **0.875%** |
| 2026 year-to-date low | 0.463% (**02-27**); 17 days below 0.55%, the most recent being **03-10** |

> **⇒ The [direction] of the widening holds, but the [size and starting point] were overstated.** The correct formulation: **from a June low of 0.678% to 0.875% on 08-28, a summer widening of about +20bp**; measured from the year's low (0.463% on 02-27) it is +41bp YTD. The 0.51→0.80 (+29bp over 2.5 months) took a **March** reading for a June one.
> 📌 **The methodological value of this item exceeds the number itself**: this misreading was not found by review — it was **exposed as a by-product of "upgrading a ⚠ single source to a ✅ official series"**. ⇒ **Adding a primary source does not only raise credibility, it is itself a test of the old number** ⇒ **any load-bearing figure carrying a ⚠ for a long time should be scheduled for upgrade rather than used indefinitely with the marker attached.**
> ⚠ **The second pit in the same family**: the same number usually appears in several places. **Count the occurrences with grep, not from memory; and grep again after fixing to confirm zero residue** — otherwise the old and new values coexist in one document, which is harder to spot than the original error.

## 10. Measures and sources (with the correction record)

### 10.1 Source grading: how much each figure should be trusted

**This report's evidence markers are the grading itself; before reading any number, look at the marker in front of it:**

| Grade | Meaning | Citation rule | Typical cases here |
|---|---|---|---|
| ✅ **primary official API / document** | Treasury Fiscal Data API, MSPD, MTS, Fed H.4.1/H.10, FRED, TreasuryDirect result sheets, BEA/BLS, the Federal Register, SEC EDGAR, full official transcripts, NBER/BIS/IMF originals | quote directly, with the source | §1.1 debt totals, §2.1 MTS, the T1 recomputation in §8.3, §6.1 Fed holdings, the rate percentiles in §7.4, the ACM term premium and MOVE |
| 🔶 **primary + this report's own calculation** | derived from the above under this report's method (percentiles, rolling 12 months, contribution decompositions) | a citation must **carry the method and the measure**, or the recomputation will not match | the T1 rolling 12 months, the historical percentiles in §7.4.1 |
| ⚠ **second-hand / institutional estimate / single source** | institutional model estimates, media relays, readings with only one source | 🔴 **never quote with the ⚠ stripped off**; here they are used to **size a window, never to settle one** | the TBAC $1.45T financing gap (minutes relayed by media), the 41.6bp 5-year CDS (single source), hike probabilities (FedWatch), the 12.1% average effective tariff rate |
| ❔ **widely accepted, not adversarially verified** | broadly accepted but not put through verification this round | keep the ❔ | parts of the institutional history in §6.2.1b |
| ❌ **falsified** | rejected on adversarial verification | **do not cite** | "the 50-year US-Saudi petrodollar agreement expired in 2024" (§4) |

🔴 **A rule for anyone reposting this**: every ⚠ item here is a **single source**, and each carries its qualifier in the original text. **Crop the qualifier out of a screenshot and what you are left with is a claim this report does not make** — especially the TBAC $1.45T gap (one of the four anchors of the 2027-28 window in §8; if that number is wrong the window weakens accordingly, which this report has registered as pending verification).

📌 **A load-bearing figure that carries a ⚠ for a long time should be scheduled for a source upgrade rather than used indefinitely with the marker attached.** The marker only solves "the reader knows it is weak"; it does not solve "it may be wrong" — the ACM term premium above is the case in point: the act of upgrading it to an official daily series exposed a March reading that had been recorded as June (correction in §9).

📌 **One indicator name can have two tables behind it**: any ratio-type figure (such as T1 in §8.3) must be cited **together with which table and which field** — the single word "receipts" has three measures and three answers in the MTS, sitting 2.25 / 1.52 / 4.02pp from the threshold.

---

**Adversarial verification record**: 21 load-bearing claims were put through adversarial verification — **15 confirmed / 6 overturned and rewritten / 0 falsified outright**. The six below are the places most easily misread; in each, the common wrong reading is given and the measure this report uses is in bold:
1. The interest / receipts growth multiple is **3.4×** (net receipts basis); using gross receipts as the denominator gives 2.7×;
2. Total foreign holdings are **not** at "a record high": **the peak was 2026-02 ($9,489B) and June was the second consecutive monthly decline**, though still +$205B y/y;
3. The DXY 2026 range is **95.5-101.5** (the commonly quoted 95.5-100 is missing the upper bound);
4. The record month for foreign holdings is **February**, not May; the ten-year COFER decline is **8.4pp**, not 9pp;
5. The financial-repression liquidation tax, **on the published version's basis**, is **2-3% of GDP** with negative-real-rate years at **50% in the US / 60% in the UK** (BIS WP 363, Table 3); the 3-4% of GDP and 25%/48% that circulate are not the published figures;
6. The 30Y auction date is **08-13** (08-14 is the date of a commentary article about it, not the auction).

**The key measures table** (check against this before citing any number here): total debt $40.08T ≠ debt held by the public $32.31T ≠ marketable $31.46T ≠ the debt-limit measure $41.1T; gross interest $1.22T ≠ net interest $970B; a general-government deficit of 7.4% ≠ the federal fiscal-year 5.8-6%; TIC is measured by custody location; COFER is allocated reserves; the liquidation tax is on the published version's basis.

**Principal primary sources**: Treasury Fiscal Data API (debt_to_penny / MSPD / MTS / interest_expense), TreasuryDirect auction result sheets, Fed H.4.1/H.10, the full official Warsh transcript (federalreserve.gov/newsevents/speech/warsh20260828a.htm), CBO 61882/62105/62704, the 2026 Trustees Reports, the BIS Triennial Survey rpfx25, IMF COFER, NBER WP 31577 (Acalin-Ball) and 16893 (Reinhart-Sbrancia) extracted in full locally, the US National Archives (JECOR files), TBAC Q3 2026 materials, GAO-26-107529.

> This research was produced by multi-agent search and adversarial verification and written up as a whole by hand; **not investment advice**. The probabilities are subjective judgements carrying a calibration disclaimer; every trigger's adjudication source is fixed, and no trigger is revised after it fires.
