## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 039 Ask the user to enter a number between 1 and 12 and then display the times table for that number.

num = int(input("Please write down a number between 1 and 12\n"))

for i in range(1,11):
	print(f"{num} * {i} = {num * i} ")