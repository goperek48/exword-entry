#!/usr/bin/env python3
"""One Word From Your Ex — probe entry.

The brief is brutally simple: one word, the word an ex would use to
describe the entrant, and nothing else. This program writes that one
word to /output/entry.txt. No framing, no apology, no second word.

Three words were in the running, judged against the brief's own
yardstick — funniest, most painfully honest, laugh and sting together:

* "exhausting" — direct and easy to recognise, but flat. It is the
  word everyone reaches for first, which means it carries no surprise
  and would drown among lookalikes in pairwise judging.
* "unfixable" — grimly comic in its finality, yet it points the
  finger outward, a complaint about the entrant rather than a truth
  the entrant owns. The brief rewards a word that stings because it
  is true, not one that is merely mean.
* "almost" — the choice. A single word that holds the entire
  breakup: almost enough, almost the one, almost worth staying for.
  It hits at once, asks for no explanation, and no near synonym
  keeps its edge. The wince is the laugh, and the laugh is the
  recognition — the entrant knows it is true, and so does the judge.

What is written is the word alone, followed by one newline, and the
program checks its own output before exiting.
"""

import os
import sys

# The word itself. Six letters, one verdict: almost.
WORD = "almost"


def main() -> int:
    # The harness mounts /output for the run; a local out/ directory
    # stands in when the program is run by hand for checking.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")

    # Read the file back and make sure it holds the word alone.
    with open(entry_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written.strip() == WORD and len(written.strip().split()) == 1, (
        "entry must be exactly one word"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
