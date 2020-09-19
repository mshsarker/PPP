## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 049 Create a variable called compnum and set the value to 50. Ask the user to enter a number. While their guess is not the same as the compnum value, tell them if their guess is too low or too high and ask them to have another guess. If they enter the same value as compnum, display the message “Well done, you took [count] attempts”.

compnum = 50
count = 1
num = int(input("Guess a number that is in my mind\n"))

while num != 50:
	num = int(input("Enter another number\n"))
	count += 1
	if num < 50:
		print("Too low")
	elif num >50:
		print("Too High")

print(f'Well done!! You took {count} attempts')
















