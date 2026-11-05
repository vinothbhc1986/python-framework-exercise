import pytest

from cart1 import Cart,CartError

def test_empty_cart_total_size_is_zero():
   cart = Cart()
   assert cart.total() == 0

def test_add_single_item():
    cart = Cart()
    cart.add("apple", 1.50)
    assert cart.total() == 1.50

def test_add_with_quantity():
    cart = Cart()
    cart.add("apple", 1.5, quantity=4)
    assert cart.total() == 6.00

def test_negative_price_rejected():
    cart = Cart()
    with pytest.raises(CartError):
        cart.add("apple", -1.0)

def test_float_prices_approx():
    cart = Cart()
    cart.add("apple", 0.10)
    cart.add("banana", 0.20)
    assert cart.total() == pytest.approx(0.30)

@pytest.fixture()
def loaded_cart():
    cart = Cart()
    cart.add("laptop", 999.00)
    cart.add("mouse", 25.00, quantity=2)
    return cart

def test_total(loaded_cart):
    assert loaded_cart.total() == 1049.00

def test_remove(loaded_cart):
    loaded_cart.remove("mouse")
    assert loaded_cart.total() == 999.00

def test_remove_missing(loaded_cart):
    with pytest.raises(CartError, match="not in cart"):
        loaded_cart.remove("keyboard")

@pytest.mark.parametrize("percent, expected",[
    (0, 1049.00),
    (10, 944.10),
    (50, 524.50),
    (100, 0.0),
])
def test_discounts(loaded_cart, percent, expected):
    assert loaded_cart.apply_discount(percent) == expected

@pytest.mark.parametrize("bad_percent", [-5, 101, 999])
def test_invalid_discounts(loaded_cart, bad_percent):
    with pytest.raises(CartError):
        loaded_cart.apply_discount(bad_percent)
