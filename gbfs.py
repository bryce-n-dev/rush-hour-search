from queue import PriorityQueue
from path_length import path_length
from node import Node


def gbfs_h1(root_node: Node,  length:path_length, board_num:int) -> Node:
    file_name="gbfs-h1-search-" + str(board_num) + ".txt"
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
        hn = node.state.h_1_n_blocking_vehicles()
        heuristics = str(hn) + " 0 " + str(hn) + " "
        board_state = node.state.get_board_string()
        node_searched = heuristics + board_state
        f.write(node_searched + '\n')


        if node.state.is_solved():
            f.close()
            return node
        else:
            children = node.get_children()
            children.sort(key=lambda x: x.state.h_1_n_blocking_vehicles(), reverse=True)
            for child in children:
                board_state = child.state.get_board_string()
                if board_state not in closed_list and board_state not in open_board_states:
                    open_list.put(child)
                    open_board_states.add(board_state)
    f.close()
    return None

def gbfs_h2(root_node: Node, length:path_length, board_num:int) -> Node:
    file_name="gbfs-h2-search-" + str(board_num) + ".txt"
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
        hn = node.state.h_2_n_blocked_positions()
        heuristics = str(hn) + " 0 " + str(hn) + " "
        board_state = node.state.get_board_string()
        node_searched = heuristics + board_state
        f.write(node_searched + '\n')

        if node.state.is_solved():
            f.close()
            return node
        else:
            children = node.get_children()
            children.sort(key=lambda x: x.state.h_2_n_blocked_positions(), reverse=True)
            for child in children:
                board_state = child.state.get_board_string()
                if board_state not in closed_list and board_state not in open_board_states:
                    open_list.put(child)
                    open_board_states.add(board_state)
    f.close()
    return None


def gbfs_h3(root_node: Node, length:path_length, board_num:int) -> Node:
    file_name="gbfs-h3-search-" + str(board_num) + ".txt"
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
        hn = hn = node.state.h_3_n_blocking_vehicles()
        heuristics = str(hn) + " 0 " + str(hn) + " "
        board_state = node.state.get_board_string()
        node_searched = heuristics + board_state
        f.write(node_searched + '\n')

        if node.state.is_solved():
            f.close()
            return node
        else:
            children = node.get_children()
            children.sort(key=lambda x: x.state.h_3_n_blocking_vehicles(), reverse=True)
            for child in children:
                board_state = child.state.get_board_string()
                if board_state not in closed_list and board_state not in open_board_states:
                    open_list.put(child)
                    open_board_states.add(board_state)
    f.close()
    return None

# this heuristic algorithm checks the number of possible moves for each child node and based on that, it will sort them.
def gbfs_h4(root_node: Node, length:path_length, board_num:int) -> Node:
    file_name="gbfs-h4-search-" + str(board_num) + ".txt"
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
        #hn = node.cost #TO MODIFY
        hn = len(node.get_children())
        heuristics = str(hn) + " 0 " + str(hn) + " "
        board_state = node.state.get_board_string()
        node_searched = heuristics + board_state
        f.write(node_searched + '\n')

        if node.state.is_solved():
            f.close()
            return node
        else:
            children = node.get_children()
            children.sort(key=lambda x: len(x.get_children()), reverse=True)
            for child in children:
                board_state = child.state.get_board_string()
                if board_state not in closed_list and board_state not in open_board_states:
                    open_list.put(child)
                    open_board_states.add(board_state)
    f.close()
    return None