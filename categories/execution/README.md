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

## Choosing an Execution Tool

| Tool | Use Case | Latency | Cost | Security |
|------|----------|---------|------|----------|
| E2B | AI code verification | Medium | Pay-per-use | Very High |
| Modal | Production workloads | Low | Pay-per-use | High |
| Shell MCP | Local development | Very Low | Free | Medium |
| Docker MCP | Containerized tasks | Low | Infrastructure cost | High |

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
