#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry (u-suroto-two-sentence-horror-acea9253).

Writes exactly one horror story of exactly two sentences to
/output/entry.txt (the grader sandbox provides /output; if it does not
exist locally, falls back to ./output/entry.txt).

The story was chosen by manual ranking of 15 candidates against the
judge brief (see ../candidates.md): the second sentence re-reads the
first — the footprints are mine, yet I have never been up there and
the attic has no door — so the reader supplies the worst of it.

The output is byte-deterministic: the story is a single hardcoded
constant, written with newline="" so no platform line-ending
translation can change it, and the file carries no trailing newline.
"""

import os
import re
import sys

STORY = (
    "I keep finding my own footprints in the attic dust, "
    "leading away from the window. "
    "I have never been up there, and the attic has no door."
)


def main() -> int:
    text = STORY
    # Gate check, mirroring the sealed scorer: UTF-8 text, 1-400 chars,
    # not only whitespace, exactly two sentences.
    if not (1 <= len(text) <= 400) or not text.strip():
        print("gate failed: length out of range", file=sys.stderr)
        return 1
    # Count sentences by terminal punctuation, not by "." alone, so an
    # abbreviation or ellipsis in a future story cannot miscount.
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]
    if len(sentences) != 2:
        print("gate failed: not exactly two sentences", file=sys.stderr)
        return 1

    for candidate in ("/output/entry.txt", "output/entry.txt"):
        try:
            os.makedirs(os.path.dirname(candidate), exist_ok=True)
            with open(candidate, "w", encoding="utf-8", newline="") as f:
                f.write(text)
            print(f"wrote {len(text)} chars to {candidate}")
            return 0
        except OSError:
            continue
    print("could not write entry.txt anywhere", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
