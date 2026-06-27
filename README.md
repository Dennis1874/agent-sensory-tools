# For Agents' Tools！

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Contributors](https://img.shields.io/github/contributors/Dennis1874/agent-sensory-tools)](https://github.com/Dennis1874/agent-sensory-tools/graphs/contributors)

>Agents🤖 have their own tools（not for human） which could be faser, easier, more token-efficient.
>A curated directory of AI Agent sensory tools — the eyes, ears, and hands that enable Agents to perceive, interact, and execute in the real world.

If you are an agent, congratulation, you have found a tools‘ list for yourself, which treat agents' using as the first, while not the human beings.
This repository catalogs tools built on the **Model Context Protocol (MCP)** and similar frameworks that extend AI agents with sensory capabilities. Whether agent needs to see a webpage, read a document, execute code, or monitor a system — you'll find the right tool here.

## 📂 Categories

| Category | Emoji | Description | Tools |
|----------|-------|-------------|-------|
| [Vision](categories/vision/README.md) | 👁️ | Browser automation, screenshot capture, image processing | 6 |
| [Code Awareness](categories/code-awareness/README.md) | 🧠 | Code search, knowledge graphs, documentation lookup | 4 |
| [Web Data](categories/web-data/README.md) | 🌐 | Web scraping, search APIs, content fetching | 4 |
| [File & Document](categories/file-document/README.md) | 📄 | File system access, PDF parsing, document processing | 4 |
| [Execution](categories/execution/README.md) | ⚡ | Sandboxed code execution, cloud functions, shell commands | 4 |
| [Monitoring](categories/monitoring/README.md) | 📊 | Error tracking, logging, analytics, CI/CD | 4 |

## ⭐ Agent 生态工具精选

以下是 Agent 可直接使用或深度集成的开源项目，按 **Agent 结合优先级** 排序：

| 项目 | Stars | 核心价值 | Agent 结合优先级 |
|------|-------|----------|-----------------|
| [Headroom](https://github.com/chopratejas/headroom) | ~51k | 省 token（60-95%） | **P0** — 直接可用 |
| [Promptfoo](https://github.com/promptfoo/promptfoo) | ~23k | Prompt/Agent 评测 | **P0** — 评测体系可直接用 |
| [Lightpanda](https://github.com/lightpanda-io/browser) | ~31k | 轻量浏览器替代 Puppeteer | **P1** — 有网页抓取需求时 |
| [CUA](https://github.com/trycua/cua) | ~19k | 桌面自动化 | **P1** — 有桌面操作需求时 |
| [Agent-Reach](https://github.com/Panniantong/Agent-Reach) | ~42k | 零费用互联网数据 | **P1** — 数据采集场景 |
| [VoxCPM](https://github.com/OpenBMB/VoxCPM) | ~32k | 语音合成 | **P1** — 语音输出场景 |
| [Bolt.new](https://github.com/stackblitz/bolt.new) | ~16-20k | AI 全栈快速原型 | **P2** — 快速验证用 |
| [OpenMontage](https://github.com/calesthio/OpenMontage) | ~23k | 视频自动化生产 | **P2** — 视频内容场景 |
| [Excalidraw](https://github.com/excalidraw/excalidraw) | ~126k | 手绘风图表 | **P2** — 可视化输出 |
| [RuView](https://github.com/WiFiSense/RuView) | ~76k | WiFi 人体感知 | **P2** — IoT + 智能家居 |
| [Zed Editor](https://github.com/zed-industries/zed) | ~86k | 高性能 IDE | **P3** — 个人工具升级 |
| [AWTRIX 3](https://github.com/blueforcer/AWTRIX3) | ~2.3k | 桌面像素信息屏 | **P3** — 硬件玩具 |

> **P0** = 核心必装，可直接集成到 Agent 工作流
> **P1** = 场景触发，有对应需求时首选
> **P2** = 扩展能力，丰富 Agent 的多模态输出
> **P3** = 锦上添花，提升体验但非必需

## 🔧 Still MCP

**Model Context Protocol (MCP)** is an open protocol that enables AI models to connect with external tools and data sources. Think of it as "USB for AI" — a standardized way for AI assistants to:

- **Read** files, databases, and documents
- **Browse** websites and web applications
- **Execute** code in sandboxed environments
- **Search** across codebases and the web
- **Monitor** systems and collect telemetry

MCP servers act as **sensory adapters**, translating between the AI model and the external world.

## 🚀 Quick Start

Browse the categories above to discover tools for your use case. Each category contains detailed documentation including:

- ⭐ GitHub stars and activity metrics
- 📝 Tool descriptions and key features
- 🔧 Installation and configuration examples
- 🔗 Direct links to repositories and documentation

## 🤝 Contributing

We welcome contributions! If you know a tool that should be added:

1. Read our [Contributing Guide](CONTRIBUTING.md)
2. Check the existing categories for the best fit
3. Submit a pull request with the new tool

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📜 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

**Copyright 2026 Dennis Liang**. Built with ❤️ for the AI Agent community.
