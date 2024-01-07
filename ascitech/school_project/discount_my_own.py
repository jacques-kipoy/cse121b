# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime , timedelta  # This is the date and time library

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

# Print the day of the week for the user to see. Monday = 0, Tuesday=1, Wednesday=2, Thursday = 3, ...
print(day_of_week)

print("Today is", current_date_and_time)

# timedelta is used to define a period of time
today = datetime.now()
one_day = timedelta(days=1)
yesterday = today - one_day
print("One day",one_day)
print("Yesterday",yesterday)
print("Today", today)

day_of_week = 2 # temporarily add this line of code, in other to test my code

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

else:
    tax = (subtotal * 6) / 100
    total = subtotal + tax
    print(f"Total: {total:.2f}")

