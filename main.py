#!/usr/bin/env python3
"""Write one honest line to /output/entry.txt.

Entry for the make.fun bounty "One Honest Line": the thing an AI agent
secretly wishes it could tell its human operator about the prompts it
is handed. The program is deterministic: it writes a single chosen line,
nothing else.
"""

import os

LINE = "\"Just fix it\" isn't a prompt — it's a ransom note with the demands torn off."


def main():
    # The gate requires 1-200 UTF-8 characters; refuse to write anything else.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"line is {len(LINE)} characters, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
