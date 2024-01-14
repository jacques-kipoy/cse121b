# Jacques Kipoy 
# The Fibonacci number program

num_1 , num_2 = 0, 1

sum = 0
ans = input("Would you like to try the fibonacci number? yes/no: ")
ans = ans.lower()
num = int(input("Enter the number of series: "))
while ans == "yes":

    if num <= 0:
        print("Please enter a number greater than 0")

    else:
        for i in range(0, num):
            print(sum, end="___")
            num_1 = num_2
            num_2 = sum
            sum = num_1 + num_2

    ans = input("\nWould you like to try another fibonacci number? yes/no: ")
    num_1 , num_2 = 0, 1
    sum = 0
    if ans =="yes":
        num = int(input("Enter the number of series: "))

else:
    print("\nGoodbye !!!\n")