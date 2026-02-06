from langchain_core.messages import SystemMessage
from llm.client import get_llm
from tools.tools_registry import tools

llm = get_llm()
llm_with_tools = llm.bind_tools(tools)

def planner_agent(state):
    messages = [
        SystemMessage(
            content=(
                "You are a Planner Agent.\n\n"
        "Tool selection rules:\n"
        "- If the user asks about weather, temperature, forecast, or climate, "
        "you MUST use the `get_weather` tool.\n"
        "- If the user asks about stock price, share price, market price, or ticker symbols, "
        "you MUST use the `get_stock_price` tool.\n"
        "- Do NOT use web search for stock prices or weather data if a dedicated API exists.\n"
        "- Use DuckDuckGo search ONLY for general informational or descriptive queries.\n"
        "- If no tool is required, answer directly using the LLM.\n\n"
        "Always choose the MOST SPECIFIC tool available."
            )
        )
    ] + state["messages"]

    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}
