from queue import PriorityQueue

from node import Node


def uniform_cost_search(root_node: Node) -> Node:
    open_list: PriorityQueue[Node] = PriorityQueue()
    closed_list = set()
    open_board_states = set()
    open_list.put(root_node)
    open_board_states.add(root_node.state.get_board_string())

    while not open_list.empty():
        node = open_list.get()
        open_board_states.remove(node.state.get_board_string())

        node.state.print_status()
        closed_list.add(node.state.get_board_string())
        if node.state.is_solved():
            return node
        else:
            children = node.get_children()
            children.sort(key=lambda x: x.cost, reverse=True)
            for child in children:
                board_state = child.state.get_board_string()
                if board_state not in closed_list and board_state not in open_board_states:
                    open_list.put(child)
                    open_board_states.add(board_state)
