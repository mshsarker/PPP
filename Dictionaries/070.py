## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

##  070 Create a tuple containing the names of five countries and display the whole tuple. Ask the user to enter one of the countries that have been shown to them and then display the index number (i.e. position in the list) of that item in the tuple. Add to program 069 to ask the user to enter a number and display the country in that position.

countries = ("Bangladesh", "India", "USA", "China", "England")
print(countries)
position = input("Please select a country from this list:    ")
print(f"Position of the selected country in our tuple is {countries.index(position)}")

ind = int(input("Enter a number between 1 to 5:  "))
print(f"Number of the selected country in our tuple is {countries[ind-1]}")