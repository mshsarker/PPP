##This program check if there is any python keyword presents in our list provided.

import keyword

def contains_keyword(*args):
	return any(arg for arg in args if keyword.iskeyword(arg))


print(contains_keyword("Noyon", "Hypnotic eye"))#False
print(contains_keyword("for", "if", "nothing"))#True

