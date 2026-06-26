# Contributing to Agent Sensory Tools

Thank you for your interest in contributing! This guide will help you add new tools to the directory.

## How to Contribute

### 1. Before You Start

- **Search first**: Check if the tool already exists in the relevant category
- **Verify the tool**: Ensure it's actively maintained and genuinely useful for AI agents
- **Check the format**: Review this guide for the expected content structure

### 2. Adding a New Tool

Each tool entry should include:

```markdown
### Tool Name
⭐ Stars: XX | 🔗 [GitHub](url)

**Description**: One-sentence description of the tool

**Key Features**:
- Feature 1
- Feature 2
- Feature 3

**Installation**:
```json
// Configuration example
```
```

### 3. Category Guidelines

Choose the right category for your tool:

| Category | What Belongs Here |
|----------|-------------------|
| `vision/` | Browser automation, screenshots, image processing |
| `code-awareness/` | Code search, documentation lookup, knowledge graphs |
| `web-data/` | Web scraping, search APIs, content fetching |
| `file-document/` | File operations, PDF parsing, document processing |
| `execution/` | Code execution, shell commands, containers |
| `monitoring/` | Error tracking, logging, analytics, CI/CD |

### 4. Submission Process

1. **Fork the repository**
2. **Create a branch**: `git checkout -b add/tool-name`
3. **Add your tool** to the appropriate category README
4. **Test your markdown** renders correctly
5. **Commit**: `git commit -m "Add [Tool Name] to [Category]"`
6. **Push**: `git push origin add/tool-name`
7. **Open a Pull Request**

### 5. Quality Standards

Good tool entries:
- ✅ Use the official repository URL
- ✅ Include accurate star counts (with "as of YYYY-MM" note if uncertain)
- ✅ Provide working installation examples
- ✅ Describe unique features (not generic features)
- ✅ Include the tool's official description verbatim when possible

Avoid:
- ❌ Duplicate tools already listed
- ❌ Abandoned/deprecated projects (unless historically significant)
- ❌ Very niche tools without clear use cases
- ❌ Broken links or outdated information

### 6. Keeping Information Current

- Star counts are approximate - use "N/A" if uncertain
- Note the date when star counts were verified
- If a tool significantly changes, consider updating its entry

## Questions?

Open an issue for discussion before submitting large contributions.

## Thank You!

Every contribution helps the AI agent community discover better tools.
