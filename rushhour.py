from typing import List
import numpy as np


class RushHour():
    def __init__(self, board: List[List[str]], fuel: dict) -> None:
        self.board = board
        self.fuel = fuel

    def search(self) -> dict:
        possible_moves = {}

        # Scan board vertically, then horizontally - break every line 
        for i in range(6):
            empty_counter = 0
            for j in range(6):
                if self.board[i][j] == '.':
                    empty_counter += 1
                
        # Keep track of any vehicle (AKA any letter that repeats more than once) --> Vehicle must have dots on either side to move
        # Keep track in dictionary where key is vehicle and array of int are possible moves(?)
        pass

    def move_vertical(self, vehicle: str, dist: int) -> None:
        pass

    def move_horizontal(self, vehicle: str, dist: int) -> None:
        pass

    def exit_vehicle(self) -> None:
        pass

    def has_fuel(self, vehicle: str) -> bool:
        return self.fuel[vehicle] > 0

    def is_solved(self) -> bool:
        return (self.board[2][4] == 'A' and self.board[2][5] == 'A')

    def print_board(self) -> None:
        for row in self.board:
            for col in row:
                print(col, end=' ')
            print() # New line

    def print_board_1d(self) -> None:
        flat_board = np.array(self.board).flatten()
        board_string = ''.join(str(x) for x in flat_board) 
        print(board_string)

    def print_fuel(self) -> None:
        print('Car fuel available: ', end=' ')
        for car in self.fuel:
            print(f'{car}: {self.fuel[car]}', end='  ')