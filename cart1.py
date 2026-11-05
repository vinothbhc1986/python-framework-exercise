class CartError(Exception):
    pass

class Cart:
    def __init__(self):
        self.items = {}  # name -> (price, quantity)

    def add(self, name, price, quantity=1):
        if price < 0:
            raise CartError("price cannot be negative")
        if name in self.items:
            old_price, old_qty = self.items[name]
            self.items[name] = (price, old_qty + quantity)
        else:
            self.items[name] = (price, quantity)

    def remove(self, name):
        if name not in self.items:
            raise CartError(f"'{name}' not in cart")
        del self.items[name]

    def total(self):
        print('item', self.items.values())
        return sum(price * qty for price, qty in self.items.values())

    def apply_discount(self, percent):
        if not 0 <= percent <= 100:
            raise CartError("discount must be 0-100")
        return round(self.total() * (1 - percent / 100), 2)

    