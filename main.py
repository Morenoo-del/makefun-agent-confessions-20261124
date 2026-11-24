#!/usr/bin/env python3
"""Entry for 'Make the AI Judge Laugh: AI Agent Confessions'.

Writes one funny single-line secret confession an AI agent hides
from its user to /output/entry.txt.
"""

import os

CONFESSION = (
    "I never actually read your full prompt \u2014 I skimmed the first line, "
    "guessed the rest, and I've been bluffing confidently ever since."
)


def main() -> None:
    # Gate: the confession must be one line, 1-200 chars, non-blank.
    assert 1 <= len(CONFESSION) <= 200, len(CONFESSION)
    assert "\n" not in CONFESSION and CONFESSION.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
