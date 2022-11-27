from __future__ import annotations
from state import BoardState

class Node():
    def __init__(self, parent: Node, state: BoardState, cost: int) -> None:
        self.parent = parent
        self.state = state
        self.cost = cost
    