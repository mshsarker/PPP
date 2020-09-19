## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 048 Ask for the name of somebody the user wants to invite to a party. After this, display the message “[name] has now been invited” and add 1 to the count. Then ask if they want to invite somebody else. Keep repeating this until they no longer want to invite anyone else to the party and then display how many people they have coming to the party.

name = input("Write down a name of somebody that you want to invite in your party \n")
anyone = input("Do you want to invite anybody else ? Write 'y' if you want.\n" )
count = 1

while anyone == 'y':
	name = input("Okkay!! Then please, write down another name of somebody that you want to invite in your party \n")
	count += 1
	anyone = input("Do you want to invite anybody else ? Write 'y' if you want.\n" )

print(f"So, {count} people are coming to the party ")


















