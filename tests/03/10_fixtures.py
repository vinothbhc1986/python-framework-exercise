import pytest

from main1 import find_average, find_biggest, find_smallest

# @pytest.fixture
# def numbers():
#     return [1, 2, 3, 4, 5]
#
# @pytest.fixture(name="some_numbers")
# def my_numbers():
#     return [1, 2, 3, 4, 5]

def test_find_average(numbers):
    assert find_average(numbers) == 3.0

def test_find_biggest(numbers):
    assert find_biggest(numbers) == 5

def test_find_smallest(some_numbers):
    assert find_smallest(some_numbers) == 1