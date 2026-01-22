import asyncio
import sys
from datetime import datetime, timedelta

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient
import os

async def run_memory_chat():
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    config_file = "browser_mcp.json"

    print("Initializing chat...")

    client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.7,
        max_retries=3,
    )

    agent = MCPAgent(
        llm = llm,
        client = client,
        max_steps = 10,
        memory_enabled = True,
    )

    print("\n=========== Interactive MCP Chat ============")
    print("Type 'exit' or 'quit' to end the conversation")
    print("Type 'clear' to clear conversation history")
    print("=============================================")

    loop = asyncio.get_event_loop()
    
    try:
        while True:
            user_input = await loop.run_in_executor(None, input, "\nYou: ")

            if user_input.lower() in ['exit', 'quit']:
                print("Ending conversation...")
                break

            if user_input.lower() == 'clear':
                agent.clear_conversation_history()
                print("Conversation history cleaned.")
                continue

            print("\nAssistant: ", end="", flush=True)

            try:
                response = await agent.run(user_input)
                print(response)

            except Exception as e:
                print(f"\nError: {type(e).__name__}: {str(e)[:100]}")

                if "429" in str(e) or "Too Many Requests" in str(e):
                    print("Rate limited. Waiting 30 seconds before next request...")
                    await asyncio.sleep(30)

    except KeyboardInterrupt:
        print("\n\nConversation interrupted.")
    finally:
        if client and client.sessions:
            await client.close_all_sessions()

if __name__ == "__main__":
    try:
        asyncio.run(run_memory_chat())
    except KeyboardInterrupt:
        print("\n\nApplication terminated by user.")
    except Exception as e:
        print(f"\nFatal error: {type(e).__name__}: {e}")
        sys.exit(1)