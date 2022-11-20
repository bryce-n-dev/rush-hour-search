import numpy as np
import re
from queue import PriorityQueue # https://www.educative.io/answers/what-is-the-python-priority-queue
from typing import List

q = PriorityQueue()


class RushHour():
    def __init__(self) -> None:
        pass
        # attributes of board

    def move_right(self, vehicle):
        pass

    def move_left(self, vehicle):
        pass

    def move_down(self, vehicle):
        pass

    def move_up(self, vehicle):
        pass

    def is_solved(self):
        pass


def parse_board(input: str) -> List[List[str]]:
    input = input[:36]
    board = np.array(list(input))
    return board.reshape(6, 6).tolist()

def print_board(board: List[List[str]]) -> None:
    for row in board:
        for col in row:
            print(col, end=' ')
        print() # New line

def parse_fuel(input: str) -> dict:
    # Each letter becomes dictionary key
    fuel_dict = {}
    cars_string = re.sub(r'[^A-Z]', '', input) # Remove non letters
    car_set = set(list(cars_string)) # Remove duplicates
    for car in car_set:
        fuel_dict[car] = 100 # Cars have 100 fuel by default
    
    special_cars = input.split()[1:] # Parse for extra fuel
    for car in special_cars:
        fuel_dict[car[0]] = int(car[1:]) # Overwrite default with specified value
    return fuel_dict

def print_fuel(fuel: dict) -> None:
    print('Car fuel available: ', end=' ')
    for car in fuel:
        print(f'{car}: {fuel[car]}', end='  ')

def init_board(file_name: str):
    with open(file_name, 'r') as filehandle:
        for line in filehandle:
            line = line.rstrip()
            if line: # Ignore empty lines
                if line[0] != "#": # Check for comments and ignore
                    board = parse_board(line)
                    fuel_dict = parse_fuel(line)
                    print_board(board)
                    print_fuel(fuel_dict)
                    print()


if __name__ == "__main__":
    init_board("sample-input.txt")

# Print status

# Move by increasing/decreasing index in one dimension
# Subtract fuel by one, only move if enough fuel

# Movement must be for all letters

# Check for goal