## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 050 Ask the user to enter a number between 10 and 20. If they enter a value under 10, display the message “Too low” and ask them to try again. If they enter a value above 20, display the message “Too high” and ask them to try again. Keep repeating this until they enter a value that is between 10 and 20 and then display the message “Thank you”.
num = int(input("Please enter an integer \n"))

while num > 20 or num < 10:
 if num > 20:
 	print("Too high")
 else :
 	print("Too low")
 num = int(input("Please enter another integer \n"))

print("Thank you")















