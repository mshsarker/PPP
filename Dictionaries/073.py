## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

##  073 Ask the user to enter four of their favourite foods and store them in a dictionary so that they are indexed with numbers starting from 1. Display the dictionary in full, showing the index number and the item. Ask them which they want to get rid of and remove it from the list. Sort the remaining data and display the dictionary

foods ={}
foods[1] = input("What are your favorite foods? First one?  ")
foods[2] = input("What are your favorite foods? Another one?  ")
foods[3] = input("What are your favorite foods? Third one?  ")
foods[4] = input("What are your favorite foods? Last one?  ")
print(f"Here is the list of the selected food  :::  {foods}" )


takeoff = int(input("Which no. of food , do you want to take off from the list :   "))
del foods[1]
print(f"Now the selected food as sorted as {sorted(foods.values())}")

