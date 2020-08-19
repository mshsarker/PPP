## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book 

# 016 Ask the user if it is raining and convert their answer to lower case so it doesn’t matter what case they type it in. If they answer “yes”, ask if it is windy. If they answer “yes” to this second question, display the answer “It is too windy for an umbrella”, otherwise display the message “Take an umbrella”. If they did not answer yes to the first question, display the answer “Enjoy your day”.
raining = input("Is it raining outside?\n")

if raining.lower() == "no":
	print("Enjoy your day")
else:
	windy = input("Is it windy outside?\n")
	if windy.lower() == 'no':
		print("Take an umbrella")
	else:
		print("It is too windy for an umbrella")