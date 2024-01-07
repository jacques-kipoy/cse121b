import math
from  datetime import datetime

# CSE 111 Class
# Week 02 L02 Prove : Calling Functions
# Jacques Kipoy
# Professor : David Christofferson

# v is the volume in liters,
# π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
# w is the width of the tire in millimeters,
# a is the aspect ratio of the tire, and
# d is the diameter of the wheel in inches.
pi = math.pi
#print(pi)
width_ = float(input("Enter the width of the tire in mm (ex 205): "))
ratio_ = float(input("Enter the aspect ratio (ex 60): "))
diameter = float(input("Enter the diameterof the wheel in inches (ex 15): "))

# w = width_
# a = ratio_
# d = diameter

curren_date_time = datetime.now()

v = (pi * (width_)**2 * ratio_ * (width_*ratio_ + 2540 * diameter)) / 10_000_000_000
#print(f"\nThe approximate volume is {v:.2f} liters\n")
name = input("Enter your name: ")
visit = input("What is the reason you visit our website ")

with open("volumes.txt", mode = "at") as my_doc :
    print(f"User name is : {name}", file=my_doc)
    print(f"The reason for visiting the website : {visit}", file=my_doc)
    print(f"{curren_date_time:%Y-%m-%d}, {width_}, {ratio_}, {diameter}, {v:.2f}", file = my_doc)


    



