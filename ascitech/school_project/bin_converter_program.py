from multiprocessing.spawn import import_main_path


import math 

print()

my_binary_number = int(input("Enter a number "))

my_binary_second_number = int(input("Enter a number "))
my_binary_third_number = int(input("Enter a number "))
my_binary_fourth_number = int(input("Enter a number "))

new_num = bin(my_binary_number)
remove_the_0b_first = new_num[2:]
new = int(remove_the_0b_first)

convert_bin__second = bin(my_binary_second_number)   #convert into binary number
remove_second = convert_bin__second[2:]      # remove the 0b

convert_bin_third = bin(my_binary_third_number)     #convert into binary number
remove_third = convert_bin_third[2:]    # remove the 0b

convert_bin_fourth = bin(my_binary_fourth_number)     #convert into binary numbe
remove_fourth = convert_bin_fourth[2:]      # remove the 0b

print(f"\n\n{remove_the_0b_first} . {remove_second} . {remove_third} . {remove_fourth}\n\n")


#print(remove_the_0b_first)



#print(type(remove_the_0b_first))
#print(type(new))








#"""""""""""""""""""""""
#a= bin(2)
#x= a[2:]     # Start at the position two
#format(2, 'b') another example 
#print(x)
#""""""""""""""""""""""""#
