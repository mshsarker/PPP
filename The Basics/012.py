## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book 

#  012 Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number, otherwise show the first number first and then the second.

num1 = int(input("Please write an interger \n"))
num2 = int(input("Please write another interger \n"))

if num1 > num2:
	print(f"The little number is {num2} and the big one {num1}")
else: 
	print(f"The little number is {num1} and the big one {num2}")