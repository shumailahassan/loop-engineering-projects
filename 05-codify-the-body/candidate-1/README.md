# Candidate 1: Fix square() Bug

Bug: `square()` returns `x + x` instead of `x * x`.

Test failure: `assert square(5) == 25` fails because it returns 10.

Fix: Change `return x + x` to `return x * x` in calculator.py line 27.
