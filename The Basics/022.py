## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 022 Ask the user to enter their first name and surname in lower case. Change the case to title case and join them together. Display the finished result.

first = input("Write down your first name in lowere case\n")
last = input("Write down your last name in lower case\n")
name = first + " " + last
print(f"Thank you {name.title()}")