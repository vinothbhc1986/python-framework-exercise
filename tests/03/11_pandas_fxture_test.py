# scope: (function - default), module, session
# name: optional
# Can also place these in conftest.py!

import pandas as pd
import pytest

from panda1 import show_top_row, show_bottom_row

@pytest.fixture(scope="module", name="dataframe")
def my_dataframe_fixture():
    return pd.read_csv("data.csv")

def test_show_top_row(dataframe):
    assert show_top_row(dataframe).equals(dataframe.iloc[0])
    print("ppp")

def test_show_bottom_row(dataframe):
    assert show_bottom_row(dataframe).equals(dataframe.iloc[-1])