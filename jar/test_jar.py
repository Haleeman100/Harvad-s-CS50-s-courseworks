import pytest
from jar import Jar

@pytest.fixture
def check_all():
    return Jar()

# test to check deposit
def test_deposit(check_all):
    check_all.deposit(3)
    assert check_all.size == 3

def test_withdraw(check_all):
    check_all.deposit(3)
    check_all.withdraw(1)
    assert check_all.size == 2