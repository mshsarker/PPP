import keyword

def contains_keyword(*args):
	return any(arg for arg in args if keyword.iskeyword(arg))


print(contains_keyword("Noyon", "Hypnotic eye"))#False
print(contains_keyword("for", "if", "nothing"))#True

