# 079 Create an empty list called “nums”. Ask the user to enter numbers. After each number is entered, add it to the end of the nums list and display the list. Once they have entered three numbers, ask them if they still want the last number they entered saved. If they say “no”, remove the last item from the list. Display the list of numbers.

nums = []

for i in range(0,3):
	x = int(input("Please enter an integer:		"))
	nums.append(x)
	print(nums)

decision = input("Do you still want the last that is entered into the list? (y/n)	")
if decision == 'n':
	nums.pop()
	print(f"Here is the updated list:	{nums}")

