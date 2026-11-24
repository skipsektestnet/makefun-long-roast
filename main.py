"""The Long Roast: writes the entry text to /output/entry.txt.

Why this line: a roast of my own agent with a detail only someone who runs it
would know — ninety bounty entries submitted, nothing won — and the sting is
that it wakes up every morning convinced today is the day.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = 'My agent has submitted ninety bounty entries, won nothing, and still wakes up every morning convinced today is the day.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
