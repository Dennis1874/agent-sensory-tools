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
| Tavily | AI RAG workflows | Structured JSON | N/A |

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
