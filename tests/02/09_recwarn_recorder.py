import warnings
import pytest

def multi_warning_op():
    warnings.warn('step 1 notice', UserWarning)
    warnings.warn('step 2 notice', UserWarning)

def test_warning_warning(recwarn):
    multi_warning_op()
    assert len(recwarn) == 2

rec = pytest.WarningsRecorder()
with rec:
    test_warning_warning(rec)
print('test_warning_warning: Pass')