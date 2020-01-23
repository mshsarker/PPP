'''
sum_floats(1.5, 2.4, 'awesome', [], 1) # 3.9
sum_floats(1,2,3,4,5) # 0
'''
def sum_floats(*args):
    total = [f for f in args if type(f) == float]
    return sum(total)

print(sum_floats(1.5, 2.4,'awesome',[],1))


#def sum_floats(*args):
    #return sum(arg for arg in args if type(arg) == float)