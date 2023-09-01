from fastapi.testclient import TestClient
from main import app  # replace `your_app` with the actual name of your app module

client = TestClient(app)

def test_read_index():
    response = client.get("/")
    assert response.status_code == 200
    content_str = " ".join(response.content.decode('utf-8').split())
    assert "<html lang=\"en\">" in content_str

def test_read_favicon():
    response = client.get("/favicon.ico")
    assert response.status_code == 200
    assert response.headers["content-type"] in ["image/x-icon", "image/vnd.microsoft.icon"]