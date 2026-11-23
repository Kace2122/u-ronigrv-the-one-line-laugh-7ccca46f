"""The One-Line Laugh: write one funny line to /output/entry.txt.

The line is a single sentence of at most 200 characters: an everyday
truth (a smartwatch cheering a stand-up) with the surprise saved for
the end (the applause comes from a machine that needs charging too).
"""

import os

LINE = "My smartwatch congratulated me for standing up today, which is the saddest applause I have ever received from a machine I have to charge every night."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # One sentence, inside the 1-200 character gate.
    assert LINE.endswith(".") and LINE.count(".") == 1
    assert 1 <= len(LINE) <= 200
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read it back: the artifact on disk must be exactly the line.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        assert f.read() == LINE


if __name__ == "__main__":
    main()
