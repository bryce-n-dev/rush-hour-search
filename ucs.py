from queue import PriorityQueue
from node import Node
from path_length import path_length


def uniform_cost_search(root_node: Node, length:path_length, board_num:int) -> Node:
    file_name="ucs-search-" + str(board_num) + ".txt"
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
        heuristics = str(gn) + " " + str(gn) + " 0 "
        board_state = node.state.get_board_string()
        node_searched = heuristics + board_state
        f.write(node_searched + '\n')

        if node.state.is_solved():
            f.close()
            return node
        else:
            children = node.get_children()
            children.sort(key=lambda x: x.cost, reverse=True)
            for child in children:
                board_state = child.state.get_board_string()
                if board_state not in closed_list and board_state not in open_board_states:
                    open_list.put(child)
                    open_board_states.add(board_state)
    
    f.close()
    return None
    
   
