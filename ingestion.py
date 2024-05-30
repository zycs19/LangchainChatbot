import os
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


def ingest_docs()->None:
    loader = ReadTheDocsLoader(path="/Users/ying/Projects/LangChainProjects/document-helper/langchain-docs/api.python.langchain.com/en/latest")
    raw_document = loader.load()
    print(f"loaded{len(raw_document)}documents")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100, separators=["\n\n", "\n", " ", ""])
    documents = text_splitter.split_documents(documents=raw_document)
    print(f"Splitted into {len(documents)} chunks")

    for doc in documents:
        old_path = doc.metadata["source"]
        new_url = old_path.replace("/Users/ying/Projects/LangChainProjects/document-helper/langchain-docs", "https:/")
        doc.metadata.update({"source": new_url})

    print(f"Going to insert {len(documents)} to Pinecone")
    PineconeVectorStore.from_documents(documents=documents, embedding=embeddings, index_name="langchain-doc-index")
    print("******* Added to Pinecone vectorstore vectores")
if __name__ == '__main__':
    ingest_docs()
