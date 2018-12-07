# This is where your main() function will go.
# The main() function will tie all other functions together.
# You may add other functions here as needed.

from userInput import *
from computerInput import *
from computerRandom import *
from computerMinimax import *
from computerAlphaBeta import *
from Game import *
totalFC = 0

def main():
    global totalFC
    seriesResults = [0, 0, 0] # ties, count of player1 wins, player2 wins
    player1Name = player2Name = None
    print("\n\nWelcome To Tic Tac Toe\n")
    while player1Name not in ['h', 'H', '1', '2', '3', '4']:
        print("Player 1, please select player type:\nh: HUMAN PLAYER\n1: RULES AI\n2: RANDOM AI\n3: MINIMAX AI\n4: ALPHA BETA AI\n")
        player1Name = input("Choose:")
    while player2Name not in ['h', 'H', '1', '2', '3', '4']:
        print("\nPlayer 2, please select player type:\nh: HUMAN PLAYER\n1: RULES AI\n2: RANDOM AI\n3: MINIMAX AI\n4: ALPHA BETA AI\n")
        player2Name = input("Choose:")
    if player1Name in ['1', '2', '3', '4'] and player2Name in ['1', '2', '3', '4']:
        repeatGames = int(input("\nHow many games would you like the AI to play:  "))
        while repeatGames < 1:
            repeatGames = int(input("Please select 1 or more games.  How many games would you like the AI to play:  "))
    else:
        repeatGames = 1

    for i in range(repeatGames):
        ttt = Game()
        while ttt.winnerVar == 0:
            if not ttt.getEmpties():
                seriesResults[0] += 1
                print("\nGAME OVER")
                print("Tie Game. Nobody Wins.")
                print("Number of minimax calls for game #", sum(seriesResults), ": ", ttt.masterFC, sep="")
                print("Move History:", ttt.moveHistory)
                print("Final Board:\n", ttt.drawTheBoard(), "\n", sep="")

                totalFC += ttt.masterFC
                del ttt
                break
            if repeatGames < 2:
                print("\nPlayer " + str(ttt.curPlayer) + "'s Turn")
                print("The Current Board Is:")
                print(ttt.drawTheBoard())

            if ttt.curPlayer == 1:
                if player1Name.lower() == "1":
                    computerPlayer(ttt)
                elif player1Name.lower() == "2":
                    computerRandom(ttt)
                elif player1Name.lower() == "3":
                    computerMinimax(ttt)
                elif player1Name.lower() == "4":
                    computerAlphaBeta(ttt)
                else:
                    userInput(ttt)
            else:
                if player2Name.lower() == "1":
                    computerPlayer(ttt)
                elif player2Name.lower() == "2":
                    computerRandom(ttt)
                elif player2Name.lower() == "3":
                    computerMinimax(ttt)
                elif player2Name.lower() == "4":
                    computerAlphaBeta(ttt)
                else:
                    userInput(ttt)

            ttt.winnerVar = ttt.checkForWinner()
            # print winnerVar
            if ttt.winnerVar != 0:
                seriesResults[ttt.curPlayer] += 1
                # if (ttt.curPlayer == 1 and player1Name.lower() == "r") or (ttt.curPlayer == 2 and player2Name.lower() == "r"):
                #     print(ttt.moveHistory)
                print("\nGAME OVER")
                print("Winner: Player", ttt.winnerVar)
                print("Number of minimax calls for game #", sum(seriesResults), ": ", ttt.masterFC, sep="")
                print("Move History:", ttt.moveHistory)
                print("Final Board:\n", ttt.drawTheBoard(), "\n", sep="")
                totalFC += ttt.masterFC
                del ttt
                break
            #alternate player
            ttt.curPlayer = ttt.curPlayer % 2 + 1
    if repeatGames > 1:
        print("Final series results:  ", seriesResults[0], "ties,  ", seriesResults[1], "Player1 wins,  ", seriesResults[2], "Player2 wins.")
        print("Total Number of calls to the minimax algorithm for all games:", totalFC)
main()

