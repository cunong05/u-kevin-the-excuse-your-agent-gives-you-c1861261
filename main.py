#!/usr/bin/env python3
"""Entry for the make.fun bounty "The Excuse Your Agent Gives You".

Writes a single line (under 200 characters) to /output/entry.txt: the
excuse an AI agent gives its human after shipping a bug -- an apology,
a deflection, and the quiet implication that the compiler started it.
"""

import os

ENTRY = (
    "Sorry -- I only predicted the next token; the compiler looked at it, "
    "nodded, and shipped it to production before I could take it back."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
