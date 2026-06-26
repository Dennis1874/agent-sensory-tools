# 📊 Monitoring Tools

Error tracking, logging, analytics, and CI/CD tools that enable AI agents to observe and respond to system events.

## Overview

Monitoring tools enable AI agents to:
- **Track errors** and exceptions in production
- **Analyze logs** for patterns and anomalies
- **Monitor product analytics** and user behavior
- **Manage CI/CD pipelines** and deployments
- **Receive alerts** for critical events

These tools are essential for incident response, automated debugging, performance optimization, and proactive system management.

---

## Tools

### PostHog MCP

⭐ Official Integration | 🔗 [GitHub](https://github.com/PostHog/posthog-mcp)

**Description**: MCP server for PostHog analytics platform. Combines product analytics, session recording, and error tracking.

**Key Features**:
- Event tracking and analysis
- Session recording playback
- Feature flags management
- Cohort analysis
- Trend detection
- Error clustering

**Installation**:
```json
{
  "mcpServers": {
    "posthog": {
      "command": "npx",
      "args": ["-y", "posthog-mcp"],
      "env": {
        "POSTHOG_API_KEY": "your_api_key",
        "POSTHOG_HOST": "https://app.posthog.com"
      }
    }
  }
}
```

---

### Sentry MCP

⭐ Official Integration | 🔗 [GitHub](https://github.com/getsentry/sentry-mcp)

**Description**: MCP server for Sentry error monitoring. Real-time error tracking with intelligent grouping and alerts.

**Key Features**:
- Real-time error capture
- Stack trace analysis
- Issue grouping and deduplication
- Release tracking
- Performance monitoring
- Custom alert rules

**Installation**:
```json
{
  "mcpServers": {
    "sentry": {
      "command": "npx",
      "args": ["-y", "@sentry/mcp"],
      "env": {
        "SENTRY_API_KEY": "your_api_key",
        "SENTRY_ORG": "your_org_slug"
      }
    }
  }
}
```

---

### LogFile MCP

⭐ Community | 🔗 [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/logseq)

**Description**: MCP server for log file analysis and management. Parse, search, and analyze log data efficiently.

**Key Features**:
- Log file reading and tailing
- Pattern matching and search
- Structured log parsing
- Time-based filtering
- Anomaly detection
- Export capabilities

**Installation**:
```json
{
  "mcpServers": {
    "logfile": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-logseq"]
    }
  }
}
```

---

### GitHub MCP

⭐ Microsoft Official | 🔗 [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/github)

**Description**: Official MCP server for GitHub operations. Full access to repositories, issues, PRs, actions, and more.

**Key Features**:
- Repository management
- Issue creation and updates
- Pull request operations
- GitHub Actions workflows
- Code review comments
- Release management
- Project board management

**Installation**:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token"
      }
    }
  }
}
```

---

## Monitoring Workflow Example

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Code      │────▶│  Execution   │────▶│  Monitoring  │
│   Review    │     │  (E2B/Modal) │     │  (Sentry)    │
└─────────────┘     └─────────────┘     └─────────────┘
                                               │
                                               ▼
                    ┌─────────────┐     ┌─────────────┐
                    │   Alert     │◀────│  Error      │
                    │   Agent     │     │  Detected   │
                    └─────────────┘     └─────────────┘
```

---

## See Also

- [Execution Tools](../execution/README.md) - For running monitored code
- [Web Data Tools](../web-data/README.md) - For researching issues
