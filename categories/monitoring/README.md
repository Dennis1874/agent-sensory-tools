# 📊 Monitoring Tools

Error tracking, logging, analytics, CI/CD tools, and memory systems that enable AI agents to observe, respond, and maintain context across sessions.

## Overview

Monitoring tools enable AI agents to:
- **Track errors** and exceptions in production
- **Analyze logs** for patterns and anomalies
- **Monitor product analytics** and user behavior
- **Manage CI/CD pipelines** and deployments
- **Maintain persistent memory** across sessions
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

### ShelbyMCP

⭐ Knowledge Graph Memory | 🔗 [GitHub](https://github.com/studio-moser/shelby-mcp)

**Description**: Knowledge graph memory server for MCP-compatible AI tools. Provides persistent memory with typed relationships (refines, cites, contradicts, tags).

**Key Features**:
- Knowledge graph with typed relationships
- Cross-session persistent memory
- Semantic memory connections
- Zero dependencies - single binary
- Claude Code / Codex / Gemini CLI compatible
- Local-first, no cloud required

**Installation**:
```bash
# Download from GitHub releases
# No dependencies required
```

---

### Memory Bank MCP

⭐ Project Context Management | 🔗 [GitHub](https://github.com/t3ta/memory-bank-mcp-server)

**Description**: MCP server for managing project documentation and context across Claude AI sessions. Stores structured JSON documents for consistent project knowledge.

**Key Features**:
- Global and branch-specific memory banks
- Structured JSON document storage
- Cross-session project context
- Version control friendly
- Claude, Cursor, Windsurf compatible
- VSCode extension available

**Installation**:
```bash
git clone https://github.com/t3ta/memory-bank-mcp-server.git
cd memory-bank-mcp-server
yarn install
yarn workspace @memory-bank/mcp start --docs /path/to/your/docs
```

---

### Datadog MCP Server

⭐ Monitoring Integration | 🔗 [GitHub](https://github.com/winor30/datadog-mcp)

**Description**: MCP server for Datadog API integration. Provides seamless management of events, monitors, logs, dashboards, metrics, traces, and hosts with extensible design for future API expansions.

**Key Features**:
- Event tracking and management
- Monitor status queries
- Log search and retrieval
- Dashboard listing and details
- Metrics querying
- APM trace access
- Host management and muting
- Scalable architecture for additional APIs

**Installation**:
```json
{
  "mcpServers": {
    "datadog": {
      "command": "npx",
      "args": ["-y", "@datadog/mcp"],
      "env": {
        "DATADOG_API_KEY": "your_api_key",
        "DATADOG_APP_KEY": "your_app_key"
      }
    }
  }
}
```

---

### Azure DevOps MCP Server

⭐ DevOps Integration | 🔗 [GitHub](https://github.com/Tiberriver256/azure-devops-mcp)

**Description**: MCP server enabling AI assistants to interact with Azure DevOps resources through a standardized protocol. Supports projects, work items, repositories, pull requests, branches, and pipelines.

**Key Features**:
- Project management
- Work item creation and updates
- Repository access
- Pull request operations
- Branch management
- Pipeline control
- Natural language DevOps workflows
- Secure authentication with PAT

**Installation**:
```json
{
  "mcpServers": {
    "azure-devops": {
      "command": "npx",
      "args": ["-y", "azure-devops-mcp"],
      "env": {
        "AZURE_DEVOPS_ORG_URL": "https://dev.azure.com/yourorg",
        "AZURE_DEVOPS_PAT": "your_personal_access_token"
      }
    }
  }
}
```

---

### Firefly MCP Server

⭐ CloudOps MCP | 🔗 [Firefly](https://www.firefly.ai) | 🔗 [Docs](https://docs.firefly.ai/integrations/mcp)

**Description**: MCP server for cloud infrastructure management. Enables AI agents to discover, manage, and codify cloud and SaaS resources using natural language. Integrates with Cursor and Claude for context-aware CloudOps.

**Key Features**:
- Discover all resources across connected cloud accounts
- Codify resources into Infrastructure as Code
- Query cloud state in real-time
- Drift detection and automated remediation
- Support for Kubernetes, IAM, SaaS, and more
- NPX plug-and-play setup
- Works with any MCP-compatible agent

**Installation**:
```json
{
  "mcpServers": {
    "firefly": {
      "command": "npx",
      "args": ["-y", "@fireflyai/firefly-mcp"],
      "env": {
        "FIREFLY_ACCESS_KEY": "your_access_key",
        "FIREFLY_SECRET_KEY": "your_secret_key"
      }
    }
  }
}
```

---

### Azure SRE Agent MCP Tools

⭐ Microsoft Official | 🔗 [Microsoft Learn](https://learn.microsoft.com/en-au/azure/developer/azure-mcp-server/tools/azure-sre-agent)

**Description**: MCP tools for Azure SRE Agent — an AI-powered reliability assistant that helps teams diagnose and resolve production issues. Provides 50+ tools covering subagents, incidents, scheduled tasks, workflows, hooks, skills, and PagerDuty/ServiceNow integration.

**Key Features**:
- AI-powered incident diagnosis and resolution
- Subagent creation and management
- PagerDuty and ServiceNow connector support
- Scheduled task management
- Workflow generation and deployment
- Knowledge base documentation management
- Hook-based event automation
- Natural language SRE operations

**Installation**:
```json
{
  "mcpServers": {
    "azure-sre": {
      "command": "npx",
      "args": ["-y", "@azure/mcp-server-sre"],
      "env": {
        "AZURE_SUBSCRIPTION_ID": "your_subscription_id",
        "AZURE_TENANT_ID": "your_tenant_id"
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


---

### Azure MCP Server

⭐ ~2.4K Stars | 🔗 [GitHub](https://github.com/Azure/azure-mcp)

**Description**: Microsoft's official MCP server for unified access to Azure cloud services. Enables AI agents to manage Azure resources, deploy applications, and automate cloud operations through natural language.

**Key Features**:
- Unified access to all Azure services
- Resource management and deployment
- Natural language cloud operations
- Integration with Azure DevOps, Functions, Storage, etc.
- Enterprise-grade security and authentication
- Official Microsoft support

**Installation**:
```json
{
  "mcpServers": {
    "azure": {
      "command": "npx",
      "args": ["-y", "@azure/mcp-server"],
      "env": {
        "AZURE_SUBSCRIPTION_ID": "your_subscription_id",
        "AZURE_TENANT_ID": "your_tenant_id"
      }
    }
  }
}
```

---

### PostgreSQL MCP

⭐ Official MCP Server | 🔗 [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres)

**Description**: Official MCP server for PostgreSQL database operations. Enables AI agents to query databases, analyze schemas, and execute SQL through natural language.

**Key Features**:
- Direct database query execution
- Schema introspection and analysis
- Table and column exploration
- SQL generation from natural language
- Read-only and read-write modes
- Connection pooling support

**Installation**:
```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost:5432/mydb"
      }
    }
  }
}
```

---

---

### Dynatrace MCP Server

⭐ Official | 🔗 [GitHub](https://github.com/dynatrace-oss/dynatrace-mcp-server)

**Description**: Official MCP server for Dynatrace observability platform. Enables AI agents to query metrics, analyze problems, explore distributed traces, and manage Dynatrace configurations using natural language.

**Key Features**:
- Query DQL (Dynatrace Query Language) via natural language
- Problem analysis and root cause detection
- Distributed trace exploration
- Metric ingestion and querying
- Entity discovery and topology mapping
- Event management and alerting
- Dashboard and notebook management
- Official Dynatrace OSS maintenance
- Streamable HTTP and stdio transport support

**Installation**:
```json
{
  "mcpServers": {
    "dynatrace": {
      "command": "npx",
      "args": ["-y", "@dynatrace-oss/dynatrace-mcp-server"],
      "env": {
        "DYNATRACE_URL": "https://your-env.dynatrace.com",
        "DYNATRACE_API_TOKEN": "your_api_token"
      }
    }
  }
}
```

