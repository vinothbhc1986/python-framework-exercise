"""Some Pandas code."""

import pandas as pd

def show_top_row(data: pd.DataFrame):
    return data.iloc[0]

def show_bottom_row(data: pd.DataFrame):
    return data.iloc[-1]

df = pd.read_csv("data.csv")

top_row = show_top_row(df)
print('top row \n',top_row)

bottom_row = show_bottom_row(df)
print('bottom row \n',bottom_row)