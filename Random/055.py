## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 055 Randomly choose a number between 1 and 5. Ask the user to pick a number. If they guess correctly, display the message “Well done”, otherwise tell them if they are too high or too low and ask them to pick a second number. If they guess correctly on their second guess, display “Correct”, otherwise display “You lose”.
import random

num = random.randint(1,6)
user = int(input("Choose a number between 1 to 5\n"))

if num == user:
	print("Well Done")
elif num > user:
	user = int(input("Too low! Give another try: \n"))
	if num == user:
		print("Well Done")
	else:
		print("You loose")
else:
	user = int(input("Too High! Give another try: \n"))
	if num == user:
		print("Well Done")
	else:
		print("You loose")