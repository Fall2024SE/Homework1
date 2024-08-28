import homework1

def test_pass():
    assert homework1.binary_search([1,2,3,4,5], 0, 4, 3)

    
def test_fail():
    assert homework1.binary_search([1,2,3,4,5], 0, 4, 9) == False
