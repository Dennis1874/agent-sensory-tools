# 🧠 Code Awareness Tools

Code search, knowledge graphs, documentation lookup, and programming assistance tools that help AI agents understand and navigate codebases.

## Overview

Code awareness tools enable AI agents to:
- **Search and navigate** large codebases efficiently
- **Build knowledge graphs** of code relationships
- **Query documentation** in real-time
- **Understand context** around specific code elements
- **Assist with programming** tasks and code generation

These tools are essential for AI coding assistants, automated code review, documentation generation, and any agent workflow that involves understanding existing code.

---

## Tools

### codebase-memory-mcp

⭐ ~9K Stars | 🔗 [GitHub](https://github.com/DeusData/codebase-memory-mcp)

**Description**: Code knowledge graph builder that creates semantic embeddings of your codebase. Enables context-aware AI assistance by understanding code relationships.

**Key Features**:
- Automatic code graph construction
- Semantic code search
- Dependency tracking
- Function call analysis
- Context retrieval for any code location

**Installation**:
```json
{
  "mcpServers": {
    "codebase-memory": {
      "command": "npx",
      "args": ["-y", "codebase-memory-mcp"]
    }
  }
}
```

---

### Context7

⭐ Active Open Source | 🔗 [GitHub](https://github.com/context7/context7)

**Description**: Real-time library documentation lookup for AI coding assistants. Ensures AI always has the latest API reference.

**Key Features**:
- Real-time documentation fetching
- Multi-library support
- Version-aware documentation
- Direct code examples
- Automatic updates when APIs change

**Installation**:
```bash
npx -y @context7/mcp-server
```

---

### Aider MCP

⭐ ~8K Stars | 🔗 [GitHub](https://github.com/Aider-Environments/aider-mcp)

**Description**: MCP server for Aider, the AI pair programming tool. Enables chat-based coding with git integration.

**Key Features**:
- Chat-based code editing
- Git-aware diff generation
- Multi-file refactoring
- Voice coding support
- Yank pad for code snippets

**Installation**:
```json
{
  "mcpServers": {
    "aider": {
      "command": "aider --mcp",
      "args": []
    }
  }
}
```

---

### Sourcegraph / Cody

⭐ Enterprise Grade | 🔗 [GitHub](https://github.com/sourcegraph/cody)

**Description**: Sourcegraph's Cody AI assistant with deep code search. The most powerful code intelligence platform.

**Key Features**:
- Universal code search across repos
- Code graph and intelligence
- Context-aware completions
- Code review assistance
- Documentation Q&A
- Multi-language support

**Installation**:
```bash
# Install Cody VS Code extension
code --install-extension sourcegraph.cody-ai

# Or use Sourcegraph CLI
npm install -g @sourcegraph/cody-cli
```

---

## Choosing a Code Awareness Tool

| Tool | Strength | Use Case | Scale |
|------|----------|----------|-------|
| codebase-memory-mcp | Knowledge graphs | Deep code understanding | Any size |
| Context7 | Documentation | API accuracy | Any project |
| Aider MCP | Pair programming | Real-time coding | Single repo |
| Cody | Full code intelligence | Enterprise | Large codebases |

---

## See Also

- [File & Document Tools](../file-document/README.md) - For reading and writing source files
- [Web Data Tools](../web-data/README.md) - For searching online resources
