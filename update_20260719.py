#!/usr/bin/env python3
"""Weekly update for agent-sensory-tools repository - 2026-07-19"""

import requests
import json
import base64

GITHUB_TOKEN = "GITHUB_TOKEN_PLACEHOLDER"
REPO = "Dennis1874/agent-sensory-tools"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}
API_BASE = f"https://api.github.com/repos/{REPO}"

def get_file(path):
    """Get file content from GitHub"""
    url = f"{API_BASE}/contents/{path}"
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code == 200:
        data = resp.json()
        content = base64.b64decode(data["content"]).decode("utf-8")
        return content, data["sha"]
    else:
        print(f"Error getting {path}: {resp.status_code} {resp.text}")
        return None, None

def update_file(path, content, sha, message):
    """Update file on GitHub"""
    url = f"{API_BASE}/contents/{path}"
    data = {
        "message": message,
        "content": base64.b64encode(content.encode("utf-8")).decode("utf-8"),
        "sha": sha
    }
    resp = requests.put(url, headers=HEADERS, json=data)
    if resp.status_code == 200:
        print(f"✅ Updated {path}")
    else:
        print(f"❌ Failed to update {path}: {resp.status_code} {resp.text}")
    return resp

# ============================================================
# 1. Update Web Data README
# ============================================================
print("\n=== Updating Web Data README ===")
web_data_content, web_data_sha = get_file("categories/web-data/README.md")

if web_data_content and web_data_sha:
    # Add new tools before the closing
    new_web_tools = """
---

### Apify MCP Server

⭐ 4K+ Stars | 🔗 [GitHub](https://github.com/apify/apify-mcp-server)

**Description**: MCP server connecting AI agents to 8,000+ Apify Actors for web scraping, crawling, and automation. Covers social media, search engines, maps, e-commerce, and any website. Supports OAuth, agentic payments via x402/Skyfire.

**Key Features**:
- Access to 8,000+ ready-made scrapers and crawlers (Apify Store)
- Social media data extraction (Facebook, Instagram, Google Maps)
- Hosted server with OAuth support (mcp.apify.com)
- Agentic payments: AI agents pay for runs with USDC via x402 or Skyfire
- Dynamic tool discovery - any Actor becomes a tool automatically
- Structured output with schema inference
- Streamable HTTP transport (replaced legacy SSE)

**Installation**:
```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": ["-y", "@apify/actors-mcp-server"],
      "env": {
        "APIFY_TOKEN": "your_api_token"
      }
    }
  }
}
```

---

### WET-MCP (Web Extended Toolkit)

⭐ 15+ Stars | 🔗 [GitHub](https://github.com/n24q02m/wet-mcp)

**Description**: All-in-one MCP server for web search, content extraction, crawling, academic research, and library docs. Built with embedded SearXNG, 5-strategy scraping escalation, and zero API key requirement.

**Key Features**:
- Web Search via embedded SearXNG (Google, Bing, DuckDuckGo, Brave)
- Academic Research: Google Scholar, Semantic Scholar, arXiv, PubMed, CrossRef
- Library Docs: Auto-discover and index documentation with FTS5 hybrid search
- 5-strategy scraping chain: basic_http → tls_spoof → render → captcha bypass
- Anti-bot stealth: bypasses Cloudflare, Medium, LinkedIn, Twitter
- Zero config: Built-in local Qwen3 embedding + reranking, no API keys needed
- Local file conversion: PDF, DOCX, XLSX, CSV, HTML, EPUB, PPTX to Markdown
- Deep crawling and site mapping

**Installation**:
```json
{
  "mcpServers": {
    "wet": {
      "command": "uvx",
      "args": ["wet-mcp"]
    }
  }
}
```

"""
    # Insert new tools before the last section or at the end
    # Find last "###" entry and append after it
    new_content = web_data_content.rstrip() + "\n" + new_web_tools
    update_file("categories/web-data/README.md", new_content, web_data_sha,
                "weekly update: 2026-07-19 - add Apify MCP Server and WET-MCP")

# ============================================================
# 2. Update File & Document README
# ============================================================
print("\n=== Updating File & Document README ===")
file_doc_content, file_doc_sha = get_file("categories/file-document/README.md")

if file_doc_content and file_doc_sha:
    new_file_tools = """
---

### TX Text Control MCP Document Server

⭐ Active Open Source | 🔗 [GitHub](https://github.com/TextControl/TXTextControl.MCPDocumentServer)

**Description**: AI-powered document generation MCP server using TX Text Control as the deterministic engine. AI agents translate natural language prompts into structured tool calls for creating professional DOCX, PDF documents with tables, styles, merge fields, and more.

**Key Features**:
- Natural language document creation ("create an invoice template")
- Deterministic document processing: layout, styles, tables, merge fields
- Export to DOCX, PDF, HTML, plain text
- Template merging with structured data
- Form field manipulation and document inspection
- AI as interface + document engine as backend pattern
- ASP.NET Core based, enterprise-ready

**Installation**:
```bash
# Clone and run the ASP.NET Core MCP server
git clone https://github.com/TextControl/TXTextControl.MCPDocumentServer.git
cd TXTextControl.MCPDocumentServer
dotnet run
```

"""
    new_content = file_doc_content.rstrip() + "\n" + new_file_tools
    update_file("categories/file-document/README.md", new_content, file_doc_sha,
                "weekly update: 2026-07-19 - add TX Text Control MCP Document Server")

# ============================================================
# 3. Update Execution README
# ============================================================
print("\n=== Updating Execution README ===")
exec_content, exec_sha = get_file("categories/execution/README.md")

if exec_content and exec_sha:
    new_exec_tools = """
---

### just-bash-mcp

⭐ New Release v3.1 | 🔗 [GitHub](https://www.npmjs.com/package/just-bash-mcp)

**Description**: Sandboxed bash environment MCP server for AI agents. Executes bash commands in a secure, isolated in-memory virtual filesystem with defense-in-depth security, Python support, and comprehensive upstream command compatibility.

**Key Features**:
- Sandboxed execution in isolated virtual filesystem
- Defense-in-depth mode with monkey-patching of dangerous JS globals
- Python3 support via upstream emscripten CPython runtime
- Stateless & stateful modes (isolated or persistent filesystem)
- OverlayFS/MountableFS/ReadWriteFS support for real directory mounting
- Network access control with URL allow-lists
- Execution limits: protection against infinite loops and deep recursion
- Byte-safe stdin handling and file IO
- AST transform tool for bash pipeline analysis
- Full upstream exec options: cwd, env, stdin, timeout, args

**Installation**:
```json
{
  "mcpServers": {
    "just-bash": {
      "command": "npx",
      "args": ["-y", "just-bash-mcp"]
    }
  }
}
```

---

### Desktop Commander MCP

⭐ 8.2K+ Stars | 🔗 [GitHub](https://github.com/wonderwhy-er/DesktopCommanderMCP)

**Description**: Full-featured MCP server providing terminal control, file system search, diff-based code editing, and process management for AI agents. GitHub Trending #1 in July 2026. Goes beyond basic file system access to become a desktop automation runtime.

**Key Features**:
- Terminal control with background execution and streaming output
- File system search with glob patterns and content search
- Diff-based line editing (not full file replacement)
- Process management: list, kill, monitor running processes
- SSH, database, and development server process management
- Office/PDF document processing (Excel, DOCX, PDF)
- MCP Resources for file preview and configuration UI
- Remote MCP support (mcp.desktopcommander.app)
- Pagination for long output reading
- TypeScript-based, MIT licensed

**Installation**:
```json
{
  "mcpServers": {
    "desktop-commander": {
      "command": "npx",
      "args": ["-y", "@anthropic/desktop-commander-mcp"]
    }
  }
}
```

"""
    new_content = exec_content.rstrip() + "\n" + new_exec_tools
    update_file("categories/execution/README.md", new_content, exec_sha,
                "weekly update: 2026-07-19 - add just-bash-mcp and Desktop Commander MCP")

# ============================================================
# 4. Update Monitoring README
# ============================================================
print("\n=== Updating Monitoring README ===")
mon_content, mon_sha = get_file("categories/monitoring/README.md")

if mon_content and mon_sha:
    new_mon_tools = """
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

"""
    new_content = mon_content.rstrip() + "\n" + new_mon_tools
    update_file("categories/monitoring/README.md", new_content, mon_sha,
                "weekly update: 2026-07-19 - add Dynatrace MCP Server")

# ============================================================
# 5. Update main README.md (tool counts)
# ============================================================
print("\n=== Updating main README.md ===")
main_content, main_sha = get_file("README.md")

if main_content and main_sha:
    # Update category counts
    # Web Data: 7 → 9
    main_content = main_content.replace(
        "| [Web Data](categories/web-data/README.md) | 🌐 | Web scraping, search APIs, content fetching | 7 |",
        "| [Web Data](categories/web-data/README.md) | 🌐 | Web scraping, search APIs, content fetching | 9 |"
    )
    # File & Document: 5 → 6
    main_content = main_content.replace(
        "| [File & Document](categories/file-document/README.md) | 📄 | File system access, PDF parsing, document processing | 5 |",
        "| [File & Document](categories/file-document/README.md) | 📄 | File system access, PDF parsing, document processing | 6 |"
    )
    # Execution: 8 → 10
    main_content = main_content.replace(
        "| [Execution](categories/execution/README.md) | ⚡ | Sandboxed code execution, cloud functions, shell commands | 8 |",
        "| [Execution](categories/execution/README.md) | ⚡ | Sandboxed code execution, cloud functions, shell commands | 10 |"
    )
    # Monitoring: 12 → 13
    main_content = main_content.replace(
        "| [Monitoring](categories/monitoring/README.md) | 📊 | Error tracking, logging, analytics, CI/CD | 12 |",
        "| [Monitoring](categories/monitoring/README.md) | 📊 | Error tracking, logging, analytics, CI/CD | 13 |"
    )
    # Total: 49 → 55
    main_content = main_content.replace(
        "**Total: 49 tools**",
        "**Total: 55 tools**"
    )
    
    update_file("README.md", main_content, main_sha,
                "weekly update: 2026-07-19 - 新增6个工具")

print("\n=== Update complete! ===")
print("New tools added:")
print("  - Web Data: Apify MCP Server, WET-MCP (+2)")
print("  - File & Document: TX Text Control MCP Document Server (+1)")
print("  - Execution: just-bash-mcp, Desktop Commander MCP (+2)")
print("  - Monitoring: Dynatrace MCP Server (+1)")
print("Total: 49 → 55 tools")
