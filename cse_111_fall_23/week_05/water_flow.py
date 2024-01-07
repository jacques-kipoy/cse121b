# CSE 111 Class
# Week 05 L05 Prove Milestone: Testing and fixing Functions
# Jacques Kipoy
# Professor : David Christofferson


def water_column_height(tower_height, tank_height):
    """This function calculate the water calumn height
    and returns the height of a column water
    parameters : tower_height and tank_height 
    return : the height of a column water
    formula : h = t + (3 * w) / 4 
    where
    h is height of the water column
    t is the height of the tower
    w is the height of the walls of the tank that is on top of the tower """
    h = tower_height + (3 * tank_height) / 4
    return h 
    
def pressure_gain_from_water_height(height):
    """this function calculate and return the pressure
    caused by Earth's gravity pulling on the water stored
    in elevated tank 
        where
    P is the pressure in kilopascals
    p is the density of water (998.2 kilogram / meter3)
    g is the acceleration from Earths gravity (9.80665 meter / second2)
    h is the height of the water column in meters
    Parameter : height
    return : Pressure in kilopascal
    P = (p * g * h) / 1000
    """
    P = (998.2 * 9.80665 * height) / 1000
    return P 

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """ calculates and returns the water pressure
    lost because of the friction between the water 
    and the walls of a pipe that it flows through.
        where
    P is the lost pressure in kilopascals
    f is the pipe’s friction factor
    L is the length of the pipe in meters
    ρ is the density of water (998.2 kilogram / meter3)
    v is the velocity of the water flowing through the pipe in meters / second
    d is the diameter of the pipe in meters
    Formula : P = -(f *L * p * (v**2)) / (2000 * d)

    Parameter : pipe_diameter, pipe_length, friction_factor, fluid_velocity
    Return : Pressure"""
    P = -(friction_factor * pipe_length * 998.2 * (fluid_velocity ** 2)) / (2000 * pipe_diameter)
    return P

