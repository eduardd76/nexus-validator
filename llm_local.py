
from langchain_community.chat_models import ChatOllama

def load_llm(model_name="phi3"):
    return ChatOllama(base_url="http://localhost:11434", model=model_name)
