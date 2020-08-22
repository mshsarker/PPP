## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book 

# 019 Ask the user to enter 1, 2 or 3. If they enter a 1, display the message “Thank you”, if they enter a 2, display “Well done”, if they enter a 3, display “Correct”. If they enter anything else, display “Error message”.

num = int(input("Please enter 1, 2 or 3\n"))

if num == 1:
	print("Thank you")
elif num ==2:
	print("Well Done")
elif num == 3:
	print("Correct")
else:
	print("Error message")