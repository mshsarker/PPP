## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 037 Ask the user to enter their name and display each letter in their name on a separate line.
name = input("Dude! What's your name ?\n")

for i in range(0, len(name)):
	print(name[i])


name = input("Dude! What's your name again ?\n")

for i in name:
	print(i)
