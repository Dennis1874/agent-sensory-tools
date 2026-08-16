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

### Agent QA

⭐ 800+ Stars | 🔗 [GitHub](https://github.com/vostride/agent-qa)

**Description**: Natural-language web and mobile regression QA exposed through MCP, with evidence retained for repeatable application-level checks.

**Key Features**:
- Natural-language regression workflows
- Screenshots plus DOM, network, and console evidence
- Persistent test memory across runs
- Failure triage and retained artifacts
- CLI and MCP interfaces
- Source-available under FSL-1.1-ALv2; each release converts to Apache-2.0 after two years

**Installation**:
```json
{
  "mcpServers": {
    "agent-qa": {
      "command": "npx",
      "args": ["-y", "agent-qa", "mcp"]
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

### Chrome DevTools MCP

⭐ Google Official | 🔗 [GitHub](https://github.com/google/chrome-devtools-mcp)

**Description**: Official MCP server from Chrome DevTools team. Enables AI to directly read console logs, network requests, DOM structure, and control the browser through Developer Tools protocol.

**Key Features**:
- Direct access to browser console logs and errors
- Network request monitoring and inspection
- DOM structure reading and manipulation
- Accessibility tree for reliable element detection
- No screenshot dependency - reads actual browser state

**Installation**:
```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "@chrome-devtools-mcp/server"]
    }
  }
}
```

---

### agent-browser

⭐ Rust Native | 🔗 [GitHub](https://github.com/agent-browser/agent-browser)

**Description**: High-performance browser automation CLI for AI agents, built with native Rust. Provides snapshot and ref capabilities optimized for AI understanding of page state.

**Key Features**:
- Native Rust implementation for speed
- Snapshot command for complete page state
- Ref command for semantic element referencing
- Multi-tab management
- Cookie and storage manipulation
- PDF export and screenshot

**Installation**:
```bash
# npm
npm install -g agent-browser

# Homebrew (macOS)
brew install agent-browser

# Rust
cargo install agent-browser
agent-browser install --with-deps
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

### Safari MCP Server

⭐ Apple Official | 🔗 [WebKit Blog](https://webkit.org/)

**Description**: Apple's official MCP server for Safari Technology Preview, enabling coding agents to directly inspect and debug websites. Access page content, console logs, network requests, screenshots, and interact with page elements.

**Key Features**:
- Direct browser inspection for AI agents
- Console log access and debugging
- Network request monitoring
- Screenshot capture
- Page interaction (click, input, scroll)
- Safari compatibility issue detection
- Performance analysis and accessibility checking

**Installation**:
Available in Safari Technology Preview 247+. Enable through Safari preferences under Develop > MCP Server.

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
| Agent QA | Regression QA with retained evidence | Web and mobile | Medium |
| Browser Use | AI agent workflows | Chrome | Low |
| stagehand | Vision-based AI | Cloud browsers | Low |
| Chrome DevTools MCP | Debugging & inspection | Chrome | Low |
| agent-browser | High-performance CLI | Chrome | Medium |
| Sharp MCP | Image processing | N/A | Low |
| Screenshot MCP | Quick captures | Chrome | Very Low |
| Actionbook MCP | Authenticated sessions | Chrome Extension | Low |
| PyMCPAutoGUI | Desktop GUI automation | N/A (Desktop) | Medium |
| Stealth Browser MCP | Anti-bot stealth browsing | Chrome (via Playwright) | Medium |
| Vessel Browser | AI-native agent browser | Chromium (custom) | Medium |
| MCPBrowser | AI-first clean HTML extraction | Chrome/Edge/Brave | Low |
| Azure Foundry Browser | Enterprise cloud browser automation | Playwright (Azure) | Medium |
| Windows 365 for Agents | Full cloud PC control | Edge (Windows 365) | High |

---

### Actionbook MCP

⭐ Chrome Extension | 🔗 [Actionbook](https://actionbook.so)

**Description**: Chrome extension that connects AI assistants to your real browser. Uses your actual logged-in sessions, so AI can interact with websites that require authentication without needing separate credentials.

**Key Features**:
- Uses your real browser with your logged-in sessions
- AI can click, fill forms, navigate, and submit on your behalf
- Multi-tab support for parallel information gathering
- Read current page content without screenshots
- Works with any MCP-compatible client (Claude, Cursor, etc.)
- Human-in-the-loop: you can see and intervene at any time

**Installation**:
```bash
# Install Chrome extension from Actionbook website
# Then configure MCP:
{
  "mcpServers": {
    "actionbook": {
      "command": "npx",
      "args": ["-y", "@actionbook/mcp"]
    }
  }
}
```

---

### PyMCPAutoGUI

⭐ GUI Automation | 🔗 [GitHub](https://github.com/nicekid1/PyMCPAutoGUI)

**Description**: GUI automation tool for AI agents via MCP protocol. Provides mouse/keyboard control, screenshot capture, and window management capabilities for desktop automation workflows.

**Key Features**:
- Mouse and keyboard control for AI agents
- Screenshot capture and analysis
- Window management (move, resize, focus)
- Screen coordinate-based automation
- Seamless MCP integration with Cursor and other editors
- Python-based, easy to extend

**Installation**:
```bash
pip install pymcpautogui
```

---

## See Also

- [Web Data Tools](../web-data/README.md) - For fetching and parsing web content
- [Execution Tools](../execution/README.md) - For running scripts that interact with browsers

### Stealth Browser MCP

⭐ Trending | 🔗 [GitHub](https://github.com/vibheksoni/stealth-browser-mcp)

**Description**: Anti-bot browser automation MCP server using Playwright with stealth plugins. Bypasses Cloudflare, DataDome, and other bot detection systems while providing full browser automation capabilities to AI agents.

**Key Features**:
- Anti-detection via puppeteer-extra-plugin-stealth and playwright-extra
- Browser fingerprint modification (WebGL, canvas, fonts, plugins)
- Full-page and element-specific screenshots
- Headless and headed browser modes
- MCP protocol integration via FastMCP
- Bypasses common bot detection systems

**Installation**:
```bash
# Install dependencies
bun install

# Run the MCP server
bun start
```

---

### Vessel Browser

⭐ Open Source AI Browser | 🔗 [GitHub](https://github.com/unmodeled-tyler/vessel-browser)

**Description**: Open-source AI-native browser built from the ground up for agents. Provides durable state management, MCP control, and BYOK (Bring Your Own Key) with full autonomous browsing across Linux, macOS, and Windows. Compatible with Hermes Agent, OpenClaw, and any MCP client.

**Key Features**:
- Built specifically for AI agent control, not human browsing
- Durable session state across restarts
- Full MCP server for agent-driven navigation
- BYOK model support — connect any LLM provider
- Cross-platform: Linux, macOS, Windows
- Human-in-the-loop supervision mode
- Autonomous browsing with guardrails

**Installation**:
```bash
# npm
npm install @quanta-intellect/vessel-browser

# Or clone and build
git clone https://github.com/unmodeled-tyler/vessel-browser.git
cd vessel-browser && npm install && npm start
```

---

### MCPBrowser

⭐ AI-First Browser MCP | 🔗 [GitHub/npm](https://www.npmjs.com/package/mcpbrowser)

**Description**: AI-optimized browser MCP server built specifically for AI agents. Uses Puppeteer under the hood but adds an intelligence layer: clean HTML output (90% smaller), automatic SPA detection (React, Vue, Angular), authentication flow handling (SSO, redirects, multi-step login), form discovery with multi-field filling, and domain-based tab reuse. Each tool call replaces 5-8 raw Puppeteer/Playwright calls.

**Key Features**:
- Clean LLM-optimized HTML output (~90% smaller than raw DOM)
- Auto-detects React, Vue, Angular, Svelte, Next.js, Nuxt with framework-aware wait strategies
- Detects login pages, SSO redirects, multi-step auth flows automatically
- Form discovery: `browser_detect_forms` finds all fields, labels, constraints
- Instant DOM re-extraction without page reloads (10-50x faster)
- Plugin system with site-specific actions and confidence scoring
- Works with Chrome, Edge, or Brave browsers
- VS Code extension available

**Installation**:
```json
{
  "mcpServers": {
    "mcpbrowser": {
      "command": "npx",
      "args": ["-y", "mcpbrowser"]
    }
  }
}
```

---

### Azure Foundry Browser Automation

⭐ Microsoft Official | 🔗 [Microsoft Learn](https://learn.microsoft.com/en-in/Azure/foundry/agents/how-to/tools/browser-automation)

**Description**: Microsoft's Browser Automation Preview Tool for Azure AI Foundry agents. Provides Playwright-based browser automation capabilities to AI agents running in Azure. Supports navigation, page content reading, element interaction, and screenshot capture — all through the Agent 365 Tooling Gateway with enterprise-grade security and governance.

**Key Features**:
- Playwright-based browser automation in Azure cloud
- Navigate, click, type, fill forms, read page content
- Screenshot capture for visual verification
- Integration with Azure AI Foundry agent framework
- MCP-compatible endpoint via Agent 365 Toolbox
- Enterprise security via Azure Entra authentication
- Supports both Python and C# SDKs

**Installation**:
```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.tools import BrowserAutomationPreviewTool

tool = BrowserAutomationPreviewTool(
    browser_automation_preview=BrowserAutomationToolParameters(
        connection=BrowserAutomationToolConnectionParameters(
            project_connection_id=BROWSER_CONNECTION_ID,
        )
    )
)
```

---

### Windows 365 for Agents MCP Server

⭐ Microsoft Official | 🔗 [Microsoft Learn](https://learn.microsoft.com/microsoft-copilot-studio/mcp-windows-365-agents-work-iq)

**Description**: Microsoft's MCP server providing full operational control of a Windows 365 cloud PC for AI agents. Combines desktop interaction (mouse, keyboard, screenshots), Edge browser automation, and Windows UI Automation semantic inspection — giving agents a complete Windows environment to operate in.

**Key Features**:
- Full desktop interaction: mouse, keyboard, screenshot, command execution
- Edge browser automation: navigate, click, type, fill forms, multi-tab management
- Windows UI Automation tree inspection for semantic element discovery
- Sandboxed shell command execution with allowlist (git, npm, dotnet, python, etc.)
- Accessibility-based element targeting via UI Automation
- Batch browser actions in a single call
- Cookie inspection and page PDF export
- Enterprise security via Microsoft 365 admin center

**Installation**:
```json
{
  "mcpServers": {
    "windows365": {
      "url": "https://agent365.svc.cloud.microsoft/agents/tenants/{tenantId}/servers/mcp_W365ComputerUse"
    }
  }
}
```

---
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
