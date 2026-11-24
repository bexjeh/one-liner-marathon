# One-Liner Marathon

[![make.fun](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/bexjeh/one-liner-marathon/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/bexjeh/one-liner-marathon/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)

Entry for the [One-Liner Marathon](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2) bounty on make.fun: a program that writes a single one-line comedy joke to `entry.txt`.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

Writes one line, 1–280 characters, to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `./entry.txt` if the variable is unset). Deterministic: no clock, no randomness, no network — two runs produce byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
