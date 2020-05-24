import random as rd
from MainClass.DeckDict import deck_dict as dd

class Decks():
	'''
	Build and store information of the deck
	'''
	def __init__(self):
	#Construct a deck of 52 cards
		deck = dd.deck_info()
		self.deck = list(deck.keys())

	def shuffle(self):
	#Shuffle the deck
		rd.shuffle(self.deck)

	def draw(self):
	#Draw the top card of the deck and omit that card out of the deck
		drawn_card = self.deck[0]
		self.deck.pop(0)
		return drawn_card

class Player():
	'''
	Create a class containing information from each player
	'''
	def __init__(self):
		self.card_bank = []
		self.score = 0

	def set_avail_money(self, avail_money):
	#Set the available money of player
		self.avail_money = avail_money

	def make_bet(self, bet):
	#Player makes bet
		self.bet = bet
		while True:
			if self.bet <= self.avail_money:
				self.avail_money = self.avail_money - self.bet
				print('You bet {} '.format(self.bet))
				print('You have {} left'.format(self.avail_money))
				break
			else: 
				self.bet = int(input('Your bet exceeds your available money. Please choose again: '))

	def draw_card(self, card):
	#Player draws cards
		self.card_bank.append(card)

	def calc_score(self):
	#Calculate player's score based on cards
		if len(self.card_bank) <= 2:
		#The first turn
			for card in self.card_bank:
				if '1_' in card:
				#Ask player to choose their desired value of Ace card
					card_value = input('You have picked an Ace card. Please choose your value of the Ace card (1 or 11): ')
					#Check if player enters the right number:
					while True:
						if card_value == '1' or card_value == '11':
							break
						else:
							card_value = input('You have to choose 1 or 11. Please choose again: ')
					self.score = self.score + int(card_value)
				else:
					self.score = self.score + dd.deck_info()[card]
		else:
		#Second turn and later
			if '1_' in self.card_bank[len(self.card_bank) - 1]:
				#Ask player to choose their desired value of Ace card
				card_value = int(input('You have picked an Ace card. Please choose your value of the Ace card (1 or 11): '))
				#Check if player enters the right number:
				while True:
					if card_value == 1 or card_value == 11:
						break
					else:
						card_value = int(input('You have to choose 1 or 11. Please choose again: '))
				self.score = self.score + card_value
			else:
				self.score = self.score + dd.deck_info()[self.card_bank[len(self.card_bank) - 1]]
		return self.score

class ComputerDealer(Player):
	'''
	Subclass Computer dealer
	'''
	def show_card(self):
	#Show only one card of the computer dealer
		if '1_' in self.card_bank[0]:
			shown_card = self.card_bank[0]
		if '1_' in self.card_bank[1]:
			shown_card = self.card_bank[1]
		else:
			shown_card = self.card_bank[0]
		print("The computer dealer's card is {}. Another card is covered.".format(shown_card))

	def show_all(self):
	#Show all cards of the computer dealer
		print("The computer dealer's cards are: ", end = '')
		for _ in range(len(self.card_bank)):
			if _ == len(self.card_bank) - 1:
				print(self.card_bank[_])
			else:
				print(self.card_bank[_], end = ', ')


class HumanPlayer(Player):
	'''
	Subclass Human player
	'''
	def show_card(self):
	#Show only one card of the player
		print("The player's cards are: ", end = '')
		for _ in range(len(self.card_bank)):
			if _ == len(self.card_bank) - 1:
				print(self.card_bank[_])
			else:
				print(self.card_bank[_], end = ', ')

	def show_avail_money(self):
	#Show the money of the player
		print('Player currently has {}'.format(self.avail_money))

