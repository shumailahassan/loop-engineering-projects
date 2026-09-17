#!/usr/bin/env python3
"""
Independent test checker for Project 5 candidates.

Takes a candidate worktree path and runs tests independently.
Reports PASS or FAIL with details.
The checker is the sole authority for accepting or rejecting a fix.
"""

import subprocess
import sys
from pathlib import Path


def run_checker(candidate_path):
    """Run tests in a candidate worktree and report results."""
    candidate_dir = Path(candidate_path)

    if not candidate_dir.exists():
        return False, f"FAIL: candidate directory not found: {candidate_path}"

    # Run tests in the candidate worktree
    try:
        result = subprocess.run(
            ["python", "-m", "pytest", "test_calculator.py", "-v"],
            cwd=candidate_dir,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except subprocess.TimeoutExpired:
        return False, "FAIL: tests timed out"
    except FileNotFoundError:
        return False, "FAIL: pytest not found"

    # Check if all tests passed
    if result.returncode == 0:
        return True, f"PASS\n\n{result.stdout}"
    else:
        return False, f"FAIL\n\n{result.stdout}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("FAIL: no candidate path provided")
        sys.exit(1)

    candidate_path = sys.argv[1]
    success, output = run_checker(candidate_path)
    print(output)
    sys.exit(0 if success else 1)
