import pytest

@pytest.mark.filterwarnings('error::DeprecationWarning')
def test_strict_deprication():
    state = {'safe': True}
    assert state['safe'] is True

test_strict_deprication()
print('test_strict_deprication: pass')
