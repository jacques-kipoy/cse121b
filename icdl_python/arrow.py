#Procedures and Functions
# Arrow.py

def start(numbers_of_starts):
    answer = ""
    for i in range(numbers_of_starts):
        answer += "*"
    answer = answer.center(30)
    return answer
    
print(start(1))
print(start(3))
print(start(5))

#Lines.py
# def line_vert():
#     for i in range(10):
#         print("*")

# def line_horz():
#     answer= ""
#     for i in range(10):
#         answer += "*"
#     print(answer)

# print("Example of two procedures called from within a program")
# line_vert()
# line_horz()
