# 06_team_activity
# No one under 36 inches may ever ride, either by themselves or with another rider.

# Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.

# If there are two riders and one of them is at least 18 years old, they may ride together.

#Notice the use of a boolean variable, set to False by default
can_ride = False
first_rider_age = int(input("What is the age of the first rider? "))
height_of_first_rider = int(input("What is the height of the first rider? "))

is_second_rider = input("Is there a second rider yes/no? ")

if is_second_rider.lower() == "yes":
    second_rider_age = int(input("What is there second rider age? "))
    height_of_second_rider = int(input("What is the height of the second rider? "))
    #Rule number 1 
    if height_of_first_rider < 36 or height_of_second_rider < 36:
        can_ride = False
    else:
        if first_rider_age >= 18 or second_rider_age >= 18:
            can_ride = True
        else:
            can_ride = False
else:
    if first_rider_age >= 18 and height_of_first_rider >= 62:
        can_ride = True
    else:
        can_ride = False

if can_ride:
    print("Welcome to the ride, please be safe and have fun! ")
else:
    print("Sorry, you may not ride")

