def get_default_config():
    return None

def test_default_config_none():
    config = get_default_config()
    assert config is None

test_default_config_none()
print('test_default_config_none: PASSED')