def get_user_record(user_id):
    return {'id': user_id, 'role': 'admin', 'verified': True}

def test_user_record():
    record = get_user_record(42)
    assert record['role'] == 'admin'
    assert record['verified'] is True

test_user_record()
print('test_user_record: PASSED')