# CSE 111 Class
# Week 03 L03 Checkpoint writting Functions
# Jacques Kipoy
# Professor : David Christofferson


def main():
    # Get an odometer value in U.S. miles from the user.
    first_odometer = float(input("Enter the first odometer reading (miles): "))

    # Get another odometer value in U.S. miles from the user.
    second_odometer = float(input("Enter the second odometer reading (miles): "))

    # Get a fuel amount in U.S. gallons from the user.
    amount_of_fuel = float(input("Enter the amount of fuel used (gallons): "))

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(first_odometer, second_odometer, amount_of_fuel)

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)

    # Display the results for the user to see.
    print(f"{mpg:.1f} miles per gallon")
    print(f"{lp100k:.2f} per 100 kilometers")
    pass


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    compute_miles_per_gallons = (end_miles - start_miles) / amount_gallons

    return compute_miles_per_gallons


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    computer_conversion_to_liter = 235.215 / mpg
    return computer_conversion_to_liter


# Call the main function so that
# this program will start executing.
main()