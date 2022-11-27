import utils


if __name__ == "__main__":
    initial_states = utils.init_boards("sample-input.txt") #list of state objects
    
    #board 2
    # game = initial_states[1] #a state object 
    # game.print_fuel()
    # game.print_board()
    # print(game.board[0][2])
    # print(game.has_fuel('E'))
    # print("Is G horizontal: " + str(game.is_horizontal('G')))
    # print("row of vehicle F: " + str(game.vehicle_row('F')))
    # print("column of vehicle J: " + str(game.vehicle_col('J')))
    # game.move_right("F",1)
    # game.print_board()
    # print()

    #board 4
    # game2 = initial_states[3]
    # game2.print_board()
    # print()
    # game2.move_right("B", 2)
    # game2.print_board()
    # print()
    # game2.move_left("B", 2)
    # game2.print_board()
    # print()
    # game2.move_left("G", 1)
    # game2.print_board()
    # print()

    #board 1
    game3 = initial_states[0]
    game3.print_board()
    print()
    game3.move_up("G", 2)
    game3.print_board()
    print()
    game3.move_down("M", 2)
    game3.print_board()
    print()