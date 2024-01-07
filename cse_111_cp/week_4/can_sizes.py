# Week 4 Team Activity Writing Function 
# Jacques Kipoy
# CSE 111
#
import math 

pi = math.pi

def main():
    name_1 = "#1 Picnic"
    radius = 6.83
    height = 10.16
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    # This will calculate the storage efficiency 
    # storage_efficiency = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f" {name_1} {storage_efficiency:.2f}")

    name_1 = "#1 Tall"
    radius = 7.78
    height = 11.91
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    # This will calculate the storage efficiency 
    # storage_efficiency = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f" {name_1} {storage_efficiency:.2f}")

    name_1 = "#2"
    radius = 8.73
    height = 11.59
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    # This will calculate the storage efficiency 
    # storage_efficiency = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f" {name_1} {storage_efficiency:.2f}")

    name_1 = "#2.5"
    radius = 10.32
    height = 11.91
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    # This will calculate the storage efficiency 
    # storage_efficiency = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f" {name_1} {storage_efficiency:.2f}")

    name_1 = "#3 Cylinder"
    radius = 10.79
    height = 17.78
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    # This will calculate the storage efficiency 
    # storage_efficiency = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f" {name_1} {storage_efficiency:.2f}")

    name_1 = "#5"
    radius = 13.02
    height = 14.29
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    # This will calculate the storage efficiency 
    # storage_efficiency = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f" {name_1} {storage_efficiency:.2f}")

    name_1 = "#6Z"
    radius = 5.40
    height = 8.89
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    # This will calculate the storage efficiency 
    # storage_efficiency = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f" {name_1} {storage_efficiency:.2f}")

    name_1 = "#8Z short"
    radius = 6.83
    height = 7.62
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    # This will calculate the storage efficiency 
    # storage_efficiency = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f" {name_1} {storage_efficiency:.2f}")

    name_1 = "#10"
    radius = 15.72
    height = 17.78
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    # This will calculate the storage efficiency 
    # storage_efficiency = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f" {name_1} {storage_efficiency:.2f}")

    name_1 = "#211"
    radius = 6.83
    height = 12.38
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    # This will calculate the storage efficiency 
    # storage_efficiency = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f" {name_1} {storage_efficiency:.2f}")

    name_1 = "#300"
    radius = 7.62
    height = 11.27
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    # This will calculate the storage efficiency 
    # storage_efficiency = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f" {name_1} {storage_efficiency:.2f}")

    name_1 = "#303"
    radius = 8.10
    height = 11.11
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    # This will calculate the storage efficiency 
    # storage_efficiency = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f" {name_1} {storage_efficiency:.2f}")



def compute_volume(radius, height):
    """This function will compute the volume of the can steel"""
    # volume = pi * radius **2 * height 
    volume = pi * radius **2 * height
    return volume

def compute_surface_area(radius, height):
    "This function will compute the surface area of the can steel"
    # surface_area = 2 * pi * radius *(radius + height)
    surface_area = 2 * pi * radius * (radius + height)
    return surface_area

main()








