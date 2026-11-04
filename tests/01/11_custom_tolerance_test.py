import pytest

def test_tolerance_levels():
    measurement = 100.05
    assert measurement == pytest.approx(100.0, abs=0.1)

test_tolerance_levels()
print('test_tolerance_levels: PASSED')

# - 100.05 — actual measurement.
# - 100.0 — expected value.
# - abs=0.1 — allows a difference of up to 0.1.
# The allowed range is 99.9 to 100.1.
#
# Since 100.05 is within this range, the assertion passes.