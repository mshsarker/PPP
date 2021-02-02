#   086 Ask the user to enter a new password. Ask them to enter it again. If the two passwords match, display “Thank you”. If the letters are correct but in the wrong case, display the message “They must be in the same case”, otherwise display the message “Incorrect”.

password = input("Please enter your secret password:	")
password2 = input("Please type your password again:		")

if password == password2:
	print("Thank you")
elif password.lower() == password2.lower():
	print("They must be in the same case")
else:
	print("Incorrect")
