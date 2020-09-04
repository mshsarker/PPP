## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

##  031 Ask the user to enter the radius of a circle (measurement from the centre point to the edge). Work out the area of the circle (π*radius2).

import math


radius = int(input("Please enter the radius of a circle\n"))
area = math.pi * (radius ** 2)
print(f"Total area of the radius {radius} is {round(area,2)}")