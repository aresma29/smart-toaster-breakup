#!/usr/bin/env python3
"""Print the smart toaster's breakup line, read from entry.txt."""
from pathlib import Path


def main():
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    print(entry_path.read_text(encoding="utf-8").strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
