import helpers
import time
import random
import main
import operator

def def_first():
	"""Game for matching word to definiton"""
	content = helpers.init()
	print('\nYou can exit at anytime by entering \'menu\'.\n') 
	random.shuffle(content)
	count = len(content)
	correct = 0
	incorrect = 0
	for word in content:
		print('\n{}. {}'.format(operator.indexOf(content, word) + 1, word['definition']))
		res = input('\nWhat word does this definition belong to?\n\t=>').lower()

		if res == word['key'].lower():
			count -= 1
			correct += 1
			if count > 0:
				print('\nGood Job! next word!')		
		elif res == 'menu':
			main.menu()
		else:
			incorrect += 1
			count -= 1
			if count > 1:
				print('\nIncorrect. Next word.')
				
	print('\nYou got {} correct and {} incorrect'.format(correct, incorrect))
	helpers.callback(def_first)


def scrambled():
	"""Unscramble the word"""

	content = helpers.init()
	print('\nYou can exit at anytime by entering \'menu\'.\n')

	random.shuffle(content)
	count = len(content)
	correct = 0
	incorrect = 0
	i = 0
	shuffled = []

	for word in content:
		to_scramble = list(word['key'].lower().strip())
		random.shuffle(to_scramble)
		shuffled.append(to_scramble)

	for scr in shuffled:
		res = input('\n{}. {}.\n\t=>'.format(i + 1, ''.join(scr))).lower()

		if res == content[i]['key'].lower():
			count -= 1
			correct += 1
			if count > 0:
				print('\nGood Job! next word!')		
		elif res == 'menu':
			main.menu()
		else:
			incorrect += 1
			count -= 1
			if count > 1:
				print('\nIncorrect. Next word.')
		i += 1
	print('\nYou got {} correct and {} incorrect'.format(correct, incorrect))
	helpers.callback(scrambled)


def menu():
	"""Menu Function"""

	def run(func):
		"""Calls functions"""

		func()
		menu()

	print('\n\t\tVocab Arcade!')


	choice = input("\nDo you want to play Guess the term (enter 'gtt') or Word Jumble (enter 'unscramble')? Enter 'x' to exit.\n\t=>").lower()
	if choice == 'gtt':
		run(def_first)
	elif choice == 'unscramble':
		run(scrambled)
	elif choice == 'x':
		return
	else:
		print('\n\tInvalid input.')
		menu()