class Card:
	def __init__(self, value, suit):   
		self.value = value
		self.suit = suit
	def __repr__(self):
		#return "{} of {}".format(self.value, self.suit)
 		return f"{self.value} of {self.suit}"

class Deck:
	def __init__(self):
		suites = ["Hearts", "Diamonds", "Clubs", "Spades"]
		values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
		self.cards = [Card(value, suit) for suit in suites for value in values]
		#List comprehension Method put codes inside self.cards

		#Traditional method should empty inside self.cards and then do the following
		# for suit in suites:
		# 	for value in values:
		# 		self.cards.append(Card(value, suit))
		print(self.cards)

	def __repr__(self):
		return f"Deck of {self.count()} cards"

	def count(self):
		return len(self.cards)

	def _deal(self, num):
		count = self.count() 
		actual = min([count, num])
		print(f"Going to remove {actual} cards")
		if count == 0:
			reaise ValueError("All Cards have been dealt")

d =  Deck()
print(d._deal(54))
print(d)
# c = Card("hearts", "A")
# print(c)
# print(c.suit)
 
