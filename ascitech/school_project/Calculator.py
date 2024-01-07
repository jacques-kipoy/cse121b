#This program is a calculator

#This function adds two numbers
def add(x, y):
    return x + y

#This function substracts two numbers
def substract(x, y):
        return x -y

#This  function multiplies two numbers 
def multiply(x, y):
    return x * y

#This function divides two numbers
def divide(x, y):
    return x/y

print("Select operation")
print("1. Add")
print("2. Substract")
print("3.Multiply ")
print("4. Divide")

while True:
    #Take the input from the user
    choice = input("Enter choice : 1, 2, 3, 4 ")

    #Check if choice is one of the four options
    if choice in ("1", "2", "3", "4"):
        num_1 = float(input("Enter the firsst number "))
        num_2 = float(input("Enter the second Number "))

        if choice == "1":
            print(num_1, "+", num_2, "=", add)(num_1, num_2)

        elif choice == "2":
            print(num_1, "-", num_2, "=", add(num_1, num_2))

        elif choice == "3":
            print(num_1, "*", num_2, "=", add(num_1, num_2))

        elif choice == "4":
            print(num_1, "/", num_2, "=", add(num_1, num_2))

        #Check if the user wants anoter calculation
        #Break the while loop if the answer is no
        next_calculation = input("would you like to calculate again? Yes or No ")
        if next_calculation =="No":
            break

        else:
            print("invalid input")
