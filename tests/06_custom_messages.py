def calculate_tax(amount):
    return amount * 0.15

def test_tax_calculation():
    tax = calculate_tax(100.0)
    assert tax == 14.0, 'Tax should equal 15 percent of total'

test_tax_calculation()
print('test_tax_calculation: PASSED')
