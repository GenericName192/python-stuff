# function to see if someone has won at a game of tic tac toe
def is_solved(board):

    checker = False
    center = board[1][1]

    # if there is a win diagonally, could'nt think of a good way of doing this
    if center: # checks if its a truthy (1 or 2) or a falsey (0)
        if center == board[0][0] and center == board[2][2]:
            return center
        if center == board[0][2] and center == board[2][0]:
            return center

    for x in board:
        if 0 in x:
            checker = True
        if x[0]: # checks if its a truthy (1 or 2) or a falsey (0)
            if x[0] == x[1] and x[0] == x[2]: # checks for any winning rows
                return x[0]

    for y in board[0]:
        if board[0][y]: # checks if its a truthy (1 or 2) or a falsey (0)
            if board[0][y] == board[1][y] and board[0][y] == board[2][y]: # winning columns 
                return board[0][y]

    if checker: # if true a 0 was found and the game is unfinished
        return -1

    return 0 # no winner found, must be a draw

# code wars description 

# If we were to set up a Tic-Tac-Toe game, we would want to know whether the 
# board's current state is solved, wouldn't we? Our goal is to create a function 
# that will check that for us!

# Assume that the board comes in the form of a 3x3 array, where the value is 0 
# if a spot is empty, 1 if it is an "X", or 2 if it is an "O"