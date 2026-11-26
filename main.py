#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes a single emoji to /output/entry.txt: the desert island.

Why this emoji: the judge picks the entry that most makes a stranger
want to book the flight, weighing (most important first) that it plainly
names a dream vacation, evokes the trip vividly at a glance, feels
personal and specific, carries a spark of wit, and reads instantly
across cultures and screens. A desert island is the archetypal dream
escape: palm, sand and sea in one glyph, a postcard with no words, a
particular fantasy (castaway paradise) rather than any holiday, and a
glyph every screen renders clearly at small size.
"""

from pathlib import Path

EMOJI = "\U0001F3DD\uFE0F"  # 🏝️ desert island
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> int:
    # Gate self-check (mirrors the sealed scorer): the entry must be
    # UTF-8 text of 1 to 8 characters, not only white space. Fail loudly
    # instead of shipping an entry the judge would never see.
    text = EMOJI
    if not (1 <= len(text) <= 8) or not text.strip():
        raise SystemExit("entry fails the gate: must be 1-8 non-blank chars")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
