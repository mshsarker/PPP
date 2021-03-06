# 093 Ask the user to enter five numbers. Sort them into order and present them to the user. Ask them to select one of the numbers. Remove it from the original array and save it in a new array.
 
from array import *


user_array = array('i', [])

for i in range(0,5):
	new = int(input("Please enter an integer number:	"))
	user_array.append(new)

user_array_ordered = sorted(user_array)

for i in user_array_ordered:
	print(i)

rmv = int(input("Please enter a number from here to remove it:	"))
user_array.remove(rmv)
print(user_array)


