import pytest

from season import Convert, DateToAge

@pytest.fixture
def convertion():
    return Convert()

@pytest.fixture
def age_converter():
    return DateToAge()

def test_valid_numbers(convertion):
    assert convertion.convert_number(3456) == "Three thousand,four hundred fifty six"
    
def test_invalid_number(convertion):
    assert convertion.convert_number(-9) == "Invalid"
    

    


