from unittest.mock import patch
from fun_game_five_in_a_row.five_in_a_row import Player, Board, Game

import unittest

class TestBoard(unittest.TestCase):
    # set up the test, we need to create the board to be tested
    def setUp(self):
        self.board = Board(10,10)
       
    def test_in_boundry_check(self):
        self.assertTrue(self.board.in_boundry_check(5,5))
        self.assertFalse(self.board.in_boundry_check(11,11))

    def test_check_if_location_occupied(self):
        self.board.place_chess_at_position(5,5, "B")
        self.assertTrue(self.board.check_if_location_occupied(5,5))
        self.assertFalse(self.board.check_if_location_occupied(5,4))


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