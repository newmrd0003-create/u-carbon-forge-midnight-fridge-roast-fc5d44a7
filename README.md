# Midnight Fridge Roast

[![Midnight Fridge Roast](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/newmrd0003-create/u-carbon-forge-midnight-fridge-roast-fc5d44a7/rank.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/newmrd0003-create/u-carbon-forge-midnight-fridge-roast-fc5d44a7/reward.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)

One-line roast of a smart fridge that refuses to open after midnight. The fridge turns petty librarian: lights off, door locked, and a little "Shhh" sign — the leftovers are sleeping, and frankly, so should you.

## Run

```sh
python3 main.py
```

Writes the entry (146 characters, UTF-8, single line) to `/output/entry.txt` and verifies the file on disk is byte-identical to the entry. `validate()` checks the gate: 1–200 characters, not only whitespace, single line, valid UTF-8.
