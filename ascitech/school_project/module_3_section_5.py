# # Sorting list 
# my_list = [8,10,6,2,4]  # List to start
# swapped = True # We need this to enter the while loop   

# while swapped:
#     swapped = False  # no swap sor far
#     for i in range(len(my_list)-1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True # a swap occurred
#             my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

# print(my_list)
""""""""""""""""""""""""""""""""""""""""""""""""""""""
# # 5.3 The bubble sort – interactive version
# my_list = []
# swapped = True
# num = int(input("How many elements do you want to sort: "))

# for i in range(num):
#     val = float(input("Enter a list element: "))
#     my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nSorted:")
# print(my_list)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Python, however, has its own sorting mechanisms. No one needs to write their own sorts, as there is a sufficient number of ready-to-use tools.
# We explained this sorting system to you because it's important to learn how to process a list's contents, and to show you how real sorting may work.

# You can use the sort() method to sort elements of a list, e.g.:
this_list = [32,54,77,4,88,9,1]
this_list.sort()        # the method named sort, can be used to sort a list 
print("Sorted list      ",this_list)

#  There is also a list method called reverse(), which you can use to reverse the list, e.g.:
this_list.reverse()  # It is reversed in a sorted way
print("The reversed list",this_list)