class TicTacToe:
	def __init__(self, player1='Player-1', player2='player-2'):
		self.player1 = { "name": player1, "simple": "X", "score": 0 }
		self.player2 = { "name": player2, "simple": "O", "score": 0 }
		self.board = [ " " for i in range(9)]
	
	def print_board(self):
		row1 = '| {} | {} | {} |'.format(self.board[0], self.board[1], self.board[2])
		row2 = '| {} | {} | {} |'.format(self.board[3], self.board[4], self.board[5])
		row3 = '| {} | {} | {} |'.format(self.board[6], self.board[7], self.board[8])

		print()
		print(row1)
		print(row2)
		print(row3)
		print()
	
	



# answer = input('Hey, would you like to play a game?: (y / n) ').lower()

# if answer == 'y':
# 	player1_name = input("Please enter player1's name:  ").strip().capitalize()
# 	player2_name = input("Please enter player2's name:  ").strip().capitalize()

	

# game = TicTacToe()

# if len(player1_name) > 0:
# 	game.player1["name"] = player1_name
# if len(player2_name) > 0:
# 	game.player2["name"] = player2_name

# game.start_game()