#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

The first word that came to mind: "petrichor".

Petrichor is the scent of rain falling on dry earth after a long
dry spell. It is a single, specific, sensory word: surprising
because it names something everyone has smelled but few can name,
vivid because it calls up dust, warm stone and the first drops of
a summer storm in nine letters, and a little witty because it hides
a small piece of Greek inside it — petra (stone) and ichor (the
blood of the gods) — so the smell of rain on stone is, literally,
the blood of the gods in the rocks.

The grader runs this program and reads /output/entry.txt. The file
holds exactly one word, nothing else.
"""

import os
import sys

WORD = "petrichor"


def output_path() -> str:
    """Where the entry word goes: the grader's /output, else ./output."""
    for candidate in ("/output/entry.txt", "output/entry.txt"):
        directory = os.path.dirname(candidate)
        try:
            os.makedirs(directory, exist_ok=True)
            return candidate
        except OSError:
            continue
    return "entry.txt"


def main() -> int:
    if not (1 <= len(WORD) <= 24) or not WORD.strip():
        print("entry word must be 1 to 24 non-blank characters", file=sys.stderr)
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(WORD)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != WORD:
        print(f"wrote {written!r}, expected {WORD!r}", file=sys.stderr)
        return 1
    print(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
