#  087 Ask the user to type in a word and then display it backwards on separate lines. For instance, if they type in “Hello” it should display as shown below:

word = input("Plaease type a word	")
character = len(word)


for w in word:
	character -= 1
	print(word[character])