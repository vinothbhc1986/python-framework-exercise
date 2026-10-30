def calculate_sum(a, b): 
    return a + b 

def test_sum_integers(): 
    total = calculate_sum(10, 20) 
    assert total == 40

test_sum_integers() 
print('test_sum_integers: PASSED') 