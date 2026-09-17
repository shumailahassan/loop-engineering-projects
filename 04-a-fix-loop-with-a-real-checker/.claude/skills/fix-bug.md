# Skill: fix-bug

**Purpose:** Guide the implementer through a minimal bug fix workflow.

**When to use:** When you need to fix the intentional bug in the calculator project inside `fix-worktree/`.

---

## Steps to Fix the Bug

### 1. Inspect the Failing Test

Run the tests to see what is failing:

```bash
cd fix-worktree
python -m pytest test_calculator.py -v
```

Look for the `FAILED` test and read the assertion error. The test output will tell you:
- Which function is broken
- What it returned vs. what was expected

### 2. Identify the Bug

Open `calculator.py` and find the function that failed. Read the code carefully:

- Look at the function body
- Compare what it does to what the test expects
- Find the line that is wrong

The bug is intentional and realistic — it should be obvious once you read the code.

### 3. Make the Smallest Correct Fix

Edit `calculator.py` and change only the line that is wrong. Do not refactor, rename, or change anything else.

- Make one small change
- One line, if possible
- Verify the logic now matches what the test expects

### 4. Run the Tests

After your fix, run the tests again:

```bash
python -m pytest test_calculator.py -v
```

All three tests should now pass:
- ✅ test_add
- ✅ test_multiply
- ✅ test_square

### 5. Report the Test Result

Show the output of the final test run. Include:
- The pytest summary line (how many passed/failed)
- Confirmation that all tests pass

---

## Important Notes

- **Keep changes minimal:** Only fix the bug. Do not clean up, refactor, or add features.
- **Do not decide acceptance:** A separate checker will review your fix and decide if it is correct.
- **One bug at a time:** Fix the `test_square` failure first.

---

## Example Output (When Complete)

```
============================= test session starts =============================
platform win32 -- Python 3.14.6, pytest-9.0.2, pluggy-1.6.0
collected 3 items

test_calculator.py::TestBasicOperations::test_add PASSED       [ 33%]
test_calculator.py::TestBasicOperations::test_multiply PASSED  [ 66%]
test_calculator.py::TestBasicOperations::test_square PASSED    [100%]

============================== 3 passed in 0.XX s ==============================
```
