/**
 * Data collection utilities for morning brief
 */

function collectRepositoryMetrics() {
  // TODO: Add file size tracking to detect large refactors

  const metrics = {
    timestamp: new Date().toISOString(),
    scanComplete: true
  };

  return metrics;
}

function formatBrief(data) {
  // TODO: Support markdown formatting in brief output
  // TODO: Add color-coded priority levels for TODOs

  const lines = [];
  lines.push(`## Morning Brief - ${new Date().toLocaleDateString()}`);

  if (data.todos && data.todos.length > 0) {
    lines.push(`\n**${data.todos.length} TODO items found**`);
  }

  return lines.join('\n');
}

module.exports = { collectRepositoryMetrics, formatBrief };
