## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 044 Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the names and after each name display “[name] has been invited”. If they enter a number which is 10 or higher, display the message “Too many people”.

quantity = int(input("How many people you want to invite into the party? \n"))

if quantity < 10:
	for i in range(0, quantity):
		guest = input("What is the name of the guest? \n")
		print(f"Congratulations! {guest} has been invited to the party.")
else:
	print("too many people")





























