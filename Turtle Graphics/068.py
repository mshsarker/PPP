## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

##  068 Draw a pattern that will change each time the program is run. Use the random function to pick the number of lines, the length of each line and the angle of each turn.
 
import random
import turtle 


turtle.pensize(3)
line = random.randrange(5,20)
length = random.randrange(25,100,5)
angle = random.randrange(10,180)
clr = random.choice(["red", 'black', 'green', 'purple', 'blue', 'yellow'])



for i in range(0,line):
	turtle.color(clr, 'red')
	turtle.right(angle)
	turtle.forward(length)
	


turtle.exitonclick()