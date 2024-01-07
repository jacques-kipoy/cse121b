# CSE 111 Class
# Week 03 L03 Team Activity: writting Functions
# Jacques Kipoy
# Professor : David Christofferson

# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    user_gender = input("Enter your gender (M or F): ")
    user_birthday = input("Enter your birthdate (YYYY-MM-DD): ")
    user_weight = float(input("Enter your weight in U.S. pounds: "))
    user_height = float(input("Enter your height in U.S. inches: "))

    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    age_ = compute_age(user_birthday)
    kg_ = kg_from_lb(user_weight)
    centi_ = cm_from_in(user_height)
    bmi_ = body_mass_index()
    bmr_ = basal_metabolic_rate()


    # Print the results for the user to see.
    print(f"Age (years): {age_}")
    print(f"Weight (kg): {kg_:.2f}")
    print(f"Height (cm): {centi_:.1f}")
    print(f"Boody mass index: {bmi_}")
    print(f"Basal metabolic rate (kcal/day): {bmr_}")
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    pound_to_kilo_gram = pounds *  0.45359237
    return pound_to_kilo_gram


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    inches_to_centimeter = inches *  2.54
    return inches_to_centimeter


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000 * weight) / (height ** 2)
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    bmr_women =  447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    bmr_man = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age 


    return bmr_women and bmr_man 


# Call the main function so that
# this program will start executing.

main()
