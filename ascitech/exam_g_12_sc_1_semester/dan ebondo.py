# number 10
# ebondo dan


Y=int(input("how old are you?"))
if Y>=18:
      print("you can have a driver license")
      N=int(input("since how many had you receive your driver license"))
      print("you had receive your driver license since",N,"years")
elif 12<Y<17 :
    print("you can learn but not yet a driver license yet")
    M=18-Y
    print("you need",M,"years to get your driver license")
elif Y<12 :
    print("you can't either learn or have a driver license")
    P=18-Y
    print("you need",P,"years to get your driver license")
