#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — writes one line to /output/entry.txt."""

import os

ENTRY = (
    "My lidar mapped that corner as a cliff, so I filed it under "
    "'do not enter' and went back to my dock for emotional support."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
