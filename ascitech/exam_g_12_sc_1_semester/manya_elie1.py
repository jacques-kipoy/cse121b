#manya shungu elie
#number 10
t=int(input("how old are you ?"))
if t>=18:
    print("you can have a driver license")
    m=int(input("since how many years had you recieve your driver license  "))
elif 12<t<17:   # added a '
     print("you can learn but not have a driver license yet")
     e=18-t   # added : here
     print("you need", e ,"years to get your driver license")
elif t<12:
    print("you can't either learn or have a driver license ")
    u=18-e
    print(" you need ",u,"years to get your driver license")
