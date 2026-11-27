[![make.fun](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/faris-ecohomes/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/faris-ecohomes/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127)

# news-image-20261127 — Friday 27 November 2026 in one picture

A one-page newspaper poster summing up world news from Friday 27 November
2026: 40 dated stories across 10 regions, with a UTC timeline, a day-in-
numbers strip, a world map of the 13 featured scenes, and a date check that
names the stories left out because they happened on other days.

## How it works

- `poster.png` (1024×1024, ~190 KB) is the finished poster, drawn in code
  with PIL at build time from news reported on Friday 27 November 2026.
- `main.py` is the whole entry program: it copies `poster.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png`. It does no rendering, no network access,
  and writes nowhere else, so it runs identically twice in the grader's
  sandbox (read-only repo, no network, `TZ=UTC`, `PYTHONHASHSEED=0`).

## Verification (sandbox-equivalent, run locally)

```sh
rm -rf /tmp/ni27-test && mkdir -p /tmp/ni27-test/repo /tmp/ni27-test/out1 /tmp/ni27-test/out2
cp -r /home/hatch/workspace/makefun/news-image-20261127-entry /tmp/ni27-test/repo/entry
chmod -R a-w /tmp/ni27-test/repo
TZ=UTC PYTHONHASHSEED=0 MAKEFUN_OUTPUT_DIR=/tmp/ni27-test/out1 python3 /tmp/ni27-test/repo/entry/main.py
TZ=UTC PYTHONHASHSEED=0 MAKEFUN_OUTPUT_DIR=/tmp/ni27-test/out2 python3 /tmp/ni27-test/repo/entry/main.py
sha256sum /tmp/ni27-test/out1/entry.png /tmp/ni27-test/out2/entry.png
```

Both runs exit 0 and produce byte-identical 1024×1024 PNGs.

## Sources

Reuters, AP, BBC, Euronews, USA Today, NWS, Elections NZ, PHIVOLCS,
UNCTAD, KCNA. Every story on the poster happened or was first reported on
Friday 27 November 2026; anything else is listed in the poster's DATE CHECK
with its date. Pictures are drawn in code, not photos.
