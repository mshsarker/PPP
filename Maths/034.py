## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 034 Display the following message:
## 1) Square
## 2) Triangle
## Enter a Number
## If the user enters 1, then it should ask them for the length of one of its sides and display the area. If they select 2, it should ask for the base and height of the triangle and display the area. If they type in anything else, it should give them a suitable error message.

import math

print("What do you want to calculate: \n 1) SQUARE \n 2) TRIANGLE \n Enter 1 or 2")
selection = int(input())

if selection == 1:
	side = int(input("Please enter one side of your Square\n"))
	area = side ** 2
	print(f"The area of your square is {area}")
elif selection == 2:
	base = int(input("What is the base of your triangle? \n"))
	height = int(input("What is the height of your triangle\n"))
	area = 0.5 * base * height
	print(f"The area of your triangle is {area}")
else:
	print("Oh! You Rebel. Please follow the instruction as mentioned before.")
