import warnings
import pytest

def old_calculate():
    warnings.warn('use new calculate instead', DeprecationWarning)
    return 42

def test_old_calculate_warning():
    with pytest.warns(DeprecationWarning):
        res = old_calculate()
    assert res == 42

test_old_calculate_warning()
print('test_old_calculate_warning: Pass')