## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 054 Randomly choose either heads or tails (“h” or “t”). Ask the user to make their choice. If their choice is the same as the randomly selected value, display the message “You win”, otherwise display “Bad luck”. At the end, tell the user if the computer selected heads or tails.

import random

hts = ['h', 't']
ht = random.choice(hts)
human = input("Choose either heads or tails ('h' or 't')\n")


if human == ht:
	print("You Win")
else:
	print("Bad luck")

print(f"Computer selected {ht}")

