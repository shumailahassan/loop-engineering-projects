
export const meta = {
  name: 'codify-the-body-workflow',
  description: 'Fix three bugs in parallel worktrees, verify each with independent checker',
  phases: [
    { title: 'Fix', detail: 'Three makers fix bugs in parallel candidate worktrees' },
    { title: 'Verify', detail: 'Three reviewers run checker on each candidate independently' },
  ],
}

const CANDIDATES = [
  {
    id: 1,
    path: 'C:\\Users\\HC\\loop_project\\05-codify-the-body\\candidate-1',
    bug: 'square() returns x + x instead of x * x',
    fix: 'Change return x + x to return x * x in square() function',
  },
  {
    id: 2,
    path: 'C:\\Users\\HC\\loop_project\\05-codify-the-body\\candidate-2',
    bug: 'divide() returns a * b instead of a / b',
    fix: 'Change return a * b to return a / b in divide() function',
  },
  {
    id: 3,
    path: 'C:\\Users\\HC\\loop_project\\05-codify-the-body\\candidate-3',
    bug: 'multiply() returns a + b instead of a * b',
    fix: 'Change return a + b to return a * b in multiply() function',
  },
]

// Phase 1: Fix bugs in parallel
phase('Fix')
const fixes = await parallel(CANDIDATES.map(candidate => () =>
  agent(
    `You are a code fixer. Fix this bug:
Bug: ${candidate.bug}
Fix: ${candidate.fix}
Location: ${candidate.path}/calculator.py

Read the file, identify the exact line with the bug, and fix it.
Then verify the file contains your fix by reading it again.
Report: FIXED or FAILED.`,
    {
      label: `maker-candidate-${candidate.id}`,
      phase: 'Fix',
    }
  )
))

// Phase 2: Verify fixes in parallel
phase('Verify')
const verifications = await parallel(CANDIDATES.map((candidate, index) => () =>
  agent(
    `You are a code reviewer. Verify the fix for candidate-${candidate.id}.

Run the checker to verify: python ${candidate.path}\\checker.py "${candidate.path}"

Parse the output: if it says "PASS", the fix is VERIFIED. If it says "FAIL", the fix is NOT verified.
Report the result as: PASS or FAIL.`,
    {
      label: `reviewer-candidate-${candidate.id}`,
      phase: 'Verify',
    }
  )
))

// Report results
log('Workflow complete')
return {
  candidates: CANDIDATES,
  fixes: fixes.map((f, i) => ({
    candidate: i + 1,
    makerResult: f,
  })),
  verifications: verifications.map((v, i) => ({
    candidate: i + 1,
    reviewerResult: v,
  })),
}
