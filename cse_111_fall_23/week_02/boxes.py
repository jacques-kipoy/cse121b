import math
# CSE 111 Class
# Week 02 L02 Checkpoint Calling function
# Jacques Kipoy
# Professor : David Christofferson
item_num = int(input("\nenter the number of items: "))
item_per_box = int(input("\nEnter the number of items per box: "))
num_of_box = item_num / item_per_box
c_ = math.ceil(num_of_box)
print(f"\nFor {item_num} ietms, packing {item_per_box} items in each box, you will need {c_} boxes.")
