import math

# define a function call main 
def main():
    # get the radius and height from the user
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))

    #compute the volume of the cylinder 
    # I ca change the names of this two arguments as I want, radius and height
    # can be for example r and h and my variables at line 6 and 7 should change too
    volume = compute_cylinder_volume(radius, height) 
    
    # print the volume of the cylinder
    print(f"The volume of the cylinder is {volume:.2f}")

#define a function that accepts two parameters
def compute_cylinder_volume(radius, height):
    """Compute and print the volume of a cylinder
    parameters
        radius: the radius of a cylinder 
        height: the height of a cylinder 
    Return the volume of the cylinder """

    pi_ = math.pi
    volume = pi_ * radius **2 * height
    return volume 

# starting the program by calling the main function
main()