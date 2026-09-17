#!/usr/bin/env python3
"""
Independent test checker for the calculator project.

This script runs tests in fix-worktree and reports PASS or FAIL.
It does NOT modify any project files.
It is the authority for accepting or rejecting a fix.
"""

import subprocess
import sys
from pathlib import Path


def run_checker():
    """Run tests and report results."""
    # Get the worktree directory
    worktree_dir = Path(__file__).parent / "fix-worktree"

    if not worktree_dir.exists():
        print("FAIL: fix-worktree directory not found")
        return False

    # Change to worktree and run tests
    try:
        result = subprocess.run(
            ["python", "-m", "pytest", "test_calculator.py", "-v"],
            cwd=worktree_dir,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except subprocess.TimeoutExpired:
        print("FAIL: tests timed out")
        return False
    except FileNotFoundError:
        print("FAIL: pytest not found")
        return False

    # Check if all tests passed
    if result.returncode == 0:
        print("PASS")
        print("\n" + result.stdout)
        return True
    else:
        print("FAIL")
        print("\n" + result.stdout)
        if result.stderr:
            print(result.stderr)
        return False


if __name__ == "__main__":
    success = run_checker()
    sys.exit(0 if success else 1)
