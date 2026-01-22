# AI-Assistant-With-MCP-Servers

Build an AI Assistant with Model Context Protocol (MCP) Servers and tools using LangChain and Groq API.

## Overview

This project demonstrates how to build an intelligent AI assistant that can:
- **Interact with Multiple MCP Servers** - Browser automation (Playwright), web search (DuckDuckGo), and accommodation listings (Airbnb)
- **Use LangChain & Groq** - Leverage the fast Groq API with LangChain for intelligent agent-based reasoning
- **Maintain Conversation Memory** - Keep track of conversation history for context-aware responses
- **Handle Rate Limiting** - Gracefully manage API rate limits with automatic retry mechanisms

## Features

✨ **Interactive Chat Interface**
- Command-line based chat with real-time responses
- Support for multi-turn conversations with memory

🛠️ **Integrated MCP Servers**
- **Playwright MCP**: Browser automation for web scraping and interaction
- **DuckDuckGo MCP**: Web search capabilities
- **Airbnb MCP**: Access to accommodation listings and details

🤖 **AI-Powered Agent**
- Uses Groq's high-speed LLM (llama-3.1-8b-instant)
- Configurable agent behavior with max steps and temperature settings
- Automatic error handling and rate limit management

💾 **Conversation Memory**
- Maintains conversation history throughout the session
- Clear history with a simple command

## Requirements

- Python 3.10+
- Node.js (for running MCP servers via npx)
- API Keys:
  - `GROQ_API_KEY` - Get from [Groq Console](https://console.groq.com)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kasiranaweera/AI-Assistant-With-MCP-Servers.git
   cd AI-Assistant-With-MCP-Servers
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   uv pip install -r pyproject.toml
   # OR
   pip install -e .
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your GROQ_API_KEY
   ```

## Configuration

### MCP Servers Configuration

The `browser_mcp.json` file configures the MCP servers:

```json
{
    "mcpServers": {
      "playwright": {
        "command": "npx",
        "args": ["@playwright/mcp@latest"]
      },
      "airbnb": {
        "command": "npx",
        "args": ["-y", "@openbnb/mcp-server-airbnb"]
      },
      "duckduckgo-search": {
        "command": "npx",
        "args": ["-y", "duckduckgo-mcp-server"]
      }
    }
}
```

### Agent Configuration

Customize agent behavior in `app.py`:
- `max_steps`: Maximum number of tool calls (default: 10)
- `temperature`: LLM creativity level 0-1 (default: 0.7)
- `max_retries`: Groq API retry attempts (default: 3)

## Usage

### Running the Application

```bash
uv run app.py
```

Or with your Python environment:
```bash
python app.py
```

### Interactive Commands

Once the chat starts, you can:

- **Ask questions**: Type any query and the agent will use available tools to find answers
  ```
  You: provide me some hotel listings to stay in New York
  ```

- **Clear history**: Remove conversation history
  ```
  You: clear
  ```

- **Exit chat**: End the conversation
  ```
  You: exit
  ```

- **Exit gracefully**: Press `Ctrl+C` to terminate

## Example Usage

```
=========== Interactive MCP Chat ============
Type 'exit' or 'quit' to end the conversation
Type 'clear' to clear conversation history
=============================================

You: Find me 5-star hotels in New York