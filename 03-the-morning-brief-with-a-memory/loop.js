#!/usr/bin/env node
/**
 * The Morning Brief with a Memory
 *
 * This loop runs daily to:
 * 1. Read progress.md (memory of previous runs)
 * 2. Gather information from the repository (TODOs, recent commits, file changes)
 * 3. Write a brief summary of findings
 * 4. Update progress.md with the date and what was found
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Path to progress file
const progressPath = path.join(__dirname, 'progress.md');

// Read current progress
function readProgress() {
  try {
    return fs.readFileSync(progressPath, 'utf-8');
  } catch (e) {
    return null;
  }
}

// Write updated progress
function writeProgress(content) {
  fs.writeFileSync(progressPath, content, 'utf-8');
}

// Gather repository information
function gatherInfo() {
  const info = {
    timestamp: new Date().toISOString(),
    todos: [],
    recentCommits: [],
    changedFiles: []
  };

  try {
    // Look for TODO comments in .js, .ts, .md files
    const findCmd = `find . -type f \\( -name "*.js" -o -name "*.ts" -o -name "*.md" \\) -not -path "./node_modules/*" -not -path "./.git/*" 2>/dev/null`;
    const files = execSync(findCmd, { encoding: 'utf-8' }).split('\n').filter(Boolean);

    files.forEach(file => {
      try {
        const content = fs.readFileSync(file, 'utf-8');
        const matches = content.match(/TODO:?[^\n]*/g) || [];
        matches.forEach(match => {
          info.todos.push({ file, text: match.trim() });
        });
      } catch (e) {
        // Skip unreadable files
      }
    });
  } catch (e) {
    // Gracefully handle find failure
  }

  try {
    // Get recent commits
    const commitCmd = `git log --oneline -5 2>/dev/null`;
    info.recentCommits = execSync(commitCmd, { encoding: 'utf-8' })
      .split('\n')
      .filter(Boolean)
      .map(line => line.trim());
  } catch (e) {
    // Not a git repo or git failed
  }

  try {
    // Get changed files (unstaged)
    const statusCmd = `git diff --name-only 2>/dev/null`;
    info.changedFiles = execSync(statusCmd, { encoding: 'utf-8' })
      .split('\n')
      .filter(Boolean)
      .map(f => f.trim());
  } catch (e) {
    // Not a git repo or no changes
  }

  return info;
}

// Main loop logic (to be called by Claude when the loop runs)
console.log('Morning Brief loop is ready.');
console.log('Repository info gathering configured.');
console.log('Progress file:', progressPath);
