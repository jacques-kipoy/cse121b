#This program will change a decimal number into a binary number in order to 
#Change a IP address into a binary number and futhermore to do the subnetting

first_part = int(input("\n Enter the first part of IP the address : "))
second_part = int(input("\n Enter the seconf part of the IP address: "))
third_part = int(input("\n Enter the third part of the IP address: "))
fourth_part = int(input("\n Enter the fourth part of the IP address: "))

x = int()
y = int()

if first_part or second_part or third_part or fourth_part > 0:
    if first_part >= 128 :
        if first_part > 64:
            first_part = 1

        else:
            first_part = 0

if second_part >= 64 or second_part > 32:
    second_part = 1
    if second_part <=32:
        second_part = 0

if third_part >= 32 or third_part > 16:
    third_part = 1
    if third_part <= 16:
        third_part = 0

if fourth_part >=16 or fourth_part > 1:
    fourth_part = 1 
    if fourth_part <=1:
        fourth_part = 0


print(f"{first_part} . {second_part} . {third_part}. {fourth_part} ")



