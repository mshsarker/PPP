## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 041 Ask the user to enter their name and a number. If the number is less than 10, then display their name that number of times; otherwise display the message “Too high” three times.

name = input("Dude! Whats your name? \n")
num = int(input("How many times? \n"))

if num < 10:
	for x in range(1, num+1):
		print(name)
else:
	print("Too High\n" * 3)