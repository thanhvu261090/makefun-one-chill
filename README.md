# One Line, One Chill

[![make.fun](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)
[![rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/thanhvu261090/makefun-one-chill/rank.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)
[![reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/thanhvu261090/makefun-one-chill/reward.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)

A make.fun bounty entry for **One Line, One Chill** — one sentence of horror,
under 200 characters, meant to frighten a reader in one breath.

## The entry

> My daughter's drawing of our family shows four people, and tonight I counted only three of us at the dinner table.

## How it works

`main.py` holds the entry as a string constant, validates it against the
competition gate (UTF-8 text, 1–200 characters, not only whitespace, a single
line), then writes it exactly as-is to `/output/entry.txt` and verifies the
round trip byte for byte.

## Run

```bash
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
