/**
 * Task manager for the morning brief loop
 */

// TODO: Add persistence layer for task history
// TODO: Implement retry logic for failed briefing runs

function createBrief(findings) {
  const brief = {
    timestamp: new Date().toISOString(),
    todos: findings.todos || [],
    recentActivity: findings.recentCommits || [],
    summary: generateSummary(findings)
  };
  return brief;
}

function generateSummary(findings) {
  // TODO: Make summary more intelligent and contextual
  let lines = [];

  if (findings.todos.length > 0) {
    lines.push(`Found ${findings.todos.length} TODO items`);
  }

  if (findings.recentCommits.length > 0) {
    lines.push(`${findings.recentCommits.length} recent commits`);
  }

  return lines.join('. ');
}

module.exports = { createBrief };
