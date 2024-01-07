from tkinter import N


my_ip = int(input("Enter the first octect "))

if my_ip > 128:
    new_var =my_ip % 128
    print(1) 
else:
    print(0)N

# print(my_ip)