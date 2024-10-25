# Find the circumference of a circle
import math 
radius = float(input("Enter the radius of a circle: "))
circumference = 2*(math.pi)*radius
print(f"The circumference of a circle is = {circumference}")
print(f"The circumference of a circle is = {round(circumference, 2)}cm")

# Find the area of a circle
radius2 = float(input("Enter the radius of a circle: "))
area = (math.pi)*pow(radius2,2)
print(f"The area of a circle is = {area}")
print(f"The area of a circle is = {round(area, 2)}cm^2")

#Find the hypotenus of a right triangle
a = float(input("Enter the side a of a right triangle: "))
b = float(input("Enter the side b of a right triangle: "))
c = math.sqrt(pow(a, 2)+pow(b, 2))
print(f"The c side of a right angle rectangle is = {round(c)}")