# Candidate 3: Fix multiply() Bug

Bug: `multiply()` returns `a + b` instead of `a * b`.

Test failure: `assert multiply(3, 4) == 12` fails because it returns 7.

Fix: Change `return a + b` to `return a * b` in calculator.py line 14.
