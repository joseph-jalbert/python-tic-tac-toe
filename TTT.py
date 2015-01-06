from __future__ import print_function

board = [[' ', ' ', ' '], 
		 [' ', ' ', ' '], 
		 [' ', ' ', ' ']]

def show(board):
	print()
	print()
	dashes = 1
	for line in board:
		print(' ' * 10, end='')
		bars = 1
		for space in line:
			print(space, end='')
			if bars < 3:
				print('|', end='') 
			bars += 1
		print()
		print(' ' * 10, end='')
		if dashes < 3:
			print('- - - ', end='')
		print()
		dashes += 1
	print()
	print()

show(board)

# track moves to determine whose turn it is

move_count = 1    

# check board for all end-game scenarios

while True:
	if (board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][2] != ' ') \
	or (board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][2] != ' ') \
	or (board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][2] != ' ') \
	or (board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[2][0] != ' ') \
	or (board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[2][1] != ' ') \
	or (board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[2][2] != ' ') \
	or (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != ' ') \
	or (board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[0][2] != ' '):
		  print()
		  print("{}s Win!!!!!!!!".format(player))
		  print()
		  show(board)
		  break
	elif board[0][0] != ' ' and board[0][1] != ' ' and board[0][2] != ' ' \
	and board[1][0] != ' ' and board[1][1] != ' ' and board[1][2] != ' ' \
	and board[2][0] != ' ' and board[2][1] != ' ' and board[2][2] != ' ':
		  print()
		  print("The game has ended in a draw")
		  print()
		  show(board)
		  break
	
	if move_count % 2 == 0:
		player = 'O'
	else:
		player = 'X'

	print()

	while True:
		try:
			column = int(raw_input("Player {} enter a column from 1-3:".format(player)))
			if not (1 <= column <= 3):
				raise ValueError()
			break
		except ValueError:
			print()
			print()
			print("You must select column 1, 2, or 3...")
			print()
			print()
	while True:		
		try:
			row = int(raw_input("Player {} enter a row from 1-3:".format(player)))
			if not (1 <= row <= 3):
				raise ValueError()
			break	
		except ValueError:
			print()
			print()
			print("You must select row 1, 2, or 3...")
			print()
			print()

	location = board[row-1][column-1]

	# ensure selected space is not already filled

	if not location == ' ':
		print()
		print()
		print("That space has already been filled in...")
		print()
		print()
	else:
		board[row-1][column-1] = player
		move_count += 1

	show(board)
	

	

























