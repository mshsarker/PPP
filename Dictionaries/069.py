## My solutions to the 150 Challenges by Nichola Lacey
## Get this wonderful book to know with the explanations and quick tips.

##  069 Create a tuple containing the names of five countries and display the whole tuple. Ask the user to enter one of the countries that have been shown to them and then display the index number (i.e. position in the list) of that item in the tuple.


countries = ("Bangladesh", "India", "USA", "China", "England")
print(countries)
position = input("Please select a country from this list:    ")
print(f"Position of the selected country in our tuple is {countries.index(position)}")