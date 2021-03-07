# 094 Display an array of five numbers. Ask the user to select one of the numbers. Once they have selected a number, display the position of that item in the array. If they enter something that is not in the array, ask them to try again until they select a relevant item.

from array import *

nums = array('i', [1,2,3,4,5])

for i in nums:
	print(i)

select = int(input("Select a number from the numbers that just displayed here:	"))
try_again = True

while try_again:
	if select in nums:
		ind = nums.index(select)
		print(f"Your chosen number has the position of {ind}")
		break
	else:
		print("You selected number doesnt exist")
		select = int(input("Select a number from the numbers that just displayed here:	"))