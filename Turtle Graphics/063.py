## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

## 063 Draw three squares in a row with a gap between each. Fill them using three different colours.

import turtle 


turtle.color("black","red")
turtle.begin_fill()
for i in range(0, 4):
	turtle.forward(100)
	turtle.right(90)
turtle.end_fill()
turtle.penup()


turtle.forward(120)
turtle.pendown()
turtle.color("black","green")
turtle.begin_fill()
for i in range(0, 4):
	turtle.forward(100)
	turtle.right(90)
turtle.end_fill()	
turtle.penup()


turtle.forward(120)
turtle.pendown()
turtle.color("black","blue")
turtle.begin_fill()
for i in range(0, 4):
	turtle.forward(100)
	turtle.right(90)
turtle.end_fill()


turtle.exitonclick()