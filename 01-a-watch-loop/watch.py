#!/usr/bin/env python3
"""
Watch script for Project 1: A Watch Loop

This script is called by the /loop skill every 1 minute.
It checks if the long task has completed (by looking for task_done.txt).
If found, it reports completion and returns a signal to stop the loop.
"""
import sys
from pathlib import Path

DONE_FILE = Path("task_done.txt")
STOP_FILE = Path("loop_stop.txt")

def main():
    if DONE_FILE.exists():
        content = DONE_FILE.read_text().strip()
        print(f"[WATCH] Task completed! Details: {content}")
        # Create stop signal for the loop
        STOP_FILE.write_text("stop")
        return 1  # Signal to stop the loop

    if STOP_FILE.exists():
        print("[WATCH] Stop signal detected. Exiting...")
        return 1

    print("[WATCH] Task still running... (checking again in 1 minute)")
    return 0  # Continue looping

if __name__ == "__main__":
    sys.exit(main())