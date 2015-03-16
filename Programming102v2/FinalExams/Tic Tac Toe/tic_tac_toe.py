import random
from copy import copy
from visualisation import Visualisation


class Tic_tac_toe():

    def __init__(self):

        self.user_mark = "X"
        self.computer_mark = "O"
        self.free_spot = " "
        self.moves_left = 9
        self.available_spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.center = 5
        self.corners = [1, 3, 7, 9]
        self.edges = [2, 4, 6, 8]
        self.board = [' '] * 10
        self.winner = ""

    def is_valid_move(self, move):
        if move < 10 and move > 0:
            if move in self.available_spots:
                return True
            else:
                return False
        else:
            return False

    def make_move(self, mark, move):
        self.board[int(move)] = mark
        self.available_spots.remove(int(move))
        self.moves_left -= 1

    def simulate_move(self, board, mark, move):
        board[move] = mark

    def take_random_place(self, move_list):
        possible_spots = []
        for item in list(move_list):
            if item in self.available_spots:
                possible_spots.append(item)
        if len(possible_spots) != 0:
            return random.choice(possible_spots)
        else:
            return None

        return random.choice(move_list)

    def its_free_spot(self, spot):
        if spot not in self.available_spots:
            return True
        else:
            return False

    def check_for_winner(self, board, mark):
        for x in range(0, 3):
            if (board[1 + x] == board[4 + x] == board[7 + x] == mark):
                return True
            elif (board[1 + x*3] == board[2 + x*3] == board[3 + x*3] == mark):
                return True
        first_diagonal = (board[1] == board[5] == board[9] == mark)
        secound_diagonal = (board[3] == board[5] == board[7] == mark)
        if first_diagonal or secound_diagonal:
            return True
        return False

    def play_again(self):
        answer = input('Do you want to play again? (yes or no)\n>')
        if answer.lower().startswith('ye'):
            self.reset_game()
            self.play()

    def reset_game(self):
        self.available_spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.board = [' '] * 10
        self.moves_left = 9

    def check_for_posible_win(self, mark):
        for spot in self.available_spots:
            board_copy = copy(self.board)
            self.simulate_move(board_copy, mark, spot)
            if self.check_for_winner(board_copy, mark):
                return (True, spot)
        return (False, None)

    def play(self):
        Visualisation.print_menu()
        while self.moves_left > 0:
            Visualisation.print_board(self.board)
            turn = self.moves_left % 2
            if turn == 1:
                self.execute_user_move()
            else:
                self.execute_computer_move()
        print('The game is a tie!')
        self.play_again()

    def execute_computer_move(self):
        mark = self.computer_mark
        move = self.get_computer_move()
        self.make_move(mark, move)
        if self.check_for_winner(self.board, mark):
            Visualisation.print_board(self.board)
            print('You lost!!!')
            self.play_again()

    def execute_user_move(self):
        mark = self.user_mark
        spot = input('Its your turn, place your X somewhere (1-9)>')
        if self.is_valid_move(int(spot)):
            self.make_move(mark, spot)
        else:
            print("wow, you can choose from : {}".format(self.available_spots))
            self.execute_user_move()
        if self.check_for_winner(self.board, mark):
            Visualisation.print_board(self.board)
            print('You won!!!')
            self.play_again()

    def get_computer_move(self):
        can_computer_win = self.check_for_posible_win(self.computer_mark)
        if can_computer_win[0] == True:
            return can_computer_win[1]
        elif can_computer_win[0] == False:
            can_user_win = self.check_for_posible_win(self.user_mark)
            if can_user_win[0] == True:
                return can_user_win[1]
            else:
                return self.take_random_spot()
        else:
            return self.take_random_spot()

    def take_random_spot(self):
        spots = [self.corners, self.center, self.edges]
        for listt in spots:
            if len(listt) == 0:
                continue
            else:
                move = self.take_random_place(listt)
            if move is not None:
                return move

    def getBoardCopy(board):
        return copy(board)

if __name__ == '__main__':
    game = Tic_tac_toe()
    game.play()
