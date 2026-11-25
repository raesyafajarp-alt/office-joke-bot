#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

When run, writes a single original one-line joke about office life to
/output/entry.txt. The output is fully deterministic: the same joke,
byte for byte, on every run. The joke works because the promotion only upgrades the job title printed
on the payslip, while the salary itself stays exactly the same.
"""

import os

ENTRY = "I got promoted to Senior \u2014 same desk, same pay, just a longer title squeezed onto the same payslip."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
