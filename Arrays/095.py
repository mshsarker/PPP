# 095 Create an array of five numbers between 10 and 100 which each have two decimal places. Ask the user to enter a whole number between 2 and 5. If they enter something outside of that range, display a suitable error message and ask them to try again until they enter a valid amount. Divide each of the numbers in the array by the number the user entered and display the answers shown to two decimal places.

from array import *
import random

num = array('f', [])
for i in range(0,5):
	num2 = random.randint(10,100)
	num.append(num2)

print(num)
# incomplete
