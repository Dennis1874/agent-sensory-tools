#!/usr/bin/env python3
"""
Weekly update script for agent-sensory-tools repository.
Date: 2026-08-09
New tools: 5
"""

import os
import subprocess
import requests

REPO_DIR = "/app/data/所有对话/主对话/agent-sensory-tools"
GITHUB_TOKEN = "GITHUB_TOKEN_PLACEHOLDER"
OWNER = "Dennis1874"
REPO = "agent-sensory-tools"

# New tools to add
NEW_TOOLS = {
    "vision": """
---

### Page Agent

⭐ ~9,600 Stars | 🔗 [GitHub](https://github.com/alibaba/page-agent)

**Description**: Alibaba's open-source JavaScript in-page GUI agent. Lives directly inside web pages as a `<script>` tag — no headless browser, no screenshots, no Python backend required. Users control web interfaces with natural language. The agent reads DOM structure, assigns indices to interactive elements, and executes clicks, inputs, and navigation via LLM decisions. Includes MCP Server (Beta) for external agent orchestration.

**Key Features**:
- Pure frontend JavaScript — runs inside the DOM context
- Natural language web interface control
- "DOM dehydration" technique: compact text representation of interactive elements
- No screenshots or multimodal models needed
- BYOK (Bring Your Own Key): supports OpenAI, Claude, Qwen, DeepSeek, Gemini, Ollama
- MCP Server (Beta) for external agent control
- Chrome extension for cross-tab workflows
- MIT license, model-agnostic
- Human-in-the-loop with confirmation dialogs

**Installation**:
```html
<!-- One-line CDN embed -->
<script src="https://cdn.jsdelivr.net/npm/page-agent@1.x.x/dist/iife/page-agent.demo.js" crossorigin="true"></script>
```
```bash
# NPM
npm install page-agent

# MCP Server configuration
{
  "mcpServers": {
    "page-agent": {
      "command": "npx",
      "args": ["-y", "page-agent-mcp"]
    }
  }
}
```

---
""",
    "execution": """
---

### Cloudflare Computer

⭐ Cloudflare Official | 🔗 [GitHub](https://github.com/cloudflare/workers-sdk) | 🔗 [npm](https://www.npmjs.com/package/@cloudflare/computer)

**Description**: Cloudflare's open-source agent runtime providing each AI agent with its own virtual computer. Features a SQLite-backed virtual filesystem (Workspace) with three execution backends: full Linux Container (FUSE mount), Isolate Shell (just-bash in Dynamic Worker), and Isolate JavaScript (ESM modules). Released August 3, 2026. The agent owns the filesystem; containers merely borrow it, execute tasks, and return changes.

**Key Features**:
- Virtual filesystem on SQLite (Durable Object-backed)
- Three execution backends: Container (full Linux), Isolate Shell (text tools), Isolate JS (npm modules)
- Agent-owned state: data survives container crashes
- FUSE mount via `computerd` daemon for Container backend
- `capnweb` RPC protocol for efficient state synchronization
- All operations logged with full audit trail
- Controlled gateways for security
- Works with Cloudflare Workers, Durable Objects, and R2
- Open-source, npm installable

**Installation**:
```bash
npm install @cloudflare/computer
```
```typescript
import { Workspace } from "@cloudflare/computer";

export class Agent {
  workspace = new Workspace({
    storage: this.ctx.storage,
  });
}
```

---
""",
    "monitoring": """
---

### BigFix Platform MCP Server

⭐ Enterprise | 🔗 [BigFix Forum](https://forum.bigfix.com/t/the-bigfix-platform-mcp-server-is-now-available/55245) | 🔗 [Docs](https://bigfix.com/mcp)

**Description**: Enterprise endpoint management MCP server by HCL BigFix. Lets AI assistants retrieve data from BigFix environments and author/run actions on endpoints using natural language. Released August 5, 2026. Built on MCP with streamable HTTP mode over HTTPS, token-based authentication, and security-first design with read-only default and human-in-the-loop protection.

**Key Features**:
- Action lifecycle management: list, create, retry, stop, delete actions
- Custom action authoring with LLM assistance
- Fixlet and Task deployment through action creation
- Computer listing and detail retrieval
- Fixlet discovery and detail inspection
- Session Relevance evaluation via Web Reports/Explorer
- Read-only by default with explicit write opt-in
- Human-in-the-loop protection for critical operations
- Token-based auth forwarded to BigFix REST API
- TLS support with auto-generated certificates
- Requires BigFix Platform 11.0.6+

**Installation**:
```json
{
  "mcpServers": {
    "bigfix": {
      "url": "https://your-bigfix-server:52311/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_BIGFIX_API_TOKEN"
      }
    }
  }
}
```

---

### Snap Ads MCP Server

⭐ Snap Official | 🔗 [Snap Business Blog](https://forbusiness.snapchat.com/blog/snapchat-ads-mcp)

**Description**: Snapchat's official MCP server for advertising data. Provides an Snap-hosted connection between Snap Ads API and AI agents (Claude, ChatGPT, Gemini). Released August 3, 2026. Advertisers can query campaign performance, trends, and diagnostics using natural language. Organization-level access control with per-agent authorization.

**Key Features**:
- Official Snap-hosted MCP endpoint (mcp.snapchat.com/ads)
- Campaign performance queries in natural language
- Week-over-week trend analysis
- Diagnostic issue identification
- 90-day historical pattern analysis
- OAuth-based authentication
- Organization-level agent authorization
- Read-only at launch; write capabilities coming later
- Per-agent access control granularity
- Compatible with Claude, ChatGPT, and Gemini

**Installation**:
```json
{
  "mcpServers": {
    "snap-ads": {
      "url": "https://mcp.snapchat.com/ads"
    }
  }
}
```

---
""",
    "web-data": """
---

### Haystack Intranet MCP Server

⭐ Enterprise Search | 🔗 [PR Newswire](https://www.prnewswire.com/news-releases/haystack-launches-the-intranet-industrys-first-model-context-protocol-mcp-server-302844392.html)

**Description**: The intranet industry's first MCP server, launched by Haystack. Enables AI agents to search and retrieve content from corporate intranets through the Model Context Protocol. Bridges the gap between AI assistants and internal enterprise knowledge bases that are typically inaccessible through public web tools.

**Key Features**:
- First MCP server purpose-built for intranet content
- Secure access to internal corporate knowledge
- Natural language search across intranet sites
- Enterprise authentication and authorization
- Compatible with major AI agent platforms
- Preserves existing intranet permission models
- Structured content extraction
- Real-time intranet content indexing

**Installation**:
```json
{
  "mcpServers": {
    "haystack-intranet": {
      "url": "https://mcp.haystacksearch.com/intranet",
      "headers": {
        "Authorization": "Bearer YOUR_HAYSTACK_API_KEY"
      }
    }
  }
}
```

---
""",
    "file-document": """
---

### Mirage

⭐ Trending | 🔗 [GitHub](https://github.com/strukto-ai/mirage)

**Description**: The world's first unified virtual filesystem for AI agents. Provides a single filesystem abstraction layer that agents can use to access, organize, and manipulate files across multiple backends (local, cloud, sandboxed). Built with Python/Bash/TypeScript, supports FUSE mounting and integrates with LangChain, Claude Code, and OpenClaw ecosystems. Updated August 8, 2026.

**Key Features**:
- Unified virtual filesystem across multiple storage backends
- FUSE mount support for shell-level access
- Agent-optimized file operations and metadata
- Sandbox isolation for safe file manipulation
- Integration with LangChain, Claude Code, OpenClaw
- Cross-backend file synchronization
- Type-safe file operations with validation
- Bash, Python, and TypeScript interfaces
- Designed for multi-agent file collaboration

**Installation**:
```bash
# npm
npm install -g @strukto-ai/mirage

# Or clone and build
git clone https://github.com/strukto-ai/mirage.git
cd mirage && pip install -e .
```

---
"""
}

# Updated counts: Vision 16->17, Execution 12->13, Monitoring 15->17, Web Data 12->13, File 7->8
# Total: 67 + 6 = 73
NEW_COUNTS = {
    "vision": 17,
    "code_awareness": 5,
    "web_data": 13,
    "file_document": 8,
    "execution": 13,
    "monitoring": 17,
}
TOTAL = 73


def update_category_readme(category_dir, content_to_append):
    """Append new tool content to a category README."""
    readme_path = os.path.join(REPO_DIR, "categories", category_dir, "README.md")
    with open(readme_path, "r") as f:
        existing = f.read()
    
    with open(readme_path, "w") as f:
        f.write(existing + content_to_append)
    print(f"Updated: {readme_path}")


def update_main_readme():
    """Update tool counts in main README."""
    readme_path = os.path.join(REPO_DIR, "README.md")
    with open(readme_path, "r") as f:
        content = f.read()
    
    # Update category counts
    content = content.replace(
        "| [Vision](categories/vision/README.md) | 👁️ | Browser automation, screenshot capture, image processing | 16 |",
        f"| [Vision](categories/vision/README.md) | 👁️ | Browser automation, screenshot capture, image processing | {NEW_COUNTS['vision']} |"
    )
    content = content.replace(
        "| [Code Awareness](categories/code-awareness/README.md) | 🧠 | Code search, knowledge graphs, documentation lookup | 5 |",
        f"| [Code Awareness](categories/code-awareness/README.md) | 🧠 | Code search, knowledge graphs, documentation lookup | {NEW_COUNTS['code_awareness']} |"
    )
    content = content.replace(
        "| [Web Data](categories/web-data/README.md) | 🌐 | Web scraping, search APIs, content fetching | 12 |",
        f"| [Web Data](categories/web-data/README.md) | 🌐 | Web scraping, search APIs, content fetching | {NEW_COUNTS['web_data']} |"
    )
    content = content.replace(
        "| [File & Document](categories/file-document/README.md) | 📄 | File system access, PDF parsing, document processing | 7 |",
        f"| [File & Document](categories/file-document/README.md) | 📄 | File system access, PDF parsing, document processing | {NEW_COUNTS['file_document']} |"
    )
    content = content.replace(
        "| [Execution](categories/execution/README.md) | ⚡ | Sandboxed code execution, cloud functions, shell commands | 12 |",
        f"| [Execution](categories/execution/README.md) | ⚡ | Sandboxed code execution, cloud functions, shell commands | {NEW_COUNTS['execution']} |"
    )
    content = content.replace(
        "| [Monitoring](categories/monitoring/README.md) | 📊 | Error tracking, logging, analytics, CI/CD | 15 |",
        f"| [Monitoring](categories/monitoring/README.md) | 📊 | Error tracking, logging, analytics, CI/CD | {NEW_COUNTS['monitoring']} |"
    )
    
    # Update total
    content = content.replace("**Total: 67 tools**", f"**Total: {TOTAL} tools**")
    
    with open(readme_path, "w") as f:
        f.write(content)
    print(f"Updated main README: total = {TOTAL}")


def git_commit_and_push():
    """Commit and push changes."""
    os.chdir(REPO_DIR)
    subprocess.run(["git", "add", "-A"], check=True)
    
    commit_msg = "weekly update: 2026-08-09 - 新增6个工具 (Page Agent/Cloudflare Computer/BigFix MCP/Snap Ads MCP/Haystack Intranet MCP/Mirage)"
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)
    
    # Push using token
    repo_url = f"https://{GITHUB_TOKEN}@github.com/{OWNER}/{REPO}.git"
    result = subprocess.run(
        ["git", "push", repo_url, "main"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        print("Successfully pushed to GitHub!")
    else:
        print(f"Push failed: {result.stderr}")
        # Try with remote
        subprocess.run(["git", "push", "origin", "main"], check=True)


if __name__ == "__main__":
    print("=== agent-sensory-tools weekly update: 2026-08-09 ===")
    print(f"Adding 5 new tools, total: {TOTAL}")
    
    # Update category READMEs
    update_category_readme("vision", NEW_TOOLS["vision"])
    update_category_readme("execution", NEW_TOOLS["execution"])
    update_category_readme("monitoring", NEW_TOOLS["monitoring"])
    update_category_readme("web-data", NEW_TOOLS["web-data"])
    update_category_readme("file-document", NEW_TOOLS["file-document"])
    
    # Update main README
    update_main_readme()
    
    # Commit and push
    git_commit_and_push()
    
    print("\n=== Update complete! ===")
    print(f"Commit: weekly update: 2026-08-09")
    print(f"New total: {TOTAL} tools")
