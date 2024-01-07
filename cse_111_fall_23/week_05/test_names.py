from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """This function will test if the value returned
     from make_full_name function """
    assert make_full_name("john", "doe") == ("doe ;john")





pytest.main(["-v", "--tb=line", "-rN", __file__])