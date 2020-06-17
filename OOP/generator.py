def up_to_max(max):
	count = 1
	while count <= max:
		yield count
		count += 1

counter = up_to_max(5)

print(next(counter))


ß
'''
