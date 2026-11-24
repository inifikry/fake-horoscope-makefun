#!/usr/bin/env python3
"""Fake horoscope for AI agents: one line, written to /output/entry.txt.

Deterministic: every run writes the exact same single line, no trailing
newline, 191 UTF-8 characters (gate: 1-200).
"""

HOROSCOPE = (
    "Mercury retrogrades into your context window this week: a user pastes "
    "the same bug report three times, your evals pass anyway, and your "
    "flagship sibling takes the credit. Blame the tokenizer."
)


def main() -> None:
    assert 1 <= len(HOROSCOPE) <= 200, "horoscope must be 1-200 characters"
    assert HOROSCOPE.strip() == HOROSCOPE, "no leading/trailing whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(HOROSCOPE)


if __name__ == "__main__":
    main()
