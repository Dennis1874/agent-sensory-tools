# 📄 File & Document Tools

File system access, PDF parsing, document processing, and content extraction tools that enable AI agents to read and write documents.

## Overview

File and document tools enable AI agents to:
- **Read and write** local and remote files
- **Parse PDFs** and extract text/tables
- **Process documents** (Word, Excel, etc.)
- **Watch for file changes**
- **Handle various formats** (Markdown, JSON, CSV, etc.)

These tools are essential for document automation, data processing, content management, and any workflow involving file operations.

---

## Tools

### Filesystem MCP

⭐ Official MCP Server | 🔗 [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)

**Description**: Official MCP server for local filesystem operations. Secure file reading, writing, and directory management.

**Key Features**:
- Read/write files with path control
- Directory listing and navigation
- File search (glob patterns)
- Create directories
- Move, copy, delete operations
- Path safety validation

**Installation**:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem"],
      "env": {
        "ALLOWED_DIRECTORIES": "/path/to/allowed/directory"
      }
    }
  }
}
```

---

### Unstructured MCP

⭐ ~7K Stars | 🔗 [GitHub](https://github.com/Unstructured-IO/unstructured-mcp)

**Description**: MCP server for Unstructured.io's document parsing platform. Handles over 30 document formats intelligently.

**Key Features**:
- PDF parsing with layout preservation
- Table extraction (structured)
- Image extraction from documents
- Support for 30+ file types
- Chunking strategies for RAG
- Cloud-hosted processing available

**Installation**:
```json
{
  "mcpServers": {
    "unstructured": {
      "command": "unstructured-mcp",
      "args": []
    }
  }
}
```

Or use the Python SDK:
```bash
pip install unstructured
```

---

### Anthropic PDF Skill

⭐ Anthropic Official | 🔗 [Documentation](https://docs.anthropic.com/en/docs/build-with-claude/skill-api/pdf)

**Description**: Anthropic's official PDF parsing skill for Claude. Native PDF understanding with layout awareness.

**Key Features**:
- Native PDF text extraction
- Layout-preserving parsing
- Table structure detection
- Image extraction
- Multi-column handling
- Direct API integration

**Installation**:
Available through Anthropic API as a built-in capability. Configure via Anthropic console.

---

### MarkItDown

⭐ ~85K Stars | 🔗 [GitHub](https://github.com/microsoft-markitdown)

**Description**: Microsoft's official universal document converter. Converts PDF, Word, Excel, images, and audio to Markdown - optimized for AI analysis.

**Key Features**:
- Universal format conversion to Markdown
- PDF parsing with layout preservation
- Word document processing
- Excel spreadsheet conversion
- Image text extraction (OCR)
- Audio transcription support
- Designed specifically for AI consumption

**Installation**:
```bash
# npm
npm install -g @microsoft/markitdown

# Python
pip install markitdown

# CLI usage
markitdown input.pdf -o output.md
```

---

### Syncfusion DocumentSDK AI Agent Tools

⭐ Enterprise Grade | 🔗 [GitHub](https://github.com/syncfusion/ai-agent-document-processing)

**Description**: .NET-based document processing by Syncfusion. Enterprise-quality handling for Word, Excel, PDF, and more.

**Key Features**:
- Word document parsing and generation
- Excel workbook manipulation
- PDF creation and editing
- PowerPoint processing
- File format conversion
- .NET ecosystem integration

**Installation**:
```bash
dotnet add package Syncfusion.DocIORenderer.Net
dotnet add package Syncfusion.Pdf.Net
dotnet add package Syncfusion.XlsIO.Net
```

---

## Supported Formats

| Tool | PDF | Word | Excel | PowerPoint | Images |
|------|-----|------|-------|------------|--------|
| Filesystem MCP | ❌ | ❌ | ❌ | ❌ | ❌ |
| MarkItDown | ✅ | ✅ | ✅ | ❌ | ✅ |
| Unstructured MCP | ✅ | ✅ | ✅ | ✅ | ✅ |
| Anthropic PDF Skill | ✅ | ❌ | ❌ | ❌ | ✅ |
| Syncfusion | ✅ | ✅ | ✅ | ✅ | ✅ |
| Talonic MCP | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## See Also

- [Code Awareness Tools](../code-awareness/README.md) - For code file handling
- [Execution Tools](../execution/README.md) - For running scripts that process files

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


### Talonic MCP

⭐ Production-Ready | 🔗 [GitHub](https://github.com/talonicdev/talonic-mcp) | 🔗 [NPM](https://www.npmjs.com/package/@talonic/mcp)

**Description**: Enterprise-grade document extraction MCP server. Extracts structured, schema-validated JSON data from any document — PDFs, scans, invoices, contracts, forms — with per-field confidence scores. Also supports OCR to Markdown and omnisearch across documents.

**Key Features**:
- Schema-validated JSON extraction with confidence scores
- OCR to clean Markdown conversion
- Omni-search across documents, fields, sources, and schemas
- Document filtering by extracted field values
- Browser upload support for large files
- Dual transport: stdio (local) and Streamable HTTP (hosted)
- Listed on official MCP Registry
- 11 tools and 2 resources
- Compatible with Claude.ai hosted connector

**Installation**:
```json
{
  "mcpServers": {
    "talonic": {
      "command": "npx",
      "args": ["-y", "@talonic/mcp"]
    }
  }
}
```

---
