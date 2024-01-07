print()
print("This is an adventure game")
print()
walking = input("You are walking down the street and you are in the intersection of two street, one on your right and the other on your left, which one are you going to choose? right or left ? ")
if walking.lower() == "right" :
    story = "On this street there is a marathon which is organized, are you going to participate, Yes or Not "
    answer = input(" what is your answer? ")
    if answer.lower() == "yes" :
        say = "Good"
    elif answer.lower() == "no" :
        say = "okay"
        print(say)
    else:
        print("choose a correct answer")
elif walking.lower() == "left" :
    story = "When you take this street, you meet your friends who are going to play soccer, will you play or not? "
    print(story)
else:
    print(" This is not an option, choose one answer ")
