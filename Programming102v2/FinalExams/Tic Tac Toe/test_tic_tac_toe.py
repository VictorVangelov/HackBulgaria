from tic_tac_toe import Tic_tac_toe
import unittest


class Test_TicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = Tic_tac_toe()
        self.user_mark = self.game.user_mark
        self.computer_mark = self.game.computer_mark

    def test_AI_win(self):
        self.game.make_move(self.user_mark, 1)
        self.game.make_move(self.user_mark, 2)
        block_move = self.game.get_computer_move()
        self.assertEqual(block_move, 3)
        self.game.make_move(self.computer_mark, 5)
        block_move = self.game.get_computer_move()
        self.assertEqual(block_move, 3)
        self.game.make_move(self.computer_mark, 4)
        win_move = self.game.get_computer_move()
        self.assertEqual(win_move, 6)

    def test_Ai_diagonals(self):
        self.game.make_move(self.user_mark, 1)
        self.game.make_move(self.computer_mark, 2)
        self.game.make_move(self.user_mark, 5)
        block_move = self.game.get_computer_move()
        self.assertEqual(block_move, 9)
        self.game.make_move(self.computer_mark, 9)
        self.game.make_move(self.user_mark, 3)
        block_move = self.game.get_computer_move()
        self.assertEqual(block_move, 7)

if __name__ == '__main__':
    unittest.main()
