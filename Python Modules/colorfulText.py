from termcolor import colored 

# This built  in module will help to make colorful text and some other colorful stuff.


rongilaText = colored("Hello World! Welcome to Rongila text", color = 'red', 
	on_color = 'on_green', attrs =  ['blink'])

print(rongilaText)
