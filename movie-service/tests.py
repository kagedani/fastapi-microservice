from fastapi.testclient import TestClient
from main import app
from app.config.config import Settings
from unittest.mock import patch
import os
import pytest


@pytest.fixture
def test_client():
    return TestClient(app)


@patch('main.get_settings')
def test_get_configs(mock_get_settings, test_client):

    mock_settings = {}

    if os.environ['env'] == 'local':
        mock_settings = {
            "app_name": "Lightweight Microservice",
            "profile": "local",
            "database_name": "movie_db_dev",
            "database_user": "movie_db_username",
            "database_host": "localhost"
        }
    elif os.environ['env'] == 'test':
        mock_settings = {
            "app_name": "Lightweight Microservice",
            "profile": "test",
            "database_name": "movie_db_dev",
            "database_user": "movie_db_username",
            "database_host": "movie_db"
        }

    mock_get_settings.return_value = mock_settings

    response = test_client.get("/api/v1/configs/")
    assert response.status_code == 200

    assert response.json() == mock_settings


def test_settings_model():
    settings = Settings(
        app_name="TestApp",
        profile="test",
        database_name="testdb",
        database_user="testuser",
        database_host="testhost"
    )

    assert settings.app_name == "TestApp"
    assert settings.profile == "test"
    assert settings.database_name == "testdb"
    assert settings.database_user == "testuser"
    assert settings.database_host == "testhost"
