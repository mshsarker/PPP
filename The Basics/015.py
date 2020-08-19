## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book 

# 015 Ask the user to enter their favourite colour. If they enter “red”, “RED” or “Red” display the message “I like red too”, otherwise display the message “I don’t like [colour], I prefer red”.
color = input("What is your favourite color? \n")

if color.lower() == "red":
	print("Red is my favourite color too")
else:
	print(f"I don’t like {color}, i prefer Red")