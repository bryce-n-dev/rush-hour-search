import utils
from node import Node
from ucs import uniform_cost_search


if __name__ == "__main__":
    # We should have everything we need to start writing the algorithms.
    root_nodes = utils.init_boards("sample-input.txt") # List of initial games (represented as root nodes)

    # Get the root node of our first game
    for root_node in root_nodes:
        final_node = uniform_cost_search(root_node)

        def print_node(node: Node):
            if node is not None:
                print_node(node.parent)
                if node.move is not None:
                    print(node.move)

        print_node(final_node)

    # # We can print the board
    # print("-----INITIAL BOARD STATE------")
    # root_node.state.print_board()

    # # We can get any Node's children by calling get_children()

    # # NOTE: For each child, the cost is incremented by 1.
    # # This will be useful for UCS, but I believe we can ignore it for other algorithms
    # children = root_node.get_children()

    # # children is a list of Node objects.
    # print("------CHILDREN------")
    # for child in children:
    #     # Just as before, we can print the board state
    #     print("-----CHILD------")
    #     child.state.print_board() 

    #     # We can print the move that was used to get to this state.
    #     # This will be used when we need to print out the moves of the solution
    #     print(f'Previous move: {child.move}') 

    #     # We can also get the board state in the form of a string.
    #     # Why is this important?
    #     # We need to be able to store board states in a way that is easily searchable.
    #     # Specifically, when we need to add states to the closed list.
    #     # If any child's board state is already in the closet list, we do not need to explore it any further.
    #     board_string = child.state.get_board_string()
    #     print(f'Board string: {board_string}')

    #     # Another important part: we need to see if the board is in the winning state!
    #     # This can be done as follows.
    #     is_win = child.state.is_solved()
    #     print(f'Did I win? {is_win}')

    #     # Here's the fun part. We will need to use recursion here!
    #     # I'm lazy so I will just call the function on each child to generate *its* children (the children of the children).
    #     children_children = child.get_children()
    #     print("---CHILDREN CHILDREN----")

    #     # Same functions work! It's nodes all the way down.
    #     for child in children_children:
    #         child.state.print_board()
    #         print(f'Previous move: {child.move}') 
    #         board_string = child.state.get_board_string()
    #         print(f'Board string: {board_string}')
    #         is_win = child.state.is_solved()
    #         print(f'Did I win? {is_win}')
    #         children_children_children = child.get_children()

    #         # Add recursion here!
    #         for child in children_children_children:
    #             child.state.print_board()
    #             print(f'Previous move: {child.move}') 
    #             board_string = child.state.get_board_string()
    #             print(f'Board string: {board_string}')
    #             is_win = child.state.is_solved()
    #             print(f'Did I win? {is_win}') # One of them actually finds the correct solution!!!
    #             children_children_children = child.get_children()
