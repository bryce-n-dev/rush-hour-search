import utils
from node import Node
from timeit import default_timer as timer
import time
from path_length import path_length
from ucs import uniform_cost_search
from a_star import a_star_h1
from a_star import a_star_h2
from a_star import a_star_h3
from a_star import a_star_h4
from gbfs import gbfs_h1
from gbfs import gbfs_h2
from gbfs import gbfs_h3
from gbfs import gbfs_h4

if __name__ == "__main__":
    # We should have everything we need to start writing the algorithms.
    root_nodes = utils.init_boards("sample-input.txt") # List of initial games (represented as root nodes)

    board = 1
    # Get the root node of our first game
    for root_node in root_nodes:
        file_name="astar-h2-sol-" + str(board) + ".txt"
        f = open(file_name, "a")

        #writing initial board info to file
        f.write("Initial board: " + '\n')
        root_node.state.write_board_to_file(file_name)
        f.write('\n')
        fuel =  root_node.state.get_fuel_string()
        f.write("Initial fuel: " + fuel)
        f.write('\n')

        length = path_length()
        start = time.time()
        
        #final_node = uniform_cost_search(root_node, length, board)

        #final_node = a_star_h1(root_node, length, board)
        final_node = a_star_h2(root_node, length, board)
        #final_node = a_star_h3(root_node, length, board)
        #final_node = a_star_h4(root_node, length, board)

        #final_node = gbfs_h1(root_node, length, board)
        #final_node = gbfs_h2(root_node, length, board)
        #final_node = gbfs_h3(root_node, length, board)
        #final_node = gbfs_h4(root_node, length, board)

        end = time.time()
        
        timer = end-start
        f.write("Runtime: " + str('%.3f' % timer) + " seconds" + '\n')
        if final_node is not None:
            f.write("Search path length:" + str(length.get_length())+'\n')

            solution_path =[]
            board_path = []

            def print_node(node: Node):
                if node is not None:
                    print_node(node.parent)
                    if node.move is not None:
                        print(node.move)
                        solution_path.append(node.move)
                        car = node.move[0]
                        move = node.move + "    " +str(node.state.get_fuel(car)) +" " + node.state.get_board_string()
                        board_path.append(move)
                        

            print_node(final_node)
            #print(final_node.cost)

            f.write("Solution path: ")
            for moves in solution_path:
                f.write(moves)
                f.write("; ")

            f.write('\n'+'\n')
            for moves in board_path:
                f.write(moves)
                f.write('\n')

            f.write('\n'+'\n')
            f.write("Final fuel: " + final_node.state.get_fuel_string() + '\n')   
            cost = final_node.cost
            f.write("Cost: " + str(cost) + '\n')         
            f.write("Final board: " + '\n')
            final_node.state.write_board_to_file(file_name)
        else:
            f.write("Sorry, could not solve the puzzle as specified." + '\n' + "Error: no solution found")

        board +=1
        f.close()




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
