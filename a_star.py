from queue import PriorityQueue
from path_length import path_length
from node import Node


def a_star_h1(root_node: Node, length:path_length, board_num:int) -> Node:
    file_name="astar-h1-search-" + str(board_num) + ".txt"
    f = open(file_name, "a")

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
        length.add_length()
        gn = node.cost
        hn = node.state.h_1_n_blocking_vehicles()
        total_cost = gn+hn
        heuristics = str(total_cost) + " " + str(gn)  + " "+ str(hn) + " "
        board_state = node.state.get_board_string()
        node_searched = heuristics + board_state
        f.write(node_searched + '\n')

        if node.state.is_solved():
            f.close()
            return node
        else:
            children = node.get_children()
            children.sort(key=lambda x: x.cost + x.state.h_1_n_blocking_vehicles(), reverse=True)
            for child in children:
                board_state = child.state.get_board_string()
                if board_state not in closed_list and board_state not in open_board_states:
                    open_list.put(child)
                    open_board_states.add(board_state)
    f.close()
    return None

def a_star_h2(root_node: Node, length:path_length, board_num:int) -> Node:
    file_name="astar-h2-search-" + str(board_num) + ".txt"
    f = open(file_name, "a")

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
        length.add_length()
        gn = node.cost
        hn = node.state.h_2_n_blocked_positions()
        total_cost = gn+hn
        heuristics = str(total_cost) + " " + str(gn)  + " "+ str(hn) + " "
        board_state = node.state.get_board_string()
        node_searched = heuristics + board_state
        f.write(node_searched + '\n')

        if node.state.is_solved():
            f.close()
            return node
        else:
            children = node.get_children()
            children.sort(key=lambda x: x.cost + x.state.h_2_n_blocked_positions(), reverse=True)
            for child in children:
                board_state = child.state.get_board_string()
                if board_state not in closed_list and board_state not in open_board_states:
                    open_list.put(child)
                    open_board_states.add(board_state)
    f.close()
    return None

def a_star_h3(root_node: Node, length:path_length, board_num:int) -> Node:
    file_name="astar-h3-search-" + str(board_num) + ".txt"
    f = open(file_name, "a")
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
        length.add_length()
        gn = node.cost
        hn = node.state.h_3_n_blocking_vehicles()
        total_cost = gn+hn
        heuristics = str(total_cost) + " " + str(gn)  + " "+ str(hn) + " "
        board_state = node.state.get_board_string()
        node_searched = heuristics + board_state
        f.write(node_searched + '\n')

        if node.state.is_solved():
            f.close()
            return node
        else:
            children = node.get_children()
            children.sort(key=lambda x: x.cost + x.state.h_3_n_blocking_vehicles(), reverse=True)
            for child in children:
                board_state = child.state.get_board_string()
                if board_state not in closed_list and board_state not in open_board_states:
                    open_list.put(child)
                    open_board_states.add(board_state)
    f.close()
    return None

# this heuristic algorithm checks the number of possible moves for each child node and based on that plus the actual cost, it will sort them.
def a_star_h4(root_node: Node, length:path_length, board_num:int) -> Node:
    file_name="astar-h4-search-" + str(board_num) + ".txt"
    f = open(file_name, "a")

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
        length.add_length()
        gn = node.cost
        #hn = node.state.h_3_n_blocking_vehicles() #TO CHANGE HERE
        hn = len(node.get_children())
        total_cost = gn+hn
        heuristics = str(total_cost) + " " + str(gn)  + " "+ str(hn) + " "
        board_state = node.state.get_board_string()
        node_searched = heuristics + board_state
        f.write(node_searched + '\n')

        if node.state.is_solved():
            f.close()
            return node
        else:
            children = node.get_children()
            children.sort(key=lambda x: x.cost + len(x.get_children()), reverse=True)
            for child in children:
                board_state = child.state.get_board_string()
                if board_state not in closed_list and board_state not in open_board_states:
                    open_list.put(child)
                    open_board_states.add(board_state)
    f.close()
    return None