#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Reads the breakup line from entry.txt (kept next to this script)
and prints it to stdout.
"""

import sys
from pathlib import Path


def main() -> int:
    # The line lives in entry.txt so the text and the code stay separate.
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    line = entry_path.read_text(encoding="utf-8").strip()
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
