import math
radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))
volume = (1/3) * math.pi * radius**2 * height
slant_height = math.sqrt(radius**2 + height**2)
surface_area = math.pi * radius * (radius + slant_height)
print(f"The volume of the cone is: {volume:.2f}")
print(f"The surface area of the cone is: {surface_area:.2f}")
