import pytest
import sys


def process_data(data):
    return data.upper()

# The fixture handles the 'Arrange' part of the test
@pytest.fixture
def sample_input():
    return "hello world"

# The test function uses the AAA pattern
@pytest.mark.skipif(sys.platform == "win32", reason="skipping this test")
def test_process_data(sample_input):
    # Arrange: This is handled by the fixture 'sample_input'

    # Act: Call the function being tested
    result = process_data(sample_input)

    # Assert: Verify the output matches expectations
    assert result == "HELLO WORLD"