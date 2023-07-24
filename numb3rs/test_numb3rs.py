import pytest
from numb3rs import validate

def test_valid_ipv4_address():
    assert validate("255.255.255.255") is True
    assert validate("23.1.0.4") is True
    assert validate("87.8.9.0") is True
    assert validate("222.243.222.200") is True

def test_invalid_ipv4_address():
    assert validate("000.000.000.800") is False
    assert validate("265.255.244.233") is False
    assert validate("26.34.89") is False
    assert validate("34.0.00.7.9") is False

if __name__ == "__main__":
    pytest.main()
