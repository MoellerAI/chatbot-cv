from pydantic_settings import BaseSettings
import os

from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    QDRANT_KEY: str = os.getenv("QDRANT_KEY")
    QDRANT_URL: str = os.getenv("QDRANT_URL")
    QDRANT_COLLECTION_NAME: str = os.getenv("QDRANT_COLLECTION_NAME")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

# global instance
settings = Settings()