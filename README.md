![Dust & Debt · The Frontier Chronicle](docs/banner.svg)

**English** · [简体中文](https://github.com/cnsdqd-dyb/dust-and-debt/blob/main/README.zh-CN.md)

# 🤖 How Far Are We from Building a Truly Playable, High-Quality Game Quickly with AI?

> *The wilderness offers opportunity. The ledger demands payment.*

**Dust & Debt is a playable experiment built entirely with GPT 5.6 sol.** It asks a practical question: can AI move beyond demos and rapidly create a game with enough depth, identity and polish that people actually want to play?

Our current answer is: **AI can already reach a broad, surprisingly playable game much faster than before. Reaching consistently high quality still takes sustained judgment, testing and refinement.** This repository lets you judge that answer yourself instead of taking our word for it.

**[⚔️ Play the English Beta](https://cnsdqd-dyb.github.io/dust-and-debt/editions/dust-and-debt-v51.5.2-en-beta.html) · [🏮 Play the Chinese Original](https://cnsdqd-dyb.github.io/dust-and-debt/versions/%E5%B0%98%E5%9C%9F%E4%B8%8E%E5%80%BA%E5%8A%A1_V51.5.2_%E9%81%93%E8%B7%AF%E5%85%AD%E5%90%91%E8%B5%84%E6%BA%90%E4%B8%8E%E5%9C%B0%E5%9B%BE%E5%85%A5%E5%8F%A3%E4%BF%AE%E5%A4%8D%E7%89%88.html) · [📥 Download](https://github.com/cnsdqd-dyb/dust-and-debt/releases/tag/v51.5.2) · [📚 Browse 38 originals](VERSIONS.md)**

Recommended build: **V51.5.2** · Best on desktop Chrome · The English Beta covers the main routes; occasional event text may remain Chinese.

---

## 🧭 What did AI actually build?

This is one interconnected browser game rather than a collection of disconnected prototypes:

| The playable result | Why it matters to the experiment |
| --- | --- |
| A 96×96 frontier with roads, rivers, terrain, weather and travel resources | AI assembled systems that affect one another, not just a visual scene |
| Bounties, treasure maps, Gold Rush and Endless Night expeditions | The game supports several complete risk-and-reward loops |
| Horses, a stable, wardrobe and a movable 3D tavern interior | Progress includes ownership and personal expression |
| Horse racing, casino games, roulette, a revolver table and a financial market | Different activities feed the same cash-and-debt economy |
| Browser saves, exportable progress and 38 preserved source snapshots | The project grew through real iteration and remains inspectable |

The screenshots below are direct captures from V51.5.2. They show the breadth that AI reached, while the repository preserves the implementation and its rough edges.

## 🗺️ Evidence I · A frontier worth crossing

Roads, rivers, farms and rough terrain shape each route. Weather, stamina and supplies turn the map into part of the game rather than a painted backdrop.

![🗺️ Actual frontier map](docs/screenshots/world-map.webp)

## 📜 Evidence II · Bounties, treasure and expeditions

Choose a wanted target, sign a Gold Rush contract, follow a treasure clue or enter Endless Night. Loot only becomes safe after you make it home.

<table><tr><td width="50%" valign="top"><a href="docs/screenshots/bounty-board.webp"><img src="docs/screenshots/bounty-board.webp" width="100%" alt="Pick your quarry"></a><h4>📜 Pick your quarry</h4><p>Compare wanted posters, rewards and targets before committing to a trail.</p></td><td width="50%" valign="top"><a href="docs/screenshots/gold-rush.webp"><img src="docs/screenshots/gold-rush.webp" width="100%" alt="Gold Rush expedition"></a><h4>💰 Chase a frontier fortune</h4><p>Explore settlements, compete with treasure hunters and bring the fortune home.</p></td></tr></table>

<table><tr><td width="50%" valign="top"><a href="docs/screenshots/treasure-map.webp"><img src="docs/screenshots/treasure-map.webp" width="100%" alt="Follow a treasure map"></a><h4>🗺️ Follow a real clue</h4><p>Each map points to one treasure, but finding it is only half the journey.</p></td><td width="50%" valign="top"><a href="docs/screenshots/endless-night.webp"><img src="docs/screenshots/endless-night.webp" width="100%" alt="Endless Night expedition"></a><h4>🌙 Survive Endless Night</h4><p>Changing fugitive activity gives the familiar frontier a darker rhythm.</p></td></tr></table>

## 🐎 Evidence III · A mount and a place to call home

Buy a mount, manage the stable, dress the hunter and arrange objects inside the 3D tavern. The systems between expeditions give the journey a sense of ownership.

<table><tr><td width="50%" valign="top"><a href="docs/screenshots/mount-market.webp"><img src="docs/screenshots/mount-market.webp" width="100%" alt="Mount market"></a><h4>🐎 Choose a travelling companion</h4><p>Compare animals and prices before spending hard-earned cash.</p></td><td width="50%" valign="top"><a href="docs/screenshots/stable.webp"><img src="docs/screenshots/stable.webp" width="100%" alt="Stable"></a><h4>🌾 Manage the stable</h4><p>Inspect and manage the companions that carry you into the wilderness.</p></td></tr></table>

<table><tr><td width="50%" valign="top"><a href="docs/screenshots/wardrobe.webp"><img src="docs/screenshots/wardrobe.webp" width="100%" alt="Wardrobe"></a><h4>🤠 Give the hunter a look</h4><p>Customize the character and mount before returning to the tavern.</p></td><td width="50%" valign="top"><a href="docs/screenshots/tavern-decoration.webp"><img src="docs/screenshots/tavern-decoration.webp" width="100%" alt="Tavern decoration"></a><h4>🏚️ Make the tavern your own</h4><p>Select and arrange objects with the in-game 3D decoration editor.</p></td></tr></table>

## 🏇 Evidence IV · A living economy of risk

Race horses, spin the roulette wheel, face the revolver table or study the financial market. Every choice returns to the same balance sheet and the same monthly debt.

<table><tr><td width="50%" valign="top"><a href="docs/screenshots/race-selection.webp"><img src="docs/screenshots/race-selection.webp" width="100%" alt="Race selection"></a><h4>🏇 Read the field</h4><p>Compare runners and odds, then decide where to place the wager.</p></td><td width="50%" valign="top"><a href="docs/screenshots/race-result.webp"><img src="docs/screenshots/race-result.webp" width="100%" alt="Race result"></a><h4>🏆 Watch the result land</h4><p>The podium, wager and net payout make every choice tangible.</p></td></tr></table>

<table><tr><td width="50%" valign="top"><a href="docs/screenshots/casino.webp"><img src="docs/screenshots/casino.webp" width="100%" alt="Casino"></a><h4>🎰 Pick a table</h4><p>Several games tempt your luck while the debt ledger keeps running.</p></td><td width="50%" valign="top"><a href="docs/screenshots/roulette.webp"><img src="docs/screenshots/roulette.webp" width="100%" alt="Roulette"></a><h4>🎡 Let the wheel decide</h4><p>Choose a bet and watch fortune move faster than the next repayment date.</p></td></tr></table>

<table><tr><td width="50%" valign="top"><a href="docs/screenshots/revolver-table.webp"><img src="docs/screenshots/revolver-table.webp" width="100%" alt="Revolver table"></a><h4>⚔️ Raise the stakes</h4><p>Opponents, items and a life-or-death wager meet in one tense scene.</p></td><td width="50%" valign="top"><a href="docs/screenshots/market.webp"><img src="docs/screenshots/market.webp" width="100%" alt="Financial market"></a><h4>💹 Find another way to earn</h4><p>Inspect prices and trading choices when the wilderness is not paying.</p></td></tr></table>

## 🍺 Evidence V · The tavern that ties it together

Every expedition begins and ends at the tavern. The fireplace, notices, furnishings and debt ledger turn separate activities into one frontier life.

![🍺 Actual 3D tavern](docs/screenshots/tavern.webp)

**📸 16 real gameplay screenshots.** Click any image for full size, or open the [interactive gallery](https://cnsdqd-dyb.github.io/dust-and-debt/#gallery). Expedition captures may use built-in test funds and full-map view; the [capture notes](docs/SCREENSHOTS.md) explain the setup.

## ⚖️ So, how far away are we?

This project suggests that the distance to a **playable game** has become dramatically shorter. GPT 5.6 sol produced a distinctive world, many linked systems and enough content for players to form strategies, preferences and stories.

The distance to a **consistently high-quality game** is still visible:

- System breadth must become coherent pacing rather than feature count.
- Long-tail bugs need repeated playtesting across routes and saves.
- Controls, feedback, onboarding and accessibility need careful product judgment.
- Localization needs contextual review beyond direct text replacement.
- Performance and external assets need packaging for dependable offline play.
- Good taste still decides what to cut, simplify and polish.

AI has made ambitious game creation far more accessible. The remaining work is increasingly about direction, evaluation and care. **Play this build and decide how much of that gap has already closed.**

## 📚 A public record of iteration

All **38 original HTML files** remain byte-for-byte intact: 37 game builds and one visual reference sheet spanning V33 through V51. The recommended build is **V51.5.2, the road six-direction resource and map-entry fix edition**.

- [📖 Version ledger](VERSIONS.md)
- [🗃️ Original file manifest](versions/manifest.json)
- [🔐 SHA-256 checksums](versions/SHA256SUMS.txt)
- [🐎 Open the recommended Chinese build](https://cnsdqd-dyb.github.io/dust-and-debt/versions/%E5%B0%98%E5%9C%9F%E4%B8%8E%E5%80%BA%E5%8A%A1_V51.5.2_%E9%81%93%E8%B7%AF%E5%85%AD%E5%90%91%E8%B5%84%E6%BA%90%E4%B8%8E%E5%9C%B0%E5%9B%BE%E5%85%A5%E5%8F%A3%E4%BF%AE%E5%A4%8D%E7%89%88.html)

## 🌙 Before setting out

Use desktop Chrome and stay online for the first visit because the 3D tavern loads Three.js and external model resources. Audio may begin after the first click. Progress is stored in browser `localStorage`; export the save before switching versions, sites or browsers.

## 🛠️ Creation statement

**The game was made entirely using GPT 5.6 sol.** The bilingual showcase and archive were prepared for this public release. Third-party libraries and models remain the property of their respective owners; this statement describes the game's creation and does not claim authorship of external resources. No open-source license has been selected.

## ⭐ Help answer the question

If this experiment makes you think differently about AI-made games, please **Star the repository**, share the build and tell us where it feels like a real game—and where the illusion breaks. Bugs and feedback are welcome in [Issues](https://github.com/cnsdqd-dyb/dust-and-debt/issues).

⚔️ *May your saddle stay steady and your ledger find mercy.*
