## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

##  057 Update program 056 so that it tells the user if they are too high or too low before they pick again.
import random


num = random.randint(1,11)
guess = int(input("Please pick a number in between 1 to 10\n"))
attempt = 1

while num != guess:
	attempt += 1
	if guess > num:
		guess = int(input("Too Higgghhhh!!! Give another shot. Pick a smaller number\n"))
	else:
		guess = int(input("Too Lowwww!!! Give another shot. Pick a bigger number\n"))

print(f"You got in right on attemp no. {attempt}")