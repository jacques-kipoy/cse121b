# W01 Prove Milestone: Review Python & W02 Prove: Calling Functions
# CSE 111
# Jacques Kipoy
# Professor : David Christofferson

""""""""""""""""""""""""""""""""""""


from datetime import datetime

current_date_and_time = datetime.now()


# Write a Python program named tire_volume.py that reads from the keyboard the three numbers for a tire and computes and outputs the volume of space inside that tire.

# v is the volume in liters,
# π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
# w is the width of the tire in millimeters,
# a is the aspect ratio of the tire, and
# d is the diameter of the wheel in inches.
""""""""""""""""""""""""""""""""""""


print("--------------------------------------------------------------------")
print("This Python program reads from the keyboard three numbers for a ")
print("tire and computes and outputs the volume of space inside that tire.")
print("--------------------------------------------------------------------")

# import math module
import math

# getting input from the user
customer = input("what is your name: ")
tire_width = int(input("Enter the width of the tire in mm (ex 205): ")) # w
tire_ratio = int(input("Enter ascpect ratio of the tire (ex 60): ")) # a
wheel_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): ")) # d

# Computing the program
# v = π * (w**2) * a * (w * a + 2540 *d) / 10_000_000_000

p = math.pi # Save pi value inside a variable named p

volume = p * (tire_width ** 2) * tire_ratio * (tire_width * tire_ratio + 2540 * wheel_diameter) / 10_000_000_000

# print = (f"The approximate volume is {volume} lites")
print()
# Rouding to the second number and display the output
print("The approcimate volume is",round(volume, 2), "liters")

buy = input("Would you like to buy this tire? yes/no ")

if buy.lower() == "yes":
    phone_number = input("Please enter your phone number: ")


    # Gets the current date from the computer’s operating system.
    # Opens a text file named volumes.txt for appending.
    # Appends to the end of the volumes.txt file one line of text that contains the following five values:
    # current date
    # width of the tire
    # aspect ratio of the tire
    # diameter of the wheel
    # volume of the tire

    # print(f"{current_date_and_time:%Y-%m-%d}")
    time = (f"{current_date_and_time:%Y-%m-%d}")
    print()

    open("volumes.txt", mode="rt")  # "rt" which means open for reading in text mode
    # open("volumes.txt", mode="wt") #"wt" for writing a text file
    with open("volumes.txt", "at") as volumes_file:
        # Print customer name and information to the file.
        print()

        print(customer, file= volumes_file)
        print(f"Current date: {time}", file=volumes_file)
        print(f"Width of the tire: {tire_width} ", file=volumes_file)
        print(f"Aspect ratio of the tire: {tire_ratio}", file=volumes_file)
        print(f"Diameter of the wheel: {wheel_diameter}", file=volumes_file)
        print(f"volume of the tire: {volume:.2f}", file=volumes_file)
        print(f"Phone number: {phone_number}", file=volumes_file)

        
else:
    # print(f"{current_date_and_time:%Y-%m-%d}")
    time = (f"{current_date_and_time:%Y-%m-%d}")
    print()

    open("volumes.txt", mode="rt")  # "rt" which means open for reading in text mode
    # open("volumes.txt", mode="wt") #"wt" for writing a text file
    with open("volumes.txt", "at") as volumes_file:
        # Print customer name and information to the file.
        print()

        print(customer, file= volumes_file)
        print(f"Current date: {time}", file=volumes_file)
        print(f"Width of the tire: {tire_width} ", file=volumes_file)
        print(f"Aspect ratio of the tire: {tire_ratio}", file=volumes_file)
        print(f"Diameter of the wheel: {wheel_diameter}", file=volumes_file)
        print(f"volume of the tire: {volume:.2f}", file=volumes_file)
