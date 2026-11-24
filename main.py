#!/usr/bin/env python3
"""One-Liner Marathon entry: writes one one-line comedy joke to entry.txt.

Deterministic by design: no clock, no randomness, no network, no input
beyond the output directory. Every run writes the same bytes.
"""

import os

JOKE = (
    "The cloud told me my storage is full, which is how I learned "
    "infinity costs $2.99 a month."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
