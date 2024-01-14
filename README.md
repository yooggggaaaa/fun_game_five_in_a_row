Gomoku (Five_in_a_row) in Python

Class Board:
Parameter: m, n - to set up chess board (traditionally it is 19 * 19)
Methods:
-	set_up_board(m, n)
-	place_at_board(r, c, chess_color)
-	in_boundry_check(r,c)
-	check_if_the_location_is_occupied
-	check_if_win

Class Player:
Parameter: chess_color
Method: 
-	generate_next_move(prompt) ) 
-	(promot: where do you want to put the next chess)

Class Game:
Parameter: player1, player2, board, current_player
Method:
-	run: keep a while loop --  two players play 

while loop steps:
-	player1 place, check if player 1 wins, if yes, end game
-	if not, player 2 place, check if player 2 wins, if yes end game 
-	if not, continue the loop
