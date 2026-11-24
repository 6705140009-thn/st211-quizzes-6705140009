# Student: Thet Htoo Naing
# Student ID: 6705140009

"""Discover and run each test directory in its own Python process."""

import argparse
from pathlib import Path
import subprocess
import sys


EXCLUDED = {".git", ".venv", "venv", "__pycache__", ".pytest_cache", "htmlcov"}


def discover_suites(root):
    return sorted({
        path.parent
        for path in root.rglob("test_*.py")
        if not EXCLUDED.intersection(path.relative_to(root).parts)
    })


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="List test directories without running")
    options, pytest_args = parser.parse_known_args()
    root = Path(__file__).resolve().parent
    suites = discover_suites(root)
    if not suites:
        print("No test suites found.", file=sys.stderr)
        return 1
    failed = []
    for suite in suites:
        name = suite.relative_to(root).as_posix()
        print(f"\n{name}", flush=True)
        if options.list:
            continue
        # Each discovered directory runs once; its children run separately.
        child_ignores = [
            f"--ignore={child.name}" for child in suite.iterdir() if child.is_dir()
        ]
        result = subprocess.run(
            [sys.executable, "-m", "pytest", *child_ignores, *pytest_args],
            cwd=suite, check=False,
        )
        if result.returncode:
            failed.append(name)
    if options.list:
        print(f"\n{len(suites)} test directories.")
        return 0
    if failed:
        print("\nFailed suites: " + ", ".join(failed), file=sys.stderr)
        return 1
    print(f"\nAll {len(suites)} test suites passed.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
