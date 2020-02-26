import pyfiglet
from termcolor import colored
#In thif exercise we are going to use pyfiglet to create asci art. It is fun!!!

def print_art(text, color):
	default_colors = ('grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan','white')
	if color not in default_colors:
		color = 'red'

	art = pyfiglet.figlet_format(text)
	colorful_art = colored(art, color = color)
	print(colorful_art)




text = input("What do you want to print?")
color = input("For that reason what color do you want to use?")
print_art(text,color)
