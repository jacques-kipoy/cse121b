
age=int(input())
years=int(input())

if age<=18 and years==18:
    print("you can have a driver license")
elif age <=12 and age <17 and years <=5 and years<2:
    print ("you can learn but not have a driver license yet")
elif age >12 and years <8:
    print ("you can not either learn or have a driver license and")
else:
    print ("nothing")
