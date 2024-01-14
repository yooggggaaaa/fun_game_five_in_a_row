from unittest.mock import patch
from five_in_a_row import Player, Board

import unittest

class TestBoard(unittest.TestCase):
    # set up the test, create the board to be tested
    def setUp(self):
        self.board = Board(10,10)
        self.board_small = Board(2,2)
       
    def test_in_boundry_check(self):
        self.assertTrue(self.board.in_boundry_check(5,5))
        self.assertFalse(self.board.in_boundry_check(11,11))

    def test_check_if_location_occupied(self):
        self.board.place_chess_at_position(5,5, "B")
        self.assertTrue(self.board.check_if_location_occupied(5,5))
        self.assertFalse(self.board.check_if_location_occupied(5,4))
    
    def test_set_color(self):
        self.board.set_color(5,5, "B")
        self.board.set_color(9,9, "B")
        self.assertEqual(self.board.get_position_color(5,5), "B")
        self.assertEqual(self.board.get_position_color(9,9), "B")
    
    def test_check_if_win(self):
        # check five in a row 
        self.board.place_chess_at_position(0,0, "W")
        self.board.place_chess_at_position(0,1, "W")
        self.board.place_chess_at_position(0,2, "W")
        self.board.place_chess_at_position(0,3, "W")
        self.assertFalse(self.board.check_if_win(0,3))
        self.board.place_chess_at_position(0,4, "W")
        self.assertTrue(self.board.check_if_win(0,3))
        self.assertTrue(self.board.check_if_win(0,4))
        self.assertFalse(self.board.check_if_win(0,6))
        self.assertFalse(self.board.check_if_win(9,9))

        # check five in a col
        self.board.place_chess_at_position(1,0, "B")
        self.board.place_chess_at_position(2,0, "B")
        self.board.place_chess_at_position(3,0, "B")
        self.board.place_chess_at_position(4,0, "B")
        self.assertFalse(self.board.check_if_win(3,0))
        self.board.place_chess_at_position(5,0, "B")
        self.assertTrue(self.board.check_if_win(1,0))
        self.assertTrue(self.board.check_if_win(4,0))
        self.assertTrue(self.board.check_if_win(5,0))
        self.assertFalse(self.board.check_if_win(6,0))

    def test_board_full(self):
        self.board_small.place_chess_at_position(0,0, "B")
        self.board_small.place_chess_at_position(0,1, "B")
        self.assertFalse(self.board.board_full(0,1))
        self.board_small.place_chess_at_position(1,0, "W")
        self.board_small.place_chess_at_position(1,1, "W")
        self.assertFalse(self.board.board_full(1,1))
   
class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_one = Player("Black")
        self.player_two = Player("White")

    def test_get_player_color(self):
        self.assertEqual(self.player_one.get_player_color(), "Black")
        self.assertEqual(self.player_two.get_player_color(), "White")

    @patch('builtins.input', side_effect=['2,3'])
    def test_generate_next_move(self, prompt):
        result = self.player_one.generate_next_move('Enter row and column: ')
        self.assertEqual(result, (2, 3))

    @patch('builtins.input', side_effect=['3,4'])
    def test_generate_next_move_invalid_then_valid_input(self, prompt):
        result = self.player_two.generate_next_move('Enter row and column: ')
        self.assertEqual(result, (3, 4))

if __name__ == '__main__':
    unittest.main()