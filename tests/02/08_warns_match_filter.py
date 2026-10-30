import warnings
import pytest

def format_data():
    warnings.warn('format data is deprecated in v2', UserWarning)
    return True

def test_format_data_warning():
    with pytest.warns(UserWarning, match='in v2'):
        ok = format_data()
    assert ok is True

test_format_data_warning()
print('test_format_data_warning: Pass')