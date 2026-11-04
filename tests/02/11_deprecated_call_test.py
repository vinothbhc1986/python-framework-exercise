import warnings
import pytest

def legacy_api():
    warnings.warn('legacy api is obsolete', DeprecationWarning)
    return 'legacy_value'

def test_deprecated_invocation():
    with pytest.deprecated_call():
        result = legacy_api()
    assert result == 'legacy_value'

test_deprecated_invocation()
print('test_deprecated_invocation: pass')