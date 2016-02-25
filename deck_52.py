# Write a card game that shuffles a deck of 52 playing cards (4 of each card type),
# deals them to a specified number of players, then adds the players' cards values up.
# The number cards are each worth their face value, the face cards are worth the following:
# Jack = 11 pts
# Queen = 12 pts
# King = 13 pts
# Ace = 1 pt

import random

class CardGame:

	def __init__(self, num_players):
		self.num_players = num_players


	deck = []

	VALUES = {
		'Jack': 11,
		'Queen': 12,
		'King': 13,
		'Ace': 1
	}

	players = []

	CARD_NAMES = ['Jack', 'Queen', 'King', 'Ace']

	def populate_deck(self):
		for i in range(52):
			random.shuffle(self.CARD_NAMES)
			face = self.CARD_NAMES[0]
			value = self.VALUES[face]
			card = {face:value}
			self.deck.append(card)

	def split_deck(self):
		self.subdeck = []
		self.subdecks = []
		_i = 0

		for x in range(0, len(self.deck), 52 // self.num_players):
		    self.subdeck = self.deck[x:x+ 52 // self.num_players]
		    self.subdecks.append(self.subdeck)


	def init_players(self):
		for i in range(self.num_players):
			self.players.append({'Player {}'.format(i +1): None})


	def deal_cards(self):
		_i = 0

		for player in self.players:
			for key in player:
				player[key] = self.subdecks[_i]
				continue
			_i += 1

	def add_decks(self):
		total = 0
		for players in self.players: # Each player dict
			for player in players: # Each player name
				for cards in players[player]: # Each player's cards

					for face in cards: # Each card's value
						total += cards[face]
				players[player].append({'total': total})
				print(player,':', players[player][-1]['total'])
				total = 0
				continue




game = CardGame(4)
game.init_players()
game.populate_deck()
game.split_deck()
game.deal_cards()
game.add_decks()
