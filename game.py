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
	
	def start_game(self):
		self.reset_board()
		current_player = self.player1
		player1 = True

		print('Welcome to the game!')
		self.print_board()

		while True:
			if player1 == True:
				current_player = self.player1
			else:
				current_player = self.player2

			position = int(input(current_player["name"] + ', please choose your position from (1 to 9): '))
			
			if self.board[position -1] != ' ':
				position = int(input(current_player["name"] + ', please choose blank spot from (1 to 9): '))
		
			self.board[position -1] = current_player["simple"]
			
			# check if Even Game
			if self.check_status(current_player) == 'EVEN':
				self.print_board()
				print('Even Game!')
				break

			# check if Winner
			elif self.check_status(current_player):
				self.print_board()
				current_player["score"] = current_player["score"] + 1
				print('Congratulation! {} won!'.format(current_player["name"]))
				break
			
			if player1 == True:
				player1 = False
			else: 
				player1 = True
			
			self.print_board()
		
		self.print_score()

		replay = str(input('Would you like to play again? (y /n ): ')).lower()

		if replay == 'y':
			self.start_game()

	def check_status(self, player):
		
		#check horizontally
		simple = player["simple"]

		row1 = self.board[0:3:]
		row2 = self.board[3:6:]
		row3 = self.board[6::]
		col1 = [ self.board[0], self.board[3], self.board[6]]
		col2 = [ self.board[1], self.board[4], self.board[7]]
		col3 = [ self.board[2], self.board[5], self.board[8]]
		cross1 = [ self.board[0], self.board[4], self.board[8]]
		cross2 = [ self.board[2], self.board[4], self.board[6]]
		

		if (row1[0] == simple and row1[1] == simple and row1[2] == simple) or (row2[0] == simple and row2[1] == simple and row2[2] == simple) or (row3[0] == simple and row3[1] == simple and row3[2] == simple):
			return True
		
		if (col1[0] == simple and col1[1] == simple and col1[2] == simple) or (col2[0] == simple and col2[1] == simple and col2[2] == simple) or (col3[0] == simple and col3[1] == simple and col3[2] == simple):
			return True
		
		if (cross1[0] == simple and cross1[1] == simple and cross1[2] == simple) or (cross2[0] == simple and cross2[1] == simple and cross2[2] == simple):
			return True
		
		# check even
		for pos in self.board:
			if pos == ' ':
				return False
		return 'EVEN'
	
	def reset_board(self):
		self.board = [ " " for i in range(9) ]
	
	def print_score(self):
		print('{} => {}  VS. {} => {}'.format(self.player1["name"], self.player1["score"], self.player2["name"], self.player2["score"]))



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