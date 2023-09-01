from langchain import VectorDBQA, OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from typing import Any
from langchain.vectorstores import Qdrant
from langchain.document_loaders import PyPDFLoader, TextLoader

class OpenAIQA:
    def __init__(
        self, 
        openai_api_key: str, 
        qdrant_url: str,
        qdrant_key: str,
        collection_name: str,
        data_path: str
    ):
        self.openai_api_key = openai_api_key
        self.qdrant_url = qdrant_url
        self.qdrant_key = qdrant_key
        self.collection_name = collection_name
        self.data_path = data_path
        self.vector_store = self.get_vector_store()
        self.qa = self.qa_model()

    def get_vector_store(self):

        embeddings = OpenAIEmbeddings(openai_api_key=self.openai_api_key)
        loader = TextLoader(self.data_path)
        pages = loader.load_and_split()

        qdrant = Qdrant.from_documents(
            pages,
            embeddings,
            url=self.qdrant_url,
            prefer_grpc=True,
            api_key=self.qdrant_key,
            collection_name=self.collection_name,
        )
        return qdrant
    
    def qa_model(self):
        llm = OpenAI(openai_api_key=self.openai_api_key)
        qa = VectorDBQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            vectorstore=self.vector_store,
            return_source_documents=False,
            verbose=True
        )
        return qa

    def run(self, question: str, top_k: int = 1) -> Any:
        return self.qa.run(query=question, top_k=top_k)
