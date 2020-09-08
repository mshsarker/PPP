## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 036 Alter program 035 so that it will ask the user to enter their name and a number and then display their name that number of times.

name = input("Please enter your name \n")
times = int(input("Please type an integer \n"))

for i in range(0,times):
	print(name)