## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book 

# 018 Ask the user to enter a number. If it is under 10, display the message “Too low”, if their number is between 10 and 20, display “Correct”, otherwise display “Too high”.

num = float(input("Please enter a number as your heart desires. \n"))

if num < 10:
	print("Too low")
elif num >= 10 and num <= 20:
	print("Correct")
else:
	print("Too high")