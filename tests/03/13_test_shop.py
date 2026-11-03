from shop import charge_customer

def test_charge_mock(monkeypatch):
    # Correct: Patch where it is used
    monkeypatch.setattr("shop.charge", lambda: "mocked_response")

    result = charge_customer()
    assert result == "mocked_response"