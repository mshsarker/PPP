#   085 Ask the user to type in their name and then tell them how many vowels are in their name.

name = input("Please write down your name:	")

count = 0
vowel = ['a', 'e', 'i', 'o', 'u']

for i in name.lower():
	if i in  vowel:
		count += 1

print(f"Your name has {count} vowels")


