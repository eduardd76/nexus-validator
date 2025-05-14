from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langchain_core.runnables import Runnable
from nodes import validate_config_node, rag_node

# Define schema
def build_graph(llm) -> Runnable:
    workflow = StateGraph(state_schema=dict)

    def entry_node(state: dict):
        return state

    workflow.add_node("entry", entry_node)
    workflow.add_node("rag", rag_node)
    workflow.add_node("validate", validate_config_node)

    workflow.set_entry_point("entry")
    workflow.add_edge("entry", "rag")
    workflow.add_edge("rag", "validate")
    workflow.set_finish_point("validate")

    return workflow.compile()
