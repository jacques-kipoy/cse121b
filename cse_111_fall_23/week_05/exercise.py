

# def test_min():
#     assert min(7,-3, 0, 2) == -3


# test_min()

# Example 4

# The variables e and f can be any floating-
# point numbers from any calculation.
e = 7.135
f = 7.128

if abs(e - f) < 0.01:
    print(f"{e} and {f} are close enough so")
    print("we'll consider them to be equal.")
else:
    print(f"{e} and {f} are not close and")
    print("therefor not equal.")


def test_function():
    assert actual_value == approx(expected_value)