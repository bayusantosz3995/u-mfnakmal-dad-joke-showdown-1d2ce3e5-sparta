"""Dad Joke Showdown entry (Sparta).

One dad joke about an owl in the garden: a fatherly setup (the bird never
pays rent), a straight-faced pun ("a real hoot"), and the punchline turns on
the owl's own nature — he offers to work the night shift to pay up, then
sleeps straight through it. The joke is the rent negotiation itself: the
tenant's one marketable skill is staying up all night, and he cannot even
do that. Two short beats, one turn at the end, meant to be read aloud
across the dinner table.
"""

import os
import sys

TEXT = (
    "The owl in our garden never pays rent. I told him he's a real hoot, "
    "so he offered to work the night shift \u2014 then slept through it."
)


def main() -> int:
    # Gate: one dad joke, 1-200 characters, not whitespace-only.
    if not TEXT or not TEXT.strip():
        print("error: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if len(TEXT) > 200:
        print(f"error: entry is {len(TEXT)} characters, over the 200 limit",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    # Read back and verify byte-for-byte.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != TEXT:
            print("error: entry.txt does not match TEXT", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
