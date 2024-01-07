# Using Comparison in python
n = int(input("Enter a number: "))
print(n >= 100) # if n >= 100 answer True, elif n < 100 answer False

# A program that finds the larger number between two numbers
number1 = int(input("Enter the first number "))
number2 = int(input("Enter the second number "))
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

print("The larger number is" , larger_number)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2 : largest_num = num1 
else: largest_num = num2
print("The largest number is", largest_num)

print()
# This program calculate the Largest number between 3 numbers
num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))
num3 = int(input("Enter the third number "))

if num1 > num2:
    largest_num = num1
if num2 > largest_num:
    largest_num = num2
if num3 > largest_num:
    largest_num = num3
print("The largest number is:", largest_num)

