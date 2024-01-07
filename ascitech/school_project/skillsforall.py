# Skills for all 
# Some convention in python


print(1_5 + 2_5) # I never new that this also works
print(15 + 25)  # It is actually the same 

# When we put 0O its a Octal number in python
print(0o123)  # This is an Octal number which equals to 83
a = 0O123
print(type(a)) # Integer but Octal number

# The second convention allows us to use hexadecimal numbers. 
# Such numbers should be preceded by the prefix 0x or 0X (zero-x).

# 0x123 is a hexadecimal number with a (decimal) value equal to 291. 
# The print() function can manage these values too. Try this:

print(0x123)  # 0x Zero and x infront of the number makes it a hexadecimal number

# When you want to use any numbers that are very large or very small, you can use scientific notation
print(3E8)  # This is a scientifc notation for 3*10**8 or 3 times 10 to the power of 8
print(5.3e4)
# the exponent (the value after the E) has to be an integer;
# the base (the value in front of the E) may be either an integer or a float.

# there are two escaped quotes inside the string ‒ can you see them both?
print("I like \"Python\" ")  #how to encode a quote inside a string which is already delimited by quotes.

#Second Method
print('I like "Python"')
print('I like \'Python\'!')

print('I\'m Mounty\' Pyhton')

# Boolean invented by George Boole
print(True > False)
print(True < False)


# Write a one-line piece of code, using the print() function, as well as the newline and escape characters, 
# to match the expected result outputted on three lines.
# "I'm "
# "" learning ""
# """ Python """
print("\"I'm\"")
print('\""learning\""')
print('\"""Python\"""')

print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")

print("\"\"\"\"I'm\"\"\"\"\"\"")

print(10//2) # This returns an integer value or it a Integer Division
print(10/2) # This returns a float value 

print(type(10//2))  # This will print the type of the literal  answer <class 'int'>
print(type(10/2)) # This will print the type of the literal  answer <class 'float'>

print(12 % 4.5)

print(+2)

# Hierachy of Priorities
print(9 % 6 % 2)

# Section quiz
print((2**4), (2*4.0), (2.4))

x = 2
x *=  2
print(x)

# Converter Programm from Mile to Kg
# 1 Mile = 1.61 Km
mile = int(input("What is the value in mile "))
convert_km = mile * 1.61
print(mile, "miles equals to ", round(convert_km, 2), "Kilometers")

print()
# Dollars to Congolese Francs currency Converter
current_exchange_rate = int(input("What is the actual dollar exchange rate "))
amount_to_exchange = int(input("How much do you want to exchange, type in dollar "))
exchange_rate_Converter = amount_to_exchange * current_exchange_rate
print("$",amount_to_exchange, "with an exchange rate of", current_exchange_rate, "equals to", round(exchange_rate_Converter,2), "CDF" )

