from sys import path

import pytest
import tempfile, os



def run_pytest(code_str, args=None ):
    with tempfile.NamedTemporaryFile(mode="w", suffix="_test.py", delete=False) as f:
        f.write(code_str)
        path = f.name
    result = pytest.main([path, *(args or [])])
    os.unlink(path)
    return result

code = '''
def add(a,b):
    return a+b

def test_add():
    assert add(1,2) == 5
'''
exit_code = run_pytest(code, ['-v', '--no-header'])
print(exit_code)


# def run_pytest_named(code_str, file_name, args=None ):
#     temp_dir = tempfile.mkdtemp()
#     path = os.path.join(temp_dir, file_name)
#     with open(path, 'w') as f:
#         f.write(code_str)
#     result = pytest.main([path, *(args or [])])
#     return result
# helper_code = 'def test_named_ok():\n   assert 1 + 1 == 2\n'
# exit_code = run_pytest_named(helper_code, 'test_naming_demo.py', ['-v', '--no-header'])
# print(exit_code)

