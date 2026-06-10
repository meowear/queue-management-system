import pytest
from unittest.mock import MagicMock, patch
from src.services.database import DatabaseService

@pytest.fixture
def mock_db_service():
    with patch("src.services.database.create_client") as mock_create:
        service = DatabaseService()
        service.supabase = MagicMock()
        yield service

def test_get_configuration(mock_db_service):
    mock_db_service.supabase.table().select().limit().execute.return_value.data = [
        {"id": "1", "entrances": 1, "exits": 1, "max_capacity": 50, "interaction_time": 5}
    ]
    config = mock_db_service.get_configuration()
    assert config["id"] == "1"
    assert config["entrances"] == 1

def test_join_queue(mock_db_service):
    mock_db_service.supabase.table().insert().execute.return_value.data = [
        {"id": "entry_1", "user_id": "user_1", "position": 1, "status": "waiting"}
    ]
    entry = mock_db_service.join_queue("user_1")
    assert entry["user_id"] == "user_1"
    assert entry["position"] == 1
