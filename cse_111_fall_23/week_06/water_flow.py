# CSE 111 Class
# Week 06 L06 Prove Milestone: Troubleshooting Functions
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

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """calculates the water pressure lost 
    because of fittings such as 45° and 90°
    bends that are in a pipeline
    where
    P is the lost pressure in kilopascals
    ρ is the density of water (998.2 kilogram / meter3)
    v is the velocity of the water flowing through the pipe in meters / second
    n is the quantity of fittings 
    formula P = (-0.04 * p * (v ** 2) * n) / 2000 
    """
    P = (-0.04 * 998.2 * (fluid_velocity **2 )* quantity_fittings) / 2000
    return P

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """calculates and returns the Reynolds number for a
    pipe with water flowing through it. The Reynolds number
    is a unitless ratio of the inertial and viscous forces 
    in a fluid that is useful for predicting fluid flow in
    different situations.
    where
    R is the Reynolds number
    ρ is the density of water (998.2 kilogram / meter3)
    d is the hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe’s inner diameter.
    v is the velocity of the water flowing through the pipe in meters / second
    μ is the dynamic viscosity of water (0.0010016 Pascal seconds)
    formula R = (p * d * v) / μ """

    R = (998.2 * hydraulic_diameter * fluid_velocity) / 0.0010016
    return R

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    """calculates the water pressure lost because of water
    moving from a pipe with a large diameter into a pipe 
    with a smaller diameter.
        where
    k is a constant computed by the first formula and used in the second formula
    R is the Reynolds number that corresponds to the pipe with the larger diameter
    D is the diameter of the larger pipe in meters
    d is the diameter of the smaller pipe in meters
    P is the lost pressure kilopascals
    ρ is the density of water (998.2 kilogram / meter3)
    v is the velocity of the water flowing through the larger diameter pipe in meters / second

    formula k = (0.1 +(50/R)) * ((D ** 4) / (d ** 4)-1)
    P = (-k * p * (v ** 2)) / 2000
    """
    k = (0.1 + (50/reynolds_number)) * ((larger_diameter ** 4) / (smaller_diameter ** 4) -1)
    P = (-k * 998.2 * (fluid_velocity ** 2)) / 2000
    return P

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()