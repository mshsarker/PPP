import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import choice


BASE_URL = "http://quotes.toscrape.com/"


def scrape_quotes():
	all_quotes = []
	url = "/page/1/"
	
	while url:
		response = requests.get(f"{BASE_URL}{url}")
		print(f"................NOW SCRAPING {BASE_URL}{url}............")
		soup = BeautifulSoup(response.text, "html.parser")
		quotes = soup.find_all(class_ = "quote")


		for quote in quotes:
			all_quotes.append({
			"text" : quote.find(class_ = "text").get_text(),
			"author": quote.find(class_ = "author").get_text(),
			"bio_link": quote.find("a")["href"]
				})


		next_btn = soup.find(class_ = "next")
		url = next_btn.find("a")["href"] if next_btn else None
		sleep(1)
	return all_quotes

# Writing quotes to CSV file
def write_quotes(quotes):
	with open("quotes.csv", "w") as file:
		headers = ["text", "author", "bio_link"]
		csv_writer = csv.DictWriter(file, fieldnames = headers)
		csv_writer.writeheader()
		for quote in quotes:
			csv_writer.writerow(quote)

quotes = scrape_quotes()
write_quotes(quotes)




def start_game(all_quotes):
	remaining_guesses = 4
	guess = ''
	quote = choice(all_quotes)
	print(" Here is a quote: ")
	print(quote['text'])
	print(quote['author'])

	while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
		guess = input(f"Who said that? \nReamining guesses {remaining_guesses}\n")

		if guess.lower() == quote['author'].lower():
			print("You got it right!")
			break

		remaining_guesses -= 1
		if remaining_guesses == 3:
			response = requests.get(f"{BASE_URL}{quote['bio_link']}")
			soup = BeautifulSoup(response.text, "html.parser")
			birth_date = soup.find(class_ = "author-born-date").get_text()
			birth_place = soup.find(class_ = "author-born-location").get_text()
			print(f"Here is a hint: Author was born on {birth_date} {birth_place}")
		elif remaining_guesses == 2:
			print(f"Here is a hint: The Author's first name starts with {quote['author'][0]}")
		elif remaining_guesses == 1:
			last_initial = quote["author"].split(" ")[1][0]
			print(f"Here is a hint: The Author's last name starts with {last_initial}")
		else:
			print(f"Sorry!!!! you are out of guesses. The answer was {quote['author']}")



	again = ''
	while again.lower() not in ('y', 'yes', 'n', 'no'):
		again = input("Would you like to play again (y/n)?")

	if again.lower() in ('yes', 'y'):
		return start_game(all_quotes)
	else:
		print("okay!! Good bye")
	
all_quotes = scrape_quotes()
start_game(all_quotes)   
