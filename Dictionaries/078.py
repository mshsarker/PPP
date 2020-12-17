# 078 Create a list containing the titles of four TV programmes and display them on separate lines. Ask the user to enter another show and a position they want it inserted into the list. Display the list again, showing all five TV programmes in their new positions.


tv = ["Ittadi", "Mr. Bean", "Alif Laila", "Sindbad"]

for i in tv:
	print(i)

show = input("Add another of your favorite show in the list:	")
position = int(input("What position do you want to put that it: 	"))

tv.insert(position, show)
print(tv)