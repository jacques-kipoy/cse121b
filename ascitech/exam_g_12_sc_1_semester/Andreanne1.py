# number 10
# balanda ya'dal

x=int(input("how old are you ?"))
if x>=18 :
      print("you can have a driver license ")
      y=x-18
      print(" you had receive your driver license since",y,"years")
elif 12<x<17 :
    print(" you can learn but not have a driver license yet")
    z=18-x
    print("you need",z,"years to get your driver license ")
elif x<12 :
    print(" you can't either learn or have a driver license ")
    w=18-x
    print ("you need ",w,"years to get your drivr license")
