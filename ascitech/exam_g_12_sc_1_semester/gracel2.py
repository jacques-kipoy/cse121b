a=int(input("how old are you "))
if a>=18:
    print("you can have a drive license")
    b=a-18
    print("you receveid your driver license ",b,"years ago" )
elif a>=12 and a<=17:
    print("you can learn but not have a driver license yet")
    c=18-a
    print("you is remaining to get a driver license in",c,"years")
elif a<12:
    print("you can t either learn or have a driver license")
    d=18-a
    print("you is remaining to get q driver license in",d,"years")
else:
    print("please read a number")



