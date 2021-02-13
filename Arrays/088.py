#  088 Ask the user for a list of five integers. Store them in an array. Sort the list and display it in reverse order.

from array import *

newArray = array('i',[])
for i in range(0,5):
	newvalue = int(input("Enter a new integer:	"))
	newArray.append(newvalue)

newArray = sorted(newArray)
newArray.reverse()
print(newArray)