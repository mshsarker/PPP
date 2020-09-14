## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 043 Ask which direction the user wants to count (up or down). If they select up, then ask them for the top number and then count from 1 to that number. If they select down, ask them to enter a number below 20 and then count down from 20 to that number. If they entered something other than up or down, display the message “I don’t understand”.

way = input("How do you want to count? Upward or downward?\nWrite up for Upward and dow for Downward\n")


if way == 'up':
	num = int(input("Write down your top number \n"))
	count = 0
	for n in range(0, num):
		count += 1
		print(count)
elif way == 'dow':
	num = int(input("Write down a number below 20 \n"))
	for n in range(20, num-1, -1):
		print(n)
else:
	print("I don't understand”")































