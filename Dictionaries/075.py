## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

##  075 Create a list of four three-digit numbers. Display the list to the user, showing each item from the list on a separate line. Ask the user to enter a three-digit number. If the number they have typed in matches one in the list, display the position of that number in the list, otherwise display the message “That is not in the list”.

listy = [111, 333, 444, 555, 666,777, 888, 999]

print("Here is the list of numbers. Please choose one from here:  ")
for l in listy:
	print(l)


match = int(input("Please choose one from here "))

if match in listy:
	print(f"Position of your selected number in the listy {listy.index(match)}")
else:
	print("That is not in the list")
