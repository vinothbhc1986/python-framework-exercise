from unittest.mock import patch
from shop import get_price

#Using the with context manager  - option A
def test_get_price2():
    with patch('shop.call_api') as fake:
        fake.return_value = 42
        assert get_price() == 42

# recommended cleaner alternative  - option B
@patch('shop.call_api', return_value=42)
def test_get_price(mock_call_api):
    assert get_price() == 42


# Option B is generally considered the better and more idiomatic choice in pytest (and unittest.mock).
#
# Here is why:
#
# Cleaner syntax: By passing return_value=42 directly into the decorator, you avoid setting properties inside the block, keeping your test concise and readable.
#
# Scope and setup separation: Setting up the mock as an argument (mock_call_api) clearly separates your test setup from your assertions.
#
# However, Option A has its place too—it's useful if you only want to mock something for a portion of a larger test function rather than the entire function.