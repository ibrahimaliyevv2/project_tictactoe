import numpy as np
import os


class Board:
    char = [" ", "X", "O"]

    def __init__(self):
        self.grid = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def print(self):
        line = ["A", "B", "C"]
        print("  " + 13 * "-")
        for i in range(3):
            print(line[i] + " | " + self.char[self.grid[i][0]] + " | "
                  + self.char[self.grid[i][1]] + " | " + self.char[self.grid[i][2]] + " |")
            print("  " + 13 * "-")
        print(4 * " " + "1" + 3 * " " + "2" + 3 * " " + "3")

    def get_value(self, coord_x, coord_y):
        return self.grid[coord_x][coord_y]

    def set_value(self, coord_x, coord_y, value):
        self.grid[coord_x][coord_y] = value

    def check_victory(self):
        # check line and column alignment
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != 0 \
                    or self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != 0:
                return True
        # check diagonal alignments
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != 0 \
                or self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != 0:
            return True
        return False

    def reinit(self):
        self.grid.fill(0)


class TicTacToe:
    moves = {"A1": (0, 0), "A2": (0, 1), "A3": (0, 2),
             "B1": (1, 0), "B2": (1, 1), "B3": (1, 2),
             "C1": (2, 0), "C2": (2, 1), "C3": (2, 2)}
    players = ["O", "X"]

    def __init__(self):
        self.turn = 1
        self.board = Board()

    def launch_game(self):
        while True:
            print(20 * "*")
            print("Turn", self.turn, ": Player", self.players[self.turn % 2])
            print(20 * "*")
            self.board.print()

            move = input("Enter your move:").upper()
            if move not in self.moves.keys():
                print(move, "is not an authorized move !")
                continue
            coord = self.moves[move]
            if self.board.get_value(coord[0], coord[1]) == 0:
                self.board.set_value(coord[0], coord[1], 2 - (self.turn % 2))
            else:
                print("Square " + move + " is not free, please retry !")
                continue
            if self.turn >= 5 and self.board.check_victory():
                os.system('clear')
                print("Player", self.players[self.turn % 2], "won !")
                self.board.print()
                break
            elif self.turn >= 9:
                os.system('clear')
                print("The game is draw !")
                self.board.print()
                break
            self.turn += 1
            os.system('clear')
        answer = input("Another game ? (Y/N)").upper()
        if answer == "Y":
            os.system('clear')
            game.reinit()


    def reinit(self):
        self.turn = 1
        self.board.reinit()
        self.launch_game()


game = TicTacToe()
game.launch_game()
