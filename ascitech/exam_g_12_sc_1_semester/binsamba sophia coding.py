#driver license
#malombo sophia
#grade12
#mr jaques
y = 0
x=int(input(" how old are you?"))
if x >= 18:
    y=x-18
    print("you can have a driver license")
    print("you had your driver license since", y)  #y=18-x
elif 12 < x < 17:
    y=18-x
    print("you can learn but not have driver license yet")
    print("you will have your driver license after", y) # The error was to copy this formula inside  y=18-x
elif x < 12:
    y=18-x
    print("you can't either learn or have a driver license") 
    print("you will have your driver license in", y) # y=18-x
