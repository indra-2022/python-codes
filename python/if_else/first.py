import math

radius = float(input("Enter the radius of the sphere: "))

volume = (4/3) * math.pi * radius ** 3
surface_area = 4 * math.pi * radius ** 2

print(f"Volume = {volume}, Surface Area = {surface_area}")
