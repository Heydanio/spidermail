from fastapi.testclient import TestClient

from src.spidermail.api.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict():
    response = client.post(
        "/predict",
        json={"text": "Urgent: verify your account immediately using this link."}
    )

    assert response.status_code == 200
    data = response.json()

    assert "label" in data
    assert "phishing_score" in data
