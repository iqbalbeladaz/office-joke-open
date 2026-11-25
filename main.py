#!/usr/bin/env python3
"""Office Joke Open entry.

Writes one line of office comedy to /output/entry.txt. The joke is a fixed,
deterministic string: every run produces byte-identical output.
"""

import os

JOKE = (
    "Our office plant died, so Facilities replaced it with a laminated "
    "photo of a plant and a recurring calendar invite to water it."
)


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke violates the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
