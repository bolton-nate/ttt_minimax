from random import randint, seed
global fc

def minimax(newGame, rootPlayer, game):
    global fc
    fc += 1
    game.masterFC += 1

    empties = newGame.getEmpties()
    # print("fc:", fc, " empties: ", empties)

    if newGame.checkForWinner() == rootPlayer:
        # print("fc:", fc, " player win return 10")
        return -1, 100
    elif newGame.checkForWinner() == rootPlayer % 2 + 1:
        # print("fc:", fc, " other player win return -10")
        return -1, -100
    elif not empties:
        # print("fc:", fc, " empty, return 0")
        return -1, -5

    moves = []
    scores = []
    for i in range(len(empties)):
        newGame.move(empties[i])
        newGame.curPlayer = newGame.curPlayer % 2 + 1
        result = minimax(newGame, rootPlayer, game)
        moves.append(empties[i])
        scores.append(result[1])
        # print("fc:", fc, " moves array: ", moves)
        # print("fc:", fc, " scores array: ", scores)

        newGame.clearMove(empties[i])
        newGame.curPlayer = newGame.curPlayer % 2 + 1

    bestMove = None
    if newGame.curPlayer == rootPlayer:
        bestScore = -10000
        for i in range(len(moves)):
            if scores[i] > bestScore:
                bestScore = scores[i]
                # print("fc:", fc, " Max bestScore now: ", bestScore)
                bestMove = moves[i]
    else:
        bestScore = 10000
        for i in range(len(moves)):
            if scores[i] < bestScore:
                bestScore = scores[i]
                # print("fc: ", fc, "Min bestScore now: ", bestScore)
                bestMove = moves[i]
    # print("fc:", fc, " returning bestmove: ", bestMove)
    return bestMove, bestScore



def computerMinimax(game):
    global fc
    fc = 0
    newGame = game.getCopy()
    # if minimax is playing first, it spends forever and always picks top left.
    # instead, make first choice random for variability and time savings
    if len(game.getEmpties()) == 9:
        seed()
        # myMove = [0, None]
        myMove = [randint(0, 8), None]
    else:
        myMove = minimax(newGame, newGame.curPlayer, game)
    # print("My minimax move:", myMove[0]+1)
    game.move(myMove[0])
    # print(minimax(game, 0))
    # exit()
    return 1
