from names import make_full_name,\
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name("John", "Doe") == "Doe; John"


def test_extract_family_name():
    assert extract_family_name("Kerr", "Ethan") == "Kerr"


def test_extract_given_name():
    assert extract_given_name("Kipoy", "Jacques") == "Jacques"


pytest.main(["-v", "--tb=line", "-rN", __file__])
