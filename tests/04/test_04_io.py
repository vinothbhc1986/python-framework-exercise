import pytest

import pricing3
from cart1 import Cart
from receipt2 import write_receipt

@pytest.fixture
def loaded_cart():
    cart = Cart()
    cart.add("laptop", 999.00)
    cart.add("mouse", 25.00, quantity=2)
    return cart

def test_receipt_file(loaded_cart, tmp_path):
    path = write_receipt(loaded_cart, tmp_path / "receipt.txt")
    text = path.read_text(encoding="utf-8")
    assert "laptop" in text
    assert "TOTAL: 1049.00" in text

class FakeResponse:
   def json(self):
       return {"rates": {"USD": 1.10}}

def test_eur_to_usd(monkeypatch):
    def fake_get(url, params=None):
        return FakeResponse()

    monkeypatch.setattr("pricing3.httpx.get", fake_get)
    assert pricing3.eur_to_usd(100) == 110.00
