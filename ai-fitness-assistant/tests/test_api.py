import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database.mongodb import db_provider
from unittest.mock import patch

client = TestClient(app)

# We use mock DB for the tests to avoid requiring real MongoDB
@pytest.fixture(autouse=True)
def mock_db():
    with patch('app.database.mongodb.DatabaseProvider.get_collection') as mock_col:
        mock_col.return_value.insert_one.return_value.inserted_id = "test_id_123"
        yield mock_col

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_diet_generate():
    payload = {
        "weight": 80,
        "height": 180,
        "goal": "fat_loss"
    }
    response = client.post("/diet/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["goal"] == "fat_loss"
    assert "calories" in data

@patch('ai_models.habit_prediction.predictor.predict_skip_probability')
def test_habit_predict(mock_predict):
    mock_predict.return_value = {
        "skip_probability": 0.8,
        "risk": "high",
        "recommendation": "Mock test response"
    }
    
    payload = {
        "sleep_hours": 4.0,
        "stress_level": 9,
        "previous_workout": 0,
        "hydration": 3,
        "consistency": 20
    }
    
    response = client.post("/habit/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["risk"] == "high"
