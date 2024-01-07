# print("Hello " + input("Enter your name "))

# print the lenth of an input, it counts the number of characters
name = input("Please enter your name ")
print(len(name)) # print the length of this variable
print(list(name)) # this fuction list will put my string inside a list

print(len(input("what is your favorite color ")))

#################################
#switch the value of a and b
a =input("a:")
b =input("b:")
a,b = b,a
print("a:",a)
print("b:",b)

#or
c = a
a = b
b = c
print("a:",a)
print("b:",b)
#################################

# Band Name generator project 
print("Welcome to the band name generator ")
city = input("What is the name of the city you grew up in ? ")
pet = input("What is your pet's name? ")
print("Your band name could be " + city +" "+ pet)