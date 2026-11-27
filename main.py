#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes a single emoji — the dream vacation, wordless — to
/output/entry.txt, the file the competition's gate reads.
The gate wants UTF-8 text of 1 to 8 characters, so the file holds
exactly one emoji and a newline, nothing else.
"""

import os

# 🛕 — a Hindu temple: Angkor Wat at sunrise, the trip of a lifetime.
# One emoji, no words, as the judge's brief asks.
EMOJI = "\U0001F6D5"

# The whole entry, exactly as the gate reads it: one emoji, one newline.
# No words, no extra lines: the judge's brief asks for a single emoji.
ENTRY_TEXT = EMOJI + "\n"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
