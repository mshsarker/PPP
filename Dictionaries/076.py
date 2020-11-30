## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

##  076 Ask the user to enter the names of three people they want to invite to a party and store them in a list. After they have entered all three names, ask them if they want to add another. If they do, allow them to add more names until they answer “no”. When they answer “no”, display how many people they have invited to the party.

names_list = []
names_list.append(input("Add a name to your list   "))
names_list.append(input("Add another name to your list   "))
names_list.append(input("Add third name to your list  "))

adding = input("Do you want to add another name into the list? Write 'y' if you want..    ")
while adding == 'y':
	names_list.append(input("Add another name to your list"))
	adding = input("Do you want to add another name into the list? Write 'y' if you want..    ")

print(f"List of invited people are : {names_list}")
