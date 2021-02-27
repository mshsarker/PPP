# 091 Create an array which contains five numbers (two of which should be repeated). Display the whole array to the user. Ask the user to enter one of the numbers from the array and then display a message saying how many times that number appears in the list.

from array import *


nums = array('i', [1,2,2,3,4])

for i in nums:
	print(i)
num = int(input("Please select an integer from this list:	"))

times = nums.count(num)
print(f"Your selected number appears {times} times in the list")