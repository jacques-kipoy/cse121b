import random 

def main():
    numbers = [16.2, 75.1, 52.3]
    
    print(f"My first is list {numbers}")

     # Call the append_random_numbers function to
    # add one random number to the numbers list.
    append_random_numbers(numbers)
    print(f"My second is list {numbers}")

    # Call the append_random_numbers function to add
    # three random numbers to the numbers list.
    append_random_numbers(numbers, 3)  # the second argument is the quantity
    print(f"My third list is {numbers}")



def append_random_numbers(numbers_list, quantity = 1):

    for i in range(quantity):
        random_numbers = random.uniform(1,100)
        rounded = round(random_numbers, 1)
        numbers_list.append(rounded)

    # num = random.uniform(1,20)
    # num_r= round(num, 1)
    # my= numbers_list.append(num_r)
    # return my





# If this file was executed like this:
# > python random_numbers.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()