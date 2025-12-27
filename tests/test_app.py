from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200

def test_health():
    r = client.get("/health")
    # I CI finns ingen Postgres uppe, så vi testar bara att endpointen svarar
    assert r.status_code == 200
