# 096 Create the following using a simple 2D list using the standard Python indexing:

simple_array = [[2,5,8], [3,7,4],[1,6,9],[4,2,0]]
print(simple_array)


# 097 Using the 2D list from program 096, ask the user to select a row and a column and display that value.
row = int(input("Hola Baby, please write me row number:	"))
column = int(input("And column number ? "))

print(simple_array[row][column])


# 098 Using the 2D list from program 096, ask the user which row they would like displayed and display just that row. Ask them to enter a new value and add it to the end of the row and display the row again.
