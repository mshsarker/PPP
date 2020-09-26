## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

##  058 Make a maths quiz that asks five questions by randomly generating two whole numbers to make the question (e.g. [num1] + [num2]). Ask the user to enter the answer. If they get it right add a point to their score. At the end of the quiz, tell them how many they got correct out of five.

import random


correct = 0

for i in range(0,5):
	num1 = random.randint(1,20)
	num2 = random.randint(1,30)
	sum = int(input(f"What is the sum of {num1} and {num2} :	"))
	num = num2 + num1
	if sum == num: 
		correct += 1

print(f"You got in right at {correct} times")


