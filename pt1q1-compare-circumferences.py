from math import *

diameter_1 = int(input("Please enter first diameter: "))
diameter_2 = int(input("Please enter second diameter: "))

if pi * diameter_1 == pi * diameter_2:
	print("Circumferences are equal")
elif pi * diameter_1 > pi * diameter_2:
	print("The first circle has a greater circumference")
else:
	print("The second circle has a greater circumference")