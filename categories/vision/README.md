# 👁️ Vision Tools

Browser automation, screenshot capture, and image processing tools that give AI agents the ability to see and interact with visual content.

## Overview

Vision tools enable AI agents to:
- **Navigate websites** through automated browsers
- **Capture screenshots** of web pages and applications
- **Process images** for analysis or manipulation
- **Interact with web elements** like clicking, typing, and scrolling

These tools are essential for web scraping, UI testing, visual regression testing, and any agent workflow that requires visual understanding of web content.

---

## Tools

### Puppeteer MCP

⭐ Official MCP Project | 🔗 [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer)

**Description**: Official MCP server for Puppeteer-based browser automation. The gold standard for headless Chrome control.

**Key Features**:
- Full headless Chrome automation
- Page navigation and interaction
- Screenshot and PDF generation
- DOM manipulation and extraction
- Network request monitoring

**Installation**:
```json
{
  "mcpServers": {
    "puppeteer": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
    }
  }
}
```

---

### Playwright MCP

⭐ Microsoft | 🔗 [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/playwright)

**Description**: Microsoft's official MCP server for Playwright browser automation. Cross-browser support with modern features.

**Key Features**:
- Cross-browser automation (Chromium, Firefox, WebKit)
- Mobile device emulation
- Video recording of sessions
- Network interception and mocking
- Built-in locators and assertions

**Installation**:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-playwright"]
    }
  }
}
```

---

### Browser Use

⭐ Active Open Source | 🔗 [GitHub](https://github.com/browser-use/browser-use)

**Description**: AI-first browser automation framework designed specifically for agent workflows. Makes browser control intuitive for LLMs.

**Key Features**:
- Natural language browser control
- Agent-optimized action handling
- Multi-tab management
- Built-in retry logic and error recovery
- Vision-capable (can see what it's doing)

**Installation**:
```bash
pip install browser-use
```

---

### stagehand

⭐ Browserbase | 🔗 [GitHub](https://github.com/browserbase/stagehand)

**Description**: AI-powered browser automation by Browserbase. Leverages computer vision for reliable element detection.

**Key Features**:
- AI-guided element finding
- No XPath or CSS selectors needed
- Visual confidence scoring
- Handles dynamic content well
- Cloud-hosted browser infrastructure

**Installation**:
```bash
npm install stagehand
```

---

### Sharp MCP

⭐ Active Development | 🔗 [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/-sharp)

**Description**: Official MCP server for Sharp image processing library. High-performance Node.js image manipulation.

**Key Features**:
- Format conversion (PNG, JPEG, WebP, AVIF)
- Image resizing and cropping
- Blur, sharpen, and filters
- Metadata extraction and modification
- Streaming support for large images

**Installation**:
```json
{
  "mcpServers": {
    "sharp": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sharp"]
    }
  }
}
```

---

### Screenshot MCP

⭐ N/A | 🔗 [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/screenshot)

**Description**: Simple and lightweight screenshot capture server for MCP. Minimal dependencies, maximum reliability.

**Key Features**:
- Full-page screenshots
- Element-specific captures
- Device emulation
- Dark mode support
- Delay and wait options

**Installation**:
```json
{
  "mcpServers": {
    "screenshot": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-screenshot"]
    }
  }
}
```

---

## Choosing a Vision Tool

| Tool | Best For | Browser Support | Learning Curve |
|------|----------|-----------------|----------------|
| Puppeteer MCP | General automation | Chrome only | Low |
| Playwright MCP | Cross-browser testing | All major | Medium |
| Browser Use | AI agent workflows | Chrome | Low |
| stagehand | Vision-based AI | Cloud browsers | Low |
| Sharp MCP | Image processing | N/A | Low |
| Screenshot MCP | Quick captures | Chrome | Very Low |

---

## See Also

- [Web Data Tools](../web-data/README.md) - For fetching and parsing web content
- [Execution Tools](../execution/README.md) - For running scripts that interact with browsers
