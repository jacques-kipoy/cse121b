def start(numbers_of_starts):
    answer = ""
    for i in range(numbers_of_starts):
        answer += "*"
    answer = answer.center(30)
    return answer
    
def arrow_head():
    for i in range(10):
        print(start(i*2+1))

arrow_head()