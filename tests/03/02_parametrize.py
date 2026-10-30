import pytest

def square(n):
    return n * n

# Using parametrize to test multiple inputs
@pytest.mark.parametrize(
    "input_val, expected",
    [
        (2, 4),   # Case 1
        (3, 9),   # Case 2
        (5, 25),  # Case 3
        (6, 36)
    ],
)
def test_square(input_val, expected):
    assert square(input_val) == expected