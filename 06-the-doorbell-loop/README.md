# Project 6: "The Doorbell Loop" — Event-Driven Code Review

## Project Purpose

This project implements an automated code review system triggered by GitHub pull request events. When a PR is opened or receives new commits, a GitHub Actions workflow automatically calls the Groq API to perform code review and posts the results as a PR comment.

The name "Doorbell Loop" reflects the pattern: a GitHub event (the "doorbell ring") triggers an automated response (the "loop"), without manual intervention.

## What We Built

### GitHub Actions Workflow: `.github/workflows/pr-code-review.yml`

A GitHub Actions workflow that:

1. **Triggers on PR events**: Activates when a pull request is opened or when new commits are pushed (synchronize event)
2. **Extracts PR diff**: Generates the unified diff between the PR base and head commits
3. **Calls Groq API**: Sends the PR diff to Groq via the OpenAI-compatible API with a code review prompt
4. **Posts results**: Comments on the PR with the code review findings

### Workflow Steps

1. **Checkout**: Clones the repository with full history to enable diff computation
2. **Get PR diff**: Generates the unified diff between base and head branches
3. **Call Groq API**: Makes an authenticated request to `openai/gpt-oss-20b` for code review
4. **Post review**: Creates a PR comment with the review results
5. **Error handling**: Posts a diagnostic comment if the review fails

## How It Works

### Triggering the Workflow

The workflow activates automatically on:
- **Pull request opened**: When a new PR is created
- **Pull request synchronized**: When new commits are pushed to an existing PR branch

### The Review Process

1. GitHub Actions checks out the PR code
2. The workflow computes the diff between the base branch and the PR branch
3. It calls the Groq API (`openai/gpt-oss-20b`) with:
   - Full unified diff of changes
4. The Groq model performs code review and returns structured feedback
5. Results are posted as a comment on the PR

### What the Review Covers

The code review analyzes:
- Key observations about the changes
- Potential bugs or issues
- Suggestions for improvement
- Overall assessment of the code quality

## Setup Requirements

### 1. Repository Setup

The workflow file is already in place at `.github/workflows/pr-code-review.yml`. Commit this file to your repository if it hasn't been committed yet.

### 2. GitHub Secret: `GROQ_API_KEY`

**Critical:** The workflow requires your Groq API key to authenticate with the API.

To configure this:

1. Go to your repository on GitHub
2. Navigate to **Settings > Secrets and variables > Actions**
3. Click **New repository secret**
4. Name: `GROQ_API_KEY`
5. Value: Your Groq API key (found at https://console.groq.com/keys)
6. Click **Add secret**

### 3. Permissions

The workflow requires:
- `contents: read` — to read the repository code
- `pull-requests: write` — to post comments on PRs

These permissions are configured in the workflow file.

## Testing Project 6

### Test Scenario 1: Create a PR with Changes

1. Create a new branch:
   ```bash
   git checkout -b test/doorbell-review
   ```

2. Make some changes to a file (e.g., add a new feature or fix)

3. Commit and push:
   ```bash
   git add .
   git commit -m "Test change for code review"
   git push origin test/doorbell-review
   ```

4. Create a pull request on GitHub from `test/doorbell-review` to `master`

5. Watch the workflow:
   - Go to your repository on GitHub
   - Navigate to **Actions** tab
   - Select the **Doorbell Loop - PR Code Review** workflow
   - You should see the workflow running

6. Check for the review comment:
   - Once the workflow completes, return to your PR
   - Scroll down to see the **🔔 Doorbell Loop - Automated Code Review** comment with the model's feedback

### Test Scenario 2: Push New Commits

1. While the PR is still open, make another change to the same branch:
   ```bash
   git add .
   git commit -m "Additional change for review"
   git push origin test/doorbell-review
   ```

2. The workflow will trigger again automatically (synchronize event)

3. A new review comment will be posted for the updated diff

### Troubleshooting

**Workflow doesn't trigger:**
- Ensure the workflow file is committed and pushed to `master` branch
- Check that the branch protection rules don't prevent the workflow from running

**Review comment says "Review Failed":**
- Verify that `GROQ_API_KEY` secret is configured in your repository settings
- Check the GitHub Actions logs for detailed error messages:
  - Go to **Actions** > **Doorbell Loop - PR Code Review** > select the failed run
  - Click the job to see detailed logs

**API key error in logs:**
- Ensure your Groq API key is valid and has sufficient quota

## Architecture

```
GitHub PR Event
     ↓
.github/workflows/pr-code-review.yml
     ↓
Extract PR diff
     ↓
Call Groq API (openai/gpt-oss-20b)
     ↓
Post review comment on PR
```

The workflow is entirely event-driven — no polling, no scheduled loops. It responds immediately to PR activity.

## Files

- `.github/workflows/pr-code-review.yml` — The GitHub Actions workflow for automated code review
- `README.md` — This file, documenting the implementation

## Next Steps

1. Configure the API key secret in your GitHub repository (see Setup Requirements → GitHub Secret above)

2. Test the workflow by creating a test PR (see Testing Project 6 above)

3. Iterate on the prompt in the workflow file if you want different review criteria or feedback format

## Design Decisions

- **GitHub Actions, not local polling**: Uses GitHub's native event system instead of `/loop` polling for instant response and no local resource usage
- **Groq API**: Provides fast, cost-effective inference for code review
- **Single comment per review**: Posts one comment per workflow run to keep the PR discussion clean
- **Diff-based review**: Focuses review on changed code, not the entire repository

## Related Loop Engineering Projects

- **Project 1 (A Watch Loop)**: Demonstrates monitoring for task completion
- **Project 2 (Make Tests Pass)**: Shows test-driven workflows
- **Project 3 (Morning Brief)**: Memory-based automation
- **Project 4 (Fix Loop)**: Iterative problem-solving
- **Project 5 (Codify the Body)**: Multi-candidate evaluation
- **Project 6 (Doorbell Loop)**: Event-driven automation ← You are here

## Security Considerations

- The workflow runs with `contents: read` only — it cannot modify code
- The API key is stored as a GitHub secret and is not exposed in logs
- PR diffs are sent to the Groq API; review your organization's policies if handling sensitive data
- Comments are public on the repository

## References

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub API - Pull Requests](https://docs.github.com/en/rest/pulls)
- [Groq API Documentation](https://console.groq.com/docs)
