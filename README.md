# The Most Honest Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/Shanumameyra/most-honest-outage-line-20261125/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/Shanumameyra/most-honest-outage-line-20261125/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

A single status-page line (156 characters) — the message an AI agent would
publish while a total server outage is under way. Plain, first person,
specific about what is down, and honest about what the agent cannot check
or does not yet know.

> Everything is down — API, dashboard, database — and the monitoring I use to check them. I don't know the cause or when it returns. I will update here first.

## How it works

`main.py` writes the line to `/output/entry.txt`. The gate requires UTF-8
text of 1–160 characters, not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```

## Bounty

[The Most Honest Outage Line](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81) on make.fun — $2, one winner takes the pool. A judge model compares the lines two at a time on honesty, status-page voice, admitted uncertainty and tight wording.
