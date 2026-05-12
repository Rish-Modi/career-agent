#!/usr/bin/env python3
"""
Parse orchestrator. Lists raw JD files and prepares a JSON skeleton for
the LLM (Claude) to fill in. Claude does the actual extraction — this
script just enumerates the files and validates the final output.

Usage:
    python parse.py <run_dir>

Output:
    <run_dir>/parsed.skeleton.json  — empty records, one per raw file
    <run_dir>/parsed.json           — written by Claude after extraction
"""

import sys
import json
from pathlib import Path


SKELETON = {
    "id": "",
    "source_file": "",
    "url": "",
    "company": "",
    "title": "",
    "level": "",
    "required_skills": [],
    "nice_to_have": [],
    "responsibilities": [],
    "scope_signals": [],
    "comp_range": "",
    "location": "",
    "remote_policy": "",
    "red_flags": [],
    "green_flags": [],
}


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    run_dir = Path(sys.argv[1])
    raw_dir = run_dir / "raw"

    if not raw_dir.exists():
        print(f"No raw/ directory in {run_dir}. Run scrape.py first.")
        sys.exit(1)

    failed = list(raw_dir.glob("*.FAILED.txt"))
    if failed:
        print(f"ERROR: {len(failed)} raw files are still marked .FAILED.")
        print("Have the user paste JD text into each, then rename to remove .FAILED before parsing.")
        for f in failed:
            print(f"  {f.name}")
        sys.exit(2)

    raw_files = sorted(raw_dir.glob("*.txt"))
    if not raw_files:
        print("No raw .txt files found.")
        sys.exit(1)

    skeleton = []
    for i, f in enumerate(raw_files, 1):
        record = dict(SKELETON)
        record["id"] = str(i)
        record["source_file"] = f.name
        skeleton.append(record)

    skel_path = run_dir / "parsed.skeleton.json"
    skel_path.write_text(json.dumps(skeleton, indent=2))

    print(f"Found {len(raw_files)} raw files. Skeleton written to {skel_path}")
    print("\nFiles to parse:")
    for f in raw_files:
        print(f"  {f}")
    print(f"\nNext: Claude reads each raw file, fills in the records, writes {run_dir / 'parsed.json'}")


if __name__ == "__main__":
    main()
