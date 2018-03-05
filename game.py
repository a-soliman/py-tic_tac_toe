class TicTacToe:
	def __init__(self, player1='Player-1', player2='player-2'):
		self.player1 = { "name": player1, "simple": "X", "score": 0 }
		self.player2 = { "name": player2, "simple": "O", "score": 0 }
		self.board = [ " " for i in range(9)]
	
	



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