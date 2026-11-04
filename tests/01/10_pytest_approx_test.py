import pytest

def test_floating_sum():
    val = 0.1 + 0.2
    assert val == pytest.approx(0.3)

test_floating_sum()
print('test_floating_sum: PASSED')
