# This is where your main() function will go.
# The main() function will tie all other functions together.
# You may add other functions here as needed.

from userInput import *
from computerInput import *
from computerRandom import *
from computerMinimax import *
from Game import *
totalFC = 0

def main():
    global totalFC
    seriesResults = [0, 0, 0] # ties, count of player1 wins, player2 wins

    print("Welcome To Tic Tac Toe")
    player1Name = input("Player 1, input your name, or c (RULES AI), r (RANDOM AI), m (MINIMAX AI):  ")
    player2Name = input("Player 2, input your name, or c (RULES AI), r (RANDOM AI), m (MINIMAX AI):  ")
    if player1Name in ['c', 'r', 'm'] and player2Name in ['c', 'r', 'm']:
        repeatGames = int(input("How many games would you like the AI to play:  "))
        while repeatGames < 1:
            repeatGames = int(input("Please select 1 or more games.  How many games would you like the AI to play:  "))
    else:
        repeatGames = 1

    for i in range(repeatGames):
        ttt = Game()
        while ttt.winnerVar == 0:
            if not ttt.getEmpties():
                seriesResults[0] += 1
                if repeatGames < 2:
                    print("GAME OVER")
                    print("Tie Game. Nobody Wins.")
                    print(ttt.drawTheBoard())
                print("game#:", sum(seriesResults))
                print("Number of calls to the minimax algorithm for this game:", ttt.masterFC)
                print(ttt.moveHistory)
                print("winner: ", ttt.winnerVar, "\n\n")
                totalFC += ttt.masterFC
                del ttt
                break
            if repeatGames < 2:
                print("Player " + str(ttt.curPlayer) + "'s Turn")
                print("The Current Board Is:")
                print(ttt.drawTheBoard())

            if ttt.curPlayer == 1:
                if player1Name.lower() == "c":
                    computerPlayer(ttt)
                elif player1Name.lower() == "r":
                    computerRandom(ttt)
                elif player1Name.lower() == "m":
                    computerMinimax(ttt)
                else:
                    userInput(ttt)
            else:
                if player2Name.lower() == "c":
                    computerPlayer(ttt)
                elif player2Name.lower() == "r":
                    computerRandom(ttt)
                elif player2Name.lower() == "m":
                    computerMinimax(ttt)
                else:
                    userInput(ttt)

            ttt.winnerVar = ttt.checkForWinner()
            # print winnerVar
            if ttt.winnerVar != 0:
                seriesResults[ttt.curPlayer] += 1
                if (ttt.curPlayer == 1 and player1Name.lower() == "r") or (ttt.curPlayer == 2 and player2Name.lower() == "r"):
                    print(ttt.moveHistory)
                if repeatGames < 2:
                    print("GAME OVER")
                    print("Player " + str(ttt.curPlayer) + " wins.")
                    print(ttt.drawTheBoard())
                print("game#:", sum(seriesResults))
                print("Number of calls to the minimax algorithm for this game:", ttt.masterFC)
                print(ttt.moveHistory)
                print("winner:", ttt.winnerVar, "\n\n")
                totalFC += ttt.masterFC
                del ttt
                break
            #toggle player
            ttt.curPlayer = ttt.curPlayer % 2 + 1
    print("Final series results:  ", seriesResults[0], "ties,  ", seriesResults[1], "Player1 wins,  ", seriesResults[2], "Player2 wins.")
    print("Total Number of calls to the minimax algorithm for all games:", totalFC)
main()
# [5, 4, 6, 0, 8, 2, 7]
