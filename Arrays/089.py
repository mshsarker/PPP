#  089 Create an array which will store a list of integers. Generate five random numbers and store them in the array. Display the array (showing each item on a separate line).

from array import *
import random


newArray = array('i', [])
for i in range(0,5):
	num = random.randint(0,100)
	newArray.append(num)

print(newArray)
for x in newArray:
	print(x)