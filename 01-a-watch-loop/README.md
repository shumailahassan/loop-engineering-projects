# A Watch Loop

## Project Purpose

This project demonstrates how to watch a long-running task without manually checking the terminal. Instead of waiting and watching, a script monitors for completion and reports when the task is done.

## What We Built

### `long_task.py`
A simulated long-running task that:
- Takes approximately 180 seconds (3 minutes) to complete
- Prints progress updates every 30 seconds
- Creates a `task_done.txt` file when finished to signal completion

### `watch.py`
A monitor script that:
- Checks for the existence of `task_done.txt`
- Reports the task completion details if the file exists
- Exits cleanly once completion is detected

### `task_done.txt`
A marker file created by `long_task.py` when the task finishes. Contains:
- A timestamp of when the task completed
- Signals to `watch.py` that work is done

## How It Works

1. Run `python long_task.py` to start the long-running task in the background
2. Use `/loop 1m python watch.py` to schedule the watch script to run every minute
3. The watch script checks for `task_done.txt` and reports completion
4. Once completion is detected and reported, cancel the loop with `CronDelete`

## What Happened

- The long-running task simulated 180 seconds of work with periodic progress updates
- The watch loop ran every minute, checking for task completion
- When the task finished, it created `task_done.txt` with timestamp: `Mon Sep 14 20:56:44 2026`
- The watch script detected and reported the completion
- All scheduled watch loops were then cancelled since the work was done

## Key Learning

The main insight: You don't need to sit and watch a terminal for a long task to finish. Instead, use a scheduled monitoring loop to detect when work is complete, then act accordingly. This is the foundation for autonomous task management and alerting systems.
