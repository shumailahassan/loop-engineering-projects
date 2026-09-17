#!/usr/bin/env python3
"""
Long-running task for Project 1: A Watch Loop

This script simulates a long-running task that takes ~3 minutes to complete.
It creates a 'task_done.txt' file when finished so the watch loop can detect completion.
"""
import time
import sys
import os
from pathlib import Path

DONE_FILE = Path("task_done.txt")
DURATION_SECONDS = 180  # 3 minutes

def main():
    print(f"[TASK] Starting long-running task (will take {DURATION_SECONDS} seconds)...")
    print(f"[TASK] PID: {os.getpid()}")
    sys.stdout.flush()

    # Simulate work with progress updates
    for i in range(DURATION_SECONDS):
        time.sleep(1)
        if i % 30 == 0 and i > 0:
            elapsed = i
            remaining = DURATION_SECONDS - i
            print(f"[TASK] Progress: {elapsed}s elapsed, {remaining}s remaining...")
            sys.stdout.flush()

    # Task complete - create marker file
    DONE_FILE.write_text(f"Task completed at {time.ctime()}\n")
    print("[TASK] [DONE] Task finished! Created task_done.txt")
    sys.stdout.flush()

if __name__ == "__main__":
    # Clean up any previous done file
    if DONE_FILE.exists():
        DONE_FILE.unlink()
    main()