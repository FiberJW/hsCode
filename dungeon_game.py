# Escape the dungeon
# find your way out without getting eaten
import random

CELLS = [(0,0), (0,1), (0,2),
		 (1,0), (1,1), (1,2),
		 (2,0), (2,1), (2,2)]

def get_locations():
	monster = random.choice(CELLS)
	door = random.choice(CELLS)
	player = random.choice(CELLS)

	if monster == door or monster == player or door == player:
		return get_locations()

	return monster, door, player

def move_player(player, move):
	x, y = player
	if move == 'LEFT':
		y -= 1
	elif move == 'RIGHT':
		y += 1
	elif move == 'UP':
		x -= 1
	elif move == 'DOWN':
		x += 1

	return x, y

def draw_map(player):
	print(' _ _ _')
	tile = '|{}'
	for index, cell in enumerate(CELLS):
		if index in [0,1,3,4,6,7]:
			if cell == player:
				print(tile.format("X"), end='')
			else:
				print(tile.format("_"), end='')
		else: 
			if cell == player:
				print(tile.format("X|"))
			else:
				print(tile.format('_|'))

def get_moves(player):
	moves = ['LEFT', 'RIGHT', 'UP', "DOWN"]
	
	if player[1] == 0:
		moves.remove('LEFT')
	if player[0] == 0:
		moves.remove('UP')
	if player[1] == 2:
		moves.remove('RIGHT')
	if player[0] == 2:
		moves.remove('DOWN')

	return moves

monster, door, player = get_locations()
print('Welcome to the dungeon!\n')
print('Find the door to escape the Man-Eating Grue!\n')

while True:
	moves = get_moves(player)
	print("You're currently in room {}\n".format(player)) # Fill in with player position
	draw_map(player)
	print("You can move {}\n".format(moves)) # Fill w/ available moves
	print("Enter QUIT to quit\n")

	move = input('=>')
	move = move.upper()

	if move == 'QUIT':
		break

	if move in moves:
		player = move_player(player, move)
	else:
		try: 
			type(int(move))
			if type(int(move)) is int:
				print('\n** Enter a valid move **\n') 
				continue
		except:
			print('\n** Enter a valid move **\n') 
			continue
		print("** Walls are hard, stop walking into them! **")
		continue

	if player == door:
		print("You escaped!")
		input('Press the enter key to exit\n\t=>')
		break
	elif player == monster:
		print("You were eaten by the grue!")
		input('Press the enter key to exit\n\t=>')
		break
	