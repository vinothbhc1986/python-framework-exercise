import pytest

def check_port(port):
    if port < 1024:
        raise ValueError(f'Privileged ports: {port}')
    return port

def test_privileged_port():
    with pytest.raises(ValueError) as exc_info:
        check_port(80)
    assert '80' in str(exc_info.value)
    print('type ',str(exc_info.type), 'type')
    print('value ', str(exc_info.value), 'value')

test_privileged_port()
print('test_privileged_port: PASS')
