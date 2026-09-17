# Project 2: Make the Tests Pass, Then Stop

## Purpose

This project demonstrates the test-driven development (TDD) workflow using the `/goal` loop in Claude Code. The goal is to fix failing code by making all tests pass, then stop — no over-engineering, no extra features.

## What We Built

### `calculator.py`
A minimal Python module with three arithmetic functions:
- `add(a, b)` — returns the sum of two numbers
- `subtract(a, b)` — returns the difference
- `multiply(a, b)` — returns the product

### `test_calculator.py`
A test suite with three unit tests (using Python's `unittest`):
- `test_add_two_numbers` — verifies `add(2, 3)` returns `5`
- `test_subtract_two_numbers` — verifies `subtract(10, 4)` returns `6`
- `test_multiply_two_numbers` — verifies `multiply(3, 7)` returns `21`

## Why Tests Initially Failed

The `calculator.py` functions were stubs that returned `0` instead of performing calculations. This forced the test runner to catch the bugs.

## How `/goal` Was Used

The `/goal` command invoked a loop with the directive:
> "Make all tests pass by fixing calculator.py. After each change, run: `python -m pytest test_calculator.py -v`. Stop immediately when all tests pass. Maximum 6 attempts."

This loop kept Claude focused on the single objective: get all tests green, then stop.

## Why `pytest` Was the Checker

`pytest` is Python's standard test runner. It:
- Discovers tests automatically
- Reports pass/fail clearly
- Provides readable output
- Exits with code 0 (all pass) or 1 (any fail)

The `-v` flag shows each test result individually.

## The 6-Attempt Limit

The limit enforced a constraint: solve the problem efficiently. It discouraged trial-and-error and encouraged a direct fix.

## Final Result

✅ **All 3 tests passed in 1 attempt**

```
test_calculator.py::TestCalculator::test_add_two_numbers PASSED
test_calculator.py::TestCalculator::test_multiply_two_numbers PASSED
test_calculator.py::TestCalculator::test_subtract_two_numbers PASSED

============================== 3 passed in 0.06s ==============================
```

The fix was simple: replace `return 0` with the actual arithmetic operations.

## What I Learned from Project 2

1. **Tests are the spec** — They define exactly what the code must do. No ambiguity.
2. **TDD works** — Write failing tests first, then fix code. The test suite is your guardrail.
3. **Stop when done** — The `/goal` loop enforces discipline. Once tests pass, the job is complete. No refactoring, no "improvements," no feature creep.
4. **Minimal is better** — Three functions, three tests, two files. No boilerplate, no frameworks. Just the essentials.
5. **Automated checking beats manual review** — The test runner is objective and repeatable. It can't be fooled.
