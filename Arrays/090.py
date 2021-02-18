#  090 Ask the user to enter numbers. If they enter a number between 10 and 20, save it in the array, otherwise display the message “Outside the range”. Once five numbers have been successfully added, display the message “Thank you” and display the array with each item shown on a separate line.

from array import *


newArray = array('i', [])

while True:
	num = int(input('Hello User! Please enter an integer number:	'))
	if num >= 10 and num <=20:
		newArray.append(num)
	else:
		print("Outside the range")

	if len(newArray) == 5:
		print("Thank you")
		break

for n in newArray:
	print(n)