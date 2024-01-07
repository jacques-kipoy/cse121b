# my_list = []
# for i in range(5):
#     my_list.insert(0, i+1)
# print(my_list)
""""""""""""""""""""""""""""""""""""
# Computing the sum of all value in a list
# my_second = [4,6,23,7,5]
# total = 0
# for i in range(len(my_second)):
#     total += my_second[i]
# print(total)
""""""""""""""""""""""""""""""""""""
# my_list = [10,5,7,3,8]
# total = 0
# for i in my_list:
#     total += i
# print(total)
""""""""""""""""""""""""""""""""""""
# Rearranging the element of a list, doing like this
# is not a good practice
# variable_1 = 1
# variable_2 = 2

# variable_2 = variable_1 
# variable_1 = variable_2
# print(variable_1)
# print(variable_2)
""""""""""""""""""""""""""""""""""""
# We need a third variable This is how you can do it:
# Swapping two variables values 
# variable_1 = 1
# variable_2 = 2

# auxiliary = variable_1
# variable_1 = variable_2
# variable_2 = auxiliary
# print(variable_1)
# print(variable_2)
""""""""""""""""""""""""""""""""""""""""""
# Swapping numbers 
# x = 5
# y = 4
# z = x
# x = y
# y = z
# print("x:",x,"y:", y)
""""""""""""""""""""""""""""""""""""""""""
# # Python offers a more convenient way of doing the swap – take a look:
# var_1 = 3
# var_2 = 4
# var_1 , var_2 = var_2, var_1
# print(var_1)
# print(var_2)

# Now you can easily swap the list's elements to reverse their order:
# my_list = [10,1,8,3,5]
# print("Previous list", my_list)
# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]
# print("Actual list", my_list)
""""""""""""""""""""""""""""""""""""""
# Will it still be acceptable with a list containing 100 elements? No, it won't.
# Can you use the for loop to do the same thing automatically, irrespective of the list's length? Yes, you can.
# n_list = [2,5,7,0,8,11,3,5,33,5,3,44,]
# length = len(n_list)
# for i in range(length// 2):
#     n_list[i], n_list[length -i -1] = n_list[length -i -1], n_list[i]
# print(n_list)
""""""""""""""""""""""""""""""""""""""
# # Step 1  create an empty list named beatles
# beatles = []
# print("Step 1:",beatles)
# #Step 2 use the append() method to add the following members of the band to the list
# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("Georges Harrison")
# print("Step 2:", beatles)
# #step 3 use the for loop and the append() method to prompt the user to add the following members of the band to the list
# for members in range(2):
#     beatles.append(input("New band members: "))
# print("Step 3:", beatles)
# #Step 4 use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
# del beatles[-1]
# del beatles[-1]
# print("Step 4:", beatles)
# #Step 5 use the insert() method to add Ringo Starr to the beginning of the list.
# beatles.insert(0, "RingoStarr")
# print("Step:", beatles)
# print("The Fab:", len(beatles))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
color_list = ["green", "purple", "white", "orange", "blue"]
for color in color_list:
    print(color, end=" ")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
hat_list[2] = int(input("Enter an integer number: "))


# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]
# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))
print(hat_list)



