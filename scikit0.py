from sklearn.model_selection import train_test_split
import pandas as pd
data = {
    "Size": [1000, 1200, 1500, 1800, 2000, 2200, 50000, 6000, 8000],
    "Rooms": [2, 2, 3, 3, 4, 4,8,10,12],
    "Price": [200000, 240000, 300000, 360000, 410000, 450000, 500000, 600000, 700000]
}

df = pd.DataFrame(data)

X = df[["Size", "Rooms"]]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

print(X_train.shape)
print(X_test.shape)

print(y_train.shape)
print(y_test.shape)
