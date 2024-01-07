# import time
# This is an example of an infinite loop
#while True:
    #print("I'm stuck inside the loop!")  # Control + C will cause a KeyboardInterrupt exception
    # exit()
""""""""""""""""""""""""""""""""""""""""""
# Program to find the Lagest number 
# largest_num = -999999999
# number = int(input("Please Enter a number or type -1 to stop "))
# while number != -1:
#     if number > largest_num:
#         largest_num = number
#     number = int(input("Please Enter a number or type -1 to stop "))


# print("The largest number is ", largest_num)
""""""""""""""""""""""""""""""""""""""""""

# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.
# odd_numeber = 0
# even_number = 0
# num = int(input("Enter a number or type 0 to stop the program "))
# while num  != 0: # or while num:
#     if num % 2 == 1:  # or if num % 2:
#         odd_numeber += 1
#     else:
#         even_number += 1
#     num = int(input("Enter a number or type 0 to stop the program "))

# print("Odd number count:", odd_numeber)
# print("Even number count:", even_number)
""""""""""""""""""""""""""""""""""""""""""

# counter= 50
# while counter != 0:
#     print("Inside loop ", counter)
#     counter -= 1
# print("Outside loop", counter)

""""""""""""""""""""""""""""""""""""""""""

#Secret number Game, Guess the number 
# secret_number = 777
# number_try = int(input("Guess the number "))
# while number_try != secret_number:
#     print("haha You are stuck inside my loop")
#     number_try = int(input("Enter a number "))
# print("Well done muggle!, you are free")

""""""""""""""""""""""""""""""""""""""""""

# # The for loop examples 
# for i in range(10):
#     print("The value of i is currently", i)

# for i in range(2,8):
#     print("The value of i is now", i)

# for i in range(2,8,3): # #The third argument is an increment , as you can see the default increment is 1
#     print("The actual value of i is", i)
""""""""""""""""""""""""""""""""""""""""""

# power = 1
# for expo in range(16):
#     print("2 to the power of", expo, "equals", power)
#     power *= 2 
""""""""""""""""""""""""""""""""""""""""""
# # Your task is very simple here: write a program that uses a
# #  for loop to "count mississippily" to five. Having counted 
# # to five, the program should print to the screen the final
# #  message "Ready or not, here I come!"
# for i in range (1,6):
#     print(i, "Mississipi")
#     time.sleep(1) # this method of sleep() will count like real seconds, 1 repreents a seconds
# print("Ready or not, here I come")
""""""""""""""""""""""""""""""""""""""""""

# # The break and continue statements
# # break example 
# print("The break instruction")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Inside the loop")
#     #time.sleep(2)    # Just to see a slowly execution of my code 

# print("Outside the loop")

# print()
# # continue example 
# print("The continue instruction")
# for i in range(1, 6):
#     if i ==3:
#         continue
#     print("Inside the loop")
#     #time.sleep(2)  # Just to see a slowly execution of my code
# print("Outside the loop")
""""""""""""""""""""""""""""""""""""""""""""""""""""""

# #exit_word = input("PLease enter the secret exit word ")
# while True:
#     exit_word = input("PLease enter the secret exit word ")
#     if exit_word == "chupacabra":
#         break
# print("You've successfully exit the loop")
""""""""""""""""""""""""""""""""""""""""""""""""""""""

# while True:
#     word = input("You're stuck in an infinite loop!\nEnter the secret word to leave the loop: ")
#     if word == "chupacabra":
#         break
# print("You've successfully left the loop!")
""""""""""""""""""""""""""""""""""""""""""

        
# word = input("Please enter a word ")# Prompt the user to enter a word
# user_word = word.upper()# and assign it to the user_word variable.

# for letter in user_word:
#     if letter == "A":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue
#     elif letter == "E":
#         continue
#     else:
#         print(letter)# Complete the body of the for loop.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""" 

# for i in range(1, 10):
#     if i % 2 == 0:
#         print(i)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# word = "Python"
# for letter in word:
#     print(letter, end="*")
#     # print(letter)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# counter = 5
# while counter > 2:
#     print(counter)
#     counter -= 1
""""""""""""""""""""""""""""""""""""""""""""
# text = "OpenEDG Python Institute"   #You use break to exit a loop
# for letter in text:
#     if letter == "P":
#         break
#     print(letter, end="")
""""""""""""""""""""""""""""""""""""""""""""
# text = "pyxpyxpyx"    #You use continue to skip the current iteration, and continue with the next iteration
# for letter in text:
#     if letter == "x":
#         continue
#     print(letter, end="")
""""""""""""""""""""""""""""""""""""""""""
# for i in range(6, 12):
#     print(i, end=" ")  # Outputs: 6, 4, 2
""""""""""""""""""""""""""""""""""""""""""
#  Create a for loop that counts from 0 to 10, and 
#  prints odd numbers to the screen. Use the skeleton below
# for i in range(1, 11):
#     if i % 2 !=0:
#         print(i)
""""""""""""""""""""""""""""""""""""""""""
#  Create a while loop that counts from 0 to 10, and prints
# odd numbers to the screen. Use the skeleton below:
# x = 1
# while x < 10:
#     if x % 2 !=0:
#         print(x)
#     x += 1
""""""""""""""""""""""""""""""""""""""""""
# Create a program with a for loop and a break statement. 
# The program should iterate over characters in an email address, 
# exit the loop when it reaches the @ symbol, and print the part before @ on one line. 
# Use the skeleton below:
# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch, end="")
""""""""""""""""""""""""""""""""""""""""""
# Create a program with a for loop and a continue statement. 
# The program should iterate over a string of digits, replace 
# each 0 with x, and print the modified string to the screen. Use the skeleton below:
# for digit in "0165031806510":
#     if digit == "0":
#         print("x", end="")# Line of code.
#         continue# Line of code.
#     print(digit, end="")# Line of code.
""""""""""""""""""""""""""""""""""""""""""
# What is the output of the following code?
# n = 3
 
# while n > 0:
#     print(n + 1)
#     n -= 1
# else:
#     print("else",n)
""""""""""""""""""""""""""""""""""""""""""
# # What is the output of the following code?
# n = range(4)
 
# for num in n:
#     print(num - 1) # this should start to the lowest number which is 0
# else:              # but since it is -1, that's why it should start from -1
#     print(num)
""""""""""""""""""""""""""""""""""""""""""
# # What is the output of the following code?
# for i in range(0, 6, 3):
#     print(i)
""""""""""""""""""""""""""""""""""""""""""

while True:
    secret_word = input("Please enter the secret word ")
    if secret_word == "chupacabra":
        break
print("You've successfully left the loop")
        
        
 
