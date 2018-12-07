# PASTE YOUR USER INPUT CODE HERE.  DON'T USE THE FUNCTION NAME "MAIN" HERE.
def userInput(game):
    """
    INPUT:  the board[][] and a 1 or 2 to indicate the player's turn
    WORK:  check board to be sure there is space left, get user's choice, check user's choice,
           place user's choice, return the modified board
    OUTPUT:  the board with the players choice added, or -1 if the board is full.
    """

    if game.isBoardFull():
        return -1

    while True:
        print('Please choose a space:')
        #  print '''
        # --- --- ---
        # | 1 | 2 | 3 |
        # --- --- ---
        # | 4 | 5 | 6 |
        # --- --- ---
        # | 7 | 8 | 9 |
        # --- --- ---'''
        theInput = int(input('Input:'))-1
        if theInput not in range(0, 9):
            print("invalid choice, please try again")
            continue
        myMove = game.move(theInput)
        if myMove == -1:
            print("That space is taken, please try again")
        elif myMove == -2:
            print("invalid choice, please try again")
        else:
            return 1
