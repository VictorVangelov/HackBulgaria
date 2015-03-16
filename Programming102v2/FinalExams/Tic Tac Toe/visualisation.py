class Visualisation():

    menu = ["start\nexit"]
    instructions= """ The object of Tic Tac Toe is to get three
    in a row. You play on a three by three game board. The first
    player is known as X and the second is O. Players alternate
    placing Xs and Os on the game board until either oppent has
    three in a row or all nine squares are filled. For example ,
    every spot is mark with his unique in number"""

    def print_board(board):
        separator = ('-----------')
        print(separator)
        for i in range(0, 3):
            row = " {} | {} | {} ".format(board[7-i*3], board[8-i*3], board[9-i*3])
            print("{}\n{}".format(row, separator))

    def print_menu():
        print(Visualisation.menu)
        print(Visualisation.instructions)
        board = list(["0", '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        Visualisation.print_board(board)

if __name__ == '__main__':
    board = list(["0", '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    Visualisation.print_board(board)

