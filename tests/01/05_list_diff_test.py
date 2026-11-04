def get_fruits():
    return ['apple', 'banana', 'cherry']

def test_fruit_inventory():
    fruits = get_fruits()
    assert 'apple' in fruits
    assert len(fruits) == 3

test_fruit_inventory()
print('test_fruit_inventory: PASSED')
