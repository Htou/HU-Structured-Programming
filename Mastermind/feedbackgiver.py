from Mastermind.mastermind_globals import *


def feedback():
    for i in range(4):
        if board[playingRow][i] == sCode[i]:
            feedbackBoard[playingRow].append(2)
        elif board[playingRow][i] in sCode:
            feedbackBoard[playingRow].append(1)
