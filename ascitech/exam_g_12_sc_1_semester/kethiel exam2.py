answer=int(input("Hello what is your age?"))
if answer==18:          #forgot to write answer but wrote aswer
 print("you can have a driver license since now")
elif answer>18:
 age1=answer-18          #forgot to write answer but wrote aswer
 print("you can have a driver license since age1")
elif answer<18 and answer>12:
 print("you can have a driver license in few years")
elif answer<18:
 print("you cannot have a driver license")
else:
 print("you are a baby ask to your parent to drive you")
