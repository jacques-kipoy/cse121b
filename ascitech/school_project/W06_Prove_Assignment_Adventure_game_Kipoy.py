
#Week_06_Prove_Assignment_Milestone_Adventure_Game
#Jacques_Kipoy
#Matt Reno
#CSE110


print("----------------------------------------------------------------------")
print("This is an adventure game, The Correct answers are in CAPITAL letters ")
print("----------------------------------------------------------------------")
a_street = input("You are in the intersection of two street, which one are you going to take RIGHT or LEFT ? ")
if a_street.lower() == "right":
    right = input(" As you walk down the street, you see people gather together and making noises as if there is a fight, will you KEEP walking toward them or SIDESTEP? ")
    if right.lower() == "keep" :
        keep = input("As you are walking toward them, you discover that it is a great event organized in the city, will you BE part or IGNORE ? ")
        if keep.lower() == "be":
            be = input("The event is really good, everyone is enjoying! so will you DANCE or SIT ? ")
            if be.lower() == "dance": 
                print("You are enjoying well, Congratulations!")
            elif be.lower() == "sit":
                print("Because you are sitted, you can't enjoy the party, so you lost!")
            else:
                print("Please enter the correct answer? DANCE / SIT")
        elif keep.lower() == "ignore":
            ignore = input(" You are in a wide a desolated area, you see a DOG and a CAT which one will you follow? ")
            if ignore.lower() == "dog":
                print("As you follow the dog, you found the way and you are safe back home! Congratulations!")
            elif ignore.lower() == "cat":
                print("You follow the cat you get more confused and you are lost! game over!")
            else:
                print("Please choose the correct answer DOG or CAT")
        else:
            print("Please choose one of them DOG or CAT")
    elif right.lower() == "sidestep":
        sidestep = input("You are in another street and you feel like nobody is there because it is so quiete and you ca only hear birds, what are you going to do, go BACK or run AWAY? ")
        if sidestep.lower() == "back":
            back = input(" you are confused because you don't remember the way, what are you going to do LOOK for help, or REST there? ")
            if back.lower() == "look":
                print("As you are looking for help you see a bick truck coming from afar and he picked you up and you find your way home! you win!")
            elif back.lower() == "rest":
                print("So you stayed there and a lion came and eats you! you lost! game over!")
            else:
                print("Please choose a correct answer LOOK/REST")
        elif sidestep.lower() == "away":
            away = input("when you runned away, you enter a big lake, will you SWIM or FISH? ")
            if away.lower()== "swim":
                print("As you are swimming, you got caught by a big crocodile, you are dead! you lost! game over!")
            elif away.lower() == "fish":
                print("You are fishing and caught lots of fish and you brought them back home and enjoy with your family! Congratilations!")
            else:
                print("Please choose the correct answer SWIM / FISH")
        else:
            print("Please choose one correst answer BACK or AWAY ")
    else:
        print("Please choose a correct answer KEEP or SIDESTEP")
elif a_street.lower() == "left" :
    left = input("As you take this street you meet your friends and they ask you to go with them, will you GO or CONTINUE your way? ")
    if left.lower() == "go":
        go = input("You go with them, they tell you that they are going hiking, are you INTERESTED or TIRED? ")
        if go.lower() == "interested":
            interested = input("You go hiking but you feel very tired and don't want to STAY but your friends ENCOURAGED you to continue, what will you do? ")
            if interested.lower() == "stay":
                print("As you are staying there, you got caught by a big grizzle bear and he ate you, you lost!")
            elif interested.lower() == "encouraged":
                print("You feel strong now and you enjoyed the activity with your friens and dicovered many things on the mountain! Congratulations!")
            else:
                print("Please choose the correct answer STAY / ENCOURAGED")
        elif go.lower() == "tired":
            tired = input("You just want to find a fast food where you can eat on your way back home, what are you going to do, look for a FAST food or go STRAIGHT home? ")
            if tired.lower() == "fast":
                print("You can't find a fast food in this area, you are starving and you go dead! you lost!")
            elif tired.lower() == "straight":
                print("You get back home and you are safe! Congratulations!")
            else:
                print("Please Choose a correct answer FAST / STRAIGHT ")
        else:
            print("Please choose a correct answer INTERESTED / TIRED ")
    elif left.lower() == "continue":
        left = input("As you are walking, you see a big junglr a far, and also another big TREE where will you go JUNGLE or TREE? ")
        if left.lower() == "jungle":
            jungle = input("You are in a big jungle and you are very afraid because of the wild animals, what will you do CRY or keep QUIET? ")
            if jungle.lower() == "cry":
                print("As you are crying, looves came and devoured you! you lost!")
            elif jungle.lower() == "quiet":
                print("AS you kept quiet, you see a pathway and you followed it, you are safe and out of the jungle, congratulations!")
            else:
                print("Please choose the correct answer CRY / QUIET")

        elif left.lower() == "tree":
            tree = input(" There is a lot of fruit, will CAST stones or CLIMB? ")
            if tree.lower() == "cast":
                print("You picked lots of fruits and you are enjoying! congratulations! ")
            elif tree.lower() == "climb":
                print("As you climbed the tree, you meet a big snake and he kills you! you lost!")
            else:
                print("Please choose a correct answer CAST or CLIMB")
        
        else:
            print("Please select a correct answer JUNGLE/TREE")
            
    else:
        print("Please enter a correct answer GO or CONTINUE")
else:
    print("Please choose a correct answer RIGHT or LEFT")
    
