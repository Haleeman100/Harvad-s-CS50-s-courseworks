import pytest
from jar import Jar

@pytest.fixture
def check_all():
    return Jar()

# test to check deposit
def test_deposit(check_all):
    check_all.deposit(3)
    assert check_all.size == 3
    
def test_invalid_deposit(check_all):
    check_all.deposit = 5
    with pytest.raises(ValueError):
        Jar(check_all) == 3
        
def test_invalid_withdraw(check_all):
    check_all.deposit == 4
    with pytest.raises(ValueError):
        check_all.withdraw(5)

def test_withdraw(check_all):
    check_all.deposit(3)
    check_all.withdraw(1)
    assert check_all.size == 2
    
def test_valid_str(check_all):
    check_all.deposit(3)
    assert str(check_all) == "🍪🍪🍪"
    
def test_capacity(check_all):
    check_all == Jar(11)
    check_all.capacity

def test_size(check_all):
    check_all.deposit(2)
    assert check_all.size == 2