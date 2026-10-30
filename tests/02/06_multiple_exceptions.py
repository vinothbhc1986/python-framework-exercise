import pytest

def safe_cast(val):
    if val is None:
        raise TypeError('val cannot be None')
    return val

def test_safe_cast_failures():
    with pytest.raises((ValueError,TypeError)):
        safe_cast(None)

test_safe_cast_failures()
print('test_safe_cast_failures(): Pass')