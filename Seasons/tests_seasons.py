import pytest

from season import Convert, DateToAge

@pytest.fixture
def convertion():
    return Convert()

@pytest.fixture
def age_converter():
    return DateToAge()

def test_valid_numbers(convertion):
    assert convertion.convert_number(3456) == "Three thousand, four hundred fifty-six"
    
def test_invalid_number(convertion):
    assert convertion.convert_number(-9) == "Invalid number"

def test_convert_date_to_age(age_converter):
    date = "2000-11-16"
    expected_age_in_minutes = 12052800 
    assert age_converter.convert_date_to_age(date) == expected_age_in_minutes

def test_convert_age_to_sentence(age_converter):
    date = "2000-11-16"
    expected_age_words = "Twelve million, fifty-two thousand, eight hundred"
    assert age_converter.convert_age_to_number(date) == expected_age_words
    
def test_invalid_date_format(age_converter):
    invalid_date = "2021/12/01"  # Incorrect format
    with pytest.raises(SystemExit):
        age_converter.convert_age_to_number(invalid_date)
    

    


