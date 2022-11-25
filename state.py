from typing import List
import numpy as np


class BoardState():
    def __init__(self, board: List[List[str]], fuel: dict) -> None:
        self.board = board
        self.fuel = fuel

    def get_children(self) -> dict:
        # possible_moves = {}

        # Scan board vertically, then horizontally - break every line 
        # for i in range(6):
        #     empty_counter = 0
        #     for j in range(6):
        #         if self.board[i][j] == '.':
        #             empty_counter += 1
                
        # Keep track of any vehicle (AKA any letter that repeats more than once) --> Vehicle must have dots on either side to move
        # Keep track in dictionary where key is vehicle and array of int are possible moves(?)
        pass

    # def move_vertical(self, vehicle: str, dist: int) -> None:
    #     pass

    # def move_horizontal(self, vehicle: str, dist: int) -> None:
    #     pass
    #     # Let end vehicle exit if possible?

    # def exit_vehicle(self) -> None:
    #     pass

    


    def has_fuel(self, vehicle: str) -> bool:
        return self.fuel[vehicle] > 0

    def is_solved(self) -> bool:
        return (self.board[2][4] == 'A' and self.board[2][5] == 'A')

    #state of board (2D)
    def print_board(self) -> None:
        for row in self.board:
            for col in row:
                print(col, end=' ')
            print() # New line

    def print_board_1d(self) -> None:
        flat_board = np.array(self.board).flatten()
        board_string = ''.join(str(x) for x in flat_board) 
        print(board_string)

    #fuel of all cars
    def print_fuel(self) -> None:
        print('Car fuel available: ', end=' ')
        for car in self.fuel:
            print(f'{car}: {self.fuel[car]}', end='  ')
        print()

    #check if vehicle is horizontal or not
    def is_horizontal(self, vehicle:str) -> bool:
        temp1 = ""
        temp2 = ""
        for row in self.board:
            for col in range(0, 5):
                temp1 = row[col]
                temp2 = row[col+1]
                if(temp1 == temp2 and temp1 == vehicle):
                    return True
        return False

    #if vehicle is horizontal, returns which row the vehicle is in
    def vehicle_row(self, vehicle:str) -> int:
        if(self.is_horizontal(vehicle)):
            row_value = 0
            for row in self.board:
                for col in row:
                    if(vehicle == col):
                        return row_value 
                row_value += 1
    
    #if vehicle is verticle, returns which col the vehicle is in
    def vehicle_col(self, vehicle:str)->int:
        if not(self.is_horizontal(vehicle)):
            col_value = 0
            for i in range(0, 6):
                column_list = np.array([row[i] for row in self.board])
                if(vehicle in column_list):
                    return col_value
                col_value += 1

    def move_right(self, vehicle:str, dist: int) -> bool: #TODO- should it return true after vehicle has been moved? 
        if(self.is_horizontal(vehicle)):
            vehicle_row = self.vehicle_row(vehicle)
            right_most_index_pos = 6 - self.board[vehicle_row][::-1].index(vehicle) -1 #gets right most index of vehicle
            spacesFree = False  #spaces to be moved to 
            nextSpaces = []
            for spaces in range(0, dist):
                nextSpaces.append(self.board[vehicle_row][right_most_index_pos+1+spaces])

            #check if all the values in array is a .
            if all(x == '.' for x in nextSpaces):
                spacesFree = True

            if(spacesFree): #performs moving vehicle to the right
                left_most_index_pos = self.board[vehicle_row].index(vehicle)
                for x in range(0, dist):
                    self.board[vehicle_row][left_most_index_pos+x] = '.' 
                    self.board[vehicle_row][right_most_index_pos+x+1] = vehicle
                
            elif not (spacesFree):
                #perform moving as much as possible?
                pass
    
    def move_left(self, vehicle:str, dist: int) -> bool: #TODO - return bool?
        if(self.is_horizontal(vehicle)):
            vehicle_row = self.vehicle_row(vehicle)
            right_most_index_pos = 6 - self.board[vehicle_row][::-1].index(vehicle) -1 #gets right most index of vehicle
            left_most_index_pos = self.board[vehicle_row].index(vehicle) 

            spacesFree = False  #spaces to be moved to 
            nextSpaces = []

            for spaces in range(0, dist):
                nextSpaces.append(self.board[vehicle_row][left_most_index_pos-1-spaces])
            
            #check if all the values in array is a .
            if all(x == '.' for x in nextSpaces):
                spacesFree = True
            
            if(spacesFree):
                for x in range(0, dist):
                    self.board[vehicle_row][right_most_index_pos-x] = '.' 
                    self.board[vehicle_row][left_most_index_pos-x-1] = vehicle
            elif not (spacesFree):
                pass
    
    def move_up(self, vehicle:str, dist: int) -> bool: #TODO - return bool?
        if not(self.is_horizontal(vehicle)):
            vehicle_col = self.vehicle_col(vehicle)
            tempArray = np.array(self.board)[:, vehicle_col].tolist()
            top_most_index_pos = tempArray.index(vehicle) #represents the row that the top letter is in
            bottom_most_index_pos = 6- tempArray[::-1].index(vehicle) -1 
            
            spacesFree = False  #spaces to be moved to 
            nextSpaces = []

            for spaces in range(0, dist):
                nextSpaces.append(tempArray[top_most_index_pos-1-spaces])
            
            #check if all the values in array is a .
            if all(x == '.' for x in nextSpaces):
                spacesFree = True

            if(spacesFree):
                for x in range(0, dist):
                    self.board[top_most_index_pos-1-x][vehicle_col] = vehicle
                    self.board[bottom_most_index_pos-x][vehicle_col] = '.'
                pass
            elif not(spacesFree):
                pass
    
    def move_down(self, vehicle:str, dist: int) -> bool: #TODO - return bool?
        if not(self.is_horizontal(vehicle)):
            vehicle_col = self.vehicle_col(vehicle)
            tempArray = np.array(self.board)[:, vehicle_col].tolist()
            top_most_index_pos = tempArray.index(vehicle) #represents the row that the top letter is in
            bottom_most_index_pos = 6- tempArray[::-1].index(vehicle) -1 

            spacesFree = False  #spaces to be moved to 
            nextSpaces = []

            for spaces in range(0, dist):
                nextSpaces.append(tempArray[bottom_most_index_pos+1+spaces])
            
            #check if all the values in array is a .
            if all(x == '.' for x in nextSpaces):
                spacesFree = True

            if(spacesFree):
                for x in range(0, dist):
                    self.board[top_most_index_pos+x][vehicle_col] = '.'
                    self.board[bottom_most_index_pos+x+1][vehicle_col] = vehicle
                pass
            elif not(spacesFree):
                pass