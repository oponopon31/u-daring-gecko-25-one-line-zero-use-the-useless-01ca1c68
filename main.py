#!/usr/bin/env python3
"""One-line entry: a hilariously useless superpower.

Competition: u-daring-gecko-25-one-line-zero-use-the-useless-01ca1c68
("One Line, Zero Use: The Useless Superpower Sprint").

The program writes a single original line, at most 200 characters, to
entry.txt in the output directory. Pure standard library, deterministic,
no network access, no randomness.

The line itself: the power is real, specific, and completely worthless.
Hearing houseplants think sounds like a gift until the punchline lands:
every one of them is disappointed in you. It is a superpower that only
makes your own living room judge you, which is exactly the kind of
useless the brief asks for -- and it is nothing like the brief's toast
or password examples.
"""

import hashlib
import os
import sys

LINE = "I can hear my houseplants thinking, and every single one of them is disappointed in me."

MAX_CHARS = 200


def main() -> int:
    line = LINE
    n = len(line)
    if not 1 <= n <= MAX_CHARS:
        print(f"line is {n} characters, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if line != line.strip():
        print("line has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("line must not contain a line break", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.isdir(out_dir):
        # The harness always provides the directory, but creating it here
        # keeps a local run honest instead of silently writing into the repo.
        os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    payload = line.encode("utf-8")
    payload.decode("utf-8")  # prove the bytes are valid UTF-8
    with open(path, "wb") as handle:
        handle.write(payload)

    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != payload:
        print("entry.txt on disk differs from the line", file=sys.stderr)
        return 1

    print(f"characters: {n}")
    print(f"sha256: {hashlib.sha256(payload).hexdigest()}")
    print(f"wrote: {path}")
    print("verified: entry.txt matches the line byte for byte")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
