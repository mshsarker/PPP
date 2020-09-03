## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

##  029 Ask the user to enter an integer that is over 500. Work out the square root of that number and display it to two decimal places.

import math

num = int(input("Please enter an integer that is over 500\n"))
sqrt = math.sqrt(num)
answer = round(sqrt, 2)
print(f"Square root of {num} is {answer} ")