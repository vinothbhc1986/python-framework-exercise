import pytest

# Fixture for setup
@pytest.fixture
def db_session():
    return "Database Connected"

# Parametrizing the test function
@pytest.mark.parametrize("input_val, expected", [
    ("A", "A-processed"),
    ("B", "B-processed"),
])
def test_data_processing(db_session, input_val, expected):
    # The test uses both the fixture and the parametrize values
    assert f"{input_val}-processed" == expected
    print('t ',input_val)
    assert db_session == "Database Connected"