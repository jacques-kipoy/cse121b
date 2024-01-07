
import datetime # Import the datetime library

from datetime import datetime # Import datetime class from datetime library
time = datetime.now()

# name = input("what is your name ")
# print("\nYour name is ", name,"\n")
# print(time)

def print_time():
    print("Hello John")
    print("Here is the time", datetime.now())

print_time()
print()

# Now using function with parameter
def print_the_time(task_name):
    print(task_name)

print_the_time("Hmm really, you did that!")

print()
def get_initial(name):
    initial = name[0:2]
    return initial

first_name = input("enter your first name ")
last_name = input("Enter your last name ")
print()
first_init = get_initial(first_name)
last_init = get_initial(last_name)
print("Your initial is", first_init + last_init)
