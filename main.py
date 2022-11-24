import utils


if __name__ == "__main__":
    initial_states = utils.init_boards("sample-input.txt") #list of state objects
    game = initial_states[0] #a state object 
    game.print_fuel()
    
    game.print_board()
    print(game.board[0][2])
    print(game.has_fuel('M'))
    print(game.is_horizontal('G'))