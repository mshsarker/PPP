import requests
from random import choice
import pyfiglet
import termcolor


header = pyfiglet.figlet_format("Dad__Joke ###")
header = termcolor.colored(header, color = 'green')
print(header)


user_input = input("What would you like to search for?")
url = 'http://www.icanhazdadjoke.com/search'
response = requests.get(
	url, 
	headers = {'Accept' : 'application/json'},
	params  = {'term' : user_input}
	).json()


num_jokes = response['total_jokes']
if num_jokes > 1:
	print(f'There are {num_jokes} jokes for {user_input}. Here is one of them: ')
	print(choice(response['results'])['joke'])
elif num_jokes == 1:
	print(f'There is only one joke about {num_jokes}')
	print(response['results'][0]['joke'])
else:
	print("There is no joke")





