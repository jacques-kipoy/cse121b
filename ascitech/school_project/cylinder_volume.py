# Example 1

import math

# Define a function named print_cylinder_volume.
def print_cylinder_volume():
    """Compute and print the volume of a cylinder.
    Parameters: none
    Return: nothing
    """
    # Get the radius and height from the user.
    radius = float(input("Enter the radius of a cylinder: "))
    height = float(input("Enter the height of a cylinder: "))

    # Compute the volume of the cylinder.
    volume = math.pi * radius**2 * height

    # Print the volume of the cylinder.
    print(f"Volume: {volume:.2f}")

print_cylinder_volume()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Getting input through parameters is much more flexible than asking the user for input because the input through parameters can come from the user or a file on a hard drive or the network or a sensor or even another function.
# Example 2

import math

# Define a function named print_cylinder_volume.
def print_cylinder_volume(radius, height):
    """Compute and print the volume of a cylinder.
    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: nothing
    """
    # Compute the volume of the cylinder.
    volume = math.pi * radius**2 * height

    # Print the volume of the cylinder.
    print(volume)

# Because the second version of the print_cylinder_volume function accepts two parameters, it must be called with two arguments like this:
print_cylinder_volume(2.5, 4.1)

""""""""""""""""""""""""""""""""""""""""""""""""""""""
# To return a result from a function, simply type the keyword return followed by whatever result you want returned to the calling function. Example 3 contains a third version of the cylinder volume function. Notice that the version in example 3 returns the volume instead of printing it, which makes the function more reusable. Notice also in example 3 that we changed the name of the function from print_cylinder_volume to compute_cylinder_volume because this version doesn’t print the volume but instead returns it.

# Example 3

import math

# Define a function named computer_cylinder_volume.
def compute_cylinder_volume(radius, height):
    """Compute and return the volume of a cylinder.
    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the volume of the cylinder
    """
    # Compute the volume of the cylinder.
    volume = math.pi * radius**2 * height

    # Return the volume of the cylinder so that the
    # volume can be used somewhere else in the program.
    return volume

# Many functions that you’ve used in the past such as input, float, and round, return a result. When a function returns a result, we usually write code to store that returned result in a variable to use later in the program like this:
    # text = input("Please enter your name: ")

# Because the compute_cylinder_volume function in example 3 accepts two parameters and returns a result, it could be called like this:

volume = compute_cylinder_volume(2.5, 4.1)
print(f"The volume of the Cylinder is:{volume:.2f}")
print("The volume of the Cylinder is:",round(volume,3))
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# In a large program, writing statements outside a function can lead to poor organization. Professional software developers write statements inside a function whenever possible. Beginning with this lesson, you will do the following in each program:

# Write nearly all statements inside a user-defined function.
# Write a user-defined function named main, which contains the beginning statements of your program.
# Write one or more user-defined functions that have parameteters, perform calculations and other useful work, and return a result to the call point.
# Write a call to the main function at the bottom of your program.
# Example 5 contains the same Python program as example 4 except most of the statements are inside a user-defined function named main.
# Example 5

import math

# Define a function named main.
def main():
    # Get the radius and height from the user.
    radius = float(input("Enter the radius of a cylinder: "))
    height = float(input("Enter the height of a cylinder: "))

    # Compute the volume of the cylinder.
    volume = math.pi * radius**2 * height

    # Print the volume of the cylinder.
    print(f"Volume: {volume:.2f}")

# Start this program by
# calling the main function.
main()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# A Complete Program with User-Defined Functions
# If you look closely at the code in examples 1 and 5, you will realize that both programs have the same problem, namely both the print_cylinder_volume function in example 1 and the main function in example 5 are not reusable because both of them get input from a user and print to a terminal window. A better way to write the program in examples 1 and 5 is to separate the program into two functions, one named main and one named compute_cylinder_volume as shown in example 6.

# Example 6 contains a complete program with two functions, the first named main at line 6 and the second named compute_cylinder_volume at line 20. At line 13, the main function calls the compute_cylinder_volume function. Notice that the compute_cylinder_volume function gets its input through parameters and returns a result which makes this function reusable in other programs, including programs that run automatically without a user.
# Example 6

import math

# Define the main function.
def main():
    # Get a radius and a height from the user.
    radius = float(input("Enter the radius of a cylinder: "))
    height = float(input("Enter the height of a cylinder: "))

    # Call the compute_cylinder_volume function and store
    # its return value in a variable to use later.
    volume = compute_cylinder_volume(radius, height)

    # Print the volume of the cylinder.
    print(f"Volume: {volume:.2f}")


# Define a function that accepts two parameters.
def compute_cylinder_volume(radius, height):
    """Compute and print the volume of a cylinder.
    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the volume of the cylinder
    """
    # Compute the volume of the cylinder.
    volume = math.pi * radius**2 * height

    # Return the volume of the cylinder so that the
    # volume can be used somewhere else in the program.
    # The returned result will be available wherever
    # this function was called.
    return volume


# Start this program by
# calling the main function.
main()