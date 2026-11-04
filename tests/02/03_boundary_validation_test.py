import pytest

def set_percentage(pct):
    if pct < 0 or pct > 100:
        raise ValueError('Percentage out of range')
    return pct

def test_boundary_limits():
    with pytest.raises(ValueError):
        set_percentage(105)

test_boundary_limits()
print('test_boundary_limits: PASS')