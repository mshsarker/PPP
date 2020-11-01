## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

##  067 Create the following pattern:
 
import random
import turtle 


turtle.pensize(3)

for i in range(0,8):
	turtle.right(45)
	clr = random.choice(["red", 'black', 'green', 'purple', 'blue', 'yellow'])
	turtle.color(clr, 'red')
	for j in range(0,8):
		turtle.right(45)
		turtle.forward(100)
	


turtle.exitonclick()