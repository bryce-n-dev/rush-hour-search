import numpy as np
import re
from typing import List

from rushhour import RushHour


def parse_board(input: str) -> List[List[str]]:
    input = input[:36]
    board = np.array(list(input))
    return board.reshape(6, 6).tolist()

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

def init_boards(file_name: str) -> List[RushHour]:
    rush_hour_games = []
    with open(file_name, 'r') as filehandle:
        for line in filehandle:
            line = line.rstrip()
            if line: # Ignore empty lines
                if line[0] != "#": # Check for comments and ignore
                    board = parse_board(line)
                    fuel_dict = parse_fuel(line)
                    rush_hour_games.append(RushHour(board, fuel_dict))
    return rush_hour_games