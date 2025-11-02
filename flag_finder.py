#!/usr/bin/env python3
"""
Flag Finder CLI
---------------
Recursively scans a directory for strings that match the pattern ctf{...}.

Usage:
    python3 flag_finder.py
    ./flag_finder.py 
"""
import argparse
import re
from pathlib import Path

DEFAULT_PATTERN = r"ctf\{[^}]{1,100}\}"

def scan_file(path: Path, regex):
    """Return a list of (path, line_number, match_string) for this file."""
    results = []
    try:
        with path.open("r", errors="ignore") as f:
            for i, line in enumerate(f, 1):
                for m in regex.finditer(line):
                    results.append((path, i, m.group(0)))
    except Exception:
        # Skip unreadable or binary files gracefully
        pass
    return results

def scan_dir(root: Path, pattern: str):
    """Scan directory recursively for matches to pattern."""
    regex = re.compile(pattern)
    hits = []
    for p in root.rglob("*"):
        if p.is_file():
            hits.extend(scan_file(p, regex))
    return hits

def main():
    parser = argparse.ArgumentParser(description="Find ctf{...} flags in a directory.")
    parser.add_argument("path", help="Directory to scan")
    parser.add_argument("--pattern", default=DEFAULT_PATTERN,
                        help=f"Regex pattern (default: {DEFAULT_PATTERN})")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.exists() or not root.is_dir():
        print(f"[!] Not a directory: {root}")
        raise SystemExit(2)

    hits = scan_dir(root, args.pattern)
    if not hits:
        print("No flags found.")
        raise SystemExit(1)

    seen = set()
    for path, lineno, text in hits:
        if text not in seen:
            seen.add(text)
            print(f"{text}  ->  {path}:{lineno}")

if __name__ == "__main__":
    main()
