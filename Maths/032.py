## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

##  032 Ask for the radius and the depth of a cylinder and work out the total volume (circle area*depth) rounded to three decimal places.

import math


radius = int(input("Please enter the radius of a circle\n"))
depth = int(input("What is the depth of your cylinder?\n"))

area = math.pi * (radius ** 2)
depth = area * depth

print(f"Total depth of the cylinder is {round(depth,3)}")