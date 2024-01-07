a = [1,2,3]
b = a
a = [4,5,6]
#print(b)


#List, we can append in a list but not a tuple
my_list = [2, True , False, ["Hello", "World"], 7, 8]
print(my_list)

#Set
my_set = {3,5,7,9,0}
print(my_set)

#The order of the element really matter so it can be True
a = [2,1] == [1,2]
print(a)

#For a set, the order of the element doesnt really matter 
b = {2,1} == {1,2}
print(b)

#Tuples : The order matter for tuples, we use parenthesis for tuples
#tuple has not attribute append
my_tuple = (2,3,54,5)
print(len(my_tuple))

#Dictionary
print()
my_dictionary = {
    "apple" : "A red fruit",
    "bear" : "A scary animal"
}
print(my_dictionary["apple"])