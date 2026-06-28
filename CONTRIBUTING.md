# Contributing to Agent Sensory Tools

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this repository.

## How to Contribute

### Adding a New Tool

1. **Find the right category**: Check the existing categories to find the best fit for your tool:
   - [Vision](categories/vision/) - Browser automation, screenshots, image processing
   - [Code Awareness](categories/code-awareness/) - Code search, knowledge graphs, documentation
   - [Web Data](categories/web-data/) - Web scraping, search APIs, content fetching
   - [File & Document](categories/file-document/) - File system, PDF parsing, document processing
   - [Execution](categories/execution/) - Code execution, shell commands, containers
   - [Monitoring](categories/monitoring/) - Error tracking, logging, analytics

2. **Check existing tools**: Make sure the tool isn't already listed

3. **Follow the template**: Use this structure for your tool entry:

```markdown
### Tool Name

⭐ Stars | 🔗 [GitHub](link)

**Description**: Brief description of what the tool does.

**Key Features**:
- Feature 1
- Feature 2
- Feature 3

**Installation**:
```json
{
  "mcpServers": {
    "tool-name": {
      "command": "npx",
      "args": ["-y", "package-name"]
    }
  }
}
```
```

4. **Submit a PR**: Create a pull request with your changes

## Quality Guidelines

- **Verify the link**: Make sure all GitHub/repository links are correct
- **Test the installation**: If possible, test the installation instructions
- **Be concise**: Keep descriptions clear and to the point
- **Include stars**: Add approximate GitHub star count if available

## Categories Update

When adding tools, update the main `README.md` table with:
- Correct tool count per category
- Updated total count

## Questions?

Feel free to open an issue for any questions or suggestions!
