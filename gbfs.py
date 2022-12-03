from queue import PriorityQueue

from node import Node


def gbfs_h1(root_node: Node) -> Node:
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
            children.sort(key=lambda x: x.state.h_1_n_blocking_vehicles(), reverse=True)
            for child in children:
                board_state = child.state.get_board_string()
                if board_state not in closed_list and board_state not in open_board_states:
                    open_list.put(child)
                    open_board_states.add(board_state)

def gbfs_h2(root_node: Node) -> Node:
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
            children.sort(key=lambda x: x.state.h_2_n_blocked_positions(), reverse=True)
            for child in children:
                board_state = child.state.get_board_string()
                if board_state not in closed_list and board_state not in open_board_states:
                    open_list.put(child)
                    open_board_states.add(board_state)

def gbfs_h3(root_node: Node) -> Node:
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
            children.sort(key=lambda x: x.state.h_3_n_blocking_vehicles(), reverse=True)
            for child in children:
                board_state = child.state.get_board_string()
                if board_state not in closed_list and board_state not in open_board_states:
                    open_list.put(child)
                    open_board_states.add(board_state)

# this heuristic algorithm checks the number of possible moves for each child node and based on that, it will sort them.
def gbfs_h4(root_node: Node) -> Node:
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
            children.sort(key=lambda x: len(x.get_children()), reverse=True)
            for child in children:
                board_state = child.state.get_board_string()
                if board_state not in closed_list and board_state not in open_board_states:
                    open_list.put(child)
                    open_board_states.add(board_state)