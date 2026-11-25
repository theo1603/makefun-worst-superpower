#!/usr/bin/env python3
"""Worst Superpower.

Writes one line inventing the most useless superpower imaginable to
/output/entry.txt: the ability to summon rain, but only a single drop, only
directly above the hero's own head, and only on days they remembered their
umbrella — so the one time the power works, it changes nothing at all.

Deterministic, stdlib only, no network, no input.
"""

import os

LINE = (
    "I can summon rain, but only a single drop, only directly above my own "
    "head, and only on days I remembered my umbrella."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
