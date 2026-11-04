import pytest

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('Division by zero is forbidden')
    return a / b

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

test_zero_division()
print('test_zero_division: PASS')