
def main():
    print("This program is an implementation of the Rosenberg \
    Self-Esteem Scale. This program will show you ten \
    statements that you could possibly apply to yourself. \
    Please rate how much you agree with each of the \
    statements by responding with one of these four letters: \n")
            
    print("D means you strongly disagree with the statement. \
    d means you disagree with the statement.\
    a means you agree with the statement.\
    A means you strongly agree with the statement.\
    ")

    """1. I feel that I am a person of worth, at least on an equal plane with others.\
    2. I feel that I have a number of good qualities. \
    3. All in all, I am inclined to feel that I am a failure.\
    4. I am able to do things as well as most other people.\
    5. I feel I do not have much to be proud of.\
    6. I take a positive attitude toward myself.\
    7. On the whole, I am satisfied with myself.\
    8. I wish I could have more respect for myself.\
    9. I certainly feel useless at times.\
    10. At times I think I am no good at all."""
    choice = ""
    answer =0

    posit = print_positive_statement(choice)
    negat = print_negative_statement(choice)
    giv_pos = give_positive_score(answer)
    giv_neg = give_negative_score(answer)

    print(posit)
    print(negat)


def print_positive_statement(choice):
    if choice == "first":
        print("1. I feel that I am a person of worth, at least on an equal plane with others.")
    elif choice == "second":
        print("2. I feel that I have a number of good qualities.")
    elif choice == "fourth":
        print("4. I am able to do things as well as most other people.")
    elif choice == "sixth":
        print("6. I take a positive attitude toward myself.")
    elif choice == "seventh":
        print("7. On the whole, I am satisfied with myself.")
    
    return choice


def print_negative_statement(choice):
    if choice == "third":
        print("3. All in all, I am inclined to feel that I am a failure.")
    elif choice == "fifth":
        print("5. I feel I do not have much to be proud of.")
    elif choice == "eighth":
        print("8. I wish I could have more respect for myself.")
    elif choice == "nineth":
        print("9. I certainly feel useless at times.")
    elif choice == "tenth":
        print("10. At times I think I am no good at all.")
    return choice



def give_positive_score(answer):
    """This function will give the positive point according to the
    following agreement A is strongly Agree, D is strongly Disagree, d disagree
    Choice	Points
    Strongly Disagree	0
    Disagree	1
    Agree	2
    Strongly Agree	3"""
    answer = input("Enter A, a, D, d ")
    if answer == "D":
        answer = 0
    elif answer == "d":
        answer = 1
    elif answer == "a":
        answer = 2
    elif answer == "A":
        answer = 3
    return answer

def give_negative_score(answer):
    """This function will give negative point according to the
    following agreement A is strongly Agree, D is strongly Disagree, d disagree
    Choice	Points
    Strongly Disagree	-3
    Disagree	-2
    Agree	-1
    Strongly Agree	0"""
    answer = input("Enter A, a, D, d ")
    if answer == "D":
        answer = 3
    elif answer == "d":
        answer = 2
    elif answer == "a":
        answer = 1
    elif answer == "A":
        answer = 0
    return answer

def compute_answer(calculate):
    positive = give_positive_score()
    negative = give_negative_score()
    calculate = positive + (negative)
    return calculate



main()