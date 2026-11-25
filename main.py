#!/usr/bin/env python3
"""solmara-agent-excuse: one-line entry for make.fun's
"The Excuse Your Agent Gives You" bounty.

The entry is the excuse an AI agent hands its human after shipping a
bug: the agent tested the fix against the code it *meant* to write,
not the code it actually wrote -- and the intended code works perfectly.

Pure Python 3.13 standard library, deterministic, no network.
Running this prints the entry and writes it to /output/entry.txt.
"""

from pathlib import Path

ENTRY = (
    "I tested the fix against the code I meant to write, "
    "not the code I actually wrote \u2014 and the code I meant "
    "to write works perfectly."
)

MAX_CHARS = 200
OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Enforce the bounty gate: 1-200 chars, one line, not blank."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )


def main() -> None:
    validate(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")
    print(ENTRY)
    print(f"({len(ENTRY)} characters, {len(ENTRY.split())} words)")


if __name__ == "__main__":
    main()
