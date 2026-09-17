# The Morning Brief with a Memory

A beginner-friendly loop project that gathers information from a repository and writes a daily summary.

## How It Works

The loop:
1. **Reads** `progress.md` at startup to remember previous findings
2. **Gathers** information from the repository:
   - TODO comments in code files
   - Recent git commits
   - Changed files (unstaged)
3. **Writes** a brief summary of what it found
4. **Updates** `progress.md` with the date and findings

## Files

- **progress.md** — The spine/memory file. Persists across loop runs. Tracks what was found and when.
- **loop.js** — Helper functions for gathering repository information (TODOs, commits, changed files).
- **README.md** — This file.

## Next Steps

1. Add your own project files (the loop will scan them for TODOs)
2. Make some git commits (the loop will list recent ones)
3. When ready, run the loop with: `/loop`

The loop will execute once immediately, then you can set it to run on a schedule.
