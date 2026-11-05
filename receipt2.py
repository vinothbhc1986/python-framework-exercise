def write_receipt(cart, path):
    lines = ["RECEIPT", "-" *24] # RECEIPT -------------
    for name, (price, qty) in cart.items.items():
        lines.append(f"{name:<12} {qty} x {price:.2f}") # Laptop    2 x 999
    lines.append("-" * 24)  # ------------------
    lines.append(f"TOTAL: {cart.total():.2f}") # TOTAL 1049
    path.write_text("\n".join(lines), encoding="utf-8")
    print("lines ",lines)
    return path

# If name is shorter than 12 characters, Python pads it with spaces on the right so that everything lines up neatly in columns.
#
# If name = "Apple", {name:<12} becomes "Apple       " (5 characters + 7 spaces = 12 total width).
#
# If name = "Banana Bread", {name:<12} stays "Banana Bread" (exactly 12 characters).