#Elie Grade 9 Etro


age = int(input("enter your age : "))
if age >= 18:
    license_year = age - 18
    print("you can have your driving license.", "you had the possibility to have a driving license {} years ago ".format(license_year))
elif age >= 12 and age <= 17:
    license_year_ = 18 - age
    print("you can get your license in","{} year".format(license_year_))
elif age < 12 :
    license_year__ = 18 - age
    print("you can get your license in","{} year".format(license_year__))