import pandas as pd
orders = pd.DataFrame({
    "order": [101, 102, 103, 104, 105],
    "customer_id": [1, 2, 1, 3, 5],
    "product": ["Coffee", "Book", "Headphones", "Tea", "Pen"],
})
customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4],
    "name": ["Sara", "Omar", "Lena", "Ali"],
    "city": ["Berlin", "Cairo", "Madrid", "Dubai"],
})
# 1. inner (the default): only the keys that are in BOTH tables
#adds the customer's name and city to every order
# print(orders.merge(customers, on="customer_id"))

# 2. left: every order (a missing name or city becomes NaN)
#every order stays; a missing name becomes NaN (not a number)
# print(orders.merge(customers, on="customer_id", how="left"))

# 3. right: every customer
# print(orders.merge(customers, on="customer_id", how="right"))
#every customer stays; a number column with NaN becomes decimals (101 becomes 101.0)

# 4. outer: everything from both tables
# print(orders.merge(customers, on="customer_id", how="outer"))

# 5. cross: every row with every row (no key)
sizes = pd.DataFrame({"size": ["S", "M", "L"]})
colors = pd.DataFrame({"color": ["Black", "White"]})
# print(sizes.merge(colors, how="cross"))

customers2 = customers.rename(columns={"customer_id": "id"})
# orders.merge(customers, on="customer_id") #gives KeyError: 'customer_id'
print(orders.merge(customers2, left_on="customer_id", right_on="id"))


