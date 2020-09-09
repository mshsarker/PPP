## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 042 Set a variable called total to 0. Ask the user to enter five numbers and after each input ask them if they want that number included. If they do, then add the number to the total. If they do not want it included, don’t add it to the total. After they have entered all five numbers, display the total.

total = 0

print("We are going to ask you 5 integers in the total and a choice")

num1 = int(input("First number : "))
decision1 = input("Do you want this number to be included to the total? (type : y or n)\n")
if decision1 == 'y':
	total += num1

num2 = int(input("Second number : "))
decision2 = input("Do you want this number to be included to the total? (type : y or n)\n")
if decision2 == 'y':
	total += num2

num3 = int(input("Third number : "))
decision3 = input("Do you want this number to be included to the total? (type : y or n)\n")
if decision3 == 'y':
	total += num3

num4 = int(input("Fourth number : "))
decision4 = input("Do you want this number to be included to the total? (type : y or n)\n")
if decision4 == 'y':
	total += num4

num5 = int(input("Fifth number : "))
decision5 = input("Do you want this number to be included to the total? (type : y or n)\n")
if decision5 == 'y':
	total += num5


print(f"Sum of your selected number is : {total}")


##### By using for loop
total = 0
print("We are going to ask you 5 integers in the total and a choice")

for i in range(0,5):
	num = int(input("number  : "))
	decision = input("Do you want this number to be included to the total? (type : y or n)\n")
	if decision == 'y':
		total += num

print(f"Sum of your selected number is : {total}")

































