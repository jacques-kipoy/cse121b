# Teach_team_activity_05
grade = int(input("What is your grade percent? "))
print()
if grade >= 90 :
    letter = "A"
elif grade >= 80 :
    letter = "B"
elif grade >= 70 :
    letter = "C" 
elif grade >= 60 :
    letter = "D"
else:
    letter = "F"

print()
# Strech challenge 1
sign = ""
last_digit = grade % 10
if last_digit >= 7 :
    sign = "+"
elif last_digit < 3 :
    sign = "-"
else:
    sign = ""
print()
# Strech challenge 2
if grade >= 97 :
    sign = ""
elif grade < 60 :
    sign = ""
print(f" Your grade letter is : {letter}{sign} ")
if grade >= 70 :
    print("Congratilations! you passed the class! ")
else:
    print("Stay focus you will get next time")
