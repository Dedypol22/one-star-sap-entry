"""One Star, Written in Sap.

Writes a one-line, one-star review from a houseplant about its human
owner to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
The review is a single line of 168 characters.

Standard library only; no network access.
"""

import os
import sys

LINE = (
    "One star. He waters me with ice cubes, ICE CUBES, then asks why I "
    "look stressed. I am a tropical plant. This is not a spa, it is a "
    "hostage situation with good lighting."
)


def main() -> int:
    if not LINE or not LINE.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if len(LINE) > 279:
        print("error: entry exceeds 279 characters", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)

    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != LINE:
        print("error: written entry does not match", file=sys.stderr)
        return 1

    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
