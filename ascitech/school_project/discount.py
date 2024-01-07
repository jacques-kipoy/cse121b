# 02 Team Activity: Calling Functions
# CSE 111
# Jacques Kipoy
# David Christofferson

# You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store’s slowest sales days. On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%

# If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the subtotal. Your program must then compute the total amount due by adding sales tax of 6% to the subtotal. Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime 

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_time.weekday()


day_of_week = 2 ## temporarily add this line of code, in other to test my code

subtotal = float(input("Please enter the subtotal: "))

if day_of_week == 1 or day_of_week == 2:
    if subtotal >= 50:
        discount = (subtotal * 10) / 100
        subtotal -= discount 
        tax = (subtotal * 6) /100
        total = subtotal + tax
        print(f"Discount amount: {discount:.2f}")
        print(f"Sales tax amount: {tax:.2f}")
        print(f"Total: {total:.2f}")

    elif subtotal < 50:
        tax = (subtotal * 6) / 100
        total = subtotal + tax
        print(f"Total: {total:.2f}")

        # Stretch Challenge
        discount = 50 - subtotal
        print(f"You need to add items for {discount} $, in other to receive a discount")

else:
    tax = (subtotal * 6) / 100
    total = subtotal + tax
    print(f"Total: {total:.2f}")

