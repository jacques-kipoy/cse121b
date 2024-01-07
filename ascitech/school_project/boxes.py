import math

manufature= int(input("Enter the number of items: "))
per_box = int(input("Enter the number of items per box: "))

formula = manufature // per_box

if manufature // per_box == 0:
    print(f"For {manufature} items, packing {per_box} items in each box, you will need {formula}")
elif manufature // per_box != 0:

    print(f"For {manufature} packing {per_box} items in each box, you will need  {formula + 1} boxes")

# The math.ceil() function rounds a number up to the nearest integer that is greater than or equal to a number.
calculation = math.ceil(manufature/per_box)
print()
print(f"For {manufature} packing {per_box} items in each box, you will need  {calculation} boxes")

