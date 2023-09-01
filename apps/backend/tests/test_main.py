from pathlib import Path

from fastapi.testclient import TestClient
from main import app  # Modify the import based on where your app is defined

client = TestClient(app)

# Setup some basic data
base_dir = Path("static").resolve()

def test_read_root():
    """Test that the root path returns index.html"""
    response = client.get("/")
    assert response.status_code == 200
    # Check that the content of index.html is returned
    assert b"<html>" in response.content  # this checks for an opening <html> tag. Adjust this based on the actual content of your index.html

def test_catch_all():
    """Test that all paths return index.html"""
    paths_to_test = [
        "/some/random/path",
        "/another/test/path",
        "/just/a/test",
    ]
    
    for path in paths_to_test:
        response = client.get(path)
        assert response.status_code == 200
        # Check that the content of index.html is returned
        assert b"<html>" in response.content 
