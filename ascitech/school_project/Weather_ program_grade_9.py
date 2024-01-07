from re import T


temp_celcius= int(input("\nWhat is your temperatuere in celcius?\n "))
if temp_celcius > 40 :
    print("Heat wave! Stay at home")
elif temp_celcius > 20 and temp_celcius <= 40:
    print("Very hot weather.Stay hydrated")
elif temp_celcius > 10 and temp_celcius <= 20:
    print("\nGreat weather with cool breeze\n")
elif temp_celcius> 0 and temp_celcius <= 10:
    print("Weather is a bit chilly.Wear warm clothes")
else :
    print("Winter time. grab your winter jacket")

