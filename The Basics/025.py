## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

##  025 Ask the user to enter their first name. If the length of their first name is under five characters, ask them to enter their surname and join them together (without a space) and display the name in upper case. If the length of the first name is five or more characters, display their first name in lower case.
first = input("What is your first name\n")
if len(first) < 5:
	last = input("What is your last name\n")
	name = first+last
	print(name.upper())
else:
	print(first.lower())
