# 083 Ask the user to type in a word in upper case. If they type it in lower case, ask them to try again. Keep repeating this until they type in a message all in uppercase.

msg = input("Type a word with an Uppercase:	")

while msg.islower():
	print("INCORRECT!!! Please try again.")
	msg = input("Type a word with an Uppercase:	")

print("You did it right. Thank you very much")



