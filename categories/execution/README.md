# ⚡ Execution Tools

Sandboxed code execution, cloud functions, shell commands, and containerized environments that enable AI agents to run code safely.

## Overview

Execution tools enable AI agents to:
- **Run code** in isolated environments
- **Execute shell commands** securely
- **Deploy serverless functions** to the cloud
- **Containerize applications** for reproducibility
- **Handle timeouts and resource limits**

These tools are essential for code generation with verification, automated testing, data processing, and any workflow requiring runtime code execution.

---

## Tools

### E2B

⭐ ~6K Stars | 🔗 [GitHub](https://github.com/e2b-dev/awesome-ai-agents)

**Description**: Sandboxed cloud environment for running AI-generated code. Secure, scalable, and designed for LLM output verification.

**Key Features**:
- Isolated sandboxed execution
- Multiple language support (Python, Node, etc.)
- Filesystem isolation
- Network sandboxing
- Built-in npm/PyPI access
- Real-time streaming output

**Installation**:
```bash
pip install e2b
```

```python
from e2b import Sandbox

sandbox = Sandbox()
sandbox.run_code("print('Hello from E2B!')")
sandbox.close()
```

---

### Modal

⭐ ~14K Stars | 🔗 [GitHub](https://github.com/modal-labs/modal-client)

**Description**: Cloud platform for running code on AWS/GCP without managing infrastructure. Fast cold starts and GPU support.

**Key Features**:
- Serverless function deployment
- GPU acceleration
- Container management
- Volume mounts for data
- Batch processing
- Cron jobs and webhooks

**Installation**:
```bash
pip install modal
```

```python
import modal

app = modal.App()

@app.function()
def hello():
    return "Hello from Modal!"
```

---

### Shell/Command MCP

⭐ Official MCP Server | 🔗 [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/shell)

**Description**: Official MCP server for secure shell command execution. Run local terminal commands with safety controls.

**Key Features**:
- Command execution with output capture
- Working directory control
- Environment variable handling
- Piping and redirection support
- Timeout configuration
- Security policy controls

**Installation**:
```json
{
  "mcpServers": {
    "shell": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-shell"]
    }
  }
}
```

---

### Docker MCP

⭐ Community | 🔗 [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/docker)

**Description**: MCP server for Docker container management. Spin up containers for isolated execution environments.

**Key Features**:
- Container lifecycle management
- Image listing and pulling
- Volume management
- Network configuration
- Log streaming
- Multi-container orchestration

**Installation**:
```json
{
  "mcpServers": {
    "docker": {
      "command": "docker",
      "args": ["run", "--rm", "-it", "-v", "/var/run/docker.sock:/var/run/docker.sock", "mcp/server-docker"]
    }
  }
}
```

---

### Herdr

⭐ ~11K Stars | 🔗 [GitHub](https://github.com/ogulcancelik/herdr)

**Description**: Terminal multiplexer designed specifically for AI agents, similar to tmux but rebuilt from the ground up. Each agent gets its own real terminal with sidebar showing blocked/working/done status.

**Key Features**:
- Agent-optimized terminal multiplexing
- Real-time status sidebar
- Session persistence across disconnections
- Auto-detection for Claude Code, Codex, Cursor, Copilot, and 20+ agents
- Single ~10MB Rust binary, no GUI, no Electron, no telemetry
- Windows beta available (v0.7.1 released June 2026)
- Server mode for background session persistence

**Installation**:
```bash
# npm
npm install -g herdr

# Or download from GitHub releases
```

---

### Secure CLI MCP

⭐ Security-Focused | 🔗 [GitHub](https://github.com/MladenSU/safe-cli-mcp)

**Description**: Secure CLI MCP server with comprehensive security features including command whitelisting, path validation, and execution controls. Prevents shell operator injection and path traversal attacks.

**Key Features**:
- Command whitelist configuration
- Path validation and restriction
- Shell injection prevention
- Execution timeout limits
- Detailed error reporting
- Async operation support
- Working directory restriction

**Installation**:
```json
{
  "mcpServers": {
    "secure-cli": {
      "command": "npx",
      "args": ["-y", "safe-cli-mcp"],
      "env": {
        "ALLOWED_DIR": "/workspace",
        "ALLOWED_COMMANDS": "git,npm,node"
      }
    }
  }
}
```

---

## Choosing an Execution Tool

| Tool | Use Case | Latency | Cost | Security |
|------|----------|---------|------|----------|
| E2B | AI code verification | Medium | Pay-per-use | Very High |
| Modal | Production workloads | Low | Pay-per-use | High |
| Shell MCP | Local development | Very Low | Free | Medium |
| Docker MCP | Containerized tasks | Low | Infrastructure cost | High |
| Microsoft MXC | OS-level agent sandbox | Very Low | Free | Very High |

---

### Microsoft MXC (Execution Containers)

⭐ Microsoft Official | 🔗 [GitHub](https://github.com/microsoft/mxc)

**Description**: Cross-platform SDK for OS-level agent sandboxing. Defines what AI agents can access through JSON policies, enforced by the operating system at runtime. Used by GitHub Copilot CLI for constraining dynamically generated code.

**Key Features**:
- Cross-platform: Windows (ProcessContainer), Linux (Bubblewrap/LXC), macOS (Seatbelt)
- Policy-driven isolation via JSON configuration
- Filesystem, network, and UI access policies
- Session isolation with separate agent identity
- Enterprise integration via Intune/Entra
- TypeScript SDK: `@microsoft/mxc-sdk`
- Multiple backends: process sandbox → micro-VM → full VM

**Installation**:
```bash
npm install @microsoft/mxc-sdk
```

```typescript
import { spawnSandboxFromConfig, createConfigFromPolicy } from '@microsoft/mxc-sdk';

const config = createConfigFromPolicy({
  version: '0.6.0-alpha',
  filesystem: {
    readonlyPaths: ['/tools', '/libs'],
    readwritePaths: ['/tmp', '/workspace'],
  },
  network: { allowOutbound: false },
  timeoutMs: 30_000,
});
```

---

## Security Best Practices

1. **Always use sandboxes** for untrusted code
2. **Set resource limits** (CPU, memory, time)
3. **Network isolation** when possible
4. **Audit logs** for all executions
5. **Clean up** resources after use

---

## See Also

- [Code Awareness Tools](../code-awareness/README.md) - For understanding code before execution
- [Monitoring Tools](../monitoring/README.md) - For tracking execution results


---

### CC Switch

⭐ Trending | 🔗 [GitHub](https://github.com/farion1231/cc-switch)

**Description**: Unified management tool for AI coding CLI tools. Manage Claude Code, Codex CLI, Gemini CLI, and other AI development tools from a single interface. Supports model switching, MCP management, and Skills configuration.

**Key Features**:
- Unified management for Claude Code, Codex CLI, Gemini CLI
- One-click model switching (e.g., switch to DeepSeek, Qwen, GLM)
- MCP server management across all tools
- Skills and plugins configuration
- Local routing proxy for seamless model switching
- Cross-tool settings synchronization

**Installation**:
```bash
# npm
npm install -g cc-switch

# Or download from GitHub releases
```

---

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


### OpenWorker

⭐ ~3,700 Stars | 🔗 [GitHub](https://github.com/andrewyng/openworker)

**Description**: Andrew Ng's open-source desktop AI agent that delivers finished work, not chat. MIT-licensed, local-first, model-agnostic. Runs multi-step workflows across local files, connected apps (25+ integrations), and the terminal — returning documents, calendar changes, Slack messages, and more.

**Key Features**:
- Delivers finished work products (documents, reports, messages), not just chat
- Local-first architecture: all data stays on your machine
- Model-agnostic: supports OpenAI, Anthropic, Gemini, open-weight models, Ollama
- 25+ hosted integrations: GitHub, Slack, Jira, Notion, Google Calendar
- MCP protocol support for extensibility
- Typed risk engine for safe autonomous operation (Read/Write_local/Exec/External)
- Human-in-the-loop approval before consequential actions
- Tauri 2 desktop shell with React 18 UI
- Built on aisuite (Andrew Ng's provider-agnostic LLM library)

**Installation**:
```bash
# macOS: Download from GitHub releases
# Windows: Coming soon
git clone https://github.com/andrewyng/openworker.git
cd openworker
# Follow setup instructions in README
```

---
