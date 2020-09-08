## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 038 Change program 037 to also ask for a number. Display their name (one letter at a time on each line) and repeat this for the number of times they entered.

name = input("Dude! What's your name again ?\n")
times = int(input("Please write down an integer\n"))

for x in range(0, times):
	for i in name:
		print(i)