"""Confest"""
import pytest

@pytest.fixture
def database_connection():
    db = "Connected to Database"
    yield db  # Provide the fixture to the test
    print("\nClosing database connection...")

@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5]

@pytest.fixture(name="some_numbers")
def my_numbers():
    return [1, 2, 3, 4, 5]

