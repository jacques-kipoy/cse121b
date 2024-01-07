# Jacques Kipoy
# Coding Trainer
#ASCITECH
#Grade 10 COM and Litt

# This programm will calculate the Compound interest of a loan after a given time 

# The compound interest formula is : A = P*(1+r/n)**(n*t)
# A = Final ammount
# P = Initial principal balance
# r = interest rate
# n = number of times interest applied per time period
# t = number of time periods elapsed

# OR

# FV = P*(1+R/N)**(n*t)
# FV = is the future value of the loan or investment
# P = is the initial principal amount
# R = is the annual interest rate 
# N = represent the number of times interest is compounded per year 
# T = represents time in years

print()
print("This program will calculate the Compound Interest Rate")
print()

principal_amount = int(input("Enter the principal amount "))
anual_interest_rate = float(input("What is the anual interest rate in percentage "))
number_of_time = int(input("What is the numer of time the interest rate is done per year? "))
time_in_year = int(input("For How many year the compound has been done? "))

future_value = principal_amount*(1+anual_interest_rate/number_of_time)**(number_of_time*time_in_year)

print()
print("----------------------------------------------------------")
print("The Compound interest rate after", time_in_year, " year is $", future_value)
print("----------------------------------------------------------")


