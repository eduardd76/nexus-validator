
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
def load_docs():
    pdf_loader = PyPDFLoader("docs/nexus_9300_config_guide.pdf")
    

    pdf_docs = pdf_loader.load()
    

    all_docs = pdf_docs 

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=64
    )
    return splitter.split_documents(all_docs)
