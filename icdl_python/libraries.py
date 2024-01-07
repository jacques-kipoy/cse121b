# Libraries
import random

fruits = ["apple", "pear","banana","grapefruit"]

print(random.choice(fruits))  #choice is a function

# Alternative version of import is 
from random import choice, randint
print()
print("An alternative version of import ")
print()
fruits = ["apple", "pear","banana","grapefruit"]
print(choice(fruits))
