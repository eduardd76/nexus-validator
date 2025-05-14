import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from llm_local import load_llm
from graph_runner import build_graph
from netmiko_utils import get_live_config


st.set_page_config(page_title="Nexus 9300 AI Validator", layout="wide")
st.title("🧠 Nexus 9300 Config AI Validator")

@st.cache_resource
def load_agent(model_path):
    llm = load_llm(model_path)
    graph = build_graph(llm)
    return graph

model_path = st.text_input("🧠 Ollama model name (e.g. mistral, mixtral)", value="mistral")


tab1, tab2 = st.tabs(["📥 Manual Config Input", "📡 Pull from Live Device"])

with tab1:
    config_text = st.text_area("Paste your Nexus config snippet", height=300)

with tab2:
    col1, col2, col3 = st.columns(3)
    ip = col1.text_input("Device IP")
    username = col2.text_input("Username")
    password = col3.text_input("Password", type="password")

    if st.button("🔄 Pull Live Config"):
        config_text = get_live_config(ip, username, password)
        st.success("✅ Config pulled successfully")
        st.text_area("Live Config", config_text, height=300)

if st.button("✅ Validate Configuration") and config_text.strip():
    st.info("Analyzing config with AI...")
    graph = load_agent(model_path)
    state = {"config": config_text, "llm": load_llm(model_path)}
    final = graph.invoke(state)
    st.subheader("📊 Validation Result")
    st.markdown(final["analysis"])
