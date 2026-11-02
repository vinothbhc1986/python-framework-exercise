import pytest

def parse_int(text):
    return int(text)

# Test successful cases
@pytest.mark.parametrize("text, expected", [
    ("0", 0),
    ("12", 12),
    (" 12 ", 12),
], ids=["zero", "two digits", "spaces"])  #id argument is used to provide human-readable names for each test case
def test_parse_int_success(text, expected):
    assert parse_int(text) == expected

# Test expected error cases
@pytest.mark.parametrize("text", [
    "abc",
    "",
], ids=["letters", "empty"])
def test_parse_int_errors(text):
    with pytest.raises(ValueError):
        parse_int(text)

#python -m pytest -q 08_mark_parameterize.py
# The -q flag stands for quiet mode. When running pytest, this option reduces the amount of output displayed in your terminal.
# making it easier to see the status of your test suite at a glance without unnecessary clutter.