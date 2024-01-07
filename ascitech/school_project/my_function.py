from datetime import datetime

date_= datetime.now()

# This fonction print date and time 
def print_time(task_name):
    print(task_name)
    print("hello John")
    print(datetime.now)

first_name = "susan"
print_time("printed first name")

""""""""""""""""""""""""""""""""""""""""""""""""
# ask for someone name and return the initial
first_name = input("Enter your first name: ")
first_name_initial = first_name[0:1] # 0 start from the first position, 1 take only one charater or take the first letter of the name entered
# print(first_name_initial)

middle_name = input("Enter your moddle name: ")
middle_name_initial = middle_name[0:1]

last_name = input("Enter your last name: ")
last_name_initial = last_name[0:1]

print("Your initial are " + first_name_initial + middle_name_initial + last_name_initial)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# The same example but with a function
# This function will return the first initial of the name 
def get_initial(name):
    initial = name[0:1]
    return initial

# ask for someone name and return the initial
first_name = input("Enter your first name: ")
first_name_initial = get_initial(first_name) 

middle_name = input("Enter your moddle name: ")
middle_name_initial = get_initial(middle_name)

last_name = input("Enter your last name: ")
last_name_initial = get_initial(last_name)

print("Your initial are " + first_name_initial + middle_name_initial + last_name_initial)
""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Using a defualt parameter boolean value
def get_initial_(name, force_uppercase = True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial
#Ask for someone's name and return initials
first_name = input("Enter your first name: ")
first_name_initial = get_initial_(first_name)  # didnt pass the force upper because the default is True, don't need to pass it again
print("Your initial is:", first_name_initial)
print("Your initial is:", first_name_initial, False)# Passing force_uppercase to False
print("Your initial is:", first_name_initial, True) # Passing force_uppercase to True
# if you want to pass the parameter in any order
print("Your initial is:", force_uppercase = False, name = first_name)

