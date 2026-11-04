# pytest is a popular Python framework used for automated testing.
#  It helps you check whether your Python code works correctly and catches bugs when you change your code.


from calculator import add

def test_add():
    assert add(2, 3) == 5