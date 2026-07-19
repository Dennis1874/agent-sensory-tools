# 🌐 Web Data Tools

Web scraping, search APIs, content fetching, and data extraction tools that enable AI agents to access and process information from the internet.

## Overview

Web data tools enable AI agents to:
- **Search the web** for current information
- **Fetch and parse** web page content
- **Convert websites** to markdown for easy processing
- **Extract structured data** from HTML
- **Monitor web changes** and updates

These tools are essential for research agents, competitive analysis, content aggregation, and any workflow requiring up-to-date web information.

---

## Tools

### Brave Search MCP

⭐ Official MCP Server | 🔗 [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search)

**Description**: Official MCP server for Brave Search API. Privacy-focused web search with high-quality results.

**Key Features**:
- Web search with Brave's index
- Image search
- News search
- Local search
- No tracking or personalization

**Installation**:
```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "your_api_key"
      }
    }
  }
}
```

---

### Firecrawl MCP

⭐ ~85K Stars | 🔗 [GitHub](https://github.com/mendableai/firecrawl)

**Description**: Advanced web scraping that transforms entire websites into clean markdown. The most popular web-to-MD solution.

**Key Features**:
- Full website crawling
- JavaScript rendering
- Clean markdown output
- Structured data extraction
- Batch processing
- Rate limiting and retries

**Installation**:
```json
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "@firecrawl/mcp-server"],
      "env": {
        "FIRECRAWL_API_KEY": "your_api_key"
      }
    }
  }
}
```

---

### Fetch MCP

⭐ Official MCP Server | 🔗 [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)

**Description**: Simple HTTP fetch server for retrieving URL content. Lightweight and reliable for basic web requests.

**Key Features**:
- GET/POST requests
- Header customization
- Response parsing
- JSON/XML extraction
- Binary content support

**Installation**:
```json
{
  "mcpServers": {
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"]
    }
  }
}
```

---

### All-in-One MCP

⭐ Multi-Service | 🔗 [GitHub](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol)

**Description**: Comprehensive MCP server integrating GitLab, Jira, Confluence, YouTube and more. Provides AI-powered search and multiple development workflow utilities.

**Key Features**:
- GitLab, Jira, Confluence integration
- YouTube data fetching
- Google Suite (Gmail, Calendar, Chat)
- DeepSeek reasoning engine
- RAG tools for memory and retrieval
- CLI tools integration

**Installation**:
```bash
go install github.com/nguyenvanduocit/all-in-one-model-context-protocol@latest
```

**Environment Variables**:
```bash
GOOGLE_AI_API_KEY=your_key
JIRA_API_TOKEN=your_token
```

---

### Tavily MCP

⭐ AI-Optimized | 🔗 [GitHub](https://github.com/tavily-ai/tavily-mcp)

**Description**: AI-optimized search API designed for retrieval-augmented generation. Returns context-rich, semantically relevant results.

**Key Features**:
- Semantic search optimized for AI
- Real-time information retrieval
- Source citations included
- Topic filtering
- Deep search mode for complex queries

**Installation**:
```json
{
  "mcpServers": {
    "tavily": {
      "command": "npx",
      "args": ["-y", "tavily-mcp"],
      "env": {
        "TAVILY_API_KEY": "your_api_key"
      }
    }
  }
}
```

---

## Comparison

| Tool | Best For | Output Format | JavaScript Rendering |
|------|----------|---------------|---------------------|
| Brave Search | General web search | JSON | N/A |
| Firecrawl | Website crawling | Markdown/JSON | ✅ Yes |
| Fetch | Simple requests | Raw/JSON | ❌ No |
| All-in-One MCP | Multi-service integration | Various | Depends on service |
| Tavily | AI RAG workflows | Structured JSON | N/A |
| Webclone | Website cloning | HTML/Assets | ✅ Yes |

---

### Webclone

⭐ Async Python | 🔗 [GitHub](https://github.com/nicekid1/webclone)

**Description**: Ultra-fast website cloning tool built on async Python, designed for AI agent integration. Supports JavaScript rendering, authentication bypass, and provides both desktop GUI and CLI interfaces.

**Key Features**:
- Extremely fast async website cloning
- JavaScript rendering support for SPAs
- Authentication bypass for protected pages
- AI agent integration via API
- Desktop GUI and command-line interface
- Full page asset preservation

**Installation**:
```bash
pip install webclone

# CLI usage
webclone clone https://example.com -o output_dir
```

---

## Pro Tips

1. **Use Firecrawl** for complex websites that require JavaScript rendering
2. **Use Brave/Tavily** for search-focused workflows
3. **Use Fetch** for simple, predictable endpoints
4. **Combine tools**: Search first, then fetch the top results

---

## See Also

- [Vision Tools](../vision/README.md) - For visual web interactions
- [File & Document Tools](../file-document/README.md) - For processing scraped content


---

### Headroom

⭐ ~50K Stars | 🔗 [GitHub](https://github.com/chopratejas/headroom)

**Description**: Token compression engine for AI agents. Compresses tool outputs, logs, RAG chunks, and files before they reach the LLM. 60-95% fewer tokens with same answer quality. Works as Library, Proxy, Agent Wrapper, or MCP Server.

**Key Features**:
- Transparent compression layer between Agent and LLM
- 60-95% token savings with <3% quality loss
- Six-layer compression pipeline (CacheAligner → ContentRouter → Compressors)
- Four deployment modes: Library, Proxy, Agent Wrap, MCP Server
- Cross-agent memory sharing (SharedContext)
- Local-first, data never leaves your machine
- Compatible with Claude Code, Cursor, Codex, Aider, Copilot, and more
- `headroom learn` auto-analyzes failed sessions for improvement

**Installation**:
```bash
# Install
pip install "headroom-ai[all]"

# Wrap your AI agent (zero code changes)
headroom wrap claude

# Or run as MCP server
headroom mcp install

# Or as HTTP proxy (zero code, change base URL)
headroom proxy --port 8787
```

---

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

