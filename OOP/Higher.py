#Higher order functions by Colt Stelle
def sum(n, func):
	total = 0
	for num in range(1, n+1):
		total += func(num)
	return total

def square(x):
	return x*x

def cube(x):
	return x*x*x
print(sum(3, square))
print(sum(3, cube))

# input 1 2 3 
# result when square 1+4+9
# result when cube 1 + 8 + 27

