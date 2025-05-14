from loader import load_docs
from embedder import get_embedder
from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader

def build_vector_db():
    docs = load_docs()
    embedder = get_embedder()
    db = Chroma.from_documents(
        documents=docs,
        embedding=embedder,
        persist_directory="./chroma_index"
    )
    db.persist()
    print("✅ Vector DB created!")

if __name__ == "__main__":
    build_vector_db()
