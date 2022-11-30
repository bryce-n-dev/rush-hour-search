from __future__ import annotations
from typing import List

from state import BoardState


class Node():
    def __init__(self, parent: Node, state: BoardState, move: str, cost: int) -> None:
        self.parent = parent
        self.state = state
        self.move = move
        self.cost = cost

    def __eq__(self, other):
        return (self.cost == other.cost)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return (self.cost < other.cost)

    def __gt__(self, other):
        return (self.cost > other.cost)

    def __le__(self, other):
        return (self.cost < other.cost) or (self.cost == other.cost)

    def __ge__(self, other):
        return (self.cost > other.cost) or (self.cost == other.cost)

    def get_children(self) -> List[Node]:
        children = []
        cars = self.state.get_game_cars()
        for car in cars:
            for i in range(1, 7):
                if self.state.move_up_available(car, i):
                    child_state = self.state.move_up(car, i)
                    if child_state is not None:
                        child_move = f'{car} up {str(i)}'
                        children.append(Node(parent=self, state=child_state, move=child_move, cost=self.cost + 1))
                if self.state.move_down_available(car, i):
                    child_state = self.state.move_down(car, i)
                    if child_state is not None:
                        child_move = f'{car} down {str(i)}'
                        children.append(Node(parent=self, state=child_state, move=child_move, cost=self.cost + 1))
                if self.state.move_left_available(car, i):
                    child_state = self.state.move_left(car, i)
                    if child_state is not None:
                        child_move = f'{car} left {str(i)}'
                        children.append(Node(parent=self, state=child_state, move=child_move, cost=self.cost + 1))
                if self.state.move_right_available(car, i):
                    child_state = self.state.move_right(car, i)
                    if child_state is not None:
                        child_move = f'{car} right {str(i)}'
                        children.append(Node(parent=self, state=child_state, move=child_move, cost=self.cost + 1))
        children = [i for i in children if i is not None] # Remove none values
        return children 
    