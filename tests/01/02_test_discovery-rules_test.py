def multiply(a, b):
    return a * b

def test_multiply_positive():
    result = multiply(4, 5)
    assert result == 20

test_multiply_positive()
print('test_multiply_positive: PASSED')