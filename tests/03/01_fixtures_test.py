import pytest

# Define the fixture to set up resources
@pytest.fixture
def sample_data():
    # Setup: Prepare your data or connection
    data = {"user": "Alice", "id": 1}
    yield data

    # Teardown: Cleanup happens here after the test
    print("\nCleaning up resources...")


# Use the fixture by passing it as an argument
def test_user_id(sample_data):
    # Act and Assert
    assert sample_data["id"] == 1