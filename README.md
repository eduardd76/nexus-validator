

# Nexus 9300 AI Config Validator 🤖

> Validate Cisco Nexus 9300 configurations using AI, LangGraph, RAG, and local LLMs via Ollama.

---

## ✨ What it does
This tool analyzes Cisco Nexus 9300 configuration snippets and returns:
- Misconfigurations and inconsistencies
- Best practice recommendations
- CLI fix suggestions

All using:
- ⚡ Local LLM (like `mistral` or `phi3`) via [Ollama](https://ollama.com/)
- 📊 RAG: Cisco documentation ingested and embedded
- 🧬 LangGraph agent pipeline
- 🌐 Streamlit frontend for easy use

---

## 📁 Project Structure

```
nexus-validator/
├── app/
│   └── streamlit_ui.py       # Streamlit web interface
├── embed/
│   ├── index.py              # RAG embedding script
│   ├── loader.py             # Loads Cisco PDF/Markdown documents
│   └── embedder.py           # Embedding using sentence-transformers
├── docs/                     # Cisco docs and CVE notes (PDFs/Markdown)
├── llm_local.py              # Loads local Ollama model
├── graph_runner.py           # Builds LangGraph pipeline
├── netmiko_utils.py          # Pulls config from live Nexus devices
├── nodes.py                  # Graph steps: RAG + LLM validation
├── requirements.txt          # All required packages
└── .env                      # (Optional) for API keys if needed
```

---

## 🛠️ Components Explained

### `streamlit_ui.py`
- Renders a clean 2-tab UI
  - Paste config OR pull live from Nexus
  - Display validation result in Markdown

### `llm_local.py`
- Uses `ChatOllama` to connect to a local Ollama LLM server
- Default model: `phi3` (runs on CPU)

### `nodes.py`
- `rag_node`: queries the embedded vector DB (Cisco docs)
- `validate_config_node`: sends prompt + context to LLM

### `graph_runner.py`
- Constructs a LangGraph state machine with 3 steps:
  1. entry node
  2. RAG node
  3. LLM validation node

### `embed/index.py`
- Ingests PDF/Markdown files from `docs/`
- Splits and embeds using `sentence-transformers`
- Saves vector DB to `chroma_index/`

### `netmiko_utils.py`
- Uses `Netmiko` to connect to a Cisco Nexus switch and run `show running-config`

---

## 🧠 Running the app

### ✅ 1. Setup your Python venv and install dependencies:
```
python -m venv venv
.env\Scriptsctivate        # On Windows
pip install -r requirements.txt
```

### ✅ 2. Pull and run your Ollama model:
```
ollama pull phi3
set OLLAMA_USE_GPU=false
ollama run phi3
```

### ✅ 3. Build your RAG index:
```
python embed/index.py
```

### ✅ 4. Launch the Streamlit app:
```
streamlit run app/streamlit_ui.py
```

---

## 🚀 Models supported
- `mistral`
- `mixtral`
- `phi3` ← recommended for CPU
- `llama2`, `llama3`, etc.

---

## 🛡️ Security Notice
All inference is local. No configs are sent over the internet.

---

## 🌍 Credits
Built by Eduard Dulharu ❤️ with love, code, and networking headaches.

---

## 📄 License
MIT License
Feel free to fork, improve, and build your own AI-powered network tools!
