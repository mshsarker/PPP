## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book 

# 014 Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range, display the message “Thank you”, otherwise display the message “Incorrect answer”.
range = int(input("Please enter a number which is in between 10 and 20 \n"))

if range >= 10 and range <= 20:
	print("Thank you")
else:
	print("Incorrect number")