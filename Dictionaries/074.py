## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

##  074 Enter a list of ten colours. Ask the user for a starting number between 0 and 4 and an end number between 5 and 9. Display the list for those colours between the start and end numbers the user input.

colors = ["Blue", "Black", "Green", "Red", "White", "Yellow", "Purple", "Magenta", "Sky Blue", "Gray"]
print(colors)
start = int(input("Please write a starting number (integer between 1 to 4) for this list of colors:   "))
end = int(input("Please write a ending number(integer between 5 to 9) for this list of colors:   "))
display = colors[start:end]
print(display)
