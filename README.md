# AI-Assistant-With-MCP-Servers# AI-Assistant-With-MCP-Servers



Build an interactive AI Assistant with Model Context Protocol (MCP) Servers and tools using LangChain and Groq API.Build an interactive AI Assistant with Model Context Protocol (MCP) Servers and tools using LangChain and Groq API.



## Overview## Overview



This project demonstrates how to build an intelligent AI assistant that can:This project demonstrates how to build an intelligent AI assistant that can:

- **Interact with Multiple MCP Servers** - Browser automation (Playwright), web search (DuckDuckGo), and accommodation listings (Airbnb)- **Interact with Multiple MCP Servers** - Browser automation (Playwright), web search (DuckDuckGo), and accommodation listings (Airbnb)

- **Use LangChain & Groq** - Leverage the fast Groq API with LangChain for intelligent agent-based reasoning- **Use LangChain & Groq** - Leverage the fast Groq API with LangChain for intelligent agent-based reasoning

- **Maintain Conversation Memory** - Keep track of conversation history for context-aware responses- **Maintain Conversation Memory** - Keep track of conversation history for context-aware responses

- **Handle Rate Limiting** - Gracefully manage API rate limits with automatic retry mechanisms- **Handle Rate Limiting** - Gracefully manage API rate limits with automatic retry mechanisms



## Features## Features



✨ **Interactive Chat Interface**✨ **Interactive Chat Interface**

- Command-line based chat with real-time responses- Command-line based chat with real-time responses

- Support for multi-turn conversations with memory- Support for multi-turn conversations with memory

- Graceful error handling and Ctrl+C support

🛠️ **Integrated MCP Servers**

🛠️ **Integrated MCP Servers**- **Playwright MCP**: Browser automation for web scraping and interaction

- **Playwright MCP**: Browser automation for web scraping and interaction- **DuckDuckGo MCP**: Web search capabilities

- **DuckDuckGo MCP**: Web search capabilities- **Airbnb MCP**: Access to accommodation listings and details

- **Airbnb MCP**: Access to accommodation listings and details

🤖 **AI-Powered Agent**

🤖 **AI-Powered Agent**- Uses Groq's high-speed LLM (llama-3.1-8b-instant)

- Uses Groq's high-speed LLM (llama-3.1-8b-instant)- Configurable agent behavior with max steps and temperature settings

- Configurable agent behavior with max steps and temperature settings- Automatic error handling and rate limit management

- Automatic error handling and rate limit management

- Non-blocking async input to prevent event loop freezing💾 **Conversation Memory**

- Maintains conversation history throughout the session

💾 **Conversation Memory**- Clear history with a simple command

- Maintains conversation history throughout the session

- Clear history with a simple command## Requirements



## Requirements- Python 3.10+

- Node.js (for running MCP servers via npx)

- Python 3.10+- API Keys:

- Node.js (for running MCP servers via npx)  - `GROQ_API_KEY` - Get from [Groq Console](https://console.groq.com)

- API Keys:

  - `GROQ_API_KEY` - Get from [Groq Console](https://console.groq.com)## Installation



## Installation1. **Clone the repository**

   ```bash

1. **Clone the repository**   git clone https://github.com/kasiranaweera/AI-Assistant-With-MCP-Servers.git

   ```bash   cd AI-Assistant-With-MCP-Servers

   git clone https://github.com/kasiranaweera/AI-Assistant-With-MCP-Servers.git   ```

   cd AI-Assistant-With-MCP-Servers

   ```2. **Create a virtual environment**

   ```bash

2. **Create a virtual environment**   python -m venv .venv

   ```bash   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

   python -m venv .venv   ```

   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

   ```3. **Install dependencies**

   ```bash

3. **Install dependencies**   uv pip install -r pyproject.toml

   ```bash   # OR

   uv pip install -r pyproject.toml   pip install -e .

   # OR   ```

   pip install -e .

   ```4. **Set up environment variables**

   ```bash

4. **Set up environment variables**   cp .env.example .env

   ```bash   # Edit .env and add your GROQ_API_KEY

   cp .env.example .env   ```

   # Edit .env and add your GROQ_API_KEY

   ```## Configuration



## Configuration### MCP Servers Configuration



### MCP Servers ConfigurationThe `browser_mcp.json` file configures the MCP servers:



The `browser_mcp.json` file configures the MCP servers:```json

{

```json    "mcpServers": {

{      "playwright": {

    "mcpServers": {        "command": "npx",

      "playwright": {        "args": ["@playwright/mcp@latest"]

        "command": "npx",      },

        "args": ["@playwright/mcp@latest"]      "airbnb": {

      },        "command": "npx",

      "airbnb": {        "args": ["-y", "@openbnb/mcp-server-airbnb"]

        "command": "npx",      },

        "args": ["-y", "@openbnb/mcp-server-airbnb"]      "duckduckgo-search": {

      },        "command": "npx",

      "duckduckgo-search": {        "args": ["-y", "duckduckgo-mcp-server"]

        "command": "npx",      }

        "args": ["-y", "duckduckgo-mcp-server"]    }

      }}

    }```

}

```### Agent Configuration



### Agent ConfigurationCustomize agent behavior in `app.py`:

- `max_steps`: Maximum number of tool calls (default: 10)

Customize agent behavior in `app.py`:- `temperature`: LLM creativity level 0-1 (default: 0.7)

- `max_steps`: Maximum number of tool calls (default: 10)- `max_retries`: Groq API retry attempts (default: 3)

- `temperature`: LLM creativity level 0-1 (default: 0.7)

- `max_retries`: Groq API retry attempts (default: 3)## Usage



## Usage### Running the Application



### Running the Application```bash

uv run app.py

```bash```

uv run app.py

```Or with your Python environment:

```bash

Or with your Python environment:python app.py

```bash```

python app.py

```### Interactive Commands



### Interactive CommandsOnce the chat starts, you can:



Once the chat starts, you can:- **Ask questions**: Type any query and the agent will use available tools to find answers

  ```

- **Ask questions**: Type any query and the agent will use available tools to find answers  You: provide me some hotel listings to stay in New York

  ```  ```

  You: provide me some hotel listings to stay in New York

  ```- **Clear history**: Remove conversation history

  ```

- **Clear history**: Remove conversation history  You: clear

  ```  ```

  You: clear

  ```- **Exit chat**: End the conversation

  ```

- **Exit chat**: End the conversation  You: exit

  ```  ```

  You: exit

  ```- **Exit gracefully**: Press `Ctrl+C` to terminate



- **Exit gracefully**: Press `Ctrl+C` to terminate## Example Usage



## Error Handling & Rate Limiting```

=========== Interactive MCP Chat ============

The application includes robust error handling for:Type 'exit' or 'quit' to end the conversation

Type 'clear' to clear conversation history

- **Rate Limiting (429 errors)**: Automatically waits 30 seconds before retrying=============================================

- **Keyboard Interrupts**: Gracefully handles Ctrl+C and cleans up resources

- **Network Errors**: Displays clear error messages and continues operationYou: Find me 5-star hotels in New York
- **API Timeouts**: Groq client automatically retries up to 3 times

## Architecture

### Key Components

1. **MCPClient**: Manages connections to multiple MCP servers
2. **MCPAgent**: Orchestrates tool use and conversation logic
3. **ChatGroq**: LLM interface for intelligent reasoning
4. **Async Event Loop**: Non-blocking input/output for responsive UI

### Tool Set

The agent has access to 25 tools across 3 MCP servers:

**Browser Tools** (Playwright):
- Navigation, screenshot, click, type, drag, hover, evaluate scripts, etc.

**Search Tools** (DuckDuckGo):
- Web search with configurable safety settings and result counts

**Accommodation Tools** (Airbnb):
- Search listings and get detailed information about properties

## Troubleshooting

### Issue: "Too Many Requests" (429 error)
**Solution**: The application automatically handles this by waiting 30 seconds. Reduce the frequency of requests or add delays between queries.

### Issue: "Cannot read properties of null"
**Solution**: This typically occurs when required parameters (like check-in/check-out dates) are missing. Provide specific dates in your queries:
```
You: Find hotels in New York for February 15-17, 2 adults
```

### Issue: KeyboardInterrupt crashes
**Solution**: Fixed in the latest version. Now handles Ctrl+C gracefully and cleans up resources.

### Issue: DuckDuckGo rate limiting
**Solution**: The service blocks rapid requests. The app includes built-in delays. Wait between queries or stick to specific questions.

## Project Structure

```
.
├── app.py                 # Main application entry point
├── main.py               # Alternative entry point
├── browser_mcp.json      # MCP servers configuration
├── pyproject.toml        # Project dependencies
└── README.md            # This file
```

## Key Improvements Made

✅ **Non-blocking Input**: Uses `loop.run_in_executor()` to prevent blocking the async event loop
✅ **Rate Limit Handling**: Automatically detects and handles 429 errors with delays
✅ **Better Error Messages**: Shows error type and truncated details for debugging
✅ **Graceful Shutdown**: Properly closes sessions on exit or interrupt
✅ **Retry Logic**: Groq client configured with max_retries for resilience
✅ **Reduced Agent Steps**: Max steps reduced from 15 to 10 to minimize API calls

## Example Use Cases

1. **Travel Planning**: Find accommodations and search for travel information
2. **Web Scraping**: Automate browser tasks to extract data
3. **General Q&A**: Use DuckDuckGo search for informational queries
4. **Multi-tool Orchestration**: Combine multiple tools to solve complex problems

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## Resources

- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [LangChain Documentation](https://python.langchain.com/)
- [Groq API Documentation](https://console.groq.com/docs)
- [Playwright MCP Server](https://github.com/mark3labs/mcp-server-playwright)
- [DuckDuckGo MCP Server](https://github.com/aphasiayc/duckduckgo-mcp-server)
- [Airbnb MCP Server](https://github.com/openbnb/mcp-server-airbnb)
