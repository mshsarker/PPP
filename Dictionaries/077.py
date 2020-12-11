## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

##  077 Change program 076 so that once the user has completed their list of names, display the full list and ask them to type in one of the names on the list. Display the position of that name in the list. Ask the user if they still want that person to come to the party. If they answer “no”, delete that entry from the list and display the list again.

names_list = []
names_list.append(input("Add a name to your list   "))
names_list.append(input("Add another name to your list   "))
names_list.append(input("Add third name to your list  "))

adding = input("Do you want to add another name into the list? Write 'y' if you want..    ")
while adding == 'y':
	names_list.append(input("Add another name to your name list:	"))
	adding = input("Do you want to add another name into the list? Write 'y' if you want..    ")

print(f"List of invited people are : {names_list}")

ignore = input("select a name from the list:	")
print(f"{ignore} is the {names_list.index(ignore)+1}th member of the list")

del_ignore = input(f"Do you still want {ignore} in your party? If yes or no(write y/n):		")

if del_ignore == 'y':
	print("You made a great decision")
else:
	names_list.remove(ignore)
	print(f"Updated list of members looks like this: {names_list}")
