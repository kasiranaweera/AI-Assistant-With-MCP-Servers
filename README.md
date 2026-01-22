# AI-Assistant-With-MCP-Servers

Build custom MCP (Model Context Protocol) servers and connect them to AI clients using LangChain and Groq API.

## Overview

This project demonstrates how to:
- **Create Custom MCP Servers** - Build your own MCP servers with FastMCP for specific functionality (Math operations, Weather data, etc.)
- **Connect Servers to Clients** - Use multiple transport protocols (stdio, HTTP) to connect MCP servers to AI clients
- **Leverage LangChain & Groq** - Build intelligent AI agents powered by Groq's fast LLM API
- **Enable Agent Tool Usage** - Expose server tools to AI agents for dynamic execution and reasoning

## Features

✨ **Custom MCP Servers**
- **Math Server** - Arithmetic operations (add, subtract, multiply, divide) via stdio transport
- **Weather Server** - Weather information retrieval via HTTP transport
- Easily extensible to add more servers

🔌 **Multiple Transport Protocols**
- **stdio** - Direct server-to-client communication for lightweight servers
- **Streamable HTTP** - Network-accessible servers for distributed architectures

🤖 **AI-Powered Agents**
- Uses Groq's high-speed LLM (llama-3.1-8b-instant)
- Agents automatically discover and use server tools
- Configurable agent behavior with max steps and temperature settings

💾 **Conversation Memory** (v1.0.0)
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

### MCP Server Setup

**v1.0.0** - Uses NPX-based MCP servers via `browser_mcp.json`:
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

**v2.0.0** - Custom MCP servers with multiple transports:
- **Math Server** (`mathserver.py`): Runs via stdio transport
- **Weather Server** (`weather.py`): Runs via streamable HTTP transport on `http://localhost:8000/mcp`

### Agent Configuration

Customize agent behavior in your client:
- `max_steps`: Maximum number of tool calls (default: 10)
- `temperature`: LLM creativity level 0-1 (default: 0.7)
- `max_retries`: Groq API retry attempts (default: 3)

## Usage

### v1.0.0 - Interactive Chat with MCP Servers

```bash
cd v1.0.0
uv run app.py
```

**Interactive Commands:**
- **Ask questions**: Type any query and the agent will use available tools
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

### v2.0.0 - Multi-Server Client

This version demonstrates connecting multiple custom MCP servers to a client.

**Step 1: Start the Weather Server** (HTTP transport)
```bash
cd v2.0.0
python weather.py
```

**Step 2: Run the Client** (in a new terminal)
```bash
cd v2.0.0
python client.py
```

The client will:
1. Connect to the Math server via stdio
2. Connect to the Weather server via HTTP
3. Send queries to the AI agent that uses both servers' tools
4. Display results for math operations and weather queries

## Example Output

```
Math Response: 10 + 20 = 30

Weather Response: The weather in Tokyo is sunny
=============================================

You: Find me 5-star hotels in New York