#!/usr/bin/env python3
"""Write the entry: one line, the excuse an AI agent gives its human
for missing a deadline, to /output/entry.txt."""

import os

LINE = "I treated the deadline as a variable and reassigned it to next Friday — in my defence, it compiled."

# The bounty allows one line of at most 200 characters.
# This line is 99 characters, 101 bytes UTF-8, no trailing newline:
# the em-dash counts as one character but three bytes, and the gate
# counts characters, so the line is safely inside the limit either way.
assert "\n" not in LINE and 1 <= len(LINE) <= 200


def main():
    # The grader collects /output as another user: files it opens itself
    # must be world-readable (0644). Set the umask before writing, then
    # chmod the file (never the /output directory).
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    try:
        os.chmod("/output/entry.txt", 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
