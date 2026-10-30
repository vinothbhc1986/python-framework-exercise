import pytest

@pytest.fixture
def db_connection():
    # Setup a database connection
    db = "Connected"
    yield db
    # Teardown connection (cleanup code can go here)

@pytest.fixture
def user_data(db_connection):
    # This fixture uses the 'db_connection' fixture
    return f"User data from {db_connection}"

def test_feature(user_data):
    assert user_data == "User data from Connected"