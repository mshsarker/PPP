## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

##  033 Ask the user to enter two numbers. Use whole number division to divide the first number by the second and also work out the remainder and display the answer in a user-friendly way (e.g. if they enter 7 and 2 display “7 divided by 2 is 3 with 1 remaining”).

import math


first = int(input("Please enter the first \n"))
second = int(input("Please enter another number\n"))

division = first // second
remain = first % second

print(f"{first} divided by {second} is {division} with {remain} remaining")