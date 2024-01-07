
# Indexing a list 
print()
numbers = [10,5,7,2,1]
print("Original list content", numbers)

numbers[0] = 111
print("previous list contents", numbers)

numbers[1] = numbers[4]
print("Current list contents", numbers)
print()
# accessing list content,  the list is a very dynamic entity
print(numbers[0])
print()
print("List length:", len(numbers)) # printing the list length
print(numbers)
#Removing elements from a list
# We use the del instruction
del numbers[0]
print(numbers)

print()
""""""""""""""""""""""""""""""""""""""""""""""""""
#print(numbers[4]) # you can't access an element that doesn't exist or assign it a value
# numbers[4] = 1
print()
# Negative indices are legal
# It may look strange, but negative indices are legal, and can be very useful.
# An element with an index equal to -1 is the last one in the list. 
# When it is negative, we count from right to left -1 is the last one, -2 is the one following and so forth
print(numbers[-1])
print(numbers[-2])
""""""""""""""""""""""""""""""""""""""""""""""""""
# Append and insert 
# insert can add in a specific location while append will only add at the end of the list
numbers.append(55)
print(len(numbers))
print(numbers)

print()

numbers.insert(0, 82)
print(len(numbers))
print(numbers)
""""""""""""""""""""""""""""""""""""""""""""""""
# Starting with an empty list 
my_list = []
for i in range(5):
    my_list.append(i)
    i += i
print(my_list)
""""""""""""""""""""""""""""""""""""""""""""""""
print()
my_list_ = []
# Using the insert methode
for i in range (5):
    my_list_.insert(0, i +1)
print(my_list_)
