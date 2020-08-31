## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

# 021 Ask the user to enter their first name and then ask them to enter their surname. Join them together with a space between and display the name and the length of whole name.

first = input("What is your First name?\n")
last = input("What is your last name?\n")
name = first + " "+last
length = len(name)
print(f"Hello!!! Your full name is {name} and it has {length} characters")