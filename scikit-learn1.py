import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "Size": [1000, 1200, 1500, 1800, 2000, 2200],
    "Rooms": [2, 2, 3, 3, 4, 4],
    "Price": [200000, 240000, 300000, 360000, 410000, 450000]
}

df = pd.DataFrame(data)

X = df[["Size", "Rooms"]]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Your dataset contains 6 rows.
# test_size=0.2 means 20% of the data is used for testing.
# The remaining 80% is used for training.

# Here, random_state=42 tells Python to use a fixed random seed when splitting your dataset into training and testing data.
# This means that every time you run the code with the same data and settings, you get the same train/test split.
# The number 42 is arbitrary. You could use 10, 100, or 7 instead.

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Training rows:", len(X_train))


print("Test houses:")
print(X_test)

print("Actual prices:")
print(y_test)

print("Predicted prices:")
print(predictions)
