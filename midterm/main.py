import games
import helpers

def menu():
	"""Menu Function"""

	def run(func):
		"""Calls functions"""

		func()
		menu()

	print('\n\t\tYour Personal dictionary!')

	choice = input("\nDo you want to 'view', 'add', 'delete', 'game', or 'destroy'? Enter 'x' to exit.\n\t=>").lower()

	if choice == 'view':
		run(helpers.view)
	elif choice == 'add':
		run(helpers.add)
	elif choice == 'delete':
		run(helpers.delete)
	elif choice == 'destroy':
		run(helpers.destroy)
	elif choice == 'game':
		run(games.menu)
	elif choice == 'x':
		raise SystemExit
	else:
		print('\n\tInvalid input.')
		menu()