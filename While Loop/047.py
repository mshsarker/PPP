## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 047 Ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they want to add another number. If they enter “y", ask them to enter another number and keep adding numbers until they do not answer “y”. Once the loop has stopped, display the total.


num1 = float(input("Please enter a number\n"))
num2 = float(input("Please enter another one\n"))
total = num1 + num2
yes = input("Do you want add another number? If yes then write 'y' \n")

while yes == 'y':
	num = float(input("Okkay! Then please enter another number\n"))
	total = total + num
	yes = input("Do you want add another number? If yes then write 'y' \n")

print(f"So!! Your total is {total}")























