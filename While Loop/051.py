## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 051 Using the song “10 green bottles”, display the lines “There are [num] green bottles hanging on the wall, [num] green bottles hanging on the wall, and if 1 green bottle should accidentally fall”. Then ask the question “how many green bottles will be hanging on the wall?” If the user answers correctly, display the message “There will be [num] green bottles hanging on the wall”. If they answer incorrectly, display the message “No, try again” until they get it right. When the number of green bottles gets down to 0, display the message “There are no more green bottles hanging on the wall”.

num = 10
print(f"There are {num} green bottles hanging on the wall, {num} green bottles hanging on the wall, and if 1 green bottle should accidentally fall")


while  num > 0 and num <= 10:
	num -= 1
	guess = int(input("how many green bottles will be hanging on the wall?\n")) 
	if guess == num:
		print(f"There will be {guess} green bottles hanging on the wall")
		break
	elif num == 0:
		print("There are no more green bottles hanging on the wall")
	else:
		print("No try again")






 

 





