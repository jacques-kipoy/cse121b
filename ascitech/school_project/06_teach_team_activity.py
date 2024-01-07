print()
age_of_the_first_rider = float(input("What is the age of the first rider? "))
height_of_the_first_rider = float(input("What is the height of the first rider? "))
is_there_a_second_rider = str(input("Is there a second rider, yes/no? "))
age_of_the_second_rider = float(input("What is the age of the second rider? "))
height_of_the_second_rider = float(input("What is the height of the seconr rider? "))

if height_of_the_first_rider < 36 or height_of_the_second_rider < 36:
    print("You can't ride, sorry oh")
elif age_of_the_first_rider >= 18 and age_of_the_second_rider >= 18:
    second_rider = input("Is there a second rider Yes/No ?")
    if second_rider.lower() == "yes":
        # print(age_of_the_second_rider)
        if age_of_the_first_rider >= 18 or age_of_the_second_rider >= 18:
            print("You can ride!")
        else:
            print("You can't ride")
    elif second_rider.lower == "no":
        print("You Can't ride")
    height =float(input("What is the height of the first rider? "))
    height_2 = float(input("what is the hieght of the second rider? "))
    if height >= 62 and height_2 >= 62:
        print("A single rider can ride ")
    else:
        print("You can't ride")
elif age_of_the_first_rider >= 18 or age_of_the_second_rider >= 18:
    print("You may ride together! ")
else:
    print("You can't ride!")
