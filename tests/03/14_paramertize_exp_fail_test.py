import pytest

@pytest.mark.parametrize(
    "raw, want",
    [
        ("1", 1),
        (" 2 ", 2),
        pytest.param("x", None, marks=pytest.mark.xfail), #This applies an expected failure (xfail) mark exclusively to this specific parameter combination, rather than the entire test function.
    ],
    ids=["plain", "spaces", "junk"],
)
def test_parse(raw, want):
    assert int(raw) == want
