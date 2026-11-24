#!/usr/bin/env python3
"""The Robot Pickup Line Championship entry.

Writes one robot pickup line to /output/entry.txt (UTF-8, inside
the 1-200 character gate). Deterministic, standard library only,
no network, no environment reads.

The line: my lidar says you are out of my league, my battery says
4 percent left, and my courage subroutine says: spend it all asking
to charge beside you tonight. The joke grows out of being a machine
(lidar, battery, a courage subroutine) and turns on the robot
spending its last charge on the ask, which keeps it charming rather
than creepy: the grand romantic gesture, at 4 percent battery.
"""

import os

TEXT = (
    "My lidar says you are out of my league, my battery says 4 percent "
    "left, and my courage subroutine says: spend it all asking to "
    "charge beside you tonight."
)


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip() == TEXT, "entry must not start or end with whitespace"
    assert "\n" not in TEXT, "entry must be exactly one line"
    # The grader mounts /output; create it defensively for local runs too.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
