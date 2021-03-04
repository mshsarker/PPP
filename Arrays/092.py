# 092 Create two arrays (one containing three numbers that the user enters and one containing a set of five random numbers). Join these two arrays together into one large array. Sort this large array and display it so that each number appears on a separate line.

from array import *
import random

user_array = array('i', [])
rand_array = array('i', [])

for i in range(0,3):
	new_value = int(input(" Please enter an integer:	"))
	user_array.append(new_value)

for i in range(0,5):
	new_value = random.randint(1,100)
	rand_array.append(new_value)

user_array.extend(rand_array)
arranged = sorted(user_array)

for i in arranged:
	print(i)



