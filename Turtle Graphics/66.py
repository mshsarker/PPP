## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

##  066 Draw an octagon that uses a different colour (randomly selected from a list of six possible colours) for each line.

import random
import turtle 


turtle.pensize(3)


for i in range(0,8):
	clr = random.choice(["red", 'black', 'green', 'purple', 'blue', 'yellow'])
	turtle.color(clr, 'red')
	turtle.right(45)
	turtle.forward(100)
	


turtle.exitonclick()