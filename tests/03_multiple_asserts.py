def get_user_status(age): 
    return {'adult': age >= 18, 'voting_eligible': age >= 18} 

def test_adult_status(): 
    status = get_user_status(20)
    assert status['adult'] is True 
    assert status['voting_eligible'] is True 

test_adult_status() 
print('test_adult_status: PASSED') 