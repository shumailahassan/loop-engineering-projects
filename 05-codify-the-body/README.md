# Codify the Body: Project 5

## Project Goal

Take the fix loop from Project 4 and codify its orchestration into one re-runnable workflow.

This project demonstrates:
- Three candidate fixes in parallel isolated worktrees
- A separate independent reviewer/checker for each candidate
- How the workflow body (maker + checker pattern) can be orchestrated as one unit
- Why this is NOT yet a loop (no heartbeat, no progress file, no retry logic)

## Project Structure

### Three Candidates (Parallel Fixes)

Each candidate is an isolated git worktree with a different intentional bug:

- **candidate-1/** (branch: `fix/candidate-1`)
  - Bug: `square()` returns `x + x` instead of `x * x`
  - Test failure: `assert square(5) == 25` fails (returns 10)
  - Fix: Change `return x + x` to `return x * x`

- **candidate-2/** (branch: `fix/candidate-2`)
  - Bug: `divide()` returns `a * b` instead of `a / b`
  - Test failure: `assert divide(10, 2) == 5` fails (returns 20)
  - Fix: Change `return a * b` to `return a / b`

- **candidate-3/** (branch: `fix/candidate-3`)
  - Bug: `multiply()` returns `a + b` instead of `a * b`
  - Test failure: `assert multiply(3, 4) == 12` fails (returns 7)
  - Fix: Change `return a + b` to `return a * b`

### Files

- **checker.py** — Independent verifier for any candidate
  - Takes a candidate path as argument
  - Runs tests and reports PASS or FAIL
  - The sole authority for acceptance

## The Workflow

The workflow (created dynamically via Claude Code's `/workflows` mechanism):

1. **Parallel Makers** — Three agents, each fixes one bug in its candidate worktree
2. **Parallel Reviewers** — Three agents, each runs the checker on its candidate
3. **Collect Verdicts** — Gather PASS/FAIL results for all three
4. **Report** — Show all results together

## Why This Is NOT Yet a Loop

A real loop would have:
- ❌ **No heartbeat** — The workflow runs once and stops; it doesn't re-run automatically
- ❌ **No progress file** — There's no state tracking what's been attempted
- ❌ **No retry logic** — Failed fixes are not retried; the workflow just reports and exits

This workflow demonstrates the **orchestration body** of a fix loop, but without these three pieces, it cannot loop.

## Running the Workflow

The workflow will be invoked via plain language through Claude Code:

```
"Use a workflow to draft fixes for these three issues in parallel worktrees, and have a reviewer grade each one."
```

The runtime will generate and execute the workflow, orchestrating all makers and reviewers in parallel.

## Expected Result

When the workflow completes:
- All three candidates will have been fixed
- The checker will verify each fix
- Results will be reported as:
  - Candidate 1: PASS
  - Candidate 2: PASS
  - Candidate 3: PASS

## Next Steps

1. Run the workflow via Claude Code
2. Observe all three candidates being fixed and reviewed in parallel
3. Save the working workflow as a reusable `/command` from the `/workflows` view
4. Demonstrate the `/command` in a fresh Claude session to prove it remembers nothing
5. Document what's missing to make it a real loop (heartbeat + progress file)
