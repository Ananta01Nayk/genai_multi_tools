from llm.client import get_llm
from langchain_core.messages import SystemMessage

llm = get_llm()

def verifier_agent(state):
    messages = [
        SystemMessage(
            content=(
                "You are a Verifier Agent. "
                "Validate tool outputs and generate a clear, user-friendly final response. "
                "If data is missing, explain gracefully."
            )
        )
    ] + state["messages"]

    response = llm.invoke(messages)
    return {"messages": [response]}
