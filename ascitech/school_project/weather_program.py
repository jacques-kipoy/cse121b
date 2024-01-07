#this program will calculate the weather
#  based on temperature use python syntax
#for this pseudo code
#_create a variable called:
temp = 0
while temp < 10:
    
    temp_celcius = int(input("Enter the temperature: "))
    if temp_celcius > 40:
        print()
        print("Heat wave! Stay at home.")
    elif temp_celcius > 20 and temp_celcius <= 40 :
        print()
        print("Very hot weather, stay hydrated")
    elif temp_celcius >10 and temp_celcius <= 20:
        print()
        print("Great weather with cool breeze ") 
    elif temp_celcius > 0 and temp_celcius <= 10:
        print()
        print("Weather is a bit chilly, wear warm clothes")
    else:
        print()
        print("Winter time, grab your winter jacket")           
