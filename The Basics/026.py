## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

##  026 Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an “ay”. If a word begins with a vowel you just add “way” to the end. For example, pig becomes igpay, banana becomes ananabay, and aadvark becomes aadvarkway. Create a program that will ask the user to enter a word and change it into Pig Latin. Make sure the new word is displayed in lower case.

print("Welcome to the world of PIG Latin. We are going to translate your word into pig latin")
word = input("Write down a word that your heart desires\n")

if word[0] in ('a', 'e', 'i', 'o', 'u'):
	vowel = word+ 'way'
	print(vowel.lower())
else:
	consonant = word[1:]+ word[0] + "ay"
	print(consonant.lower())