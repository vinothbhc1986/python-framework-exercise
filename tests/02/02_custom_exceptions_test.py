import pytest

class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError('Overdraft limit reached')
    return balance - amount

def test_overdraft():
    with pytest.raises(InsufficientFundsError):
        withdraw(50,100)

test_overdraft()
print('test_overdraft: PASS')