# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

#day_of_week = 5   # a test with any day of the week

# Print the day of the week for the user to see.
print(day_of_week)

customer_subtotal = float(input("Pleaase Enter the subtotal: "))

# discount = .10
# tax_1 = .06

if customer_subtotal >= 50 and day_of_week > 0 and day_of_week < 3:
    discount = customer_subtotal * 10 / 100   # 10 %
    new_sub = customer_subtotal - discount
    tax_6 = new_sub *6 /100 # -10 + 6
    sub_t = new_sub - tax_6

#total = customer_subtotal - discount + tax_6

    print(f"Sales tax amount: {tax_6:.2f}")    

    print(f"{sub_t:.2f}")

    
