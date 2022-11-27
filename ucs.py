import numpy as np
import re
from typing import List
from state import BoardState
from node import Node

class UniformCostSearch():
    def __init__(self, board:BoardState)->None:
        self.board = board
        self.open_list = [] #priority queue
        self.closed_list = [] #visited list
        self.current_node = self.define_current_node(board, None, 1)
        

    def define_current_node(self, board:BoardState, parent:Node, cost:int)->Node:
        current_node = Node(board, parent, cost)
        return current_node


    def start_search(self)->None:
        while not self.current_node.get_board_state().is_solved():
            self.closed_list.append(self.current_node)
            pass 

    def generate_child(self)->Node:
        pass
