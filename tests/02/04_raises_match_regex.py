import pytest

def parse_user_id(val):
    if not isinstance(val, int):
        raise TypeError('User ID must be an integer')
    return val

def test_invalid_type_message():
    with pytest.raises(
        TypeError, match='must be an integer'
    ):
        parse_user_id('abc')

test_invalid_type_message()
print('test_invalid_type_message: PASS')
