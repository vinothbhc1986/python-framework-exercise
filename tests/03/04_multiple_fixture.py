import pytest

@pytest.fixture
def user_data():
    return {"name": "Alice"}

@pytest.fixture
def database_connection():
    # Setup logic for a mock database
    db = "connected"
    yield db
    # Teardown logic (e.g., closing connections)
    # db = "disconnected"

# Using both fixtures in a single test
def test_save_user(user_data, database_connection):
    # Add your test assertions and logic here
    assert database_connection == "connected"
    assert user_data["name"] == "Alice"