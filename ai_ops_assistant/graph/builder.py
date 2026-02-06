from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from graph.state import ChatState
from agents.planner import planner_agent
from agents.verifier import verifier_agent
from tools.tools_registry import tools

def build_graph():
    graph = StateGraph(ChatState)

    graph.add_node("planner", planner_agent)
    graph.add_node("tools", ToolNode(tools))   # 👈 NAME MUST BE "tools"
    graph.add_node("verifier", verifier_agent)

    graph.add_edge(START, "planner")
    graph.add_conditional_edges("planner", tools_condition)
    graph.add_edge("tools", "verifier")
    graph.add_edge("verifier", END)

    return graph.compile()
