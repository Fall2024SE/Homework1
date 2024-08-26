import homework1

def test_pass():
    assert homework1.binary_search([1,2,3,4,5], 0, 4, 3)

    
Commenting for test badge
def test_fail():
    assert homework1.binary_search([1,2,3,4,5], 0, 10, 3)
