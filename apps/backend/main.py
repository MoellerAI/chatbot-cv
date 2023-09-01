from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from config import settings
import os
from helpers.model_helper import OpenAIQA

current_directory = os.path.dirname(os.path.realpath(__file__))
root_directory = os.path.abspath(os.path.join(current_directory, os.pardir, os.pardir))

data_path = os.path.join(root_directory, "data", "CV.txt")
print(data_path)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def index():
    return FileResponse("static/index.html")

@app.get("/favicon.ico")
async def favicon():
    return FileResponse("static/favicon.ico")

@app.get("/test")
async def test():
    return {"message": settings.QDRANT_KEY}

@app.get("/similarity_search")
async def similarity_search_endpoint(query: str):
    qa = OpenAIQA(
        openai_api_key=settings.OPENAI_API_KEY,
        qdrant_url=settings.QDRANT_URL,
        qdrant_key=settings.QDRANT_KEY,
        collection_name=settings.QDRANT_COLLECTION_NAME,
        data_path=data_path
    )
    response = qa.run(question=query, top_k=1)
    if response:
        return JSONResponse(content={"response": response})
    else:
        return JSONResponse(content={"error": "An error occurred while performing the similarity search"}, status_code=500)