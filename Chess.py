import pandas as pd
import numpy as np
#Creation of a visual chess board

#Chessboard  for calculations in relation to the movement of the pieces
ChessBoard = [  ['WR','--','WB','WQ','WK','WB','WN','WR'],
                [['WP',0],['WP',0],['WP',0],['WP',0],['WP',0],['WP',0],['WP',0],['WP',0]],  
                ['--','--','--','--','--','--','--','--'],
                ['--','--','--','--','--','--','--','--'],
                ['--','--','--','--','--','--','--','--'],
                ['--','WN','--','--','--','--','--','--'],
                [['BP',0],['BP',0],['BP',0],['BP',0],['BP',0],['BP',0],['BP',0],['BP',0]],
                ['BR','BN','BB','BQ','BK','BB','BN','BR']]


def PawnMovement(x,y):
    currentColumn = 0
    letters = ['A','B','C','D','E','F','G','H']
    for i in range(len(letters)):
        if x[1] == letters[i]:
            currentColumn = i+1
    print(currentColumn)
    
    def BlackPawnMovement(x,y):
        if (x[1] == y[1]): #Checks if the pawn if moving in the same column
            if int(x[2]) - int(y[2]) <= 2:#Checks if the pawn is moving two spaces or less
                if int(x[2]) - int(y[2]) == 2: #Checks if the pawn is moving two spaces
                    if ChessBoard[int(x[2])-1][currentColumn][1] == 0: #Checks if the pawn has moved before
                        if ChessBoard[(int(x[2])-1)-1][currentColumn] == '--': #Checks if there is a piece in front of the pawn
                            if ChessBoard[(int(x[2])-1)-2][currentColumn] == '--':#Checks if there is a piece two tiles in front of the pawn
                                ChessBoard[int(x[2])-1][currentColumn][1] = 1
                                ChessBoard[(int(x[2])-1)-2][currentColumn] = ChessBoard[int(x[2])-1][currentColumn] #Moves the pawn two tiles forward
                                ChessBoard[int(x[2])-1][currentColumn] = '--'
                        else:
                            print('invalid move')
                    else:
                        print('invalid move')
                if int(x[2]) - int(y[2]) == 1: #Checks if the pawn is moving one space
                    if ChessBoard[(int(x[2])-1)-1][currentColumn] == '--':
                        ChessBoard[int(x[2])-1][currentColumn][1] = 1
                        ChessBoard[(int(x[2])-1)-1][currentColumn] = ChessBoard[int(x[2])-1][currentColumn] #Moves the pawn one tiles forward
                        ChessBoard[int(x[2])-1][currentColumn] = '--'

                    else:
                        print('invalid move')
        else:
            print('invalid move')
        
    def WhitePawnMovement(x,y):
        print('White')
    
    if (ChessBoard[int(x[2])-1][currentColumn][0] == 'BP'):
        BlackPawnMovement(x,y)
    elif (ChessBoard[int(x[2])-1][currentColumn][0] == 'WP'):
        WhitePawnMovement(x,y)
    else:
        print('There is no pawn in that position')



PawnMovement('PB7','PB6')
print(pd.DataFrame(ChessBoard))
PawnMovement('PB7','PB5')
print(pd.DataFrame(ChessBoard))
PawnMovement('PC7','PC5')
print(pd.DataFrame(ChessBoard))
PawnMovement('PC5','PC3')
print(pd.DataFrame(ChessBoard))
PawnMovement('PC5','PC4')
print(pd.DataFrame(ChessBoard))
PawnMovement('PC4','PC3')
print(pd.DataFrame(ChessBoard))
PawnMovement('PC3','PC2')
print(pd.DataFrame(ChessBoard))
PawnMovement('PD7','PD6')
print(pd.DataFrame(ChessBoard))
PawnMovement('PD6','PD4')
print(pd.DataFrame(ChessBoard))


