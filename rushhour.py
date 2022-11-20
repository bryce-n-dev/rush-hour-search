from typing import List
import numpy as np


class RushHour():
    def __init__(self, board: List[List[str]], fuel: dict) -> None:
        self.board = board
        self.fuel = fuel

    def move_right(self, vehicle: str, dist: int):
        pass

    def move_left(self, vehicle: str, dist: int):
        pass

    def move_down(self, vehicle: str, dist: int):
        pass

    def move_up(self, vehicle: str, dist: int):
        pass

    def is_solved(self):
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