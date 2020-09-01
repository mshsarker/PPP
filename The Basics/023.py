## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 023 Ask the user to type in the first line of a nursery rhyme and display the length of the string. Ask for a starting number and an ending number and then display just that section of the text (remember Python starts counting from 0 and not 1).

rhyme = input("Write down your favorite quote or rhyme from your elementary school\n")
print(f"It looks like your quote contains {len(rhyme)} characters")
start = int(input("Please type the starting point\n"))
end = int(input("Please type the ending point\n"))
print(rhyme[start:end])