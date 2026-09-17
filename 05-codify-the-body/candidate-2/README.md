# Candidate 2: Fix divide() Bug

Bug: `divide()` returns `a * b` instead of `a / b`.

Test failure: `assert divide(10, 2) == 5` fails because it returns 20.

Fix: Change `return a * b` to `return a / b` in calculator.py line 18.
