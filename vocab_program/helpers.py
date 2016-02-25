import os
import json
import sys
import random 
import time

filename = "db.json"

def init():
	"""Initialize Database"""

	if os.path.isfile(filename) != True:
		db = open(filename, 'w').close()
	else:
		db = open(filename, 'r')
		try:
			content = json.load(db)
		except ValueError:
			content = []
	return content

def callback(func):
	time.sleep(0.2)
	res = input('\nWould you like to try again? [y]es or [n]o\n\t=>').lower()
	if res == 'n' or res == 'no':
		return
	elif res == 'y' or res == 'yes':
		func()
	else:
		callback(func)


def add():
	"""Appends words to dictionary."""

	content = init()

	key = input('\nWhat is your term?\n\t=>')
	definition = input('\nWhat is your definition?\n\t=>')

	content.append({'key':key, 'definition': definition})

	db = open(filename, 'w')

	json.dump(content, db)
	db.close()
	callback(add)


def view():
	"""View your dictionary"""

	content = init()
	index = 1

	if len(content) == 0:
		print('\nYou have no words. Add more.')

	for i in content:
		key = i['key']
		definition = i['definition']
		print('{}. {}: {}\n'.format(index, key, definition))
		index += 1
	callback(view)


def delete():
	"""Remove a word from your dictionary."""

	content = init()
	newContent = []

	print('\n\tWord Choices (Case Sensitive):')

	for word in content:
		print('\n\t{}'.format(word['key']))

	wordToDel = input('\n\tWhat word do you want to delete?\n\t\t=>')

	validList = []
	vCount = 0
	for word in content:
		validList.append(word['key'])
	for key in validList:
		print('\n\tScanning..')
		time.sleep(0.1)
		vCount += 1
		if key != wordToDel and vCount < len(validList):
			continue
		elif key == wordToDel:
			print('\n\tFound. Deleting..')
			time.sleep(1)
			print('\n\t\tSuccess!')
			break
		else:
			print("\nInvalid Input.")
			delete()

	for i in content:
		if i['key'] != wordToDel:
			newContent.append(i)

	db = open(filename, 'w')
	json.dump(newContent, db)
	db.close()

	callback(delete)

def destroy():
	"""Wipes dictionary clear of anything"""

	open(filename, 'w').close()

def menu():
	"""Menu Function"""

	def run(func):
		"""Calls functions"""

		func()
		menu()

	print('\n\t\tYour Personal dictionary!')

	choice = input("\nDo you want to 'view', 'add', 'delete', or 'destroy'? Enter 'x' to exit.\n\t=>").lower()

	if choice == 'view':
		run(view)
	elif choice == 'add':
		run(add)
	elif choice == 'delete':
		run(delete)
	elif choice == 'destroy':
		run(destroy)
	elif choice == 'x':
		raise SystemExit
	else:
		print('\n\tInvalid input.')
		menu()