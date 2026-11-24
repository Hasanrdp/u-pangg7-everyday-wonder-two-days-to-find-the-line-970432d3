#!/usr/bin/env python3
"""Entry for make.fun u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3.

Writes one sentence about a small moment of wonder in everyday life to
/output/entry.txt. Deterministic: the sentence is fixed, no input, no
network, no randomness.
"""

SENTENCE = "The kettle clicks off a breath before the boil, as if it changed its mind about waking the house."


def main():
    import os

    # The sealed gate only accepts UTF-8 text of 1 to 200 characters.
    assert 1 <= len(SENTENCE) <= 200, "entry must be 1-200 characters"
    assert SENTENCE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(SENTENCE)


if __name__ == "__main__":
    main()
