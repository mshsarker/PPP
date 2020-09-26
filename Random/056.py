## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 056 Randomly pick a whole number between 1 and 10. Ask the user to enter a number and keep entering numbers until they enter the number that was randomly picked.

import random


num = random.randint(1,11)
guess = int(input("Please pick a number in between 1 to 10\n"))
attempt = 1

while num != guess:
	attempt += 1
	guess = int(input("Wronggggg!!! Give another shot. Pick a number in between 1 to 10\n"))

print(f"You got in right on attemp no. {attempt}")