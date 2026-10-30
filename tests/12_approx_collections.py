import pytest

def test_vector_approx():
    coords = [0.1 + 0.2, 1.0 / 3.0]
    assert coords == pytest.approx([0.3, 0.333333], abs=1e-4)

test_vector_approx()
print('test_vector_approx: PASSED')

# 1e-4  ==>  0.0001