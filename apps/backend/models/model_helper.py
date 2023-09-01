from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Qdrant
from langchain.document_loaders import PyPDFLoader

class SimilaritySearch:
    def __init__(self, 
                 data_path,
                 chunk_size,
                 chunk_overlap,
                 openai_api_key,
                 qdrant_url,
                 qdrant_key,
                 qdrant_collection_name):
        
        self.data_path = data_path
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.openai_api_key = openai_api_key
        self.qdrant_url = qdrant_url
        self.qdrant_key = qdrant_key
        self.qdrant_collection_name = qdrant_collection_name
        self.qdrant = None
        self._initialize()

    def _initialize(self):
        loader = PyPDFLoader(self.data_path)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        docs = text_splitter.split_documents(documents)

        embeddings = OpenAIEmbeddings(openai_api_key=self.openai_api_key)

        self.qdrant = Qdrant.from_documents(
            docs,
            embeddings,
            url=self.qdrant_url,
            prefer_grpc=True,
            api_key=self.qdrant_key,
            collection_name=self.qdrant_collection_name,
        )

    def search(self, query):
        if self.qdrant is not None:
            return self.qdrant.similarity_search_with_score(query)
        else:
            return None