# A Fix Loop with a Real Checker

## Project Goal

Demonstrate a maker-checker fix loop: an implementer makes small, testable fixes to code, while an independent checker verifies whether the fix is correct by running automated tests. The checker is the sole authority for acceptance.

## Project Structure

This project uses a **Git worktree** to isolate the fix work:

- **Main repository:** `04-a-fix-loop-with-a-real-checker/`
- **Worktree:** `fix-worktree/` (on branch `fix/bug-fix`)
- **Branch:** `fix/bug-fix` (created specifically for this fix loop)

## Project Files

### Inside `fix-worktree/`

**calculator.py**
- A simple calculator module with four arithmetic functions: `add()`, `multiply()`, `divide()`, and `square()`.
- Contains an intentional bug in the `square()` function for demonstration.

**test_calculator.py**
- Pytest test suite with 3 tests: `test_add()`, `test_multiply()`, and `test_square()`.
- Tests verify correct behavior; the `test_square()` test initially fails due to the bug.

**README.md**
- Explains the small project and the intentional bug.
- Documents the bug and how to fix it.

### In Main Repository

**checker.py**
- Independent verification script that runs tests and reports results.
- Does not modify any project files.
- Reports `PASS` if all tests pass, `FAIL` with reason if any test fails.
- The checker is the sole authority for accepting or rejecting a fix.

**.claude/skills/fix-bug.md**
- A beginner-friendly skill guide for the implementer.
- Provides 5 clear steps:
  1. Inspect the failing test
  2. Identify the bug
  3. Make the smallest correct fix
  4. Run the tests
  5. Report the test result
- Emphasizes keeping changes minimal and not deciding acceptance (that's the checker's job).

## The Intentional Bug

The `square(x)` function in `calculator.py` had a bug:

```python
def square(x):
    """Return the square of a number."""
    return x + x  # Bug: adds instead of multiplying
```

**Impact:**
- `square(5)` returned `10` instead of `25`
- `square(0)` returned `0` (accidentally correct)
- `square(-3)` returned `-6` instead of `9`

**Initial test result:** `test_square()` failed with `assert 10 == 25`

## The Fix

The implementer made the smallest possible fix:

**Changed line 27 in `calculator.py`:**
```python
return x * x  # Fixed: now multiplies correctly
```

**Verification:** All 3 tests passed.

## The Checker Verification

The independent `checker.py` verified the fix:

```
PASS

============================= test session starts =============================
collected 3 items

test_calculator.py::TestBasicOperations::test_add PASSED       [ 33%]
test_calculator.py::TestBasicOperations::test_multiply PASSED  [ 66%]
test_calculator.py::TestBasicOperations::test_square PASSED    [100%]

============================== 3 passed in 0.06s ==============================
```

## Demonstration: Bad Fix Rejection

To demonstrate the checker's validation, a bad fix was intentionally introduced:

**Bad fix:** Changed `square()` to `return x + 1`

**Checker result:** `FAIL`

```
FAIL

test_calculator.py::TestBasicOperations::test_square FAILED

>       assert square(5) == 25
E       assert 6 == 25
E        +  where 6 = square(5)

test_calculator.py:28: AssertionError
```

The checker correctly rejected the bad fix and showed exactly why: `square(5)` returned `6` instead of `25`.

## Restoration and Final Verification

The correct fix was restored: `return x * x`

**Final checker result:** `PASS`

```
PASS

============================== 3 passed in 0.06s ==============================
```

## Key Lesson

**The Maker-Checker Pattern:**

- **Maker (Implementer):** Inspects the failing test, identifies the bug, makes the smallest correct fix, and runs tests locally to verify.
- **Checker (Authority):** Independently runs the same tests and decides acceptance. The checker does not modify code; it only verifies and reports.

**Separation of Concerns:**
- The maker focuses on the fix.
- The checker focuses on validation.
- The checker is the sole decision authority.

This pattern ensures:
- ✅ Fixes are minimal and focused
- ✅ Tests are the source of truth
- ✅ Acceptance is objective and independent
- ✅ No one person decides whether a fix is correct

## Running the Project

**To fix the bug:**
```bash
cd fix-worktree
python -m pytest test_calculator.py -v  # See the failing test
# Edit calculator.py to fix the bug
python -m pytest test_calculator.py -v  # Verify the fix locally
```

**To check if the fix passes (from main repo):**
```bash
python checker.py
```

The checker will report `PASS` or `FAIL` with details.
