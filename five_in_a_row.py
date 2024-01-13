class Board:
    def __init__(self, m, n):
        # set up a board of m rows and n columns
        self.board = []
        for _ in range(m):
            row = []
            for _ in range(n):
                row.append(" ")
            self.board.append(row)
        
    '''
    print the board in m * n rows 
    '''
    def print_board(self):
        for row in self.board:
            print(row)

    # placing at (r,c) and check if its in the boundry of the board
    def in_boundry_check(self, r, c):
        if 0 <= r < len(self.board) and 0 <= c < len(self.board[0]):
            return True 
        return False 

    # placing at (r,c) and check if its already occupied by other player
    def check_if_location_occupied(self, r, c):
        if self.board[r][c] != " ":
            return True 
        return False

    def place_chess_at_position(self, r, c, player_color):
        self.set_color(r,c,player_color)
    
    def set_color(self, r, c, color):
        # print(color)
        
        self.board[r][c] = color

    # check if the player wins by placing the chess at location (r,c)
    def check_if_win(self, r, c):
        if self._check_if_five_in_a_col(r,c) or self._check_if_five_in_a_row(r,c) or self._check_if_five_in_a_diagonal_to_the_right(r,c) or self._check_if_five_in_a_diagonal_to_the_left(r,c):
            return True
        return False

    def _check_if_five_in_a_row(self, r, c):
        # check if there are 5 chesses with same color
        # check how many chesses are to the right and left of current chess
        count = 1
        right_c = c
        for i in range(1,5):
            right_c = c + i 
            if not self.in_boundry_check(r, right_c):
                break
            else: 
                if self.board[r][right_c] == self.board[r][c]:
                    count += 1
                    if count == 5:
                        return True
                else:
                    break

        # print(f"the current count for chesses is {count}") 
        left_c = c
        for i in range(1,5):
            left_c = c - i 
            if not self.in_boundry_check(r, left_c):
                break
            else: 
                if self.board[r][left_c] == self.board[r][c]:
                    count += 1 
                    if count == 5:
                        return True
                else:
                    break
        #print(f"counting left, the current count for chesses is {count}") 
        return False
                
    
    def _check_if_five_in_a_col(self, r, c):
        # check if there are 5 chesses with same color
        # check how many chesses are above and below the current chess
        count = 1
        r_up = r
        for i in range(1,5):
            r_up = r - i 
            if not self.in_boundry_check(r_up, c):
                break
            else: 
                if self.board[r_up][c] == self.board[r][c]:
                    count += 1
                    if count == 5:
                        return True
                else:
                    break

        r_down = c
        for i in range(1,5):
            r_down = r + i 
            if not self.in_boundry_check(r_down, c):
                break
            else:
                if self.board[r_down][c] == self.board[r][c]:
                    count += 1 
                    if count == 5:
                        return True
                else:
                    break
        return False


    def _check_if_five_in_a_diagonal_to_the_right(self, r, c):

        count = 1
        r_up = r
        c_left = c
        for i in range(1,5):
            r_up = r - i 
            c_left = c - i
            if not self.in_boundry_check(r_up, c_left):
                break
            else:
                if self.board[r_up][c_left] == self.board[r][c]:
                    count += 1
                    if count == 5:
                        return True
                else:
                    break

        r_down = r
        c_right = c
        for i in range(1,5):
            r_down = r + i 
            c_right = c + i

            if not self.in_boundry_check(r_down, c_right):
                break
            else:   
                if self.board[r_down][c_right] == self.board[r][c]:
                    count += 1 
                    if count == 5:
                        return True
                else:
                    break

        return False


    def _check_if_five_in_a_diagonal_to_the_left(self, r, c):
        count = 1
        r_up = r
        c_left = c
        for i in range(1,5):
            r_up = r - i 
            c_right = c + i
            if not self.in_boundry_check(r_up, c_right):
                break
            else:
                if self.board[r_up][c_right] == self.board[r][c]:
                    count += 1
                    if count == 5:
                        return True
                else:
                    break

        r_down = r
        c_left = c
        for i in range(1,5):
            r_down = r + i 
            c_left = c - i

            if not self.in_boundry_check(r_down, c_left):
                break
            else:   
                if self.board[r_down][c_left] == self.board[r][c]:
                    count += 1 
                    if count == 5:
                        return True
                else:
                    break

        return False

    def board_full(self, r,c):
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[r][c] == " ":
                    return False
        return True

class Player:
    def __init__(self, player_color):
        self.player_color = player_color
    
    def generate_next_move(self, prompt):
        while True:
        # ask the user the prompt question, input function returns userinput as a string
            user_input = input(prompt)
            input_values = user_input.split(",")

            if len(input_values) != 2:
                print("Input not valid, please enter a valid position in the format of 'row, col'.")
                continue 
        
            try:
                # try to cast the user's input into a tople
                r = int(input_values[0])
                c = int(input_values[1])
                break   # if we found value numbers, break out of the loop
                
            # catch error and print message
            except ValueError:
                print("Input not valid, please enter a valid position with numeric values.")
                continue

        return (r,c)
    
    # get player's color
    def get_player_color(self):
        return self.player_color
    
class Game:
    # will have board, and two players
    def __init__(self, board_row, board_col):
        self.board = Board(board_row, board_col) # create a board to play 
        self.player_one = Player("Black")  # create two players: black and white
        self.player_two = Player("White")
        self.current_player = None  # to define the player for each round
    
    def run(self):
        game_on = True 
        prompt = "Where do you want to place your chess? please put in this format: 2, 3. An integer followed by another integer: \n"
        self.current_player = self.player_one

        while game_on:
            
            while True:
                player_color = self.current_player.get_player_color()
                print()
                print(f"Hi, {player_color} player")
                print("The current board is: ")
                self.board.print_board()  # print the current board
                (r,c) = self.current_player.generate_next_move(prompt)

            # check if the current position is valid
                if self.board.in_boundry_check(r,c):
                    if not self.board.check_if_location_occupied(r,c):
                        break
                    else:
                        print("the position is occupied.")
                    
                else:
                    print("You have placed out of bountry. Please place again.")
                    print("game continues.")
                    print()
                     
            self.board.place_chess_at_position(r,c, player_color[0])
            print(f"The {player_color} player placed a chess at position {r}, {c}.")
            print() # print an empty line
            
            current_player_win = self.board.check_if_win(r,c)
            #print(f"The {player_color} player wins? : {current_player_win}.")
            if current_player_win:
                print(f"The {player_color} wins! Congratulations!")
                print(f"Game over. See you next time...")
                game_on = False
                break

            if self.board.board_full(r,c):
                print("Tie! no one wins.")
                break
            
            if self.current_player == self.player_one:
                self.current_player = self.player_two
            else:
                self.current_player = self.player_one

            
    def print_instructions(self):
        '''Prints welcome message and the rules of the game.
        '''
        print("Let's play five_in_a_row!")
        print("The game is played with 2 human players, ")
        print("The players' moves are decided by the user playing the game, by asking for input.")
        print("Let's go!!")
        print() # print an empty line

        
def main():
    game = Game(10,10)
    game.print_instructions()
    game.run()
    

# run main 
if __name__ == "__main__":
    main()


            

            
        








    


