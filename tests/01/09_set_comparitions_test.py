def get_active_roles():
    return {'reader', 'editor', 'admin', 'admin'}

def test_roles_membership():
    roles = get_active_roles()
    assert 'admin' in roles
    assert len(roles) == 3

test_roles_membership()
print('test_roles_membership: PASSED')
