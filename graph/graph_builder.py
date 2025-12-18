from langgraph.graph import StateGraph
from graph.state import GraphState
from graph.nodes import input_node, reasoning_node, final_node

def build_graph():
    builder = StateGraph(GraphState)

    builder.add_node("input", input_node)
    builder.add_node("reasoning", reasoning_node)
    builder.add_node("final", final_node)

    builder.set_entry_point("input")
    builder.add_edge("input", "reasoning")
    builder.add_edge("reasoning", "final")

    return builder.compile()