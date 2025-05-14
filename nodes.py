def validate_config_node(state):
    config = state["config"]
    context = state.get("rag_context", "")
    llm = state["llm"]

    prompt = f"""
You are a Cisco Nexus 9300 expert.

Knowledge base:
{context}

Analyze this config:
{config}

Return:
1. Risk level
2. Issues
3. Suggestions
4. Corrected CLI
"""

    result = llm.invoke([
        {"role": "system", "content": "You are a network AI validator for Cisco Nexus 9300."},
        {"role": "user", "content": prompt}
    ])

    state["analysis"] = result.content
    return state



def rag_node(state):
    from embed.embedder import get_embedder
    from langchain.vectorstores import Chroma

    retriever = Chroma(persist_directory="./chroma_index", embedding_function=get_embedder()).as_retriever()
    query = state["config"]
    results = retriever.get_relevant_documents(query)
    context = "\n\n".join([doc.page_content for doc in results[:3]])
    state["rag_context"] = context
    return state
