import pytest
import time

@pytest.mark.slow
def test_long_running_process():
    # Simulate a slow test
    time.sleep(5)
    print("long running process")
    assert True

def test_fast_process():
    # Simulate a fast test
    print("fast")
    assert True

#pytest -m slow .\tests\03\15_mark_slow_test.py
#pytest -m "not slow" .\tests\03\15_mark_slow_test.py